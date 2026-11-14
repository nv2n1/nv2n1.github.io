---
title: "rstconv(1)"
name: "rstconv"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rstconv/"
description: "rstconv – The Free Pascal resource string converter tool."
---

<h2>NAME</h2>
<p> rstconv &#8211; The Free Pascal resource string converter tool. </p>
<h2>SYNOPSIS</h2>
<p> <code>rstconv [options] -o outfile</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>rstconv</code> reads a resource string file ( <i>.rst</i> ) that was produced by the Free Pascal compiler and outputs a file that can be used by an internationalization tool (currently only GNU <i>gettext</i> is supported) for internationalizing your application. </p>
<h2>USAGE</h2>
<p> <code>rstconv</code> has one required option: <code>-o</code><i> outfile</i> to specify the output file name. If no input file is specified, then standard input is assumed. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i> format</i></p>
<dd> Specify the output file format. Currently only the following format is supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>po</i></p>
<dd> emit a <i>.po</i> file for use with GNU <i>gettext</i> , which converts it to a .mo file, that can be read with the <i>gettext</i> unit.</dl>
</dl>
<dt><code>-h (or &#8211;help)</code></p>
<dd> outputs a short help message.</p>
<dt><code>-i</code><i> infile</i></p>
<dd> Specifies the input file name. If omitted, then standard input is assumed.</p>
<dt><code>-o</code><i> outfile</i></p>
<dd> (Required) specify the output file name.</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-gettext/">gettext</a></code>(1) <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) </p>
</dl>
<h2>Index</h2>
