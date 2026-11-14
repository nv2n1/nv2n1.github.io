---
title: "string_to_av_perm(3)"
name: "string_to_av_perm"
section: "3"
letter: "s"
url: "/docs/linux/man/3-string_to_av_perm/"
description: "security_class_to_string, security_av_perm_to_string, string_to_security_class, string_to_av_perm, security_av_string, mode_to_security_class – convert between SELinux class and permission values a..."
---

<p>security_class_to_string, security_av_perm_to_string, string_to_security_class, string_to_av_perm, security_av_string, mode_to_security_class &#8211; convert between SELinux class and permission values and string names. print_access_vector &#8211; display an access vector in human-readable form.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
const char *security_class_to_string(security_class_t tclass);
const char *security_av_perm_to_string(security_class_t tclass, access_vector_t av);
int security_av_string(security_class_t tclass, access_vector_t av, char **result);</code></pre>
<p> <code>security_class_t string_to_security_class(const char *</code><i>name</i><code>);</code> <code>security_class_t mode_to_security_class(mode_t </code><i>mode</i><code>);</code> <code>access_vector_t string_to_av_perm(security_class_t </code><i>tclass</i><code>, const char *</code><i>name</i><code>);</code> </p>
<pre><code>void print_access_vector(security_class_t tclass, access_vector_t av);</code></pre>
<h2>Description</h2>
<p><code>security_class_to_string</code>() returns a string name for class <i>tclass</i>, or NULL if the class is invalid. The returned string must not be modified or freed. </p>
<p> <code>security_av_perm_to_string</code>() returns a string name for the access vector bit <i>av</i> of class <i>tclass</i>, or NULL if either argument is invalid. The returned string must not be modified or freed. </p>
<p> <code>security_av_string</code>() computes a full access vector string representation using <i>tclass</i> and <i>av</i>, which may have multiple bits set. The string is returned in the memory pointed to by <i>result</i>, and should be freed by the caller using <code><a href="/docs/linux/man/3-free/">free</a></code>(3). </p>
<p> <code>string_to_security_class</code>() returns the class value corresponding to the string name <i>name</i>, or zero if no such class exists. </p>
<p> <code>mode_to_security_class</code>() returns the class value corresponding to the specified <i>mode</i>, or zero if no such class exists. </p>
<p> <code>string_to_av_perm</code>() returns the access vector bit corresponding to the string name <i>name</i> and security class <i>tclass</i>, or zero if no such value exists. </p>
<p> <code>print_access_vector</code>() displays an access vector in human-readable form on the standard output stream.</p>
<h2>Return Value</h2>
<p><code>security_av_string</code>() returns zero on success or -1 on error with <i>errno</i> set appropriately. <code>print_access_vector</code>() does not return a value. All other functions return zero or NULL on error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd>A class or access vector argument is not recognized by the currently loaded policy. </p>
<dt><code>ENOMEM</code></p>
<dd>An attempt to allocate memory failed.</dl>
<h2>Author</h2>
<p>Eamon Walsh &lt;ewalsh [at] tycho.nsa.gov&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-getcon/">getcon</a></code>(3), <code><a href="/docs/linux/man/3-getfilecon/">getfilecon</a></code>(3) <code><a href="/docs/linux/man/3-stat/">stat</a></code>(3) </p>
