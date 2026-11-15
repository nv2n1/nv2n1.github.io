---
layout: home
title: "Programming Languages"
category: programming-languages
permalink: /category/programming-languages/
---

# Programming Languages

Part of [Programming Academy](/programming-academy/).

244 posts.

{% assign posts = site.categories[page.category] | sort: date | reverse %}
<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
