---
title: "match_futex(9)"
name: "match_futex"
section: "9"
letter: "m"
url: "/docs/linux/man/9-match_futex/"
description: "match_futex – Check whether two futex keys are equal"
---

<p>match_futex &#8211; Check whether two futex keys are equal</p>
<h2>Synopsis</h2>
<pre><code>int match_futex(union futex_key *key1, union futex_key *key2);</code></pre>
<h2>Arguments</h2>
<p><i>key1</i></p>
<dl>
<dd>
<dd>Pointer to key1</dl>
<p> <i>key2</i></p>
<dl>
<dd>Pointer to key2</dl>
<h2>Description</h2>
<p>Return 1 if two futex_keys are equal, 0 otherwise.</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
