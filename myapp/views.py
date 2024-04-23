from django.shortcuts import render
from django.http import HttpResponse
from .mongodb_utils import create_document, read_documents, update_document, delete_document

from django.db.models import Avg, Count, Max, Min, Sum

from .models import UserInfo


def hello_world(request):
    return HttpResponse("Hello World")


def create(request):
    data = {'name': 'akash', 'age': 21}
    inserted_id = create_document('User_Info', data)
    return HttpResponse("create operations done")


def read(request):
    documents = read_documents('User_Info')
    return HttpResponse(documents)

def updates(request):
    query = {'name': 'akash'}
    update = {'$set': {'name': 'chauhan'}}
    modified_count = update_document('User_Info', query, update)
    return HttpResponse(modified_count)

def delete(request):
    query = {'name': 'akash'}
    deleted_count = delete_document('User_Info', query)
    return HttpResponse(deleted_count)
    

    
def querry(request):
    documents = read_documents('User_Info')
    query = {'age': {'$gt': 10}}  
    documents = read_documents('User_Info', query)
    return HttpResponse(documents)

    query = {'age': {'$lt': 25}} 
    documents = read_documents('User_Info', query)
    print(HttpResponse(documents))

    update = {'$set': {'isStudent': True}}
    modified_count = update_document('User_Info', query, update)


    query = {'isStudent': True}
    deleted_count = delete_document('User_Info', query)




def crudsql(request):


    #create
    obj = UserInfo(name='John', age=30)
    obj.save()

    # Read records
    objects = UserInfo.objects.all()

    # Update a record
    obj = UserInfo.objects.get(name='John')
    obj.age = 31
    obj.save()

    # Delete a record
    obj = UserInfo.objects.get(name='John')
    obj.delete()


def querry_orm(request):
    all_records = UserInfo.objects.all()
    filtered_records = UserInfo.objects.filter(age__gt=30)  
    filtered_records = UserInfo.objects.filter(name__startswith='J')  

    
    single_record = UserInfo.objects.get(name='John')

    ordered_records = UserInfo.objects.order_by('age') #-age for dec
    limited_records = UserInfo.objects.all()[:5]  # Get the first 5 records

    UserInfo.objects.update(age=25) # Update all records

    UserInfo.objects.filter(name='John').update(age=31)

    # Delete a single record (returns the number of deleted objects and the Python dictionary representing the deleted values)
    deleted_dict = UserInfo.objects.get(name='John').delete()

    # Delete multiple records
    deleted_dict = UserInfo.objects.filter(age__lt=25).delete()

    average_age = UserInfo.objects.aggregate(Avg('age'))



    # to use sql commands, we need to import connections    

    # with connection.cursor() as cursor:
    #     # Execute your raw SQL query
    #     cursor.execute("SELECT * FROM myapp_mymodel WHERE field1 = %s", ['value1'])
        
    #     # Fetch the result
    #     result = cursor.fetchall()
    
    # return HttpResponse(result)