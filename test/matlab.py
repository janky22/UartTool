import numpy as np
import matplotlib.pyplot as plt

g_lng_last = 0.0
g_lat_last = 0.0
g_angle_last = 0

g_dy_last = 0.0
g_dx_last = 0.0

def get_xy_angle(x, y, x_last, y_last):
    dx = x - x_last
    dy = y - y_last
    global g_angle_last
    Dangle = 0
    angle = 0
    if dx != 0.0 :
        angle = (int) ( np.degrees(np.arctan( dy/dx )) )
    if dx == 0.0 :
        angle = 90

    if ( ( angle > 0 and g_angle_last < 0 ) or ( angle < 0 and g_angle_last > 0 ) ) and dx > 0 :
        Dangle = abs(angle) + abs(g_angle_last)
        print("1(%3.1f,%0.1f)=(%3.1f,%3.1f) da(%3.1f,%3.1f)=%3.1f"%(x,y,dx,dy, g_angle_last,angle,Dangle))
    elif ( ( angle > 0 and g_angle_last < 0 ) or ( angle < 0 and g_angle_last > 0 ) ) and dx < 0 :
        Dangle = 180 - abs(angle - g_angle_last)
        print("2(%3.1f,%0.1f)=(%3.1f,%3.1f) da(%3.1f,%3.1f)=%3.1f"%(x,y,dx,dy, g_angle_last,angle,Dangle))
    else:
        Dangle = abs(angle - g_angle_last)
        print("3(%3.1f,%0.1f)=(%3.1f,%3.1f) da(%3.1f,%3.1f)=%3.1f"%(x,y,dx,dy, g_angle_last,angle,Dangle))
    


    g_angle_last = angle
    return Dangle

def gpsOnLocation(lng, lat):
    global g_lng_last
    global g_lat_last

    Dangle = get_xy_angle(lng, lat, g_lng_last, g_lat_last)
    g_lng_last = lng
    g_lat_last = lat
    
    
    return Dangle

def main():
    fig = plt.figure(figsize=(7,7))
    axes = fig.add_subplot(1,1,1)
    axes_x = []
    axes_y = []

    axes.set(xlim=[0, 200], ylim=[0, 200], title='lng-lat test', ylabel='Y', xlabel='X')
    # for num in range(100):
    #     axes_x.append(num)
    #     axes_y.append(num)
    # axes.set_xticks(axes_x)
    # axes.set_yticks(axes_y)
    x = [0.0, 20.0, 30.0, 50.0, 63.0, 80.0, 85.0, 120, 120, 140, 130, 145] # len
    y = [0.0, 23.0, 60.0, 30.0, 45.0, 35.0, 20.0, 20,  30,  35,  50,  100]
    
    d_angle_l = []
    for i in range(len(x)) :
        d_angle = gpsOnLocation(x[i], y[i])
        d_angle_l.append(d_angle)
 

    print(len(x))
    print(len(d_angle_l))
    # slope = np.diff(y) / np.diff(x)
    # angle = abs( np.degrees(np.arctan(slope)) ) # len-1
    # d_angle = abs( np.diff(angle) )# len-2

    # 设置数字标签
    for a, b in zip(x, y):
        plt.text(a, b, '(%0.1f,%0.1f)'%(a,b), fontsize=8, ha='center', va='baseline', color ='green')
    plt.plot(x, y)

    for a, b in zip(x[:-1], d_angle_l[1:]):
        plt.text(a, b, '(%0.1f,%0.1f)'%(a,b), fontsize=8, ha='center', va='bottom', color ='black')
    plt.bar(x[:-1], d_angle_l[1:], color ='red')

    plt.show()

if __name__ == '__main__':
    main()