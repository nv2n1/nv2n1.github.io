---
title: "shinken-discovery(8)"
name: "shinken-discovery"
section: "8"
letter: "s"
url: "/docs/linux/man/8-shinken-discovery/"
description: "shinken-discovery – Shinken discovery command"
---

<p>shinken-discovery &#8211; Shinken discovery command</p>
<h2>Synopsis</h2>
<p>shinken-discovery [-w] [-c CONFIGFILE] [-o OUTPUT_PATH] [-r RUNNER[,RUNNER,&#8230;]] [-mMACRO* [MACRO &#8230;]]</p>
<h2>Description</h2>
<p>Shinken discovery command </p>
<p> There are two discovery modules included: * Standard network discovery which uses the nmap tool * VMware discovery which uses the check_esx3.pl script and a vcenter installation. </p>
<p> It is best to do the whole discovery in one pass because one module can use data from the other.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8212; version</code></p>
<dd>Show the version and exit</p>
<dl>
<dd></dl>
<dt><code>-c </code>CONFIGFILE, &#8211;cfg-input CONFIGGILE</p>
<dd>Discovery configuration file</p>
<dl>
<dd></dl>
<dt><code>-o </code>OUTPUT_PATH, &#8211;dir-output OUTPUT_PATH</p>
<dd>Directory output for results</p>
<dl>
<dd></dl>
<dt><code>-w, &#8211;overright</code></p>
<dd>Allow overwriting existing files (disabled by default)</p>
<dl>
<dd></dl>
<dt><code>-r </code>RUNNERS</p>
<dd>Comma-separated list of discovery runner modules to use</p>
<dl>
<dd></dl>
<dt><code>-m </code>MACROS</p>
<dd>List of macros to pass to discovery runner modules. Must be the last argument. Ex: NMAPTARGETS=192.168.0.0/24</p>
<dl>
<dd></dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Print detailed help screen.</p>
<dl>
<dd></dl>
</dl>
<h2>Authors</h2>
<p>David Hannequin. Arthur Gautier. Michael Leinartas.</p>
