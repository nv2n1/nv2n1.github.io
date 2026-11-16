---
title: "list_for_each_entry_reverse(9)"
name: "list_for_each_entry_reverse"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_for_each_entry_reverse/"
description: "list_for_each_entry_reverse – iterate backwards over list of given type."
---

<p>list_for_each_entry_reverse &#8211; iterate backwards over list of given type.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>list_for_each_entry_reverse(</code><i>pos</i><code>, </code><i>head</i><code>, </code><i>member</i><code>);</code></dt></dl>
<h2>Arguments</h2>
<p><i>pos</i></p>
<dl>
<dd>
</dd><dd>the type * to use as a loop cursor.</dd></dl>
<p> <i>head</i></p>
<dl>
<dd>the head for your list.</dd></dl>
<p> <i>member</i></p>
<dl>
<dd>the name of the list_head within the struct.</dd></dl>
<h2>Copyright</h2>
