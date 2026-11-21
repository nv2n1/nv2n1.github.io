---

title: "odvicopy(1)"
name: "odvicopy"
section: "1"
letter: "o"
url: "/docs/linux/man/1-odvicopy/"
description: "dvicopy, odvicopy – produce modified copy of DVI file"
---

<p> <code>dvicopy</code> [<i>options</i>] [<i>infile</i>[<i></i><code>.dvi</code>] [<i>outfile</i>[<i></i><code>.dvi</code>]]]</p>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> <code>dvicopy</code> reads a DVI file, expands any references to virtual fonts to base fonts, and writes the resulting DVI file. Thus you can use virtual fonts even if your DVI processor does not support them, by passing the documents through <code>dvicopy</code> first.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-magnification=</code><i>NUMBER</i></dt>
<dd> Override existing magnification with <i>NUMBER</i>.</dd></dl>
<dl>
<dt><code>-max-pages=</code><i>NUMBER</i></dt>
<dd> Process <i>NUMBER</i> pages; default one million.</dd></dl>
<dl>
<dt><code>-page-start=</code><i>PAGE-SPEC</i></dt>
<dd> Start at <i>PAGE-SPEC</i>, for example `2&#8242; or `5.*.-2&#8242;.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dviselect/">dviselect</a></code>(1), <code><a href="/docs/linux/man/1-dvitype/">dvitype</a></code>(1).</p>
<h2>AUTHORS</h2>
<p> Peter Breitenlohner wrote the program. Klaus Guntermann originally ported it to Unix. </p>
