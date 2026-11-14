---
title: "libssh2_knownhost_init(3)"
name: "libssh2_knownhost_init"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_knownhost_init/"
description: "libssh2_knownhost_init – init a collection of known hosts"
---

<h2>NAME</h2>
<p> libssh2_knownhost_init &#8211; init a collection of known hosts</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> LIBSSH2_KNOWNHOSTS *libssh2_knownhost_init(LIBSSH2_SESSION *session);</p>
<h2>DESCRIPTION</h2>
<p> Init a collection of known hosts for this session. Returns the handle to an internal representation of a known host collection. </p>
<p> Call <code><a href="/docs/linux/man/3-libssh2_knownhost_free/">libssh2_knownhost_free</a>(3)</code> to free the collection again after you&#8217;re doing using it.</p>
<h2>RETURN VALUE</h2>
<p> Returns a handle pointer or NULL if something went wrong. The returned handle is used as input to all other known host related functions libssh2 provides.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_knownhost_free/">libssh2_knownhost_free</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_add/">libssh2_knownhost_add</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_check/">libssh2_knownhost_check</a>(3)</code> </p>
<h2>Index</h2>
