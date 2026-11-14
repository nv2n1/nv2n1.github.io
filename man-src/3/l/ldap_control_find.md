---
title: "ldap_control_find(3)"
name: "ldap_control_find"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_control_find/"
description: "ldap_control_create, ldap_control_find, ldap_control_dup, ldap_controls_dup, ldap_control_free, ldap_controls_free – LDAP control manipulation routines"
---

<h2 class="name">NAME</h2>
<p> ldap_control_create, ldap_control_find, ldap_control_dup, ldap_controls_dup, ldap_control_free, ldap_controls_free &#8211; LDAP control manipulation routines </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;ldap.h&gt;</code> </p>
<p> <code>int ldap_control_create(const char *</code><i>oid</i><code>, int </code><i>iscritical</i><code>, struct berval *</code><i>value</i><code>, int </code><i>dupval</i><code>, LDAPControl **</code><i>ctrlp</i><code>);</code> </p>
<p> <code>LDAPControl *ldap_control_find( const char *</code><i>oid</i><code>, LDAPControl **</code><i>ctrls</i><code>, LDAPControl ***</code><i>nextctrlp</i><code>);</code> </p>
<p> <code>LDAPControl *ldap_control_dup(LDAPControl *</code><i>ctrl</i><code>);</code> </p>
<p> <code>LDAPControl **ldap_controls_dup(LDAPControl **</code><i>ctrls</i><code>);</code> </p>
<p> <code>void ldap_control_free(LDAPControl *</code><i>ctrl</i><code>);</code> </p>
<p> <code>void ldap_controls_free(LDAPControl **</code><i>ctrls</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> These routines are used to manipulate structures used for LDAP controls. </p>
<p> <code>ldap_control_create</code>() creates a control with the specified <i>OID</i> using the contents of the <i>value</i> parameter for the control value, if any. The content of <i>value </i> is duplicated if <i>dupval</i> is non-zero. The <i>iscritical</i> parameter must be non-zero for a critical control. The created control is returned in the <i>ctrlp</i> parameter. The routine returns <code>LDAP_SUCCESS</code> on success or some other error code on failure. The content of <i>value</i>, for supported control types, can be prepared using helpers provided by this implementation of libldap, usually in the form <code>ldap_create_&lt;control name&gt;_control_value</code>(). Otherwise, it can be BER-encoded using the functionalities of liblber. </p>
<p> <code>ldap_control_find</code>() searches the NULL-terminated <i>ctrls</i> array for a control whose OID matches the <i>oid</i> parameter. The routine returns a pointer to the control if found, NULL otherwise. If the parameter <i>nextctrlp</i> is not NULL, on return it will point to the next control in the array, and can be passed to the <code>ldap_control_find</code>() routine for subsequent calls, to find further occurrences of the same control type. The use of this function is discouraged; the recommended way of handling controls in responses consists in going through the array of controls, dealing with each of them in the returned order, since it could matter. </p>
<p> <code>ldap_control_dup</code>() duplicates an individual control structure, and <code>ldap_controls_dup</code>() duplicates a NULL-terminated array of controls. </p>
<p> <code>ldap_control_free</code>() frees an individual control structure, and <code>ldap_controls_free</code>() frees a NULL-terminated array of controls. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
