import sys
import os
from pathlib import Path

# Ensure Tcl/Tk paths are set for test runner
tcl_dir = Path(sys.base_prefix) / "tcl"
if tcl_dir.exists():
    tcl_86 = tcl_dir / "tcl8.6"
    tk_86 = tcl_dir / "tk8.6"
    if tcl_86.exists():
        os.environ["TCL_LIBRARY"] = str(tcl_86)
    if tk_86.exists():
        os.environ["TK_LIBRARY"] = str(tk_86)
