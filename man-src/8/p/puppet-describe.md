---
title: "puppet-describe(8)"
name: "puppet-describe"
section: "8"
letter: "p"
url: "/docs/linux/man/8-puppet-describe/"
description: "puppet-describe – Display help about resource types"
---

<p><code>puppet-describe</code> &#8211; Display help about resource types</p>
<h2>Synopsis</h2>
<p>Prints help about Puppet resource types, providers, and metaparameters.</p>
<h2>Usage</h2>
<p>puppet describe [-h|&#8211;help] [-s|&#8211;short] [-p|&#8211;providers] [-l|&#8211;list] [-m|&#8211;meta]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</dt>
<dd>Print this help text</dd>
<dt>&#8211;providers</dt>
<dd>Describe providers in detail for each type</dd>
<dt>&#8211;list</dt>
<dd>List all types</dd>
<dt>&#8211;meta</dt>
<dd>List all metaparameters</dd>
<dt>&#8211;short</dt>
<dd>List only parameters without detail</dd></dl>
<h2>Example</h2>
<pre>$ puppet describe --list
$ puppet describe file --providers
$ puppet describe user -s -m</pre>
<h2>Author</h2>
<p>David Lutterkort</p>
<h2>Copyright</h2>
<p>Copyright (c) 2011 Puppet Labs, LLC Licensed under the Apache 2.0 License</p>
