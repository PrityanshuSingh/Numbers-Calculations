import sys,time,os
width=180
message=("H.E.Y T.H.E.R.E".center(width))
for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)
print("\n")

message=("Welcome to the world of calculations!".center(width))
for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)
print("\n")

message=("I am your personal assitant to help you in any of your problems!".center(width))
for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)
print("\n")

width=150
a=str(input('\nPress enter key to continue:'.center(width)))
width=180
msg="|Note|".center(width)
for char in msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)
print("\n")

width=180
msg="|Before we get started|".center(width)
for char in msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)
print("\n")

msg="|Plzz fill up your details|".center(width)
for char in msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)
print("\n")



def calculate():
    if f==1:
        width=100
        msg="|WELCOME TO CONVERSIONS|".rjust(width)
        for char in msg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print('\n|what type of conversion do you want to do?|')
        print('\nIn areas (press a)')
        print('In volumes (press v)')
        print('In length (press l)')
        print('In mass (press m)')
        print('In temperature (press t)')
        print('In speed (press s)')
        width=150
        g = str(input('\nSelect the required field-'.center(width)))
        if g=='a':
            width=150
            A=int(input('\n|Enter area in m sq.|'.center(width)))
            area= A*10000
            width=180
            print('|Area in cm sq.=|'.center(width))
            width=83
            print(' '.center(width),area,end=" ")
            msg="cm^2"
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.01)
        elif g=='v':
            width=150
            B=int(input('\n|Enter volume in m cube|'.center(width)))
            volume=B*1000000
            width = 180
            print('|Volume in cm cube=|'.center(width))
            width=83
            print(' '.center(width),volume,end=" ")
            msg="cm^3"
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(1.0)
        elif g=='l':
            width=180
            print('|what u want to convert nd in which unit?|'.center(width))
            print('\nFor KM to M (press 1)')
            print('For M to CM (press 2)')
            print('For CM to MM(press 3)')
            h=int(input('\nSelect the option u need='.center(width)))
            if h==1:
                width=150
                C=int(input('|Enter length in KM-|'))
                meter=C*1000
                width = 180
                print('|Length in meter=|'.center(width))
                width=83
                print(' '.center(width),meter,end=" ")
                msg="meters"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(1.0)
            elif h==2:
                width=150
                D=int(input('|Enter length in M-|'))
                cm=D*100
                width = 180
                print('|Length in centimeter=|'.center(width))
                width=83
                print(' '.center(width),cm,end=" ")
                msg="cm"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(1.0)
            elif h==3:
                width=150
                E=int(input('|Enter length in cm-|'))
                mm=E*10
                width = 180
                print('|Length in mm=|'.center(width))
                width=83
                print(' '.center(width),mm,end=" ")
                msg="mm"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(1.0)
            else:
                print('Opps error!')
        elif g=='m':
            width=180
            print('|what u want to convert nd in which unit?|'.center(width))
            print('\nFor KG to G (press 1)')
            print('For QUIENTAL to KG (press 2)')
            print('For KG to POUND (press 3)')
            i=int(input('\nSelect the option u need='.center(width)))
            if i==1:
                width=150
                F=int(input('|Enter mass in KG-|'))
                grams=F*1000
                width = 180
                print('|Mass in Grams=|'.center(width))
                width=83
                print(' '.center(width),grams,end=" ")
                msg="g"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(1.0)
            elif i==2:
                width = 150
                G=int(input('|Enter mass in Quiental-|'))
                kg=G*100
                width=180
                print('|Mass in Kilograms=|'.center(width))
                width = 83
                print(' '.center(width),kg,end=" ")
                msg="kg"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(1.0)
            elif i==3:
                width = 150
                H=int(input('|enter mass in KG-|'))
                pound=H*2.2046
                width = 180
                print('|Mass in Pounds =|'.center(width))
                width=83
                print(' '.center(width),pound,end=" ")
                msg="pounds"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(1.0)
            else:
                print('Opps error!')
        elif g=='t':
            width=180
            print('|what u want to convert nd in which unit?|'.center(width))
            print('\nFor Fahrenheit to Celsius (press 1)')
            print('For Celsius to Kelvin(press 2)')
            print('For Kelvin to Celsius(press 3)')
            j=int(input('\nSelect the option u need='.center(width)))
            if j==1:
                width = 150
                I=float(input('|Enter temp. in °F-|'))
                Cen=(I-32)*5/9
                width = 180
                print('|Temp. in Celsius=|'.center(width))
                width=83
                print(' '.center(width),Cen,end=" ")
                msg="°C"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(1.0)
            elif j==2:
                width = 150
                J=float(input('|enter temp. in °C-|'))
                kelvin=J+273.15
                width = 180
                print('|Temp. in Kelvin=|'.center(width))
                width=83
                print(' '.center(width),kelvin,end=" ")
                msg="kelvins"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(1.0)
            elif j==3:
                width = 150
                K=float(input('|Enter temp. in Kelvin-|'))
                Cent=K-273.15
                width = 180
                print('|Temp. in Celsius=|'.center(width))
                width=83
                print(' '.center(width),Cent,end=" ")
                msg="°C"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(1.0)
            else:
                print('Opps error!')
        elif g=='s':
            width=180
            print('|what u want to convert nd in which unit?|'.center(width))
            print('\nFor km/h to m/s (press 1)')
            print('For m/s to km/h(press 2)')
            k=int(input('\nSelect the option u need='.center(width)))
            if k==1:
                width = 150
                L=int(input('|Enter speed in km/h-|'))
                ms=L*(5/18)
                width = 180
                print('|Speed in m/s=|'.center(width))
                width=83
                print(' '.center(width),ms,end=" ")
                msg="m/s"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(1.0)
            elif k==2:
                width = 150
                M=int(input('|enter speed in m/s|-|'))
                kmh=M*(18/5)
                width = 180
                print('|Speed in km/h=|'.center(width))
                width=83
                print(' '.center(width),kmh,end=" ")
                msg="km/h"
                for char in msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(1.0)
            else:
                print('Opps error!')
        else:
            print('Opps error!')
    elif f==2:
        width=100
        msg="|SO HERE WE GO FOR AREAS|".rjust(width)
        for char in msg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print('|\nSelect the figure u need to find the area of:\n|')
        print('\n|Rectangle|(1)')
        print('|Square|(2)')
        print('|Circle|(3)')
        print('|Triangle|(4)')
        print('|Trapizium|(5)')
        width = 150
        h=int(input('\nEnter the required field number:'.center(width)))
        if h==1:
            width = 150
            A=float(input('Enter length:'))
            B=float(input('Enter breadth:'))
            area=A*B
            width = 180
            print('|Area of Rectangle=|'.center(width))
            width=83
            print(' '.center(width),area,end=" ")
            msg="units sq."
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(1.0)
        elif h==2:
            width = 150
            C=float(input('Enter the side of square:'))
            area=C**2
            width = 180
            print('|Area of square=|'.center(width))
            width=83
            print(' '.center(width),area,end=" ")
            msg="units sq."
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(1.0)
        elif h==3:
            width = 150
            D=float(input('Enter radius of circle:'))
            area=3.14*D**2
            width = 180
            print('|Area of circle=|'.center(width))
            width=83
            print(' '.center(width),area,end=" ")
            msg="units sq."
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(1.0)
        elif h==4:
            width = 150
            E=float(input('Enter Base:'))
            F=float(input('Enter Height:'))
            area=1/2*E*F
            width = 180
            print('|Area of Triangle=|'.center(width))
            width=83
            print(' '.center(width),area,end=" ")
            msg="units sq."
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(1.0)
        elif h==5:
            width = 150
            G=float(input('Enter one side of Trapizium:'))
            H=float(input('Enter another side of Trapizium:'))
            I=float(input('Enter the height of Trapizium:'))
            area=1/2*I*(G+H)
            width = 180
            print('|Area of Trapizium=|'.center(width))
            width=83
            print(' '.center(width),area,end=" ")
            msg="units sq."
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(1.0)
        else:
            print('Opps Error!')
    elif f==3:
        width=100
        msg="|LETS FIND PERIMETERS|".rjust(width)
        for char in msg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print('\nSelect the figure u need to find the perimeter of:\n')
        print('\n|Rectangle|(1)')
        print('|Square|(2)')
        print('|Circle|(3)')
        print('|Triangle|(4)')
        width = 150
        I=int(input('\nEnter the required field number:'.center(width)))
        if I==1:
            width = 150
            A=float(input('Enter length:'))
            B=float(input('Enter breadth:'))
            peri=2*(A+B)
            width = 180
            print('|Perimeter of Rectangle=|'.center(width))
            width=83
            print(' '.center(width),peri,end=" ")
            msg="units"
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(1.0)
        elif I==2:
            width = 150
            C=float(input('Enter the side of square:'))
            peri=4*C
            width = 180
            print('|Perimeter of square=|'.center(width))
            width=83
            print(' '.center(width),peri,end=" ")
            msg="units"
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(1.0)
        elif I==3:
            width = 150
            D=float(input('Enter radius of circle:'))
            peri=2*3.14*D
            width = 180
            print('|Perimeter of circle=|'.center(width))
            width=83
            print(' '.center(width),peri,end=" ")
            msg="units"
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(1.0)
        elif I==4:
            width = 150
            E=float(input('Enter 1st side:'))
            F=float(input('Enter 2nd side:'))
            G=float(input('Enter 3rd side:'))
            peri=E+F+G
            width = 180
            print('|Perimeter of Triangle=|'.center(width))
            width=83
            print(' '.center(width),peri,end=" ")
            msg="units"
            for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(1.0)
        else:
            print('Opps Error!')
    elif f==4:
        width=100
        msg="|LETS CALCULATE IT OUT|".rjust(width)
        for char in msg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)
        print('\n|What u wanna do?|\n')
        print('\n|Addition|(1)')
        print('|Subtraction|(2)')
        print('|Multiplication|(3)')
        print('|Division|(4)')
        width = 150
        J=int(input('\nEnter the required field number:'.center(width)))
        if J==1:
            width = 150
            n=int(input('\nHow many numbers do u want to add:'.center(width)))
            sum=0
            for a in range(1,n+1):
                num=float(input('\n'))
                print('+',end=' ')
                sum=sum+num
            width = 180
            print('|Sum is=|'.center(width))
            width=87
            print(''.center(width),sum)
        elif J==2:
            width = 150
            a=int(input('\n'))
            print('-',end=' ')
            b=int(input(''))
            if a>b:
                dif=a-b
                width = 180
                print('|Difference is =|'.center(width))
                width=87
                print(''.center(width),dif)
            elif a<b:
                dif=a-b
                width = 180
                print('|Difference is =|'.center(width))
                width=87
                print(''.center(width),dif)
            elif a==b:
                dif=0
                width = 180
                print('|Difference is =|'.center(width))
                width=87
                print(''.center(width),dif)
            else:
                print('Opps error!')
        elif J==3:
            width = 150
            n=int(input('\nHow many numbers do u want to multiply:'.center(width)))
            product=1
            for a in range(1,n+1):
                num=float(input(''))
                product=product*num
                print('×')
            print('')
            width = 180
            print('|Product is =|'.center(width))
            width=87
            print(''.center(width),product)
        elif J==4:
            width = 150
            a=int(input('\n'))
            print('÷')
            b=int(input(''))
            if a>b:
                div=a/b
                width = 180
                print('|Quotient is =|'.center(width))
                width=87
                print(''.center(width),div)
            elif a<b:
                div=a/b
                width = 180
                print('|Quotient is =|'.center(width))
                width=87
                print(''.center(width),div)
            elif a==b:
                div=1
                width = 180
                print('|Quotient is=|'.center(width))
                width=87
                print(''.center(width),div)
        else:
            print('Opps error!')
    else:
        print('Opps error!')

    mg="\nHAVE A GOOD DAY!"
    for char in mg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

