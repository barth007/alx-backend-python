import asyncio

async def main():
    host = 'example.com'
    port = 80

    reader, writer = await asyncio.open_connection(host, port)

    writer.write(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
    await writer.drain()

    data = await reader.read(100)
    print(data.decode())

    writer.close()
    await writer.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())

