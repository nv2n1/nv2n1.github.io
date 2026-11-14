---
title: "sss_ssh_knownhostsproxy(1)"
name: "sss_ssh_knownhostsproxy"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sss_ssh_knownhostsproxy/"
description: "sss_ssh_knownhostsproxy – get OpenSSH host keys"
---

<h2 class="name">NAME</h2>
<p> sss_ssh_knownhostsproxy &#8211; get OpenSSH host keys </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>sss_ssh_knownhostsproxy</code> [<i>options</i>] <i>HOST</i> [<i>PROXY_COMMAND</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>sss_ssh_knownhostsproxy</code></p>
<dd>acquires SSH host public keys for host <i>HOST</i>, stores them in a custom OpenSSH known_hosts file (see the &#8220;SSH_KNOWN_HOSTS FILE FORMAT&#8221; section of <code><a href="/docs/linux/man/8-sshd/">sshd</a></code>(8) for more information) /var/lib/sss/pubconf/known_hosts and establishes the connection to the host. </p>
<p> If <i>PROXY_COMMAND</i> is specified, it is used to create the connection to the host instead of opening a socket. </p>
<p> <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) can be configured to use <code>sss_ssh_knownhostsproxy</code> for host key authentication by using the following directives for <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) configuration: </p>
<dl>
<dt>
<dd>
<pre>
ProxyCommand /usr/bin/sss_ssh_knownhostsproxy -p %p %h
GlobalKnownHostsFile /var/lib/sss/pubconf/known_hosts
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-p</code>,<code>&#8211;port</code> <i>PORT</i></p>
<dl>
<dt>
<dd> Use port <i>PORT</i> to connect to the host. By default, port 22 is used.</dl>
<p> <code>-d</code>,<code>&#8211;domain</code> <i>DOMAIN</i></p>
<dl>
<dt>
<dd> Search for host public keys in SSSD domain <i>DOMAIN</i>.</dl>
<p> <code>-?</code>,<code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help message and exit.</dl>
<h2>EXIT STATUS</h2>
<p> In case of success, an exit value of 0 is returned. Otherwise, 1 is returned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/5-sssd-secrets/">sssd-secrets</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>AUTHORS</h2>
<p> <code>The SSSD upstream &#8211; <a rel="nofollow" href="https://pagure.io/SSSD/sssd/">https://pagure.io/SSSD/sssd/</a></code> </p>
<h2>Index</h2>
