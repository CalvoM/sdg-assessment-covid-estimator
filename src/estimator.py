def estimator(data):
  impact = {}
  severeImpact={}
  impact["currentlyInfected"] =  data["reportedCases"]*10
  severeImpact["currentlyInfected"] =  data["reportedCases"]*50
  factor = 28//3
  impact["infectionsByRequestedTime"] = impact["currentlyInfected"]*(2**factor)
  severeImpact["infectionsByRequestedTime"]= severeImpact["currentlyInfected"]*(2**factor)
  print(data)
  return {"data":data,"impact":impact,"severeImpact":severeImpact}
