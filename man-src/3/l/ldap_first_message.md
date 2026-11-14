---
title: "ldap_first_message(3)"
name: "ldap_first_message"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_first_message/"
description: "ldap_first_message, ldap_next_message, ldap_count_messages – Stepping through messages in a result chain"
---

<h2 class="name">NAME</h2>
<p> ldap_first_message, ldap_next_message, ldap_count_messages &#8211; Stepping through messages in a result chain </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_count_messages(LDAP *ld, LDAPMessage *result)
    LDAPMessage *ldap_first_message(LDAP *ld, LDAPMessage *result)
        LDAPMessage *ldap_next_message(LDAP *ld, LDAPMessage *message)
</code></pre>
<h2>DESCRIPTION</h2>
<p> These routines are used to step through the messages in a result chain received from <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3)<code>.</code> For search operations, the result chain can contain referral, entry and result messages. The <code><a href="/docs/linux/man/3-ldap_msgtype/">ldap_msgtype</a></code>(3) function can be used to distinguish between the different message types. </p>
<p> The <code>ldap_first_message()</code> routine is used to retrieve the first message in a result chain. It takes the <i>result</i> as returned by a call to <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-ldap_search_s/">ldap_search_s</a></code>(3) or <code><a href="/docs/linux/man/3-ldap_search_st/">ldap_search_st</a></code>(3) and returns a pointer to the first message in the result chain. </p>
<p> This pointer should be supplied on a subsequent call to <code>ldap_next_message()</code> to get the next message, the result of which should be supplied to the next call to <code>ldap_next_message()</code>, etc. <code>ldap_next_message()</code> will return NULL when there are no more messages. </p>
<p> These functions are useful when using routines like <code><a href="/docs/linux/man/3-ldap_parse_result/">ldap_parse_result</a></code>(3) that only operate on the first result in the chain. </p>
<p> A count of the number of messages in the result chain can be obtained by calling <code>ldap_count_messages()</code>. It can also be used to count the number of remaining messages in a chain if called with a message, entry or reference returned by <code>ldap_first_message() ,</code> <code>ldap_next_message() ,</code> <code><a href="/docs/linux/man/3-ldap_first_entry/">ldap_first_entry</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-ldap_next_entry/">ldap_next_entry</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-ldap_first_reference/">ldap_first_reference</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-ldap_next_reference/">ldap_next_reference</a></code>(3)<code>.</code></p>
<h2>ERRORS</h2>
<p> If an error occurs in <code>ldap_first_message()</code> or <code>ldap_next_message()</code>, NULL is returned. If an error occurs in <code>ldap_count_messages()</code>, -1 is returned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_search/">ldap_search</a></code>(3), <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3), <code><a href="/docs/linux/man/3-ldap_parse_result/">ldap_parse_result</a></code>(3), <code><a href="/docs/linux/man/3-ldap_first_entry/">ldap_first_entry</a></code>(3), <code><a href="/docs/linux/man/3-ldap_first_reference/">ldap_first_reference</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
