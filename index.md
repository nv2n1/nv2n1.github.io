---
title: SysTutorials
layout: home
---

# SysTutorials

Welcome to SysTutorials! Learn through 5 focused learning academies. Explore systems, AI, blockchain, and programming.

## Choose Your Learning Hub

<div class="academies">
  <div class="academy">
    <h3>&#127760; Distributed Systems Academy</h3>
    <p>Master distributed systems design, consensus algorithms, and modern architecture patterns.</p>
    <p class="paths"><strong>Learning Paths:</strong> <a href="/advanced-systems-path/">Advanced Systems &amp; Architecture</a> &middot; <a href="/security-cryptography-path/">Security &amp; Cryptography</a></p>
    <p class="explore"><a href="/distributed-systems-academy/">Explore Academy &rarr;</a></p>
  </div>
  <div class="academy">
    <h3>&#128421;&#65039; Linux &amp; Systems Administration Academy</h3>
    <p>Master Linux administration, command-line tools, system configuration, and single-machine systems.</p>
    <p class="paths"><strong>Learning Paths:</strong> <a href="/linux-essentials-path/">Linux Essentials</a> &middot; <a href="/linux-sysadmin-path/">Linux System Administration</a></p>
    <p class="explore"><a href="/linux-systems-administration-academy/">Explore Academy &rarr;</a></p>
  </div>
  <div class="academy">
    <h3>&#129302; AI Engineering Hub</h3>
    <p>Build with modern AI models. Learn LLM fundamentals, CLI+AI integration, and prompt engineering.</p>
    <p class="explore"><a href="/ai-engineering-hub/">Explore Hub &rarr;</a></p>
  </div>
  <div class="academy">
    <h3>&#128279; Web3 &amp; Crypto Academy</h3>
    <p>Master blockchain, cryptocurrency, Web3, and decentralized finance.</p>
    <p class="explore"><a href="/web3-crypto-academy/">Explore Academy &rarr;</a></p>
  </div>
  <div class="academy">
    <h3>&#128187; Programming Academy</h3>
    <p>Master programming languages, algorithms, and software development.</p>
    <p class="explore"><a href="/programming-academy/">Explore Academy &rarr;</a></p>
  </div>
</div>

## Recent Posts {#posts}

{% for post in site.posts limit:10 %}
  <article class="recent-post">
    <h3><a href="{{ post.url }}">{{ post.title | escape }}</a></h3>
    <p class="meta"><time>{{ post.date | date: "%B %-d, %Y" }}</time>{% if post.author %} &middot; {{ post.author | escape }}{% endif %}</p>
  </article>
{% endfor %}

<p><a href="/archive/">Browse all {{ site.posts | size }} posts &rarr;</a></p>

## Recent Updates

<ul class="posts">
{% assign updated_posts = site.posts | sort: 'modified' | reverse %}
{% for post in updated_posts limit:10 %}
  <li><time>{{ post.modified | date: "%b %-d, %Y" }}</time> <a href="{{ post.url }}">{{ post.title | escape }}</a></li>
{% endfor %}
</ul>

## Browse by Category

Every category is a learning topic in an academy and learning path. See [all categories](/categories/), or start from an [academy](/#academies).

