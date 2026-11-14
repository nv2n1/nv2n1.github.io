---
title: "ipsec_readwriteconf(8)"
name: "ipsec_readwriteconf"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_readwriteconf/"
description: "ipsec_readwriteconf – validate and output an Libreswan IPsec configuration file"
---

<p>ipsec_readwriteconf &#8211; validate and output an Libreswan IPsec configuration file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec readwriteconf </code> [&#8211;config&nbsp;<wbr><code>file</code>] [&#8211;debug] [&#8211;verbose] [&#8211;rootdir&nbsp;<wbr><code>dir</code>]</dl>
<h2>Description</h2>
<dd>This program reads the given ipsec.conf style configuration file, interpreting the also= options, and outputs an equivalent ipsec.conf file. The purpose of this program is to validate the input processing. This can also be used to validate the syntax of a configuration file. </p>
<p> The options &#8211;debug and &#8211;verbose are currently synonyms. </p>
<p> The &#8211;rootdir option changes the programs idea of what &quot;/&quot; is when processing include directives. This is useful when validating a configuration which is not installed on a target system yet.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
