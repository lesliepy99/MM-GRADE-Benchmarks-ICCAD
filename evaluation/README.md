# Score Evaluation Criteria (LLM-Score)
The scoring criteria of all queries in ORD-MMBench is saved in the file [ORD-MMBench-Scoring-criteria.xlsx](./ORD-MMBench-Scoring-criteria.xlsx).

For each query, there are 3 score levels : 25, 50 100. During the evaluation of the generated answer, the LLM-evaluator should first refer to the 100-score-level criteria to see if the answer satisfies the criteria: If satisfied, the generated answer is scored 100 points; otherwise, the evaluator switch to the 50-score-level criteria and repeat the above procedure. 
The 25-score-level criteria should be finally refered to if the generated answer does not meet the 50-score-level criteria.

Note that for each generated answer for a query, the evaluation score ranges from 0 to 100.


One example is as follows:
|query id | 25 | 50 | 100 |
| ------------- | ------------- |------------- | ------------- |
|1 | (1) mention global_net_threshold | (1) give the command "triton_part_design -global_net_threshold X" (X indicates a number greater than 1000) | (1) suggest setting a larger value of global_net_threshold |

where there is one scoring item under the 25-score-level, 50-score-level and 100-score-level scoring criteria.


In some scenarios, there may be more than 1 scoring items under a specific score-level, for example:

|query id | 25 | 50 | 100 |
| ------------- | ------------- |------------- | ------------- |
|3 || "(1) give the command ""initialize_floorplan"" (2) provide the option ""-core_space""" |

In this example, the 100-score-level and 25-score-level criteria is empty, and there are two scoring items under the 50-score-level criteria. If both the (1) and (2) items are satisfied by the generated answer, the evaluated score is 100; if either (1) or (2) is satisfied, the ultimate evaluation score i 50; otherwise if neither is satisfied, the evaluation score is 0.

In this experiment, we use GPT-4o for LLM-Score evaluation, the corresponding prompt is:
```
You are an expert in Exploratory Data Analysis (EDA) and are tasked with evaluating the performance of an EDA tool's Question Answering (QA) system.  

Given an EDA question (`q`), its scoring criteria (`sc`), and the corresponding answer (`a`), your role is to assess the score of the provided answer (`a`) based on the scoring criteria (`sc`).  

### Scoring Guidelines:
The scoring criteria (`sc`) are divided into three score levels: **25**, **50**, and **100**. Each score level may contain up to 4 scoring items (or none, if the level is empty).  

To evaluate the score:  
1. Start with the **highest score level (100)**. Check if the answer (`a`) meets any of the criteria for the 100-score level.  
   - If `a` satisfies the 100-score level, assign a score of **100**, and **stop the evaluation process**.  
   - If `a` does not meet any criteria for the 100-score level, proceed to the next lower level.  
2. Move to the **50-score level**. Count the number of items in this level that `a` satisfies.  
   - If `n` items are met, assign a score of `n * 50`, and **stop the evaluation process**.  
   - If no items are satisfied, proceed to the next level.  
3. Finally, evaluate the **25-score level** if the previous levels were not satisfied. Count the number of items in this level that `a` satisfies.  
   - If `n` items are met, assign a score of `n * 20`
   - If no criteria in this level are met, assign a score of **0**.  

### Notes:
1. The total evaluation score for any given question (`q`) and answer (`a`) pair will range from **0 to 100**, in increments of 25.  
2. Some scoring levels may have no criteria. If a level’s scoring criteria are empty, **skip evaluation for that level**.
3. Your score can only come from only one level among the 100-score, 50-score and 25-score level. If there is already on item in 50-score level matched with the answer, you should skip evaluating the 25-score level.

### Required Output:
Your output should adhere to the following structure:  

```
<analysis>
In this section, provide a detailed explanation of your evaluation process for each score level. If a scoring level has no criteria, explicitly state that the level is skipped.
</analysis>

<score>
In this part, you should solely output the number of the evaluated score. Don't include anything else.
</score>
```

### Input:
- **User question (`q`)**: {q}  
- **Scoring criteria for each score level (`sc`)**: {sc}  
- **Given answer (`a`)**: {a}  

### Your output:
```