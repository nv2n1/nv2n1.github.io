---
title: "sk_for_each_entry_offset_rcu(9)"
name: "sk_for_each_entry_offset_rcu"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_for_each_entry_offset_rcu/"
description: "sk_for_each_entry_offset_rcu – iterate over a list at a given struct offset"
---

<p>sk_for_each_entry_offset_rcu &#8211; iterate over a list at a given struct offset</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>sk_for_each_entry_offset_rcu(</code><i>tpos</i><code>, </code><i>pos</i><code>, </code><i>head</i><code>, </code><i>offset</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>tpos</i></p>
<dl>
<dd>
<dd>the type * to use as a loop cursor.</dl>
<p> <i>pos</i></p>
<dl>
<dd>the struct hlist_node to use as a loop cursor.</dl>
<p> <i>head</i></p>
<dl>
<dd>the head for your list.</dl>
<p> <i>offset</i></p>
<dl>
<dd>offset of hlist_node within the struct.</dl>
<h2>Copyright</h2>
