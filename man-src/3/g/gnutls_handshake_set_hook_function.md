---
title: "gnutls_handshake_set_hook_function(3)"
name: "gnutls_handshake_set_hook_function"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_handshake_set_hook_function/"
description: "gnutls_handshake_set_hook_function – API function"
---

<h2>NAME</h2>
<p> gnutls_handshake_set_hook_function &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/gnutls.h&gt;</code> </p>
<p> <code>void gnutls_handshake_set_hook_function(gnutls_session_t </code><i>session</i><code>, unsigned int </code><i>htype</i><code>, int </code><i>post</i><code>, gnutls_handshake_hook_func </code><i>func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_session_t session</p>
<dd> is a <code>gnutls_session_t</code> structure</p>
<dt>unsigned int htype</p>
<dd> the <code>gnutls_handshake_description_t</code> of the message to hook at</p>
<dt>int post</p>
<dd> <code>GNUTLS_HOOK_</code>* depending on when the hook function should be called</p>
<dt>gnutls_handshake_hook_func func</p>
<dd> is the function to be called</dl>
<h2>DESCRIPTION</h2>
<p> This function will set a callback to be called after or before the specified handshake message has been received or generated. This is a generalization of <code>gnutls_handshake_set_post_client_hello_function()</code>. </p>
<p> To call the hook function prior to the message being sent/generated use <code>GNUTLS_HOOK_PRE</code> as <i>post</i> parameter, <code>GNUTLS_HOOK_POST</code> to call after, and <code>GNUTLS_HOOK_BOTH</code> for both cases. </p>
<p> This callback must return 0 on success or a gnutls error code to terminate the handshake. </p>
<p> Note to hook at all handshake messages use an <i>htype</i> of <code>GNUTLS_HANDSHAKE_ANY</code>.</p>
<h2>WARNING</h2>
<p> You should not use this function to terminate the handshake based on client input unless you know what you are doing. Before the handshake is finished there is no way to know if there is a man-in-the-middle attack being performed.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;.<br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></p>
<dd> </code></dl>
<h2>Index</h2>
