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
    <h3>&#128279; Web3, Blockchain &amp; Cryptocurrency Academy</h3>
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

## Browse by Category

<ul class="cat-grid">
<li><a href="/category/linux-systems-administration/">linux systems administration</a> <span>(722)</span></li>
<li><a href="/category/programming-languages/">programming languages</a> <span>(129)</span></li>
<li><a href="/category/development-best-practices/">development best practices</a> <span>(99)</span></li>
<li><a href="/category/languages-frameworks/">languages frameworks</a> <span>(89)</span></li>
<li><a href="/category/scripting-utilities/">scripting utilities</a> <span>(68)</span></li>
<li><a href="/category/systems-architecture/">systems architecture</a> <span>(36)</span></li>
<li><a href="/category/testing-devops/">testing devops</a> <span>(32)</span></li>
<li><a href="/category/system-administration-cloud/">system administration cloud</a> <span>(31)</span></li>
<li><a href="/category/linux-system-configuration/">linux system configuration</a> <span>(28)</span></li>
<li><a href="/category/web-development/">web development</a> <span>(25)</span></li>
<li><a href="/category/design-patterns-architecture/">design patterns architecture</a> <span>(17)</span></li>
<li><a href="/category/security-cryptography-2/">security cryptography 2</a> <span>(17)</span></li>
<li><a href="/category/blockchain-cryptocurrency/">blockchain cryptocurrency</a> <span>(15)</span></li>
<li><a href="/category/databases-storage/">databases storage</a> <span>(11)</span></li>
<li><a href="/category/algorithms-data-structures/">algorithms data structures</a> <span>(10)</span></li>
<li><a href="/category/code-optimization/">code optimization</a> <span>(8)</span></li>
<li><a href="/category/object-oriented-programming/">object oriented programming</a> <span>(4)</span></li>
<li><a href="/category/functional-programming/">functional programming</a> <span>(4)</span></li>
<li><a href="/category/ai-engineering/">ai engineering</a> <span>(4)</span></li>
</ul>

