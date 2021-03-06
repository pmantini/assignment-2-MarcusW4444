# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries
import numpy as np
import math
class DFT:

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""
        #return np.fft.fft(matrix) #just wanted to see what is to be expected
        sx = matrix.shape[0]
        sy = matrix.shape[1]
        N = max(matrix.shape[0],matrix.shape[1])
        newimage = np.zeros((sx,sy),dtype=np.complex)


        W = np.exp(-1j * ((2*math.pi)/N))
        for u in range(sx):
            for v in range(sy):
                t = 0

                for i in range(sx):
                    for j in range(sy):
                        #t = t + (matrix[i,j]*math.exp((-1j.imag)*((2*math.pi)/N)*((u*i) +(v*j))))
                        t = t + ((matrix[i,j]*(math.cos(((math.pi*2)/N)*((u*i)+(v*j)))  - (((1j)*math.sin(((math.pi*2)/N)*((u*i)+(v*j))))))))
                        #((1j).imag)
                newimage[u,v] = t



        return newimage

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        matrix: a 2d matrix (DFT) usually complex
        takes as input:
        returns a complex matrix representing the inverse fourier transform"""
        #return np.fft.ifft(matrix) #just wanted to see what is to be expected
        sx = matrix.shape[0]
        sy = matrix.shape[1]
        N = max(matrix.shape[0], matrix.shape[1])
        newimage = np.zeros((sx,sy),dtype=np.complex)
        for u in range(sx):
            for v in range(sy):
                t = 0

                for i in range(sx):
                    for j in range(sy):
                        t = t + ((matrix[i, j] * (math.cos(((math.pi * 2) / N) * ((u * i) + (v * j))) - (
                        ((1j) * math.sin(((math.pi * 2) / N) * ((u * i) + (v * j))))))))

                         #t = t + (matrix[i,j]*math.exp((1j.imag)*((2*math.pi)/N)*((u*i) +(v*j))))

                        #t = t + (matrix[i, j] * (math.cos(((math.pi * 2) / N) * ((u * i) + (v * j))) + (
                        #(((1j).imag) * math.sin(((math.pi * 2) / N) * ((u * i) + (v * j)))))))

                newimage[u, v] = t #round(t)

        if (False):
            for u in range(sx):
                for v in range(sy):
                    newimage[u,v] = math.floor(math.log(abs(newimage[u,v])))

        return newimage


    def discrete_cosine_tranform(self, matrix):
        """Computes the discrete cosine transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing discrete cosine transform"""

        sx = matrix.shape[0]
        sy = matrix.shape[1]
        N = max(matrix.shape[0], matrix.shape[1])
        newimage = np.zeros((sx,sy),dtype=np.complex)

        for u in range(sx):
            for v in range(sy):
                t = 0

                for i in range(sx):
                    for j in range(sy):
                        t = t + (matrix[i, j] * math.cos(((2*math.pi)/N)*((u*i)+(v*j))))

                newimage[u, v] = t


        return newimage


    def magnitude(self, matrix):
        """Computes the magnitude of the DFT
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the dft"""


        sx = matrix.shape[0]
        sy = matrix.shape[1]
        N = max(matrix.shape[0], matrix.shape[1])
        newimage = np.zeros((sx, sy))

        for u in range(sx):
            for v in range(sy):
                t = matrix[u, v]
                if (False):
                    t = 0
                    for i in range(sx):
                        for j in range(sy):
                            # t = t + (matrix[i,j]*math.exp((-1j.imag)*((2*math.pi)/N)*((u*i) +(v*j))))
                            m = (matrix[i, j] * (math.pow(math.cos(((math.pi * 2) / N) * ((u * i) + (v * j))),2) - (
                            (math.pow(math.sin(((math.pi * 2) / N) * ((u * i) + (v * j))),2)))))

                            #m = 1j

                            t = t + m
                y = math.sqrt(math.pow(t.real, 2) + math.pow(t.imag, 2))  # magnitude
                #np.log(np.abs(t))
                newimage[u, v] = y


        mx = np.max(newimage)
        mn = np.min(newimage)
        for u in range(sx):
            for v in range(sy):
                newimage[u,v] = ((newimage[u,v] - mn)/ max(1, mx)) * (255)
        return newimage