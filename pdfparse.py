import pdftotext

# with open('pdf-only-text.pdf', 'rb') as f:
# with open('sample-equation.pdf', 'rb') as f:
with open('pdf-visuals.pdf', 'rb') as f:
    pdf = pdftotext.PDF(f)



print(len(pdf))

for page in pdf:
    print(page)

print("\n\n".join(pdf))
