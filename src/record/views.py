from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, DetailView

from .forms import DocumentUploadForm, Document
from utils.helper_functions import generate_id
from .models import Document, Transmital


class DocumentView(ListView):
    queryset = Document.objects.select_related('uploaded_by').order_by('-date_uploaded')
    success_url = '/'
    template_name = 'pages/records.html'
    context_object_name = 'records'
    
def document_details(request, id):
    document = Document.objects.get(id=id)
    return render(request, 'partials/doc-details.html', {"document": document})

def add_record(request):

    form = DocumentUploadForm()
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('document')
        for file in files:
            doc = Document.objects.create(uploaded_by=request.user, document=file, reference_number=generate_id(10))
            doc.save()
        return redirect('documents')
    return render(request, 'partials/docfile.html', {"form": form})

