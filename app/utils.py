async def streamer(response):
    # Generate a CSV file as a stream
    await response.write('alpha,')
    await response.write('bravo')
