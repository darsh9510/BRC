import os
import math
from concurrent.futures import ThreadPoolExecutor, as_completed

def load_chunk(file_name, start, end, file_size):
    with open(file_name, "rb") as f:
        f.seek(start)
        data = f.read(end - start)
        if end < file_size:
            data += f.readline()
        if start != 0:
            newline_index = data.find(b'\n')
            if newline_index != -1:
                data = data[newline_index+1:]
    return data.decode("utf-8", errors="ignore").splitlines()

def process_batch(lines, order, num_cities):
    stats = [[1000, -1000, 0, 0] for _ in range(num_cities)]
    for line in lines:
        parts = line.rstrip("\r\n").split(";")
        if len(parts) < 2:
            continue
        city = parts[0]
        try:
            temp = float(parts[1])
        except ValueError:
            continue
        idx = order.get(city)
        if idx is None:
            continue
        stats[idx][0] = min(stats[idx][0], temp)
        stats[idx][1] = max(stats[idx][1], temp)
        stats[idx][2] += temp
        stats[idx][3] += 1
    return stats

def main(input_file_name="testcase.txt", output_file_name="output.txt"):
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
    num_cities = len(cities)
    
    file_size = os.path.getsize(input_file_name)
    chunk_size = int(1e6)
    
    boundaries = []
    for start in range(0, file_size, chunk_size):
        end = min(start + chunk_size, file_size)
        boundaries.append((start, end))
    
    chunks_results = [None] * len(boundaries)
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(load_chunk, input_file_name, start, end, file_size): i
                   for i, (start, end) in enumerate(boundaries)}
        for future in as_completed(futures):
            idx = futures[future]
            chunks_results[idx] = future.result()
    
    lines = []
    for chunk in chunks_results:
        lines.extend(chunk)
    
    batch_size = 100000
    batches = [lines[i:i+batch_size] for i in range(0, len(lines), batch_size)]
    
    overall_stats = [[1000, -1000, 0, 0] for _ in range(num_cities)]
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(process_batch, batch, order, num_cities) for batch in batches]
        for future in as_completed(futures):
            batch_stats = future.result()
            for i in range(num_cities):
                overall_stats[i][0] = min(overall_stats[i][0], batch_stats[i][0])
                overall_stats[i][1] = max(overall_stats[i][1], batch_stats[i][1])
                overall_stats[i][2] += batch_stats[i][2]
                overall_stats[i][3] += batch_stats[i][3]
    
    output = []
    for idx, city in enumerate(cities):
        if overall_stats[idx][3] == 0:
            output.append(f"{city}=NaN/NaN/NaN\n")
        else:
            min_temp = overall_stats[idx][0]
            max_temp = overall_stats[idx][1]
            avg_temp = overall_stats[idx][2] / overall_stats[idx][3]
            avg_rounded = math.ceil(avg_temp * 10) / 10
            output.append(f"{city}={min_temp}/{avg_rounded}/{max_temp}\n")
    
    with open(output_file_name, "w") as f:
        f.writelines(output)

if __name__ == "__main__":
    main()
