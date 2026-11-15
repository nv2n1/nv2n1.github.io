---
layout: home
title: "Self-Custody & Security"
category: self-custody-security
permalink: /category/self-custody-security/
---

# Self-Custody & Security

Part of [Web3 & Crypto Academy](/web3-crypto-academy/).

3 posts.

{% assign posts = site.categories[page.category] | sort: date | reverse %}
<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
