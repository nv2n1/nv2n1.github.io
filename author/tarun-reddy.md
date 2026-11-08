---
layout: home
title: "Btcman.io"
author_name: "Btcman.io"
permalink: /author/tarun-reddy/
---

## "Btcman.io"

{% assign posts = site.posts | where: 'author', page.author_name %}
{{ posts | size }} posts.

<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
