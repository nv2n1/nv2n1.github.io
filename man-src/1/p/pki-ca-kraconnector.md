---
title: "pki-ca-kraconnector(1)"
name: "pki-ca-kraconnector"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-ca-kraconnector/"
description: "pki-ca-kraconnector – Command-Line Interface for managing CA-KRA connectors."
---

<h2 class="name">NAME</h2>
<p> pki-ca-kraconnector &#8211; Command-Line Interface for managing CA-KRA connectors.</p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options] ca - kraconnector pki[CLI options] ca - kraconnector - show pki[CLI options] ca - kraconnector - add-- input - file&lt;input file&gt; | --host&lt;KRA host&gt; --port&lt;KRA port&gt;
                                                                                                                                                           pki[CLI options] ca -
                                                                                                                                                       kraconnector - del-- host&lt;KRA host&gt; --port&lt;KRA port&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki-ca-kraconnector</code> commands provide command-line interfaces to manage CA-KRA connectors. This command should be applied against CAs only. </p>
<p> When keys are archived, the CA communicates with the KRA through authenticated persistent connections called Connectors. Because the CA initiates the communication, the connector configuration is performed on the CA only. A Connector is automatically configured on the issuing CA whenever a KRA is set up by <code>pkispawn</code>. </p>
<p> A CA may have only one KRA connector. This connector can be configured to talk to multiple KRAs (for high availability) only if the KRAs are clones. </p>
<p> <code>pki</code> [CLI options] <code>ca-kraconnector</code></p>
<dl>
<dt>
<dd> This command is to list available KRA connector commands.</dl>
<p> <code>pki</code> [CLI options] <code>ca-kraconnector-show</code></p>
<dl>
<dt>
<dd> This command is to view the configuration settings for the CA-KRA connector configured on the CA. These details can be redirected to a file, modified as needed, and used as the input file for the <code>ca-kraconnector-add</code> command.</dl>
<p> <code>pki</code> [CLI options] <code>ca-kraconnector-add</code> &#8211;input-file &lt;input_file&gt;</p>
<dl>
<dt>
<dd> This command is to configure the CA-KRA connector on the CA subsystem. The input file is an XML document as provided by the <code>ca-kraconnector-show</code> command. </p>
<p> A CA-KRA connector can only be created from an input file only if a connector does not already exist. If one already exists, it should be removed first.</dl>
<p> <code>pki</code> [CLI options] <code>ca-kraconnector-add</code> &#8211;host &lt;KRA host&gt; &#8211;port &lt;KRA Port&gt;</p>
<dl>
<dt>
<dd> This command is to add a host to an existing CA-KRA connector.</dl>
<p> <code>pki</code> [CLI options] <code>ca-kraconnector-del</code> &#8211;host &lt;KRA Host&gt; &#8211;port &lt;KRA Port&gt;</p>
<dl>
<dt>
<dd> This command is to delete a host from the CA-KRA connector on a CA. If the last KRA host is removed, the connector configuration is removed from the CA.</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available CA-KRA connector commands, type <code>pki ca-kraconnector</code>. To view each command&#8217;s usage, type <code> pki ca-kraconnector-&lt;command&gt; &#8211;help</code>. </p>
<p> All CA-KRA connector commands must be executed as the CA administrator. </p>
<p> To retrieve the CA-KRA connector configuration from the CA: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-kraconnector-show</code> </p>
<p> One of the most common use cases for these commands is to add a KRA clone to an existing CA-KRA connector for high availability. This can be done using the pki ca-kraconnector-add command as shown: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-kraconnector-add &#8211;host kra2.example.com &#8211;port 8443</code> </p>
<p> To delete a KRA clone from the connector: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-kraconnector-del &#8211;host kra2.example.com &#8211;port 8443</code> </p>
<h2>AUTHOR</h2>
<p> Ade Lee &lt;alee [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2016 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>Index</h2>
