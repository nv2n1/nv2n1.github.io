---
layout: home
title: "systemd & Services"
category: systemd-services
permalink: /category/systemd-services/
---

# systemd & Services

Part of [Linux & Systems Administration Academy](/linux-systems-administration-academy/) > [Linux System Administration Path](/linux-sysadmin-path/).

22 posts.

{% assign posts = site.categories[page.category] | sort: date | reverse %}
<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
