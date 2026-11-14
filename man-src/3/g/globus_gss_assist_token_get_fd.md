---
title: "globus_gss_assist_token_get_fd(3)"
name: "globus_gss_assist_token_get_fd"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gss_assist_token_get_fd/"
description: "Token Transport –"
---

<h2 class="name">NAME</h2>
<p> Token Transport &#8211; </p>
<p> Send and Receive Security Tokens.</p>
<h3>Functions</h3>
<p> int <code>globus_gss_assist_token_get_fd</code> (void *arg, void **bufp, size_t *sizep)<br />
 <i>Get token from a FILE *. </i><br />
 int <code>globus_gss_assist_token_send_fd</code> (void *arg, void *buf, size_t size)<br />
 <i>Send token via a FILE *. </i><br />
 int <code>globus_gss_assist_token_send_fd_without_length</code> (void *arg, void *buf, size_t size)<br />
 <i>Send token to a FILE *. </i><br />
 int <code>globus_gss_assist_token_send_fd_ex</code> (void *exp, void *buf, size_t size)<br />
 <i>Send a token to a FILE *. </i></p>
<h2>Detailed Description</h2>
<p> Send and Receive Security Tokens. </p>
<p> The functions in this section are used to send and receive GSSAPI tokens using various methods. These are used by the <code>Security Context Management</code> functions.</p>
<h2>Function Documentation</h2>
<h3>int globus_gss_assist_token_get_fd (void *arg, void **bufp, size_t *sizep)</h3>
<p> Get token from a FILE *. Use a open FILE handle to get a token. This function provides parameter types that allow it to be passed to <code>globus_gss_assist_init_sec_context</code> and <code>globus_gss_assist_accept_sec_context</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>arg</i> the FILE * stream cast to a void pointer<br />
 <i>bufp</i> the resulting token<br />
 <i>sizep</i> the size (number of bytes) read into bufp</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success </p>
<dl>
<dt>
<dd> 0 is internal return </p>
</dl>
<p> &lt; 0 is the -errno</dl>
<h3>int globus_gss_assist_token_send_fd (void *arg, void *buf, size_tsize)</h3>
<p> Send token via a FILE *. Write a token to the open FILE handle. Will write it with a 4 byte length. This function provides parameter types that allow it to be passed to <code>globus_gss_assist_init_sec_context</code> and <code>globus_gss_assist_accept_sec_context</code> </p>
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
<h3>int globus_gss_assist_token_send_fd_ex (void *exp, void *buf, size_tsize)</h3>
<p> Send a token to a FILE *. Write a token to the open FILE *. This function will look at the flag to determine if the length field needs to be written. </p>
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
<h3>int globus_gss_assist_token_send_fd_without_length (void *arg, void *buf, size_tsize)</h3>
<p> Send token to a FILE *. Write a token to the open FILE. This function will write it without a length, so that the FILE stream only contains GSSAPI tokens.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gss_assist from the source code. </p>
<h2>Index</h2>
