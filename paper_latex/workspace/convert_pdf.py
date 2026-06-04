import fitz
import os

pdf_path = "/ai-inventor/aii_data/runs/run_PJcQ6RjRK3Db/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.pdf"
out_dir = "/ai-inventor/aii_data/runs/run_PJcQ6RjRK3Db/4_gen_paper_repo/_4_assemble_paper/paper/workspace"

doc = fitz.open(pdf_path)
for i, page in enumerate(doc):
    mat = fitz.Matrix(150/72, 150/72)
    pix = page.get_pixmap(matrix=mat)
    path = os.path.join(out_dir, f"page-{i+1:02d}.png")
    pix.save(path)
    print(f"Saved {path}")
print(f"Total pages: {len(doc)}")
