from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
# Change these paths to point to your data files
RAW_PATH = ROOT / "data" / "raw"
EP_RAW = "EP.txt"
IN_RAW = "IN.txt"
MU_RAW = "MU.txt"
MW_RAW = "MW.txt"

CSV_RAWS = []

OUT_PATH = DATA / "processed"
GRAPHS = DATA / "saved_graphs"