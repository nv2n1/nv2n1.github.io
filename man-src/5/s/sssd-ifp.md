---
title: "sssd-ifp(5)"
name: "sssd-ifp"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sssd-ifp/"
description: "sssd-ifp – SSSD InfoPipe responder"
---

<p>sssd-ifp &#8211; SSSD InfoPipe responder</p>
<h2>Description</h2>
<p>This manual page describes the configuration of the InfoPipe responder for <code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8). For a detailed syntax reference, refer to the &#8220;FILE FORMAT&#8221; section of the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page. </p>
<p> The InfoPipe responder provides a public D-Bus interface accessible over the system bus. The interface allows the user to query information about remote users and groups over the system bus.</p>
<h2>Configuration Options</h2>
<p>These options can be used to configure the InfoPipe responder. </p>
<p> allowed_uids (string)</p>
<dl>
<dd>Specifies the comma-separated list of UID values or user names that are allowed to access the InfoPipe responder. User names are resolved to UIDs at startup. </p>
<p> Default: 0 (only the root user is allowed to access the InfoPipe responder) </p>
<p> Please note that although the UID 0 is used as the default it will be overwritten with this option. If you still want to allow the root user to access the InfoPipe responder, which would be the typical case, you have to add 0 to the list of allowed UIDs as well.</dl>
<p> user_attributes (string)</p>
<dl>
<dd>Specifies the comma-separated list of white or blacklisted attributes. </p>
<p> By default, the InfoPipe responder only allows the default set of POSIX attributes to be requested. This set is the same as returned by <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3) and includes: </p>
<p> name</p>
<dl>
<dd>user&#8217;s login name</dl>
<p> uidNumber</p>
<dl>
<dd>user ID</dl>
<p> gidNumber</p>
<dl>
<dd>primary group ID</dl>
<p> gecos</p>
<dl>
<dd>user information, typically full name</dl>
<p> homeDirectory</p>
<dl>
<dd>home directory</dl>
<p> loginShell</p>
<dl>
<dd>user shell</dl>
<p> It is possible to add another attribute to this set by using &#8220;+attr_name&#8221; or explicitly remove an attribute using &#8220;-attr_name&#8221;. For example, to allow &#8220;telephoneNumber&#8221; but deny &#8220;loginShell&#8221;, you would use the following configuration: </p>
<dl>
<dd>
<pre>user_attributes = +telephoneNumber, -loginShell</pre>
</dl>
<p> Default: not set. Only the default set of POSIX attributes is allowed.</dl>
<p> wildcart_limit (integer)</p>
<dl>
<dd>Specifies an upper limit on the number of entries that are downloaded during a wildcard lookup that overrides caller-supplied limit. </p>
<p> Default: 0 (let the caller set an upper limit)</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="http://fedorahosted.org/sssd">http://fedorahosted.org/sssd</a></code></p>
