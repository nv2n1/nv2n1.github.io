---
title: "iv_fd_pump_init(3)"
name: "iv_fd_pump_init"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_fd_pump_init/"
description: "IV_FD_PUMP_INIT, iv_fd_pump_init, iv_fd_pump_destroy, iv_fd_pump_pump, iv_fd_pump_is_done – pump data between file descriptors"
---

<h2>NAME</h2>
<p> IV_FD_PUMP_INIT, iv_fd_pump_init, iv_fd_pump_destroy, iv_fd_pump_pump, iv_fd_pump_is_done &#8211; pump data between file descriptors</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;iv_fd_pump.h&gt;</code> </p>
<pre><code>
struct iv_fd_pump {
    int from_fd;
    int to_fd;
    void *cookie;
    void (*set_bands)(void *cookie, int pollin, int pollout);
    unsigned int flags;
};
</code></pre>
<p> <code>void IV_FD_PUMP_INIT(struct iv_fd_pump *</code><i>this</i><code>);</code><br />
 <code>void iv_fd_pump_init(struct iv_fd_pump *</code><i>this</i><code>);</code><br />
 <code>void iv_fd_pump_destroy(struct iv_fd_pump *</code><i>this</i><code>);</code><br />
 <code>int iv_fd_pump_pump(struct iv_fd_pump *</code><i>this</i><code>);</code><br />
 <code>int iv_fd_pump_is_done(struct iv_fd_pump *</code><i>this</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>iv_fd_pump</code> provides a way for moving data between two file descriptors. </p>
<p> To set up <code>iv_fd_pump</code> for moving data, call <code>IV_FD_PUMP_INIT</code> on a <code>struct iv_fd_pump</code> object, fill in the <code>-&gt;from_fd, -&gt;to_fd, -&gt;cookie, -&gt;set_bands</code> and <code>-&gt;flags</code> members, and then call <code>iv_fd_pump_init</code> on the object. </p>
<p> Conversely, to destroy a <code>struct iv_fd_pump</code> object, call <code>iv_fd_pump_destroy.</code> There are no restrictions on when this function can be called. </p>
<p> A call to <code>iv_fd_pump_pump</code> will attempt to move data from <code>-&gt;from_fd</code> to <code>-&gt;to_fd</code> via an internal buffer associated with the <code>struct iv_fd_pump</code> object. </p>
<p> During calls to <code>iv_fd_pump_init,</code> <code>iv_fd_pump_destroy</code> and <code>iv_fd_pump_pump,</code> the callback function specified by <code>-&gt;set_bands</code> may be invoked (with <code>-&gt;cookie</code> as its first argument), by which <code>iv_fd_pump</code> indicates under which circumstances it wishes for future invocations of <code>iv_fd_pump_pump</code> to be done. </p>
<p> If the <code>pollin</code> argument to <code>-&gt;set_bands</code> is true, there is space left in the internal buffer (and we have not yet seen an end-of-file condition on input), and so you should call <code>iv_fd_pump_pump</code> again when there is a POLLIN condition on <code>-&gt;from_fd.</code> </p>
<p> If the <code>pollout</code> argument to <code>-&gt;set_bands</code> is true, there is data in the internal buffer that could not all be transferred to <code>-&gt;to_fd,</code> and so you should call <code>iv_fd_pump_pump</code> again when there is a POLLOUT condition on <code>-&gt;to_fd.</code> </p>
<p> If <code>IV_FD_PUMP_FLAG_RELAY_EOF</code> is set in <code>-&gt;flags,</code> <code>iv_fd_pump_pump</code> will call <code><a href="/docs/linux/man/2-shutdown/">shutdown</a></code>(2) on <code>-&gt;to_fd</code> with <code>SHUT_WR</code> as its second argument upon seeing an end-of-file condition on <code>-&gt;from_fd</code> (but only after all data from the internal buffer has been drained into <code>-&gt;to_fd</code> first). </p>
<p> <code>iv_fd_pump_pump</code> will return -1 if there was an error, 0 if we&#8217;re done pumping data (meaning that an end-of-file condition was seen on the input file descriptor and that all data in the internal buffer has been drained into the output file descriptor), or 1 if there is more data left to be pumped. </p>
<p> <code>iv_fd_pump_is_done</code> will return a true value if iv_fd_pump_pump has previously returned 0, otherwise it will return false. </p>
<p> Internally, <code>iv_fd_pump_pump</code> will use <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2) if it is available, otherwise it will fall back to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-write/">write</a></code>(2). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2) </p>
<h2>Index</h2>
