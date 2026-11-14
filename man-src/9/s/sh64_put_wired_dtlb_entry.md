---
title: "sh64_put_wired_dtlb_entry(9)"
name: "sh64_put_wired_dtlb_entry"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sh64_put_wired_dtlb_entry/"
description: "sh64_put_wired_dtlb_entry – Free a wired (locked-in) entry in the DTLB."
---

<p>sh64_put_wired_dtlb_entry &#8211; Free a wired (locked-in) entry in the DTLB.</p>
<h2>Synopsis</h2>
<pre><code>int sh64_put_wired_dtlb_entry(unsigned long long entry);</code></pre>
<h2>Arguments</h2>
<p><i>entry</i></p>
<dl>
<dd>
<dd>Address of TLB slot.</dl>
<h2>Description</h2>
<p>Works like a stack, last one to allocate must be first one to free.</p>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
