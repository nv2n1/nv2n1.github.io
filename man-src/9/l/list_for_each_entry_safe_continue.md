---
title: "list_for_each_entry_safe_continue(9)"
name: "list_for_each_entry_safe_continue"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_for_each_entry_safe_continue/"
description: "list_for_each_entry_safe_continue – continue list iteration safe against removal"
---

<p>list_for_each_entry_safe_continue &#8211; continue list iteration safe against removal</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>list_for_each_entry_safe_continue(</code><i>pos</i><code>, </code><i>n</i><code>, </code><i>head</i><code>, </code><i>member</i><code>);</code></dl>
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
<h2>Description</h2>
<p>Iterate over list of given type, continuing after current point, safe against removal of list entry.</p>
<h2>Copyright</h2>
