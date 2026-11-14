---
title: "podofoimg2pdf(1)"
name: "podofoimg2pdf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podofoimg2pdf/"
description: "podofoimg2pdf – Convert images to PDF files"
---

<h2 class="name">NAME</h2>
<p> podofoimg2pdf &#8211; Convert images to PDF files</p>
<h2>SYNOPSIS</h2>
<p> <code>podofoimg2pdf</code> [output.pdf] [-useimgsize] [image1 image2 image3 &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>podofoimg2pdf</code> is one of the command line tools from the PoDoFo library that provide several useful operations to work with PDF files. This tool will combine any number of images into a single PDF. This is useful for creating a document from scanned images. Large pages will be scaled to fit the page and images smaller than the defined page size will be centered. </p>
<p> Supported image formats:</p>
<dl>
<dt>
<dd> JPEG<br />
 PNG<br />
 TIFF</dl>
<h2>OPTIONS</h2>
<p> <code>-useimgsize</code></p>
<dl>
<dt>
<dd> Use the image size as page size instead of A4</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-podofobox/">podofobox</a></code>(1), <code><a href="/docs/linux/man/1-podofocolor/">podofocolor</a></code>(1), <code><a href="/docs/linux/man/1-podofocountpages/">podofocountpages</a></code>(1), <code><a href="/docs/linux/man/1-podofocrop/">podofocrop</a></code>(1), <code><a href="/docs/linux/man/1-podofoencrypt/">podofoencrypt</a></code>(1), <code><a href="/docs/linux/man/1-podofogc/">podofogc</a></code>(1), <code><a href="/docs/linux/man/1-podofoimgextract/">podofoimgextract</a></code>(1), <code><a href="/docs/linux/man/1-podofoincrementalupdates/">podofoincrementalupdates</a></code>(1), <code><a href="/docs/linux/man/1-podofoimpose/">podofoimpose</a></code>(1), <code><a href="/docs/linux/man/1-podofomerge/">podofomerge</a></code>(1), <code><a href="/docs/linux/man/1-podofopages/">podofopages</a></code>(1), <code><a href="/docs/linux/man/1-podofopdfinfo/">podofopdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-podofotxt2pdf/">podofotxt2pdf</a></code>(1), <code><a href="/docs/linux/man/1-podofotxtextract/">podofotxtextract</a></code>(1), <code><a href="/docs/linux/man/1-podofouncompress/">podofouncompress</a></code>(1), <code><a href="/docs/linux/man/1-podofoxmp/">podofoxmp</a></code>(1) </p>
<h2>AUTHORS</h2>
<p> PoDoFo is written by Dominik Seichter &lt;domseichter [at] web.de&gt; and others. </p>
<p> This manual page was written by Oleksandr Moskalenko &lt;malex [at] debian.org&gt; for the Debian Project (but may be used by others). </p>
<h2>Index</h2>
