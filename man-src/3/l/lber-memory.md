---
title: "lber-memory(3)"
name: "lber-memory"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lber-memory/"
description: "ber_memalloc, ber_memcalloc, ber_memrealloc, ber_memfree, ber_memvfree – OpenLDAP LBER memory allocators"
---

<h2 class="name">NAME</h2>
<p> ber_memalloc, ber_memcalloc, ber_memrealloc, ber_memfree, ber_memvfree &#8211; OpenLDAP LBER memory allocators </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LBER (liblber, -llber)</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;lber.h&gt;</code> </p>
<p> <code>void *ber_memalloc(ber_len_t </code><i>bytes</i><code>);</code> </p>
<p> <code>void *ber_memcalloc(ber_len_t </code><i>nelems</i><code>, ber_len_t </code><i>bytes</i><code>);</code> </p>
<p> <code>void *ber_memrealloc(void *</code><i>ptr</i><code>, ber_len_t </code><i>bytes</i><code>);</code> </p>
<p> <code>void ber_memfree(void *</code><i>ptr</i><code>);</code> </p>
<p> <code>void ber_memvfree(void **</code><i>vec</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> These routines are used to allocate/deallocate memory used/returned by the Lightweight BER library as required by <code><a href="/docs/linux/man/3-lber-encode/">lber-encode</a></code>(3) and <code><a href="/docs/linux/man/3-lber-decode/">lber-decode</a></code>(3). <code>ber_memalloc</code>(), <code>ber_memcalloc</code>(), <code>ber_memrealloc</code>(), and <code>ber_memfree</code>() are used exactly like the standard <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-calloc/">calloc</a></code>(3), <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3), and <code><a href="/docs/linux/man/3-free/">free</a></code>(3) routines, respectively. The <code>ber_memvfree</code>() routine is used to free a dynamically allocated array of pointers to arbitrary dynamically allocated objects.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-lber-decode/">lber-decode</a></code>(3), <code><a href="/docs/linux/man/3-lber-encode/">lber-encode</a></code>(3), <code><a href="/docs/linux/man/3-lber-types/">lber-types</a></code>(3) </p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
