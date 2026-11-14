---
title: "getpeercon_raw(3)"
name: "getpeercon_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getpeercon_raw/"
description: "getcon, getprevcon, getpidcon – get SELinux security context of a process"
---

<h2 class="name">NAME</h2>
<p> getcon, getprevcon, getpidcon &#8211; get SELinux security context of a process </p>
<p> freecon, freeconary &#8211; free memory associated with SELinux security contexts </p>
<p> getpeercon &#8211; get security context of a peer socket </p>
<p> setcon &#8211; set current security context of a process </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code> </p>
<p> <code>int getcon(char **</code><i>context</i><code>);</code> </p>
<p> <code>int getcon_raw(char **</code><i>context</i><code>);</code> </p>
<p> <code>int getprevcon(char **</code><i>context</i><code>);</code> </p>
<p> <code>int getprevcon_raw(char **</code><i>context</i><code>);</code> </p>
<p> <code>int getpidcon(pid_t </code><i>pid</i><code>, char **</code><i>context</i><code>);</code> </p>
<p> <code>int getpidcon_raw(pid_t </code><i>pid</i><code>, char **</code><i>context</i><code>);</code> </p>
<p> <code>int getpeercon(int </code><i>fd</i><code>, char **</code><i>context</i><code>);</code> </p>
<p> <code>int getpeercon_raw(int </code><i>fd</i><code>, char **</code><i>context</i><code>);</code> </p>
<p> <code>void freecon(char *</code><i>con</i><code>);</code> </p>
<p> <code>void freeconary(char **</code><i>con</i><code>);</code> </p>
<p> <code>int setcon(char *</code><i>context</i><code>);</code> </p>
<p> <code>int setcon_raw(char *</code><i>context</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>getcon</code>() retrieves the context of the current process, which must be free&#8217;d with freecon. </p>
<p> <code>getprevcon</code>() same as getcon but gets the context before the last exec. </p>
<p> <code>getpidcon</code>() returns the process context for the specified PID. </p>
<p> <code>getpeercon</code>() retrieves context of peer socket, and set <code>*</code><i>context</i> to refer to it, which must be free&#8217;d with <code>freecon</code>(). </p>
<p> <code>freecon</code>() frees the memory allocated for a security context. </p>
<p> <code>freeconary</code>() frees the memory allocated for a context array. </p>
<p> If <i>con</i> is NULL, no operation is performed. </p>
<p> <code>setcon</code>() sets the current security context of the process to a new value. Note that use of this function requires that the entire application be trusted to maintain any desired separation between the old and new security contexts, unlike exec-based transitions performed via <code><a href="/docs/linux/man/3-setexeccon/">setexeccon</a></code>(3). When possible, decompose your application and use <code><a href="/docs/linux/man/3-setexeccon/">setexeccon</a></code>(3) and <code><a href="/docs/linux/man/3-execve/">execve</a></code>(3) instead. </p>
<p> Since access to file descriptors is revalidated upon use by SELinux, the new context must be explicitly authorized in the policy to use the descriptors opened by the old context if that is desired. Otherwise, attempts by the process to use any existing descriptors (including <i>stdin</i>, <i>stdout</i>, and <i>stderr</i>) after performing the <code>setcon</code>() will fail. </p>
<p> A multi-threaded application can perform a <code>setcon</code>() prior to creating any child threads, in which case all of the child threads will inherit the new context. However, prior to Linux 2.6.28, <code>setcon</code>() would fail if there are any other threads running in the same process since this would yield an inconsistency among the security contexts of threads sharing the same memory space. Since Linux 2.6.28, <code>setcon()</code> is permitted for threads within a multi-threaded process if the new security context is bounded by the old security context, where the bounded relation is defined through typebounds statements in the policy and guarantees that the new security context has a subset of the permissions of the old security context. </p>
<p> If the process was being ptraced at the time of the <code>setcon</code>() operation, ptrace permission will be revalidated against the new context and the <code>setcon</code>() will fail if it is not allowed by policy. </p>
<p> <code>getcon_raw</code>(), <code>getprevcon_raw</code>(), <code>getpidcon_raw</code>(), <code>getpeercon_raw</code>() and <code>setcon_raw</code>() behave identically to their non-raw counterparts but do not perform context translation.</p>
<h2>RETURN VALUE</h2>
<p> On error -1 is returned. On success 0 is returned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-setexeccon/">setexeccon</a></code>(3) </p>
<h2>Index</h2>
