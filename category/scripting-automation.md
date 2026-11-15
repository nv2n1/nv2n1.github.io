---
layout: home
title: "Scripting & Automation"
category: scripting-automation
permalink: /category/scripting-automation/
---

# Scripting & Automation

Part of [Programming Academy](/programming-academy/).

51 posts.

{% assign posts = site.categories[page.category] | sort: date | reverse %}
<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
