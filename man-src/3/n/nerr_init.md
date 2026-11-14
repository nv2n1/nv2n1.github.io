---
title: "nerr_init(3)"
name: "nerr_init"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nerr_init/"
description: "nerr_init"
---

<p>nerr_init</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;util/neo_err.h&gt;
</code></pre>
<pre>NEOERR *nerr_init (void);</pre>
<h2>Arguments</h2>
<p>None</p>
<h2>Description</h2>
<p>initialize the NEOERR system. Can be called more than once. Is not thread safe. This registers all of the built in error types as defined at the top of this file. If you don&#8217;t call this, all exceptions will be returned as UnknownError. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nerr_error_traceback/">nerr_error_traceback</a></code>(3), <a href="/docs/linux/man/3-nerr_pass/">nerr_pass</a><code>(3), <a href="/docs/linux/man/3-nerr_error_string/">nerr_error_string</a></code>(3), <a href="/docs/linux/man/3-defined/">defined</a><code>(3), <a href="/docs/linux/man/3-nerr_pass_ctx/">nerr_pass_ctx</a></code>(3), <a href="/docs/linux/man/3-nerr_passf/">nerr_passf</a><code>(3), <a href="/docs/linux/man/3-nerr_init/">nerr_init</a></code>(3), <a href="/docs/linux/man/3-nerr_match/">nerr_match</a><code>(3), <a href="/docs/linux/man/3-nerr_log_error/">nerr_log_error</a></code>(3), <a href="/docs/linux/man/3-nerr_ignore/">nerr_ignore</a><code>(3), <a href="/docs/linux/man/3-nerr_register/">nerr_register</a></code>(3), nerr_handle </p>
