import ExtractData
import config
import GradePrediction

def operate():
    ExtractData.extract()
    GradePrediction.predictGrades()

if __name__ == "__main__":
    operate()