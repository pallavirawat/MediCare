from unittest import TestCase
from src.Classifiers_cluster import Classifiers_cluster
class Classifier_cluster_test_GBT(TestCase):
    def setUp(self):
        self.classifier_cluster=Classifiers_cluster()

    def test_breast_cancer(self):
        data = "../data/breast_cancer_svm.txt"
        self.classifier_cluster.Gradient_Boosted_Tree(data)

    def test_invalid_input(self):
        data="/dsa"
        self.classifier_cluster.Gradient_Boosted_Tree(data)

    def test_diabetes(self):
        data="../data/diabetes_svm.txt"
        self.classifier_cluster.Gradient_Boosted_Tree(data)