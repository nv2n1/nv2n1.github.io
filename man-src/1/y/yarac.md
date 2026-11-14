---
title: "yarac(1)"
name: "yarac"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yarac/"
description: "yarac – compile rules to yara"
---

<h2>NAME</h2>
<p> <code>yarac </code>&#8211; compile rules to yara</p>
<h2>SYNOPSIS</h2>
<pre><code>
yarac[OPTION]...[RULE_FILE]... OUTPUT_FILE
</code></pre>
<h2>DESCRIPTION</h2>
<p> To invoke YARA you will need two things: a file with the rules you want to use (either in source code or compiled form) and the target to be scanned. The target can be a file, a folder, or a process. </p>
<p> Rule files can be passed directly in source code form, or can be previously compiled with the <code>yarac</code> tool. You may prefer to use your rules in compiled form if you are going to invoke YARA multiple times with the same rules. This way you’ll save time, because for YARA is faster to load compiled rules than compiling the same rules over and over again. </p>
<p> The rules will be applied to the target specified as the last argument to YARA, if it’s a path to a directory all the files contained in it will be scanned.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code> &lt;identifier&gt;=&lt;value&gt;</p>
<dd> define external variable.</p>
<dt><code>-w</code></p>
<dd> disable warnings.</p>
<dt><code>-v</code></p>
<dd> show version information.</dl>
<h2>EXAMPLE</h2>
<p> The <code>-d</code> is used to define external variables. For example: </p>
<p> <code>-d</code> flag=true </p>
<p> <code>-d</code> beast=666 </p>
<p> <code>-d</code> name=&quot;James Bond&quot;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-yara/">yara</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>yarac</code> was written by Victor M. Alvarez &lt;vmalvarez [at] virustotal.com&gt;. This manual page was written by Joao Eriberto Mota Filho &lt;eriberto [at] eriberto.pro.br&gt; for the Debian project (but may be used by others). </p>
<h2>Index</h2>
