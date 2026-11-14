---
title: "ldap_add_s(3)"
name: "ldap_add_s"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_add_s/"
description: "ldap_add_ext, ldap_add_ext_s – Perform an LDAP add operation"
---

<h2 class="name">NAME</h2>
<p> ldap_add_ext, ldap_add_ext_s &#8211; Perform an LDAP add operation </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<p> <code> #include &lt;ldap.h&gt; </p>
<p> </code></p>
<pre><code>
int ldap_add_ext(
    LDAP *ld,
    const char *dn,
    LDAPMod **attrs,
    LDAPControl **sctrls,
    LDAPControl **cctrls,
    int *msgidp);

int ldap_add_ext_s(
    LDAP *ld,
    const char *dn,
    LDAPMod **attrs,
    LDAPControl *sctrls,
    LDAPControl *cctrls);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ldap_add_ext_s()</code> routine is used to perform an LDAP add operation. It takes <i>dn</i>, the DN of the entry to add, and <i>attrs</i>, a null-terminated array of the entry&#8217;s attributes. The LDAPMod structure is used to represent attributes, with the <i>mod_type</i> and <i>mod_values</i> fields being used as described under <code><a href="/docs/linux/man/3-ldap_modify_ext/">ldap_modify_ext</a></code>(3), and the <i>ldap_op</i> field being used only if you need to specify the LDAP_MOD_BVALUES option. Otherwise, it should be set to zero. </p>
<p> Note that all entries except that specified by the last component in the given DN must already exist. <code>ldap_add_ext_s()</code> returns an code indicating success or, in the case of failure, indicating the nature of failure of the operation. See <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3) for more details. </p>
<p> The <code>ldap_add_ext()</code> routine works just like <code>ldap_add_ext_s()</code>, but it is asynchronous. It returns the message id of the request it initiated. The result of this operation can be obtained by calling <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3).</p>
<h2>DEPRECATED INTERFACES</h2>
<p> The <code>ldap_add</code>() and <code>ldap_add_s</code>() routines are deprecated in favor of the <code>ldap_add_ext</code>() and <code>ldap_add_ext_s</code>() routines, respectively. </p>
<p> Deprecated interfaces generally remain in the library. The macro LDAP_DEPRECATED can be defined to a non-zero value (e.g., -DLDAP_DEPRECATED=1) when compiling program designed to use deprecated interfaces. It is recommended that developers writing new programs, or updating old programs, avoid use of deprecated interfaces. Over time, it is expected that documentation (and, eventually, support) for deprecated interfaces to be eliminated.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3), <code><a href="/docs/linux/man/3-ldap_modify/">ldap_modify</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
