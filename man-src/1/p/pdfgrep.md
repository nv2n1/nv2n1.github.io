---
title: "pdfgrep(1)"
name: "pdfgrep"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfgrep/"
description: "pdfgrep – search pdf files for a regular expression"
---

<h2 class="name">NAME</h2>
<p> pdfgrep &#8211; search pdf files for a regular expression </p>
<h2>SYNOPSIS</h2>
<p> <code>pdfgrep</code> [<i>OPTION</i>&#8230;] <i>PATTERN</i> <i>FILE</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Search for <i>PATTERN</i> in each <i>FILE</i>. <i>PATTERN</i> is an extended regular expression. </p>
<p> <code>pdfgrep</code> works much like grep, with one distinction: It operates on pages and not on lines.</p>
<h2>OPTIONS</h2>
<p> <code>-i</code>, <code>&#8211;ignore-case</code></p>
<dl>
<dt>
<dd> Ignore case distinctions in both the <i>PATTERN</i> and the input files.</dl>
<p> <code>-H</code>, <code>&#8211;with-filename</code></p>
<dl>
<dt>
<dd> Print the file name for each match. This is the default setting when there is more than one file to search.</dl>
<p> <code>-h</code>, <code>&#8211;no-filename</code></p>
<dl>
<dt>
<dd> Suppress the prefixing of file name on output. This is the default setting when there is only one file to search.</dl>
<p> <code>-n</code>, <code>&#8211;page-number</code></p>
<dl>
<dt>
<dd> Prefix each match with the number of the page where it was found.</dl>
<p> <code>-c</code>, <code>&#8211;count</code></p>
<dl>
<dt>
<dd> Suppress normal output. Instead print the number of matches for each input file. Note that unlike grep, multiple matches on the same page will be counted individually.</dl>
<p> <code>-p</code>, <code>&#8211;page-count</code></p>
<dl>
<dt>
<dd> Like <code>-c</code>, but prints the number of matches per page.</dl>
<p> <code>-C</code>, <code>&#8211;context</code> <i>NUM</i></p>
<dl>
<dt>
<dd> Print at most <i>INUM</i> characters of context around each match. The exact number will vary, because pdfgrep tries to respect word boundaries. If <i>NUM</i> is &quot;<code>line</code>&quot;, the whole line will be printed. If this option is not set, pdfgrep tries to print lines that are not longer than the terminal width.</dl>
<p> <code>&#8211;color</code> <i>WHEN</i></p>
<dl>
<dt>
<dd> Surround file names, page numbers and matched text with escape sequences to display them in color on the terminal. (The default setting is <code>auto</code>). <i>WHEN</i> can be: </p>
<p> <code>always</code></p>
<dl>
<dt>
<dd> Always use colors, even when stdout is not a terminal.</dl>
<p> <code>never</code></p>
<dl>
<dt>
<dd> Do not use colors.</dl>
<p> <code>auto</code></p>
<dl>
<dt>
<dd> Use colors only when stdout is a terminal.</dl>
</dl>
<p> <code>-r</code>, <code>&#8211;recursive</code></p>
<dl>
<dt>
<dd> Recursively search all files (restricted by <code>&#8211;include</code> and <code>&#8211;exclude</code>) under each directory, following symlinks only if they are on the command line.</dl>
<p> <code>-R</code>, <code>&#8211;dereference-recursive</code></p>
<dl>
<dt>
<dd> Same as <code>-r</code>, but follows all symlinks.</dl>
<p> <code>&#8211;exclude=</code><i>GLOB</i></p>
<dl>
<dt>
<dd> Skip files whose base name matches <i>GLOB</i>. See <i><a href="/docs/linux/man/7-glob/">glob</a></i>(7) for wildcards you can use. You can use this option multiple times to exclude more patterns. It takes precedence over <code>&#8211;include</code>. Note, that in- and excludes apply only to files found via <code>&#8211;recursive</code> and not to the argument list.</dl>
<p> <code>&#8211;include=</code><i>GLOB</i></p>
<dl>
<dt>
<dd> Only search files whose base name matches <i>GLOB</i>. See <code>&#8211;exclude</code> for details. The default is <i>*.pdf</i>.</dl>
<p> <code>&#8211;password=</code><i>PASSWORD</i></p>
<dl>
<dt>
<dd> Use PASSWORD to decrypt the PDF-files. <code>Note</code> that this password will show up in your command history and the output of <i><a href="/docs/linux/man/1-ps/">ps</a></i>(1). So please do not use this if the security of <i>PASSWORD</i> is important. It is also currently not possible to use individual passwords for different files.</dl>
<p> <code>-m</code>, <code>&#8211;max-count</code> <i>NUM</i></p>
<dl>
<dt>
<dd> Stop reading a file after <i>NUM</i> matching lines. When the -c or &#8211;count option is also used, pdfgrep does not output a count greater than <i>NUM</i>.</dl>
<p> <code>&#8211;unac</code></p>
<dl>
<dt>
<dd> Remove accents and ligatures from both the search pattern and the PDF documents. This is useful if you want to search for a word containing &quot;ae&quot;, but the PDF uses the single character &quot;æ&quot; instead. See <code><a href="/docs/linux/man/3-unac/">unac</a>(3)</code> and <code><a href="/docs/linux/man/1-unaccent/">unaccent</a>(1)</code> for details. </p>
<p> <code>This option is experimental and only available if pdfgrep is compiled with unac support.</code></dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Suppress all normal output to stdout. Errors will be printed and the exit codes will be returned (see below).</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short summary of the options.</dl>
<p> <code>-V</code>, <code>&#8211;version</code> Show version information.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The behavior of <code>pdfgrep</code> is affected by the following environment variable. </p>
<p> <code>GREP_COLORS</code></p>
<dl>
<dt>
<dd> Specifies the colors and other attributes used to highlight various parts of the output. The syntax and values are like <code>GREP_COLORS</code> of <code>grep</code>. See <i><a href="/docs/linux/man/1-grep/">grep</a></i>(1) for more details. Currently only the capabilities <code>mt</code>, <code>ms</code>, <code>mc</code>, <code>fn</code>, <code>ln</code> and <code>se</code> are used by <code>pdfgrep</code>, where <code>mt</code>, <code>ms</code> and <code>mc</code> have the same effect on <code>pdfgrep</code>.</dl>
<h2>EXIT STATUS</h2>
<p> Normally, the exit status is 0 if at least one match is found, 1 if no match is found and 2 if an error occurred. But if the <code>&#8211;quiet</code> or <code>-q</code> option is used and a match was found, <code>pdfgrep</code> will return 0 regardless of errors.</p>
<h2>AUTHOR</h2>
<p> Hans-Peter Deifel &lt;hpdeifel at gmx.de&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-grep/">grep</a>(1), <a href="/docs/linux/man/7-regex/">regex</a>(7) </p>
<h2>Index</h2>
