---
title: "libssh2_channel_get_exit_status(3)"
name: "libssh2_channel_get_exit_status"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_get_exit_status/"
---

<h2>NAME</h2>

 libssh2_channel_get_exit_status - get the remote exit code

<h2>SYNOPSIS</h2>

 #include &lt;libssh2.h&gt; 

 int libssh2_channel_get_exit_status(LIBSSH2_CHANNEL* channel) 

<h2>DESCRIPTION</h2>

 <i>channel</i> - Closed channel stream to retreive exit status from. 

 Returns the exit code raised by the process running on the remote host at the other end of the named channel. Note that the exit status may not be available if the remote end has not yet set its status to closed. 

<h2>RETURN VALUE</h2>

 Returns 0 on failure, otherwise the <i>Exit Status</i> reported by remote host 

<h2>Index</h2>


