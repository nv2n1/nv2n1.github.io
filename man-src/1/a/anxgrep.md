---

title: "anxgrep(1)"
name: "anxgrep"
section: "1"
letter: "a"
url: "/docs/linux/man/1-anxgrep/"
description: "anxgrep — Search for PATTERN in each annodex FILE or standard input."
---

<p> anxgrep &#8212; Search for PATTERN in each annodex FILE or standard input.<br/>
&nbsp;<wbr></p>
<h2>SYNOPSIS</h2>
<p> <code>anxgrep</code> [-E | &#8211;extended-regexp ] [-G | &#8211;basic-regexp ] [-i | &#8211;ignore-case ] [-v | &#8211;invert-match ] [-o <code>filename</code> | &#8211;output <code>filename</code> ] [&#8211;label <code>LABEL</code> ] [-q | &#8211;quiet | &#8211;silent ] [-L | &#8211;files-without-match ] [-l | &#8211;files-with-matches ] [-c | &#8211;count ] [-h | &#8211;help ] [&#8211;version ] filename</p>
<h2>Description</h2>
<p> <code>anxgrep</code> searches the CMML tracks of Annodex FILEs (or standard input if no files are named, or the file name &#8211; is given) for elements containing a match to the given PATTERN. By default, <code>anxgrep</code> prints the matching elements.<br/>
&nbsp;<wbr></p>
<h2>Options</h2>
<p> <code>anxgrep</code> accepts the following options:<br/>
&nbsp;<wbr></p>
<h3>Regexp selection and interpretation</h3>
<dl>
<dt>-E, &#8211;extended-regexp</dt>
<dd> PATTERN is an extended regular expression</dd>
<dt>-G, &#8211;basic-regexp</dt>
<dd> PATTERN is a basic regular expression</dd>
<dt>-i, &#8211;ignore-case</dt>
<dd> Ignore case distinctions</dd>
<dt>-v, &#8211;invert-match</dt>
<dd> Select non-matching elements</dd></dl>
<h3>CMML options</h3>
<dl>
<dt>&#8211;head</dt>
<dd> Search only the CMML head element of each file (ignore clips)</dd>
<dt>&#8211;meta</dt>
<dd> Search only meta elements (ignore clip descriptions)</dd></dl>
<h3>Output options</h3>
<dl>
<dt>-o <code>filename</code>, &#8211;output <code>filename</code></dt>
<dd> Write output to the specified <code>filename</code> instead of printing it to standard output.</dd>
<dt>&#8211;label <code>LABEL</code></dt>
<dd> Print <code>LABEL</code> as the filename for standard input.</dd>
<dt>-q, &#8211;quiet, &#8211;silent</dt>
<dd> Suppress all normal output</dd>
<dt>-L, &#8211;files-without-match</dt>
<dd> Only print FILE names containing no match</dd>
<dt>-l, &#8211;files-with-matches</dt>
<dd> Only print FILE names containing matches</dd>
<dt>-c, &#8211;count</dt>
<dd> Only print a count of matching lines per FILE</dd></dl>
<h3>Miscellaneous options</h3>
<dl>
<dt>-h, &#8211;help</dt>
<dd> Display usage information and exit.</dd>
<dt>&#8211;version</dt>
<dd> Output version information and exit.</dd></dl>
<h2>AUTHOR</h2>
<p> Conrad Parker March 2, 2005;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 CSIRO Australia<br/>
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-grep/">grep</a></code><code>(1)</code> <code><a href="/docs/linux/man/1-anxrip/">anxrip</a></code><code>(1)</code> </p>
<p> More information is available at <i>Annodex.net (link to URL <a rel="nofollow" href="http://www.annodex.net/)">http://www.annodex.net/)</a> </i> </p>
