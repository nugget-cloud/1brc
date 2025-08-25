import asyncio
import time
import pprint

city = {} 

async def calculate(val:dict):
    for key , value in val.items():
        val[key]=[min(val[key]) , sum(val[key])/len(val[key]) , max(val[key])]
    pprint.pprint(val) 
    return val
    
async def row_wise():
    file = await read_file("data/measurements.txt")
    for row in file:
        first_item, second_item = row.split(";")
        if first_item in city:
            city[first_item].append(float(second_item))
        else:
            city[first_item] = [float(second_item)]  
    
    pprint.pprint(city)
    return city
    
async def read_file(file_path:str):
    with open(file_path , 'r') as file:
        content = file.readlines()
        return content
    
async def main():
    start_time = time.perf_counter()
    pprint.pprint("The calculation starts now")
    result = await row_wise()
    pprint.pprint("Row wise calculation done")
    result =  await calculate(result)
    end_time = time.perf_counter()
    print(end_time - start_time)
     
asyncio.run(main())
