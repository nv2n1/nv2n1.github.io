---
layout: home
title: "Algorithms & Data Structures"
category: algorithms-data-structures
permalink: /category/algorithms-data-structures/
---

## "Algorithms & Data Structures"

{% assign posts = site.categories[page.category] | sort: date | reverse %}
{{ posts | size }} posts.

<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
