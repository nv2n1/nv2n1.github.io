---
title: "resgen(1)"
name: "resgen"
section: "1"
letter: "r"
url: "/docs/linux/man/1-resgen/"
description: "resgen, resgen2 – Mono/CLI Resource Generator"
---

<h2>NAME</h2>
<p> resgen, resgen2 &#8211; Mono/CLI Resource Generator</p>
<h2>SYNOPSIS</h2>
<p> <code>resgen source.ext [dest.ext] </code> </p>
<p> <code>resgen /compile source.ext[,dest.resources] [&#8230;]</code> </p>
<p> <code>resgen2 </code></p>
<h2>DESCRIPTION</h2>
<p> Convert a resource file from one format to another. </p>
<p> The currently supported formats are text, resources, resx and po.</p>
<dl>
<dt><i>.txt, .text</i></p>
<dd>
<p> Used to process text files, the format of the text file is of the form: </p>
<pre>
        key=value
</pre>
<p> The value argument can contain special characters as long as they are escaped. The escape sequences currently supported are 
, , 	, \ (to get the escape sequence itself) and with resgen2 unicode escape sequences are supported with the 
