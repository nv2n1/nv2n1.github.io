---
title: "fprcp(1)"
name: "fprcp"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fprcp/"
description: "fprcp – Free Pascal windres preprocessor program."
---

<h2>NAME</h2>
<p> fprcp &#8211; Free Pascal windres preprocessor program. </p>
<h2>SYNOPSIS</h2>
<p> <code>fprcp -i file_name [-n] [-C] [-l PASCAL|C] [-p &lt;include_path&gt;] </code> </p>
<h2>DESCRIPTION</h2>
<p> <code>fprcp</code> reads a .rc file and preprocesses it, writing the result to standard output as it goes along. It replaces defined constants with their values, so <code>windres</code> can process the resulting file and create a resource. </p>
<h2>USAGE</h2>
<p> <code>fprcp</code> needs as a minimum the <code>-i filename</code> option, which is the file to process. </p>
<h2>OPTIONS</h2>
<p> fprcp has a small number of options to control its behaviour: </p>
<dl>
<dt><code>-C </code></p>
<dd> Define the symbol <i>symbol</i> before processing is started.</p>
<dt><code>-i file</code></p>
<dd> Specify the input file name. This argument is mandatory.</p>
<dt><code>-l language</code></p>
<dd> Set the programming language for include files. The <i>language</i> constant may be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>C</i></p>
<dd> The C programming language.</p>
<dt><i>PASCAL</i></p>
<dd> the Pascal programming language</dl>
</dl>
<dt><code>-n </code></p>
<dd> Do not support nested comments. By default, pascal nested comments are enabled.</p>
<dt><code>-p path</code></p>
<dd> Set the include path. This may contain several files, separated by semicolons. </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-windres/">windres</a></code>(1) </p>
</dl>
<h2>Index</h2>
