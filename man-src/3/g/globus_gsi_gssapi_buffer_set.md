---
title: "globus_gsi_gssapi_buffer_set(3)"
name: "globus_gsi_gssapi_buffer_set"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_gssapi_buffer_set/"
description: "Buffer Set Utilities –"
---

<h2 class="name">NAME</h2>
<p> Buffer Set Utilities &#8211; </p>
<p> Buffer Set Utilities.</p>
<h3>Functions</h3>
<p> OM_uint32 GSS_CALLCONV <code>gss_create_empty_buffer_set</code> (OM_uint32 *minor_status, gss_buffer_set_t *buffer_set)<br />
 <i>Create a empty buffer set. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_add_buffer_set_member</code> (OM_uint32 *minor_status, const gss_buffer_t member_buffer, gss_buffer_set_t *buffer_set)<br />
 <i>Add a buffer to a buffer set. </i><br />
 OM_uint32 GSS_CALLCONV <code>gss_release_buffer_set</code> (OM_uint32 *minor_status, gss_buffer_set_t *buffer_set)<br />
 <i>Free a Buffer Set. </i></p>
<h2>Detailed Description</h2>
<p> Buffer Set Utilities. </p>
<p> Functions in this group provide utilities for creating, modifying, and freeing a buffer set.</p>
<h2>Function Documentation</h2>
<h3>OM_uint32 GSS_CALLCONV gss_add_buffer_set_member (OM_uint32 *minor_status, const gss_buffer_tmember_buffer, gss_buffer_set_t *buffer_set)</h3>
<p> Add a buffer to a buffer set. This function allocates a new gss_buffer_t, initializes it with the values in the member_buffer parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> The minor status returned by this function. This parameter will be 0 upon success.<br />
 <i>member_buffer</i> Buffer to insert into the buffer set.<br />
 <i>buffer_set</i> Pointer to a initialized buffer set structure.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GSS_S_COMPLETE</i> Success<br />
 <i>GSS_S_FAILURE</i> Failure</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>gss_create_empty_buffer_set</code> </p>
<p> <code>gss_release_buffer_set</code></dl>
<h3>OM_uint32 GSS_CALLCONV gss_create_empty_buffer_set (OM_uint32 *minor_status, gss_buffer_set_t *buffer_set)</h3>
<p> Create a empty buffer set. This function allocates and initializes a empty buffer set. The memory allocated in this function should be freed by a call to gss_release_buffer_set. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> The minor status returned by this function. This parameter will be 0 upon success.<br />
 <i>buffer_set</i> Pointer to a buffer set structure.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GSS_S_COMPLETE</i> Success<br />
 <i>GSS_S_FAILURE</i> Failure</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>gss_add_buffer_set_member</code> </p>
<p> <code>gss_release_buffer_set</code></dl>
<h3>OM_uint32 GSS_CALLCONV gss_release_buffer_set (OM_uint32 *minor_status, gss_buffer_set_t *buffer_set)</h3>
<p> Free a Buffer Set. This function will free all memory associated with a buffer set. Note that it will also free all memory associated with the buffers int the buffer set. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>minor_status</i> The minor status returned by this function. This parameter will be 0 upon success.<br />
 <i>buffer_set</i> Pointer to a buffer set structure. This pointer will point at a NULL value upon return.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GSS_S_COMPLETE</i> Success<br />
 <i>GSS_S_FAILURE</i> Failure</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>gss_create_empty_buffer_set</code> </p>
<p> <code>gss_add_buffer_set_member</code></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gssapi_gsi from the source code. </p>
<h2>Index</h2>
