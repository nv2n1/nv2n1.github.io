---
title: "ldap_rename(3)"
name: "ldap_rename"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_rename/"
description: "ldap_rename, ldap_rename_s – Renames the specified entry."
---

<h2 class="name">NAME</h2>
<p> ldap_rename, ldap_rename_s &#8211; Renames the specified entry. </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_rename(ld, dn, newrdn, newparent, deleteoldrdn, sctrls[], cctrls[], msgidp);
LDAP *ld;
const char *dn, *newrdn, *newparent;
int deleteoldrdn;
LDAPControl *sctrls[], *cctrls[];
int *msgidp);
int ldap_rename_s(ld, dn, newrdn, newparent, deleteoldrdn, sctrls[], cctrls[]);
LDAP *ld;
const char *dn, *newrdn, *newparent;
int deleteoldrdn;
LDAPControl *sctrls[], *cctrls[];
</code></pre>
<h2>DESCRIPTION</h2>
<p> These routines are used to perform a LDAP rename operation. The function changes the leaf component of an entry&#8217;s distinguished name and optionally moves the entry to a new parent container. The <code>ldap_rename_s</code> performs a rename operation synchronously. The method takes <i>dn</i>, which points to the distinguished name of the entry whose attribute is being compared, <i>newparent</i>,the distinguished name of the entry&#8217;s new parent. If this parameter is NULL, only the RDN is changed. The root DN is specified by passing a zero length string, &quot;&quot;. <i>deleteoldrdn</i> specifies whether the old RDN should be retained or deleted. Zero indicates that the old RDN should be retained. If you choose this option, the attribute will contain both names (the old and the new). Non-zero indicates that the old RDN should be deleted. <i>serverctrls</i> points to an array of LDAPControl structures that list the client controls to use with this extended operation. Use NULL to specify no client controls. <i>clientctrls</i> points to an array of LDAPControl structures that list the client controls to use with the search. </p>
<p> <code>ldap_rename</code> works just like <code>ldap_rename_s,</code> but the operation is asynchronous. It returns the message id of the request it initiated. The result of this operation can be obtained by calling <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a>(3).</code></p>
<h2>ERRORS</h2>
<p> <code>ldap_rename()</code> returns -1 in case of error initiating the request, and will set the <i>ld_errno</i> field in the <i>ld</i> parameter to indicate the error. <code>ldap_rename_s()</code> returns the LDAP error code resulting from the rename operation.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_modify/">ldap_modify</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
