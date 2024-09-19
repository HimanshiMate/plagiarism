from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Document
from .forms import DocumentForm
from .models import PlagiarismResult
from .utils import calculate_similarity


def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            # You can trigger text extraction here
            return JsonResponse({'message': 'File uploaded successfully'})
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})



def compare_texts(document_id, comparison_text):
    document = Document.objects.get(id=document_id)
    similarity = calculate_similarity(document.text, comparison_text)
    PlagiarismResult.objects.create(
        document=document,
        similarity_score=similarity,
        compared_with=comparison_text
    )

