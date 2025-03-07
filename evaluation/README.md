# Score Evaluation Criteria (Human-Eval)
The scoring criteria of all queries in ORD-MMBench is saved in the file [ORD-MMBench-Scoring-criteria.xlsx](./ORD-MMBench-Scoring-criteria.xlsx).

For each query, there are 3 score levels : 25, 50 100. During the evaluation of the generated answer, the evaluator should first refer to the 100-score-level criteria to see if the answer satisfies the criteria: If satisfied, the generated answer is scored 100 points; otherwise, the evaluator switch to the 50-score-level criteria and repeat the above procedure. 
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
