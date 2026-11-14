---
title: "nerr_handle(3)"
name: "nerr_handle"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nerr_handle/"
description: "nerr_handle"
---

<p>nerr_handle</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;util/neo_err.h&gt;

int nerr_handle(NEOERR **err, NERR_TYPE type);
</code></pre>
<h2>Arguments</h2>
<p>err &#8211; pointer to a pointer NEOERR<br />
 type &#8211; the NEOERR type, as registered with nerr_register</p>
<h2>Description</h2>
<p>nerr_handle is a convenience function. It is the equivalent of nerr_match, but it will also deallocate the error chain on a match. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nerr_error_traceback/">nerr_error_traceback</a></code>(3), <a href="/docs/linux/man/3-nerr_pass/">nerr_pass</a><code>(3), <a href="/docs/linux/man/3-nerr_error_string/">nerr_error_string</a></code>(3), <a href="/docs/linux/man/3-defined/">defined</a><code>(3), <a href="/docs/linux/man/3-nerr_pass_ctx/">nerr_pass_ctx</a></code>(3), <a href="/docs/linux/man/3-nerr_passf/">nerr_passf</a><code>(3), <a href="/docs/linux/man/3-nerr_init/">nerr_init</a></code>(3), <a href="/docs/linux/man/3-nerr_match/">nerr_match</a><code>(3), <a href="/docs/linux/man/3-nerr_log_error/">nerr_log_error</a></code>(3), <a href="/docs/linux/man/3-nerr_ignore/">nerr_ignore</a><code>(3), <a href="/docs/linux/man/3-nerr_register/">nerr_register</a></code>(3), nerr_handle </p>
