# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 16:29:07 2021

@author: amint
"""
import cv2
import numpy as np
import math

import scipy.spatial
import skimage.draw
import skimage.measure


xy = EllipseModel().predict_xy(np.linspace(0, 2 * np.pi, 25),
                               params=(10, 15, 4, 8, np.deg2rad(30)))
ellipse = EllipseModel()
ellipse.estimate(xy)

np.round(ellipse.params, 2)

np.round(abs(ellipse.residuals(xy)), 5)

