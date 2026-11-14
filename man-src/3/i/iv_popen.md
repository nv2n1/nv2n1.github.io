---
title: "iv_popen(3)"
name: "iv_popen"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_popen/"
description: "IV_POPEN_REQUEST_INIT, iv_popen_request_submit, iv_popen_request_close – popen(3) for ivykis applications"
---

<h2>NAME</h2>
<p> IV_POPEN_REQUEST_INIT, iv_popen_request_submit, iv_popen_request_close &#8211; <code><a href="/docs/linux/man/3-popen/">popen</a></code>(3) for ivykis applications</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;iv_popen.h&gt;</code> </p>
<pre><code>
struct iv_popen_request {
    char *file;
    char **argv;
    char *type;
};
</code></pre>
<p> <code>void IV_POPEN_REQUEST_INIT(struct iv_popen_request *</code><i>this</i><code>);</code><br />
 <code>int iv_popen_request_submit(struct iv_popen_request *</code><i>this</i><code>);</code><br />
 <code>void iv_popen_request_close(struct iv_popen_request *</code><i>this</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>iv_popen</code> provides <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3) applications with an asynchronous version of <code><a href="/docs/linux/man/3-popen/">popen</a></code>(3) that is integrated with the ivykis event loop. </p>
<p> After initialising a <code>struct iv_popen_request</code> object using <code>IV_POPEN_REQUEST_INIT</code> and assigning its <code>-&gt;file</code> and <code>-&gt;argv</code> and <code>-&gt;type</code> members, one can call <code>iv_popen_request_submit</code> on it to fork off a child process which will call <code><a href="/docs/linux/man/2-execvp/">execvp</a>(2)</code> on <code>-&gt;file</code> and <code>-&gt;argv,</code> while in the parent process returning a file descriptor that is connected to the child&#8217;s standard input (if <code>-&gt;type</code> equals &quot;w&quot;) or standard output (if <code>-&gt;type</code> equals &quot;r&quot;). </p>
<p> When the application is done with the child process, it should call <code>iv_popen_request_close,</code> and close the file descriptor returned by <code>iv_popen_request_submit</code> (this is not done automatically). </p>
<p> <code>iv_popen</code> will continue to monitor the child&#8217;s process state while it is running, by registering an <code><a href="/docs/linux/man/3-iv_wait/">iv_wait</a></code>(3) interest for its process ID. </p>
<p> If the child process has not yet terminated when <code>iv_popen_request_close</code> is called, <code>iv_popen</code> will attempt to terminate the child process in the background by sending it a series of SIGTERM and SIGKILL signals. </p>
<p> <code>iv_popen_request_close</code> must be called from the same thread that <code>iv_popen_request_submit</code> was called from on this object. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_wait/">iv_wait</a></code>(3), <code><a href="/docs/linux/man/2-execvp/">execvp</a></code>(2), <code><a href="/docs/linux/man/3-popen/">popen</a></code>(3) </p>
<h2>Index</h2>
