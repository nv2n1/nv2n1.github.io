---
layout: home
title: "Anjaneyulu Naini"
author_name: "Anjaneyulu Naini"
permalink: /author/anjaneyulu-appmajix/
---

## "Anjaneyulu Naini"

{% assign posts = site.posts | where: 'author', page.author_name %}
{{ posts | size }} posts.

<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
