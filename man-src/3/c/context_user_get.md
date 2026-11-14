---
title: "context_user_get(3)"
name: "context_user_get"
section: "3"
letter: "c"
url: "/docs/linux/man/3-context_user_get/"
description: "context_new, context_str, context_free, context_type_get, context_type_set, context_range_get, context_range_set,context_role_get, context_role_set, context_user_get, context_user_set – Routines to..."
---

<h2 class="name">NAME</h2>
<p> context_new, context_str, context_free, context_type_get, context_type_set, context_range_get, context_range_set,context_role_get, context_role_set, context_user_get, context_user_set &#8211; Routines to manipulate SELinux security contexts </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/context.h&gt;</code> </p>
<p> <code>context_t context_new(const char *</code><i>context_str</i><code>);</code> </p>
<p> <code>const char * context_str(context_t </code><i>con</i><code>);</code> </p>
<p> <code>void context_free(context_t </code><i>con</i><code>);</code> </p>
<p> <code>const char * context_type_get(context_t </code><i>con</i><code>);</code> </p>
<p> <code>const char * context_range_get(context_t </code><i>con</i><code>);</code> </p>
<p> <code>const char * context_role_get(context_t </code><i>con</i><code>);</code> </p>
<p> <code>const char * context_user_get(context_t </code><i>con</i><code>);</code> </p>
<p> <code>int context_type_set(context_t </code><i>con</i><code>, const char *</code><i>type</i><code>);</code> </p>
<p> <code>int context_range_set(context_t </code><i>con</i><code>, const char *</code><i>range</i><code>);</code> </p>
<p> <code>int context_role_set(context_t </code><i>con</i><code>, const char *</code><i>role</i><code>);</code> </p>
<p> <code>int context_user_set(context_t </code><i>con</i><code>, const char *</code><i>user</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> These functions allow an application to manipulate the fields of a security context string without requiring it to know the format of the string. </p>
<p> <code>context_new</code>() returns a new context initialized to a context string. </p>
<p> <code>context_str</code>() returns a pointer to the string value of the <code>context_t</code>, valid until the next call to <code>context_str</code>() or <code>context_free</code>() for the same <code>context_t*</code>. </p>
<p> <code>context_free</code>() frees the storage used by a context. </p>
<p> <code>context_type_get</code>(), <code>context_range_get</code>(), <code>context_role_get</code>(), <code>context_user_get</code>() get a pointer to the string value of a context component. </p>
<p> <code>Note:</code> Values returned by the get functions are only valid until the next call to a set function or <code>context_free</code>() for the same <code>context_t</code> structure. </p>
<p> <code>context_type_set</code>(), <code>context_range_set</code>(), <code>context_role_set</code>(), <code>context_user_set</code>() set a context component.</p>
<h2>RETURN VALUE</h2>
<p> On failure <code>context_*_set</code>() functions return non-zero and 0 on success. </p>
<p> The other functions return NULL on failure and non-NULL on success. </p>
<p> On failure <i>errno</i> is set appropriately.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
<h2>Index</h2>
