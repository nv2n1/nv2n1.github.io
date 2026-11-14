---
title: "sss_useradd(8)"
name: "sss_useradd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sss_useradd/"
description: "sss_useradd – create a new user"
---

<p>sss_useradd &#8211; create a new user</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>sss_useradd</code> [<i>options</i>] <i>LOGIN</i></dl>
<h2>Description</h2>
<p><code>sss_useradd</code></p>
<dd>creates a new user account using the values specified on the command line plus the default values from the system.</p>
<h2>Options</h2>
<p><code>-u</code>,<code>&#8211;uid</code> <i>UID</i></p>
<dl>
<dd>Set the UID of the user to the value of <i>UID</i>. If not given, it is chosen automatically.</dl>
<p> <code>-c</code>,<code>&#8211;gecos</code> <i>COMMENT</i></p>
<dl>
<dd>Any text string describing the user. Often used as the field for the user&#8217;s full name.</dl>
<p> <code>-h</code>,<code>&#8211;home</code> <i>HOME_DIR</i></p>
<dl>
<dd>The home directory of the user account. The default is to append the <i>LOGIN</i> name to /home and use that as the home directory. The base that is prepended before <i>LOGIN</i> is tunable with &#8220;user_defaults/baseDirectory&#8221; setting in sssd.conf.</dl>
<p> <code>-s</code>,<code>&#8211;shell</code> <i>SHELL</i></p>
<dl>
<dd>The user&#8217;s login shell. The default is currently /bin/bash. The default can be changed with &#8220;user_defaults/defaultShell&#8221; setting in sssd.conf.</dl>
<p> <code>-G</code>,<code>&#8211;groups</code> <i>GROUPS</i></p>
<dl>
<dd>A list of existing groups this user is also a member of.</dl>
<p> <code>-m</code>,<code>&#8211;create-home</code></p>
<dl>
<dd>Create the user&#8217;s home directory if it does not exist. The files and directories contained in the skeleton directory (which can be defined with the -k option or in the config file) will be copied to the home directory.</dl>
<p> <code>-M</code>,<code>&#8211;no-create-home</code></p>
<dl>
<dd>Do not create the user&#8217;s home directory. Overrides configuration settings.</dl>
<p> <code>-k</code>,<code>&#8211;skel</code> <i>SKELDIR</i></p>
<dl>
<dd>The skeleton directory, which contains files and directories to be copied in the user&#8217;s home directory, when the home directory is created by <code>sss_useradd</code>. </p>
<p> Special files (block devices, character devices, named pipes and unix sockets) will not be copied. </p>
<p> This option is only valid if the <code>-m</code> (or <code>&#8211;create-home</code>) option is specified, or creation of home directories is set to TRUE in the configuration.</dl>
<p> <code>-Z</code>,<code>&#8211;selinux-user</code> <i>SELINUX_USER</i></p>
<dl>
<dd>The SELinux user for the user&#8217;s login. If not specified, the system default will be used.</dl>
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
