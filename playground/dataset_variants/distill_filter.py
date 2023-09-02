import argparse
import json


def gen_distill_data(filepath, output_file):
    with open(filepath, "r") as f:
        all_data = json.load(f)
    print(all_data[0].keys())

    distill_data = []
    for conv in all_data:
        if conv["model"] in ["claude-1", "claude-instant-1", "gpt-4", "claude-2"]:
            distill_data.append(conv)
    print("distill data size", len(distill_data))

    # models = set()
    # for conv in distill_data:
    #     models.add(conv["model"])
    # print(models)

    with open(output_file, "w") as f:
        json.dump(distill_data, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", type=str, default="clean_conv_20230809_1M.json")
    parser.add_argument("--output-file", type=str, default="distill.json")
    args = parser.parse_args()

    # distill_data = gen_distill_data(args.filepath, args.output_file)
    # upvote_data = gen_upvote_data()
