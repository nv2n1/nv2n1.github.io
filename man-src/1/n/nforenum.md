---
title: "nforenum(1)"
name: "nforenum"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nforenum/"
description: "NFORenum – A tool for checking NFO code for errors, and for beautifying that code"
---

<h2>NAME</h2>
<p> <code>NFORenum</code> &#8211; A tool for checking NFO code for errors, and for beautifying that code</p>
<h2>SYNOPSIS</h2>
<p> <code>nforenum</code> [options] [file [file2 [file3 [&#8230;]]]]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;auto-correct | -a</code></p>
<dd> Perform some rudimentary automatic correction of incorrect pseudo sprites. This may be specified twice to enable the corrections that are more likely to be incorrect. See the README for detailed information on the auto-correcter.</p>
<dt><code>&#8211;comments = </code><i>type | &#8211;</i><code>c </code><i>type</i></p>
<dd> &lt;type&gt; is one character, either /, ;, or #, and specifies the comment style that NFORenum will use. This will not change the header, because grfcodec requires that the header be commented in C++-style.</p>
<dt><code>&#8211;data [= </code><i>dir ] | &#8211;</i><code>D [ </code><i>dir</i></p>
<dd> If &lt;dir&gt; is specified, look for the .nforenum directory in &lt;dir&gt;, and create it if not found. </p>
<p> If &lt;dir&gt; is not specified, report the location of the .nforenum directory. In either case, eliminate the 5-second wait used to ensure that those not running NFORenum from a command line can see the directory-created message. </p>
<p> Default: Look for the .nforenum directory in the current directory, and then in the environment variable <code>HOME , if defined. If </code>not found attempt to create in <code>HOME , then in</code></p>
<dt><code>&#8211;force | -f</code></p>
<dd> Forces processing of files that do not look like NFO files. The default is to treat such files as if they specified a too-high info version.</p>
<dt><code>&#8211;help | -h</code></p>
<dd> Display the help message.</p>
<dt><code>&#8211;lock</code></p>
<dd> Locks the current comment command state. Commands will continue to be parsed as normal (so NOPRESERVE will be honored, @@DIFF will be removed, &amp;c.) but their changes (such as turning on the diff-assister) will not be honored.</p>
<dt><code>&#8211;no-replace | &#8211;keep-old | -k</code></p>
<dd> Do not replace the old NFO file; write new file to file.new.nfo. Default: Use file[.nfo].new as temporary, rename it to file[.nfo] when done.</p>
<dt><code>&#8211;silent | -s</code></p>
<dd> Silence the progress output in interactive mode.</p>
<dt><code>&#8211;version | -v</code></p>
<dd> Display the version.</p>
<dt><code>&#8211;write-data</code></p>
<dd> Refresh all data files, unless they are newer.</dl>
<p> The following options cause NFORenum to behave as if all files started with the associated command. The readme has full details on the comment commands. Options associated with comment commands that require additional information take that information as an argument. With the exception of &#8211;<code>L / &#8211;let , the options to the command line versions are case insensitive.</code> &quot;ON&quot; and &quot;OFF&quot; may be specified with &quot;+&quot; and &quot;-&quot;, respectively.</p>
<dl>
<dt><code>&#8211;beautify | -b</code></p>
<dd> @@BEAUTIFY</p>
<dt><code>&#8211;diff | -d</code></p>
<dd> @@DIFF</p>
<dt><code>&#8211;let | -L</code></p>
<dd> @@LET</p>
<dt><code>&#8211;lint | -l</code></p>
<dd> @@LINT</p>
<dt><code>&#8211;preserve-messages | -p</code></p>
<dd> @@PRESERVEMESSAGES</p>
<dt><code>&#8211;real-sprites | -r</code></p>
<dd> @@REALSPRITES</p>
<dt><code>&#8211;use-old-nums | -o</code></p>
<dd> @@USEOLDSPRITENUMS</p>
<dt><code>&#8211;warning-disable | -w</code></p>
<dd> @@WARNING DISABLE</p>
<dt><code>&#8211;warning-enable | -W</code></p>
<dd> @@WARNING ENABLE</dl>
<p> &#8211;<code>w</code> and &#8211;<code>W</code> (and their long counterparts) also accept a comma-separated list of messages, all of which will be ENABLEd or DISABLEd.</p>
<h2>SEE ALSO</h2>
<p> The documentation in /usr/share/doc/nforenum/</p>
<h2>AUTHOR</h2>
<p> nforenum was written by Dale McCoy, with portions by Dan Masek, Thijs Marinussen, Remko Bijker and Christoph Elsenhans. </p>
<p> This manual page was written by Remko Bijker. </p>
<h2>Index</h2>
