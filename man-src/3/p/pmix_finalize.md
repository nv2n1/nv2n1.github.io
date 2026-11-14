---
title: "pmix_finalize(3)"
name: "pmix_finalize"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmix_finalize/"
---

PMIx_Finalize - Finalize the PMIx Client

<h2>Synopsis</h2>

<pre><code>#include &lt;pmix.h&gt;

pmix_status_t PMIx_Finalize(void);</code></pre>

<h2>Arguments</h2>

<h2>Description</h2>

Finalize the PMIx client, closing the connection with the local PMIx server.

<h2>Return Value</h2>

Returns PMIX_SUCCESS on success. On error, a negative value corresponding to a PMIx errno is returned.

<h2>Errors</h2>

PMIx errno values are defined in pmix_common.h.

<h2>Notes</h2>



<h2>See Also</h2>

<a HREF="/docs/linux/man/3-pmix_init/">PMIx_Init</a>(3)

<h2>Authors</h2>

PMIx.
