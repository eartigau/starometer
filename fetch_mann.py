import urllib.request, io, tarfile

url = 'https://arxiv.org/e-print/1501.01635'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=30) as r:
    data = r.read()

tf = tarfile.open(fileobj=io.BytesIO(data))
content = tf.extractfile('main.tex').read().decode('latin-1')

# Find the teffcolor table definition
idx = content.find('label{tab:teffcolor')
if idx > 0:
    print(content[max(0,idx-3000):idx+3000])
else:
    # Search for all table environments near 'Teff' or 'teff'
    for search_term in ['teffcolor', 'tab:tcolor', 'eqn:teff3', 'Equation~']:
        idx2 = content.find(search_term)
        if idx2 > 0:
            print(f"=== '{search_term}' at {idx2} ===")
            print(content[max(0,idx2-200):idx2+3000])
            break
