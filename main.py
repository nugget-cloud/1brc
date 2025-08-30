import asyncio
import time
import pprint
from multiprocessing import Process

FILE_PATH = "data/measurements.txt"
city = {} 

async def calculate(val:dict):
    for key , value in val.items():
        val[key]=[min(val[key]) , sum(val[key])/len(val[key]) , max(val[key])]
    return val
    
async def row_wise():
    async for chunk in read_file():
        for row in chunk:
            first_item, second_item = row.split(";")
            if first_item in city:
                city[first_item].append(float(second_item))
            else:
                city[first_item] = [float(second_item)]  
    
    return city
    
async def read_file():
    with open(FILE_PATH , 'r') as file:
        while True:
            chunk = file.readlines(1_00_000)
            if not chunk:
                break
            yield chunk
    
async def main():
    start_time = time.perf_counter()
    pprint.pprint(f"The calculation starts now {start_time}")
    result = Process(target=row_wise)
    pprint.pprint("Row wise calculation done")
    result =  await calculate(result)
    end_time = time.perf_counter()
    print(end_time - start_time)
     
asyncio.run(main())
