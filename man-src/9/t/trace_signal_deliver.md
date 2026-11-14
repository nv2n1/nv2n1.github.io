---
title: "trace_signal_deliver(9)"
name: "trace_signal_deliver"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_signal_deliver/"
description: "trace_signal_deliver – called when a signal is delivered"
---

<p>trace_signal_deliver &#8211; called when a signal is delivered</p>
<h2>Synopsis</h2>
<pre><code>void trace_signal_deliver(int sig, struct siginfo *info, struct k_sigaction *ka);</code></pre>
<h2>Arguments</h2>
<p><i>sig</i></p>
<dl>
<dd>
<dd>signal number</dl>
<p> <i>info</i></p>
<dl>
<dd>pointer to struct siginfo</dl>
<p> <i>ka</i></p>
<dl>
<dd>pointer to struct k_sigaction</dl>
<h2>Description</h2>
<p>A &#8216;sig&#8217; signal is delivered to current process with &#8216;info&#8217; siginfo, and it will be handled by &#8216;ka&#8217;. ka-&gt;sa.sa_handler can be SIG_IGN or SIG_DFL. Note that some signals reported by signal_generate tracepoint can be lost, ignored or modified (by debugger) before hitting this tracepoint. This means, this can show which signals are actually delivered, but matching generated signals and delivered signals may not be correct.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
