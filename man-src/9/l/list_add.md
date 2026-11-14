---
title: "list_add(9)"
name: "list_add"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_add/"
---

list_add - add a new entry

<h2>Synopsis</h2>

<pre><code>void list_add(struct list_head *new, struct list_head *head);</code></pre>

<h2>Arguments</h2>

<i>new</i>
<dl><dd><dd>new entry to be added</dl>
 

 <i>head</i>
<dl><dd>list head to add it after</dl>

<h2>Description</h2>

Insert a new entry after the specified head. This is good for implementing stacks.

<h2>Copyright</h2>


