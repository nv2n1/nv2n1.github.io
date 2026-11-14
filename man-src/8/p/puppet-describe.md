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
<dt>&#8211;help</p>
<dd>Print this help text</p>
<dt>&#8211;providers</p>
<dd>Describe providers in detail for each type</p>
<dt>&#8211;list</p>
<dd>List all types</p>
<dt>&#8211;meta</p>
<dd>List all metaparameters</p>
<dt>&#8211;short</p>
<dd>List only parameters without detail</dl>
<h2>Example</h2>
<pre>$ puppet describe --list
$ puppet describe file --providers
$ puppet describe user -s -m</pre>
<h2>Author</h2>
<p>David Lutterkort</p>
<h2>Copyright</h2>
<p>Copyright (c) 2011 Puppet Labs, LLC Licensed under the Apache 2.0 License</p>
