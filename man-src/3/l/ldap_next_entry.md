---
title: "ldap_next_entry(3)"
name: "ldap_next_entry"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_next_entry/"
description: "ldap_first_entry, ldap_next_entry, ldap_count_entries – LDAP result entry parsing and counting routines"
---

<h2 class="name">NAME</h2>
<p> ldap_first_entry, ldap_next_entry, ldap_count_entries &#8211; LDAP result entry parsing and counting routines </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_count_entries(LDAP *ld, LDAPMessage *result)
    LDAPMessage *ldap_first_entry(LDAP *ld, LDAPMessage *result)
        LDAPMessage *ldap_next_entry(LDAP *ld, LDAPMessage *entry)
</code></pre>
<h2>DESCRIPTION</h2>
<p> These routines are used to parse results received from <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3) or the synchronous LDAP search operation routines <code><a href="/docs/linux/man/3-ldap_search_s/">ldap_search_s</a></code>(3) and <code><a href="/docs/linux/man/3-ldap_search_st/">ldap_search_st</a></code>(3). </p>
<p> The <code>ldap_first_entry()</code> routine is used to retrieve the first entry in a chain of search results. It takes the <i>result</i> as returned by a call to <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3) or <code><a href="/docs/linux/man/3-ldap_search_s/">ldap_search_s</a></code>(3) or <code><a href="/docs/linux/man/3-ldap_search_st/">ldap_search_st</a></code>(3) and returns a pointer to the first entry in the result. </p>
<p> This pointer should be supplied on a subsequent call to <code>ldap_next_entry()</code> to get the next entry, the result of which should be supplied to the next call to <code>ldap_next_entry()</code>, etc. <code>ldap_next_entry()</code> will return NULL when there are no more entries. The entries returned from these calls are used in calls to the routines described in <code><a href="/docs/linux/man/3-ldap_get_dn/">ldap_get_dn</a></code>(3), <code><a href="/docs/linux/man/3-ldap_first_attribute/">ldap_first_attribute</a></code>(3), <code><a href="/docs/linux/man/3-ldap_get_values/">ldap_get_values</a></code>(3), etc. </p>
<p> A count of the number of entries in the search result can be obtained by calling <code>ldap_count_entries()</code>.</p>
<h2>ERRORS</h2>
<p> If an error occurs in <code>ldap_first_entry()</code> or <code>ldap_next_entry()</code>, NULL is returned and the ld_errno field in the <i>ld</i> parameter is set to indicate the error. If an error occurs in <code>ldap_count_entries()</code>, -1 is returned, and <code>ld_errno</code> is set appropriately. See <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3) for a description of possible error codes.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3), <code><a href="/docs/linux/man/3-ldap_search/">ldap_search</a></code>(3), <code><a href="/docs/linux/man/3-ldap_first_attribute/">ldap_first_attribute</a></code>(3), <code><a href="/docs/linux/man/3-ldap_get_values/">ldap_get_values</a></code>(3), <code><a href="/docs/linux/man/3-ldap_get_dn/">ldap_get_dn</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
