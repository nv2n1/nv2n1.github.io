---
title: "ldap_msgid(3)"
name: "ldap_msgid"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_msgid/"
description: "ldap_result – Wait for the result of an LDAP operation"
---

<h2 class="name">NAME</h2>
<p> ldap_result &#8211; Wait for the result of an LDAP operation </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_result(LDAP *ld, int msgid, int all,
                struct timeval *timeout, LDAPMessage **result);
int ldap_msgfree(LDAPMessage *msg);
int ldap_msgtype(LDAPMessage *msg);
int ldap_msgid(LDAPMessage *msg);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ldap_result()</code> routine is used to wait for and return the result of an operation previously initiated by one of the LDAP asynchronous operation routines (e.g., <code><a href="/docs/linux/man/3-ldap_search_ext/">ldap_search_ext</a></code>(3), <code><a href="/docs/linux/man/3-ldap_modify_ext/">ldap_modify_ext</a></code>(3), etc.). Those routines all return -1 in case of error, and an invocation identifier upon successful initiation of the operation. The invocation identifier is picked by the library and is guaranteed to be unique across the LDAP session. It can be used to request the result of a specific operation from <code>ldap_result()</code> through the <i>msgid</i> parameter. </p>
<p> The <code>ldap_result()</code> routine will block or not, depending upon the setting of the <i>timeout</i> parameter. If timeout is not a NULL pointer, it specifies a maximum interval to wait for the selection to complete. If timeout is a NULL pointer, the LDAP_OPT_TIMEOUT value set by <code><a href="/docs/linux/man/3-ldap_set_option/">ldap_set_option</a></code>(3) is used. With the default setting, the select blocks indefinitely. To effect a poll, the timeout argument should be a non-NULL pointer, pointing to a zero-valued timeval structure. To obtain the behavior of the default setting, bypassing any value set by <code><a href="/docs/linux/man/3-ldap_set_option/">ldap_set_option</a></code>(3), set to -1 the <i>tv_sec</i> field of the <i>timeout</i> parameter. See <code><a href="/docs/linux/man/2-select/">select</a></code>(2) for further details. </p>
<p> If the result of a specific operation is required, <i>msgid</i> should be set to the invocation identifier returned when the operation was initiated, otherwise LDAP_RES_ANY or LDAP_RES_UNSOLICITED should be supplied to wait for any or unsolicited response. </p>
<p> The <i>all</i> parameter, if non-zero, causes <code>ldap_result()</code> to return all responses with msgid, otherwise only the next response is returned. This is commonly used to obtain all the responses of a search operation. </p>
<p> A search response is made up of zero or more search entries, zero or more search references, and zero or more extended partial responses followed by a search result. If <i>all</i> is set to 0, search entries will be returned one at a time as they come in, via separate calls to <code>ldap_result()</code>. If it&#8217;s set to 1, the search response will only be returned in its entirety, i.e., after all entries, all references, all extended partial responses, and the final search result have been received.</p>
<h2>RETURN VALUE</h2>
<p> Upon success, the type of the result received is returned and the <i>result</i> parameter will contain the result of the operation; otherwise, the <i>result</i> parameter is undefined. This result should be passed to the LDAP parsing routines, <code><a href="/docs/linux/man/3-ldap_first_message/">ldap_first_message</a></code>(3) and friends, for interpretation. </p>
<p> The possible result types returned are: </p>
<pre>
        LDAP_RES_BIND (0x61)
        LDAP_RES_SEARCH_ENTRY (0x64)
        LDAP_RES_SEARCH_REFERENCE (0x73)
        LDAP_RES_SEARCH_RESULT (0x65)
        LDAP_RES_MODIFY (0x67)
        LDAP_RES_ADD (0x69)
        LDAP_RES_DELETE (0x6b)
        LDAP_RES_MODDN (0x6d)
        LDAP_RES_COMPARE (0x6f)
        LDAP_RES_EXTENDED (0x78)
        LDAP_RES_INTERMEDIATE (0x79)
</pre>
<p> The <code>ldap_msgfree()</code> routine is used to free the memory allocated for result(s) by <code>ldap_result()</code> or <code><a href="/docs/linux/man/3-ldap_search_ext_s/">ldap_search_ext_s</a></code>(3) and friends. It takes a pointer to the result or result chain to be freed and returns the type of the last message in the chain. If the parameter is NULL, the function does nothing and returns zero. </p>
<p> The <code>ldap_msgtype()</code> routine returns the type of a message. </p>
<p> The <code>ldap_msgid()</code> routine returns the message id of a message.</p>
<h2>ERRORS</h2>
<p> <code>ldap_result()</code> returns -1 if something bad happens, and zero if the timeout specified was exceeded. <code>ldap_msgtype()</code> and <code>ldap_msgid()</code> return -1 on error.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_first_message/">ldap_first_message</a></code>(3), <code><a href="/docs/linux/man/2-select/">select</a></code>(2)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
