from django.shortcuts import render
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

# class DocumentView(FormView):
#     form_class = DocumentUploadForm
    # success_url = '/'
    # template_name = 'pages/records.html'

#     def post(self, request):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         if form.is_valid():
#             files = request.FILES.getlist('document')
#             for index, file in enumerate(files):
#                 doc = Document.objects.create(
#                     uploaded_by=request.user, 
#                     document=file, 
#                     reference_number=generate_id(10)*(index+1))
#                 doc.save()
#             return redirect('documents')

#         return redirect('documents')



