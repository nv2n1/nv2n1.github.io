---
title: "audit_encode_nv_string(3)"
name: "audit_encode_nv_string"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_encode_nv_string/"
description: "audit_encode_nv_string – encode a name/value pair in a string"
---

<h2>NAME</h2>
<p> audit_encode_nv_string &#8211; encode a name/value pair in a string</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> <code>char *audit_encode_nv_string(const char *name, const char *value, unsigned int vlen)</code> </p>
<h2>DESCRIPTION</h2>
<p> This function is used to encode a name/value pair. This should be used on any field being logged that potentially contains a space, a double-quote, or a control character. Any value containing those have to be specially encoded for the auparse library to correctly handle the value. The encoding method is designed to prevent log injection attacks where malicious values could cause parsing errors. </p>
<p> To use this function, pass the name string and value strings on their respective arguments. If the value is likely to have a NUL value embedded within it, you will need to pass a value length that tells in bytes how big the value is. Otherwise, you can pass a 0 for vlen and the function will simply use strlen against the value pointer. Also be aware that the name of the field will cause auparse to do certain things when interpretting the value. If the name is uid, a user id value in decimal is expected. Make sure that well known names are used for their intended purpose or that there is no chance of name collision with something new. </p>
<h2>RETURN VALUE</h2>
<p> Returns a freshly malloc&#8217;ed string that the caller must free or NULL on error. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_log_user_message/">audit_log_user_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_user_comm_message/">audit_log_user_comm_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_user_avc_message/">audit_log_user_avc_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_semanage_message/">audit_log_semanage_message</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
