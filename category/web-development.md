---
layout: home
title: "Web Development"
category: web-development
permalink: /category/web-development/
---

# Web Development

Part of [Programming Academy](/programming-academy/).

60 posts.

{% assign posts = site.categories[page.category] | sort: date | reverse %}
<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
