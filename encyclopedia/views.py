from django.shortcuts import render
import markdown
from . import util


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
