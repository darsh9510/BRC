import atexit, io, os, math, mmap

def main(input_file_name="testcase.txt", output_file_name="output.txt"):
    # Read file in 1e6 byte chunks while preserving full lines
    lines = []
    chunk_size = int(1e6)
    leftover = ""  # store any partial line from the previous chunk

    with open(input_file_name, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            # Decode the current chunk and prepend any leftover from previous chunk
            text = leftover + chunk.decode("utf-8", errors="ignore")
            # Split into lines; if the last line is incomplete, keep it in leftover
            parts = text.splitlines(keepends=True)
            if parts and not parts[-1].endswith("\n"):
                leftover = parts.pop()
            else:
                leftover = ""
            # Remove line-ending characters and add to our list of lines
            lines.extend(line.rstrip("\r\n") for line in parts)
    # Don't forget the leftover if there's any remaining data
    if leftover:
        lines.append(leftover.rstrip("\r\n"))

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
    order = {city: idx for idx, city in enumerate(cities)}
    stats = [[1000, -1000, 0, 0] for _ in range(len(cities))]

    for line in lines:
        parts = line.split(';')
        temp = float(parts[1])
        city = parts[0]
        idx = order[city]
        stats[idx][0] = min(stats[idx][0], temp)
        stats[idx][1] = max(stats[idx][1], temp)
        stats[idx][2] += temp
        stats[idx][3] += 1

    output = []
    for idx, city in enumerate(cities):
        if stats[idx][3] == 0:
            output.append(f"{city}=NaN/NaN/NaN\n")
            continue
        min_temp = stats[idx][0]
        max_temp = stats[idx][1]
        avg_temp = stats[idx][2] / stats[idx][3]
        avg_rounded = math.ceil(avg_temp * 10) / 10
        output.append(f"{city}={min_temp}/{avg_rounded}/{max_temp}\n")

    with open(output_file_name, 'w') as f:
        f.writelines(output)

if __name__ == "__main__":
    main()
