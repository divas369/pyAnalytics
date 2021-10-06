# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 18:06:09 2021

@author: anand
"""
import pandas as pd
import numpy as np
#import os

#os.listdir("D:/analytics/projects/HHEmployeePerformance")
data = pd.ExcelFile("D:/analytics/projects/HHEmployeePerformance/Data Sheet for Interns.xlsx")

data_cdcw = pd.read_excel(data,sheet_name = "CDCW")
data_gst = pd.read_excel(data,sheet_name = "GST")
data_ssbb = pd.read_excel(data,sheet_name = "SSBB")
data_ssgb = pd.read_excel(data,sheet_name = "SSGB")
data_anly = pd.read_excel(data,sheet_name = "Analytics")
data_pmp = pd.read_excel(data,sheet_name = "PMP")

data_cdcw.columns = data_cdcw.iloc[0,:]
data_gst.columns  = data_gst.iloc[0,:]
data_ssbb.columns = data_ssbb.iloc[0,:]
data_ssgb.columns = data_ssgb.iloc[0,:]
data_anly.columns = data_anly.iloc[0,:]
data_pmp.columns  = data_pmp.iloc[0,:]

#%% Taking Gst sheet

filt = data_gst["Month"] == "Month"
data_gst[filt].index

data_gst.drop(data_gst[filt].index, inplace = True)

filt2 = data_gst["Owner"].isnull() == True
data_gst[filt2].index

data_gst.drop(data_gst[filt2].index, inplace = True)


data_gst["Course Name"].replace(["Na","na","Nill","nill"],np.nan,inplace = True)

data_gst["Course Name"].fillna("GST", inplace = True)

uq_val = data_gst["Course Name"].value_counts()

filt = data_gst["Course Name"] == (type=ArithmeticErrordatetime)
data_gst[filt].index















