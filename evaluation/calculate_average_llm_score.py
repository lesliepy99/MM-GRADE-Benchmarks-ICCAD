# SCORING_FILE_PATH = "./evaluate_results/rag-flow/MM-GRADE_without_ESA.json"
SCORING_FILE_PATH = "./scores/echosight_with-MM-GRADE-generator.json"
QA_PATH = "../benchmark/QA.jsonl"
import json
import statistics

id2type_map = {}
with open(QA_PATH) as fr:
    for l in fr:
        sample = json.loads(l)
        id2type_map [sample["id"]] = sample["type"]

scores = []
type2scores_map = {}
with open(SCORING_FILE_PATH) as fr:
    samples = json.load(fr)
    # print(samples)
    for k in samples:
      
        scores.append(int(samples[k]["score"]))
        # print(int(samples[k]["score"]))
        type = id2type_map[int(k)]
        if type not in type2scores_map:
            type2scores_map[type] = [int(samples[k]["score"])]
        else:
            type2scores_map[type].append(int(samples[k]["score"]))
        
print("==============")
print(SCORING_FILE_PATH)
print("overall average score",statistics.mean(scores))
for tp in type2scores_map:
    print("type",tp,"score",statistics.mean(type2scores_map[tp]),len(type2scores_map[tp]))