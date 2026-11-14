---
title: "xcfinfo(1)"
name: "xcfinfo"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xcfinfo/"
description: "xcfinfo – display information about GIMP xcf files"
---

<h2>NAME</h2>
<p> xcfinfo &#8211; display information about GIMP xcf files</p>
<h2>SYNOPSIS</h2>
<p> <code>xcfinfo</code> [ <i>options</i> ] <i>filename</i></p>
<h2>DESCRIPTION</h2>
<p> <code>xcfinfo</code> is a command-line tool that displays information about the contents of image files in the XCF format used by <code><a href="/docs/linux/man/1-gimp/">gimp</a></code>(1), particularly about the layers in the image.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print an option summery to standard output and exit with a return code of 0.</p>
<dt><code>-j</code>, <code>&#8211;bzip</code></p>
<dd> Equivalent to <code>-Z bzcat</code>. Default if the filename ends with <code>bz2</code>.</p>
<dt><code>-u</code>, <code>&#8211;utf8</code></p>
<dd> Use the raw UTF-8 representation from the XCF file to compare and display layer names. Ordinarily, layer names will be converted to the character set of the current locale.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print progress messages about the conversion to standard error.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version numer of <code>xcftools</code> to standard output and exit with a return code of 0.</p>
<dt><code>-z</code>, <code>&#8211;gzip</code></p>
<dd> Equivalent to <code>-Z zcat</code>. Default if the filename ends with <code>gz</code>.</p>
<dt><code>-Z</code> <i>command</i>, <code>&#8211;unpack</code> <i>command</i></p>
<dd> Specify a command that the input file is filtered through before being interpreted as an XCF file. The command is invoked as <i>command filename</i> and must produce output to its standard output. Note that it is not possible to specify arguments as part of <i>command</i>. An uncompressor is selected automatically if the filename ends with <code>gz</code> or <code>bz2</code>; to suppress this, use <code>-Z cat</code> (which is implemented without actually starting a <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1) process).</dl>
<h2>OUTPUT</h2>
<p> Information about the image is displayed on standard output in a fixed format. The first line contains general information about the XCF file:</p>
<dl>
<dt>&#8211;</p>
<dd> The file format version</p>
<dt>&#8211;</p>
<dd> The canvas size</p>
<dt>&#8211;</p>
<dd> The image mode (color, grayscale, or indexed)</p>
<dt>&#8211;</p>
<dd> The numer of layers</p>
<dt>&#8211;</p>
<dd> The internal compression algorithm Following this line there is a line for each layer:</p>
<dt>1)</p>
<dd> The character <code>+</code> if the layer is visible and <code>&#8211;</code> if it is not</p>
<dt>2)</p>
<dd> The size and offset of the layer</p>
<dt>3)</p>
<dd> The pixel format of the layer, including whether the layer has an alpha channel.</p>
<dt>4)</p>
<dd> The layer mode, as well as the opacity if not 100%, and <code>/mask</code> if the layer has an active layer mask.</p>
<dt>5)</p>
<dd> The name of the layer.</dl>
<h2>EXIT STATUS</h2>
<p> The exit status of <code>xcfinfo</code> is</p>
<dl>
<dt>0</p>
<dd> Success</p>
<dt>20</p>
<dd> Problems parsing the command line.</p>
<dt>21</p>
<dd> The specified XCF file does not exist or cannot be read.</p>
<dt>123</p>
<dd> The XCF file contains presumably valid features that <code>xcftools</code> does not support. (As of this writing there is no known way of getting the Gimp to write an XCF file that will provoke this return. Please notify the author if you discover one).</p>
<dt>125</p>
<dd> The XCF file is malformed.</p>
<dt>126</p>
<dd> An uncompression program could not be executed, or terminated abnormally.</p>
<dt>127</p>
<dd> Unexpected I/O error, internal errors, or other &quot;this can&#8217;t happen&quot; situations. If an uncompression program returns an error exit status, this will be returned from <code>xcfinfo</code> too.</dl>
<h2>AUTHOR</h2>
<p> <code>xcfinfo</code> was written by Henning Makholm &lt;henning [at] makholm.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xcf2pnm/">xcf2pnm</a></code>(1), <code><a href="/docs/linux/man/1-xcf2png/">xcf2png</a></code>(1) </p>
<h2>Index</h2>
