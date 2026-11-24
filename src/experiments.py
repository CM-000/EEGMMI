EXPERIMENTS = {

    "imagery_lr": {

        "description": "Imagined left vs right motor imagery",

        "subjects": [
            "S001",
            "S002",
            "S003",
            "S004",
            "S005"
        ],

        "runs": [
            "R04",
            "R08",
            "R12"
        ],

        "channels": [
            "C3",
            "CZ",
            "C4"
        ],

        "preprocessing": {

            "l_freq": 8.0,
            "h_freq": 30.0,

            "tmin": 0.0,
            "tmax": 1.0,

            "event_id": {
                "T1": 2,
                "T2": 3
            },

            "reject_bad_epochs": True
        },

        "feature_extraction": {

            "n_components": 3

        },

        "evaluation": {

            "test_size": 0.2,
            "random_state": 42,
            "cv": 5

        }
    }
}