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
<dt><code>&#8211;skip-version-check</code></dt>
<dd> Skip version check. WARNING: this option may break your system</dd>
<dt><code>&#8211;force</code></dt>
<dd> Force upgrade (alias for &#8211;skip-version-check)</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show IPA version</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show help message and exit</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Print debugging information</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Output only errors</dd>
<dt><code>&#8211;log-file=FILE</code></dt>
<dd> Log to given file</dd>
</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the command was successful </p>
<p> 1 if an error occurred </p>
<h2>Index</h2>
