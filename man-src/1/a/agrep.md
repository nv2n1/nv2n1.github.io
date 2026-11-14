---
title: "agrep(1)"
name: "agrep"
section: "1"
letter: "a"
url: "/docs/linux/man/1-agrep/"
description: "agrep – print lines approximately matching a pattern"
---

<h2>NAME</h2>
<p> agrep &#8211; print lines approximately matching a pattern</p>
<h2>SYNOPSIS</h2>
<p> <code>agrep</code> [<i>OPTION</i>]&#8230; <i>PATTERN</i> [<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Searches for approximate matches of PATTERN in each FILE or standard input. Example: `agrep -2 optimize foo.txt&#8217; outputs all lines in file `foo.txt&#8217; that match &quot;optimize&quot; within two errors. E.g. lines which contain &quot;optimise&quot;, &quot;optmise&quot;, and &quot;opitmize&quot; all match.</p>
<h2>OPTIONS</h2>
<h3>Regexp selection and interpretation:</h3>
<dl>
<dt><code>-e</code><i> PATTERN</i>, &#8211;regexp=<i>PATTERN</i></p>
<dd> Use <i>PATTERN</i> as a regular expression; useful to protect patterns beginning with <code>&#8211;</code>.</p>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></p>
<dd> Ignore case distinctions (as defined by the current locale) in <i>PATTERN</i> and input files.</p>
<dt><code>-k</code>, <code>&#8211;literal</code></p>
<dd> Treat <i>PATTERN</i> as a literal string, that is, a fixed string with no special characters.</p>
<dt><code>-w</code>, <code>&#8211;word-regexp</code></p>
<dd> Force <i>PATTERN</i> to match only whole words. A &quot;whole word&quot; is a substring which either starts at the beginning or the record or is preceded by a non-word constituent character. Similarly, the substring must either end at the end of the record or be followed by a non-word constituent character. Word-constituent characters are alphanumerics (as defined by the current locale) and the underscore character. Note that the non-word constituent characters <code>must</code> surround the match; they cannot be counted as errors.</dl>
<h3>Approximate matching settings:</h3>
<dl>
<dt><code>-D</code><i> NUM</i>, &#8211;delete-cost=<i>NUM</i></p>
<dd> Set cost of missing characters to <i>NUM</i>.</p>
<dt><code>-I</code><i> NUM</i>, &#8211;insert-cost=<i>NUM</i></p>
<dd> Set cost of extra characters to <i>NUM</i>.</p>
<dt><code>-S</code><i> NUM</i>, &#8211;substitute-cost=<i>NUM</i></p>
<dd> Set cost of incorrect characters to <i>NUM</i>. Note that a deletion (a missing character) and an insertion (an extra character) together constitute a substituted character, but the cost will be the that of a deletion and an insertion added together. Thus, if the const of a substitution is set to be larger than the sum of the costs of deletion and insertion, direct substitutions will never be done.</p>
<dt><code>-E</code><i> NUM</i>, &#8211;max-errors=<i>NUM</i></p>
<dd> Select records that have at most <i>NUM</i> errors.</p>
<dt>&#8211;<i>#</i></p>
<dd> Select records that have at most <i>#</i> errors (<i>#</i> is a digit between 0 and 9).</dl>
<h3>Miscellaneous:</h3>
<dl>
<dt><code>-d</code><i> PATTERN</i>, &#8211;delimiter=<i>PATTERN</i></p>
<dd> Set the record delimiter regular expression to <i>PATTERN</i>. The text between two delimiters, before the first delimiter, and after the last delimiter is considered to be a record. The default record delimiter is the regexp &quot;
&quot;, so by default a record is a line. <i>PATTERN</i> can be any regular expression that does not match the empty string. For example, using <code>-d</code> &quot;^From &quot; defines mail messages as records in a Mailbox format file.</p>
<dt><code>-v</code>, <code>&#8211;invert-match</code></p>
<dd> Select non-matching records instead of matching records.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version information and exit.</p>
<dt><code>-y</code>, <code>&#8211;nothing</code></p>
<dd> Does nothing. This options exists only for compatibility with the non-free agrep program.</p>
<dt><code>&#8211;help</code></p>
<dd> Display a brief help message and exit.</dl>
<h3>Output control:</h3>
<dl>
<dt><code>-B</code>, <code>&#8211;best-match</code></p>
<dd> Only output the best matching records, that is, the records with the lowest cost. This is currently implemented by making two passes over the input files and cannot be used when reading from standard input.</p>
<dt><code>&#8211;color</code>, <code>&#8211;colour</code></p>
<dd> Highlight the matching strings in the output with a color marker. The color string is taken from the <code>GREP_COLOR</code> environment variable. The default color is red.</p>
<dt><code>-c</code>, <code>&#8211;count</code></p>
<dd> Only print a count of matching records per each input file, suppressing normal output.</p>
<dt><code>-h</code>, <code>&#8211;no-filename</code></p>
<dd> Suppress the prefixing filename on output when multiple files are searched.</p>
<dt><code>-H</code>, <code>&#8211;with-filename</code></p>
<dd> Prefix each output record with the name of the input file where the record was read from.</p>
<dt><code>-l</code>, <code>&#8211;files-with-matches</code></p>
<dd> Only print the name of each input file which contains at least one match, suppressing normal output. The scanning for each file will stop on the first match.</p>
<dt><code>-n</code>, <code>&#8211;record-number</code></p>
<dd> Prefix each output record with its sequence number in the input file. The number of the first record is 1.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</code></p>
<dd> Do not write anything to standard output. Exit immediately with zero exit status if a match is found.</p>
<dt><code>-s</code>, <code>&#8211;show-cost</code></p>
<dd> Print match cost with output.</p>
<dt><code>&#8211;show-position</code></p>
<dd> Prefix each output record with the start and end offset of the first match within the record. The offset of the first character of the record is 0. The end position is given as the offset of the first character after the match.</p>
<dt><code>-M</code>, <code>&#8211;delimiter-after</code></p>
<dd> By default, the record delimiter is the newline character and is output after the matching record. If <code>-d</code> is used, the record delimiter will be output before the matching record. This option causes the delimiter to be output after the matching record.</dl>
<p> With no <i>FILE</i>, or when <i>FILE</i> is -, reads standard input. If less than two <i>FILE</i>s are given <code>-h</code> is assumed, otherwise <code>-H</code> is the default.</p>
<h2>DIAGNOSTICS</h2>
<p> Exit status is 0 if a match is found, 1 for no match, and 2 if there were errors. If <code>-E</code> or &#8211;<i>#</i> is not specified, only exact matches are selected. </p>
<p> <i>PATTERN</i> is a POSIX extended regular expression (ERE) with the TRE extensions.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to the TRE mailing list &lt;<code>tre-general [at] lists.laurikari.net</code>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2004 Ville Laurikari.<br />
 This is free software, and comes with ABSOLUTELY NO WARRANTY. You are welcome to redistribute this software under certain conditions; see the source for the full license text. </p>
<h2>Index</h2>
