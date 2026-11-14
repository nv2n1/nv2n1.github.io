---
title: "nerr_register(3)"
name: "nerr_register"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nerr_register/"
description: "nerr_register"
---

<p>nerr_register</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;util/neo_err.h&gt;
</code></pre>
<pre>NEOERR *nerr_register (NERR_TYPE *err, const char *name);</pre>
<h2>Arguments</h2>
<p>err &#8211; pointer to a NERR_TYPE<br />
 name &#8211; pretty name for the error type</p>
<h2>Description</h2>
<p>register an error type. This will assign a numeric value to the type, and keep track of the &quot;pretty name&quot; for it. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nerr_error_traceback/">nerr_error_traceback</a></code>(3), <a href="/docs/linux/man/3-nerr_pass/">nerr_pass</a><code>(3), <a href="/docs/linux/man/3-nerr_error_string/">nerr_error_string</a></code>(3), <a href="/docs/linux/man/3-defined/">defined</a><code>(3), <a href="/docs/linux/man/3-nerr_pass_ctx/">nerr_pass_ctx</a></code>(3), <a href="/docs/linux/man/3-nerr_passf/">nerr_passf</a><code>(3), <a href="/docs/linux/man/3-nerr_init/">nerr_init</a></code>(3), <a href="/docs/linux/man/3-nerr_match/">nerr_match</a><code>(3), <a href="/docs/linux/man/3-nerr_log_error/">nerr_log_error</a></code>(3), <a href="/docs/linux/man/3-nerr_ignore/">nerr_ignore</a><code>(3), <a href="/docs/linux/man/3-nerr_register/">nerr_register</a></code>(3), nerr_handle </p>
