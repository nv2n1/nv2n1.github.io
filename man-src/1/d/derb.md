---
title: "derb(1)"
name: "derb"
section: "1"
letter: "d"
url: "/docs/linux/man/1-derb/"
description: "derb – disassemble a resource bundle"
---

<h2 class="name">NAME</h2>
<p> <code>derb</code> &#8211; disassemble a resource bundle </p>
<h2>SYNOPSIS</h2>
<p> <code>derb</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-V</code>, <code>&#8211;version</code> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-e</code>, <code>&#8211;encoding</code><i> encoding</i> ] [ <code>&#8211;bom</code> ] [ <code>-t</code>, <code>&#8211;truncate</code><i> </i>[ size ] ] [ <code>-s</code>, <code>&#8211;sourcedir</code><i> source</i> ] [ <code>-d</code>, <code>&#8211;destdir</code><i> destination</i> ] [ <code>-i</code>, <code>&#8211;icudatadir</code><i> directory</i> ] [ <code>-c</code>, <code>&#8211;to-stdout</code> ] <i>bundle</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>derb</code> reads the compiled resource <i>bundle</i> files passed on the command line and write them back in text form. The resulting text files have a <code>.txt</code> extension while compiled resource bundle source files typically have a <code>.res</code> extension. </p>
<p> It is customary to name the resource bundles by their locale name, i.e. to use a local identifier for the <i>bundle</i> filename, e.g. <code>ja_JP.res</code> for Japanese (Japan) data, or <code>root.res</code> for the root bundle. This is especially important for <code>derb</code> since the locale name is not accessible directly from the compiled resource bundle, and to know which locale to ask for when opening the bundle. <code>derb</code> will produce a file whose base name is the base name of the compiled resource file itself. If the <code>&#8211;to-stdout</code>, <code>-c</code> option is used, however, the text will be written on the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Print help about usage and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version of <code>derb</code> and exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display extra informative messages during execution.</p>
<dt><code>-A</code>, <code>&#8211;suppressAliases</code></p>
<dd> Don&#8217;t follow aliases when producing output.</p>
<dt><code>-e</code>, <code>&#8211;encoding</code><i> encoding</i></p>
<dd> Set the encoding used to write output files to <i>encoding</i>. The default encoding is the invariant (subset of ASCII or EBCDIC) codepage for the system (see section <code>INVARIANT CHARACTERS</code>). The choice of the encoding does not affect the data, just their representation. Characters that cannot be represented in the <i>encoding</i> will be represented using <code>
