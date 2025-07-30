from rest_framework.decorators import api_view, permission_classes
from rest_framework.views  import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..serializers import BlogSerializer, CategorySerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from ..models import Blog, Category, Product


# @api_view(['POST','GET'])
# def blog(request):
#     if request.method == 'POST':
#         serializer= BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'Inserted Successfully'}, status= status.HTTP_201_CREATED)
#         else:
#             return Response({'message':'Failed to insert'}, status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method =='GET':
#         blog_data=Blog.objects.all()
#         serializer= BlogSerializer(blog_data, many=True)
#         return Response({'data':serializer.data}, status=status.HTTP_200_OK)
    
# @api_view(['PUT','DELETE'])
# def blog_b(request,id):
#     try:
#         blog_data=Blog.objects.get(id=id)
#     except Blog.DoesNotExist:
#             return Response({'message':'Blog doesnot found'}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'PUT':
#             serializer=BlogSerializer(blog_data, data=request.data, partial=True)
#             if serializer.is_valid():
#                  serializer.save()
#                  return Response({'message':'Updated Successfully','data':serializer.data},status=status.HTTP_200_OK)
#             else:
#                  return Response({'message':'Unable to Update','error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method =='DELETE':
#          blog_data=Blog.objects.get(id=id)
#          blog_data.delete()
#          return Response({'message':'Deleted Successfully'})

class BlogView(APIView):
    permission_classes =[AllowAny]
    def post(self, request):
        serializer= BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"Blog posted successfully",'posted':serializer.data})
        else:
            return Response({'message':"Failed to post",'err':serializer.errors})
    def get(self, request):
        blog=Blog.objects.all()
        serializer= BlogSerializer(blog, many=True)
        return Response({'message':'Successfully Updated','Updated_date':serializer.data})
    
class BlogViewApp(APIView):
    permission_classes=[AllowAny]
    def put(self, request, id):
        try:
            blog_data=Blog.objects.get(id=id)
        except:
            return Response({'message':"NOT FOUND"},status=status.HTTP_404_NOT_FOUND)
        serializer=BlogSerializer(blog_data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"Successfully updated",'updated_data':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'Failed to update'}, status=status.HTTP_400_BAD_REQUEST)
        

        
    def delete(self, request, id):
        try:
            blog_data= Blog.objects.get(id=id)
        except:
            return Response({'message':'NOT FOUND'}, status= status.HTTP_404_NOT_FOUND)
        blog_data.delete()
        return Response({'message':'Deleted Successfully'}, status=status.HTTP_200_OK)

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])

def category_view(request):
    if request.method == 'POST':
       serializer=CategorySerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response({'message':'Successful'}, status= status.HTTP_200_OK)
       else:
           return Response({'message':'Failed'}, status= status.HTTP_400_BAD_REQUEST)
       
    elif request.method == "GET":
        categories=Category.objects.all()
        serializer=CategorySerializer(category, many=True)
        data = []
    for category in categories:
        products = Product.objects.filter(category=category)
        if products.exists():
            category_data = CategorySerializer(category).data
            product_data = ProductSerializer(products, many=True).data
            category_data['products'] = product_data
            data.append(category_data)
    return Response({'data': data}, status=status.HTTP_200_OK)
    
@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def get_delete(request, id):
    try:
        category=Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response({"message":"Category doesnot exist"},status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PUT":
        serializer=CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":'Successful','updated':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'mesage':'Failed'},status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response({"message":"Deleted Successfully"},status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def product_view(request):
    if request.method == "POST":
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user) #user ko id pass garcha
            return Response({'message':"Successful", "product": serializer.data},status= status.HTTP_200_OK)
        else:
            return Response({"message":"failed", "error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        try:
            product_data= Product.objects.all()
            serializer=ProductSerializer(product_data, many=True)
            return Response(serializer.data, status= status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "failed to fetch data","error":e})


@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def update_del_product(request, id):
    try:
        product_data=Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({"message":"Product doesnot exist"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer=ProductSerializer(product_data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Successful", "updated_data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"Failed"},status= status.HTTP_400_BAD_REQUEST)
        
    if request.method == "DELETE":
        product_data.delete()
        return Response({'message':"Successful deleted"}, status=status.HTTP_400_BAD_REQUEST)
   



        


        

        

        
            
    





        

        

    
        







    
        
        

    



