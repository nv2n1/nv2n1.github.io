---
layout: home
title: "Command Line & Text Tools"
category: command-line-text-tools
permalink: /category/command-line-text-tools/
---

# Command Line & Text Tools

Part of [Linux & Systems Administration Academy](/linux-systems-administration-academy/) > [Linux Essentials Path](/linux-essentials-path/).

38 posts.

{% assign posts = site.categories[page.category] | sort: date | reverse %}
<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
