import streamlit as st
import CoolProp.CoolProp as CP


def main():
    st.title("CoolProp Streamlit App")

    # Example usage of CoolProp
    fluid = "Water"
    temperature = 300  # in Kelvin
    pressure = 101325  # in Pa

    density = CP.PropsSI("D", "T", temperature, "P", pressure, fluid)
    st.write(
        f"Density of {fluid} at {temperature} K and {pressure} Pa: {density} kg/m³"
    )


if __name__ == "__main__":
    main()
