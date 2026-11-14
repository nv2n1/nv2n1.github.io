---
title: "ldap_parse_sort_control(3)"
name: "ldap_parse_sort_control"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_parse_sort_control/"
description: "ldap_parse_sort_control – Decode the information returned from a search operation that used a server-side sort control"
---

<h2 class="name">NAME</h2>
<p> ldap_parse_sort_control &#8211; Decode the information returned from a search operation that used a server-side sort control </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_parse_sort_control(ld, ctrls, returnCode, attribute)
LDAP *ld;
LDAPControl **ctrls;
unsigned long *returnCode;
char **attribute;
</code></pre>
<h2>DESCRIPTION</h2>
<p> This function is used to parse the results returned in a search operation that uses a server-side sort control. </p>
<p> It takes a null terminated array of LDAPControl structures usually obtained by a call to the <code>ldap_parse_result</code> function. A returncode which points to the sort control result code,and an array of LDAPControl structures that list the client controls to use with the search. The function also takes an out parameter <i>attribute</i> and if the sort operation fails, the server may return a string that indicates the first attribute in the sortKey list that caused the failure. If this parameter is NULL, no string is returned. If a string is returned, the memory should be freed by calling the ldap_memfree function.</p>
<h2>NOTES</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3), <code><a href="/docs/linux/man/3-ldap_controls_free/">ldap_controls_free</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
