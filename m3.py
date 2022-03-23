def control(inputs):
    
    distance_right = inputs["distance-right"]
    distance_left  = inputs["distance-left"]
    front_left  = inputs["front-left"]
    front_right = inputs["front-right"]
    
    leftSpeed  =  0;
    rightSpeed =  0;
    
    if distance_right<300 and distance_left<300:
        leftSpeed  = 30;
        rightSpeed = -30;
    elif distance_right==300 and distance_left<300:
        leftSpeed  = -10;
        rightSpeed = -10;
    else:
        leftSpeed  =  10;
        rightSpeed =  10;

    if front_right>=1:
        leftSpeed  = -10;
        rightSpeed = -10;
    elif front_left>=1:
        leftSpeed  =  10;
        rightSpeed =  10;
        
    return {
        'leftSpeed': leftSpeed,
        'rightSpeed': rightSpeed,
        'log': [
            { 'name': 'Distance Left',  'value': distance_left,  'min': 0, 'max': 300 },
            { 'name': 'Distance Right', 'value': distance_right, 'min': 0, 'max': 300 }
        ]
    }
