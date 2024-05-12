from doctest import debug
from lossless_compression import lossless_compression
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.post("/compress")
def compress(message: str):
    return lossless_compression(message.replace(" ", ""))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000, loop="uvloop")


# # Get input from the user
# message = input("Enter the message to be encoded: ")
# print()

# # Perform lossless compression
# results= lossless_compression(message)

# # Print results
# for algorithm, result in results.items():
#     try:
#         print("\nResults for", algorithm)
#         for key, value in result.items():
#             print(key + ":", value)
#     except:
#         continue

# # Find the algorithm with the best compression ratio
# print("Best compression achieved by:", results['best_algorithm'])
