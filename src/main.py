import mmap
import math
import cProfile
def main(input_file_name="testcase.txt", output_file_name="output.txt"):
    city_values = {}

    with open(input_file_name, "r+b") as input_file:
        with mmap.mmap(input_file.fileno(), 0, access=mmap.ACCESS_READ) as mmapped_file:
            while True:
                line = mmapped_file.readline()
                if not line:
                    break
                parts = line.strip().split(b';')
                if len(parts) < 2:
                    continue
                city = parts[0].decode('utf-8')
                temp = float(parts[1])
                if city in city_values:
                    city_values[city].append(temp)
                else:
                    city_values[city] = [temp]
    output = []
    for city in sorted(city_values.keys()):
        values = city_values[city]
        total = math.fsum(values)
        count = len(values)
        avg_temp = total / count
        avg_rounded = math.ceil(avg_temp * 10) / 10
        min_temp = min(values)
        max_temp = max(values)
        output.append(f"{city}={min_temp}/{avg_rounded}/{max_temp}\n")

    with open(output_file_name, "w") as output_file:
        output_file.writelines(output)

if __name__ == "__main__":
    main()
    # cProfile.run('main()')