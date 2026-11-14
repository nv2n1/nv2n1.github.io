---
title: "ccze-cssdump(1)"
name: "ccze-cssdump"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ccze-cssdump/"
description: "ccze-cssdump – Dump CCZE color setup into CSS format"
---

<h2>NAME</h2>
<p> ccze-cssdump &#8211; Dump CCZE color setup into CSS format</p>
<h2>SYNOPSIS</h2>
<p> <code>ccze-cssdump</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>ccze-cssdump</code> utility, which is a simple tool to dump the color setup of CCZE into Cascading Style Sheet format, to be used later by <code>ccze -h -o cssfile</code>.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-F, &#8211;rcfile </code><i>rcfile</i></p>
<dd> Read <i>rcfile</i> as a configuration file upon startup.</p>
<dt><code>-l, &#8211;load</code></p>
<dd> Load the default configuration files upon startup.</p>
<dt><code>&#8211;help</code></p>
<dd> Show summary of options and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show version of program.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/colorizerc</i>, <i>$HOME/.colorizerc</i></p>
<dd>
<dl>
<dt>
<dd> These files are the default configuration files for <code>colorize</code>, and are parsed by <code>ccze</code> for the sake of full compatibility.</dl>
<p> <i>/etc/cczerc</i>, <i>$HOME/.cczerc</i></p>
<dl>
<dt>
<dd> This two are the main configuration files, in which one can change the colors used by the program to his liking. See the comments in the beginning of <i>/etc/cczerc</i> for a description on the files&#8217; structure.</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ccze/">ccze</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> ccze was written by Gergely Nagy &lt;algernon [at] bonehunter.rulez.org&gt;, based on colorize by Istvan Karaszi &lt;colorize [at] spam.raszi.hu&gt;. </p>
<h2>Index</h2>
