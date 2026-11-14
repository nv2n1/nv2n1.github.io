---
title: "acct_collect(9)"
name: "acct_collect"
section: "9"
letter: "a"
url: "/docs/linux/man/9-acct_collect/"
---

acct_collect - collect accounting information into pacct_struct

<h2>Synopsis</h2>

<pre><code>void acct_collect(long exitcode, int group_dead);</code></pre>

<h2>Arguments</h2>

<i>exitcode</i>
<dl><dd><dd>task exit code</dl>
 

 <i>group_dead</i>
<dl><dd>not 0, if this thread is the last one in the process.</dl>

<h2>Copyright</h2>


