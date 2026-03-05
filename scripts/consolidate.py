import csv
from pathlib import Path


def avgpop(row):
    total = 0.0
    count = 0
    for col in row[2:]:
        if col:
            count += 1
            total += float(col)
    return total / count if count else None


def main():
    data_path = Path(__file__).resolve().parents[1] / "data" / "population.csv"
    with data_path.open(newline="", encoding="utf-8") as infile:
        rows = list(csv.reader(infile))

    outrows = []
    for idx, row in enumerate(rows):
        if idx != 0:
            value = avgpop(row)
            row[1] = "" if value is None else str(value)
        outrows.append(row)

    with data_path.open("w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerows(outrows)


if __name__ == "__main__":
    main()
