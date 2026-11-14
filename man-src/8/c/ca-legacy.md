---
title: "ca-legacy(8)"
name: "ca-legacy"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ca-legacy/"
description: "ca-legacy – Manage the system configuration for legacy CA certificates"
---

<p>ca-legacy &#8211; Manage the system configuration for legacy CA certificates</p>
<h2>Synopsis</h2>
<p><code>ca-legacy</code> [<i>COMMAND</i>]</p>
<h2>Description</h2>
<p><a href="/docs/linux/man/8-ca-legacy/">ca-legacy</a>(8) is used to include or exclude a set of legacy Certificate Authority (CA) certificates in the system&#8217;s list of trusted CA certificates. </p>
<p> The list of CA certificates and trust flags included in the ca-certificates package are based on the decisions made by Mozilla.org according to the Mozilla CA policy. </p>
<p> Occasionally, removal or distrust decisions made by Mozilla.org might be incompatible with the requirements or limitations of some applications that also use the CA certificates list in the Linux environment. </p>
<p> The ca-certificates package might keep some CA certificates included and trusted by default, as long as it is seen necessary by the maintainers, despite the fact that they have been removed by Mozilla. These certificates are called legacy CA certificates. </p>
<p> The general requirements to keep legacy CA certificates included and trusted might change over time, for example if functional limitations of software packages have been resolved. Future versions of the ca-certificates package might reduce the set of legacy CA certificates that are included and trusted by default. </p>
<p> The <a href="/docs/linux/man/8-ca-legacy/">ca-legacy</a>(8) command can be used to override the default behaviour. </p>
<p> The mechanisms to individually trust or distrust CA certificates as described in <a href="/docs/linux/man/8-update-ca-trust/">update-ca-trust</a>(8) still apply.</p>
<h2>Commands</h2>
<p><code>check</code></p>
<dl>
<dd>The current configuration will be shown.</dl>
<p> <code>default</code></p>
<dl>
<dd>Configure the system to use the default configuration, as recommended by the package maintainers.</dl>
<p> <code>disable</code></p>
<dl>
<dd>Configure the system to explicitly disable legacy CA certificates. Using this configuration, the system will use the set of included and trusted CA certificates as released by Mozilla.</dl>
<p> <code>install</code></p>
<dl>
<dd>The configuration file will be read and the system configuration will be set accordingly. This command is executed automatically during upgrades of the ca-certificates package.</dl>
<h2>Files</h2>
<p>/etc/pki/ca-trust/ca-legacy.conf</p>
<dl>
<dd>A configuration file that will be used and modified by the ca-legacy command. The contents of the configuration file will be read on package upgrades.</dl>
<h2>Author</h2>
<p>Written by Kai Engert.</p>
