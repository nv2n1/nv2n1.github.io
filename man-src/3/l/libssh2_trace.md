---
title: "libssh2_trace(3)"
name: "libssh2_trace"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_trace/"
description: "libssh2_trace – enable debug info from inside libssh2"
---

<h2>NAME</h2>
<p> libssh2_trace &#8211; enable debug info from inside libssh2</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> void libssh2_trace(LIBSSH2_SESSION *session, int bitmask); </p>
<h2>DESCRIPTION</h2>
<p> This is a function present in the library that can be used to get debug info from within libssh2 when it is running. Helpful when trying to trace or debug behaviors. Note that this function has no effect unless libssh2 was built to support tracing! It is usually disabled in release builds. </p>
<p> <code>bitmask</code> can be set to the logical OR of none, one or more of these:</p>
<dl>
<dt>
<dd>
<dl>
<dt>LIBSSH2_TRACE_SOCKET</p>
<dd> Socket low-level debugging</p>
<dt>LIBSSH2_TRACE_TRANS</p>
<dd> Transport layer debugging</p>
<dt>LIBSSH2_TRACE_KEX</p>
<dd> Key exchange debugging</p>
<dt>LIBSSH2_TRACE_AUTH</p>
<dd> Authentication debugging</p>
<dt>LIBSSH2_TRACE_CONN</p>
<dd> Connection layer debugging</p>
<dt>LIBSSH2_TRACE_SCP</p>
<dd> SCP debugging</p>
<dt>LIBSSH2_TRACE_SFTP</p>
<dd> SFTP debugging</p>
<dt>LIBSSH2_TRACE_ERROR</p>
<dd> Error debugging</p>
<dt>LIBSSH2_TRACE_PUBLICKEY</p>
<dd> Public Key debugging</dl>
</dl>
<h2>Index</h2>
