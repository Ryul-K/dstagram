from django.shortcuts import render

# Create your views here.
#제너릭 뷰할거야
from .models import Photo

def photo_list(request):
    # 보여줄 사진데이터, (request) 관례적으로 첫번째 메소드는 req
    photos = Photo.objects.all()
        #objects: DB manager에게 all 반환해달라 느낌
    return render(request, 'photo/list.html', {'photos':photos})
        #'photo/list.html': 템플릿의 photo/list.html

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect #업로드후 리다이렉트~

class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text'] #작성자 (author), 작성시간(created)
    template_name = 'photo/upload.html'

    def form_valid(self, form): #작성된 데이터가 올바른 데이터인지, author정보 등
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            #데이터가 올바르다면
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})