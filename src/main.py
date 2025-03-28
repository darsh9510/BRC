import mmap
import math
import cProfile
import io
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
    "Valsad", "Vapi", "Varanasi", "Vasai-Virar", "Vellore", "Vijayawada", "Visakhapatnam", "Warangal", "Wardha", "Yavatmal"]
    city_values = {}
    for city in cities:
        city_values[city]=[]
    with open(input_file_name, "r+b") as input_file:
        with mmap.mmap(input_file.fileno(), 0, access=mmap.ACCESS_READ) as mmapped_file:
            data = mmapped_file.read()
    lines = data.split(b'\n')
    for line in lines:
        if not line:
            continue
        before, sep, after = line.partition(b';')
        if sep != b';':
            continue
        try:
            city = before.decode('utf-8')
            temp = float(after)
        except (ValueError, UnicodeDecodeError):
            continue
        if city in city_values:
            city_values[city].append(temp)
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

    with open(output_file_name, "wb") as output_file:
        buffered_writer = io.BufferedWriter(output_file, buffer_size=1024*1024)
        for line in output:
            buffered_writer.write(line.encode('utf-8'))
        buffered_writer.flush()

if __name__ == "__main__":
    main()
    # cProfile.run('main()')