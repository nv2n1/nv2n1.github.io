---
title: "trace_softirq_entry(9)"
name: "trace_softirq_entry"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_softirq_entry/"
description: "trace_softirq_entry – called immediately before the softirq handler"
---

<p>trace_softirq_entry &#8211; called immediately before the softirq handler</p>
<h2>Synopsis</h2>
<pre><code>void trace_softirq_entry(unsigned int vec_nr);</code></pre>
<h2>Arguments</h2>
<p><i>vec_nr</i></p>
<dl>
<dd>
<dd>softirq vector number</dl>
<h2>Description</h2>
<p>When used in combination with the softirq_exit tracepoint we can determine the softirq handler routine.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
