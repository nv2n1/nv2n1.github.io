---
title: "nomarch(1)"
name: "nomarch"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nomarch/"
description: "nomarch – extract `.arc’ archives"
---

<h2 class="name">NAME</h2>
<p> nomarch &#8211; extract `.arc&#8217; archives </p>
<h2>SYNOPSIS</h2>
<p> <code>nomarch</code> [<i>-hlptUv</i>] [<code>archive.arc</code>] [<code>match1</code> [<code>match2</code> &#8230; ]] </p>
<h2>DESCRIPTION</h2>
<p> nomarch lists, extracts, or tests `.arc&#8217; archives. (An alternate extension sometimes used was `.ark&#8217;; these work too.) This is a <i>very</i> outdated file format which should certainly not be used for anything new, but you may still need an extraction utility, and here it is. :-) </p>
<p> The default action is to extract all files in the specified archive; see <code>OPTIONS</code> below for how to do other things instead.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h</i></p>
<dd> give terse usage help.</p>
<dt><i>-l</i></p>
<dd> list files in archive. If verbose listings are enabled, it shows the filename, compression method, compressed/uncompressed size, date/time, and CRC; but by default, it just shows the filename, uncompressed size, and date/time.</p>
<dt><i>-p</i></p>
<dd> extract to standard output, rather than to separate files.</p>
<dt><i>-t</i></p>
<dd> test files in archive (more precisely, check file CRCs).</p>
<dt><i>-U</i></p>
<dd> use uppercase filenames; more precisely, preserve original case from archive.</p>
<dt><i>-v</i></p>
<dd> give verbose output (when used with `<i>-l</i>&#8216;).</p>
<dt><code>archive.arc</code></p>
<dd> the archive to operate on.</p>
<dt><code>match1</code> etc.</p>
<dd> optionally specify which archive members to list/extract/test. Those which match any of these filenames/wildcards are processed. Wildcard operators supported are shell-like `*&#8217; and `?&#8217;, but don&#8217;t forget to quote arguments which use these (e.g. `<i>nomarch</i> <i>foo.arc &#8216;*.bar&#8217;</i>&#8216;).</dl>
<h2>EXTRACTING MULTIPLE ARCHIVES</h2>
<p> nomarch follows the `unzip&#8217;-like practice of working on only one archive per run, with further `filenames&#8217; given on the command-line actually specifying files to extract (or whatever). The easiest way to work on multiple files with nomarch is simply to run it multiple times using <i>for</i>; for example: </p>
<p> for i in *.arc; do nomarch $i; done </p>
<p> The above would extract all archives in the current directory.</p>
<h2>USING THE PROGRAM FROM EMACS</h2>
<p> Emacs&#8217;s arc-mode facility lets you work with various kinds of archive file directly from the editor. Making it use nomarch for extracting `.arc&#8217; files isn&#8217;t too hard. Just add the following to your <i>~/.emacs</i> file: </p>
<p> (setq archive-arc-extract &#8216;(&quot;nomarch&quot; &quot;-U&quot;))</p>
<h2>BUGS</h2>
<p> The CRC used by the format is only 16-bit, so `<i>-t</i>&#8216; is a less-than-perfect test. </p>
<p> One compression method, obsolete even by `.arc&#8217; standards :-), isn&#8217;t supported yet. This is partly because I&#8217;ve yet to find a single file which uses it, despite testing an awful lot of files. </p>
<p> Subdirectories in Spark archives are extracted as the `.arc&#8217;-format files they really are, which may not be terribly convenient.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-tar/">tar</a></i>(1), <i><a href="/docs/linux/man/1-gzip/">gzip</a></i>(1), <i><a href="/docs/linux/man/1-bzip2/">bzip2</a></i>(1), <i><a href="/docs/linux/man/1-lbrate/">lbrate</a></i>(1)</p>
<h2>AUTHOR</h2>
<p> Russell Marks (rus [at] svgalib.org). </p>
<h2>Index</h2>
