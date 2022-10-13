from django.shortcuts import render, redirect
from .models import Video
from .task import fetchsrt
import boto3
import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env()

def gallery(request):
    photos = Video.objects.all()
    context = {'photos': photos}
    return render(request, 'videobasic/gallery.html', context)


def viewPhoto(request, pk):
    photo = Video.objects.get(id=pk)

    if request.method == 'POST':
        data = request.POST
        dynamo_client  =  boto3.resource(service_name = 'dynamodb',region_name = 'ap-south-1',  aws_access_key_id =env('aws_access_key_id'), aws_secret_access_key = env('aws_secret_access_key'))
    
        product_table = dynamo_client.Table('videoshare')

        response = product_table.get_item(Key={'srt_id': str(pk)})
        contentText = ""
        startTime = ""
        for content in response['Item']['data']:
            if data['description'].upper() in content['content']:
                contentText = " ".join(content['content'].split())  
                startTime = content['start'] 
        
        return render(request, 'videobasic/video.html', {'photo': photo, 'contentText': contentText, 'starttime': startTime})


    return render(request, 'videobasic/video.html', {'photo': photo})

def addPhoto(request):

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        file = request.FILES.get('video')
        handle_uploaded_file(file)
        photo = Video.objects.create(
            description=data['description'],
            image=image,
            file=file
        )
        fetchsrt.delay(photo.id, file.name)
        return redirect('gallery')

    return render(request, 'videobasic/add.html')

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

