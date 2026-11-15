---
layout: home
title: "Consistency Models"
category: consistency-models
permalink: /category/consistency-models/
---

# Consistency Models

Part of [Distributed Systems Academy](/distributed-systems-academy/) > [Advanced Systems & Architecture Path](/advanced-systems-path/).

5 posts.

{% assign posts = site.categories[page.category] | sort: date | reverse %}
<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
