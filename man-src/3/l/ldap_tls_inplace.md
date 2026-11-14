---
title: "ldap_tls_inplace(3)"
name: "ldap_tls_inplace"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_tls_inplace/"
description: "ldap_start_tls, ldap_start_tls_s, ldap_tls_inplace, ldap_install_tls – LDAP TLS initialization routines"
---

<h2 class="name">NAME</h2>
<p> ldap_start_tls, ldap_start_tls_s, ldap_tls_inplace, ldap_install_tls &#8211; LDAP TLS initialization routines </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;ldap.h&gt;</code> </p>
<p> <code>int ldap_start_tls(LDAP *</code><i>ld</i><code>);</code> </p>
<p> <code>int ldap_start_tls_s(LDAP *</code><i>ld</i><code>, LDAPControl **</code><i>serverctrls</i><code>, LDAPControl **</code><i>clientctrls</i><code>);</code> </p>
<p> <code>int ldap_tls_inplace(LDAP *</code><i>ld</i><code>);</code> </p>
<p> <code>int ldap_install_tls(LDAP *</code><i>ld</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> These routines are used to initiate TLS processing on an LDAP session. <code>ldap_start_tls_s</code>() sends a StartTLS request to a server, waits for the reply, and then installs TLS handlers on the session if the request succeeded. The routine returns <code>LDAP_SUCCESS</code> if everything succeeded, otherwise it returns an LDAP error code. <code>ldap_start_tls</code>() sends a StartTLS request to a server and does nothing else. It returns <code>LDAP_SUCCESS</code> if the request was sent successfully. <code>ldap_tls_inplace</code>() returns 1 if TLS handlers have been installed on the specified session, 0 otherwise. <code>ldap_install_tls</code>() installs the TLS handlers on the given session. It returns <code>LDAP_LOCAL_ERROR</code> if TLS is already installed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_error/">ldap_error</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
