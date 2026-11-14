---
title: "list_for_each_entry_safe(9)"
name: "list_for_each_entry_safe"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_for_each_entry_safe/"
description: "list_for_each_entry_safe – iterate over list of given type safe against removal of list entry"
---

<p>list_for_each_entry_safe &#8211; iterate over list of given type safe against removal of list entry</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>list_for_each_entry_safe(</code><i>pos</i><code>, </code><i>n</i><code>, </code><i>head</i><code>, </code><i>member</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>pos</i></p>
<dl>
<dd>
<dd>the type * to use as a loop cursor.</dl>
<p> <i>n</i></p>
<dl>
<dd>another type * to use as temporary storage</dl>
<p> <i>head</i></p>
<dl>
<dd>the head for your list.</dl>
<p> <i>member</i></p>
<dl>
<dd>the name of the list_head within the struct.</dl>
<h2>Copyright</h2>
