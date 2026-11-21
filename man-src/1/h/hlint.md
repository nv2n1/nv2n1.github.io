---
title: "hlint(1)"
name: "hlint"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hlint/"
description: "HLint – haskell source code suggestions"
---

<h2>NAME</h2>
<p> HLint &#8211; haskell source code suggestions</p>
<h2>SYNOPSIS</h2>
<p> <code>hlint</code> [<i>files/directories</i>] [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> <i>HLint</i> is a tool for suggesting possible improvements to Haskell code. These suggestions include ideas such as using alternative functions, simplifying code and spotting redundancies. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code> <code>&#8211;help</code></dt>
<dd> Display help message</dd>
<dt><code>-v</code> <code>&#8211;version</code></dt>
<dd> Display version information</dd>
<dt><code>-r[file]</code> <code>&#8211;report</code>[=<i>file</i>]</dt>
<dd> Generate a report in HTML</dd>
<dt><code>-h</code> <i>file</i> <code>&#8211;hint</code>=<i>file</i></dt>
<dd> Hint/ignore file to use</dd>
<dt><code>-c</code> <code>&#8211;color</code>, <code>&#8211;colour</code></dt>
<dd> Color the output (requires ANSI terminal)</dd>
<dt><code>-i</code> <i>message</i> <code>&#8211;ignore</code>=<i>message</i></dt>
<dd> Ignore a particular hint</dd>
<dt><code>-s</code> <code>&#8211;show</code></dt>
<dd> Show all ignored ideas</dd>
<dt><code>-t</code> <code>&#8211;test</code></dt>
<dd> Run in test mode</dd></dl>
<h2>EXAMPLE</h2>
<p> &quot;To check all Haskell files in &#8216;src&#8217; and generate a report type:&quot;</p>
<dl>
<dt>
</dt><dd> hlint src <code>&#8211;report</code></dd></dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>HLint</code> is available in <i>/usr/share/doc/hlint/hlint.html. </i></p>
<h2>AUTHOR</h2>
<p> This manual page was written by Joachim Breitner &lt;nomeata [at] debian.org&gt; for the Debian system (but may be used by others). </p>
