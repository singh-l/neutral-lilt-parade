from preprocessing import read_data
from sklearn.neural_network import MLPClassifier
from evaluation import evaluate_bow_classifier

if __name__ == "__main__":
    clf = MLPClassifier(verbose=1)
    instances, labels = read_data('../data/Tweets.csv')
    evaluate_bow_classifier(instances, labels, clf, use_argmax_labels=False)
