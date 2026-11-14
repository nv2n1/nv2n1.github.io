---
title: "list_for_each_safe(9)"
name: "list_for_each_safe"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_for_each_safe/"
description: "list_for_each_safe – iterate over a list safe against removal of list entry"
---

<p>list_for_each_safe &#8211; iterate over a list safe against removal of list entry</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>list_for_each_safe(</code><i>pos</i><code>, </code><i>n</i><code>, </code><i>head</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>pos</i></p>
<dl>
<dd>
<dd>the struct list_head to use as a loop cursor.</dl>
<p> <i>n</i></p>
<dl>
<dd>another struct list_head to use as temporary storage</dl>
<p> <i>head</i></p>
<dl>
<dd>the head for your list.</dl>
<h2>Copyright</h2>
