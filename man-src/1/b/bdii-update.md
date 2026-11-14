---
title: "bdii-update(1)"
name: "bdii-update"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bdii-update/"
description: "bdii-update – the bdii update process"
---

<h2>NAME</h2>
<p> bdii-update &#8211; the bdii update process</p>
<h2>SYNOPSIS</h2>
<p> <code>bdii-update [-d ] -c </code> <i>config-file</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>bdii-update </code> process obtains the LDIF by reading files found the <code>ldif</code> directory, running providers found in the <code>provider</code> directory and running plugins found in the <code>plugin</code><br />
&nbsp;<wbr>directory.&nbsp;<wbr> The difference between providers and plugins is that providers return complete entries and plugins provide modifications to existing entries. The process can be run either as a daemon that periodically syncronizes an LDAP database or as a command that will print the result to stdout.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-d</p>
<dd> Run as a daemon process.</p>
<dt>-c config</p>
<dd> The configuration to use.</dl>
<h2>FILES</h2>
<p> <i>/etc/bdii.conf</i></p>
<dl>
<dt>
<dd> The default configuration file.</dl>
<h2>AUTHOR</h2>
<p> Laurence Field &lt;Laurence.Field at cern dot ch&gt; </p>
<h2>Index</h2>
