---
layout: home
title: "Cryptocurrency & Trading"
category: cryptocurrency-trading
permalink: /category/cryptocurrency-trading/
---

# Cryptocurrency & Trading

Part of [Web3 & Crypto Academy](/web3-crypto-academy/).

6 posts.

{% assign posts = site.categories[page.category] | sort: date | reverse %}
<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
