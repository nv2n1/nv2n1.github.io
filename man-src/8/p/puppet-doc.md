---
title: "puppet-doc(8)"
name: "puppet-doc"
section: "8"
letter: "p"
url: "/docs/linux/man/8-puppet-doc/"
description: "puppet-doc – Generate Puppet documentation and references"
---

<p><code>puppet-doc</code> &#8211; Generate Puppet documentation and references</p>
<h2>Synopsis</h2>
<p>Generates a reference for all Puppet types. Largely meant for internal Puppet Labs use. </p>
<p> WARNING: RDoc support is only available under Ruby 1.8.7 and earlier.</p>
<h2>Usage</h2>
<p>puppet doc [-a|&#8211;all] [-h|&#8211;help] [-o|&#8211;outputdir <i>rdoc-outputdir</i>] [-m|&#8211;mode text|pdf|rdoc] [-r|&#8211;reference <i>reference-name</i>] [&#8211;charset <i>charset</i>] [<i>manifest-file</i>]</p>
<h2>Description</h2>
<p>If mode is not &#8216;rdoc&#8217;, then this command generates a Markdown document describing all installed Puppet types or all allowable arguments to puppet executables. It is largely meant for internal use and is used to generate the reference document available on the Puppet Labs web site. </p>
<p> In &#8216;rdoc&#8217; mode, this command generates an html RDoc hierarchy describing the manifests that are in &#8216;manifestdir&#8217; and &#8216;modulepath&#8217; configuration directives. The generated documentation directory is doc by default but can be changed with the &#8216;outputdir&#8217; option. </p>
<p> If the command is run with the name of a manifest file as an argument, puppet doc will output a single manifest&#8217;s documentation on stdout. </p>
<p> WARNING: RDoc support is only available under Ruby 1.8.7 and earlier. The internal API used to support manifest documentation has changed radically in newer versions, and support is not yet available for using those versions of RDoc.</p>
<h2>Options</h2>
<dl>
<dt>&#8211;all</p>
<dd>Output the docs for all of the reference types. In &#8216;rdoc&#8217; mode, this also outputs documentation for all resources.</p>
<dt>&#8211;help</p>
<dd>Print this help message</p>
<dt>&#8211;outputdir</p>
<dd>Used only in &#8216;rdoc&#8217; mode. The directory to which the rdoc output should be written.</p>
<dt>&#8211;mode</p>
<dd>Determine the output mode. Valid modes are &#8216;text&#8217;, &#8216;pdf&#8217; and &#8216;rdoc&#8217;. The &#8216;pdf&#8217; mode creates PDF formatted files in the /tmp directory. The default mode is &#8216;text&#8217;.</p>
<dt>&#8211;reference</p>
<dd>Build a particular reference. Get a list of references by running &#8216;puppet doc &#8211;list&#8217;.</p>
<dt>&#8211;charset</p>
<dd>Used only in &#8216;rdoc&#8217; mode. It sets the charset used in the html files produced.</p>
<dt>&#8211;manifestdir</p>
<dd>Used only in &#8216;rdoc&#8217; mode. The directory to scan for stand-alone manifests. If not supplied, puppet doc will use the manifestdir from puppet.conf.</p>
<dt>&#8211;modulepath</p>
<dd>Used only in &#8216;rdoc&#8217; mode. The directory or directories to scan for modules. If not supplied, puppet doc will use the modulepath from puppet.conf.</p>
<dt>&#8211;environment</p>
<dd>Used only in &#8216;rdoc&#8217; mode. The configuration environment from which to read the modulepath and manifestdir settings, when reading said settings from puppet.conf.</dl>
<h2>Example</h2>
<pre>$ puppet doc -r type &gt; /tmp/type_reference.markdown</pre>
<p>or</p>
<dl>
<dd>
<pre>$ puppet doc --outputdir /tmp/rdoc --mode rdoc /path/to/manifests</pre>
<dd></dl>
<p> or</p>
<dl>
<dd>
<pre>$ puppet doc /etc/puppet/manifests/site.pp</pre>
<dd></dl>
<p> or</p>
<dl>
<dd>
<pre>$ puppet doc -m pdf -r configuration</pre>
<dd></dl>
<h2>Author</h2>
<p>Luke Kanies</p>
<h2>Copyright</h2>
<p>Copyright (c) 2011 Puppet Labs, LLC Licensed under the Apache 2.0 License</p>
