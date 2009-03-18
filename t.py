from pydy import *
from sympy import *
import sympy
print sympy.__file__
t, x, y = symbols('t x y')
q1 = Function("q1")(t)
q2 = Function("q2")(t)
q3 = Function("q3")(t)

N = ReferenceFrame('N')
A = N.rotate('A', 3, q1)
B = A.rotate('B', 1, q2)
C = B.rotate('C', 2, q3)
D = A.rotate('D', 2, q3)
E = D.rotate('E', 2, q3)
F = E.rotate('F', 3, q1)

print "N.ref_frame_list", N.ref_frame_list
print "A.ref_frame_list", A.ref_frame_list
print "N to N", N.get_frames_list(N)
print "N to A", N.get_frames_list(A)
print "A to A", A.get_frames_list(A)
print "A to N", A.get_frames_list(N)
print "B to B", B.get_frames_list(B)
print "B to A", B.get_frames_list(A)
print "B to N", B.get_frames_list(N)
print "A to B", A.get_frames_list(B)
print "N to B", N.get_frames_list(B)
print "C to D: ", C.get_frames_list(D)
print "C to E: ", C.get_frames_list(E)
print "C to F: ", C.get_frames_list(F)
print "D to C: ", D.get_frames_list(C)
print "E to C: ", E.get_frames_list(C)
print "F to C: ", F.get_frames_list(C)
stop


#print coeff(C.get_omega(N),[q1.diff(t),q2.diff(t),q3.diff(t)])
#print N.get_omega(C)

##
e = y + x*A[1] + x + A[2]
print e
print coeff(e,[x,y])
print [A[1]+1, 1]

stop
#print A.W
#stop
#print B.W
#print C.W

#print B.get_rot_matrices(A)
#print A.get_rot_matrices(B)
#print A.get_rot_matrices(C)

#e = B[1]*q1.diff(t)*B[1]
#e = B[1]*q1*B[1]
#print B[1].is_commutative
#print q2.is_commutative
#print q1.is_commutative
#print q1.diff(t).is_commutative
#print sin(q2).is_commutative
#print e

stop
e = cross(N[1], A[1])
print e
e = cross(N[1], A[2])
print e
e = cross(N[1], A[3])
print e
e = cross(N[2], A[1])
print e
e = cross(N[2], A[2])
print e
e = cross(N[2], A[3])
print e
e = cross(N[3], A[1])
print e
e = cross(N[3], A[2])
print e
e = cross(N[3], A[3])
print e


e = cross(A[1], A[1])
print e
