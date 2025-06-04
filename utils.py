import numpy as np
import matplotlib.pyplot as plt
from geomdl import BSpline
from time import time

class YCurve:
    def __init__(self, curve:BSpline.Curve()):
        # load the bspline
        self.curve = curve
        self.err = 0.0001

        if True:
            self.curve = BSpline.Curve()
            self.curve.degree = 2
            self.curve.ctrlpts = [[0.0, 0.0], [1.0, 0.5], [2.0, 1.0], [3.0, 1.0]]
            self.curve.knotvector = [0.0, 0.0, 0.0, 1.0, 3.0, 3.0, 3.0]

        self.endpoint = None        # the endpoint of the curve
        self.startpoint = None      # the startpoint of the curve
        self.x = None               # TARGET                        (also just x)
        self.t = None               # CURRENT T ESTIMATE            (also just t)
        self.est = None             # CURRENT RES FOR T ESTIMATE    (also just est)

    def evaluate_point(self, x):
        def recur_eval(erri, ti):
            ti = (ti+(erri/self.endpoint))
            esti = self.curve.evaluate_single(ti)
            erri = self.x-esti[0]
            if abs(erri) < self.err: return ti, esti
            else: recur_eval(erri, ti)

        # eval points
        self.endpoint = self.curve.evaluate_single(1.0)[0]
        self.startpoint = self.curve.evaluate_single(1.0)
        self.x = x

        # make first estimate (g1 = x)
        t = x/self.endpoint
        est = self.curve.evaluate_single(t)
        err = x - est[0]

        results = recur_eval(err, t)

    def viz(self, est):
        self.curve.sample_size = 1000
        pts = self.curve.evalpts

        x, y = [], []
        for pt in pts:
            x.append(pt[0])
            y.append(pt[1])

        plt.plot(x, y, color='red')
        plt.scatter(est[0], est[1], color='green', marker='x')
        plt.plot([est[0], est[0]], [0, est[1]], color='blue', linestyle='--')
        plt.plot([self.x, self.x], [0, max(y)], color='black', linestyle='--')
        plt.show()

    def reset(self):
        pass
        #TODO: implement a reset of known evaluated points

if __name__ == '__main__':


    crv = YCurve(None)
    crv.evaluate_point(0.5)