---
title: "list_safe_reset_next(9)"
name: "list_safe_reset_next"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_safe_reset_next/"
description: "list_safe_reset_next – reset a stale list_for_each_entry_safe loop"
---

<p>list_safe_reset_next &#8211; reset a stale list_for_each_entry_safe loop</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>list_safe_reset_next(</code><i>pos</i><code>, </code><i>n</i><code>, </code><i>member</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>pos</i></p>
<dl>
<dd>
<dd>the loop cursor used in the list_for_each_entry_safe loop</dl>
<p> <i>n</i></p>
<dl>
<dd>temporary storage used in list_for_each_entry_safe</dl>
<p> <i>member</i></p>
<dl>
<dd>the name of the list_head within the struct.</dl>
<h2>Description</h2>
<p>list_safe_reset_next is not safe to use in general if the list may be modified concurrently (eg. the lock is dropped in the loop body). An exception to this is if the cursor element (pos) is pinned in the list, and list_safe_reset_next is called after re-taking the lock and before completing the current iteration of the loop body.</p>
<h2>Copyright</h2>
