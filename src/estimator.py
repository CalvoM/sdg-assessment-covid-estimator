def estimator(data):
  impact = {}
  severeImpact={}
  impact.currentlyInfected =  data.reportedCases*10
  severeImpact.currentlyInfected =  data.reportedCases*50
  factor = data.timeToElapse//3
  impact.infectionsByRequestedTime = impact.currentlyInfected*(2**factor)
  severeImpact.infectionsByRequestedTime= severeImpact.currentlyInfected*(2**factor)
  print(data)
  return {data,impact,severeImpact}
