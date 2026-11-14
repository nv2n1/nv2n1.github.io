---
title: "pr(1)"
name: "pr"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pr/"
description: "pr – convert text files for printing"
---

<h2 class="name">NAME</h2>
<p> pr &#8211; convert text files for printing </p>
<h2>SYNOPSIS</h2>
<p> <code>pr</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Paginate or columnate FILE(s) for printing. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt>+FIRST_PAGE[:LAST_PAGE], <code>&#8211;pages</code>=<i>,FIRST_PAGE[/</i>:LAST_PAGE]</p>
<dd> begin [stop] printing with page FIRST_[LAST_]PAGE</p>
<dt><code>-COLUMN</code>, <code>&#8211;columns</code>=<i>,COLUMN/</i></p>
<dd> output COLUMN columns and print columns down, unless <code>-a</code> is used. Balance number of lines in the columns on each page</p>
<dt><code>-a</code>, <code>&#8211;across</code></p>
<dd> print columns across rather than down, used together with <code>-COLUMN</code></p>
<dt><code>-c</code>, <code>&#8211;show-control-chars</code></p>
<dd> use hat notation (^G) and octal backslash notation</p>
<dt><code>-d</code>, <code>&#8211;double-space</code></p>
<dd> double space the output</p>
<dt><code>-D</code>, <code>&#8211;date-format</code>=<i>,FORMAT/</i></p>
<dd> use FORMAT for the header date</p>
<dt><code>-e[CHAR[WIDTH]]</code>, <code>&#8211;expand-tabs</code>[=<i>,CHAR[WIDTH]/</i>]</p>
<dd> expand input CHARs (TABs) to tab WIDTH (8)</p>
<dt><code>-F</code>, <code>-f</code>, <code>&#8211;form-feed</code></p>
<dd> use form feeds instead of newlines to separate pages (by a 3-line page header with <code>-F</code> or a 5-line header and trailer without <code>-F</code>)</p>
<dt><code>-h</code>, <code>&#8211;header</code>=<i>,HEADER/</i></p>
<dd> use a centered HEADER instead of filename in page header, <code>-h</code> &quot;&quot; prints a blank line, don&#8217;t use <code>-h</code>&quot;&quot;</p>
<dt><code>-i[CHAR[WIDTH]]</code>, <code>&#8211;output-tabs</code>[=<i>,CHAR[WIDTH]/</i>]</p>
<dd> replace spaces with CHARs (TABs) to tab WIDTH (8)</p>
<dt><code>-J</code>, <code>&#8211;join-lines</code></p>
<dd> merge full lines, turns off <code>-W</code> line truncation, no column alignment, <code>&#8211;sep-string</code>[=<i>,STRING/</i>] sets separators</p>
<dt><code>-l</code>, <code>&#8211;length</code>=<i>,PAGE_LENGTH/</i></p>
<dd> set the page length to PAGE_LENGTH (66) lines (default number of lines of text 56, and with <code>-F</code> 63). implies <code>-t</code> if PAGE_LENGTH &lt;= 10</p>
<dt><code>-m</code>, <code>&#8211;merge</code></p>
<dd> print all files in parallel, one in each column, truncate lines, but join lines of full length with <code>-J</code></p>
<dt><code>-n[SEP[DIGITS]]</code>, <code>&#8211;number-lines</code>[=<i>,SEP[DIGITS]/</i>]</p>
<dd> number lines, use DIGITS (5) digits, then SEP (TAB), default counting starts with 1st line of input file</p>
<dt><code>-N</code>, <code>&#8211;first-line-number</code>=<i>,NUMBER/</i></p>
<dd> start counting with NUMBER at 1st line of first page printed (see +FIRST_PAGE)</p>
<dt><code>-o</code>, <code>&#8211;indent</code>=<i>,MARGIN/</i></p>
<dd> offset each line with MARGIN (zero) spaces, do not affect <code>-w</code> or <code>-W</code>, MARGIN will be added to PAGE_WIDTH</p>
<dt><code>-r</code>, <code>&#8211;no-file-warnings</code></p>
<dd> omit warning when a file cannot be opened</p>
<dt><code>-s[CHAR]</code>, <code>&#8211;separator</code>[=<i>,CHAR/</i>]</p>
<dd> separate columns by a single character, default for CHAR is the &lt;TAB&gt; character without <code>-w</code> and &#8216;no char&#8217; with <code>-w</code>. <code>-s[CHAR]</code> turns off line truncation of all 3 column options (<code>-COLUMN</code>|-a <code>-COLUMN</code>|-m) except <code>-w</code> is set</p>
<dt><code>-S[STRING]</code>, <code>&#8211;sep-string</code>[=<i>,STRING/</i>]</p>
<dd> separate columns by STRING, without <code>-S</code>: Default separator &lt;TAB&gt; with <code>-J</code> and &lt;space&gt; otherwise (same as <code>-S</code>&quot; &quot;), no effect on column options</p>
<dt><code>-t</code>, <code>&#8211;omit-header</code></p>
<dd> omit page headers and trailers; implied if PAGE_LENGTH &lt;= 10</p>
<dt><code>-T</code>, <code>&#8211;omit-pagination</code></p>
<dd> omit page headers and trailers, eliminate any pagination by form feeds set in input files</p>
<dt><code>-v</code>, <code>&#8211;show-nonprinting</code></p>
<dd> use octal backslash notation</p>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>,PAGE_WIDTH/</i></p>
<dd> set page width to PAGE_WIDTH (72) characters for multiple text-column output only, <code>-s[char]</code> turns off (72)</p>
<dt><code>-W</code>, <code>&#8211;page-width</code>=<i>,PAGE_WIDTH/</i></p>
<dd> set page width to PAGE_WIDTH (72) characters always, truncate lines, except <code>-J</code> option is set, no interference with <code>-S</code> or <code>-s</code></p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>AUTHOR</h2>
<p> Written by Pete TerMaat and Roland Huebner.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/pr">https://www.gnu.org/software/coreutils/pr</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) pr invocation&#8217; </p>
<h2>Index</h2>
