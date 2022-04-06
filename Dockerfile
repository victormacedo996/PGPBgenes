FROM ubuntu:20.04
RUN apt-get update && apt-get upgrade -y
RUN apt-get install software-properties-common -y
RUN add-apt-repository --yes ppa:deadsnakes/ppa
RUN apt-get install python3.10 -y
RUN apt-get install python3-pip -y
RUN apt-get install ncbi-blast+ -y
COPY . ./app
WORKDIR ./app
RUN makeblastdb -in fasta_result.fasta -dbtype nucl -title fasta_result -out /app/PGPBgenes/database/nucl/fasta_result
RUN rm fasta_result.fasta
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["run.py"]