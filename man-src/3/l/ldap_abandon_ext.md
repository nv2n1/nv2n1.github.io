---
title: "ldap_abandon_ext(3)"
name: "ldap_abandon_ext"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_abandon_ext/"
description: "ldap_abandon_ext – Abandon an LDAP operation in progress"
---

<h2 class="name">NAME</h2>
<p> ldap_abandon_ext &#8211; Abandon an LDAP operation in progress </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_abandon_ext(
    LDAP *ld,
    Bint msgid,
    LDAPControl **sctrls,
    LDAPControl **cctrls);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ldap_abandon_ext()</code> routine is used to send a LDAP Abandon request for an operation in progress. The <i>msgid</i> passed should be the message id of an outstanding LDAP operation, such as returned by <code><a href="/docs/linux/man/3-ldap_search_ext/">ldap_search_ext</a></code>(3). </p>
<p> <code>ldap_abandon_ext</code>() checks to see if the result of the operation has already come in. If it has, it deletes it from the queue of pending messages. If not, it sends an LDAP abandon request to the LDAP server. </p>
<p> The caller can expect that the result of an abandoned operation will not be returned from a future call to <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3). </p>
<p> <code>ldap_abandon_ext()</code> allows server and client controls to be passed in via the <i>sctrls</i> and <i>cctrls</i> parameters, respectively. </p>
<p> <code>ldap_abandon_ext()</code> returns a code indicating success or, in the case of failure, the nature of the failure. See <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3) for details.</p>
<h2>DEPRECATED INTERFACES</h2>
<p> The <code>ldap_abandon()</code> routine is deprecated in favor of the <code>ldap_abandon_ext()</code> routine. </p>
<p> Deprecated interfaces generally remain in the library. The macro LDAP_DEPRECATED can be defined to a non-zero value (e.g., -DLDAP_DEPRECATED=1) when compiling program designed to use deprecated interfaces. It is recommended that developers writing new programs, or updating old programs, avoid use of deprecated interfaces. Over time, it is expected that documentation (and, eventually, support) for deprecated interfaces to be eliminated. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3), <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3), <code><a href="/docs/linux/man/3-ldap_search_ext/">ldap_search_ext</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
