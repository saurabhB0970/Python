movies_db2022 = {
    "Gangubai Kathiawadi": ["Alia Bhatt", 'Vijay Raaz', 'Seema Pahwa'],
    "Bhool Bhulaiyaa 2": [" Kartik Aaryan", "Kiara Advani","Rajpal Yadav"]

}
movies_db2023 = {
    "Sam Bahadur": ["Vicky Kaushal", "Fatima Sana Shaikh", "Sanya Malhotra"],
    "Gadar 2": ["Sunny Deol",'Ameesha Patel', "Utkarsh Sharma"]
}
movies_db2024 = {
    "Bade Miyan Chote Miyan": ["Akshay Kumar", "Tiger Shroff", "Prithviraj Sukumaran"],
    "Chhaava": [" Vicky Kaushal", "Akshaye Khanna", "Rashmika Mandanna"]
}
movies_db2025 = {
    "Alpha": ["Alia Bhatt, Sharvari Wagh"],

    "Housefull 5": ["Akshay Kumar", "Abhishek Bachchan ","Riteish Deshmukh",'Jacqueline Fernandez','Sonam Bajwa' ]
}

big_db = {
    "2022": movies_db2022,
    "2023": movies_db2023,
    "2024": movies_db2024,
    "2025": movies_db2025
}

for year, movies in big_db.items():
    print(f"\nMovies released in {year}:")
    for movie, cast in movies.items():
        print(f"  {movie}: Cast - {', '.join(cast)}")
    

print(movies_db2025["Housefull 5"][3])

Output:
Movies released in 2022:
  Gangubai Kathiawadi: Cast - Alia Bhatt, Vijay Raaz, Seema Pahwa     
  Bhool Bhulaiyaa 2: Cast -  Kartik Aaryan, Kiara Advani, Rajpal Yadav

Movies released in 2023:
  Sam Bahadur: Cast - Vicky Kaushal, Fatima Sana Shaikh, Sanya Malhotra
  Gadar 2: Cast - Sunny Deol, Ameesha Patel, Utkarsh Sharma

Movies released in 2024:
  Bade Miyan Chote Miyan: Cast - Akshay Kumar, Tiger Shroff, Prithviraj Sukumaran
  Chhaava: Cast -  Vicky Kaushal, Akshaye Khanna, Rashmika Mandanna

Movies released in 2025:
  Alpha: Cast - Alia Bhatt, Sharvari Wagh
  Housefull 5: Cast - Akshay Kumar, Abhishek Bachchan , Riteish Deshmukh, Jacqueline Fernandez, Sonam Bajwa
Jacqueline Fernandez
PS C:\Users\HP\Desktop\Python JBK\Day7> 
