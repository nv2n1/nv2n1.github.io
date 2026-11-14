---
title: "list_replace(9)"
name: "list_replace"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_replace/"
---

list_replace - replace old entry by new one

<h2>Synopsis</h2>

<pre><code>void list_replace(struct list_head *old, struct list_head *new);</code></pre>

<h2>Arguments</h2>

<i>old</i>
<dl><dd><dd>the element to be replaced</dl>
 

 <i>new</i>
<dl><dd>the new element to insert</dl>

<h2>Description</h2>

If <i>old</i> was empty, it will be overwritten.

<h2>Copyright</h2>


