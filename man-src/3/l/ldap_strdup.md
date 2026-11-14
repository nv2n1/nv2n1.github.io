---
title: "ldap_strdup(3)"
name: "ldap_strdup"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_strdup/"
description: "ldap_memfree, ldap_memvfree, ldap_memalloc, ldap_memcalloc, ldap_memrealloc, ldap_strdup – LDAP memory allocation routines"
---

<h2 class="name">NAME</h2>
<p> ldap_memfree, ldap_memvfree, ldap_memalloc, ldap_memcalloc, ldap_memrealloc, ldap_strdup &#8211; LDAP memory allocation routines </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;ldap.h&gt;</code> </p>
<p> <code>void ldap_memfree(void *</code><i>p</i><code>);</code> </p>
<p> <code>void ldap_memvfree(void **</code><i>v</i><code>);</code> </p>
<p> <code>void *ldap_memalloc(ber_len_t </code><i>s</i><code>);</code> </p>
<p> <code>void *ldap_memcalloc(ber_len_t </code><i>n</i><code>, ber_len_t </code><i>s</i><code>);</code> </p>
<p> <code>void *ldap_memrealloc(void *</code><i>p</i><code>, ber_len_t </code><i>s</i><code>);</code> </p>
<p> <code>char *ldap_strdup(LDAP_CONST char *</code><i>p</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> These routines are used to allocate/deallocate memory used/returned by the LDAP library. <code>ldap_memalloc</code>(), <code>ldap_memcalloc</code>(), <code>ldap_memrealloc</code>(), and <code>ldap_memfree</code>() are used exactly like the standard <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-calloc/">calloc</a></code>(3), <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3), and <code><a href="/docs/linux/man/3-free/">free</a></code>(3) routines, respectively. The <code>ldap_memvfree</code>() routine is used to free a dynamically allocated array of pointers to arbitrary dynamically allocated objects. The <code>ldap_strdup</code>() routine is used exactly like the standard <code><a href="/docs/linux/man/3-strdup/">strdup</a></code>(3) routine.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
