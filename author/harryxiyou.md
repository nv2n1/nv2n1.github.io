---
layout: home
title: "Weiwei Jia"
author_name: "Weiwei Jia"
permalink: /author/harryxiyou/
---

## "Weiwei Jia"

{% assign posts = site.posts | where: 'author', page.author_name %}
{{ posts | size }} posts.

<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
