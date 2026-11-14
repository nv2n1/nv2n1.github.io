---
title: "fiwalk(1)"
name: "fiwalk"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fiwalk/"
description: "fiwalk – print the filesystem statistics and exit"
---

<h2 class="name">NAME</h2>
<p> <code>fiwalk </code>&#8211; print the filesystem statistics and exit </p>
<h2>SYNOPSIS</h2>
<pre>
 <code>fiwalk</code> [<i>options</i>] <i>iso-name</i>
</pre>
<h2>DESCRIPTION</h2>
<p> <code>fiwalk</code> is a program that processes a disk image using the SleuthKit library and outputs its results in Digital Forensics XML, the Attribute Relationship File Format (ARFF) format used by the Weka Datamining Toolkit, or an easy-to-read textual format. </p>
<p> This application uses SleuthKit to generate a report of all of the files and orphaned inodes found in a disk image. It can optionally compute the MD5 of any objects, save those objects into a directory, or both.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> config.txt</p>
<dd> read config.txt for metadata extraction tools</p>
<dt><code>-C</code> nn</p>
<dd> only process nn files, then do a clean exit</dl>
<p> Include/exclude parameters; may be repeated:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-n</code> pattern</p>
<dd> only match files for which the filename matches the pattern. Example: <code>-n</code> .jpeg <code>-n</code> .jpg will find all JPEG files. Case is ignored. Will not match orphan files.</dl>
</dl>
<p> Ways to make this program run faster:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-I</code></p>
<dd> ignore NTFS system files</p>
<dt><code>-g</code></p>
<dd> just report the file objects &#8211; don&#8217;t get the data</p>
<dt><code>-O</code></p>
<dd> only walk allocated files</p>
<dt><code>-b</code></p>
<dd> do not report byte runs if data not accessed</p>
<dt><code>-z</code></p>
<dd> do not calculate MD5 or SHA1 values</p>
<dt><code>-Gnn</code></p>
<dd> Only process the contents of files smaller than nn gigabytes (default 2). Use <code>-G0</code> to remove space restrictions.</dl>
</dl>
<p> Ways to make this program run slower:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-M</code></p>
<dd> Report MD5 for each file (default on)</p>
<dt><code>-1</code></p>
<dd> Report SHA1 for each file (default on)</p>
<dt><code>-f</code></p>
<dd> Report the output of the &#8216;file&#8217; command for each</dl>
</dl>
<p> Output <i>options</i>: <code>-m</code> = Output in SleuthKit &#8216;Body file&#8217; format</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-A</code>&lt;file&gt;</p>
<dd> ARFF output to &lt;file&gt;</p>
<dt><code>-X</code>&lt;file&gt;</p>
<dd> XML output to a &lt;file&gt; (full DTD)</p>
<dt><code>-X0</code></p>
<dd> Write output to filename.xml</p>
<dt><code>-Z</code></p>
<dd> zap (erase) the output file</p>
<dt><code>-x</code></p>
<dd> XML output to stdout (no DTD)</p>
<dt><code>-T</code>&lt;file&gt;</p>
<dd> Walkfile output to &lt;file&gt;</p>
<dt><code>-a</code> &lt;audit.txt&gt;</p>
<dd> Read the scalpel audit.txt file</dl>
</dl>
<p> Misc:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-d</code></p>
<dd> debug this program</p>
<dt><code>-v</code></p>
<dd> Enable SleuthKit verbose flag</dl>
</dl>
<h2>AUTHOR</h2>
<p> The Sleuth Kit was written by Brian Carrier &lt;carrier [at] sleuthkit.org&gt;. </p>
<p> This manual page was written by Joao Eriberto Mota Filho &lt;eriberto [at] debian.org&gt; for the Debian project (but may be used by others). </p>
<h2>Index</h2>
