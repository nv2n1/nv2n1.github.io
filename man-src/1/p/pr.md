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
<dt>+FIRST_PAGE[:LAST_PAGE], <code>&#8211;pages</code>=<i>,FIRST_PAGE[/</i>:LAST_PAGE]</dt>
<dd> begin [stop] printing with page FIRST_[LAST_]PAGE</dd>
<dt><code>-COLUMN</code>, <code>&#8211;columns</code>=<i>,COLUMN/</i></dt>
<dd> output COLUMN columns and print columns down, unless <code>-a</code> is used. Balance number of lines in the columns on each page</dd>
<dt><code>-a</code>, <code>&#8211;across</code></dt>
<dd> print columns across rather than down, used together with <code>-COLUMN</code></dd>
<dt><code>-c</code>, <code>&#8211;show-control-chars</code></dt>
<dd> use hat notation (^G) and octal backslash notation</dd>
<dt><code>-d</code>, <code>&#8211;double-space</code></dt>
<dd> double space the output</dd>
<dt><code>-D</code>, <code>&#8211;date-format</code>=<i>,FORMAT/</i></dt>
<dd> use FORMAT for the header date</dd>
<dt><code>-e[CHAR[WIDTH]]</code>, <code>&#8211;expand-tabs</code>[=<i>,CHAR[WIDTH]/</i>]</dt>
<dd> expand input CHARs (TABs) to tab WIDTH (8)</dd>
<dt><code>-F</code>, <code>-f</code>, <code>&#8211;form-feed</code></dt>
<dd> use form feeds instead of newlines to separate pages (by a 3-line page header with <code>-F</code> or a 5-line header and trailer without <code>-F</code>)</dd>
<dt><code>-h</code>, <code>&#8211;header</code>=<i>,HEADER/</i></dt>
<dd> use a centered HEADER instead of filename in page header, <code>-h</code> &quot;&quot; prints a blank line, don&#8217;t use <code>-h</code>&quot;&quot;</dd>
<dt><code>-i[CHAR[WIDTH]]</code>, <code>&#8211;output-tabs</code>[=<i>,CHAR[WIDTH]/</i>]</dt>
<dd> replace spaces with CHARs (TABs) to tab WIDTH (8)</dd>
<dt><code>-J</code>, <code>&#8211;join-lines</code></dt>
<dd> merge full lines, turns off <code>-W</code> line truncation, no column alignment, <code>&#8211;sep-string</code>[=<i>,STRING/</i>] sets separators</dd>
<dt><code>-l</code>, <code>&#8211;length</code>=<i>,PAGE_LENGTH/</i></dt>
<dd> set the page length to PAGE_LENGTH (66) lines (default number of lines of text 56, and with <code>-F</code> 63). implies <code>-t</code> if PAGE_LENGTH &lt;= 10</dd>
<dt><code>-m</code>, <code>&#8211;merge</code></dt>
<dd> print all files in parallel, one in each column, truncate lines, but join lines of full length with <code>-J</code></dd>
<dt><code>-n[SEP[DIGITS]]</code>, <code>&#8211;number-lines</code>[=<i>,SEP[DIGITS]/</i>]</dt>
<dd> number lines, use DIGITS (5) digits, then SEP (TAB), default counting starts with 1st line of input file</dd>
<dt><code>-N</code>, <code>&#8211;first-line-number</code>=<i>,NUMBER/</i></dt>
<dd> start counting with NUMBER at 1st line of first page printed (see +FIRST_PAGE)</dd>
<dt><code>-o</code>, <code>&#8211;indent</code>=<i>,MARGIN/</i></dt>
<dd> offset each line with MARGIN (zero) spaces, do not affect <code>-w</code> or <code>-W</code>, MARGIN will be added to PAGE_WIDTH</dd>
<dt><code>-r</code>, <code>&#8211;no-file-warnings</code></dt>
<dd> omit warning when a file cannot be opened</dd>
<dt><code>-s[CHAR]</code>, <code>&#8211;separator</code>[=<i>,CHAR/</i>]</dt>
<dd> separate columns by a single character, default for CHAR is the &lt;TAB&gt; character without <code>-w</code> and &#8216;no char&#8217; with <code>-w</code>. <code>-s[CHAR]</code> turns off line truncation of all 3 column options (<code>-COLUMN</code>|-a <code>-COLUMN</code>|-m) except <code>-w</code> is set</dd>
<dt><code>-S[STRING]</code>, <code>&#8211;sep-string</code>[=<i>,STRING/</i>]</dt>
<dd> separate columns by STRING, without <code>-S</code>: Default separator &lt;TAB&gt; with <code>-J</code> and &lt;space&gt; otherwise (same as <code>-S</code>&quot; &quot;), no effect on column options</dd>
<dt><code>-t</code>, <code>&#8211;omit-header</code></dt>
<dd> omit page headers and trailers; implied if PAGE_LENGTH &lt;= 10</dd>
<dt><code>-T</code>, <code>&#8211;omit-pagination</code></dt>
<dd> omit page headers and trailers, eliminate any pagination by form feeds set in input files</dd>
<dt><code>-v</code>, <code>&#8211;show-nonprinting</code></dt>
<dd> use octal backslash notation</dd>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>,PAGE_WIDTH/</i></dt>
<dd> set page width to PAGE_WIDTH (72) characters for multiple text-column output only, <code>-s[char]</code> turns off (72)</dd>
<dt><code>-W</code>, <code>&#8211;page-width</code>=<i>,PAGE_WIDTH/</i></dt>
<dd> set page width to PAGE_WIDTH (72) characters always, truncate lines, except <code>-J</code> option is set, no interference with <code>-S</code> or <code>-s</code></dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
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
