---

title: "fiwalk(1)"
name: "fiwalk"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fiwalk/"
description: "fiwalk – print the filesystem statistics and exit"
---

<p> <code>fiwalk </code>&#8211; print the filesystem statistics and exit </p>
<pre>
 <code>fiwalk</code> [<i>options</i>] <i>iso-name</i>
</pre>
<p> <code>fiwalk</code> is a program that processes a disk image using the SleuthKit library and outputs its results in Digital Forensics XML, the Attribute Relationship File Format (ARFF) format used by the Weka Datamining Toolkit, or an easy-to-read textual format. </p>
<p> This application uses SleuthKit to generate a report of all of the files and orphaned inodes found in a disk image. It can optionally compute the MD5 of any objects, save those objects into a directory, or both.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> config.txt</dt>
<dd> read config.txt for metadata extraction tools</dd>
<dt><code>-C</code> nn</dt>
<dd> only process nn files, then do a clean exit</dd></dl>
<p> Include/exclude parameters; may be repeated:</p>
<dl>
<dl>
<dt><code>-n</code> pattern</dt>
<dd> only match files for which the filename matches the pattern. Example: <code>-n</code> .jpeg <code>-n</code> .jpg will find all JPEG files. Case is ignored. Will not match orphan files.</dd></dl>
</dl>
<p> Ways to make this program run faster:</p>
<dl>
<dl>
<dt><code>-I</code></dt>
<dd> ignore NTFS system files</dd>
<dt><code>-g</code></dt>
<dd> just report the file objects &#8211; don&#8217;t get the data</dd>
<dt><code>-O</code></dt>
<dd> only walk allocated files</dd>
<dt><code>-b</code></dt>
<dd> do not report byte runs if data not accessed</dd>
<dt><code>-z</code></dt>
<dd> do not calculate MD5 or SHA1 values</dd>
<dt><code>-Gnn</code></dt>
<dd> Only process the contents of files smaller than nn gigabytes (default 2). Use <code>-G0</code> to remove space restrictions.</dd></dl>
</dl>
<p> Ways to make this program run slower:</p>
<dl>
<dl>
<dt><code>-M</code></dt>
<dd> Report MD5 for each file (default on)</dd>
<dt><code>-1</code></dt>
<dd> Report SHA1 for each file (default on)</dd>
<dt><code>-f</code></dt>
<dd> Report the output of the &#8216;file&#8217; command for each</dd></dl>
</dl>
<p> Output <i>options</i>: <code>-m</code> = Output in SleuthKit &#8216;Body file&#8217; format</p>
<dl>
<dl>
<dt><code>-A</code>&lt;file&gt;</dt>
<dd> ARFF output to &lt;file&gt;</dd>
<dt><code>-X</code>&lt;file&gt;</dt>
<dd> XML output to a &lt;file&gt; (full DTD)</dd>
<dt><code>-X0</code></dt>
<dd> Write output to filename.xml</dd>
<dt><code>-Z</code></dt>
<dd> zap (erase) the output file</dd>
<dt><code>-x</code></dt>
<dd> XML output to stdout (no DTD)</dd>
<dt><code>-T</code>&lt;file&gt;</dt>
<dd> Walkfile output to &lt;file&gt;</dd>
<dt><code>-a</code> &lt;audit.txt&gt;</dt>
<dd> Read the scalpel audit.txt file</dd></dl>
</dl>
<p> Misc:</p>
<dl>
<dl>
<dt><code>-d</code></dt>
<dd> debug this program</dd>
<dt><code>-v</code></dt>
<dd> Enable SleuthKit verbose flag</dd></dl>
</dl>
<h2>AUTHOR</h2>
<p> The Sleuth Kit was written by Brian Carrier &lt;carrier [at] sleuthkit.org&gt;. </p>
<p> This manual page was written by Joao Eriberto Mota Filho &lt;eriberto [at] debian.org&gt; for the Debian project (but may be used by others). </p>
