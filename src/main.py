import mmap
import math
import cProfile
def main(input_file_name = "testcase.txt", output_file_name = "output.txt"):
    city_stats = {}
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
                if city in city_stats:
                    min_temp, max_temp, total_temp, count = city_stats[city]
                    min_temp = min(min_temp, temp)
                    max_temp = max(max_temp, temp)
                    total_temp += temp
                    count += 1
                    city_stats[city] = (min_temp, max_temp, total_temp, count)
                else:
                    city_stats[city] = (temp, temp, temp, 1)
    output = []
    for city in sorted(city_stats.keys()):
        min_temp, max_temp, total_temp, count = city_stats[city]
        avg_temp = total_temp / count
        avg_rounded = math.ceil(avg_temp * 10) / 10
        output.append(f"{city}={min_temp}/{avg_rounded}/{max_temp}\n")

    with open(output_file_name, "w") as output_file:
        output_file.writelines(output)

if __name__ == "__main__":
    main()
    # cProfile.run('main()')