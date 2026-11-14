---
title: "list_add_tail(9)"
name: "list_add_tail"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_add_tail/"
---

list_add_tail - add a new entry

<h2>Synopsis</h2>

<pre><code>void list_add_tail(struct list_head *new, struct list_head *head);</code></pre>

<h2>Arguments</h2>

<i>new</i>
<dl><dd><dd>new entry to be added</dl>
 

 <i>head</i>
<dl><dd>list head to add it before</dl>

<h2>Description</h2>

Insert a new entry before the specified head. This is useful for implementing queues.

<h2>Copyright</h2>


