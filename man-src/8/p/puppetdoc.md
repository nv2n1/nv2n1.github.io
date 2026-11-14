---
title: "puppetdoc(8)"
name: "puppetdoc"
section: "8"
letter: "p"
url: "/docs/linux/man/8-puppetdoc/"
description: "–"
---

<p>&nbsp;<wbr>&#8211;&nbsp;<wbr></p>
<h2>Synopsis</h2>
<p>Generate a reference for all Puppet types. Largely meant for internal Puppet Labs use.</p>
<h2>Usage</h2>
<dl>
<dt><code>puppetdoc [-a|&#8211;all] [-h|&#8211;help] [-o|&#8211;outputdir &lt;rdoc outputdir&gt;] [-m|&#8211;mode &lt;text|pdf|markdown|trac|rdoc&gt;]</code></p>
<dd>[-r|&#8211;reference &lt;[type]|configuration|..&gt;] [manifest-file]</dl>
<h2>Description</h2>
<p>If mode is not aqrdocaq, then this command generates a restructured-text document describing all installed Puppet types or all allowable arguments to puppet executables. It is largely meant for internal use and is used to generate the reference document available on the Puppet Labs web site. </p>
<p> In aqrdocaq mode, this command generates an html RDoc hierarchy describing the manifests that are in aqmanifestdiraq and aqmodulepathaq configuration directives. The generated documentation directory is doc by default but can be changed with the aqoutputdiraq option. </p>
<p> If the command is started with aqmanifest-fileaq command-line arguments, puppetdoc generate a single manifest documentation that is output on stdout.</p>
<h2>Options</h2>
<dl>
<dt><code>all: Output the docs for all of the reference types. In aqrdocaq</code></p>
<dd>modes, this also outputs documentation for all resources </p>
<p> help: Print this help message</p>
<dt><code>outputdir: Specifies the directory where to output the rdoc</code></p>
<dd>documentation in aqrdocaq mode.</p>
<dt><code>mode: Determine the output mode. Valid modes are aqtextaq, aqtracaq,</code></p>
<dd>aqpdfaq, aqmarkdownaq and aqrdocaq. The aqpdfaq and aqmarkdownaq modes create PDF or Markdown formatted files in the /tmp directory. Note that aqtracaq mode only works on Puppet Labs servers. The default mode is aqtextaq. In aqrdocaq mode you must provide aqmanifests-pathaq</p>
<dt><code>reference: Build a particular reference. Get a list of references by</code></p>
<dd>running +puppetdoc &#8211;list+.</dl>
<h2>Example</h2>
<p>$ puppetdoc -r type &gt; /tmp/type_reference.rst </p>
<p> or </p>
<p> $ puppetdoc &#8211;outputdir /tmp/rdoc &#8211;mode rdoc /path/to/manifests </p>
<p> or </p>
<p> $ puppetdoc /etc/puppet/manifests/site.pp </p>
<p> or </p>
<p> $ puppetdoc -m markdown -r configuration</p>
<h2>Author</h2>
<p>Luke Kanies</p>
<h2>Copyright</h2>
<p>Copyright (c) 2005-2007 Puppet Labs, LLC Licensed under the GNU Public License</p>
