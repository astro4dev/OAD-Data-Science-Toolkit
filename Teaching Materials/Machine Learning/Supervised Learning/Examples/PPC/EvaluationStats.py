"""
This file is part of contribution to the OAD Data Science Toolkit.

This is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

The software is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this software.  If not, see <http://www.gnu.org/licenses/>.

File name:    EvaluationStats.py
Created:      April 11th, 2018
Author:       Dr. Rob Lyon
 
Contact:    rob@scienceguyrob.com or robert.lyon@manchester.ac.uk
Web:        <http://www.scienceguyrob.com>

Computes and stores the performance statistics of a classifier
given a confusion matrix containing it's true positive, false positive,
true negative and false negative rates.

Designed to run on python 2.4 or later. 
 
"""

from numpy import sqrt

# ******************************
#
# CLASS DEFINITION
#
# ******************************

class ClassifierStats:
    """                
    Computes the performance statistics of a BINARY classifier only.
    
    """

    # ****************************************************************************************************
    #
    # Constructor.
    #
    # ****************************************************************************************************

    def __init__(self,confusionMatrix):
        """
        Default constructor.
        
        Parameters:
        
        confusionMatrix     -    a matrix containing the performance of a given BINARY classifier on
                                 a training set. For example given the matrix,
                                 
                                 [[15528   731]
                                 [  249  1390]]
                                 
                                 Where,
                                 
                                 TrueNegatives  = confusionMatrix[0][0] # Negatives correctly receiving negative label.
                                 FalseNegatives = confusionMatrix[0][1] # Positives incorrectly receiving negative label.
                                 FalsePositives = confusionMatrix[1][0] # Negatives incorrectly receiving positive label.
                                 TruePositives  = confusionMatrix[1][1] # Positives correctly receiving positive label.
                                 
                                 Will not evaluate the performance of multi-class classifiers.
        """

        # The accuracy of the classifier.
        self.accuracy = 0.0

        # The precision of the classifier. Precision is the fraction of retrieved instances that are relevant.
        self.precision = 0

        # The recall of the classifier. Recall is the fraction of relevant instances that are retrieved.
        self.recall = 0.0

        # The precision of the map. Specificity relates to the ability of the map to identify negative results.
        self.specificity = 0.0

        # The negative predictive value (NPV) is a summary statistic
        # defined as the proportion of input patterns identified as negative,
        # that are correctly identified as such. A high NPV means that when the
        # classifier yields a negative result, it is most likely correct in its assessment.
        self.negativePredictiveValue = 0.0

        # The Matthews correlation coefficient is used in machine learning
        # as a measure of the quality of binary (two-class) classifications.
        # It takes into account true and false positives and negatives and
        # is generally regarded as a balanced measure which can be used even
        # if the classes are of very different sizes. The MCC is in essence a
        # correlation coefficient between the observed and predicted binary
        # classifications; it returns a value between -1 and +1. A coefficient
        # of +1 represents a perfect prediction, 0 no better than random prediction
        # and -1 indicates total disagreement between prediction and observation.
        # The statistic is also known as the phi coefficient.
        self.matthewsCorrelation = 0.0

        # The F1 score (also F-score or F-measure) is a measure of a classifier's accuracy.
        # It considers both the precision p and the recall r of the classifier to compute
        # the score: p is the number of correct results divided by the number of all
        # returned results and r is the number of correct results divided by the
        # number of results that should have been returned.
        self.fScore = 0.0

        # The g-mean is a measure of useful for data sets with skewed class distributions.
        # In other words when most examples belong to one class (say the negative), then this
        # metric helps asses performance irrespective of the imbalance. It evaluates the 
        # inductive bias in terms of the ratio between positive and negative accuracy.
        self.gmean = 0.0

        # The kappa statistic. Cohen's kappa coefficient is a statistical measure of inter-rater
        # agreement or inter-annotator agreement for qualitative (categorical) items. It is
        # generally thought to be a more robust measure than simple percent agreement
        # calculation since k takes into account the agreement occurring by chance.
        self.kappa = 0.0

        # The true positives.
        self.TP = 0.0

        # The true negatives.
        self.TN = 0.0

        # The false positives.
        self.FP = 0.0

        # The false negatives.
        self.FN = 0.0

        # The area under the roc curve.
        self.auroc = float('NaN')

        # The area under the precision-recall curve.
        self.auprc = float('NaN')

        self.load(confusionMatrix)
        self.calculate()


    # ****************************************************************************************************

    def load(self,confusionMatrix):
        """
        Loads data from the confusion matrix into the correct variables.
        
        Parameters:
        
        confusionMatrix     -    a matrix containing the performance of a given BINARY classifier on
                                 a training set. For example given the matrix,
                                 
                                 [[15528   731]
                                 [  249  1390]]
                                 
                                 Where,
                                 
                                 TrueNegatives  = confusionMatrix[0][0] # Negatives correctly receiving negative label.
                                 FalseNegatives = confusionMatrix[0][1] # Positives incorrectly receiving negative label.
                                 FalsePositives = confusionMatrix[1][0] # Negatives incorrectly receiving positive label.
                                 TruePositives  = confusionMatrix[1][1] # Positives correctly receiving positive label.
                                 
                                 Will not evaluate the performance of multi-class classifiers.
                                 
        Returns:    N/A.
        """

        self.TN = float(confusionMatrix[0][0]) # Negatives correctly receiving negative label.
        self.FN = float(confusionMatrix[0][1]) # Positives incorrectly receiving negative label.
        self.FP = float(confusionMatrix[1][0]) # Negatives incorrectly receiving positive label.
        self.TP = float(confusionMatrix[1][1]) # Positives correctly receiving positive label.

    # ****************************************************************************************************

    def calculate(self):
        """
        Computes the values of the statistics describing classifier performance.
        
        Parameters: None.
        
        Returns:    N/A.
        
        """
        try:
            self.accuracy = (self.TP + self.TN) / (self.TP + self.FP + self.FN + self.TN)
        except ZeroDivisionError as error:
            self.accuracy = float('Nan')

        try:
            self.precision = (self.TP) / (self.TP + self.FP)
        except ZeroDivisionError as error:
            self.precision = float('Nan')

        try:
            self.recall = (self.TP) / (self.TP + self.FN)
        except ZeroDivisionError as error:
            self.recall = float('Nan')

        try:
            self.specificity = (self.TN) / (self.FP+self.TN)
        except ZeroDivisionError as error:
            self.specificity = float('Nan')

        try:
            self.negativePredictiveValue = (self.TN) / (self.FN + self.TN)
        except ZeroDivisionError as error:
            self.negativePredictiveValue = float('Nan')

        try:
            self.matthewsCorrelation = ((self.TP * self.TN) - (self.FP * self.FN)) /\
                                       sqrt((self.TP+self.FP) * (self.TP+self.FN) * (self.TN+self.FP) * (self.TN+self.FN))
        except ZeroDivisionError as error:
            self.matthewsCorrelation = float('Nan')

        try:
            self.fScore = 2 * ((self.precision * self.recall) / (self.precision + self.recall))
        except ZeroDivisionError as error:
            self.fscore = float('Nan')

        # Kappa = (totalAccuracy - randomAccuracy) / (1 - randomAccuracy)
        #
        # where,
        #
        # totalAccuracy = (TP + TN) / (TP + TN + FP + FN)
        #
        # and
        #
        # randomAccuracy = (TN + FP) * (TN + FN) + (FN + TP) * (FP + TP) / (Total*Total).
        total     = self.TP + self.TN + self.FP + self.FN
        totalAcc  = (self.TP + self.TN) / (self.TP + self.TN + self.FP + self.FN)
        randomAcc =  (((self.TN + self.FP) * (self.TN + self.FN)) + ((self.FN + self.TP) * (self.FP + self.TP))) / (total*total)

        try:
            self.kappa = (totalAcc - randomAcc) / (1 - randomAcc)
        except ZeroDivisionError as error:
            self.kappa = float('Nan')

        try:
            self.gmean = sqrt( ( self.TP /( self.TP + self.FN ) ) * ( self.TN / ( self.TN + self.FP ) ) )
        except ZeroDivisionError as error:
            self.gmean = float('Nan')

    # ****************************************************************************************************

    def show(self):
        """
        Prints classifier performance stats to standard output.

        Parameters: None.

        Returns:    N/A.
        """

        output ='{:<14}'.format("TP:")         +"\t" + str(int(self.TP))                       + "\n" +\
                '{:<14}'.format("TN:")         +"\t" + str(int(self.TN))                       + "\n" +\
                '{:<14}'.format("FP:")         +"\t" + str(int(self.FP))                       + "\n" +\
                '{:<14}'.format("FN:")         +"\t" + str(int(self.FN))                       + "\n" +\
                '{:<14}'.format("Accuracy:")   +"\t" + str(self.accuracy * 100)                + "\n" +\
                '{:<14}'.format("Precision:")  +"\t" + str(self.precision * 100)               + "\n" +\
                '{:<14}'.format("Recall:")     +"\t" + str(self.recall * 100)                  + "\n" +\
                '{:<14}'.format("Specificity:")+"\t" + str(self.specificity * 100)             + "\n" +\
                '{:<14}'.format("NPV:")        +"\t" + str(self.negativePredictiveValue * 100) + "\t(Negative Predictive Value)\n" +\
                '{:<14}'.format("MCC:")        +"\t" + str(self.matthewsCorrelation)           + "\t(Matthews Correlation Coefficient)\n" +\
                '{:<14}'.format("F-Score:")    +"\t" + str(self.fScore)                        +"\n" +\
                '{:<14}'.format("Kappa:")      +"\t" + str(self.kappa)                         +"\n" +\
                '{:<14}'.format("G-Mean:" )    +"\t" + str(self.gmean)                         +"\n" +\
                '{:<14}'.format("AUROC:" )     +"\t" + str(self.auroc)                         +"\n" +\
                '{:<14}'.format("AUPRC:" )     +"\t" + str(self.auprc)                         +"\n"

        print (output)

    # ****************************************************************************************************

    # ******************************
    #           Getters
    # ******************************


    def getAccuracy(self):
        """
        Accuracy of the classifier where accuracy = (TP + TN) / (TP + FP + FN + TN).

        Parameters: None.

        Returns:    accuracy as a float.
        """
        return float(self.accuracy)

    def getPrecision(self):
        """
        Precision of the classifier where precision = (TP) / (TP + FP).

        Parameters: None.

        Returns:    precision as a float.
        """
        return float(self.precision)

    def getRecall(self):
        """
        Recall of the classifier where recall = (TP) / (TP + FN).

        Parameters: None.

        Returns:    recall as a float.
        """
        return float(self.recall)


    def getSpecificity(self):
        """
        Specificity of the classifier where specificity = (TN) / (FP+TN).

        Parameters: None.

        Returns:    specificity as a float.
        """
        return float(self.specificity)


    def getMatthewsCorrelation(self):
        """
        Matthew's Correlation Coefficient of the classifier where,

        matthewsCorrelation = ((TP * TN) - (FP * FN)) / sqrt((TP+FP) * (TP+FN) * (TN+FP) * (TN+FN)).

        Parameters: None.

        Returns:    mcc as a float.
        """
        return float(self.matthewsCorrelation)

    def getfScore(self):
        """
        F-Score of the classifier where fScore = 2 * ((precision * recall) / (precision + recall)).

        Parameters: None.

        Returns:    F-score as a float.
        """
        return float(self.fScore)

    def getNegativePredictiveValue(self):
        """
        Negative predictive value of the classifier where negativePredictiveValue = (TN) / (FN + TN).

        Parameters: None.

        Returns:    npv as a float.
        """
        return float(self.negativePredictiveValue)

    def getKappa(self):
        """
        Cohen's Kappa of the classifier where,

        kappa = (totalAccuracy - randomAccuracy) / (1 - randomAccuracy)

        where,

        totalAccuracy = (TP + TN) / (TP + TN + FP + FN)

        and

        randomAccuracy = (TN + FP) * (TN + FN) + (FN + TP) * (FP + TP) / (Total*Total).

        Parameters: None.

        Returns:    kappa as a float.
        """
        return float(self.kappa)

    def getGMean(self):
        """
        G-mean of the classifier where gmean = sqrt( ( TP /( TP + FN ) ) * ( TN / ( TN + FP ) ) ).

        Parameters: None.

        Returns:    gmean as a float.
        """
        return float(self.gmean)

    def getAUROC(self):
        """
        Area under the roc curve of the classifier.

        Parameters: None.

        Returns:    auroc as a float.
        """
        return float(self.auroc)

    def setAUROC(self,auroc):
        """
        Sets the Area under the roc curve of the classifier.

        Parameters:

        auroc    -    the area under the roc curve calculated externally.

        Returns:    None.
        """
        self.auroc = auroc

    def getAUPRC(self):
        """
        Area under the precision-recall curve of the classifier.

        Parameters: None.

        Returns:    auroc as a float.
        """
        return float(self.auprc)

    def setAUPRC(self,auprc):
        """
        Sets the Area under the precision-recall curve of the classifier.

        Parameters:

        auprc    -    the area under the precision-recall curve calculated externally.

        Returns:    None.
        """
        self.auprc = auprc

    def getTP(self):
        """
        True positives (TP) returned by the classifier.

        Parameters: None.

        Returns:    true positives as an integer.
        """
        return int(self.TP)

    def getTN(self):
        """
        True negatives (TN) returned by the classifier.

        Parameters: None.

        Returns:    true negatives as an integer.
        """
        return int(self.TN)

    def getFP(self):
        """
        False positives (FP) returned by the classifier.

        Parameters: None.

        Returns:    false positives as an integer.
        """
        return int(self.FP)

    def getFN(self):
        """
        False negatives (FN) returned by the classifier.

        Parameters: None.

        Returns:    false negatives as an integer.
        """
        return int(self.FN)

    # ****************************************************************************************************