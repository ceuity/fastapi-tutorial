from fastapi import Depends, FastAPI

app = FastAPI()


def generate_dep_a():
    print("a")
    return "a"


def generate_dep_b():
    print("b")
    return "b"


def generate_dep_c():
    print("c")
    return "c"


async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        print("dep_a.close()")
        # dep_a.close()


async def dependency_b(dep_a=Depends(dependency_a)):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        print("dep_b.close()")
        # dep_b.close(dep_a)


async def dependency_c(dep_b=Depends(dependency_b)):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        print("dep_c.close()")
        # dep_c.close(dep_b)


@app.get("/")
async def get_main(common: str = Depends(dependency_c)):
    return {"message": common}
