from django.urls import path

from review.views import (
    home,
    posts,
    ranking,
    search,
    forbidden_permission,
    ticket_detail,
    ticket_create,
    ticket_update,
    ticket_delete,
    review_detail,
    ticket_self_review_create,
    self_review_create,
    review_create,
    review_delete,
    self_review_delete,
    review_update,
    self_review_update,
    relation,
    relation_delete,
    relation_block
)


urlpatterns = [
    # ticket & review
    path("home/", home, name="home"),
    path("posts/", posts, name="posts"),
    path("ranking/", ranking, name="ranking"),
    path("search/", search, name="search"),
    path("forbidden_permission/", forbidden_permission, name="forbidden_permission"),
    path(
        "reviews/ticket_self_review_create/",
        ticket_self_review_create,
        name="ticket_self_review_create",
    ),
    # ticket
    path("tickets/<int:ticket_id>/", ticket_detail, name="ticket_detail"),
    path("tickets/create/", ticket_create, name="ticket_create"),
    path("tickets/<int:ticket_id>/update/", ticket_update, name="ticket_update"),
    path("tickets/<int:ticket_id>/delete/", ticket_delete, name="ticket_delete"),
    # review
    path("reviews/<int:review_id>/", review_detail, name="review_detail"),
    path(
        "reviews/<int:review_id>/self_review_create/",
        self_review_create,
        name="self_review_create",
    ),
    path("reviews/<int:review_id>/review_create/", review_create, name="review_create"),
    path("reviews/<int:review_id>/review_delete/", review_delete, name="review_delete"),
    path(
        "reviews/<int:review_id>/self_review_delete/",
        self_review_delete,
        name="self_review_delete",
    ),
    path("reviews/<int:review_id>/review_update/", review_update, name="review_update"),
    path(
        "reviews/<int:review_id>/self_review_update/",
        self_review_update,
        name="self_review_update",
    ),
    # relation
    path("relations/", relation, name="relation"),
    path("relations/<int:relation_id>/delete", relation_delete, name="relation_delete"),
    path("relations/<int:relation_id>/block", relation_block, name="relation_block"),
]
