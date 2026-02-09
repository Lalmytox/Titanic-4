from __future__ import annotations

import argparse

from src.data_preprocessing import load_data, make_features
from src.model_evaluation import predict, save_submission
from src.model_training import train_model


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Titanic end-to-end pipeline")
    parser.add_argument("--train-path", default="data/train.csv")
    parser.add_argument("--test-path", default="data/test.csv")
    parser.add_argument("--output-path", default="submission.csv")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    train_df, test_df = load_data(args.train_path, args.test_path)
    x, y, x_test, passenger_id = make_features(train_df, test_df)

    model = train_model(x, y)
    predictions = predict(model, x_test)

    save_submission(passenger_id, predictions, args.output_path)
    print(f"Saved submission to: {args.output_path}")


if __name__ == "__main__":
    main()
