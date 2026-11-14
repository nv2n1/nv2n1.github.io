---
title: "sssd-files(5)"
name: "sssd-files"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sssd-files/"
description: "sssd-files – SSSD files provider"
---

<p>sssd-files &#8211; SSSD files provider</p>
<h2>Description</h2>
<p>This manual page describes the files provider for <code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8). For a detailed syntax reference, refer to the &#8220;FILE FORMAT&#8221; section of the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page. </p>
<p> The files provider mirrors the content of the <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5) and <code><a href="/docs/linux/man/5-group/">group</a></code>(5) files. The purpose of the files provider is to make the users and groups traditionally only accessible with NSS interfaces also available through the SSSD interfaces such as <code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5).</p>
<h2>Configuration Options</h2>
<p>The files provider has no specific options of its own, however, generic SSSD domain options can be set where applicable. Refer to the section &#8220;DOMAIN SECTIONS&#8221; of the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page for details on the configuration of an SSSD domain.</p>
<h2>Example</h2>
<p>The following example assumes that SSSD is correctly configured and files is one of the domains in the <i>[sssd]</i> section.</p>
<dl>
<dd>
<pre>[domain/files]
id_provider = files</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/5-sssd-secrets/">sssd-secrets</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="https://pagure.io/SSSD/sssd/">https://pagure.io/SSSD/sssd/</a></code></p>
