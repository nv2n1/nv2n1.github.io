---
layout: home
title: "CLI + AI Integration"
category: cli-ai-integration
permalink: /category/cli-ai-integration/
---

# CLI + AI Integration

Part of [AI Engineering Hub](/ai-engineering-hub/).

2 posts.

{% assign posts = site.categories[page.category] | sort: date | reverse %}
<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
