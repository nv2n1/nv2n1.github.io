---
title: "ne_set_session_flag(3)"
name: "ne_set_session_flag"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_set_session_flag/"
description: "ne_set_session_flag, ne_get_session_flag – set and retrieve session flags"
---

<p>ne_set_session_flag, ne_get_session_flag &#8211; set and retrieve session flags</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_request.h&gt;

void ne_set_session_flag(ne_session *sess, ne_session_flag flag, int value);

int ne_get_session_flag(ne_session *sess, ne_session_flag flag);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_set_session_flag</code> function enables or disables a session flag. Passing a non-zero <i>value</i> argument enables the flag, and zero disables it. </p>
<p> The following flags are defined: </p>
<p> <code>NE_SESSFLAG_PERSIST</code></p>
<dl>
<dd>disable this flag to prevent use of persistent connections</dl>
<p> <code>NE_SESSFLAG_ICYPROTO</code></p>
<dl>
<dd>enable this flag to enable support for non-HTTP ShoutCast-style &quot;ICY&quot; responses</dl>
<p> <code>NE_SESSFLAG_SSLv2</code></p>
<dl>
<dd>disable this flag to disable support for the SSLv2 protocol</dl>
<p> <code>NE_SESSFLAG_RFC4918</code></p>
<dl>
<dd>enable this flag to enable support for RFC4918-only WebDAV features; losing backwards-compatibility with RFC2518 servers</dl>
<p> <code>NE_SESSFLAG_CONNAUTH</code></p>
<dl>
<dd>enable this flag if an RFC-violating connection-based HTTP authentication scheme is in use</dl>
<p> <code>NE_SESSFLAG_TLS_SNI</code></p>
<dl>
<dd>disable this flag if a server is used which does not correctly support the TLS SNI extension</dl>
<p> <code>NE_SESSFLAG_EXPECT100</code></p>
<dl>
<dd>enable this flag to enable the request flag <code>NE_REQFLAG_EXPECT100</code> for new requests</dl>
<h2>Return Value</h2>
<p>The <code>ne_get_session_flag</code> function returns zero if a flag is disabled, less than zero if the flag is not supported, or greater than zero if the flag is enabled.</p>
<h2>See Also</h2>
<p>ne_session_create, ne_set_request_flag.</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
