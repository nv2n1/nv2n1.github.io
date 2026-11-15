---
layout: home
title: "Packages, Desktop & Applications"
category: packages-desktop-applications
permalink: /category/packages-desktop-applications/
---

# Packages, Desktop & Applications

Part of [Linux & Systems Administration Academy](/linux-systems-administration-academy/) > [Linux Essentials Path](/linux-essentials-path/).

107 posts.

{% assign posts = site.categories[page.category] | sort: date | reverse %}
<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
