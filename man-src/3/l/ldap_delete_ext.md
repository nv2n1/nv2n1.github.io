---
title: "ldap_delete_ext(3)"
name: "ldap_delete_ext"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_delete_ext/"
description: "ldap_delete, ldap_delete_s, ldap_delete_ext, ldap_delete_ext_s – Perform an LDAP delete operation."
---

<h2 class="name">NAME</h2>
<p> ldap_delete, ldap_delete_s, ldap_delete_ext, ldap_delete_ext_s &#8211; Perform an LDAP delete operation. </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_delete_s(ld, dn)
LDAP *ld;
char *dn;
int ldap_delete(ld, dn)
LDAP *ld;
char *dn;
int ldap_delete_ext(ld, dn, serverctrls, clientctrls, msgidp)
LDAP *ld;
char *dn;
LDAPControl **serverctrls, **clientctrls;
int *msgidp;
int ldap_delete_ext_s(ld, dn, serverctrls, clientctrls)
LDAP *ld;
char *dn;
LDAPControl **serverctrls, **clientctrls;
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ldap_delete_s()</code> routine is used to perform an LDAP delete operation synchronously. It takes <i>dn</i>, the DN of the entry to be deleted. It returns an LDAP error code, indicating the success or failure of the operation. </p>
<p> The <code>ldap_delete()</code> routine is used to perform an LDAP delete operation asynchronously. It takes the same parameters as <code>ldap_delete_s(),</code> but returns the message id of the request it initiated. The result of the delete can be obtained by a subsequent call to <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3). </p>
<p> The <code>ldap_delete_ext()</code> routine allows server and client controls to be specified to extend the delete request. This routine is asynchronous like ldap_delete(), but its return value is an LDAP error code. It stores the message id of the request in the integer pointed to by msgidp. </p>
<p> The <code>ldap_delete_ext_s()</code> routine is the synchronous version of <code>ldap_delete_ext().</code> It also returns an LDAP error code indicating success or failure of the operation.</p>
<h2>ERRORS</h2>
<p> <code>ldap_delete_s()</code> returns an LDAP error code which can be interpreted by calling one of <code><a href="/docs/linux/man/3-ldap_perror/">ldap_perror</a></code>(3) and friends. <code>ldap_delete()</code> returns -1 if something went wrong initiating the request. It returns the non-negative message id of the request if things went ok. </p>
<p> <code>ldap_delete_ext()</code> and <code>ldap_delete_ext_s()</code> return some Non-zero value if something went wrong initiating the request, else return 0.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
