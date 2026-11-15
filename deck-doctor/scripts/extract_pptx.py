"""Print the text of every slide in a .pptx: number, title, body, speaker notes.

Usage: python extract_pptx.py deck.pptx
Needs python-pptx (pip install python-pptx).
"""
import sys

from pptx import Presentation


def slides(path):
    for n, slide in enumerate(Presentation(path).slides, 1):
        title_shape = slide.shapes.title
        title = title_shape.text_frame.text.strip() if title_shape is not None else ""
        body = []
        title_id = title_shape.shape_id if title_shape is not None else None
        for shape in slide.shapes:
            if shape.shape_id == title_id:  # python-pptx returns new proxies, so compare ids
                continue
            if shape.has_text_frame:
                body += [p.text.strip() for p in shape.text_frame.paragraphs if p.text.strip()]
            if shape.has_table:
                for row in shape.table.rows:
                    body.append(" | ".join(c.text.strip() for c in row.cells))
        notes = ""
        if slide.has_notes_slide:
            notes = slide.notes_slide.notes_text_frame.text.strip()
        yield n, title, body, notes


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python extract_pptx.py deck.pptx")
    sys.stdout.reconfigure(encoding="utf-8")  # Windows consoles default to cp1252 and mangle €
    for n, title, body, notes in slides(sys.argv[1]):
        print(f"--- Slide {n}: {title or '(no title)'}")
        for line in body:
            print(f"  {line}")
        if notes:
            print(f"  [notes] {notes}")
