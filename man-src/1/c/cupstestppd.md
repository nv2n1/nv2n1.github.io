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
<dt><code>-I filename</code></dt>
<dd> Ignores all PCFileName warnings.</dd>
<dt><code>-I filters</code></dt>
<dd> Ignores all filter errors.</dd>
<dt><code>-I profiles</code></dt>
<dd> Ignores all profile errors.</dd>
<dt><code>-R </code><i>rootdir</i></dt>
<dd> Specifies an alternate root directory for the filter, pre-filter, and other support file checks.</dd>
<dt><code>-W constraints</code></dt>
<dd> Report all UIConstraint errors as warnings.</dd>
<dt><code>-W defaults</code></dt>
<dd> Except for size-related options, report all default option errors as warnings.</dd>
<dt><code>-W filters</code></dt>
<dd> Report all filter errors as warnings.</dd>
<dt><code>-W profiles</code></dt>
<dd> Report all profile errors as warnings.</dd>
<dt><code>-W sizes</code></dt>
<dd> Report all media size errors as warnings.</dd>
<dt><code>-W translations</code></dt>
<dd> Report all translation errors as warnings.</dd>
<dt><code>-W all</code></dt>
<dd> Report all of the previous errors as warnings.</dd>
<dt><code>-W none</code></dt>
<dd> Report all of the previous errors as errors.</dd>
<dt><code>-q</code></dt>
<dd> Specifies that no information should be displayed.</dd>
<dt><code>-r</code></dt>
<dd> Relaxes the PPD conformance requirements so that common whitespace, control character, and formatting problems are not treated as hard errors.</dd>
<dt><code>-v</code></dt>
<dd> Specifies that detailed conformance testing results should be displayed rather than the concise PASS/FAIL/ERROR status.</dd>
<dt><code>-vv</code></dt>
<dd> Specifies that all information in the PPD file should be displayed in addition to the detailed conformance testing results.</dd></dl>
<p> The <i>-q</i>, <i>-v</i>, and <i>-vv</i> options are mutually exclusive.</p>
<h2>EXIT STATUS</h2>
<p> <code>cupstestppd</code> returns zero on success and non-zero on error. The error codes are as follows:</p>
<dl>
<dt>1</dt>
<dd> Bad command-line arguments or missing PPD filename.</dd>
<dt>2</dt>
<dd> Unable to open or read PPD file.</dd>
<dt>3</dt>
<dd> The PPD file contains format errors that cannot be skipped.</dd>
<dt>4</dt>
<dd> The PPD file does not conform to the Adobe PPD specification.</dd></dl>
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
