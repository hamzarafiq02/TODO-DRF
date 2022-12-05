from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
    api_urls= {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pkr>/',
        'Create': '/task-create/',
        'Update': '/task-update<str:pkr>/',
        'Delete': '/task-delete<str:pkr>/',
    }
    return Response(api_urls)
    
@api_view(['GET'])
def Tasklist(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Taskdetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Taskcreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def Taskupdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def Taskdelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Item successfully Deleted....!')