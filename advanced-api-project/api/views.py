from typing import Any

from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):

	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [AllowAny]

	def get_queryset(self):
		qs = super().get_queryset()
		year = self.request.query_params.get("year")
		if year:
			try:
				year_int = int(year)
				qs = qs.filter(publication_year=year_int)
			except (TypeError, ValueError):
				pass
		return qs


class BookDetailView(generics.RetrieveAPIView):

	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [AllowAny]


class BookCreateView(generics.CreateAPIView):


	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer: BookSerializer) -> None:

		serializer.save()


class BookUpdateView(generics.UpdateAPIView):

	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticated]

	def perform_update(self, serializer: BookSerializer) -> None:
		serializer.save()


class BookDeleteView(generics.DestroyAPIView):

	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticated]

