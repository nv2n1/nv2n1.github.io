---
title: "trace_softirq_raise(9)"
name: "trace_softirq_raise"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_softirq_raise/"
description: "trace_softirq_raise – called immediately when a softirq is raised"
---

<p>trace_softirq_raise &#8211; called immediately when a softirq is raised</p>
<h2>Synopsis</h2>
<pre><code>void trace_softirq_raise(unsigned int vec_nr);</code></pre>
<h2>Arguments</h2>
<p><i>vec_nr</i></p>
<dl>
<dd>
<dd>softirq vector number</dl>
<h2>Description</h2>
<p>When used in combination with the softirq_entry tracepoint we can determine the softirq raise to run latency.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
