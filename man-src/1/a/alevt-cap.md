---
title: "alevt-cap(1)"
name: "alevt-cap"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alevt-cap/"
description: "alevt-cap – simple capture of teletext pages"
---

<h2>NAME</h2>
<p> alevt-cap &#8211; simple capture of teletext pages </p>
<h2>SYNOPSIS</h2>
<p> <code>alevt-cap</code> [<i>options</i>] <i>ppp</i>[<i>.ss</i>] <i>&#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>alevt-cap</code> is a simple program to capture teletext pages and write them to disk. You just give it a list of pages to fetch and it will save them. Nothing fancy like time-outs, page ranges, or channel name detection is supported. Though, it supports different file formats &#8211; at the moment ascii, ansi (ascii with color escape sequences), html, png, and ppm. </p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-name</code><i>&nbsp;<wbr>filename</i></p>
<dd> Gives the filename under which the pages should be saved. It may contain a couple of %-sequences (see below). (default: ttext-%s.%e)</p>
<dt><code>-format</code><i>&nbsp;<wbr>format-specifier</i></p>
<dd> Sets the file format used to save pages (see below). (default: ascii)</p>
<dt><code>-format</code><i>&nbsp;<wbr>list|help</i></p>
<dd> Lists all known file formats and their options.</p>
<dt><code>-vbi</code><i>&nbsp;<wbr>device</i></p>
<dd> Use the given device name (default: /dev/vbi0).</p>
<dt><code>-finetune</code><i>&nbsp;<wbr>-4..4|auto</i></p>
<dd> Specify the fine tuning for the decoder. For the right value play with <code>alevt</code>. Default: 1.</p>
<dt><code>-timeout</code><i>&nbsp;<wbr>seconds</i></p>
<dd> If the pages cannot be captured in <i>seconds</i>, the program terminates with exit status 1 after saving the already captured pages. The default is to wait forever.</p>
<dt><code>-charset</code><i>&nbsp;<wbr>latin-1|latin-2|russian</i></p>
<dd> Selects the character set to use. Characters not present in the selected set are replaced by similar looking symbols. (default: latin-1)</p>
<dt><code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version of program.</dl>
<p> Every non-option argument is taken as a page number. Subpages may be given in the form <i>ppp</i><code>.</code><i>ss</i> where <i>ppp</i> is the page number and <i>ss</i> is the subpage number. If no subpage is specified, the first transmitted subpage of that page is taken. The page is saved with the prior given format and name. </p>
<h3>Filenames</h3>
<p> The filename may contain %-sequences. The following sequences are defined:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>%%</code></p>
<dd> a single % sign.</p>
<dt><code>%e</code></p>
<dd> the default extension of the selected output format.</p>
<dt><code>%p</code></p>
<dd> the page number and an optional subpage number.</p>
<dt><code>%P</code></p>
<dd> the page number.</p>
<dt><code>%S</code></p>
<dd> the subpage number.</p>
<dt><code>%s</code></p>
<dd> the page number as given on the command line.</dl>
</dl>
<p> Between the % sign and the letter you can give a field width to which the replacement string should be padded. </p>
<h3>Format specifiers</h3>
<p> The output format and associated options are given by the format specifier. It is made up of one or more comma separated words. The first word selects the output format and the others are options for that format. There are common options valid for all output formats and format specific (private) ones. Some options have the form of an assignment. The order of the options is free. Only the format name itself must be the first word. An example:</p>
<dl>
<dt><code>ansi,reveal,bg=none</code></p>
<dd> The <code>ansi</code> is the format and <code>reveal</code>, and <code>bg=none</code> are options.</dl>
<p> At the moment there are only two common options: <code>reveal</code>, and <code>hide</code>. They control whether the hidden characters present in a page should be shown in the output or not. The default is <code>hide</code>. </p>
<p> The special format string <code>list</code> (or <code>help</code>) will give you a list of all supported output formats and their options. </p>
<p> (The <code>ansi</code> format is an alias for <code>ascii,color</code>.) </p>
<h2>DIAGNOSTICS</h2>
<p> If the program timed out and some pages are missing the exit status is 1. On fatal errors the exit status is 2. </p>
<h2>NOTE</h2>
<p> Before starting this program, you have to set the TV channel with another program like <code>xawtv</code> of <code>set-tv</code>. </p>
<h2>FILES</h2>
<p> <i>/dev/vbi*</i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="//www.systutorials.com/docs/linux/man/1x-alevt/">alevt</a></code>(1x), <code><a href="/docs/linux/man/1-alevt-date/">alevt-date</a></code>(1), </p>
<h2>BUGS</h2>
<p> If you give a page number that is never transmitted the program will not terminate. </p>
<p> Bug reports to &lt;froese [at] gmx.de&gt;. </p>
<h2>Index</h2>
