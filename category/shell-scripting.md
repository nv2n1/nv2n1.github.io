---
layout: home
title: "Shell & Scripting"
category: shell-scripting
permalink: /category/shell-scripting/
---

# Shell & Scripting

Part of [Linux & Systems Administration Academy](/linux-systems-administration-academy/) > [Linux Essentials Path](/linux-essentials-path/).

47 posts.

{% assign posts = site.categories[page.category] | sort: date | reverse %}
<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
