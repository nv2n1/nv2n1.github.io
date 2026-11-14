---
title: "ldap_parse_reference(3)"
name: "ldap_parse_reference"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_parse_reference/"
description: "ldap_parse_reference – Extract referrals and controls from a reference message"
---

<h2 class="name">NAME</h2>
<p> ldap_parse_reference &#8211; Extract referrals and controls from a reference message </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
int ldap_parse_reference(LDAP *ld, LDAPMessage *reference,
                         char ***referralsp, LDAPControl ***serverctrlsp,
                         int freeit)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ldap_parse_reference()</code> routine is used to extract referrals and controls from a reference message. The <i>reference</i> parameter is a reference message as returned by a call to <code><a href="/docs/linux/man/3-ldap_first_reference/">ldap_first_reference</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-ldap_next_reference/">ldap_next_reference</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-ldap_first_message/">ldap_first_message</a></code>(3)<code>,</code> <code><a href="/docs/linux/man/3-ldap_next_message/">ldap_next_message</a></code>(3)<code>,</code> or <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3)<code>.</code> </p>
<p> The <i>referralsp</i> parameter will be filled in with an allocated array of character strings. The strings are copies of the referrals contained in the parsed message. The array should be freed by calling <code><a href="/docs/linux/man/3-ldap_value_free/">ldap_value_free</a></code>(3)<code>.</code> If <i>referralsp</i> is NULL, no referrals are returned. If no referrals were returned, <i>*referralsp</i> is set to NULL. </p>
<p> The <i>serverctrlsp</i> parameter will be filled in with an allocated array of controls copied from the parsed message. The array should be freed by calling <code><a href="/docs/linux/man/3-ldap_controls_free/">ldap_controls_free</a></code>(3). If <i>serverctrlsp</i> is NULL, no controls are returned. If no controls were returned, <i>*serverctrlsp</i> is set to NULL. </p>
<p> The <i>freeit</i> parameter determines whether the parsed message is freed or not after the extraction. Any non-zero value will make it free the message. The <code><a href="/docs/linux/man/3-ldap_msgfree/">ldap_msgfree</a></code>(3) routine can also be used to free the message later.</p>
<h2>ERRORS</h2>
<p> Upon success LDAP_SUCCESS is returned. Otherwise the values of the <i>referralsp</i> and <i>serverctrlsp</i> parameters are undefined.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_first_reference/">ldap_first_reference</a></code>(3), <code><a href="/docs/linux/man/3-ldap_first_message/">ldap_first_message</a></code>(3), <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3), <code><a href="/docs/linux/man/3-ldap_get_values/">ldap_get_values</a></code>(3), <code><a href="/docs/linux/man/3-ldap_controls_free/">ldap_controls_free</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
