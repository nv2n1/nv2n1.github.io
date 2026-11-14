---
title: "sssd-sudo(5)"
name: "sssd-sudo"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sssd-sudo/"
description: "sssd-sudo – Configuring sudo with the SSSD back end"
---

<p>sssd-sudo &#8211; Configuring sudo with the SSSD back end</p>
<h2>Description</h2>
<p>This manual page describes how to configure <code><a href="/docs/linux/man/8-sudo/">sudo</a></code>(8) to work with <code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8) and how SSSD caches sudo rules.</p>
<h2>Configuring Sudo To Cooperate With Sssd</h2>
<p>To enable SSSD as a source for sudo rules, add <i>sss</i> to the <i>sudoers</i> entry in <code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5). </p>
<p> For example, to configure sudo to first lookup rules in the standard <code><a href="/docs/linux/man/5-sudoers/">sudoers</a></code>(5) file (which should contain rules that apply to local users) and then in SSSD, the nsswitch.conf file should contain the following line: </p>
<dl>
<dd>
<pre>sudoers: files sss</pre>
</dl>
<p> More information about configuring the sudoers search order from the nsswitch.conf file as well as information about the LDAP schema that is used to store sudo rules in the directory can be found in <code><a href="/docs/linux/man/5-sudoers-ldap/">sudoers.ldap</a></code>(5). </p>
<p> <i>Note</i>: in order to use netgroups or IPA hostgroups in sudo rules, you also need to correctly set <code><a href="/docs/linux/man/1-nisdomainname/">nisdomainname</a></code>(1) to your NIS domain name (which equals to IPA domain name when using hostgroups).</p>
<h2>Configuring Sssd To Fetch Sudo Rules</h2>
<p>All configuration that is needed on SSSD side is to extend the list of <i>services</i> with &quot;sudo&quot; in [sssd] section of <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5). To speed up the LDAP lookups, you can also set search base for sudo rules using <i>ldap_sudo_search_base</i> option. </p>
<p> The following example shows how to configure SSSD to download sudo rules from an LDAP server. </p>
<dl>
<dd>
<pre>[sssd]
config_file_version = 2
services = nss, pam, sudo
domains = EXAMPLE
[domain/EXAMPLE]
id_provider = ldap
sudo_provider = ldap
ldap_uri = <a href="ldap://example.com">ldap://example.com</a>
ldap_sudo_search_base = ou=sudoers,dc=example,dc=com</pre>
</dl>
<p> It&#8217;s important to note that on platforms where systemd is supported there&#8217;s no need to add the &quot;sudo&quot; provider to the list of services, as it became optional. However, sssd-sudo.socket must be enabled instead. </p>
<p> When SSSD is configured to use IPA as the ID provider, the sudo provider is automatically enabled. The sudo search base is configured to use the IPA native LDAP tree (cn=sudo,$SUFFIX). If any other search base is defined in sssd.conf, this value will be used instead. The compat tree (ou=sudoers,$SUFFIX) is no longer required for IPA sudo functionality.</p>
<h2>The Sudo Rule Caching Mechanism</h2>
<p>The biggest challenge, when developing sudo support in SSSD, was to ensure that running sudo with SSSD as the data source provides the same user experience and is as fast as sudo but keeps providing the most current set of rules as possible. To satisfy these requirements, SSSD uses three kinds of updates. They are referred to as full refresh, smart refresh and rules refresh. </p>
<p> The <i>smart refresh</i> periodically downloads rules that are new or were modified after the last update. Its primary goal is to keep the database growing by fetching only small increments that do not generate large amounts of network traffic. </p>
<p> The <i>full refresh</i> simply deletes all sudo rules stored in the cache and replaces them with all rules that are stored on the server. This is used to keep the cache consistent by removing every rule which was deleted from the server. However, full refresh may produce a lot of traffic and thus it should be run only occasionally depending on the size and stability of the sudo rules. </p>
<p> The <i>rules refresh</i> ensures that we do not grant the user more permission than defined. It is triggered each time the user runs sudo. Rules refresh will find all rules that apply to this user, check their expiration time and redownload them if expired. In the case that any of these rules are missing on the server, the SSSD will do an out of band full refresh because more rules (that apply to other users) may have been deleted. </p>
<p> If enabled, SSSD will store only rules that can be applied to this machine. This means rules that contain one of the following values in <i>sudoHost</i> attribute: </p>
<dl>
<dd>&bull; keyword ALL</dl>
<dl>
<dd>&bull; wildcard</dl>
<dl>
<dd>&bull; netgroup (in the form &quot;+netgroup&quot;)</dl>
<dl>
<dd>&bull; hostname or fully qualified domain name of this machine</dl>
<dl>
<dd>&bull; one of the IP addresses of this machine</dl>
<dl>
<dd>&bull; one of the IP addresses of the network (in the form &quot;address/mask&quot;)</dl>
<p> There are many configuration options that can be used to adjust the behavior. Please refer to &quot;ldap_sudo_*&quot; in <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5) and &quot;sudo_*&quot; in <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/5-sssd-secrets/">sssd-secrets</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="https://pagure.io/SSSD/sssd/">https://pagure.io/SSSD/sssd/</a></code></p>
