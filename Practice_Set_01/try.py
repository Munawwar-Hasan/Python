user_id = 25
region_id = 4

combined = (region_id << 8) | user_id

print("The value of var comabined is : ",combined)

print("The value of var user_id",user_id&0xFF,"The value of var region_id",combined>>8)