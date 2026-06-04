import fitz  # pymupdf
import os

pdf_path = "/ai-inventor/aii_data/runs/run_PJcQ6RjRK3Db/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.pdf"
out_dir = "/ai-inventor/aii_data/runs/run_PJcQ6RjRK3Db/4_gen_paper_repo/_4_assemble_paper/paper/workspace/page_imgs"
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")
for i, page in enumerate(doc):
    mat = fitz.Matrix(150/72, 150/72)
    pix = page.get_pixmap(matrix=mat)
    pix.save(f"{out_dir}/page_{i+1:02d}.png")
    print(f"Saved page {i+1}")
print("Done")
