---
title: "apt-extracttemplates(1)"
name: "apt-extracttemplates"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apt-extracttemplates/"
description: "apt-extracttemplates – Utility to extract debconf config and templates from Debian packages"
---

<h2 class="name">NAME</h2>
<p> apt-extracttemplates &#8211; Utility to extract <code>debconf</code> config and templates from Debian packages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>apt-extracttemplates</code> [<code>-t=</code><i>temporary_directory</i>] <i>filename</i>&#8230; {-v | &#8211;version} {-h | &#8211;help}</dl>
<h2>DESCRIPTION</h2>
<p> <code>apt-extracttemplates</code></p>
<dd>will take one or more Debian package files as input and write out (to a temporary directory) all associated config scripts and template files. For each passed in package that contains config scripts and templates, one line of output will be generated in the format: </p>
<p> package version template-file config-script </p>
<p> template-file and config-script are written to the temporary directory specified by the <code>-t</code> or <code>&#8211;tempdir</code> (APT::ExtractTemplates::TempDir) directory, with filenames of the form package.template.XXXXXX and package.config.XXXXXX</p>
<h2>OPTIONS</h2>
<p> All command line options may be set using the configuration file, the descriptions indicate the configuration option to set. For boolean options you can override the config file by using something like <code>-f-</code>,<code>&#8211;no-f</code>, <code>-f=no</code> or several other variations. </p>
<p> <code>-t</code>, <code>&#8211;tempdir</code></p>
<dl>
<dt>
<dd> Temporary directory in which to write extracted <code>debconf</code> template files and config scripts. Configuration Item: APT::ExtractTemplates::TempDir</dl>
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
<p> <code>apt-extracttemplates</code> returns zero on normal operation, decimal 100 on error.</p>
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
