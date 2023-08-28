# gene_sequence_app/views.py
from django.shortcuts import render
import requests
import json

def retrieve_gene_sequences(request):
    if request.method == 'POST':
        gene_name = request.POST.get('gene_name', '')

        # NCBI API URL to retrieve gene sequences
        ncbi_url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id={gene_name}&rettype=fasta&retmode=text'
        
        # PubMed API URL to retrieve gene-related articles
        pubmed_url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={gene_name}&retmode=json'

        # Fetch gene sequences from NCBI
        response_ncbi = requests.get(ncbi_url)
        gene_sequence = response_ncbi.text if response_ncbi.status_code == 200 else None

        # Fetch gene-related articles from PubMed
        response_pubmed = requests.get(pubmed_url)
        articles_data = response_pubmed.json() if response_pubmed.status_code == 200 else None

        return render(request, 'gene_sequence.html', {'gene_sequence': gene_sequence, 'articles_data': articles_data})

    return render(request, 'gene_sequence.html')
