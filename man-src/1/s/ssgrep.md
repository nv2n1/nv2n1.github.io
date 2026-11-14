---
title: "ssgrep(1)"
name: "ssgrep"
section: "1"
letter: "s"
url: "/docs/linux/man/1-ssgrep/"
description: "ssgrep – search spreadsheets for strings"
---

<h2 class="name">NAME</h2>
<p> ssgrep &#8211; search spreadsheets for strings</p>
<h2>SYNOPSIS</h2>
<p> <code>ssgrep </code> [<i>OPTIONS</i>] [<i>FILES</i>] </p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents the <code>ssgrep</code> command. </p>
<p> <code>ssgrep</code> is a command line utility to search for strings in spreadsheets of any format supported by gnumeric. Without any output modifying options, <code>ssgrep</code> prints one line for each match. A match consists of the matching content of a cell or, if the <code>-R</code> option is given, the matching expression result of a cell. </p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with single letter options starting with a single dash (`-&#8216;) and longer options starting with two dashes (`&#8211;&#8216;). </p>
<h3>Options controlling input file handling</h3>
<dl>
<dt><code>&#8211;recalc</code></p>
<dd> Recalculate all cells </p>
</dl>
<h3>Options controlling patterns and pattern matching</h3>
<dl>
<dt><code>-f, &#8211;keyword-file=</code><i>FILE</i></p>
<dd> The path to a text file containing one key per line</p>
<dt><code>-i, &#8211;ignore-case</code></p>
<dd> Ignore differences in letter case</p>
<dt><code>-w, &#8211;word-regexp</code></p>
<dd> Match only whole words</p>
<dt><code>-F, &#8211;fixed-strings</code></p>
<dd> Pattern is a set of fixed strings</p>
<dt><code>-R, &#8211;search-results</code></p>
<dd> Search results of expressions too</p>
<dt><code>-v, &#8211;invert-match</code></p>
<dd> Search for cells that do not match </p>
</dl>
<h3>Options controlling output in general</h3>
<dl>
<dt><code>-c, &#8211;count</code></p>
<dd> Only print a count of matches per file</p>
<dt><code>-L, &#8211;files-without-matches</code></p>
<dd> Print filenames without matches</p>
<dt><code>-l, &#8211;files-with-matches</code></p>
<dd> Print filenames with matches</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Suppress all normal output</p>
<dt><code>-H, &#8211;with-filename</code></p>
<dd> Print the filename for each match</p>
<dt><code>-h, &#8211;without-filename</code></p>
<dd> Do not print the filename for each match</p>
<dt><code>-n, &#8211;print-locus</code></p>
<dd> Print the location of each match</p>
<dt><code>-T, &#8211;print-type</code></p>
<dd> Print the location type of each match </p>
</dl>
<h3>Help options</h3>
<dl>
<dt><code>-V, &#8211;version</code></p>
<dd> Display ssgrep&#8217;s version</p>
<dt><code>-?, &#8211;help</code></p>
<dd> Display the supported options</p>
<dt><code>&#8211;usage</code></p>
<dd> Display a brief usage message </p>
</dl>
<h2>EXAMPLE</h2>
<p> To search for the string &quot;SUM&quot; in the file <i>foo.gnumeric</i> : </p>
<p> <code>ssgrep</code> <i>SUM</i> <i>foo.gnumeric</i> </p>
<p> To search for the strings from the file <i>keywords</i> in the spreadsheet <i>foo.xls</i> : </p>
<p> <code>ssgrep</code> <code>&#8211;keyword-file=</code><i>keywords</i> <i>foo.xls</i> </p>
<h2>LICENSE</h2>
<p> <code>ssgrep</code> is licensed under the terms of the General Public License (GPL), version 2 or 3. For information on this license look at the source code that came with the software or see the GNU project page &lt;URL: <a rel="nofollow" href="http://www.gnu.org">http://www.gnu.org</a> &gt;. </p>
<h2>COPYRIGHT</h2>
<p> The copyright on <code>ssgrep</code> and the <code>gnumeric</code> software and source code is held by the individual authors as is documented in the source code. </p>
<h2>AUTHOR</h2>
<p> <code>ssgrep</code>&#8216;s primary author is Jody Goldberg &lt;jody [at] gnome.org&gt;; <code>ssgrep</code> builds on the <code>gnumeric</code> codebase. </p>
<p> The initial version of this manpage was based on ssindex.1 by J.H.M. Dassen (Ray) &lt;jdassen [at] debian.org&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-beagled/">beagled</a></code>(1), <code><a href="/docs/linux/man/1-gnumeric/">gnumeric</a></code>(1), <code><a href="/docs/linux/man/1-ssconvert/">ssconvert</a></code>(1), <code><a href="/docs/linux/man/1-ssdiff/">ssdiff</a></code>(1) <code><a href="/docs/linux/man/1-ssindex/">ssindex</a></code>(1) </p>
<p> The Gnumeric Homepage &lt;URL: <a rel="nofollow" href="http://www.gnome.org/projects/gnumeric/">http://www.gnome.org/projects/gnumeric/</a> &gt;. </p>
<p> The GNOME project page &lt;URL: <a rel="nofollow" href="http://www.gnome.org/">http://www.gnome.org/</a> &gt;. </p>
<h2>Index</h2>
