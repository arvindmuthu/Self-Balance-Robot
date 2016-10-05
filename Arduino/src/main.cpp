/**
*************************************************
* @Project: Self Balance
* @Platform: Arduino Nano ATmega328
* @Description: Main thread
* @Owner: Guilherme Chinellato
* @Email: guilhermechinellato@gmail.com
*************************************************
*/

#include "Arduino.h"
#include <string.h>
#include <Wire.h>
#include "IMU/GY80.h"
#include "Motion/Motor/motor.h"
#include "Motion/Encoder/encoder.h"
#include "Motion/PID/PID.h"
#include "main.h"

Configuration configuration;
UserControl userControl = {0, 0};

// PID variables
float anglePIDSetpoint, anglePIDInput, anglePIDOutput;
float speedPIDInput, speedPIDOutput, speedPIDSetpoint;

float lastDistance1 = 0, lastDistance2 = 0;

// start and stop flag
boolean started = false;

//PID objects
PID speedPID;
PID anglePID;
PIDTuning activePIDTuning = CONSERVATIVE;

//Motors objects
Motor motor1(PWM1_PIN,CW1_PIN,CCW1_PIN,CS1_PIN);
Motor motor2(PWM2_PIN,CW2_PIN,CCW2_PIN,CS2_PIN);

//Encoder objects
Encoder encoder1(ENCODERA1_PIN,ENCODERB1_PIN);
Encoder encoder2(ENCODERA2_PIN,ENCODERB2_PIN);

/* interrupt functions for counting revolutions in the encoders */
/*when the callback function is called due an interrup event on pinEncoder1 and pinEncoder2 is true, then is clockwise, if not it is counter-clockwise*/
void encoderISR1()
{
    if(digitalRead(encoder1.pin2)){ encoder1.ticks++; }
    else{ encoder1.ticks--; }
}

void encoderISR2()
{
    if(digitalRead(encoder2.pin2)){ encoder2.ticks++; }
    else{ encoder2.ticks--; }
}

void setConfiguration()
{
    configuration.speedPIDKp = SPEED_KP;
    configuration.speedPIDKi = SPEED_KI;
    configuration.speedPIDKd = SPEED_KD;
    configuration.speedPIDOutputLowerLimit = -10.00;
    configuration.speedPIDOutputHigherLimit = 10.00;
    configuration.anglePIDAggKp = ANGLE_KP_AGGR;
    configuration.anglePIDAggKi = ANGLE_KP_AGGR;
    configuration.anglePIDAggKd = ANGLE_KP_AGGR;
    configuration.anglePIDConKp = ANGLE_KP_CONS;
    configuration.anglePIDConKi = ANGLE_KP_CONS;
    configuration.anglePIDConKd = ANGLE_KP_CONS;
    configuration.anglePIDLowerLimit = ANGLE_LIMIT;
    configuration.calibratedZeroAngle = CALIBRATED_ZERO_ANGLE;
}

void setup()
{
    timestamp=millis();
    Serial.begin(SERIAL_BAUDRATE);
    Serial.setTimeout(10);
    while(!Serial) {}

    //Caution: beware to change TIMER0 default register.
    //Millis, delay and other functions uses the same TIMER0 as PWM pin 5 and 6.
    //Check https://arduino-info.wikispaces.com/Arduino-PWM-Frequency
    //define PWM pre-scaler to 3921.16 Hz in TIMER1
    TCCR1B = (TCCR1B & B11111000) | B00000010;

    //interrupt pins
    pinMode(encoder1.pin1, INPUT_PULLUP);
    pinMode(encoder2.pin1, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(encoder1.pin1), encoderISR1, RISING);
    attachInterrupt(digitalPinToInterrupt(encoder2.pin1), encoderISR2, RISING);

    setConfiguration();

/*
    GY80 imu;
	if (CALIBRATION_MAGNETO == 1)
	{
		Serial.println("MAGNETOMETER CALIBRATION STARTED");
		imu.magCalibration();
		Serial.println("CALIBRATION FINISHED");
	}
*/
}

