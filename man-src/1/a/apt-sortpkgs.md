---
title: "apt-sortpkgs(1)"
name: "apt-sortpkgs"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apt-sortpkgs/"
description: "apt-sortpkgs – Utility to sort package index files"
---

<h2 class="name">NAME</h2>
<p> apt-sortpkgs &#8211; Utility to sort package index files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>apt-sortpkgs</code> [<code>-s</code>] [<code>-o=</code><i>config_string</i>] [<code>-c=</code><i>config_file</i>] <i>filename</i>&#8230; {-v | &#8211;version} {-h | &#8211;help}</dl>
<h2>DESCRIPTION</h2>
<p> <code>apt-sortpkgs</code></p>
<dd>will take an index file (source index or package index) and sort the records so that they are ordered by the package name. It will also sort the internal fields of each record according to the internal sorting rules. </p>
<p> All output is sent to standard output; the input must be a seekable file.</p>
<h2>OPTIONS</h2>
<p> All command line options may be set using the configuration file, the descriptions indicate the configuration option to set. For boolean options you can override the config file by using something like <code>-f-</code>,<code>&#8211;no-f</code>, <code>-f=no</code> or several other variations. </p>
<p> <code>-s</code>, <code>&#8211;source</code></p>
<dl>
<dt>
<dd> Use source index field ordering. Configuration Item: APT::SortPkgs::Source.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show a short usage summary.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show the program version.</dl>
<p> <code>-c</code>, <code>&#8211;config-file</code></p>
<dl>
<dt>
<dd> Configuration File; Specify a configuration file to use. The program will read the default configuration file and then this configuration file. If configuration settings need to be set before the default configuration files are parsed specify a file with the <code>APT_CONFIG</code> environment variable. See <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) for syntax information.</dl>
<p> <code>-o</code>, <code>&#8211;option</code></p>
<dl>
<dt>
<dd> Set a Configuration Option; This will set an arbitrary configuration option. The syntax is <code>-o Foo::Bar=bar</code>. <code>-o</code> and <code>&#8211;option</code> can be used multiple times to set different options.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5)</p>
<h2>DIAGNOSTICS</h2>
<p> <code>apt-sortpkgs</code> returns zero on normal operation, decimal 100 on error.</p>
<h2>BUGS</h2>
<p> m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[1]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>AUTHORS</h2>
<p> <code>Jason Gunthorpe</code></p>
<dl>
<dt>
<dd></dl>
<p> <code>APT team</code></p>
<dl>
<dt>
<dd></dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> APT bug page</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://bugs.debian.org/src:apt">http://bugs.debian.org/src:apt</a></dl>
</dl>
<h2>Index</h2>
