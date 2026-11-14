---
title: "list_prepare_entry(9)"
name: "list_prepare_entry"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_prepare_entry/"
description: "list_prepare_entry – prepare a pos entry for use in list_for_each_entry_continue"
---

<p>list_prepare_entry &#8211; prepare a pos entry for use in <code>list_for_each_entry_continue</code></p>
<h2>Synopsis</h2>
<dl>
<dt> <code>list_prepare_entry(</code><i>pos</i><code>, </code><i>head</i><code>, </code><i>member</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>pos</i></p>
<dl>
<dd>
<dd>the type * to use as a start point</dl>
<p> <i>head</i></p>
<dl>
<dd>the head of the list</dl>
<p> <i>member</i></p>
<dl>
<dd>the name of the list_head within the struct.</dl>
<h2>Description</h2>
<p>Prepares a pos entry for use as a start point in <code>list_for_each_entry_continue</code>.</p>
<h2>Copyright</h2>
