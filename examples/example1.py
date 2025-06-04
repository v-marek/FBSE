from geomdl import BSpline
from fbse import YCurve

curve = BSpline.Curve()
curve.degree = 2
curve.ctrlpts = [[0.0, 0.0], [1.0, 0.5], [2.0, 1.0], [3.0, 1.0]]
curve.knotvector = [0.0, 0.0, 0.0, 1.0, 3.0, 3.0, 3.0]

x = 0.5     # x for which we require a y value

curve_evaluator = YCurve(curve)
result = curve_evaluator.evaluate_point(x)

print(f'for target x={x}, we have t={result[0]}, with spline x={result[1][0]}, y={result[1][1]}')
