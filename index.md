## About PGPBgenes

The aim of the project is to empower researchers working with molecular biology to have a more user-friendly, flexible and controllable access under the NCBI Blast+ tool. To achieve this objective, a web interface was developed that communicates through a backend with the NCBI Blast+ program whose function is to perform comparisons between the genes provided by the user through a .fasta file and the sequences present in the database. Thus, returning information such as: % identity, Alignment length, Nº of mismatches, Gap openings, Q start, Q end, S start, Send, eValue, and Bit score for each gene provided by the user in the form of a human readable table.

### What is BLAST?

The Basic Local Alignment Search Tool (BLAST) is an algorithm for comparing primary biological sequence information.

The program compares nucleotide or amino-acid query sequences of DNA or RNA to sequence databases and directly approximates alignments that optimize a measure of local similarity, the maximal segment pair (MSP)score. It allows to filter the output, to infer functional and evolutionary relationships between sequences as well as help identify members of gene families. BLAST can also be used to realize motif searches, gene identification searches, to analyze multiple regions of similarity in long DNA sequences, to remove low-complexity region or sequence repeats in the query sequence, extend the exact matches to high-scoring segment pair (HSP) andevaluate the significance of the HSP score. In short, as The New York Times called, it is the Google of biological research.


### The database

Genes of agricultural importance were selected and, through a Genbank search, sequences of the genes nifH, gcd, apr, phoD pstS, pitA, phnX, ackA, epsB, gltA, mdh, ppc, chiA and acdS were collected.

| Gene | Nº of sequences |
|------|-----------------|
| acds | 516             |
| acka | 154             |
| esps | 17              |
| gdc  | 7               |
| glta | 3531            |
| mdh  | 511             |
| nifh | 6740            |
| phnx | 56              |
| phod | 1418            |
| pita | 482             |
| ppc  | 121             |
| pqq  | 39              |
| psts | 738             |



### Instalation

This project can be runned locally or using `Docker`. It is highly recommended to run on Docker to avoid any problems with dependencies or any other kind of conflict. To do so you will need:

1. [Install Docker](https://docs.docker.com/get-docker/)
2. Start Docker (if you're on Windows or Mac)
3. With a `terminal` or `cmd` open just run the following command: `docker run --name <CHOOSE_A_CONTAINER_NAME> -p 5000:5000 victormacedo996/pgpbgenes`
4. Open you favorite web browser (Chrome, Firefox, Edge, Brave, etc...) and on the URL type: `localhost:5000`
5. To stop the execution go back to your `terminal` or `cmd` and run the command: `docker container stop <CONTAINER_NAME>`
6. If you want to rerun the application run on your `terminal` or `cmd`: `docker container start <CONTAINER_NAME>`; then you can open you web browser and type on the URL: `localhost:5000`

If you realy want to run it locally I tested it on `Ubuntu 20.04` and must be installed `Python 3.8+` together with `pip` and `ncbi-blast+` software. Once you have the dependencies installed you will need to:

1. Clone this repository with `git clone https://github.com/victormacedo996/PGPBgenes`
2. Change to the project directory `cd PGPBgenes`
3. Create the database from the fasta file on the projects root directory and place it inside the `PGPBgenes/database/nucl` with `makeblastdb -in fasta_result.fasta -dbtype nucl -title fasta_result -out $PWD/PGPBgenes/database/nucl/fasta_result`. It is important to do not change the name `fasta_result`
4. Install the project dependencies with the command `pip install -r requirements.txt` (it is highly recommended to create a virtual envoiroment before this step)
5. To run the project you will need to execute the `run.py` file with the Python interpreter

## Citation

This service uses [NCBI Blast+ Application](https://blast.ncbi.nlm.nih.gov/Blast.cgi)

[Altschul SF, Gish W, Miller W, Myers EW, Lipman DJ. Basic local alignment search tool. J Mol Biol. 1990 Oct 5;215(3):403-10](https://doi.org/10.1016/S0022-2836(05)80360-2)
