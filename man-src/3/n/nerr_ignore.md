---
title: "nerr_ignore(3)"
name: "nerr_ignore"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nerr_ignore/"
description: "nerr_ignore"
---

<p>nerr_ignore</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;util/neo_err.h&gt;

void nerr_ignore(NEOERR **err);
</code></pre>
<h2>Description</h2>
<p>you should only call this if you actually handle the error (should I rename it?). Free&#8217;s the error chain. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-nerr_error_traceback/">nerr_error_traceback</a></code>(3), <a href="/docs/linux/man/3-nerr_pass/">nerr_pass</a><code>(3), <a href="/docs/linux/man/3-nerr_error_string/">nerr_error_string</a></code>(3), <a href="/docs/linux/man/3-defined/">defined</a><code>(3), <a href="/docs/linux/man/3-nerr_pass_ctx/">nerr_pass_ctx</a></code>(3), <a href="/docs/linux/man/3-nerr_passf/">nerr_passf</a><code>(3), <a href="/docs/linux/man/3-nerr_init/">nerr_init</a></code>(3), <a href="/docs/linux/man/3-nerr_match/">nerr_match</a><code>(3), <a href="/docs/linux/man/3-nerr_log_error/">nerr_log_error</a></code>(3), <a href="/docs/linux/man/3-nerr_ignore/">nerr_ignore</a><code>(3), <a href="/docs/linux/man/3-nerr_register/">nerr_register</a></code>(3), nerr_handle </p>
