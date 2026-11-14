---
title: "libssh2_base64_decode(3)"
name: "libssh2_base64_decode"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_base64_decode/"
---

<h2>NAME</h2>

 libssh2_base64_decode - decode a base64 encoded string

<h2>SYNOPSIS</h2>

 #include &lt;libssh2.h&gt; 

 int libssh2_base64_decode(LIBSSH2_SESSION *session, char **dest, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned int&nbsp;<wbr>*dest_len, const char&nbsp;<wbr>*src, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned int src_len);

<h2>DESCRIPTION</h2>

 This function is deemed DEPRECATED and will be removed from libssh2 in a future version. Don't use it! 

 Decode a base64 chunk and store it into a newly allocated buffer. 'dest_len' will be set to hold the length of the returned buffer that '*dest' will point to. 

 The returned buffer is allocated by this function, but it is not clear how to free that memory!

<h2>BUGS</h2>

 The memory that *dest points to is allocated by the malloc function libssh2 uses, but there's no way for an appliction to free this data in a safe and reliable way!

<h2>RETURN VALUE</h2>

 0 if successful, -1 if any error occurred. 

<h2>Index</h2>