void loop()
{
    //unsigned int start;
    //unsigned int end;
    float velocity1=0, velocity2=0;
    float distance1, distance2;
    int command = 0;
    String msg;
    char buff[128];
    char *ret;
    int size;

    GY80 imu;

    while(1)
	{
        if ((millis() - timestamp) >= DATA_INTERVAL)
		{
			timestamp_old = timestamp;
			timestamp = millis();

			if (timestamp > timestamp_old)
			{
				dt = (float)(timestamp - timestamp_old) / 1000.0f;
			}
			else
			{
				dt = 0;
			}

            msg = "";
            //read serial trace
            //(TRACE_BEGIN)(COMMAND),(NUM_PARAM),(PARAM_1),(PARAM_2),(...)(TRACE_END)
            while(Serial.available() > 0)
            {
                // read the incoming byte:
                msg = Serial.readString();
                Serial.println("msg: " + msg);

                //valid packet?
                if(msg.startsWith(TRACE_BEGIN) && msg.endsWith(TRACE_END)){
                    //remove TRACE_BEGIN
                    msg.remove(0,7);
                    //remove TRACE_END
                    msg.remove(msg.length()-5,5);

                    //convert from string to char array
                    msg.toCharArray(buff, 128);

                    //split string into tokens
                    ret = strtok(buff, ",");

                    //get command
                    command = atoi(ret);
                    size = int(strtok(NULL, ","));

                    switch (command) {
                        case STARTED:
                            started = int(strtok(NULL, ","));
                            Serial.println("STARTED command");
                            break;
                        case DIRECTION:
                            userControl.direction = atof(strtok(NULL, ","));
                            Serial.println("DIRECTION command: " + String(userControl.direction));
                            break;
                        case STEERING:
                            userControl.steering = atof(strtok(NULL, ","));
                            Serial.println("STEERING command: " + String(userControl.steering));
                            break;
                        case SPEED_PID:
                            configuration.speedPIDKp = atof(strtok(NULL, ","));
                            configuration.speedPIDKi = atof(strtok(NULL, ","));
                            configuration.speedPIDKd = atof(strtok(NULL, ","));
                            Serial.println("SPEED_PID command");
                            break;
                        case ANGLE_PID_AGGR:
                            configuration.anglePIDAggKp = atof(strtok(NULL, ","));
                            configuration.anglePIDAggKi = atof(strtok(NULL, ","));
                            configuration.anglePIDAggKd = atof(strtok(NULL, ","));
                            Serial.println("ANGLE_PID_AGGR command");
                            break;
                        case ANGLE_PID_CONS:
                            configuration.anglePIDConKp = atof(strtok(NULL, ","));
                            configuration.anglePIDConKi = atof(strtok(NULL, ","));
                            configuration.anglePIDConKd = atof(strtok(NULL, ","));
                            Serial.println("ANGLE_PID_CONS command");
                            break;
                        case ZERO_ANGLE:
                            configuration.calibratedZeroAngle = atof(strtok(NULL, ","));
                            Serial.println("ZERO_ANGLE command");
                            break;
                        case ANGLE_LIMITE:
                            configuration.anglePIDLowerLimit = atof(strtok(NULL, ","));
                            Serial.println("ANGLE_LIMITE command");
                            break;
                        default:
                            Serial.println("Unknown command");
                            break;
                    }
                }
                else{
                    //Invalid packtet
                }
            }

            //read sensors and calculate Euler Angles
			ori = imu.getOrientation(1, dt); //roll pitch yaw
            anglePIDInput = ori[1];
			//Serial.println("Roll: " + String(ori[0]) + ", Pitch: " + String(ori[1]) + ", Yaw: " + String(ori[2]) + ", DT: " + String(G_Dt) );

            //update velocity
            //velocity: derivative of position (Pf - Pi)/dt in m/s
            if(dt > 0)
            {
                distance1 = encoder1.getDistance();
                distance2 = encoder2.getDistance();
                velocity1 = (distance1 - lastDistance1)*0.01/(dt/1000.0);
                velocity2 = (distance2 - lastDistance2)*0.01/(dt/1000.0);
                lastDistance1 = distance1;
                lastDistance2 = distance2;
            }

            //update motor speed
            motor1.motorSpeed = (float)(encoder1.ticks - encoder1.lastTicks);
            encoder1.lastTicks = encoder1.ticks;
            motor2.motorSpeed = (float)(encoder2.ticks - encoder2.lastTicks);
            encoder2.lastTicks = encoder2.ticks;

            //Compute Speed PID (input is wheel speed. output is angleSetpoint)
            speedPIDInput = motor1.motorSpeed + motor2.motorSpeed;
            speedPID.setSetpoint(userControl.direction);
            speedPIDOutput = speedPID.compute(speedPIDInput);

            //set angle setpoint and compensate to reach equilibrium point
            anglePID.setSetpoint(speedPIDOutput+configuration.calibratedZeroAngle);

            // update angle pid tuning. only update if different from current tuning
    		if((activePIDTuning == AGGRESSIVE) && (abs(anglePIDInput) < ANGLE_LIMIT)) {
    			//we're close to setpoint, use conservative tuning parameters
    			activePIDTuning = CONSERVATIVE;
    			anglePID.setTunings(configuration.anglePIDConKp, configuration.anglePIDConKi, configuration.anglePIDConKd);
    		}
    		else if ((activePIDTuning == CONSERVATIVE) && (abs(anglePIDInput) >= ANGLE_LIMIT)) {
    			//we're far from setpoint, use aggressive tuning parameters
    			activePIDTuning = AGGRESSIVE;
    			anglePID.setTunings(configuration.anglePIDAggKp, configuration.anglePIDAggKi, configuration.anglePIDAggKd);
    		}
    		else if (abs(anglePIDInput) > ANGLE_IRRECOVERABLE){
    			// so sorry, we're licking the floor :(
    			started = false;
    		}

            // Compute Angle PID (input is current angle, output is angleSetpoint)
    		anglePIDOutput = anglePID.compute(anglePIDInput);
            //Serial.println("Pitch: " + String(anglePIDInput) + ", anglePIDOutput: " + String(anglePIDOutput));

            //Set PWM value
            if (started) {
                if (userControl.steering > 0) {
                    motor1.setSpeedPercentage(anglePIDOutput+userControl.steering);
                    motor2.setSpeedPercentage(anglePIDOutput);
                }
                else if (userControl.steering < 0) {
                    motor1.setSpeedPercentage(anglePIDOutput);
                    motor2.setSpeedPercentage(anglePIDOutput-userControl.steering);
                }
                else {
                    motor1.setSpeedPercentage(anglePIDOutput);
                    motor2.setSpeedPercentage(anglePIDOutput);
                }
            }
            else {
                motor1.motorOff();
                motor2.motorOff();
            }

            //write serial trace
            /*Serial.println(TRACE_BEGIN + \
                           String(round(ori[0])) + "," + \
                           String(round(ori[1])) + "," + \
                           String(round(ori[2])) + "," + \
                           String(encoder1.ticks) + "," + \
                           String(encoder2.ticks) + "," + \
                           String(encoder1.getDistance()) + "," + \
                           String(encoder2.getDistance()) + "," + \
                           String(round(velocity1)) + "," + \
                           String(round(velocity2)) + "," + \
                           String(round(speedPIDOutput)) + "," + \
                           String(round(anglePIDOutput)) + "," + \
                           String(round(userControl.direction)) + "," + \
                           String(round(userControl.steering)) + \
                           TRACE_END);*/
        }
	}
}