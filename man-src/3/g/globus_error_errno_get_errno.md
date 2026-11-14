---
title: "globus_error_errno_get_errno(3)"
name: "globus_error_errno_get_errno"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_error_errno_get_errno/"
description: "Error Data Accessors and Modifiers –"
---

<h2 class="name">NAME</h2>
<p> Error Data Accessors and Modifiers &#8211; </p>
<h3>Get Errno</h3>
<p> int <code>globus_error_errno_get_errno</code> (globus_object_t *error) </p>
<h3>Set Errno</h3>
<p> void <code>globus_error_errno_set_errno</code> (globus_object_t *error, const int system_errno) </p>
<h2>Detailed Description</h2>
<p> Get and set data in a Globus Errno Error object. </p>
<p> This section defines operations for accessing and modifying data in a Globus Errno Error object.</p>
<h2>Function Documentation</h2>
<h3>int globus_error_errno_get_errno (globus_object_t *error)</h3>
<p> Retrieve the system errno from a errno error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error from which to retrieve the errno</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The errno stored in the object</dl>
<h3>void globus_error_errno_set_errno (globus_object_t *error, const intsystem_errno)</h3>
<p> Set the errno in a errno error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error object for which to set the errno<br />
 <i>system_errno</i> The system errno</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> void</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
