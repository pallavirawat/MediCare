from unittest import TestCase
from src.Classifiers_cluster import Classifiers_cluster
class DTModelTest(TestCase):
    def setUp(self):
        self.classifier_cluster=Classifiers_cluster()

    def test_breast_cancer(self):
        data = "../data/breast_cancer_svm.txt"
        self.classifier_cluster.PredictDecision_Tree(data)