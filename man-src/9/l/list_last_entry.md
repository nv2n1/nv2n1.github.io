---
title: "list_last_entry(9)"
name: "list_last_entry"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_last_entry/"
description: "list_last_entry – get the last element from a list"
---

<p>list_last_entry &#8211; get the last element from a list</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>list_last_entry(</code><i>ptr</i><code>, </code><i>type</i><code>, </code><i>member</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>ptr</i></p>
<dl>
<dd>
<dd>the list head to take the element from.</dl>
<p> <i>type</i></p>
<dl>
<dd>the type of the struct this is embedded in.</dl>
<p> <i>member</i></p>
<dl>
<dd>the name of the list_head within the struct.</dl>
<h2>Description</h2>
<p>Note, that list is expected to be not empty.</p>
<h2>Copyright</h2>
