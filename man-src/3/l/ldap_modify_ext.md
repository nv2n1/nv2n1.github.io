---
title: "ldap_modify_ext(3)"
name: "ldap_modify_ext"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_modify_ext/"
description: "ldap_modify_ext, ldap_modify_ext_s – Perform an LDAP modify operation"
---

<h2 class="name">NAME</h2>
<p> ldap_modify_ext, ldap_modify_ext_s &#8211; Perform an LDAP modify operation </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_modify_ext(
    LDAP *ld,
    char *dn,
    LDAPMod *mods[],
    LDAPControl **sctrls,
    LDAPControl **cctrls,
    int *msgidp);

int ldap_modify_ext_s(
    LDAP *ld,
    char *dn,
    LDAPMod *mods[],
    LDAPControl **sctrls,
    LDAPControl **cctrls);

void ldap_mods_free(
    LDAPMod **mods,
    int freemods);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The routine <code>ldap_modify_ext_s()</code> is used to perform an LDAP modify operation. <i>dn</i> is the DN of the entry to modify, and <i>mods</i> is a null-terminated array of modifications to make to the entry. Each element of the <i>mods</i> array is a pointer to an LDAPMod structure, which is defined below. </p>
<pre><code>
typedef struct ldapmod {
    int mod_op;
    char *mod_type;
    union {
        char **modv_strvals;
        struct berval **modv_bvals;
    } mod_vals;
    struct ldapmod *mod_next;
} LDAPMod;
#define mod_values mod_vals.modv_strvals
#define mod_bvalues mod_vals.modv_bvals
</code></pre>
<p> The <i>mod_op</i> field is used to specify the type of modification to perform and should be one of LDAP_MOD_ADD, LDAP_MOD_DELETE, or LDAP_MOD_REPLACE. The <i>mod_type</i> and <i>mod_values</i> fields specify the attribute type to modify and a null-terminated array of values to add, delete, or replace respectively. The <i>mod_next</i> field is used only by the LDAP server and may be ignored by the client. </p>
<p> If you need to specify a non-string value (e.g., to add a photo or audio attribute value), you should set <i>mod_op</i> to the logical OR of the operation as above (e.g., LDAP_MOD_REPLACE) and the constant LDAP_MOD_BVALUES. In this case, <i>mod_bvalues</i> should be used instead of <i>mod_values</i>, and it should point to a null-terminated array of struct bervals, as defined in &lt;lber.h&gt;. </p>
<p> For LDAP_MOD_ADD modifications, the given values are added to the entry, creating the attribute if necessary. For LDAP_MOD_DELETE modifications, the given values are deleted from the entry, removing the attribute if no values remain. If the entire attribute is to be deleted, the <i>mod_values</i> field should be set to NULL. For LDAP_MOD_REPLACE modifications, the attribute will have the listed values after the modification, having been created if necessary. All modifications are performed in the order in which they are listed. </p>
<p> <code>ldap_mods_free()</code> can be used to free each element of a NULL-terminated array of mod structures. If <i>freemods</i> is non-zero, the <i>mods</i> pointer itself is freed as well. </p>
<p> <code>ldap_modify_ext_s()</code> returns a code indicating success or, in the case of failure, indicating the nature of the failure. See <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3) for details </p>
<p> The <code>ldap_modify_ext()</code> operation works the same way as <code>ldap_modify_ext_s()</code>, except that it is asynchronous. The integer that <i>msgidp</i> points to is set to the message id of the modify request. The result of the operation can be obtained by calling <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3). </p>
<p> Both <code>ldap_modify_ext() </code> and <code>ldap_modify_ext_s() </code> allows server and client controls to be passed in via the sctrls and cctrls parameters, respectively.</p>
<h2>DEPRECATED INTERFACES</h2>
<p> The <code>ldap_modify()</code> and <code>ldap_modify_s()</code> routines are deprecated in favor of the <code>ldap_modify_ext()</code> and <code>ldap_modify_ext_s()</code> routines, respectively. </p>
<p> Deprecated interfaces generally remain in the library. The macro LDAP_DEPRECATED can be defined to a non-zero value (e.g., -DLDAP_DEPRECATED=1) when compiling program designed to use deprecated interfaces. It is recommended that developers writing new programs, or updating old programs, avoid use of deprecated interfaces. Over time, it is expected that documentation (and, eventually, support) for deprecated interfaces to be eliminated.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3),</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