width=150
z = str(input('\nOR YOU WANT TO SKIP(yes or no):'.center(width)))
width=180
if z == 'no':
    b = str(input('|First Name|-'))
    c = str(input('|Last Name|-'))
    d = int(input('|Age|-'))
    e = str(input('|School or College?|-'))
    print('')
    print('|THANKS FOR YOUR INFO|'.center(width), end="\n")
    mg = ('|HOPE YOU WILL ENJOY YOUR EXPERIENCE|'.center(width))
    for char in mg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print('\nSelect your required option by pressing the required number:\n')
    width = 120
    print('|Conversions(1)|'.center(width), end="")
    print('|Areas(2)|', end="\n")
    print('|Perimeters(3)|'.center(width), end="")
    print('|Simple calculations(4)|', end="\n")
    width = 160
    f = int(input('\nenter ur choice-'.center(width)))
    calculate()

elif z == 'yes':
    print('')
    mg = ('|HOPE YOU WILL ENJOY YOUR EXPERIENCE|'.center(width))
    for char in mg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print('\nSelect your required option by pressing the required number:\n')
    width = 120
    print('|Conversions(1)|'.center(width), end="")
    print('|Areas(2)|', end="\n")
    print('|Perimeters(3)|'.center(width), end="")
    print('|Simple calculations(4)|', end="\n")
    width = 160
    f = int(input('\nenter ur choice-'.center(width)))
    calculate()

else:
    print('Opps error!')