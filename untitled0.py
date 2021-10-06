# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 21:09:11 2021

@author: divas
"""
import pandas as pd
import numpy as np
data = pd.ExcelFile("D:/analytics/projects/HHEmployeePerformance/Data Sheet for Interns.xlsx")

data_gst = pd.read_excel(data,sheet_name = "GST")
print(data_gst)
data_gst = data_gst.iloc[0,:]
