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
<p> #include &lt;libssh2.h&gt; </p>
<p> void libssh2_trace(LIBSSH2_SESSION *session, int bitmask); </p>
<p> This is a function present in the library that can be used to get debug info from within libssh2 when it is running. Helpful when trying to trace or debug behaviors. Note that this function has no effect unless libssh2 was built to support tracing! It is usually disabled in release builds. </p>
<p> <code>bitmask</code> can be set to the logical OR of none, one or more of these:</p>
<dl>
<dl>
<dt>LIBSSH2_TRACE_SOCKET</dt>
<dd> Socket low-level debugging</dd>
<dt>LIBSSH2_TRACE_TRANS</dt>
<dd> Transport layer debugging</dd>
<dt>LIBSSH2_TRACE_KEX</dt>
<dd> Key exchange debugging</dd>
<dt>LIBSSH2_TRACE_AUTH</dt>
<dd> Authentication debugging</dd>
<dt>LIBSSH2_TRACE_CONN</dt>
<dd> Connection layer debugging</dd>
<dt>LIBSSH2_TRACE_SCP</dt>
<dd> SCP debugging</dd>
<dt>LIBSSH2_TRACE_SFTP</dt>
<dd> SFTP debugging</dd>
<dt>LIBSSH2_TRACE_ERROR</dt>
<dd> Error debugging</dd>
<dt>LIBSSH2_TRACE_PUBLICKEY</dt>
<dd> Public Key debugging</dd></dl>
</dl>
