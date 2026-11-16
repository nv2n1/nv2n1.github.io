---
title: "pdftopng(1)"
name: "pdftopng"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdftopng/"
description: "pdftopng – Portable Document Format (PDF) to Portable Network Graphics (PNG) converter (version 3.04)"
---

<h2>NAME</h2>
<p> pdftopng &#8211; Portable Document Format (PDF) to Portable Network Graphics (PNG) converter (version 3.04)</p>
<h2>SYNOPSIS</h2>
<p> <code>pdftopng</code> [options] <i>PDF-file PNG-root</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Pdftopng</code> converts Portable Document Format (PDF) files to color, grayscale, or monochrome image files in Portable Network Graphics (PNG) format. </p>
<p> Pdftopng reads the PDF file, <i>PDF-file</i>, and writes one PNG file for each page, <i>PNG-root</i>&#8211;<i>nnnnnn</i>.png, where <i>nnnnnn</i> is the page number. If <i>PNG-root</i> is &#8216;-&#8216;, the image is sent to stdout (this is probably only useful when converting a single page).</p>
<h2>CONFIGURATION FILE</h2>
<p> Pdftopng reads a configuration file at startup. It first tries to find the user&#8217;s private config file, ~/.xpdfrc. If that doesn&#8217;t exist, it looks for a system-wide config file, typically /usr/local/etc/xpdfrc (but this location can be changed when pdftopng is built). See the <code><a href="/docs/linux/man/5-xpdfrc/">xpdfrc</a></code>(5) man page for details.</p>
<h2>OPTIONS</h2>
<p> Many of the following options can be set with configuration file commands. These are listed in square brackets with the description of the corresponding command line option.</p>
<dl>
<dt><code>-f</code><i> number</i></dt>
<dd> Specifies the first page to convert.</dd>
<dt><code>-l</code><i> number</i></dt>
<dd> Specifies the last page to convert.</dd>
<dt><code>-r</code><i> number</i></dt>
<dd> Specifies the resolution, in DPI. The default is 150 DPI.</dd>
<dt><code>-mono</code></dt>
<dd> Generate a monochrome image (instead of a color image).</dd>
<dt><code>-gray</code></dt>
<dd> Generate a grayscale image (instead of a color image).</dd>
<dt><code>-freetype</code><i> yes | no</i></dt>
<dd> Enable or disable FreeType (a TrueType / Type 1 font rasterizer). This defaults to &quot;yes&quot;. [config file: <code>enableFreeType</code>]</dd>
<dt><code>-aa</code><i> yes | no</i></dt>
<dd> Enable or disable font anti-aliasing. This defaults to &quot;yes&quot;. [config file: <code>antialias</code>]</dd>
<dt><code>-aaVector</code><i> yes | no</i></dt>
<dd> Enable or disable vector anti-aliasing. This defaults to &quot;yes&quot;. [config file: <code>vectorAntialias</code>]</dd>
<dt><code>-opw</code><i> password</i></dt>
<dd> Specify the owner password for the PDF file. Providing this will bypass all security restrictions.</dd>
<dt><code>-upw</code><i> password</i></dt>
<dd> Specify the user password for the PDF file.</dd>
<dt><code>-q</code></dt>
<dd> Don&#8217;t print any messages or errors. [config file: <code>errQuiet</code>]</dd>
<dt><code>-v</code></dt>
<dd> Print copyright and version information.</dd>
<dt><code>-h</code></dt>
<dd> Print usage information. (<code>-help</code> and <code>&#8211;help</code> are equivalent.)</dd></dl>
<h2>EXIT CODES</h2>
<p> The Xpdf tools use the following exit codes:</p>
<dl>
<dt>0</dt>
<dd> No error.</dd>
<dt>1</dt>
<dd> Error opening a PDF file.</dd>
<dt>2</dt>
<dd> Error opening an output file.</dd>
<dt>3</dt>
<dd> Error related to PDF permissions.</dd>
<dt>99</dt>
<dd> Other error.</dd></dl>
<h2>AUTHOR</h2>
<p> The pdftopng software and documentation are copyright 1996-2014 Glyph &amp; Cog, LLC.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xpdf/">xpdf</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/5-xpdfrc/">xpdfrc</a></code>(5)<br />
 <code><a rel="nofollow" href="http://www.foolabs.com/xpdf/">http://www.foolabs.com/xpdf/</a></code> </p>
<h2>Index</h2>
