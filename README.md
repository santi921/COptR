"# COptR" 

This repo is intended to provide simulation tools for a charge qubit design
diag_trans is the
 file performing the the circuit parameter calculations
it recieved josephson junction and capacitor energies to construct a hamiltonian matrix 
based on a charge basis for representation. The test_slider.py file makes use of the 
diag_trans.py methods to calculate energy levels for proposed circuits that a user can input using
slider commands. The optimizer.py file also makes use of diag_trans.py to calculate energies
 but instead constructs a loss function out of the energies returned in order to output a circuit 
 with low noise sensitivity that also features anharmonic energy levels. This optimizer was used 
 to computationally confirm the desired parameters of a transmon qubit-variant of the charge qubit.

