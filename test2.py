import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing(file='schematic.svg') as d:
    r1 = elm.Resistor().id('resistor1').label('100KΩ')
    elm.Capacitor().id('capacitor2')
    T = (elm.Ic()
    .side('L', spacing=1.5, pad=1.5, leadlen=0)   # left side!
    #.side('R', spacing=10)   seems unnuecessary!
    .side('T', pad=1.5, spacing=1, leadlen= 0.5,pinlabel_size= 8 )
    .pin(name='TRG', side='left', pin='2')
    .pin(name='THR', side='left', pin='6')
    .pin(name='DIS', side='left', pin='7')
    .pin(name='CTL', side='right', pin='5')
    .pin(name='OUT', side='right', pin='3')
    .pin(name='RST', side='top', pin='4')
    .pin(name='Vcc', side='top', pin='8')
    .pin(name='GND', side='bot', pin='1')
    .label('Sensor2')
    .id('myarduino1'))
    elm.Wire('n').at(T.RST).to(T.CTL).id('wire1')
    elm.Wire('n').at(T.CTL).to(T.GND).id('wire1')
