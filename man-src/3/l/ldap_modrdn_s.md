---
title: "ldap_modrdn_s(3)"
name: "ldap_modrdn_s"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_modrdn_s/"
description: "ldap_modrdn, ldap_modrdn_s, ldap_modrdn2, ldap_modrdn2_s – Perform an LDAP modify RDN operation"
---

<h2 class="name">NAME</h2>
<p> ldap_modrdn, ldap_modrdn_s, ldap_modrdn2, ldap_modrdn2_s &#8211; Perform an LDAP modify RDN operation </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_modrdn(ld, dn, newrdn)
LDAP *ld;
char *dn, *newrdn;

int ldap_modrdn_s(ld, dn, newrdn)
LDAP *ld;
char *dn, *newrdn;
int ldap_modrdn2(ld, dn, newrdn, deleteoldrdn)
LDAP *ld;
char *dn, *newrdn;
int deleteoldrdn;
int ldap_modrdn2_s(ld, dn, newrdn, deleteoldrdn)
LDAP *ld;
char *dn, *newrdn;
int deleteoldrdn;
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ldap_modrdn()</code> and <code>ldap_modrdn_s()</code> routines perform an LDAP modify RDN operation. They both take <i>dn</i>, the DN of the entry whose RDN is to be changed, and <i>newrdn</i>, the new RDN to give the entry. The old RDN of the entry is never kept as an attribute of the entry. <code>ldap_modrdn()</code> is asynchronous, returning the message id of the operation it initiates. <code>ldap_modrdn_s()</code> is synchronous, returning the LDAP error code indicating the success or failure of the operation. Use of these routines is deprecated. Use the versions described below instead. </p>
<p> The <code>ldap_modrdn2()</code> and <code>ldap_modrdn2_s()</code> routines also perform an LDAP modify RDN operation, taking the same parameters as above. In addition, they both take the <i>deleteoldrdn</i> parameter which is used as a boolean value to indicate whether the old RDN values should be deleted from the entry or not.</p>
<h2>ERRORS</h2>
<p> The synchronous (_s) versions of these routines return an LDAP error code, either LDAP_SUCCESS or an error if there was trouble. The asynchronous versions return -1 in case of trouble, setting the <code>ld_errno</code> field of <i>ld</i>. See <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3) for more details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
