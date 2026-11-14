---
title: "facter(8)"
name: "facter"
section: "8"
letter: "f"
url: "/docs/linux/man/8-facter/"
description: "facter – Gather system information"
---

<p><code>facter</code> &#8211; Gather system information</p>
<h2>Synopsis</h2>
<p>Collect and display facts about the system.</p>
<h2>Usage</h2>
<pre>facter [-h|--help] [-t|--timing] [-d|--debug] [-p|--puppet] [-v|--version]
 [-y|--yaml] [-j|--json] [--plaintext] [--external-dir DIR] [--no-external-dir]
 [fact] [fact] [...]</pre>
<h2>Description</h2>
<p>Collect and display facts about the current system. The library behind Facter is easy to expand, making Facter an easy way to collect information about a system from within the shell or within Ruby. </p>
<p> If no facts are specifically asked for, then all facts will be returned.</p>
<h2>Example</h2>
<p>Display all facts:</p>
<dl>
<dd>
<pre>$ facter
architecture =&gt; amd64
blockdevices =&gt; sda,sr0
domain =&gt; example.com
fqdn =&gt; puppet.example.com
hardwaremodel =&gt; x86_64
[...]</pre>
<dd></dl>
<p> Display a single fact:</p>
<dl>
<dd>
<pre>$ facter kernel
Linux</pre>
<dd></dl>
<p> Format facts as JSON:</p>
<dl>
<dd>
<pre>$ facter --json architecture kernel hardwaremodel
{
 &quot;architecture&quot;: &quot;amd64&quot;,
 &quot;kernel&quot;: &quot;Linux&quot;,
 &quot;hardwaremodel&quot;: &quot;x86_64&quot;
}</pre>
<dd></dl>
<h2>Author</h2>
<p>Luke Kanies</p>
<h2>Copyright</h2>
<p>Copyright (c) 2011-2014 Puppet Labs, Inc Licensed under the Apache 2.0 license</p>
<h2>Options</h2>
<pre>-y, --yaml Emit facts in YAML format.
-j, --json Emit facts in JSON format.
 --plaintext Emit facts in plaintext format.
 --trace Enable backtraces.
 --external-dir DIR The directory to use for external facts.
 --no-external-dir Turn off external facts.
-d, --debug Enable debugging.
-t, --timing Enable timing.
-p, --puppet Load the Puppet libraries, thus allowing Facter to load Puppet-specific facts.
-v, --version Print the version and exit.
-h, --help Print this help message.</pre>
