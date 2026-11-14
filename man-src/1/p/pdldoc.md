---
title: "pdldoc(1)"
name: "pdldoc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdldoc/"
description: "pdldoc – shell interface to PDL documentation"
---

<h2 class="name">NAME</h2>
<p> pdldoc &#8211; shell interface to PDL documentation </p>
<h2>SYNOPSIS</h2>
<p> <code>pdldoc</code> &lt;text&gt;</p>
<h2>DESCRIPTION</h2>
<p> The aim of <code>pdldoc</code> is to provide the same functionality as the <tt>&quot;apropos&quot;</tt>, <tt>&quot;help&quot;</tt>, <tt>&quot;sig&quot;</tt>,</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> help</p>
<dd> print documentation about a <font SIZE="-1">PDL</font> function or module or show a <font SIZE="-1">PDL</font> manual. This is the default option.</p>
<dt><code>-a</code> apropos</p>
<dd> Regex search <font SIZE="-1">PDL</font> documentation database.</p>
<dt><code>-b</code> badinfo</p>
<dd> Information on the support for bad values provided by the function.</p>
<dt><code>-s</code> sig</p>
<dd> prints signature of <font SIZE="-1">PDL</font> function.</p>
<dt><code>-u</code> usage</p>
<dd> Prints usage information for a <font SIZE="-1">PDL</font> function.</p>
<dt>$PDL::Config{PDLDOC_IGNORE_AUTOLOADER}</p>
<dd> This <font SIZE="-1">PDL</font> configuration variable may be set in the perldl.conf file to disable runtime search for documentation in PDL::AutoLoader files.</dl>
<h2>VERSION</h2>
<p> This is pdldoc version 0.3.</p>
<h2>AUTHOR</h2>
<p> Doug Burke &lt;burke at ifa dot hawaii dot edu&gt;. Chris Marshall &lt;chm at cpan dot org&gt;. </p>
<h2>Index</h2>
