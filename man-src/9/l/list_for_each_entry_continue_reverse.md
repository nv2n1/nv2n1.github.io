---
title: "list_for_each_entry_continue_reverse(9)"
name: "list_for_each_entry_continue_reverse"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_for_each_entry_continue_reverse/"
description: "list_for_each_entry_continue_reverse – iterate backwards from the given point"
---

<p>list_for_each_entry_continue_reverse &#8211; iterate backwards from the given point</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>list_for_each_entry_continue_reverse(</code><i>pos</i><code>, </code><i>head</i><code>, </code><i>member</i><code>);</code></dl>
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
<dd>the name of the list_head within the struct.</dl>
<h2>Description</h2>
<p>Start to iterate over list of given type backwards, continuing after the current position.</p>
<h2>Copyright</h2>
