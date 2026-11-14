---
title: "globus_error_gssapi_set_major_status(3)"
name: "globus_error_gssapi_set_major_status"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_error_gssapi_set_major_status/"
description: "Error Data Accessors and Modifiers –"
---

<h2 class="name">NAME</h2>
<p> Error Data Accessors and Modifiers &#8211; </p>
<h3>Functions</h3>
<p> OM_uint32 <code>globus_error_gssapi_get_major_status</code> (globus_object_t *error)<br />
 <i>Get Major Status. </i><br />
 void <code>globus_error_gssapi_set_major_status</code> (globus_object_t *error, const OM_uint32 major_status)<br />
 <i>Set Major Status. </i><br />
 OM_uint32 <code>globus_error_gssapi_get_minor_status</code> (globus_object_t *error)<br />
 <i>Get Minor Status. </i></p>
<h2>Detailed Description</h2>
<p> Get and set data in a Globus GSSAPI Error object. </p>
<p> This section defines operations for accessing and modifying data in a Globus GSSAPI Error object.</p>
<h2>Function Documentation</h2>
<h3>OM_uint32 globus_error_gssapi_get_major_status (globus_object_t *error)</h3>
<p> Get Major Status. Retrieve the major status from a GSSAPI error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error from which to retrieve the major status</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The major status stored in the object</dl>
<h3>OM_uint32 globus_error_gssapi_get_minor_status (globus_object_t *error)</h3>
<p> Get Minor Status. Retrieve the minor status from a gssapi error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error from which to retrieve the minor status</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The minor status stored in the object</dl>
<h3>void globus_error_gssapi_set_major_status (globus_object_t *error, const OM_uint32major_status)</h3>
<p> Set Major Status. Set the major status in a GSSAPI error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error object for which to set the major status<br />
 <i>major_status</i> The major status</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> void</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gssapi_error from the source code. </p>
<h2>Index</h2>
