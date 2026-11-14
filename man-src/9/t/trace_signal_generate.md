---
title: "trace_signal_generate(9)"
name: "trace_signal_generate"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_signal_generate/"
description: "trace_signal_generate – called when a signal is generated"
---

<p>trace_signal_generate &#8211; called when a signal is generated</p>
<h2>Synopsis</h2>
<pre><code>void trace_signal_generate(int sig, struct siginfo *info, struct task_struct *task, int group, int result);</code></pre>
<h2>Arguments</h2>
<p><i>sig</i></p>
<dl>
<dd>
<dd>signal number</dl>
<p> <i>info</i></p>
<dl>
<dd>pointer to struct siginfo</dl>
<p> <i>task</i></p>
<dl>
<dd>pointer to struct task_struct</dl>
<p> <i>group</i></p>
<dl>
<dd>shared or private</dl>
<p> <i>result</i></p>
<dl>
<dd>TRACE_SIGNAL_*</dl>
<h2>Description</h2>
<p>Current process sends a &#8216;sig&#8217; signal to &#8216;task&#8217; process with &#8216;info&#8217; siginfo. If &#8216;info&#8217; is SEND_SIG_NOINFO or SEND_SIG_PRIV, &#8216;info&#8217; is not a pointer and you can&#8217;t access its field. Instead, SEND_SIG_NOINFO means that si_code is SI_USER, and SEND_SIG_PRIV means that si_code is SI_KERNEL.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
