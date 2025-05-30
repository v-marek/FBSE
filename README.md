# FBSE
### Fast B-Spline Evaluation 

This program allows for fast evaluation of a point on a bspline, given x as input. It is designed to only work on 
simple one-to-one b-splines, where y values are close to zero. The closer, the faster (theoretically).

Mathematical explanation of the code is not and will not be given, because I cannot be bothered. 

An example of the use of the program is given in main.py, using geomdl for the B-spline geometry. This function was very 
much designed with geomdl in mind and the author recommends its use over other implementations. 

~ V.M. (2025)