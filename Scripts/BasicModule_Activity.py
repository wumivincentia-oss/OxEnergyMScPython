#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright 2026 University of Oxford. All Rights Reserved.
The authors, being Dr Scot Wheeler, have asserted their moral rights.

This is the module docstring. It can be used to introduce the purpose and
key functionality of the module. It will appear in documentation/help.
As an example, in the spyder help window (top right subwindow be default), 
type scipy.optimize to see an example of the docstring for the 
optimize module of the scipy library.

The very first line of the script is an optional shebang line. It tells the 
operating system which interpreter to use to execute the code if the script 
was treated as a stadalone executable.
"""

# Complete the script by filling in the missing code sections marked with <---.

# import required libraries
import math

# =============================================================================
# Calculate PV array size function TODO
# =============================================================================

def calc_pv_array_size(building_width, building_length,
                       roof_angle, pv_width, pv_height,
                       pv_power):
    """
    This is a docstring. Use it to explain to the user what a function does.
    It will automatically be read by 'help' functions such as in spyder.
    
    Function to calculate the size of a PV array that can fit on a building
    with shed style roof.

    Parameters
    ----------
    building_width : float
        Width of building in metres.
    building_length : float
        Length of building in metres.
    roof_angle : float
        Angle of the roof from horizontal in degrees.
    pv_width : float
        Width of single PV panel in mm.
    pv_height : float
        Width of single PV panel in mm.
    pv_power : float
        Power of single PV panel in W.

    Returns
    -------
    total_power : float
        Total power of PV array in kW.
    """

    # TODO: add your code to calculate PV array size from the previous exercise.

    return # TODO: return the calculated total power

# =============================================================================
# Example PV class
# =============================================================================
class PV():
    """
    PV object

    Parameters
    ----------
    pv_id : str
        Unique identifier for the PV asset.
    capacity_factor : list or numpy array
        Capacity factor (kW/kWp) profile for the PV asset.
    installed_capacity : float, optional
            Installed capacity of the PV asset in kW.
    dt : float, optional
        Time step in hours. The default is 1 hour.
    
    """

    def __init__(self, pv_id, capacity_factor, installed_capacity, dt=1):
        """
        The __init__ method is a special method that is called when an object is first created from a class.
        It allows the class to initialize the attributes of the class.
        """
        self.id = pv_id
        self.capacity_factor = capacity_factor # capacity factor profile for the PV asset
        self.installed_capacity = installed_capacity
        self.T = len(capacity_factor)
        self.dt = dt

        # we can call the method to calculate the output profile on initialisation
        self.pv_output_kW = self.pv_power_output()

    def pv_power_output(self):
        """
        Calculate the PV power output profile.

        Returns
        -------
        pv_output : list
            Power output profile of the PV asset in kW.
        """
        self.pv_output_kW = self.capacity_factor * self.installed_capacity
        return self.pv_output_kW

    def total_energy_output(self):
        """
        Calculate the total energy output of the PV asset over the time period.

        Returns
        -------
        total_energy : float
            Total energy output of the PV asset in kWh.
        """
        total_energy = sum(self.pv_output_kW) * self.dt
        return total_energy

# =============================================================================
# Basic conditional battery class
# =============================================================================
class Storage():
    """
    Storage object

    Parameters
    ----------
    id : str
        Unique identifier for the battery asset.
    T : int
        Total number of time periods.
    max_soc : float, optional
        Maximum state of charge (kWh). The default is 10.0 kWh.
    min_soc : float, optional
        Minimum state of charge (kWh). The default is 1.0 kWh.
    max_power : float, optional
        Maximum power the battery can handle (kW). The default is 15.0 kW.
    efficiency : float, optional
        Base battery efficiency. The default is 0.98.
    soc_0 : float, optional
        Initial state of charge (kWh). The default is 5.0 kWh.
    model : str, optional
        Battery model name. The default is "Tesla Powerwall".
    """

    def __init__(self, id, T, dt, max_soc=14.0, min_soc=0.5, max_power=11.0,
                  efficiency=0.98, soc_0=5.0):

        # Initialize the Storage object with the given parameters.
        self.id = id
        self.T = T # Total number of time periods
        self.dt = dt # Time step in hours
        self.max_soc = max_soc  # Maximum state of charge (kWh)
        self.min_soc = min_soc   # Minimum state of charge (kWh)
        self.max_power = max_power # Maximum power the battery can handle (kW)
        self.efficiency = efficiency    # Base battery efficiency
        self.soc_0 = soc_0  # Initial state of charge (kWh)

        # Initialize lists to track storage power and state of charge over time.
        self.bat_P = [0] * self.T  # Initialize storage power list
        self.soc_E = [self.soc_0] * self.T  # Initialize state of charge list
        

    def storage_charge_action(self, demand_P, t):
        """
        This function decides if to charge or discharge a battery based on a 
        simple conditional battery model, within a single time period t of length dt.
        It is expected to be called inside a loop over all time periods, with the current time period index t passed as an argument.
        It returns the net demand after the storage action.
        
        Parameters
        ----------
        demand_P : float
            The power demand (units of power e.g. kW)
        t : int
            The current time period index.
            
        Returns
        -------
        net_demand : float
            The net demand post storage operation.
        """
        # add you conditional storage model from above
        # the for loop will be outside this function, and will call this function for each timestep t.
        # remember to use the self. prefix to access the class attributes, e.g. self.bat_P, self.soc_E, etc.

        # previous SoC (initial SoC for the first timestep)
        if t == 0:
            soc_prev = self.soc_0
        else:
            soc_prev = self.soc_E[t-1]
        
        # 5. Battery power  (discharge = negative, charge = positive)
        if demand_P > 0:
            # Case (a): discharge
            self.bat_P[t] = ...  # TODO
        elif demand_P < 0:
            # Case (b): charge
            self.bat_P[t] = ...  # TODO
        else:
            # Case (c): no battery operation
            self.bat_P[t] = 0
    
        # 6. Update SoC (apply efficiency depending on charge/discharge)
        if self.bat_P[t] >= 0:
            self.soc_E[t] = ...  # TODO charge
        else:
            self.soc_E[t] = ...  # TODO discharge
    
        result_net_P_t = ...  # TODO
        
        
        return result_net_P_t


if __name__ == "__main__":
    # =============================================================================
    # This section is a common way to incorporate code that you want to run if the 
    # script is executed directly, but will be ignored if the script is 
    # imported as a module into another. 
    # 
    # It separates the executable part of the script from the part that defines
    # reusable components e.g. functions.
    # 
    # This is useful way of testing the code or providing examples of how to 
    # use the code.
    # =============================================================================
    
    
    
    pass