---
title: "pmix_commit(3)"
name: "pmix_commit"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmix_commit/"
---

PMIx_Commit - Push all previously PMIxPut_ values to the local PMIx server.

<h2>Synopsis</h2>

<pre><code>#include &lt;pmix.h&gt;

pmix_status_t PMIx_Commit(void);</code></pre>

<h2>Arguments</h2>

none

<h2>Description</h2>

This is an asynchronous operation - the library will immediately return to the caller while the data is transmitted to the local server in the background

<h2>Return Value</h2>

Returns PMIX_SUCCESS on success. On error, a negative value corresponding to a PMIx errno is returned.

<h2>Errors</h2>

PMIx errno values are defined in pmix_common.h.

<h2>Notes</h2>



<h2>See Also</h2>

<a HREF="/docs/linux/man/3-pmix_put/">PMIx_Put</a>(3)

<h2>Authors</h2>

PMIx.
