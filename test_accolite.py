print("Hello World...")
import asyncio

# class AsyncClass:
#     async def task_one(self):
#         print("Task One: Start")
#         await asyncio.sleep(2)  # Simulate I/O operation
#         print("Task One: End")
#
#     async def task_two(self):
#         print("Task Two: Start")
#         await asyncio.sleep(1)  # Simulate I/O operation
#         print("Task Two: End")
#
#     async def run_tasks(self):
#         print("Running tasks asynchronously:")
#         await asyncio.gather(self.task_one(), self.task_two())
#
# # Create an instance of the class
# async_class_instance = AsyncClass()
#
# # Run the asynchronous tasks
# asyncio.run(async_class_instance.run_tasks())

tup = (1,2,3)
print(type(tup))
set_ex = {1,2,3}
print(type(set_ex))
a = [1,2,3]
b=[3,4,5]
print(a+b)


#print(zip(a,b))
for i in zip(a,b):
    for j in i:
        print(j)

z = zip(a,b)
lc = [val[0] for val in z]
print(lc)


