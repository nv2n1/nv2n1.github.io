---
title: "ldap_search_s(3)"
name: "ldap_search_s"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_search_s/"
description: "ldap_search, ldap_search_s, ldap_search_st, ldap_search_ext, ldap_search_ext_s – Perform an LDAP search operation"
---

<h2 class="name">NAME</h2>
<p> ldap_search, ldap_search_s, ldap_search_st, ldap_search_ext, ldap_search_ext_s &#8211; Perform an LDAP search operation </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
#include &lt;sys/types.h&gt;
int ldap_search_ext(
    LDAP *ld,
    char *base,
    int scope,
    char *filter,
    char *attrs[],
    int attrsonly,
    LDAPControl **serverctrls,
    LDAPControl **clientctrls,
    struct timeval *timeout,
    int sizelimit,
    int *msgidp);

int ldap_search_ext_s(
    LDAP *ld,
    char *base,
    int scope,
    char *filter,
    char *attrs[],
    int attrsonly,
    LDAPControl **serverctrls,
    LDAPControl **clientctrls,
    struct timeval *timeout,
    int sizelimit,
    LDAPMessage **res);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These routines are used to perform LDAP search operations. The <code>ldap_search_ext_s()</code> routine does the search synchronously (i.e., not returning until the operation completes), providing a pointer to the resulting LDAP messages at the location pointed to by the <i>res</i> parameter. </p>
<p> The <code>ldap_search_ext()</code> routine is the asynchronous version, initiating the search and returning the message id of the operation it initiated in the integer pointed to by the <i>msgidp</i> parameter. </p>
<p> The <i>base</i> parameter is the DN of the entry at which to start the search. </p>
<p> The <i>scope</i> parameter is the scope of the search and should be one of LDAP_SCOPE_BASE, to search the object itself, LDAP_SCOPE_ONELEVEL, to search the object&#8217;s immediate children, LDAP_SCOPE_SUBTREE, to search the object and all its descendants, or LDAP_SCOPE_CHILDREN, to search all of the descendants. Note that the latter requires the server support the LDAP Subordinates Search Scope extension. </p>
<p> The <i>filter</i> is a string representation of the filter to apply in the search. The string should conform to the format specified in RFC 4515 as extended by RFC 4526. For instance, &quot;(cn=Jane Doe)&quot;. Note that use of the extension requires the server to support the LDAP Absolute True/False Filter extension. NULL may be specified to indicate the library should send the filter (objectClass=*). </p>
<p> The <i>attrs</i> parameter is a null-terminated array of attribute descriptions to return from matching entries. If NULL is specified, the return of all user attributes is requested. The description &quot;*&quot; (LDAP_ALL_USER_ATTRIBUTES) may be used to request all user attributes to be returned. The description &quot;+&quot;(LDAP_ALL_OPERATIONAL_ATTRIBUTES) may be used to request all operational attributes to be returned. Note that this requires the server to support the LDAP All Operational Attribute extension. To request no attributes, the description &quot;1.1&quot; (LDAP_NO_ATTRS) should be listed by itself. </p>
<p> The <i>attrsonly</i> parameter should be set to a non-zero value if only attribute descriptions are wanted. It should be set to zero (0) if both attributes descriptions and attribute values are wanted. </p>
<p> The <i>serverctrls</i> and <i>clientctrls</i> parameters may be used to specify server and client controls, respectively. </p>
<p> The <code>ldap_search_ext_s()</code> routine is the synchronous version of <code>ldap_search_ext().</code> </p>
<p> It also returns a code indicating success or, in the case of failure, indicating the nature of the failure of the operation. See <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3) for details.</p>
<h2>NOTES</h2>
<p> Note that both read and list functionality are subsumed by these routines, by using a filter like &quot;(objectclass=*)&quot; and a scope of LDAP_SCOPE_BASE (to emulate read) or LDAP_SCOPE_ONELEVEL (to emulate list). </p>
<p> These routines may dynamically allocate memory. The caller is responsible for freeing such memory using supplied deallocation routines. Return values are contained in &lt;ldap.h&gt;. </p>
<p> Note that <i>res</i> parameter of <code>ldap_search_ext_s()</code> and <code>ldap_search_s()</code> should be freed with <code>ldap_msgfree()</code> regardless of return value of these functions.</p>
<h2>DEPRECATED INTERFACES</h2>
<p> The <code>ldap_search()</code> routine is deprecated in favor of the <code>ldap_search_ext()</code> routine. The <code>ldap_search_s()</code> and <code>ldap_search_st()</code> routines are deprecated in favor of the <code>ldap_search_ext_s()</code> routine. </p>
<p> Deprecated interfaces generally remain in the library. The macro LDAP_DEPRECATED can be defined to a non-zero value (e.g., -DLDAP_DEPRECATED=1) when compiling program designed to use deprecated interfaces. It is recommended that developers writing new programs, or updating old programs, avoid use of deprecated interfaces. Over time, it is expected that documentation (and, eventually, support) for deprecated interfaces to be eliminated.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3), <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
