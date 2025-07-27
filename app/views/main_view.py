from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..serializers import StudentSerializers, EmployeeSerializers
from ..models import Student, Employee

@api_view(['POST'])
def add_student(request):
    if request.method == 'POST':
        serializers = StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message':'Student inserted successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'Failed to inserted'}.serializers.errors,status= status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def get_student(request):
    if request.method == 'GET':
        student_data=Student.objects.all()
        serializers= StudentSerializers(student_data, many=True)
        return Response({'data':serializers.data},status=status.HTTP_200_OK)
    
@api_view(['PUT'])
def update(request, id):
    try:
        student_data=Student.objects.get(id=id)

    except Student.DoesNotExist:
        return Response({'message':'student not found'})
    
    if request.method == "PUT":
        serializers=StudentSerializers(student_data, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'Student Updated Successfully','data':serializers.data},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'meaasge':'Failed to Update'},status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def get_stu(request,id):
    try:
        student_data=Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({'message':'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
       serializers= StudentSerializers(student_data)
       return Response({'data':serializers.data}, status=status.HTTP_200_OK)
    
@api_view(['DELETE'])
def delete_stu(request,id):
    try:
        student_data=Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"message":"Student is not found"},status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        student_data.delete()
        return Response({'message':'student delete successfully'},status=status.HTTP_103_EARLY_HINTS)

@api_view(['POST'])
def add_employee(request):
    if request.method == "POST":
        serializer= EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Meaasge':'Student  Data is Inserted Successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'Failed to Insert data'},status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def get_employeee(request):
    if request.method == 'GET':
        try:
            employee_data=Employee.objects.all()
            serializer=EmployeeSerializers(employee_data, many=True)
            return Response({'data':serializer.data}, status= status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({'message':"Employee doesnot exist"}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['PUT'])
def update(request, id):
    try:
        employee_data=Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response({"meaasge":"Employee doesnot Exist"},status= status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer= EmployeeSerializers(employee_data, data=request.data, partial=True)
        if serializer.is_valid:
            serializer.save()
            return Response({'message':'Employee is Updated Successfully','data':serializer.data}, status= status.HTTP_200_OK)
    else:
        return Response({'message':'Failed is Updated'},status=status.HTTP_400_BAD_REQUEST)
    

api_view(['DELETE'])
def delete_employee(request, id):
    try:
        employee_data= Employee.objects.get(id=id)
    except:
        return Response({'message':'Employee not found'},status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        employee_data.delete()
        return Response({'message':'Couldnot delete'})
    
    



        
        


        


    








