def main(input_file_name = "testcase.txt", output_file_name = "output.txt"):
    input_file = open(input_file_name, "r")
    output_file = open(output_file_name, "w")

    # first_line = input_file.readline().strip()
    # first_line = first_line.split(";")

    lines = input_file.readlines()
    # cities = {}
    # for i in lines:
    #     i = i.split(";")
    #     i[1]=round(float(i[1]),1)
    #     if i[0] in cities:
    #         val = cities[i[0]]
    #         temp = (min(val[0],i[1]),max(val[1],i[1]),val[2]+i[1],val[3]+1)
    #         cities[i[0]] = temp
    #     else:
    #         cities[i[0]] = (i[1],i[1],i[1],1)
    # cities = dict(sorted(cities.items()))
    # for i,j in cities.items():
    #     mn = j[2]/j[3]
    #     temp = mn*10
    #     temp_int = int(temp)
    #     rem = temp - float(temp_int)
    #     if rem>0:
    #         temp+=1
    #     temp=int(temp)
    #     temp/=10
    #     output_file.write(f"{i}={j[0]}/{temp}/{j[1]}\n")
    # lines = [line.split(";") for line in lines]
    # cities = set()
    cities = [
        "Adoni", "Agartala", "Agra", "Ahmedabad", "Aizawl", "Ajmer", "Akola", "Aligarh", "Allahabad", "Ambala",
        "Ambattur", "Amravati", "Amreli", "Amritsar", "Anand", "Arrah", "Asansol", "Aurangabad", "Bally", "Bangalore",
        "Bareilly", "Begusarai", "Belagavi", "Bhagalpur", "Bharatpur", "Bhavnagar", "Bhilai", "Bhimavaram", "Bhiwandi",
        "Bhiwani", "Bhopal", "Bhosari", "Bhubaneswar", "Bhuj", "Bhusawal", "Bidar", "Bijapur", "Bikaner", "Bilaspur",
        "Bokaro", "Burhanpur", "Chandigarh", "Chandrapur", "Chennai", "Chhapra", "Chhindwara", "Chikkamagaluru", "Chittoor",
        "Chutia", "Coimbatore", "Cumbum", "Cuttack", "Dahod", "Daltonganj", "Daman", "Darbhanga", "Davanagere", "Dehradun",
        "Delhi", "Dewas", "Dhanbad", "Dibrugarh", "Dindigul", "Durgapur", "Erode", "Faridabad", "Firozabad", "Gali-Makhian-Wali",
        "Gandhidham", "Gangtok", "Gaya", "Ghaziabad", "Giridih", "Godhra", "Gondia", "Gopalganj", "Gopalpur", "Gorakhpur",
        "Gulbarga", "Guntur", "Guwahati", "Gwalior", "Hajipur", "Hazaribagh", "Himatnagar", "Hingoli", "Hospet", "Hosur",
        "Howrah", "Hubballi-Dharwad", "Hyderabad", "Imphal", "Indore", "Itanagar", "Jabalpur", "Jaipur", "Jalgaon", "Jammu",
        "Jamnagar", "Jamshedpur", "Jhansi", "Jodhpur", "Junagadh", "Kakinada", "Kalyan-Dombivli", "Kanpur", "Karaikal", "Karwar",
        "Katihar", "Kavaratti", "Kochi", "Kohima", "Kolhapur", "Kolkata", "Kollam", "Korba", "Kota", "Kotha", "Kozhikode",
        "Kundara", "Kurnool", "Kutta", "LaiLunga", "Loni", "Lucknow", "Ludhiana", "Lula-Ahir", "Lulla-Nagar", "Machilipatnam",
        "Madurai", "Maheshtala", "Malegaon", "Mangalore", "Mapusa", "Margao", "Mathura", "Meerut", "Mehsana", "Moradabad",
        "Morbi", "Mumbai", "Munger", "Muzaffarnagar", "Muzaffarpur", "Mysore", "Nagpur", "Nanded", "Nashik", "Navi-Mumbai",
        "Navsari", "Nellore", "Nizamabad", "North-Dumdum", "Ongole", "Palanpur", "Panaji", "Panipat", "Parbhani", "Patiala",
        "Patna", "Porbandar", "Port-Blair", "Porvorim", "Proddatur", "Pune", "Purnia", "Raichur", "Raipur", "Rajahmundry",
        "Rajkot", "Ranchi", "Ratlam", "Rewa", "Rohtak", "Rourkela", "Sagar", "Saharanpur", "Salem", "Samastipur",
        "Sangli-Miraj-&-Kupwad", "Sasaram", "Satna", "Shahjahanpur", "Shillong", "Shimoga", "Sikar", "Siliguri", "Silvassa",
        "Sirsa", "Siwan", "Solapur", "South Dumdum", "Srinagar", "Surendranagar", "Tatti-Khana", "Tezpur", "Thane",
        "Tiruchirappalli", "Tirunelveli", "Tiruppur", "Tiruvannamalai", "Tumkur", "Udaipur", "Ujjain", "Ulhasnagar", "Vadodara",
        "Valsad", "Vapi", "Varanasi", "Vasai-Virar", "Vellore", "Vijayawada", "Visakhapatnam", "Warangal", "Wardha", "Yavatmal"
    ]
    # for i in lines:
    #     i = i.split(";")
    #     cities.add(i[0])
    # cities = sorted(cities)
    order = {}
    c=0
    for i in cities:
        order[i]=c
        c+=1
    stats = []
    for i in range(len(order)):
        temp = [1000,-1000,0,0]
        stats.append(temp)
    for i in lines:
        i = i.split(";")
        i[1]=float(i[1])
        # output_file.write(f"{i[0]}={i[1]}/{i[1]}/{i[1]}\n")
        idx = order[i[0]]
        # if stats[idx][0]>i[1]:
        #     stats[idx][0]=i[1]
        # if stats[idx][1]<i[1]:
        #     stats[idx][1]=i[1]
        stats[idx][0]=min(stats[idx][0],i[1])
        stats[idx][1]=max(stats[idx][1],i[1])
        stats[idx][2]+=i[1]
        stats[idx][3]+=1
        # output_file.write(f"{i[0]}={i[1]}/{i[1]}/{i[1]}\n")
    c=0
    for j in range(len(stats)):
        i = stats[j]
        mn = i[2]/i[3]
        # mn = 135
        temp = mn*10
        temp_int = int(temp)
        rem = temp - float(temp_int)
        if rem>0:
            temp+=1
        temp=int(temp)
        temp/=10
        output_file.write(f"{list(cities)[j]}={i[0]}/{temp}/{i[1]}\n")
    # for i in range(c):
    #     output_file.write(f"{list(cities)[i]}={c}/{len(cities)}/{len(order)}\n")
    # for i in lines:
    #     i[1]=round(float(i[1]),1)
    #     if i[0] in cities:
    #         val = cities[i[0]]
    #         temp = (min(val[0],i[1]),max(val[1],i[1]),val[2]+i[1],val[3]+1)
    #         cities[i[0]] = temp
    #     else:
    #         cities[i[0]] = (i[1],i[1],i[1],1)
    # cities = dict(sorted(cities.items()))
    # for i,j in cities.items():
    #     mn = j[2]/j[3]
    #     temp = mn*10
    #     temp_int = int(temp)
    #     rem = temp - float(temp_int)
    #     if rem>0:
    #         temp+=1
    #     temp=int(temp)
    #     temp/=10
    #     output_file.write(f"{i}={j[0]}/{temp}/{j[1]}\n")

    output_file.close()
    input_file.close()

if __name__ == "__main__":
    main()