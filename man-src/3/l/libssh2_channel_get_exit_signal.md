---
title: "libssh2_channel_get_exit_signal(3)"
name: "libssh2_channel_get_exit_signal"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_get_exit_signal/"
---

<h2>NAME</h2>

 libssh2_channel_get_exit_signal - get the remote exit signal

<h2>SYNOPSIS</h2>

 #include &lt;libssh2.h&gt; 

 int libssh2_channel_get_exit_signal(LIBSSH2_CHANNEL *channel, char **exitsignal, size_t *exitsignal_len, char **errmsg, size_t *errmsg_len, char **langtag, size_t *langtag_len); 

<h2>DESCRIPTION</h2>

 <i>channel</i> - Closed channel stream to retrieve exit signal from. 

 <i>exitsignal</i> - If not NULL, is populated by reference with the exit signal (without leading &quot;SIG&quot;). Note that the string is stored in a newly allocated buffer. If the remote program exited cleanly, the referenced string pointer will be set to NULL. 

 <i>exitsignal_len</i> - If not NULL, is populated by reference with the length of exitsignal. 

 <i>errmsg</i> - If not NULL, is populated by reference with the error message (if provided by remote server, if not it will be set to NULL). Note that the string is stored in a newly allocated buffer. 

 <i>errmsg_len</i> - If not NULL, is populated by reference with the length of errmsg. 

 <i>langtag</i> - If not NULL, is populated by reference with the language tag (if provided by remote server, if not it will be set to NULL). Note that the string is stored in a newly allocated buffer. 

 <i>langtag_len</i> - If not NULL, is populated by reference with the length of langtag. 

<h2>RETURN VALUE</h2>

 Numeric error code corresponding to the the Error Code constants. 

<h2>Index</h2>


