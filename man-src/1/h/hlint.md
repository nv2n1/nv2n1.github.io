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
<dt><code>-?</code> <code>&#8211;help</code></p>
<dd> Display help message</p>
<dt><code>-v</code> <code>&#8211;version</code></p>
<dd> Display version information</p>
<dt><code>-r[file]</code> <code>&#8211;report</code>[=<i>file</i>]</p>
<dd> Generate a report in HTML</p>
<dt><code>-h</code> <i>file</i> <code>&#8211;hint</code>=<i>file</i></p>
<dd> Hint/ignore file to use</p>
<dt><code>-c</code> <code>&#8211;color</code>, <code>&#8211;colour</code></p>
<dd> Color the output (requires ANSI terminal)</p>
<dt><code>-i</code> <i>message</i> <code>&#8211;ignore</code>=<i>message</i></p>
<dd> Ignore a particular hint</p>
<dt><code>-s</code> <code>&#8211;show</code></p>
<dd> Show all ignored ideas</p>
<dt><code>-t</code> <code>&#8211;test</code></p>
<dd> Run in test mode</dl>
<h2>EXAMPLE</h2>
<p> &quot;To check all Haskell files in &#8216;src&#8217; and generate a report type:&quot;</p>
<dl>
<dt>
<dd> hlint src <code>&#8211;report</code></dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>HLint</code> is available in <i>/usr/share/doc/hlint/hlint.html. </i></p>
<h2>AUTHOR</h2>
<p> This manual page was written by Joachim Breitner &lt;nomeata [at] debian.org&gt; for the Debian system (but may be used by others). </p>
<h2>Index</h2>
