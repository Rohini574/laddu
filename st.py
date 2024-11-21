import streamlit as st

def ohms_law(voltage=None, current=None, resistance=None):
    if voltage is None:
        voltage = current * resistance
    elif current is None:
        current = voltage / resistance
    elif resistance is None:
        resistance = voltage / current
    return voltage, current, resistance

st.title('Ohm\'s Law Calculator')

option = st.selectbox(
    'Which value do you want to calculate?',
    ('Voltage', 'Current', 'Resistance')
)

if option == 'Voltage':
    current = st.number_input('Enter the current (A):', min_value=0.0)
    resistance = st.number_input('Enter the resistance (Ω):', min_value=0.0)
    if st.button('Calculate Voltage'):
        voltage, _, _ = ohms_law(current=current, resistance=resistance)
        st.write(f'The voltage is {voltage}V')
elif option == 'Current':
    voltage = st.number_input('Enter the voltage (V):', min_value=0.0)
    resistance = st.number_input('Enter the resistance (Ω):', min_value=0.0)
    if st.button('Calculate Current'):
        _, current, _ = ohms_law(voltage=voltage, resistance=resistance)
        st.write(f'The current is {current}A')
elif option == 'Resistance':
    voltage = st.number_input('Enter the voltage (V):', min_value=0.0)
    current = st.number_input('Enter the current (A):', min_value=0.0)
    if st.button('Calculate Resistance'):
        _, _, resistance = ohms_law(voltage=voltage, current=current)
        st.write(f'The resistance is {resistance}Ω')

st.write('''Ohm's Law states that V = I * R, where:
- V is the voltage in volts
- I is the current in amperes
- R is the resistance in ohms''')
