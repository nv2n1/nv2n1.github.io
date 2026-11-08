---
layout: home
title: "Testing & DevOps"
category: testing-devops
permalink: /category/testing-devops/
---

## "Testing & DevOps"

{% assign posts = site.categories[page.category] | sort: date | reverse %}
{{ posts | size }} posts.

<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
