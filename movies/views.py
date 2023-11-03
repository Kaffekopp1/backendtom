from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies
import json
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from django.core import serializers

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def TestView(request):
  if request.method == 'GET':
   print("test")
   movie = Movies.objects.all()
   print(movie)
   data = {
    "team": "data",
    "userTeam": "serializerU.data,",
    "teamnord": "test",
    "teamsyd": "test"
     }
   return Response(data)

@api_view(['POST','GET',"DELETE","PUT","PATCH"])
@renderer_classes([JSONRenderer])
def TestViewPOST(request):
  if request.method == 'POST':
   body_unicode = request.body.decode('utf-8')
   body= json.loads(body_unicode)
  #  print(body["movie"])
  #  movie = Movies(movie=body["movie"], betyg=body["betyg"])
  #  movie.save()
  #  return Response()
   movie_name = body.get('movie')
   betyg = body.get('betyg')
   try:
            movie = Movies.objects.create(
                movie=movie_name,
                betyg=betyg
            )
            # Access the automatically generated ID
            movie_id = movie.id

            return JsonResponse({'message': 'Movie created successfully', 'id': movie_id})
   except Exception as e:
            return JsonResponse({'error': str(e)})

  # if request.method == 'GET':
  #  print("testGET")
  #  movies = Movies.objects.all()
  #  print(movies)
  #  movie_data = [
  #       {
  #           'movie': movie.movie,
  #           'betyg': movie.betyg,
  #           'created_at': movie.created_at,
  #           'updated_at': movie.updated_at
  #       }
  #       for movie in movies
  #   ]
  #  return JsonResponse({'movies': movie_data}, safe=False)
  if request.method == 'GET':
    print("testGET")
    movies = Movies.objects.all()


    serialized_movies = serializers.serialize("json", movies)
    deserialized_movies = json.loads(serialized_movies)
    # print(serialized_movies[1]["pk"])
    movie_data = []
    for movie in movies:
            movie_info = {
                'id': movie.id,
                'movie': movie.movie,
                'betyg': movie.betyg,
                'created_at': movie.created_at,
                'updated_at': movie.updated_at
            }
            movie_data.append(movie_info)

    return JsonResponse({'movies': movie_data}, safe=False)

    # return HttpResponse(serialized_movies, content_type="application/json")


  if request.method == 'DELETE':
      print("del")
      movie_id = request.data.get('id')
      try:
        movie = Movies.objects.get(id=movie_id)
        # Use get_object_or_404 to retrieve the movie object or return a 404 response if not found
        # Delete the movie
        movie.delete()
        return HttpResponse("Movie deleted successfully")  # 204 No Content indicates successful deletion
      except Movies.DoesNotExist:
            return HttpResponse("Movie not found", status=404)

  if request.method == 'PUT':
        movie_id = request.data.get('id')  # Assuming you pass the ID in the request data
        try:
           movie = Movies.objects.get(id=movie_id)
            # You can access the request data directly without using request.body
           if 'movie' in request.data:
                movie.movie = request.data['movie']
           if 'betyg' in request.data:
                movie.betyg = request.data['betyg']
           movie.save()
           return HttpResponse("Movie updated successfully")
        except Movies.DoesNotExist:
            return HttpResponse("Movie not found", status=404)

  # if request.method == 'PUT':
  #       movie_id = request.data.get('id')  # Assuming you pass the ID in the request data
  #       try:
  #           movie = Movies.objects.get(id=movie_id)
  #           body_unicode = request.body.decode('utf-8')
  #           body = json.loads(body_unicode)
  #           movie.movie = body['movie']
  #           movie.betyg = body['betyg']
  #           movie.save()
  #           return HttpResponse("Movie updated successfully")
  #       except Movies.DoesNotExist:
  #           return HttpResponse("Movie not found", status=404)
  #       except json.JSONDecodeError:
  #           return HttpResponse("Invalid JSON data", status=400)

  if request.method == 'PATCH':
        movie_id = request.data.get('id')  # Assuming you pass the ID in the request data
        try:
           movie = Movies.objects.get(id=movie_id)
            # You can access the request data directly without using request.body
           if 'movie' in request.data:
                movie.movie = request.data['movie']
           if 'betyg' in request.data:
                movie.betyg = request.data['betyg']
           movie.save()
           return HttpResponse("Movie updated successfully")
        except Movies.DoesNotExist:
            return HttpResponse("Movie not found", status=404)


  return HttpResponse("Invalid request method", status=405)
