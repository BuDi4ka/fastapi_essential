

@app.get('/')
async def read_results():
    results = await some_library()
    return results


@app.get('/')
def results():
    results = some_library()
    return results



async def get_burgers(number: int):
    # Готовим бургеры по специальному асинхронному рецепту
    return number # return coroutines

@app.get('/burgers')
async def read_burgers():
    burgers = await get_burgers(2)
    return burgers