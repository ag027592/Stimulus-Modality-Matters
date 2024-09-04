import argparse

parser = argparse.ArgumentParser(description="Parse accuracy values from a text file")
parser.add_argument(
    "--input_file", default="None", type=str, help="Path to the input text file"
)
args = parser.parse_args()


with open(args.input_file, "r") as file:
    acc = []
    for line in file:
        if line.startswith("test acc:"):
            accuracy = float(line.split(":")[1].strip())
            acc.append(accuracy)

            if (len(acc) == 4):
                print("\t".join(map(str, acc)))
                acc = []