---
title: "ldap_get_values_len(3)"
name: "ldap_get_values_len"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_get_values_len/"
description: "ldap_get_values, ldap_get_values_len, ldap_count_values – LDAP attribute value handling routines"
---

<h2 class="name">NAME</h2>
<p> ldap_get_values, ldap_get_values_len, ldap_count_values &#8211; LDAP attribute value handling routines </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
char **ldap_get_values(ld, entry, attr)
LDAP *ld;
LDAPMessage *entry;
char *attr;
struct berval **ldap_get_values_len(ld, entry, attr)
LDAP *ld;
LDAPMessage *entry;
char *attr;
int ldap_count_values(vals)
char **vals;
int ldap_count_values_len(vals)
struct berval **vals;
void ldap_value_free(vals) char **vals;
void ldap_value_free_len(vals) struct berval **vals;
</code></pre>
<h2>DESCRIPTION</h2>
<p> These routines are used to retrieve and manipulate attribute values from an LDAP entry as returned by <code><a href="/docs/linux/man/3-ldap_first_entry/">ldap_first_entry</a></code>(3) or <code><a href="/docs/linux/man/3-ldap_next_entry/">ldap_next_entry</a></code>(3). <code>ldap_get_values()</code> takes the <i>entry</i> and the attribute <i>attr</i> whose values are desired and returns a NULL-terminated array of the attribute&#8217;s values. <i>attr</i> may be an attribute type as returned from <code><a href="/docs/linux/man/3-ldap_first_attribute/">ldap_first_attribute</a></code>(3) or <code><a href="/docs/linux/man/3-ldap_next_attribute/">ldap_next_attribute</a></code>(3), or if the attribute type is known it can simply be given. </p>
<p> The number of values in the array can be counted by calling <code>ldap_count_values()</code>. The array of values returned can be freed by calling <code>ldap_value_free()</code>. </p>
<p> If the attribute values are binary in nature, and thus not suitable to be returned as an array of char *&#8217;s, the <code>ldap_get_values_len()</code> routine can be used instead. It takes the same parameters as <code>ldap_get_values()</code>, but returns a NULL-terminated array of pointers to berval structures, each containing the length of and a pointer to a value. </p>
<p> The number of values in the array can be counted by calling <code>ldap_count_values_len()</code>. The array of values returned can be freed by calling <code>ldap_value_free_len()</code>.</p>
<h2>ERRORS</h2>
<p> If an error occurs in <code>ldap_get_values()</code> or <code>ldap_get_values_len()</code>, NULL is returned and the <code>ld_errno</code> field in the <i>ld</i> parameter is set to indicate the error. See <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3) for a description of possible error codes.</p>
<h2>NOTES</h2>
<p> These routines dynamically allocate memory which the caller must free using the supplied routines.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_first_entry/">ldap_first_entry</a></code>(3), <code><a href="/docs/linux/man/3-ldap_first_attribute/">ldap_first_attribute</a></code>(3), <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
