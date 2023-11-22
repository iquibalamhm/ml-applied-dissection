import json
import csv
import argparse
import pickle

# Parse command line argument for qid

parser = argparse.ArgumentParser()
parser.add_argument("dataset", help="Question ID to look for", type=str
                    , choices=['siq2', 'how2qa'])
parser.add_argument("qid", help="Question ID to look for", type=int)
parser.add_argument("blackout_percent", help="Percentage of words to blackout", type=int, default=100)
args = parser.parse_args()

dataset_name = args.dataset
dataset_folder = 'SIQ2' if dataset_name == 'siq2' else 'How2QA'

# Open and read JSON file for 0 blackout percent
with open(f'results/ft_{dataset_name}_{str(0)}/{dataset_name}_val.json') as json_file:
    json_data = json.load(json_file)
    # Extract 'pred' and 'acc' from JSON data
    pred_0 = json_data[str(args.qid)]['pred']
    acc_0 = json_data[str(args.qid)]['acc']

# Open and read JSON file for blackout percent given in args
if args.blackout_percent != 0:
    with open(f'results/ft_{dataset_name}_{str(args.blackout_percent)}/{dataset_name}_val.json') as json_file:
        json_data = json.load(json_file)
        # Extract 'pred' and 'acc' from JSON data
        pred_arg = json_data[str(args.qid)]['pred']
        acc_arg = json_data[str(args.qid)]['acc']

# Open and read CSV file
with open(f'datasets/{dataset_folder}/public_val.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if int(row['qid']) == args.qid:
            question = row['question']
            options = [row['a0'], row['a1'], row['a2'], row['a3']]
            correct_answer_id = row['answer_id']
            video_id = row['video_id']
            break

# Open and load pickle file
with open(f'datasets/{dataset_folder}/subtitles.pkl', 'rb') as pkl_file:
    subtitles = pickle.load(pkl_file)

# Print question, options, correct answer_id, and subtitles
print(f"Question: {question}")
print(f"Options: {options}")
print(f"Correct Answer ID: {correct_answer_id}")
print(f"Subtitles: {subtitles[video_id]}")
#Print 'pred' and 'acc' with 0 blackout percent
print(f"Prediction with {str(0)} blackout percentage: {pred_0}")
print(f"Accuracy with {str(0)} blackout percentage: {acc_0}")
if args.blackout_percent != 0:
    # Print 'pred' and 'acc' with blackout percent given in args
    print(f"Prediction with {str(args.blackout_percent)} blackout percentage: {pred_arg}")
    print(f"Accuracy with {str(args.blackout_percent)} blackout percentage: {acc_arg}")