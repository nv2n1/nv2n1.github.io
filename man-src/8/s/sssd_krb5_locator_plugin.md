---
title: "sssd_krb5_locator_plugin(8)"
name: "sssd_krb5_locator_plugin"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sssd_krb5_locator_plugin/"
description: "sssd_krb5_locator_plugin – Kerberos locator plugin"
---

<p>sssd_krb5_locator_plugin &#8211; Kerberos locator plugin</p>
<h2>Description</h2>
<p>The Kerberos locator plugin <code>sssd_krb5_locator_plugin</code> is used by the Kerberos provider of <code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8) to tell the Kerberos libraries what Realm and which KDC to use. Typically this is done in <code><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a></code>(5) which is always read by the Kerberos libraries. To simplify the configuration the Realm and the KDC can be defined in <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) as described in <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5) </p>
<p> <code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8) puts the Realm and the name or IP address of the KDC into the environment variables SSSD_KRB5_REALM and SSSD_KRB5_KDC respectively. When <code>sssd_krb5_locator_plugin</code> is called by the kerberos libraries it reads and evaluates these variables and returns them to the libraries.</p>
<h2>Notes</h2>
<p>Not all Kerberos implementations support the use of plugins. If <code>sssd_krb5_locator_plugin</code> is not available on your system you have to edit /etc/krb5.conf to reflect your Kerberos setup. </p>
<p> If the environment variable SSSD_KRB5_LOCATOR_DEBUG is set to any value debug messages will be sent to stderr.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/5-sssd-secrets/">sssd-secrets</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="https://pagure.io/SSSD/sssd/">https://pagure.io/SSSD/sssd/</a></code></p>
