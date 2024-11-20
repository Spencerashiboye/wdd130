""" Purpose: Water flow test 
Arthur: Spencer Ashiboye
"""


def water_column_height(tower_height, tank_height):
    """ Calculate the height of the water column based on the tower height and tank height.

    parameterss:
    tower_height (float): Height of the tower.
    tank(flaot): Height of the tank walls.

    returns:
    float: Height of the water column.
    """
    # calculation of the water column hieght using the fomular
    water_height = tower_height + (3 * tank_height) / 4
    return water_height

def pressure_gain_from_water_height(height):

    water_density = 998.2
    gravity = 9.80665
    pressure = (water_density * gravity * height)  / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    density = 998.2
    pressure = (-friction_factor * pipe_length * density * (fluid_velocity ** 2)) / (2000 * pipe_diameter)
    return pressure

def pressure_loss_from_fittings( fluid_velocity, quantity_fittings):
    density = 998.2
    pressure = (-0.04 * density * (fluid_velocity**2) * quantity_fittings) / 2000
    return pressure

def reynolds_number(hydraulic_diameter, fluid_velocity):
    density = 998.3
    dynamic_viscosity = 0.0010016
    reynolds_number = (density * hydraulic_diameter * fluid_velocity) / dynamic_viscosity
    return reynolds_number

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    density = 998.2
    # calculation of constant K
    k =  0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    # calculate the pressure loss
    pressure_loss = -k * density * fluid_velocity**2 / 2000
    return pressure_loss

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
if __name__ == "__main__":
    main()