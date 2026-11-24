from pathlib import Path

line = "Kancing baju itu menggelinding ke bawah lemari; dari gelap, terdengar kancing lain menjawab."
output = Path("/output")
if not output.is_dir():
    output = Path(__file__).parent / "output"
output.mkdir(parents=True, exist_ok=True)
(output / "entry.txt").write_text(line + "\n", encoding="utf-8")
