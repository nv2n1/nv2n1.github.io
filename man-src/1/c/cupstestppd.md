---
title: "cupstestppd(1)"
name: "cupstestppd"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cupstestppd/"
description: "cupstestppd – test conformance of ppd files (deprecated)"
---

<h2 class="name">NAME</h2>
<p> cupstestppd &#8211; test conformance of ppd files (deprecated) </p>
<h2>SYNOPSIS</h2>
<p> <code>cupstestppd</code> [ <code>-I</code> <i>category</i> ] [ <code>-R</code> <i>rootdir</i> ] [ <code>-W</code> <i>category</i> ] [ <code>-q</code> ] [ <code>-r</code> ] [ <code>-v</code>[<code>v</code>] ] <i>filename.ppd[.gz]</i> [ &#8230; <i>filename.ppd[.gz]</i> ]<br />
 <code>cupstestppd</code> [ <code>-R</code> <i>rootdir</i> ] [ <code>-W</code> <i>category</i> ] [ <code>-q</code> ] [ <code>-r</code> ] [ <code>-v</code>[<code>v</code>] ] <code>&#8211;</code></p>
<h2>DESCRIPTION</h2>
<p> <code>cupstestppd</code> tests the conformance of PPD files to the Adobe PostScript Printer Description file format specification version 4.3. It can also be used to list the supported options and available fonts in a PPD file. The results of testing and any other output are sent to the standard output. </p>
<p> The first form of <code>cupstestppd</code> tests one or more PPD files on the command-line. The second form tests the PPD file provided on the standard input.</p>
<h2>OPTIONS</h2>
<p> <code>cupstestppd</code> supports the following options:</p>
<dl>
<dt><code>-I filename</code></p>
<dd> Ignores all PCFileName warnings.</p>
<dt><code>-I filters</code></p>
<dd> Ignores all filter errors.</p>
<dt><code>-I profiles</code></p>
<dd> Ignores all profile errors.</p>
<dt><code>-R </code><i>rootdir</i></p>
<dd> Specifies an alternate root directory for the filter, pre-filter, and other support file checks.</p>
<dt><code>-W constraints</code></p>
<dd> Report all UIConstraint errors as warnings.</p>
<dt><code>-W defaults</code></p>
<dd> Except for size-related options, report all default option errors as warnings.</p>
<dt><code>-W filters</code></p>
<dd> Report all filter errors as warnings.</p>
<dt><code>-W profiles</code></p>
<dd> Report all profile errors as warnings.</p>
<dt><code>-W sizes</code></p>
<dd> Report all media size errors as warnings.</p>
<dt><code>-W translations</code></p>
<dd> Report all translation errors as warnings.</p>
<dt><code>-W all</code></p>
<dd> Report all of the previous errors as warnings.</p>
<dt><code>-W none</code></p>
<dd> Report all of the previous errors as errors.</p>
<dt><code>-q</code></p>
<dd> Specifies that no information should be displayed.</p>
<dt><code>-r</code></p>
<dd> Relaxes the PPD conformance requirements so that common whitespace, control character, and formatting problems are not treated as hard errors.</p>
<dt><code>-v</code></p>
<dd> Specifies that detailed conformance testing results should be displayed rather than the concise PASS/FAIL/ERROR status.</p>
<dt><code>-vv</code></p>
<dd> Specifies that all information in the PPD file should be displayed in addition to the detailed conformance testing results.</dl>
<p> The <i>-q</i>, <i>-v</i>, and <i>-vv</i> options are mutually exclusive.</p>
<h2>EXIT STATUS</h2>
<p> <code>cupstestppd</code> returns zero on success and non-zero on error. The error codes are as follows:</p>
<dl>
<dt>1</p>
<dd> Bad command-line arguments or missing PPD filename.</p>
<dt>2</p>
<dd> Unable to open or read PPD file.</p>
<dt>3</p>
<dd> The PPD file contains format errors that cannot be skipped.</p>
<dt>4</p>
<dd> The PPD file does not conform to the Adobe PPD specification.</dl>
<h2>EXAMPLES</h2>
<p> The following command will test all PPD files under the current directory and print the names of each file that does not conform: </p>
<pre>
    find . -name \*.ppd \! -exec cupstestppd -q '{}' \; -print
</pre>
<p> The next command tests all PPD files under the current directory and print detailed conformance testing results for the files that do not conform: </p>
<pre><code>
find.- name \*.ppd \!-exec cupstestppd - q '{}' \;
- exec cupstestppd - v '{}' \;
</code></pre>
<h2>NOTES</h2>
<p> PPD files are deprecated and will no longer be supported in a future feature release of CUPS. Printers that do not support IPP can be supported using applications such as <code><a href="/docs/linux/man/1-ippeveprinter/">ippeveprinter</a></code>(1).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-lpadmin/">lpadmin</a></code>(8), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a>), Adobe PostScript Printer Description File Format Specification, Version 4.3.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
<h2>Index</h2>
