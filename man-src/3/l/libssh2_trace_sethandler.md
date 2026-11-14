---
title: "libssh2_trace_sethandler(3)"
name: "libssh2_trace_sethandler"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_trace_sethandler/"
description: "libssh2_trace_sethandler – set a trace output handler"
---

<h2>NAME</h2>
<p> libssh2_trace_sethandler &#8211; set a trace output handler</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
typedef void (*libssh2_trace_handler_func)(LIBSSH2_SESSION *session,
                                           void *context,
                                           const char *data,
                                           size_t length);
int libssh2_trace_sethandler(LIBSSH2_SESSION *session,
                             void *context,
                             libssh2_trace_handler_func callback);
</code></pre>
<h2>DESCRIPTION</h2>
<p> libssh2_trace_sethandler installs a trace output handler for your application. By default, when tracing has been switched on via a call to libssh2_trace(), all output is written to stderr. By calling this method and passing a function pointer that matches the libssh2_trace_handler_func prototype, libssh2 will call back as it generates trace output. This can be used to capture the trace output and put it into a log file or diagnostic window. This function has no effect unless libssh2 was built to support this option, and a typical &quot;release build&quot; might not. </p>
<p> <code>context</code> can be used to pass arbitrary user defined data back into the callback when invoked.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 version 1.2.3 </p>
<h2>Index</h2>
