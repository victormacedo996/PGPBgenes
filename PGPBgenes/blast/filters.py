from PGPBgenes.main.routes import main


@main.app_template_filter()
def fasta_link_template_formater(gene_id):
    if ':' in gene_id:
        gene_id = gene_id.split(':')
        begin, end = gene_id[1].split('-')
        end = end.split('$')[0]
        link = f'https://www.ncbi.nlm.nih.gov/nuccore/{gene_id[0]}?from={begin}&to={end}&report=fasta'
        return link
    else:
        if '$' in gene_id:
            gene_id = gene_id.split("$")[0]
            link = f'https://www.ncbi.nlm.nih.gov/nuccore/{gene_id}?report=fasta'
            return link
        else:
            link = f'https://www.ncbi.nlm.nih.gov/nuccore/{gene_id}?report=fasta'
            return link