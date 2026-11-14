---
title: "get_default_context_with_level(3)"
name: "get_default_context_with_level"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_default_context_with_level/"
description: "get_ordered_context_list, get_ordered_context_list_with_level, get_default_context, get_default_context_with_level, get_default_context_with_role, get_default_context_with_rolelevel, query_user_con..."
---

<h2 class="name">NAME</h2>
<p> get_ordered_context_list, get_ordered_context_list_with_level, get_default_context, get_default_context_with_level, get_default_context_with_role, get_default_context_with_rolelevel, query_user_context, manual_user_enter_context, get_default_role &#8211; determine SELinux context(s) for user sessions </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code><br />
 <code>#include &lt;selinux/get_context_list.h&gt;</code> </p>
<p> <code>int get_ordered_context_list(const char *</code><i>user</i><code>, char *</code><i>fromcon</i><code>, char ***</code><i>list</i><code>);</code> </p>
<p> <code>int get_ordered_context_list_with_level(const char *</code><i>user</i><code>, const char *</code><i>level</i><code>, char *</code><i>fromcon</i><code>, char ***</code><i>list</i><code>);</code> </p>
<p> <code>int get_default_context(const char *</code><i>user</i><code>, char *</code><i>fromcon</i><code>, char **</code><i>newcon</i><code>);</code> </p>
<p> <code>int get_default_context_with_level(const char *</code><i>user</i><code>, const char *</code><i>level</i><code>, char *</code><i>fromcon</i><code>, char **</code><i>newcon</i><code>);</code> </p>
<p> <code>int get_default_context_with_role(const char *</code><i>user</i><code>, const char *</code><i>role</i><code>, char *</code><i>fromcon</i><code>, char **</code><i>newcon</i><code>);</code> </p>
<p> <code>int get_default_context_with_rolelevel(const char *</code><i>user</i><code>, const char *</code><i>role</i><code>, const char *</code><i>level</i><code>, char *</code><i>fromcon</i><code>, char **</code><i>newcon</i><code>);</code> </p>
<p> <code>int query_user_context(char **</code><i>list</i><code>, char **</code><i>newcon</i><code>);</code> </p>
<p> <code>int manual_user_enter_context(const char *</code><i>user</i><code>, char **</code><i>newcon</i><code>);</code> </p>
<p> <code>int get_default_type(const char *</code><i>role</i><code>, char **</code><i>type</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>get_ordered_context_list</code>() invokes the <code><a href="/docs/linux/man/3-security_compute_user/">security_compute_user</a></code>(3) function to obtain the list of contexts for the specified <i>user</i> that are reachable from the specified <i>fromcon</i> context. The function then orders the resulting list based on the global <i>/etc/selinux/{SELINUXTYPE}/contexts/default_contexts</i> file and the per-user <i>/etc/selinux/{SELINUXTYPE}/contexts/users/&lt;username&gt;</i> file if it exists. The <i>fromcon</i> parameter may be NULL to indicate that the current context should be used. The function returns the number of contexts in the list, or -1 upon errors. The list must be freed using the <code><a href="/docs/linux/man/3-freeconary/">freeconary</a></code>(3) function. </p>
<p> <code>get_ordered_context_list_with_level</code>() invokes the <code>get_ordered_context_list</code>() function and applies the specified level. </p>
<p> <code>get_default_context</code>() is the same as <code>get_ordered_context_list</code>() but only returns a single context which has to be freed with <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3). </p>
<p> <code>get_default_context_with_level</code>() invokes the <code>get_default_context</code>() function and applies the specified level. </p>
<p> <code>get_default_context_with_role</code>() is the same as <code>get_default_context</code>() but only returns a context with the specified role, returning -1 if no such context is reachable for the user. </p>
<p> <code>get_default_context_with_rolelevel</code>() invokes the <code>get_default_context_with_role</code>() function and applies the specified level. </p>
<p> <code>query_user_context</code>() takes a list of contexts, queries the user via stdin/stdout as to which context they want, and returns a new context as selected by the user (which has to be freed with <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3)). </p>
<p> <code>manual_user_enter_context</code>() allows the user to manually enter a context as a fallback if a list of authorized contexts could not be obtained. Caller must free via <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3). </p>
<p> <code>get_default_type</code>() Get the default type (domain) for <i>role</i> and set <i>type</i> to refer to it, which has to be freed with free.</p>
<h2>RETURN VALUE</h2>
<p> <code>get_ordered_context_list</code>() and <code>get_ordered_context_list_with_level</code>() return the number of contexts in the list upon success or -1 upon errors. The other functions return 0 for success or -1 for errors.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-freeconary/">freeconary</a></code>(3), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/3-security_compute_av/">security_compute_av</a></code>(3), <code><a href="/docs/linux/man/3-getseuserbyname/">getseuserbyname</a></code>(3) </p>
<h2>Index</h2>
