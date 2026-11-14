---
title: "podofobox(1)"
name: "podofobox"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podofobox/"
description: "podofocolor – modify colors in a PDF file."
---

<h2 class="name">NAME</h2>
<p> podofocolor &#8211; modify colors in a PDF file.</p>
<h2>SYNOPSIS</h2>
<p> <code>podofocolor</code> [converter] [inputfile] [outpufile] </p>
<h2>DESCRIPTION</h2>
<p> <code>podofocolor</code> is one of the command line tools from the PoDoFo library that provide several useful operations to work with colors in PDF files. It can parse and/or modify all colors or colorspaces in a PDF file. The modifications can be defined via C++ or a Lua script. Custom conversions like onvert all colors to grayscaleare included. Please note that only colors of vector objects on pages and in XObjects are affected. This tool does not transform colos in images at the moment. </p>
<h2>CONVERTERS</h2>
<p> [converter] can be any of</p>
<dl>
<dt>
<dd> dummy &#8211; Convert all colors to red. Just a dummy and test implementation which serves as an example for developers. grayscale &#8211; Convert all colors of vector objects in a PDF to grayscale. lua &#8211; Convert all colors based on a Lua description. A lua script has to be passed as an additional parameter.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-podofocolor/">podofocolor</a></code>(1), <code><a href="/docs/linux/man/1-podofocountpages/">podofocountpages</a></code>(1), <code><a href="/docs/linux/man/1-podofocrop/">podofocrop</a></code>(1), <code><a href="/docs/linux/man/1-podofoencrypt/">podofoencrypt</a></code>(1), <code><a href="/docs/linux/man/1-podofogc/">podofogc</a></code>(1), <code><a href="/docs/linux/man/1-podofoimg2pdf/">podofoimg2pdf</a></code>(1), <code><a href="/docs/linux/man/1-podofoimgextract/">podofoimgextract</a></code>(1), <code><a href="/docs/linux/man/1-podofoimpose/">podofoimpose</a></code>(1), <code><a href="/docs/linux/man/1-podofomerge/">podofomerge</a></code>(1), <code><a href="/docs/linux/man/1-podofoincrementalupdates/">podofoincrementalupdates</a></code>(1), <code><a href="/docs/linux/man/1-podofopages/">podofopages</a></code>(1), <code><a href="/docs/linux/man/1-podofopdfinfo/">podofopdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-podofotxt2pdf/">podofotxt2pdf</a></code>(1), <code><a href="/docs/linux/man/1-podofotxtextract/">podofotxtextract</a></code>(1), <code><a href="/docs/linux/man/1-podofouncompress/">podofouncompress</a></code>(1), <code><a href="/docs/linux/man/1-podofoxmp/">podofoxmp</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> PoDoFo is written by Dominik Seichter &lt;domseichter [at] web.de&gt; and others. </p>
<p> This manual page was written by Dominik Seichter &lt;domseichter [at] web.de&gt; for the PoDoFo Project (but may be used by others). </p>
<h2>Index</h2>
