---
title: "nerr_pass_ctx(3)"
name: "nerr_pass_ctx"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nerr_pass_ctx/"
description: "nerr_pass_ctx"
---

<p>nerr_pass_ctx</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;util/neo_err.h&gt;
</code></pre>
<pre>nerr_pass_ctx()</pre>
<h2>Arguments</h2>
<p>with the macro, the function name, file and lineno are<br />
 automagically recorded. Just pass the error and<br />
 a printf format string giving more information about where<br />
 the error is occuring.</p>
<h2>Description</h2>
<p>this function is used to pass an error up a level in the call chain (ie, if the error isn&#8217;t handled at the current level). This allows us to track the traceback of the error. This version includes context information about lower errors </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nerr_error_traceback/">nerr_error_traceback</a></code>(3), <a href="/docs/linux/man/3-nerr_pass/">nerr_pass</a><code>(3), <a href="/docs/linux/man/3-nerr_error_string/">nerr_error_string</a></code>(3), <a href="/docs/linux/man/3-defined/">defined</a><code>(3), <a href="/docs/linux/man/3-nerr_pass_ctx/">nerr_pass_ctx</a></code>(3), <a href="/docs/linux/man/3-nerr_passf/">nerr_passf</a><code>(3), <a href="/docs/linux/man/3-nerr_init/">nerr_init</a></code>(3), <a href="/docs/linux/man/3-nerr_match/">nerr_match</a><code>(3), <a href="/docs/linux/man/3-nerr_log_error/">nerr_log_error</a></code>(3), <a href="/docs/linux/man/3-nerr_ignore/">nerr_ignore</a><code>(3), <a href="/docs/linux/man/3-nerr_register/">nerr_register</a></code>(3), nerr_handle </p>
