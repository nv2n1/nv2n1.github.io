---
title: "iv_fatal(3)"
name: "iv_fatal"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_fatal/"
description: "iv_fatal, iv_set_fatal_msg_handler – ivykis fatal error condition handling"
---

<h2>NAME</h2>
<p> iv_fatal, iv_set_fatal_msg_handler &#8211; ivykis fatal error condition handling</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;iv.h&gt;</code> </p>
<p> <code>void iv_fatal(const char *</code><i>fmt</i><code>, &#8230;);</code><br />
 <code>void iv_set_fatal_msg_handler(void (*</code><i>handler</i><code>)(const char *</code><i>msg</i><code>));</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>iv_fatal</code> aborts the running program, after possibly emitting an error message. The <code>fmt</code> parameter is a <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3)-style format string, the message to be logged. </p>
<p> If no handler is set (the default), the formatted message will be sent to <code>syslog</code>, with critical severity. Otherwise the <code>handler</code> as set by <code>iv_set_fatal_msg_handler</code> will be used instead. </p>
<p> <code>iv_fatal</code> is also used internally by ivykis, whenever a fatal situation is detected. </p>
<p> <code>iv_set_fatal_msg_handler</code> can be used to set an alternative (as opposed to <code>syslog</code>) function to call from <code>iv_fatal</code>, and its argument should be a function that does not return, and takes a single string as argument &#8211; the formatted error message.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_examples/">iv_examples</a></code>(3) </p>
<h2>Index</h2>
