from pathlib import Path
import json
import nbformat
from nbclient import NotebookClient
folder=Path(__file__).resolve().parent
source=folder/'Fashion_MNIST_Completed.ipynb'
nb=nbformat.read(source,as_version=4)
print('Executing',source,flush=True)
client=NotebookClient(nb,timeout=1800,kernel_name='python3',resources={'metadata':{'path':str(folder)}})
try:
    client.execute()
finally:
    nbformat.write(nb,source)
errors=[(i,o.get('ename'),o.get('evalue')) for i,c in enumerate(nb.cells) if c.cell_type=='code' for o in c.get('outputs',[]) if o.output_type=='error']
counts=[c.execution_count for c in nb.cells if c.cell_type=='code']
print('Execution counts:',counts,'Errors:',errors,flush=True)
if errors: raise RuntimeError(errors)
print((folder/'fashion_outputs'/'execution_metrics.json').read_text(),flush=True)
