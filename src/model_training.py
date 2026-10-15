from sklearn.svm import SVC

def train_svm(X, y):
    """
    Train a simple linear SVM.

    Parameters
    ----------
    X : ndarray
        Feature matrix from CSP.

    y : ndarray
        Labels corresponding to each trial.

    Returns
    -------
    model : SVC
        Trained SVM model.
    """

    model = SVC(kernel="linear")

    model.fit(X, y)

    return model