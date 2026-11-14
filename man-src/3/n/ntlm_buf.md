---
title: "ntlm_buf(3)"
name: "ntlm_buf"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ntlm_buf/"
description: "ntlm_buf –"
---

<p>ntlm_buf &#8211;</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;heimntlm.h&gt;

Data Fields
size_t length



void * data</code></pre>
<h2>Detailed Description</h2>
<p>Buffer for storing data in the NTLM library. When filled in by the library it should be freed with <code>heim_ntlm_free_buf()</code>. </p>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h2>Field Documentation</h2>
<h3>void* ntlm_buf::data</h3>
<p>pointer to the data itself </p>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h3>size_t ntlm_buf::length</h3>
<p>length buffer data </p>
<p> <code>Examples: </code> <code>test_ntlm.c</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Heimdalntlmlibrary from the source code.</p>
