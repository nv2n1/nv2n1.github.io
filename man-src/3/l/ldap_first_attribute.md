---
title: "ldap_first_attribute(3)"
name: "ldap_first_attribute"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_first_attribute/"
description: "ldap_first_attribute, ldap_next_attribute – step through LDAP entry attributes"
---

<h2 class="name">NAME</h2>
<p> ldap_first_attribute, ldap_next_attribute &#8211; step through LDAP entry attributes </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
char *ldap_first_attribute(
    LDAP *ld, LDAPMessage *entry, BerElement **berptr) char *ldap_next_attribute(LDAP *ld, LDAPMessage *entry, BerElement *ber)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ldap_first_attribute()</code> and <code>ldap_next_attribute()</code> routines are used to step through the attributes in an LDAP entry. <code>ldap_first_attribute()</code> takes an <i>entry</i> as returned by <code><a href="/docs/linux/man/3-ldap_first_entry/">ldap_first_entry</a></code>(3) or <code><a href="/docs/linux/man/3-ldap_next_entry/">ldap_next_entry</a></code>(3) and returns a pointer to character string containing the first attribute description in the entry. <code>ldap_next_attribute()</code> returns the next attribute description in the entry. </p>
<p> It also returns, in <i>berptr</i>, a pointer to a BerElement it has allocated to keep track of its current position. This pointer should be passed to subsequent calls to <code>ldap_next_attribute()</code> and is used to effectively step through the entry&#8217;s attributes. The caller is solely responsible for freeing the BerElement pointed to by <i>berptr</i> when it is no longer needed by calling <code><a href="/docs/linux/man/3-ber_free/">ber_free</a></code>(3). When calling <code><a href="/docs/linux/man/3-ber_free/">ber_free</a></code>(3) in this instance, be sure the second argument is 0. </p>
<p> The attribute names returned are suitable for inclusion in a call to <code><a href="/docs/linux/man/3-ldap_get_values/">ldap_get_values</a></code>(3) to retrieve the attribute&#8217;s values.</p>
<h2>ERRORS</h2>
<p> If an error occurs, NULL is returned and the ld_errno field in the <i>ld</i> parameter is set to indicate the error. See <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3) for a description of possible error codes.</p>
<h2>NOTES</h2>
<p> The <code>ldap_first_attribute()</code> and <code>ldap_next_attribute()</code> return dynamically allocated memory that must be freed by the caller via <code><a href="/docs/linux/man/3-ldap_memfree/">ldap_memfree</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_first_entry/">ldap_first_entry</a></code>(3), <code><a href="/docs/linux/man/3-ldap_get_values/">ldap_get_values</a></code>(3), <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
