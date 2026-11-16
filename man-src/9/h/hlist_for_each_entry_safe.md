---
title: "hlist_for_each_entry_safe(9)"
name: "hlist_for_each_entry_safe"
section: "9"
letter: "h"
url: "/docs/linux/man/9-hlist_for_each_entry_safe/"
description: "hlist_for_each_entry_safe – iterate over list of given type safe against removal of list entry"
---

<p>hlist_for_each_entry_safe &#8211; iterate over list of given type safe against removal of list entry</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>hlist_for_each_entry_safe(</code><i>pos</i><code>, </code><i>n</i><code>, </code><i>head</i><code>, </code><i>member</i><code>);</code></dt></dl>
<h2>Arguments</h2>
<p><i>pos</i></p>
<dl>
<dd>
</dd><dd>the type * to use as a loop cursor.</dd></dl>
<p> <i>n</i></p>
<dl>
<dd>another struct hlist_node to use as temporary storage</dd></dl>
<p> <i>head</i></p>
<dl>
<dd>the head for your list.</dd></dl>
<p> <i>member</i></p>
<dl>
<dd>the name of the hlist_node within the struct.</dd></dl>
<h2>Copyright</h2>
