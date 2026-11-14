---
title: "libssh2_publickey_add_ex(3)"
name: "libssh2_publickey_add_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_publickey_add_ex/"
---

<h2>NAME</h2>

 libssh2_publickey_add_ex - Add a public key entry

<h2>SYNOPSIS</h2>

 #include &lt;libssh2.h&gt; 

 int libssh2_publickey_add_ex(LIBSSH2_PUBLICKEY *pkey, const unsigned char *name, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned long name_len, const unsigned char&nbsp;<wbr>*blob, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned long blob_len, char overwrite, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned long num_attrs, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>const libssh2_publickey_attribute attrs[]) 

<h2>DESCRIPTION</h2>

 TBD

<h2>RETURN VALUE</h2>

 Returns 0 on success, negative on failure.

<h2>ERRORS</h2>

 LIBSSH2_ERROR_BAD_USE LIBSSH2_ERROR_ALLOC, LIBSSH2_ERROR_EAGAIN LIBSSH2_ERROR_SOCKET_SEND, LIBSSH2_ERROR_SOCKET_TIMEOUT, LIBSSH2_ERROR_PUBLICKEY_PROTOCOL,

<h2>SEE ALSO</h2>

 

<h2>Index</h2>


