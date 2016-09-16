# /usr/bin/env python

import numpy as np
import scipy.linalg as linalg

from tools.tools import *

from solver.AXYB.SolverAXYB import SolverAXYB

class ABStar(SolverAXYB):

    @property
    def shortName(self):
        return "YQuatR*"

    def solveRotation(self):
        N = self.N
        M = np.zeros( (4,4) )

        for i in range(N):
            QA = quaternion_from_matrix(self.RA(i))
            QB = quaternion_from_matrix(self.RB(i))

            RA = matrix_representation(QA, PLUS)
            RB = matrix_representation(QB, MINUS)

            M += RA.dot(RB.T)

        [u,s,v] = linalg.svd(M)

        X = quaternion_matrix(v[0,:])
        Y = quaternion_matrix(u[:,0])

        return (X, Y)
