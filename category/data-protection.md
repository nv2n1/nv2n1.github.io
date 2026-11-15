---
layout: home
title: "Data Protection"
category: data-protection
permalink: /category/data-protection/
---

# Data Protection

Part of [Distributed Systems Academy](/distributed-systems-academy/) > [Security & Cryptography Path](/security-cryptography-path/).

1 posts.

{% assign posts = site.categories[page.category] | sort: date | reverse %}
<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
