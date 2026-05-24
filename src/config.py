from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Change these paths to point to your data files
RAW_PATH = ROOT / "data" / "raw"
EP_RAW = "EP.txt"
IN_RAW = "IN.txt"
MU_RAW = "MU.txt"
MW_RAW = "MW.txt"

CSV_RAWS = []

OUT_PATH = ROOT / "data" / "processed"