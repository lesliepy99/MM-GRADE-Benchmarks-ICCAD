import evaluate
import json
import statistics
bleu = evaluate.load("bleu")
rouge = evaluate.load("rouge")

EVAL_NAME = "MM-GRADE_top4"
QA_PATH = "../benchmark/QA.jsonl"

id2type_map = {}
with open(QA_PATH) as fr:
    for l in fr:
        sample = json.loads(l)
        id2type_map[sample["id"]] = sample["type"]

type2bleu_map = {}
type2rougeL_map = {}
bleu_scores = []
rougeL_scores = []
with open("./answers/"+EVAL_NAME+".jsonl") as fr:
    for l in fr:
        sample = json.loads(l)
        model_answer = sample["model_answer"]
        gt_answer = sample["gt_answer"]
        results_bleu = bleu.compute(predictions=[model_answer],references=[gt_answer])
        results_rouge = rouge.compute(predictions=[model_answer],references=[gt_answer])
        bleu_scores.append(results_bleu["bleu"])
        rougeL_scores.append(results_rouge["rougeL"])
        tp = id2type_map[sample["id"]]
        if tp not in type2bleu_map:
            type2bleu_map[tp] = [results_bleu["bleu"]]
            type2rougeL_map[tp] = [results_rouge["rougeL"]]
        else:
            type2bleu_map[tp].append(results_bleu["bleu"])
            type2rougeL_map[tp].append(results_rouge["rougeL"])
print("Average Bleu ",statistics.mean(bleu_scores))
for tp in type2bleu_map:
    print(tp,"=",statistics.mean(type2bleu_map[tp]))

print("=============")
print("Average RougeL ",statistics.mean(rougeL_scores))
for tp in type2rougeL_map:
    print(tp,"=",statistics.mean(type2rougeL_map[tp]))