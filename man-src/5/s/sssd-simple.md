---
title: "sssd-simple(5)"
name: "sssd-simple"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sssd-simple/"
description: "sssd-simple – the configuration file for SSSD’s ‘simple’ access-control provider"
---

<p>sssd-simple &#8211; the configuration file for SSSD&#8217;s &#8216;simple&#8217; access-control provider</p>
<h2>Description</h2>
<p>This manual page describes the configuration of the simple access-control provider for <code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8). For a detailed syntax reference, refer to the &#8220;FILE FORMAT&#8221; section of the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page. The simple access provider grants or denies access based on an access or deny list of user or group names. The following rules apply:</p>
<dl>
<dd>&bull; If all lists are empty, access is granted</dl>
<dl>
<dd>&bull; If any list is provided, the order of evaluation is allow,deny. This means that any matching deny rule will supersede any matched allow rule.</dl>
<dl>
<dd>&bull; If either or both &quot;allow&quot; lists are provided, all users are denied unless they appear in the list.</dl>
<dl>
<dd>&bull; If only &quot;deny&quot; lists are provided, all users are granted access unless they appear in the list.</dl>
<h2>Configuration Options</h2>
<p>Refer to the section &#8220;DOMAIN SECTIONS&#8221; of the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page for details on the configuration of an SSSD domain. </p>
<p> simple_allow_users (string)</p>
<dl>
<dd>Comma separated list of users who are allowed to log in.</dl>
<p> simple_deny_users (string)</p>
<dl>
<dd>Comma separated list of users who are explicitly denied access.</dl>
<p> simple_allow_groups (string)</p>
<dl>
<dd>Comma separated list of groups that are allowed to log in. This applies only to groups within this SSSD domain. Local groups are not evaluated.</dl>
<p> simple_deny_groups (string)</p>
<dl>
<dd>Comma separated list of groups that are explicitly denied access. This applies only to groups within this SSSD domain. Local groups are not evaluated.</dl>
<p> Specifying no values for any of the lists is equivalent to skipping it entirely. Beware of this while generating parameters for the simple provider using automated scripts. </p>
<p> Please note that it is an configuration error if both, simple_allow_users and simple_deny_users, are defined.</p>
<h2>Example</h2>
<p>The following example assumes that SSSD is correctly configured and example.com is one of the domains in the <i>[sssd]</i> section. This examples shows only the simple access provider-specific options.</p>
<dl>
<dd>
<pre>[domain/example.com]
access_provider = simple
simple_allow_users = user1, user2</pre>
</dl>
<h2>Notes</h2>
<p>The complete group membership hierarchy is resolved before the access check, thus even nested groups can be included in the access lists. Please be aware that the &#8220;ldap_group_nesting_level&#8221; option may impact the results and should be set to a sufficient value. (<code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5)) option.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/5-sssd-secrets/">sssd-secrets</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="https://pagure.io/SSSD/sssd/">https://pagure.io/SSSD/sssd/</a></code></p>
