# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import argparse
import utils


def main(args_):
    num_predictions = 0
    total, correct = 0, 0
    with open(args_.eval_corpus_path) as f:
        for _ in f:
            num_predictions += 1
    predictions = ["London"] * num_predictions
    total, correct = utils.evaluate_places(args_.eval_corpus_path, predictions)
    if total:
        print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))


if __name__ == '__main__':

    argp = argparse.ArgumentParser()
    argp.add_argument('--eval_corpus_path', help="Path of the corpus to evaluate on", default=None)
    args = argp.parse_args()

    main(args)
