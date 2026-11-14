---
title: "ldap_compare_ext_s(3)"
name: "ldap_compare_ext_s"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_compare_ext_s/"
description: "ldap_compare, ldap_compare_s, ldap_compare_ext, ldap_compare_ext_s – Perform an LDAP compare operation."
---

<h2 class="name">NAME</h2>
<p> ldap_compare, ldap_compare_s, ldap_compare_ext, ldap_compare_ext_s &#8211; Perform an LDAP compare operation. </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_compare_ext(
    LDAP *ld,
    char *dn,
    char *attr,
    const struct berval *bvalue,
    LDAPControl **serverctrls,
    LDAPControl **clientctrls,
    int *msgidp);

int ldap_compare_ext_s(
    LDAP *ld,
    char *dn,
    char *attr,
    const struct berval *bvalue,
    LDAPControl **serverctrls,
    LDAPControl **clientctrls);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ldap_compare_ext_s()</code> routine is used to perform an LDAP compare operation synchronously. It takes <i>dn</i>, the DN of the entry upon which to perform the compare, and <i>attr</i> and <i>value</i>, the attribute description and value to compare to those found in the entry. It returns a code, which will be LDAP_COMPARE_TRUE if the entry contains the attribute value and LDAP_COMPARE_FALSE if it does not. Otherwise, an error code is returned that indicates the nature of the problem. See <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3) for details. </p>
<p> The <code>ldap_compare_ext()</code> routine is used to perform an LDAP compare operation asynchronously. It takes the same parameters as <code>ldap_compare_ext_s()</code>, but provides the message id of the request it initiated in the integer pointed to <i>msgidp</i>. The result of the compare can be obtained by a subsequent call to <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3). </p>
<p> Both routines allow server and client controls to be specified to extend the compare request.</p>
<h2>DEPRECATED INTERFACES</h2>
<p> The routines <code>ldap_compare</code>() and <code>ldap_compare_s</code>() are deprecated in favor of <code>ldap_compare_ext</code>() and <code>ldap_compare_ext_s</code>(), respectively. </p>
<p> Deprecated interfaces generally remain in the library. The macro LDAP_DEPRECATED can be defined to a non-zero value (e.g., -DLDAP_DEPRECATED=1) when compiling program designed to use deprecated interfaces. It is recommended that developers writing new programs, or updating old programs, avoid use of deprecated interfaces. Over time, it is expected that documentation (and, eventually, support) for deprecated interfaces to be eliminated.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
