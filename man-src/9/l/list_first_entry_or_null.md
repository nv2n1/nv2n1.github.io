---
title: "list_first_entry_or_null(9)"
name: "list_first_entry_or_null"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_first_entry_or_null/"
description: "list_first_entry_or_null – get the first element from a list"
---

<p>list_first_entry_or_null &#8211; get the first element from a list</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>list_first_entry_or_null(</code><i>ptr</i><code>, </code><i>type</i><code>, </code><i>member</i><code>);</code></dl>
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
<p>Note that if the list is empty, it returns NULL.</p>
<h2>Copyright</h2>
