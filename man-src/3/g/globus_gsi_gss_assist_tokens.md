---
title: "globus_gsi_gss_assist_tokens(3)"
name: "globus_gsi_gss_assist_tokens"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_gss_assist_tokens/"
description: "Security Token Transport –"
---

<h2 class="name">NAME</h2>
<p> Security Token Transport &#8211; </p>
<p> Token routines using fread and fwrite.</p>
<h3>Token Get File Descriptor</h3>
<p>&nbsp;<wbr><br />
 int <code>globus_gss_assist_token_get_fd</code> (void *arg, void **bufp, size_t *sizep) </p>
<h3>Token Send File Descriptor</h3>
<p>&nbsp;<wbr><br />
 int <code>globus_gss_assist_token_send_fd</code> (void *arg, void *buf, size_t size) </p>
<h3>Token Send File Descriptor Without Length</h3>
<p>&nbsp;<wbr><br />
 int <code>globus_gss_assist_token_send_fd_without_length</code> (void *arg, void *buf, size_t size) </p>
<h3>Token Send File Descriptor Flag EX</h3>
<p>&nbsp;<wbr><br />
 int <code>globus_gss_assist_token_send_fd_ex</code> (void *exp, void *buf, size_t size) </p>
<h2>Detailed Description</h2>
<p> Token routines using fread and fwrite. </p>
<p> Additional code has been added to detect tokens which are sent without a length field. These can currently be only SSL tokens. This does require some knowledge of the underlying GSSAPI, by the application, but is within the guidelines of the GSSAPI specifications. </p>
<p> The get routine will automaticly attempt this test, while a new send routine will check a flag. The old send routine will work as before, sending a 4-byte length.</p>
<h2>Function Documentation</h2>
<h3>int globus_gss_assist_token_get_fd (void * arg, void ** bufp, size_t * sizep)</h3>
<p> Use a open file discriptor to get a token. This function provides parameter types that allow it to be passed to <code>globus_gss_assist_init_sec_context</code> and <code>globus_gss_assist_accept_sec_context</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>arg</i> the FILE * stream cast to a void pointer<br />
 <i>bufp</i> the resulting token<br />
 <i>sizep</i> the size (number of bytes) read into bufp</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success &gt; 0 is internal return &lt; 0 is the -errno</dl>
<h3>int globus_gss_assist_token_send_fd (void * arg, void * buf, size_t size)</h3>
<p> Write a token to the open file descriptor. WIll write it with a 4 byte length. This function provides parameter types that allow it to be passed to <code>globus_gss_assist_init_sec_context</code> and <code>globus_gss_assist_accept_sec_context</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>arg</i> the FILE * stream to send the token on<br />
 <i>buf</i> the token<br />
 <i>size</i> the size of the token in bytes</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success &gt;0 on error &lt;0 on errno error</dl>
<h3>int globus_gss_assist_token_send_fd_without_length (void * arg, void * buf, size_t size)</h3>
<p> Write a token to the open file descripter. Will write it without a length. so as to</p>
<h3>int globus_gss_assist_token_send_fd_ex (void * exp, void * buf, size_t size)</h3>
<p> Write a token to the open file descripter. will look at the flag to determine if the length field need to be written. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>exp</i> the globus_gss_assist_ex variable that holds the FILE * stream and flags to bet set<br />
 <i>buf</i> the token buffer to send<br />
 <i>size</i> size of the token buffer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success &gt;0 on error &lt;0 on errno error (-errno)</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus gss assist from the source code. </p>
<h2>Index</h2>
