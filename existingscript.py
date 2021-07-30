from psdi.server import MXServer
from psdi.mbo import MboValue

if (app is None or app == “” ) and mbo.getOwner() is not None:
      app = mbo.getOwner().getThisMboSet().getApp()
if app is not None:
      srcAttributes = [“INVOICEDATE”, ” EXCHANGEDATE”]
      for index in srcAttributes:
            current = MXServer.getMXServer().getDate()
            val = mbo.getMboValue(index).getDate()
            if val is not None and val.
                   errorkey=”invalidDate”
                   errorgroup=”invoice”
