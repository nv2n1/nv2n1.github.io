---
title: "anxgrep(1)"
name: "anxgrep"
section: "1"
letter: "a"
url: "/docs/linux/man/1-anxgrep/"
description: "anxgrep — Search for PATTERN in each annodex FILE or standard input."
---

<h2>NAME</h2>
<p> anxgrep &#8212; Search for PATTERN in each annodex FILE or standard input.<br />
&nbsp;<wbr></p>
<h2>SYNOPSIS</h2>
<p> <code>anxgrep</code> [-E | &#8211;extended-regexp ] [-G | &#8211;basic-regexp ] [-i | &#8211;ignore-case ] [-v | &#8211;invert-match ] [-o <code>filename</code> | &#8211;output <code>filename</code> ] [&#8211;label <code>LABEL</code> ] [-q | &#8211;quiet | &#8211;silent ] [-L | &#8211;files-without-match ] [-l | &#8211;files-with-matches ] [-c | &#8211;count ] [-h | &#8211;help ] [&#8211;version ] filename</p>
<h2>Description</h2>
<p> <code>anxgrep</code> searches the CMML tracks of Annodex FILEs (or standard input if no files are named, or the file name &#8211; is given) for elements containing a match to the given PATTERN. By default, <code>anxgrep</code> prints the matching elements.<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p> <code>anxgrep</code> accepts the following options:<br />
&nbsp;<wbr></p>
<h3>Regexp selection and interpretation</h3>
<dl>
<dt>-E, &#8211;extended-regexp</p>
<dd> PATTERN is an extended regular expression</p>
<dt>-G, &#8211;basic-regexp</p>
<dd> PATTERN is a basic regular expression</p>
<dt>-i, &#8211;ignore-case</p>
<dd> Ignore case distinctions</p>
<dt>-v, &#8211;invert-match</p>
<dd> Select non-matching elements</dl>
<h3>CMML options</h3>
<dl>
<dt>&#8211;head</p>
<dd> Search only the CMML head element of each file (ignore clips)</p>
<dt>&#8211;meta</p>
<dd> Search only meta elements (ignore clip descriptions)</dl>
<h3>Output options</h3>
<dl>
<dt>-o <code>filename</code>, &#8211;output <code>filename</code></p>
<dd> Write output to the specified <code>filename</code> instead of printing it to standard output.</p>
<dt>&#8211;label <code>LABEL</code></p>
<dd> Print <code>LABEL</code> as the filename for standard input.</p>
<dt>-q, &#8211;quiet, &#8211;silent</p>
<dd> Suppress all normal output</p>
<dt>-L, &#8211;files-without-match</p>
<dd> Only print FILE names containing no match</p>
<dt>-l, &#8211;files-with-matches</p>
<dd> Only print FILE names containing matches</p>
<dt>-c, &#8211;count</p>
<dd> Only print a count of matching lines per FILE</dl>
<h3>Miscellaneous options</h3>
<dl>
<dt>-h, &#8211;help</p>
<dd> Display usage information and exit.</p>
<dt>&#8211;version</p>
<dd> Output version information and exit.</dl>
<h2>AUTHOR</h2>
<p> Conrad Parker March 2, 2005;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 CSIRO Australia<br />
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-grep/">grep</a></code><code>(1)</code> <code><a href="/docs/linux/man/1-anxrip/">anxrip</a></code><code>(1)</code> </p>
<p> More information is available at <i>Annodex.net (link to URL <a rel="nofollow" href="http://www.annodex.net/)">http://www.annodex.net/)</a> </i> </p>
<h2>Index</h2>
