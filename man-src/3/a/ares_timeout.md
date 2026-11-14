---
title: "ares_timeout(3)"
name: "ares_timeout"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_timeout/"
description: "ares_timeout – return maximum time to wait"
---

<h2>NAME</h2>
<p> ares_timeout &#8211; return maximum time to wait</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
struct timeval *ares_timeout(ares_channel channel,
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_timeout</code> function determines the maximum time for which the caller should wait before invoking <i><a href="/docs/linux/man/3-ares_process/">ares_process</a>(3)</i> to process timeouts. The parameter <i>maxtv</i> specifies a existing maximum timeout, or <code>NULL</code> if the caller does not wish to apply a maximum timeout. The parameter <i>tv</i> must point to a writable buffer of type <code>struct timeval</code>. It is valid for <i>maxtv</i> and <i>tv</i> to have the same value. </p>
<p> If no queries have timeouts pending sooner than the given maximum timeout, <code>ares_timeout</code> returns the value of <i>maxtv;</i> otherwise <code>ares_timeout</code> stores the appropriate timeout value into the buffer pointed to by <i>tv</i> and returns the value of <i>tv</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_fds/">ares_fds</a></code>(3), <code><a href="/docs/linux/man/3-ares_process/">ares_process</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Greg Hudson, MIT Information Systems<br />
 Copyright 1998 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
