---
title: "sss_usermod(8)"
name: "sss_usermod"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sss_usermod/"
description: "sss_usermod – modify a user account"
---

<p>sss_usermod &#8211; modify a user account</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>sss_usermod</code> [<i>options</i>] <i>LOGIN</i></dl>
<h2>Description</h2>
<p><code>sss_usermod</code></p>
<dd>modifies the account specified by <i>LOGIN</i> to reflect the changes that are specified on the command line.</p>
<h2>Options</h2>
<p><code>-c</code>,<code>&#8211;gecos</code> <i>COMMENT</i></p>
<dl>
<dd>Any text string describing the user. Often used as the field for the user&#8217;s full name.</dl>
<p> <code>-h</code>,<code>&#8211;home</code> <i>HOME_DIR</i></p>
<dl>
<dd>The home directory of the user account.</dl>
<p> <code>-s</code>,<code>&#8211;shell</code> <i>SHELL</i></p>
<dl>
<dd>The user&#8217;s login shell.</dl>
<p> <code>-a</code>,<code>&#8211;append-group</code> <i>GROUPS</i></p>
<dl>
<dd>Append this user to groups specified by the <i>GROUPS</i> parameter. The <i>GROUPS</i> parameter is a comma separated list of group names.</dl>
<p> <code>-r</code>,<code>&#8211;remove-group</code> <i>GROUPS</i></p>
<dl>
<dd>Remove this user from groups specified by the <i>GROUPS</i> parameter.</dl>
<p> <code>-l</code>,<code>&#8211;lock</code></p>
<dl>
<dd>Lock the user account. The user won&#8217;t be able to log in.</dl>
<p> <code>-u</code>,<code>&#8211;unlock</code></p>
<dl>
<dd>Unlock the user account.</dl>
<p> <code>-Z</code>,<code>&#8211;selinux-user</code> <i>SELINUX_USER</i></p>
<dl>
<dd>The SELinux user for the user&#8217;s login.</dl>
<p> <code>&#8211;addattr</code> <i>ATTR_NAME_VAL</i></p>
<dl>
<dd>Add an attribute/value pair. The format is attrname=value.</dl>
<p> <code>&#8211;setattr</code> <i>ATTR_NAME_VAL</i></p>
<dl>
<dd>Set an attribute to a name/value pair. The format is attrname=value. For multi-valued attributes, the command replaces the values already present</dl>
<p> <code>&#8211;delattr</code> <i>ATTR_NAME_VAL</i></p>
<dl>
<dd>Delete an attribute/value pair. The format is attrname=value.</dl>
<p> <code>-?</code>,<code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<h2>The Local Domain</h2>
<p>In order to function correctly, a domain with &#8220;id_provider=local&#8221; must be created and the SSSD must be running. </p>
<p> The administrator might want to use the SSSD local users instead of traditional UNIX users in cases where the group nesting (see <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8)) is needed. The local users are also useful for testing and development of the SSSD without having to deploy a full remote server. The <code>sss_user*</code> and <code>sss_group*</code> tools use a local LDB storage to store users and groups.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="http://fedorahosted.org/sssd">http://fedorahosted.org/sssd</a></code></p>
