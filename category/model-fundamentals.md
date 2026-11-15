---
layout: home
title: "Model Fundamentals"
category: model-fundamentals
permalink: /category/model-fundamentals/
---

# Model Fundamentals

Part of [AI Engineering Hub](/ai-engineering-hub/).

2 posts.

{% assign posts = site.categories[page.category] | sort: date | reverse %}
<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
