---
title: "ipa-kra-install(1)"
name: "ipa-kra-install"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-kra-install/"
description: "ipa-kra-install – Install a KRA on a server"
---

<h2>NAME</h2>
<p> ipa-kra-install &#8211; Install a KRA on a server</p>
<h2>SYNOPSIS</h2>
<p> ipa-kra-install [<i>OPTION</i>]&#8230; [replica_file]</p>
<h2>DESCRIPTION</h2>
<p> Adds a KRA as an IPA-managed service. This requires that the IPA server is already installed and configured, including a CA. </p>
<p> The KRA (Key Recovery Authority) is a component used to securely store secrets such as passwords, symmetric keys and private asymmetric keys. It is used as the back-end repository for the IPA Password Vault. </p>
<p> ipa-kra-install can be run without replica_file to add KRA to the existing CA. ipa-kra-install will contact the CA to determine if a KRA has already been installed on another replica, and if so, will exit indicating that a replica_file is required. </p>
<p> The replica_file is created using the ipa-replica-prepare utility. A new replica_file should be generated on the master IPA server after the KRA has been installed and configured, so that the replica_file will contain the master KRA configuration and system certificates. </p>
<p> The uninstall option can be used to remove the KRA from the local IPA server. KRA instances on other replicas are not affected. The KRA will also be removed if the entire server is removed using ipa-server-install &#8211;uninstall.</p>
<h2>OPTIONS</h2>
<p> <code>-p</code> <i>DM_PASSWORD</i>, <code>&#8211;password</code>=<i>DM_PASSWORD</i> Directory Manager (existing master) password</p>
<dl>
<dt><code>-U</code>, <code>&#8211;unattended</code></p>
<dd> An unattended installation that will never prompt for user input</p>
<dt><code>&#8211;uninstall</code></p>
<dd> Uninstall the KRA from the local IPA server.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Enable debug output when more verbose output is needed</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Output only errors</p>
<dt><code>-v</code>, <code>&#8211;log-file</code>=ILE</p>
<dd> Log to the given file</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the command was successful </p>
<p> 1 if an error occurred </p>
<h2>Index</h2>
