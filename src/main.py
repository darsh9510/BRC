def main(input_file_name = "testcase.txt", output_file_name = "output.txt"):
    input_file = open(input_file_name, "r")
    output_file = open(output_file_name, "w")

    # first_line = input_file.readline().strip()
    # first_line = first_line.split(";")

    cities = {}
    lines = [line.strip().split(";") for line in input_file]
    for i in lines:
        i[1]=round(float(i[1]),1)
        if i[0] in cities:
            val = cities[i[0]]
            temp = (min(val[0],i[1]),max(val[1],i[1]),val[2]+i[1],val[3]+1)
            cities[i[0]] = temp
        else:
            cities[i[0]] = (i[1],i[1],i[1],1)
    cities = dict(sorted(cities.items()))
    for i,j in cities.items():
        mn = j[2]/j[3]
        temp = mn*10
        temp_int = int(temp)
        rem = temp - float(temp_int)
        if rem>0:
            temp+=1
        temp=int(temp)
        temp/=10
        # 0.33606522205535294 - multi by 1e6 or smth
        # 0.33606522205535294 - by 1e8 ig
        # 0.336065222055353 - none
        output_file.write(f"{i}={j[0]}/{temp}/{j[1]}\n")

    output_file.close()
    input_file.close()

if __name__ == "__main__":
    main()