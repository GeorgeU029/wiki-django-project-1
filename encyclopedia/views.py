from django.shortcuts import render, redirect
from django.urls import reverse
import markdown
from . import util
from django.core.files.storage import default_storage


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,title):
    article = util.get_entry(title)
    context = {}
    if article: 
        html_content = markdown.markdown(article)
        return render(request, "encyclopedia/entry.html", {
            "title" : title,
            "content" : html_content
        })
    else:
        return render(request,"encyclopedia/error.html",{
            "message" : f"The article '{title}' was not found"
        }
        )
def search(request):
    query = request.GET.get("q","")

    entries = util.list_entries()

    for entry in entries:
        if entry.lower() == query.lower():
            return redirect(reverse("title", kwargs ={"title" : entry}))
    matching_entries = []
    for entry in entries:
        if entry.lower() in query.lower():
            matching_entries.append(entry)
    return render(
        request,"encyclopedia/search_results.html",
        {
            "query" : query,
            "entries" : matching_entries
        }
    )



