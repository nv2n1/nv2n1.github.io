---
title: "umap(1)"
name: "umap"
section: "1"
letter: "u"
url: "/docs/linux/man/1-umap/"
---

<h2 class="name">NAME</h2>
 

 umap - map between different character sets 

<h2>SYNOPSIS</h2>

 <pre>
 umap [options] &lt;before&gt;:&lt;after&gt;
</pre>

<h2>DESCRIPTION</h2>

 The <i>umap</i> script acts as a filter between different encodings and character sets. 

 The following options are recognized:
<dl>
<dt>--list [charset]
<dd> Without argument list all character sets recognized. With a specified character set list the mapping between this set and Unicode.
<dt>--strict
<dd> Do the stict mapping between the character sets. The default is to not translate unmapped character. With <i>--stict</i> we will remove unmapped characters or use the default specified with <i>--def8</i> or <i>--def16</i>.
<dt>--def8=&lt;charcode&gt;
<dd> Set the default 8-bit code for unmapped chars.
<dt>--def16=&lt;charcode&gt;
<dd> Set the default 16-bit code for unmapped chars.
<dt>--verbose
<dd> Generate more verbose output.
<dt>--version
<dd> Print the version number of this program and quit.
<dt>--help
<dd> Print the usage message.</dl>

<h2>SEE ALSO</h2>

 Unicode::String, Unicode::Map8, <i><a HREF="/docs/linux/man/1-recode/">recode</a></i>(1)

<h2>COPYRIGHT</h2>

 Copyright 1998 Gisle Aas. 

 This is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

<h2>Index</h2>


