---
title: "globus_gss_assist_display_status(3)"
name: "globus_gss_assist_display_status"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gss_assist_display_status/"
description: "GSSAPI Result Status Strings –"
---

<h2 class="name">NAME</h2>
<p> GSSAPI Result Status Strings &#8211; </p>
<p> Display Error Status from a GSSAPI Result.</p>
<h3>Functions</h3>
<p> OM_uint32 <code>globus_gss_assist_display_status</code> (FILE *fp, char *comment, OM_uint32 major_status, OM_uint32 minor_status, int token_status) </p>
<p> OM_uint32 <code>globus_gss_assist_display_status_str</code> (char **str, char *comment, OM_uint32 major_status, OM_uint32 minor_status, int token_status) </p>
<h2>Detailed Description</h2>
<p> Display Error Status from a GSSAPI Result. </p>
<p> The functions in this section convert a GSSAPI result code into a message.</p>
<h2>Function Documentation</h2>
<h3>OM_uint32 globus_gss_assist_display_status (FILE *fp, char *comment, OM_uint32major_status, OM_uint32minor_status, inttoken_status)</h3>
<p> Display the messages for the major and minor status on the file pointed at by fp. Takes care of the overloaded major_status if there was a problem with the get_token or send_token routines. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>fp</i> a file pointer<br />
 <i>comment</i> String to print out before other error messages.<br />
 <i>major_status</i> The major status to display<br />
 <i>minor_status</i> The minor status to display<br />
 <i>token_status</i> token status to display</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0</dl>
<h3>OM_uint32 globus_gss_assist_display_status_str (char **str, char *comment, OM_uint32major_status, OM_uint32minor_status, inttoken_status)</h3>
<p> Display the messages for the major and minor status and return a string with the messages. Takes care of the overloaded major_status if there was a problem with the get_token or send_token routines. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>str</i> pointer to char * for returned string. Must be freed<br />
 <i>comment</i> String to print out before other error messages.<br />
 <i>major_status</i> The major status to display<br />
 <i>minor_status</i> The minor status to display<br />
 <i>token_status</i> token status to display</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gss_assist from the source code. </p>
<h2>Index</h2>
