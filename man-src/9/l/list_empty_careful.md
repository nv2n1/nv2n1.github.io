---
title: "list_empty_careful(9)"
name: "list_empty_careful"
section: "9"
letter: "l"
url: "/docs/linux/man/9-list_empty_careful/"
description: "list_empty_careful – tests whether a list is empty and not being modified"
---

<p>list_empty_careful &#8211; tests whether a list is empty and not being modified</p>
<h2>Synopsis</h2>
<pre><code>int list_empty_careful(const struct list_head *head);</code></pre>
<h2>Arguments</h2>
<p><i>head</i></p>
<dl>
<dd>
<dd>the list to test</dl>
<h2>Description</h2>
<p>tests whether a list is empty _and_ checks that no other CPU might be in the process of modifying either member (next or prev)</p>
<h2>Note</h2>
<p>using <code>list_empty_careful</code> without synchronization can only be safe if the only activity that can happen to the list entry is <code>list_del_init</code>. Eg. it cannot be used if another CPU could re-<code>list_add</code> it.</p>
<h2>Copyright</h2>
