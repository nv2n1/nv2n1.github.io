---
title: "bidiv(1)"
name: "bidiv"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bidiv/"
description: "bidiv – bidirectional text filter"
---

<h2>NAME</h2>
<p> bidiv &#8211; bidirectional text filter</p>
<h2>SYNOPSIS</h2>
<p> <code>bidiv</code> [ <code>-plj</code> ] [ <code>-w&nbsp;<wbr></code><i>width</i> ] <code>[</code><i>file&#8230;</i><code>]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>bidiv</code> is a filter, or viewer, for birectional text stored in logical-order. It converts such text into visual-order text which can be viewed on terminals that do not handle bidirectionality. The output visual-order text is formatted assuming a fixed number of characters per line (automatically determined or given with the <code>-w</code> parameter). </p>
<p> <code>bidiv</code> is oriented towards Hebrew, and assumes the input to be a Hebrew and ASCII text encoded in one of the two common logical-order encodings: ISO-8859-8-i or UTF-8. Actually, bidiv guesses the encoding of its input at a character by character basis, so the input might be a mix of ISO-8859-8-i and Hebrew UTF-8. <code>bidiv</code>&#8216;s output is visual-order text, in either the ISO-8859-8 or UTF-8 encoding, depending on your locale setting. </p>
<p> <code>bidiv</code> reads each <i>file</i> in sequence, converts it into visual order and writes it on the standard output. Thus: </p>
<dl>
<dt>
<dd> <code>$ bidiv file</code></dl>
<p> prints <code>file</code> on your terminal (assuming it has the appropriate fonts, but no bidirectionality support), and: </p>
<dl>
<dt>
<dd> <code>$ bidiv file1 file2 | less</code></dl>
<p> concatenates <code>file1</code> and <code>file2</code>, and shows the results using the pager <code>less</code>. </p>
<p> If no input file is given, <code>bidiv</code> reads from the standard input file. </p>
<p> For more ideas on how to use <code>bidiv</code>, see the <code>EXAMPLES</code> section below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p </code></p>
<dd> Paragraph-based direction (default): When formatting a bidirectional output line, <code>bidiv</code> needs to be aware of that line&#8217;s base direction. A line whose base direction is RTL (right to left) gets right-justified and its first element appears on the right. Otherwise, the line is left-justified and its first element appears on the left. </p>
<p> The <code>-p</code> option tells <code>bidiv</code> to choose a base direction per paragraph, where a paragraph is delimited by an empty line. This is bidiv&#8217;s default behavior, and usually gives the expected results on most texts and emails. </p>
<p> The direction of the entire paragraph is chosen according to the first strongly-directioned character (i.e., an alphabetic character) appearing in the paragraph. Currently, if the first output line of a paragraph has no directional characters (e.g., a line of minus signs before an email signature, or a line containing only numbers) that line is output with the same direction of the previous paragraph, but it does not determine the direction of the rest of the paragraph. If the first line of the first paragraph does not have a direction, the RTL direction is arbitrarily chosen.</p>
<dt><code>-l</code></p>
<dd> Line-based direction: This option choose an alternative method of choosing each output line&#8217;s base direction. When this option is enabled, the base direction of each output line is determined on its own (again, according to the first character on the line with a strong direction). This method may give wrong results in the case where a line starts with a word of the opposite direction. This case is rare, but does happen under random line-splitting circumstances, or when the text is defining words of a foreign language. </p>
<dt><code>-j</code></p>
<dd> Do not justify: By default, RTL lines are right-justified, i.e., they are padded with spaces on the left when shorter than the required line width (see the <code>-w</code> option). The <code>-j</code> option tells <code>bidiv</code> not to preform this justifications, and leave short lines unpadded.</p>
<dt><code>-w&nbsp;<wbr></code><i>width</i></p>
<dd> <code>bidiv</code> formats its output for lines of the given width. Lines are split when longer than this width, and RTL lines are right-justfied to fill that width unless the <code>-j</code> option is given. </p>
<p> When the <code>-w</code> option is not given, <code>bidiv</code> uses the value of the <code>COLUMNS</code> variable, which is usually automatically defined by the user&#8217;s shell. When that both the <code>-w</code> option and the <code>COLUMNS</code> variable are missing, the default of 80 columns is used.</dl>
<h2>OPERANDS</h2>
<p> The following operand is supported:</p>
<dl>
<dt><i>file</i></p>
<dd> A path name of an input file. If no <i>file</i> is specified, the standard input is used. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>1.</p>
<dd> bidiv README | less</p>
<dt>2.</p>
<dd> man something | bidiv | less </p>
<p> (or groff -man -Tlatin1 something.1 |sed &#8216;s/.^H\(.\)/\1/g&#8217; |../bidiv -w 65)</p>
<dt>3.</p>
<dd> set &quot;bidiv&quot; as a filter for your mail program (mutt, pine, etc.) for viewing mail with the ISO 8859-8-i character set, and Hebrew UTF-8 mail. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> <code>COLUMNS</code> see <code>-w</code> option.</p>
<h2>EXIT STATUS</h2>
<p> The following exit values are returned:</p>
<dl>
<dt><code>0</code></p>
<dd> All input files were output successfully.</p>
<dt><code>&gt;0</code></p>
<dd> An error occurred.</dl>
<h2>AUTHOR</h2>
<p> Written by Nadav Har&#8217;El, <a rel="nofollow" href="http://nadav.harel.org.il.">http://nadav.harel.org.il.</a> </p>
<p> Please send bug reports and comments to nyh [at] math.technion.ac.il. </p>
<p> The latest version of this software can be found in <code><a href="ftp://ftp.ivrix.org.il/pub/ivrix/src/cmdline">ftp://ftp.ivrix.org.il/pub/ivrix/src/cmdline</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1), <code><a href="/docs/linux/man/3-fribidi/">fribidi</a></code>(3) </p>
<h2>Index</h2>
