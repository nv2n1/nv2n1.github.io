---
title: "ldap_extended_operation(3)"
name: "ldap_extended_operation"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_extended_operation/"
description: "ldap_extended_operation, ldap_extended_operation_s – Extends the LDAP operations to the LDAP server."
---

<h2 class="name">NAME</h2>
<p> ldap_extended_operation, ldap_extended_operation_s &#8211; Extends the LDAP operations to the LDAP server. </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_extended_operation(
    LDAP *ld,
    const char *requestoid,
    const struct berval *requestdata,
    LDAPControl **sctrls,
    LDAPControl **cctrls,
    int *msgidp);

int ldap_extended_operation_s(
    LDAP *ld,
    const char *requestoid,
    const struct berval *requestdata,
    LDAPControl **sctrls,
    LDAPControl **cctrls,
    char **retoidp,
    struct berval **retdatap);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ldap_extended_operation_s()</code> routine is used to synchronously perform an LDAP extended operation. It takes <i>requestoid</i>, which points to a dotted-decimal OID string identifying the extended operation to perform. <i>requestdata</i> is the data required for the request, <i>sctrls</i> is an array of LDAPControl structures to use with this extended operation, <i>cctrls</i> is an array of LDAPControl structures that list the client controls to use with this extended operation. </p>
<p> The output parameter <i>retoidp</i> points to a dotted-decimal OID string returned by the LDAP server. The memory used by the string should be freed with the <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3) function. The output parameter <i>retdatap</i> points to a pointer to a berval structure that contains the returned data. If no data is returned by the server, the pointer is set this to NULL. The memory used by this structure should be freed with the <code><a href="/docs/linux/man/3-ber_bvfree/">ber_bvfree</a></code>(3) function. </p>
<p> The <code>ldap_extended_operation()</code> works just like <code>ldap_extended_operation_s()</code>, but the operation is asynchronous. It provides the message id of the request it initiated in the integer pointed to be <i>msgidp</i>. The result of this operation can be obtained by calling <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a>(3).</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ber_bvfree/">ber_bvfree</a></code>(3), <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3), <code><a href="/docs/linux/man/3-ldap_parse_extended_result/">ldap_parse_extended_result</a></code>(3), <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
