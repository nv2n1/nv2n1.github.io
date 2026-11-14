---
title: "hx509_peer_info_alloc(3)"
name: "hx509_peer_info_alloc"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_peer_info_alloc/"
description: "hx509 certificate selecting functions –"
---

<h2 class="name">NAME</h2>
<p> hx509 certificate selecting functions &#8211; </p>
<h3>Functions</h3>
<p> int <code>hx509_peer_info_add_cms_alg</code> (hx509_context, hx509_peer_info, const AlgorithmIdentifier *) </p>
<p> int <code>hx509_peer_info_alloc</code> (hx509_context, hx509_peer_info *) </p>
<p> void <code>hx509_peer_info_free</code> (hx509_peer_info) </p>
<p> int <code>hx509_peer_info_set_cert</code> (hx509_peer_info, hx509_cert) </p>
<p> int <code>hx509_peer_info_set_cms_algs</code> (hx509_context, hx509_peer_info, const AlgorithmIdentifier *, size_t) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>int hx509_peer_info_add_cms_alg (hx509_contextcontext, hx509_peer_infopeer, const AlgorithmIdentifier *val)</h3>
<p> Add an additional algorithm that the peer supports. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>peer</i> the peer to set the new algorithms for<br />
 <i>val</i> an AlgorithmsIdentier to add</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_peer_info_alloc (hx509_contextcontext, hx509_peer_info *peer)</h3>
<p> Allocate a new peer info structure an init it to default values. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>peer</i> return an allocated peer, free with <code>hx509_peer_info_free()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>void hx509_peer_info_free (hx509_peer_infopeer)</h3>
<p> Free a peer info structure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>peer</i> peer info to be freed.</dl>
<h3>int hx509_peer_info_set_cert (hx509_peer_infopeer, hx509_certcert)</h3>
<p> Set the certificate that remote peer is using. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>peer</i> peer info to update<br />
 <i>cert</i> cerificate of the remote peer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_peer_info_set_cms_algs (hx509_contextcontext, hx509_peer_infopeer, const AlgorithmIdentifier *val, size_tlen)</h3>
<p> Set the algorithms that the peer supports. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>peer</i> the peer to set the new algorithms for<br />
 <i>val</i> array of supported AlgorithmsIdentiers<br />
 <i>len</i> length of array val.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalx509library from the source code. </p>
<h2>Index</h2>
