---
layout: home
title: "Linux & Systems Administration"
category: linux-systems-administration
permalink: /category/linux-systems-administration/
---

## "Linux & Systems Administration"

{% assign posts = site.categories[page.category] | sort: date | reverse %}
{{ posts | size }} posts.

<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
