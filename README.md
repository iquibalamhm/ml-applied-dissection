# ml-applied-dissection
Run the error analysis the only argument required is the qid (question id)
```
python3 get_question.py 1
```

Example output
```
Question: What program is used in this clip?
Options: ['Excel', 'Powerpoint', 'Word', 'Access']
Correct Answer ID: 0
Subtitles: [{'text': 'friend will going to learn how to', 'start': 0.08, 'end': 3.44}, {'text': 'hello friend will going to learn how to a digital clock in Excel', 'start': 3.44, 'end': 6.89}, {'text': "create a digital clock in Excel like this let's go to make", 'start': 6.89, 'end': 11.15}, {'text': "worksheet like this let's go to make this I want to tell you before start to it please download the VBA code", 'start': 11.15, 'end': 15.98}, {'text': 'make it please download the VBA code file which is in the description box and open the text file and', 'start': 15.98, 'end': 25.18}, {'text': 'download and open the text file and the full movies to follow the step', 'start': 25.18, 'end': 29.35}, {'text': 'watch the full movies to follow the step open Excel in the cell a1 give now', 'start': 29.35, 'end': 40.22}, {'text': 'now open Excel in the cell a1 give now formula', 'start': 40.22, 'end': 43.58}, {'text': 'change the format to tie now insert', 'start': 43.59, 'end': 53.7}, {'text': 'and change the format to tie now insert a text box [Music]', 'start': 53.7, 'end': 60.0}]

```

# Results
FrozenBILM finetuned on How2qa; ablation studies on How2qa dataset:
1. Correct video: 86.32
2. Shuffled video frames: 85.37
3. Reversed video frames: 84.39
4. 10% randomly blackedout: 86.11
5. 20% randomly blackedout: 85.96
6. 30% randomly blackedout: 85.65
7. 40% randomly blackedout: 85.47
8. 50% randomly blackedout: 85.16
9. 60% randomly blackedout: 84.56
10. 70% randomly blackedout: 83.68
11. 80% randomly blackedout: 83.16
12. 90% randomly blackedout: 80.77
13. 100% blackedout video: 76.25

FrozenBILM finetuned on SIQ2; ablation studies on SIQ2 dataset:
1. Correct video: 78.97
2. Shuffled video frames: 79.54
3. Reversed video frames: 79.43
4. 10% randomly blackedout: 79.54
5. 20% randomly blackedout: 79.31
6. 30% randomly blackedout: 79.08
7. 40% randomly blackedout: 79.31
8. 50% randomly blackedout: 78.97
9. 60% randomly blackedout: 79.08
10. 70% randomly blackedout: 79.88
11. 80% randomly blackedout: 78.4
12. 90% randomly blackedout: 78.05
13. 100% blackedout video: 79.31