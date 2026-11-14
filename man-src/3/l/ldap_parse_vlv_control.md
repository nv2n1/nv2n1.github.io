---
title: "ldap_parse_vlv_control(3)"
name: "ldap_parse_vlv_control"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_parse_vlv_control/"
description: "ldap_parse_vlv_control – Decode the information returned from a search operation that used a VLV (virtual list view) control"
---

<h2 class="name">NAME</h2>
<p> ldap_parse_vlv_control &#8211; Decode the information returned from a search operation that used a VLV (virtual list view) control </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_parse_vlv_control(ld, ctrlp, target_posp, list_countp, contextp, errcodep)
LDAP *ld;
LDAPControl **ctrlp;
unsigned long *target_posp, *list_countp;
struct berval **contextp;
int *errcodep;
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ldap_parse_vlv_control</code> is used to decode the information returned from a search operation that used a VLV (virtual list view)control. It takes a null terminated array of LDAPControl structures, usually obtained by a call to the <code>ldap_parse_result</code>function, a <i>target_pos</i> which points to the list index of the target entry. If this parameter is NULL, the target position is not returned. The index returned is an approximation of the position of the target entry. It is not guaranteed to be exact. The parameter <i>list_countp</i> points to the server&#8217;s estimate of the size of the list. If this parameter is NULL, the size is not returned. <i>contextp</i> is a pointer to the address of a berval structure that contains a server-generated context identifier if server returns one. If server does not return a context identifier, the server returns a NULL in this parameter. If this parameter is set to NULL, the context identifier is not returned. You should use this returned context in the next call to create a VLV control. When the berval structure is no longer needed, you should free the memory by calling the <i>ber_bvfree function.e</i> <i>errcodep</i> is an output parameter, which points to the result code returned by the server. If this parameter is NULL, the result code is not returned. </p>
<p> See ldap.h for a list of possible return codes.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap_search/">ldap_search</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
