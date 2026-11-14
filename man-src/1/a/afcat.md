---
title: "afcat(1)"
name: "afcat"
section: "1"
letter: "a"
url: "/docs/linux/man/1-afcat/"
description: "afcat – Output contents of an image file to stdout."
---

<h2>NAME</h2>
<p> afcat &#8211; Output contents of an image file to stdout.</p>
<h2>SYNOPSIS</h2>
<p> <code>afcat [options] </code> <i>image [images] </i></p>
<h2>DESCRIPTION</h2>
<p> <code>affcat</code> outputs the contents of an image file to stdout. Image files that are not raw but are recognized by AFF will be output in raw format. Missing pages will not be padded, but the fact that they are missing will be noted on STDERR. </p>
<p> The options are as follows:</p>
<dl>
<dt>-s name</p>
<dd> Output the named segment, instead of the image data. This is a way to output metadata.</p>
<dt>-p nnn</p>
<dd> Just output page number <code>nnn</code></p>
<dt>-S nnn</p>
<dd> Just output data sector number <code>nnn.</code> Sector #0 is the first sector.</p>
<dt>-q</p>
<dd> Quiet mode. Don&#8217;t print to STDERR if a page is skipped because it is not present.</p>
<dt>-n</p>
<dd> Noisy mode. Tell when pages are skipped.</p>
<dt>-l</p>
<dd> List all the segment names, rather than outputing data.</p>
<dt>-L</p>
<dd> List Long. Prints segment names, lengths, and args.</p>
<dt>-d</p>
<dd> Debug mode. Print the page numbers to stderr as data goes to stdout.</p>
<dt>-b</p>
<dd> Output BADFALG for bad blocks (default is to output NULLs).</p>
<dt>-v</p>
<dd> Just print the version number and exit.</p>
<dt>-r offset:count</p>
<dd> Seek to the given byte offset and output count characters in each file; may be repeated.</dl>
<h2>HISTORY</h2>
<p> <code>afcat</code> first appeared in <code>AFFLIB</code> v1.00.</p>
<h2>AUTHOR</h2>
<p> Simson Garfinkel &lt;simsong [at] acm.org&gt; </p>
<h2>Index</h2>
