---
title: "sss_obfuscate(8)"
name: "sss_obfuscate"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sss_obfuscate/"
description: "sss_obfuscate – obfuscate a clear text password"
---

<p>sss_obfuscate &#8211; obfuscate a clear text password</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>sss_obfuscate</code> [<i>options</i>] <i>[PASSWORD]</i></dl>
<h2>Description</h2>
<p><code>sss_obfuscate</code></p>
<dd>converts a given password into human-unreadable format and places it into appropriate domain section of the SSSD config file. </p>
<p> The cleartext password is read from standard input or entered interactively. The obfuscated password is put into &#8220;ldap_default_authtok&#8221; parameter of a given SSSD domain and the &#8220;ldap_default_authtok_type&#8221; parameter is set to &#8220;obfuscated_password&#8221;. Refer to <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5) for more details on these parameters. </p>
<p> Please note that obfuscating the password provides <i>no real security benefit</i> as it is still possible for an attacker to reverse-engineer the password back. Using better authentication mechanisms such as client side certificates or GSSAPI is <i>strongly</i> advised.</p>
<h2>Options</h2>
<p><code>-h</code>,<code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-s</code>,<code>&#8211;stdin</code></p>
<dl>
<dd>The password to obfuscate will be read from standard input.</dl>
<p> <code>-d</code>,<code>&#8211;domain</code> <i>DOMAIN</i></p>
<dl>
<dd>The SSSD domain to use the password in. The default name is &#8220;default&#8221;.</dl>
<p> <code>-f</code>,<code>&#8211;file</code> <i>FILE</i></p>
<dl>
<dd>Read the config file specified by the positional parameter. </p>
<p> Default: /etc/sssd/sssd.conf</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="http://fedorahosted.org/sssd">http://fedorahosted.org/sssd</a></code></p>
