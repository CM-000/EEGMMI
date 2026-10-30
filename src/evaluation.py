from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)

def evaluate_model(
    model,
    X,
    y,
    test_size=0.2,
    random_state=42,
    cv=5
):
    """
    Evaluate a trained model using both:
    - Train/test split accuracy
    - Cross-validation accuracy

    Returns
    -------
    results : dict
        Dictionary containing evaluation metrics.
    """

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )

    model.fit(X_train, y_train)

    test_accuracy = model.score(X_test, y_test)

    # Cross-validation
    cv_scores = cross_val_score(
        model,
        X,
        y,
        cv=cv
    )

    return {
        "test_accuracy": test_accuracy,
        "cv_scores": cv_scores,
        "cv_mean": cv_scores.mean()
    }