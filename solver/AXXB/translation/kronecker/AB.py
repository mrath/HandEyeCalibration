# /usr/bin/env python

import numpy as np
import scipy.linalg as linalg

from tools.tools import *

from solver.AXXB.SolverAXXB import SolverAXXB

class AB(SolverAXXB):

    @property
    def shortName(self):
        return "XKronT"

    def solveRotation(self):
        N = self.N
        I = np.identity(3)
        A = np.zeros( (N,3,12) )
        b = np.zeros( (N,3,1) )

        for i in range(N):
            RA = self.RA(i)
            RB = self.RB(i)
            tA = self.tA(i)
            tB = self.tB(i)

            A[i, 0:3, 0:9 ] = linalg.kron(I, tB.T)
            A[i, 0:3, 9:12] = I - RA

            b[i] = tA

        A = np.reshape(A, (A.shape[0]*A.shape[1],-1))
        b = np.reshape(b, (b.shape[0]*b.shape[1],-1))
        x = linalg.lstsq(A, b)[0]

        R = np.reshape(x[0:9], (3,3))
        t = x[9:12]

        X = np.identity(4)
        X[0:3, 0:3] = orthonormalize_rotation(R)
        X[0:3, 3:4] = t

        return (X, X)
