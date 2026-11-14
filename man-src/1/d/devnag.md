---
title: "devnag(1)"
name: "devnag"
section: "1"
letter: "d"
url: "/docs/linux/man/1-devnag/"
description: "devnag – Devanagari for TeX preprocessor"
---

<h2 class="name">NAME</h2>
<p> devnag &#8211; Devanagari for TeX preprocessor </p>
<h2>SYNOPSIS</h2>
<p> <code>devnag in[.dn] [out[.tex]]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>devnag</code> is a preprocessor that reads transliterated Devanagari input delimited by \dn and converts it into a form with which TeX is familiar. </p>
<p> The preprocessor handles the details of character placement such as the alignment of vowel diacritics and consonant ligatures. The rest of the layout, however, must be managed by the user. </p>
<p> For specification of the format please see the documentation accompanying the package.</p>
<h2>OPTIONS</h2>
<dl>
<dt>in[.dn] out[.tex]</p>
<dd> The default file extension for an input file is .dn and for an output file .tex. The output filename is optional. If an output filename is not specified, the preprocessor will name it after the input file.</p>
<dt><code>-v</code></p>
<dd> report devnag version</dl>
<h2>AUTHORS</h2>
<p> <code>devnag</code> was written by Frans J. Velthuis and is currently maintained by Zdenek Wagner as part of TeX Live &lt;tex-live [at] tug.org&gt;. </p>
<p> This manpage was written by Norbert Preining for Debian/GNU Linux and may be used, modified and/or distributed freely by anyone. </p>
<h2>Index</h2>
