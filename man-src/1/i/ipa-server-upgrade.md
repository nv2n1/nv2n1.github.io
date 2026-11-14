---
title: "ipa-server-upgrade(1)"
name: "ipa-server-upgrade"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-server-upgrade/"
description: "ipa-server-upgrade – upgrade IPA server"
---

<h2>NAME</h2>
<p> ipa-server-upgrade &#8211; upgrade IPA server</p>
<h2>SYNOPSIS</h2>
<p> ipa-server-upgrade [options]</p>
<h2>DESCRIPTION</h2>
<p> ipa-server-upgrade is used to upgrade IPA server when the IPA packages are being updated. It is not intended to be executed by end-users. </p>
<p> ipa-server-upgrade will: </p>
<p>&nbsp;<wbr>*&nbsp;<wbr>update LDAP schema<br />
&nbsp;<wbr>*&nbsp;<wbr>process all files with the extension .update in&nbsp;<wbr>/usr/share/ipa/updates&nbsp;<wbr>(including update plugins).<br />
&nbsp;<wbr>*&nbsp;<wbr>upgrade local configurations of IPA services </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;skip-version-check</code></p>
<dd> Skip version check. WARNING: this option may break your system</p>
<dt><code>&#8211;force</code></p>
<dd> Force upgrade (alias for &#8211;skip-version-check)</p>
<dt><code>&#8211;version</code></p>
<dd> Show IPA version</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help message and exit</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print debugging information</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Output only errors</p>
<dt><code>&#8211;log-file=FILE</code></p>
<dd> Log to given file</p>
<dt>
<dd></dl>
<h2>EXIT STATUS</h2>
<p> 0 if the command was successful </p>
<p> 1 if an error occurred </p>
<h2>Index</h2>
