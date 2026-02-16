import re
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def clean_text(s):
    s = re.sub(r"\x1B\[[0-9;]*[A-Za-z]", "", s)
    s = ''.join(ch for ch in s if 32 <= ord(ch) <= 126 or ch in '\n\r\t')
    return s

p1 = Path('bench_llama3.2.txt')
if p1.exists():
    t1 = clean_text(p1.read_text())
else:
    t1 = 'No output captured.'

p2 = Path('bench_llama3.txt')
if p2.exists() and p2.stat().st_size>0:
    t2 = clean_text(p2.read_text())
else:
    t2 = 'No output captured or run failed.'

c = canvas.Canvas('technical_report.pdf', pagesize=letter)
width, height = letter

c.setFont('Helvetica-Bold', 16)
c.drawString(40, height-50, 'Technical Report — AI-Powered GitHub Analysis (Updated Benchmarks)')

c.setFont('Helvetica', 11)
text = c.beginText(40, height-90)
text.textLine('Author: umeshrai01')
text.textLine('Date: 16 February 2026')
text.textLine('')
text.textLine('Model Benchmarking:')
text.textLine('Notes: Attempts were made to benchmark local Ollama models via CLI.')
text.textLine('Some runs produced outputs; timing metrics were not fully available due to')
text.textLine('local Ollama server issues (bind/address or service availability).')
text.textLine('')
text.textLine('Model: llama3.2')
text.textLine('Sample output (truncated):')
sample1 = t1.strip().replace('\n',' ')[:800]
text.textLine(sample1)
text.textLine('')
text.textLine('Model: llama3')
text.textLine('Sample output (truncated):')
sample2 = t2.strip().replace('\n',' ')[:800]
text.textLine(sample2)
text.textLine('')
text.textLine('Timing:')
text.textLine('- Wall-clock timings: Not available for all runs due to server connection issues.')
text.textLine('- Recommendation: run the following commands locally to capture exact timings:')
text.textLine('  /usr/bin/time -p ollama run llama3.2 "<PROMPT>" > out_llama3.2.txt 2>&1')
text.textLine('  /usr/bin/time -p ollama run phi-3-mini "<PROMPT>" > out_phi3.txt 2>&1')

c.drawText(text)
c.showPage()

c.setFont('Helvetica-Bold', 14)
c.drawString(40, height-50, 'Appendix — Full Captured Outputs (cleaned)')
text = c.beginText(40, height-90)
text.setFont('Helvetica', 9)
text.textLine('--- llama3.2 output ---')
for line in t1.strip().split('\n')[:120]:
    text.textLine(line[:120])
text.textLine('')
text.textLine('--- llama3 output ---')
for line in t2.strip().split('\n')[:120]:
    text.textLine(line[:120])

c.drawText(text)
c.save()
print('technical_report.pdf updated with available benchmarks')
