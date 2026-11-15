---
layout: home
title: "Files & Storage"
category: files-storage
permalink: /category/files-storage/
---

# Files & Storage

Part of [Linux & Systems Administration Academy](/linux-systems-administration-academy/) > [Linux Essentials Path](/linux-essentials-path/).

116 posts.

{% assign posts = site.categories[page.category] | sort: date | reverse %}
<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
