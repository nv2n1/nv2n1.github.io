---
title: "sss_userdel(8)"
name: "sss_userdel"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sss_userdel/"
description: "sss_userdel – delete a user account"
---

<p>sss_userdel &#8211; delete a user account</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>sss_userdel</code> [<i>options</i>] <i>LOGIN</i></dl>
<h2>Description</h2>
<p><code>sss_userdel</code></p>
<dd>deletes a user identified by login name <i>LOGIN</i> from the system.</p>
<h2>Options</h2>
<p><code>-?</code>,<code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-r</code>,<code>&#8211;remove</code></p>
<dl>
<dd>Files in the user&#8217;s home directory will be removed along with the home directory itself and the user&#8217;s mail spool. Overrides the configuration.</dl>
<p> <code>-R</code>,<code>&#8211;no-remove</code></p>
<dl>
<dd>Files in the user&#8217;s home directory will NOT be removed along with the home directory itself and the user&#8217;s mail spool. Overrides the configuration.</dl>
<p> <code>-f</code>,<code>&#8211;force</code></p>
<dl>
<dd>This option forces <code>sss_userdel</code> to remove the user&#8217;s home directory and mail spool, even if they are not owned by the specified user.</dl>
<p> <code>-k</code>,<code>&#8211;kick</code></p>
<dl>
<dd>Before actually deleting the user, terminate all his processes.</dl>
<h2>The Local Domain</h2>
<p>In order to function correctly, a domain with &#8220;id_provider=local&#8221; must be created and the SSSD must be running. </p>
<p> The administrator might want to use the SSSD local users instead of traditional UNIX users in cases where the group nesting (see <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8)) is needed. The local users are also useful for testing and development of the SSSD without having to deploy a full remote server. The <code>sss_user*</code> and <code>sss_group*</code> tools use a local LDB storage to store users and groups.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="http://fedorahosted.org/sssd">http://fedorahosted.org/sssd</a></code></p>
