import http.client

if __name__ == "__main__":

    conn = http.client.HTTPSConnection("indianstockexchange.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "8f1e26dc6bmsh1d9190aab19b7b0p149803jsnbca5eb89028d",
        'X-RapidAPI-Host': "indianstockexchange.p.rapidapi.com"
    }

    conn.request("GET", "/index.php?id=%7Bscrip-id%7D", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
