from bs4 import BeautifulSoup

html = "<html><body><h1>Hello, World!</h1></body></html>"

soup = BeautifulSoup (html, "html.parser")

print (soup.h1.text)




htmlTable = """<table>
    <tr><th>Nome</th><th>Idade</th></tr>
    <tr><td>João</td><td>20</td></tr>
    <tr><td>Ana</td><td>22</td></tr>
</table>"""

soup = BeautifulSoup(htmlTable, "html.parser")
table = soup.find("table")

for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    print(f"Nome: {cols[0].text}, Idade: {cols[1].text}")