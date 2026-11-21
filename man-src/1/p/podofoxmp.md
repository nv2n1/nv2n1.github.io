---

title: "podofoxmp(1)"
name: "podofoxmp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podofoxmp/"
description: "podofoxmp – Modify or extract XMP information from a PDF file"
---

<p> podofoxmp &#8211; Modify or extract XMP information from a PDF file</p>
<h2>SYNOPSIS</h2>
<p> <code>podofoxmp</code> [inputfile] [xmpfile outputfile] </p>
<h2>DESCRIPTION</h2>
<p> <code>podofoxmp</code> is one of the command line tools from the PoDoFo library that provide several useful operations to work with PDF files. It can extract or modify XMP information in a PDF file. </p>
<h2>OPTIONS</h2>
<p> <code>[inputfile]</code></p>
<dl>
<dt>
</dt><dd>
<p> Input PDF file. This is the only option needed to extract the XMP information from a PDF file.</dd></dl>
<p> <code>[xmpfile]</code></p>
<dl>
<dt>
</dt><dd>
<p> Optional file that provides PDF XMP structure. It must be used in conjuction with an [outputfile].</dd></dl>
<p> <code>[outputfile]</code></p>
<dl>
<dt>
</dt><dd>
<p> Output PDF file. It is only used in conjuction with an [xmpfile].</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-podofobox/">podofobox</a></code>(1), <code>podofocolor</code>(1), <code><a href="/docs/linux/man/1-podofocountpages/">podofocountpages</a></code>(1), <code><a href="/docs/linux/man/1-podofocrop/">podofocrop</a></code>(1), <code><a href="/docs/linux/man/1-podofoencrypt/">podofoencrypt</a></code>(1), <code>podofogc</code>(1), <code><a href="/docs/linux/man/1-podofoimg2pdf/">podofoimg2pdf</a></code>(1), <code><a href="/docs/linux/man/1-podofoimgextract/">podofoimgextract</a></code>(1), <code><a href="/docs/linux/man/1-podofoimpose/">podofoimpose</a></code>(1), <code><a href="/docs/linux/man/1-podofoincrementalupdates/">podofoincrementalupdates</a></code>(1), <code><a href="/docs/linux/man/1-podofomerge/">podofomerge</a></code>(1), <code><a href="/docs/linux/man/1-podofopages/">podofopages</a></code>(1), <code><a href="/docs/linux/man/1-podofopdfinfo/">podofopdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-podofotxt2pdf/">podofotxt2pdf</a></code>(1), <code><a href="/docs/linux/man/1-podofotxtextract/">podofotxtextract</a></code>(1), <code><a href="/docs/linux/man/1-podofouncompress/">podofouncompress</a></code>(1) </p>
<h2>AUTHORS</h2>
<p> PoDoFo is written by Dominik Seichter &lt;domseichter [at] web.de&gt; and others. </p>
<p> This manual page was written by Oleksandr Moskalenko &lt;malex [at] debian.org&gt; for the Debian Project (but may be used by others). </p>
