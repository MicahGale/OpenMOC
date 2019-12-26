#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.pardir)
sys.path.insert(0, os.path.join(os.pardir, 'openmoc'))
from testing_harness import MultiSimTestHarness
from input_set import PinCellInput
import openmoc


class MultiSimSimpleTestHarness(MultiSimTestHarness):
    """A multi-simulation eigenvalue calculation for a pin cell problem
    with C5G7 7-group cross section data."""

    def __init__(self):
        super(MultiSimSimpleTestHarness, self).__init__()
        self.input_set = PinCellInput()

    def _create_solver(self):
        """Instantiate a CPULSSolver."""
        self.solver = openmoc.CPULSSolver(self.track_generator)
        self.solver.setNumThreads(self.num_threads)
        self.solver.setConvergenceThreshold(self.tolerance)

if __name__ == '__main__':
    harness = MultiSimSimpleTestHarness()
    harness.main()
