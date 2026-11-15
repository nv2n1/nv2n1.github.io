---
layout: home
title: "Web3 & DeFi"
category: web3-defi
permalink: /category/web3-defi/
---

# Web3 & DeFi

Part of [Web3 & Crypto Academy](/web3-crypto-academy/).

1 posts.

{% assign posts = site.categories[page.category] | sort: date | reverse %}
<ul class="posts">
{% for post in posts %}
  <li><time>{{ post.date | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>
