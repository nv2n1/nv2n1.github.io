---
title: "hlist_for_each_entry(9)"
name: "hlist_for_each_entry"
section: "9"
letter: "h"
url: "/docs/linux/man/9-hlist_for_each_entry/"
description: "hlist_for_each_entry – iterate over list of given type"
---

<p>hlist_for_each_entry &#8211; iterate over list of given type</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>hlist_for_each_entry(</code><i>pos</i><code>, </code><i>head</i><code>, </code><i>member</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>pos</i></p>
<dl>
<dd>
<dd>the type * to use as a loop cursor.</dl>
<p> <i>head</i></p>
<dl>
<dd>the head for your list.</dl>
<p> <i>member</i></p>
<dl>
<dd>the name of the hlist_node within the struct.</dl>
<h2>Copyright</h2>
