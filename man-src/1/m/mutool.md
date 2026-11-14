---
title: "mutool(1)"
name: "mutool"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mutool/"
description: "mutool – all purpose tool for dealing with PDF files"
---

<h2 class="name">NAME</h2>
<p> mutool &#8211; all purpose tool for dealing with PDF files</p>
<h2>SYNOPSIS</h2>
<p> mutool &lt;sub-command&gt; [options] </p>
<h2>DESCRIPTION</h2>
<p> mutool is a tool based on MuPDF for dealing with PDF files in various manners. There are several sub commands available, as described below. </p>
<h2>CLEAN</h2>
<p> mutool clean [options] input.pdf [output.pdf] [pages] </p>
<p> The clean command pretty prints and rewrites the syntax of a PDF file. It can be used to repair broken files, expand compressed streams, filter out a range of pages, etc. </p>
<p> If no output file is specified, it will write the cleaned PDF to &quot;out.pdf&quot; in the current directory.</p>
<dl>
<dt><code>-p password</code></p>
<dd> Use the specified password if the file is encrypted.</p>
<dt><code>-g</code></p>
<dd> Garbage collect objects that have no references from other objects. Give the option twice to renumber all objects and compact the cross reference table. Give it three times to merge and reuse duplicate objects.</p>
<dt><code>-s</code></p>
<dd> Rewrite content streams.</p>
<dt><code>-d</code></p>
<dd> Decompress streams. This will make the output file larger, but provides easy access for reading and editing the contents with a text editor.</p>
<dt><code>-l</code></p>
<dd> Linearize output. Create a &quot;Web Optimized&quot; output file.</p>
<dt><code>-i</code></p>
<dd> Toggle decompression of image streams. Use in conjunction with -d to leave images compressed.</p>
<dt><code>-f</code></p>
<dd> Toggle decompression of font streams. Use in conjunction with -d to leave fonts compressed.</p>
<dt><code>-a</code></p>
<dd> ASCII Hex encode binary streams. Use in conjuction with -d and -i or -f to ensure that although the images and/or fonts are compressed, the resulting file can still be viewed and edited with a text editor.</p>
<dt><code>pages</code></p>
<dd> Comma separated list of page numbers and ranges to include. </p>
</dl>
<h2>EXTRACT</h2>
<p> mutool extract [options] file.pdf [object numbers] </p>
<p> The extract command can be used to extract images and font files from a PDF. If no object numbers are given on the command line, all images and fonts will be extracted.</p>
<dl>
<dt><code>-p password</code></p>
<dd> Use the specified password if the file is encrypted.</p>
<dt><code>-r</code></p>
<dd> Convert images to RGB when extracting them. </p>
</dl>
<h2>INFO</h2>
<p> mutool info [options] file.pdf [pages] </p>
<p> The info command lists the resources used on each page in a PDF file. The default is to list all resource types, but if one or more flags are given, only the flagged types will be shown.</p>
<dl>
<dt><code>-p password</code></p>
<dd> Use the specified password if the file is encrypted.</p>
<dt><code>-F</code></p>
<dd> List fonts.</p>
<dt><code>-I</code></p>
<dd> List images.</p>
<dt><code>-M</code></p>
<dd> List page dimensions.</p>
<dt><code>-S</code></p>
<dd> List shadings.</p>
<dt><code>-P</code></p>
<dd> List patterns.</p>
<dt><code>-X</code></p>
<dd> List form and postscript XObjects.</p>
<dt><code>pages</code></p>
<dd> Comma separated list of page numbers and ranges to include. </p>
</dl>
<h2>PAGES</h2>
<p> mutool pages [options] input.pdf [pages &#8230;] </p>
<p> The pages command dumps information about the size and orientation of pages within the document.</p>
<dl>
<dt><code>-p password</code></p>
<dd> Use the specified password if the file is encrypted.</p>
<dt><code>pages</code></p>
<dd> Comma separated list of page numbers and ranges to include. </p>
</dl>
<h2>POSTER</h2>
<p> mutool poster [options] input.pdf [output.pdf] </p>
<p> The poster command splits each page into tiles, and puts each tile on a page of its own. It&#8217;s useful for printing a large page onto smaller pieces of paper that can then be glued together to create a large poster.</p>
<dl>
<dt><code>-p password</code></p>
<dd> Use the specified password if the file is encrypted.</p>
<dt><code>-x factor</code></p>
<dd> Split the page into this many horizontal pieces.</p>
<dt><code>-y factor</code></p>
<dd> Split the page into this many vertical pieces.</dl>
<p> The output will have x times y number of pages for each input page.</p>
<h2>SHOW</h2>
<p> mutool show [options] file.pdf [object numbers &#8230;] </p>
<p> The show command will print the specified objects and streams to stdout. Streams are decoded and non-printable characters are represented with a period by default.</p>
<dl>
<dt><code>-p password</code></p>
<dd> Use the specified password if the file is encrypted.</p>
<dt><code>-o file</code></p>
<dd> Write output to file instead of stdout.</p>
<dt><code>-b</code></p>
<dd> Print streams as binary data and omit the object header.</p>
<dt><code>-e</code></p>
<dd> Print streams in their original encoded (or compressed) form.</dl>
<p> Specify objects by number, or use one of the following special names:</p>
<dl>
<dt><code>&#8216;xref&#8217; or &#8216;x&#8217;</code></p>
<dd> Print the cross reference table.</p>
<dt><code>&#8216;trailer&#8217; or &#8216;t&#8217;</code></p>
<dd> Print the trailer dictionary.</p>
<dt><code>&#8216;pagetree&#8217; or &#8216;p&#8217;</code></p>
<dd> List the object numbers for every page.</p>
<dt><code>&#8216;grep&#8217; or &#8216;g&#8217;</code></p>
<dd> Print all the objects in the file in a compact one-line format suitable for piping to grep.</p>
<dt><code>&#8216;outline&#8217; or &#8216;o&#8217;</code></p>
<dd> Print the outline (table of contents). </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mudraw/">mudraw</a></code>(1). <code><a href="/docs/linux/man/1-mupdf/">mupdf</a></code>(1), </p>
<h2>AUTHOR</h2>
<p> MuPDF is Copyright 2006-2015 Artifex Software, Inc. </p>
<h2>Index</h2>
