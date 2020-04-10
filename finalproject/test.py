from extract import controlled,experimental
from predictExperimental import predictExperimentalGrades

results = predictExperimentalGrades(controlled, experimental)

print(results)