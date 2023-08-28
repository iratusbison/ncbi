import requests
from django.shortcuts import render
'''
def literature_mining(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        if keyword:
            # Make API call to PubMed to search for articles related to the keyword
            url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
            params = {
                'db': 'pubmed',
                'term': keyword,
                'retmax': 10,  # Number of articles to retrieve
                'retmode': 'json'
            }
            response = requests.get(url, params=params)
            data = response.json()

            article_ids = data.get('esearchresult', {}).get('idlist', [])
            articles = []

            if article_ids:
                # Retrieve article details for each ID
                for article_id in article_ids:
                    summary_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi'
                    summary_params = {
                        'db': 'pubmed',
                        'id': article_id,
                        'retmode': 'json'
                    }
                    summary_response = requests.get(summary_url, params=summary_params)
                    summary_data = summary_response.json()
                    article = summary_data.get('result', {}).get(article_id, {})
                    articles.append({
                        'title': article.get('title', ''),
                        'authors': ', '.join(article.get('authors', [])),
                        'abstract': article.get('abstract', '')
                    })

            context = {'articles': articles, 'keyword': keyword}
            return render(request, 'results.html', context)

    return render(request, 'home.html')
'''
'''
from django.shortcuts import render

def literature_mining(request):
    articles = []
    keyword = ''

    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        if keyword:
            # Make API call to PubMed to search for articles related to the keyword
            url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
            params = {
                'db': 'pubmed',
                'term': keyword,
                'retmax': 10,  # Number of articles to retrieve
                'retmode': 'json'
            }
            response = requests.get(url, params=params)
            data = response.json()

            article_ids = data.get('esearchresult', {}).get('idlist', [])
            articles = []

            if article_ids:
                # Retrieve article details for each ID
                for article_id in article_ids:
                    summary_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi'
                    summary_params = {
                        'db': 'pubmed',
                        'id': article_id,
                        'retmode': 'json'
                    }
                    summary_response = requests.get(summary_url, params=summary_params)
                    summary_data = summary_response.json()
                    article = summary_data.get('result', {}).get(article_id, {})

                    # Ensure authors are formatted as strings in the list
                    authors = article.get('authors', [])
                    formatted_authors = [str(author) for author in authors]

                    articles.append({
                        'title': article.get('title', ''),
                        'authors': ', '.join(formatted_authors),
                        'abstract': article.get('abstract', '')
                    })

            context = {'articles': articles, 'keyword': keyword}
            return render(request, 'results.html', context)

    return render(request, 'home.html')
'''
from django.shortcuts import render
from .models import SearchInfo

def literature_mining(request):
    articles = []
    keyword = ''

    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        if keyword:
            # Make API call to PubMed to search for articles related to the keyword
            url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
            params = {
                'db': 'pubmed',
                'term': keyword,
                'retmax': 10,  # Number of articles to retrieve
                'retmode': 'json'
            }
            response = requests.get(url, params=params)
            data = response.json()

            article_ids = data.get('esearchresult', {}).get('idlist', [])
            articles = []

            if article_ids:
                # Retrieve article details for each ID
                for article_id in article_ids:
                    summary_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi'
                    summary_params = {
                        'db': 'pubmed',
                        'id': article_id,
                        'retmode': 'json'
                    }
                    summary_response = requests.get(summary_url, params=summary_params)
                    summary_data = summary_response.json()
                    article = summary_data.get('result', {}).get(article_id, {})

                    # Handle authors' names correctly
                    authors = article.get('authors', [])
                    formatted_authors = [author.get('name', '') for author in authors]

                    articles.append({
                        'title': article.get('title', ''),
                        'authors': ', '.join(formatted_authors),
                        'abstract': article.get('abstract', '')
                    })

            # Save the search information to the database
            num_results = len(articles)
            search_info = SearchInfo.objects.create(keyword=keyword, num_results=num_results)

            context = {'articles': articles, 'keyword': keyword, 'search_info': search_info}
            return render(request, 'results.html', context)

    return render(request, 'home.html')

