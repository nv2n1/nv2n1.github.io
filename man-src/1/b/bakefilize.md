---
title: "bakefilize(1)"
name: "bakefilize"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bakefilize/"
description: "bakefilize – prepare Bakefile project for use with Autoconf"
---

<h2 class="name">NAME</h2>
<p> bakefilize &#8211; prepare Bakefile project for use with Autoconf </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bakefilize</code> [<code>&#8211;copy</code>] [<code>&#8211;dry-run</code>] [<code>&#8211;force</code>] [<code>&#8211;verbose</code>] [<code>&#8211;help</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>For the &quot;autoconf&quot; format, Bakefile creates Makefile.in files that depend on the availability of common pieces of a GNU build system. (config.guess, install-sh, etc.) These tools are part of Automake, which can copy these files into a project&#8217;s directory during processing. <code>bakefilize</code> effectively replaces the <code>automake &#8211;add-missing</code> feature. </p>
<p> It is standard practice in Autoconf-based projects to provide a &quot;bootstrap&quot; script (commonly called either <code>bootstrap</code> or <code>autogen.sh</code>) to run commands like <code>autoconf</code> with the proper flags and in the proper order. You should run <code>bakefilize</code> in that script, at some point before the <code>configure</code> script runs.</p>
<h2>COMMAND LINE OPTIONS</h2>
<p> <code>-c</code>, <code>&#8211;copy</code></p>
<dl>
<dt>
<dd> Copy the files from the Automake directory, rather than the default behavior of making symbolic links.</dl>
<p> <code>-n</code>, <code>&#8211;dry-run</code></p>
<dl>
<dt>
<dd> Only show the commands that would be executed.</dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Replace all existing files, instead of only adding missing files.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Show debugging messages.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display usage information for <code>bakefilize</code></dl>
<h2>Index</h2>
