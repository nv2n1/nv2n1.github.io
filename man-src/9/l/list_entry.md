---
title: "list_entry(9)"
name: "list_entry"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_entry/"
description: "list_entry – get the struct for this entry"
---

<p>list_entry &#8211; get the struct for this entry</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>list_entry(</code><i>ptr</i><code>, </code><i>type</i><code>, </code><i>member</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>ptr</i></p>
<dl>
<dd>
<dd>the struct list_head pointer.</dl>
<p> <i>type</i></p>
<dl>
<dd>the type of the struct this is embedded in.</dl>
<p> <i>member</i></p>
<dl>
<dd>the name of the list_head within the struct.</dl>
<h2>Copyright</h2>
