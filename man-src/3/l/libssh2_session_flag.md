---
title: "libssh2_session_flag(3)"
name: "libssh2_session_flag"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_flag/"
---

<h2>NAME</h2>

 libssh2_session_flag - TODO

<h2>SYNOPSIS</h2>

 int libssh2_session_flag(LIBSSH2_SESSION *session, int flag, int value);

<h2>DESCRIPTION</h2>

 Set options for the created session. <i>flag</i> is the option to set, while <i>value</i> is typically set to 1 or 0 to enable or disable the option.

<h2>FLAGS</h2>

<dl>
<dt>LIBSSH2_FLAG_SIGPIPE
<dd> If set, libssh2 will not attempt to block SIGPIPEs but will let them trigger from the underlying socket layer.
<dt>LIBSSH2_FLAG_COMPRESS
<dd> If set - before the connection negotiation is performed - libssh2 will try to negotiate compression enabling for this connection. By default libssh2 will not attempt to use compression.</dl>

<h2>RETURN VALUE</h2>

 Returns regular libssh2 error code.

<h2>AVAILABILITY</h2>

 This function has existed since the age of dawn. LIBSSH2_FLAG_COMPRESS was added in version 1.2.8.

<h2>SEE ALSO</h2>

 

<h2>Index</h2>


