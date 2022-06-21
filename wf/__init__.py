"""
Scan contig files against traditional PubMLST typing schemes
"""

import subprocess
from pathlib import Path

from latch import small_task, workflow
from latch.types import LatchFile, LatchDir


@small_task
def mlst_task(fasta_file: LatchFile, out_dir: LatchDir)-> LatchDir:

    # defining the subprocess
    mlst_cmd=[
        "mlst",
        str(fasta_file),
    ]
    subprocess.run(mlst_cmd)
    return file_glob(*.tsv, out_dir.remote_path)


@workflow
def mlst(fasta_file: LatchFile, out_dir:LatchDir) -> LatchDir:
    """Scan contig files against traditional PubMLST typing schemes

    _MLST_
    ----

    __metadata__:
        display_name: Scan contig files against traditional PubMLST typing schemes

        author:
            name: Geodette

            email: steveodettegeorge@gmail.com

            github:
        repository:

        license:
            id: MIT

    Args:

        fasta_file:
          Fasta file to be proccessed

          __metadata__:
            display_name: Fasta File

        out_dir:
          Output directory

          __metadata__:
            display_name: Output directory


    """

    return mlst_task(fasta_file=fasta_file, out_dir=out_dir)
