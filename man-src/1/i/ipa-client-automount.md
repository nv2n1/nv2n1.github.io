---
title: "ipa-client-automount(1)"
name: "ipa-client-automount"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-client-automount/"
description: "ipa-client-automount – Configure automount and NFS for IPA"
---

<h2>NAME</h2>
<p> ipa-client-automount &#8211; Configure automount and NFS for IPA</p>
<h2>SYNOPSIS</h2>
<p> ipa-client-automount [<i>OPTION</i>]&#8230; &lt;location&gt;</p>
<h2>DESCRIPTION</h2>
<p> Configures automount for IPA. </p>
<p> The automount configuration consists of three files: </p>
<dl>
<dt>o</p>
<dd> /etc/nsswitch.conf</p>
<dt>o</p>
<dd> /etc/sysconfig/autofs</p>
<dt>o</p>
<dd> /etc/autofs_ldap_auth.conf </p>
<dt>By default this will use DNS discovery to attempt to determine the IPA server(s) to use. If IPA servers are discovered then the automount client will be configured to use DNS discovery.</p>
<dd>
<dt>If DNS discovery fails or a specific server is desired, use the &#8211;server option.</p>
<dd>
<dt>The default automount location is named default. To specify a different one use the &#8211;location option.</p>
<dd>
<dt>The IPA client must already be configured in order to configure automount. The IPA client is configured as part of a server installation.</p>
<dd>
<dt>There are two ways to configure automount. The default is to use sssd to manage the automount maps. Alternatively autofs can configured to bind to LDAP over GSSAPI and authenticate using the machine&#8217;s host principal.</p>
<dd>
<dt>The nsswitch automount service is configured to use either sss or ldap and files depending on whether SSSD is configured or not.</p>
<dd>
<dt>NFSv4 is also configured. The rpc.gssd and rpc.idmapd are started on clients to support Kerberos-secured mounts.</p>
<dd></dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;server</code>=<i>SERVER</i> Set the FQDN of the IPA server to connect to</p>
<dl>
<dt><code>&#8211;location</code>=<i>LOCATION</i></p>
<dd> Automount location</p>
<dt><code>-S</code>, <code>&#8211;no-sssd</code></p>
<dd> Do not configure the client to use SSSD for automount</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Print debugging information to stdout</p>
<dt><code>-U</code>, <code>&#8211;unattended</code></p>
<dd> Unattended installation. The user will not be prompted</p>
<dt><code>&#8211;uninstall</code></p>
<dd> Restore the automount configuration files </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>Files that will be always be configured:</p>
<dd>
<p> /etc/nsswitch.conf</p>
<dt>Files that will be configured when SSSD is the automount client (default):</p>
<dd>
<p> /etc/sssd/sssd.conf </p>
<dt>Files that will be configured when using the ldap automount client:</p>
<dd>
<p> /etc/sysconfig/autofs </p>
<p> /etc/autofs_ldap_auth.conf </p>
</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the installation was successful </p>
<p> 1 if an error occurred </p>
<h2>Index</h2>
