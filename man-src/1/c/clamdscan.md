---
title: "clamdscan(1)"
name: "clamdscan"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clamdscan/"
description: "clamdscan – scan files and directories for viruses using Clam AntiVirus Daemon"
---

<h2>NAME</h2>
<p> clamdscan &#8211; scan files and directories for viruses using Clam AntiVirus Daemon</p>
<h2>SYNOPSIS</h2>
<p> clamdscan [options] [file/directory]</p>
<h2>DESCRIPTION</h2>
<p> clamdscan is a clamd client which may be used as a clamscan replacement. It accepts all the options implemented in clamscan but most of them will be ignored because its scanning abilities only depend on clamd.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display help information and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print version number and exit.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Be verbose.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Be quiet &#8211; only output error messages.</p>
<dt><code>&#8211;stdout</code></p>
<dd> Write all messages (except for libclamav output) to the standard output (stdout).</p>
<dt><code>&#8211;config-file=FILE</code></p>
<dd> Read clamd settings from FILE.</p>
<dt><code>-l FILE, &#8211;log=FILE</code></p>
<dd> Save the scan report to FILE.</p>
<dt><code>-f FILE, &#8211;file-list=FILE</code></p>
<dd> Scan files listed line by line in FILE.</p>
<dt><code>-m, &#8211;multiscan</code></p>
<dd> In the multiscan mode clamd will attempt to scan the directory contents in parallel using available threads. This option is especially useful on multiprocessor and multi-core systems. If you pass more than one file or directory in the command line, they are put in a queue and sent to clamd individually. This means, that single files are always scanned by a single thread. Similarly, clamdscan will wait for clamd to finish a directory scan (performed in multiscan mode) before sending request to scan another directory. This option can be combined with &#8211;fdpass (see below).</p>
<dt><code>-z, &#8211;allmatch</code></p>
<dd> After a match, continue scanning within the file for additional matches.</p>
<dt><code>&#8211;remove</code></p>
<dd> Remove infected files. <code>Be careful.</code></p>
<dt><code>&#8211;move=DIRECTORY</code></p>
<dd> Move infected files into DIRECTORY.</p>
<dt><code>&#8211;no-summary</code></p>
<dd> Do not display summary at the end of scanning.</p>
<dt><code>&#8211;reload</code></p>
<dd> Request clamd to reload virus database.</p>
<dt><code>&#8211;fdpass</code></p>
<dd> Pass the file descriptor permissions to clamd. This is useful if clamd is running as a different user as it is faster than streaming the file to clamd. Only available if connected to clamd via local(unix) socket.</p>
<dt><code>&#8211;stream</code></p>
<dd> Forces file streaming to clamd. This is generally not needed as clamdscan detects automatically if streaming is required. This option only exists for debugging and testing purposes, in all other cases &#8211;fdpass is preferred.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>(0) To scan a one file:</p>
<dd>
<p> <code>clamdscan file</code></p>
<dt>(1) To scan a current working directory:</p>
<dd>
<p> <code>clamdscan</code></p>
<dt>(2) To scan all files in /home:</p>
<dd>
<p> <code>clamdscan /home</code></p>
<dt>(3) To scan a file when clamd is running as a different user:</p>
<dd>
<p> <code>clamdscan &#8211;fdpass ~/downloads</code></p>
<dt>(4) To scan from standard input:</p>
<dd>
<p> <code>clamdscan &#8211; &lt; file_to_scan</code> </p>
<p> <code>cat file_to_scan | clamdscan &#8211;</code></dl>
<h2>RETURN CODES</h2>
<p> 0 : No virus found.</p>
<dl>
<dt>1 : Virus(es) found.</p>
<dd>
<dt>2 : An error occured.</p>
<dd></dl>
<h2>CREDITS</h2>
<p> Please check the full documentation for credits.</p>
<h2>AUTHOR</h2>
<p> Tomasz Kojm &lt;tkojm [at] clamav.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-clamd/">clamd</a>(8), <a href="/docs/linux/man/5-clamd-conf/">clamd.conf</a>(5), <a href="/docs/linux/man/1-clamscan/">clamscan</a>(1) </p>
<h2>Index</h2>
