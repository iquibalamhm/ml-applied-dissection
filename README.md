# ml-applied-dissection
Run the error analysis the only 3 arguments required are the dataset (how2qa,siq2), the qid (question id) and the blackout percent to compare with the 0 blackout percent (correct video input)  
```
python3 get_question.py how2qa 123 100
```

Example output
```
Question: What type of video is this?
Options: ['cooking', 'gambling', 'sport', 'travelling']
Correct Answer ID: 0
Subtitles: [{'text': 'this around a little bit', 'start': 0, 'end': 8.47}, {'text': "and last but not least let's serve own", 'start': 8.48, 'end': 28.05}, {'text': 'Oh', 'start': 28.06, 'end': 33.5}, {'text': "let's just add a little bit of that chicken", 'start': 33.51, 'end': 37.54}, {'text': "chicken so nicely cooked earlier it's a", 'start': 37.54, 'end': 42.86}, {'text': "wee-wee so nicely cooked earlier it's a light breading and last but not", 'start': 42.86, 'end': 47.81}, {'text': 'nice light breading and last but not for ourselves some fancy wine', 'start': 47.81, 'end': 53.83}, {'text': 'least for ourselves some fancy wine coca-cola one hand action for me', 'start': 53.83, 'end': 60.0}]
Prediction with 0 blackout percentage: 0
Accuracy with 0 blackout percentage: True
Prediction with 70 blackout percentage: 0
Accuracy with 70 blackout percentage: True
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