---
title: "list_cut_position(9)"
name: "list_cut_position"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_cut_position/"
---

list_cut_position - cut a list into two

<h2>Synopsis</h2>

<pre><code>void list_cut_position(struct list_head *list, struct list_head *head, struct list_head *entry);</code></pre>

<h2>Arguments</h2>

<i>list</i>
<dl><dd><dd>a new list to add all removed entries</dl>
 

 <i>head</i>
<dl><dd>a list with entries</dl>
 

 <i>entry</i>
<dl><dd>an entry within head, could be the head itself and if so we won't cut the list</dl>

<h2>Description</h2>

This helper moves the initial part of <i>head</i>, up to and including <i>entry</i>, from <i>head</i> to <i>list</i>. You should pass on <i>entry</i> an element you know is on <i>head</i>. <i>list</i> should be an empty list or a list you do not care about losing its data.

<h2>Copyright</h2>


