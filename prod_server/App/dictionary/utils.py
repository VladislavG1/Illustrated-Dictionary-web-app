

from dictionary.models import Word


def q_search(query):
    if query.isdigit():
        return Word.objects.filter(pk=int(query))