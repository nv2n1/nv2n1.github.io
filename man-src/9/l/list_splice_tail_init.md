---
title: "list_splice_tail_init(9)"
name: "list_splice_tail_init"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_splice_tail_init/"
---

list_splice_tail_init - join two lists and reinitialise the emptied list

<h2>Synopsis</h2>

<pre><code>void list_splice_tail_init(struct list_head *list, struct list_head *head);</code></pre>

<h2>Arguments</h2>

<i>list</i>
<dl><dd><dd>the new list to add.</dl>
 

 <i>head</i>
<dl><dd>the place to add it in the first list.</dl>

<h2>Description</h2>

Each of the lists is a queue. The list at <i>list</i> is reinitialised

<h2>Copyright</h2>


