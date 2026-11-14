---
title: "ldap_next_reference(3)"
name: "ldap_next_reference"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_next_reference/"
description: "ldap_first_reference, ldap_next_reference, ldap_count_references – Stepping through continuation references in a result chain"
---

<h2 class="name">NAME</h2>
<p> ldap_first_reference, ldap_next_reference, ldap_count_references &#8211; Stepping through continuation references in a result chain </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_count_references(LDAP *ld, LDAPMessage *result)
    LDAPMessage *ldap_first_reference(LDAP *ld, LDAPMessage *result)
        LDAPMessage *ldap_next_reference(LDAP *ld, LDAPMessage *reference)
</code></pre>
<h2>DESCRIPTION</h2>
<p> These routines are used to step through the continuation references in a result chain received from <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3) or the synchronous LDAP search operation routines. </p>
<p> The <code>ldap_first_reference()</code> routine is used to retrieve the first reference message in a result chain. It takes the <i>result</i> as returned by a call to <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-ldap_search_s/">ldap_search_s</a></code>(3) or <code><a href="/docs/linux/man/3-ldap_search_st/">ldap_search_st</a></code>(3) and returns a pointer to the first reference message in the result chain. </p>
<p> This pointer should be supplied on a subsequent call to <code>ldap_next_reference()</code> to get the next reference message, the result of which should be supplied to the next call to <code>ldap_next_reference()</code>, etc. <code>ldap_next_reference()</code> will return NULL when there are no more reference messages. The reference messages returned from these calls are used by <code><a href="/docs/linux/man/3-ldap_parse_reference/">ldap_parse_reference</a></code>(3) to extract referrals and controls. </p>
<p> A count of the number of reference messages in the search result can be obtained by calling <code>ldap_count_references()</code>. It can also be used to count the number of reference messages remaining in a result chain.</p>
<h2>ERRORS</h2>
<p> If an error occurs in <code>ldap_first_reference()</code> or <code>ldap_next_reference()</code>, NULL is returned. If an error occurs in <code>ldap_count_references()</code>, -1 is returned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3), <code><a href="/docs/linux/man/3-ldap_search/">ldap_search</a></code>(3), <code><a href="/docs/linux/man/3-ldap_parse_reference/">ldap_parse_reference</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
