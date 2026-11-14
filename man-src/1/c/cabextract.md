---
title: "cabextract(1)"
name: "cabextract"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cabextract/"
description: "cabextract – program to extract files from Microsoft cabinet (.cab) archives"
---

<h2 class="name">NAME</h2>
<p> cabextract &#8211; program to extract files from Microsoft cabinet (.cab) archives </p>
<h2>SYNOPSIS</h2>
<p> <code>cabextract</code> [<code>-d</code><i>dir</i><code>]</code> [<code>-f</code>] [<code>-F</code><i>pattern</i><code>]</code> [<code>-h</code>] [<code>-l</code>] [<code>-L</code>] [<code>-p</code>] [<code>-q</code>] [<code>-s</code>] [<code>-t</code>] [<code>-v</code>] <i> cabinet files &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>cabextract</code> is a program that un-archives files in the Microsoft cabinet file format (.cab) or any binary file which contains an embedded cabinet file (frequently found in .exe files). </p>
<p> <code>cabextract</code> will extract all files from all cabinet files specified on the command line. </p>
<p> To extract a multi-part cabinet consisting of several files, only the <i>first</i> cabinet file needs to be given as an argument to <code>cabextract</code> as it will automatically look for the remaining files. To prevent <code>cabextract</code> from extracting cabinet files you did not specify, use the <code>-s</code> option.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-d </code><i>dir</i></p>
<dd> Extracts all files into the directory <i>dir</i>.</p>
<dt><code>-f</code></p>
<dd> When testing or extracting cabinet files, corrupted MSZIP blocks will be ignored. A warning will be printed if a corrupted MSZIP block is encountered.</p>
<dt><code>-F </code><i>pattern</i></p>
<dd> Only files with names that match the shell pattern <i>pattern</i> shall be listed, tested or extracted. On non-GNU systems, this match may be case-sensitive.</p>
<dt><code>-h</code></p>
<dd> Prints a page of help and exits.</p>
<dt><code>-l</code></p>
<dd> Lists the contents of the given cabinet files, rather than extracting them.</p>
<dt><code>-L</code></p>
<dd> When extracting cabinet files, makes each extracted file&#8217;s name lowercase.</p>
<dt><code>-p</code></p>
<dd> Files shall be extracted to standard output.</p>
<dt><code>-q</code></p>
<dd> When extracting cabinet files, suppresses all messages except errors and warnings.</p>
<dt><code>-s</code></p>
<dd> When testing, listing or extracting cabinets which span multiple files, only cabinet files given on the command line shall be used.</p>
<dt><code>-t</code></p>
<dd> Tests the integrity of the cabinet. Files are decompressed, but not written to disk or standard output. If the file successfully decompresses, the MD5 checksum of the file is printed.</p>
<dt><code>-v</code></p>
<dd> If given alone on the command line, prints the version of <code>cabextract</code> and exits. Given with a list of cabinet files, it will list the contents of the cabinet files.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Stuart Caie &lt;kyzer [at] 4u.net&gt;, based on the one written by Eric Sharkey &lt;sharkey [at] debian.org&gt;, for the Debian GNU/Linux system.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lcab/">lcab</a></code>(1) </p>
<h2>Index</h2>
