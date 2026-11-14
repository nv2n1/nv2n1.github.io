---
title: "recode(1)"
name: "recode"
section: "1"
letter: "r"
url: "/docs/linux/man/1-recode/"
description: "recode – manual page for recode 3.6"
---

<h2>NAME</h2>
<p> recode &#8211; manual page for recode 3.6</p>
<h2>SYNOPSIS</h2>
<p> <code>lt-recode</code> [<i>OPTION</i>]&#8230; [ [<i>CHARSET</i>] <i>| REQUEST </i>[<i>FILE</i>]&#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> Free `recode&#8217; converts files between various character sets and surfaces. </p>
<p> If a long option shows an argument as mandatory, then it is mandatory for the equivalent short option also. Similarly for optional arguments.</p>
<h3>Listings:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;list</code>[=<i>FORMAT</i>]</p>
<dd> list one or all known charsets and aliases</p>
<dt><code>-k</code>, <code>&#8211;known</code>=<i>PAIRS</i></p>
<dd> restrict charsets according to known PAIRS list</p>
<dt><code>-h</code>, <code>&#8211;header[</code>=<i>[LN</i>/]NAME]</p>
<dd> write table NAME on stdout using LN, then exit</p>
<dt><code>-F</code>, <code>&#8211;freeze-tables</code></p>
<dd> write out a C module holding all tables</p>
<dt><code>-T</code>, <code>&#8211;find-subsets</code></p>
<dd> report all charsets being subset of others</p>
<dt><code>-C</code>, <code>&#8211;copyright</code></p>
<dd> display Copyright and copying conditions</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h3>Operation modes:</h3>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> explain sequence of steps and report progress</p>
<dt><code>-q</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</code></p>
<dd> inhibit messages about irreversible recodings</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> force recodings even when not reversible</p>
<dt><code>-t</code>, <code>&#8211;touch</code></p>
<dd> touch the recoded files after replacement</p>
<dt><code>-i</code>, <code>&#8211;sequence</code>=<i>files</i></p>
<dd> use intermediate files for sequencing passes</p>
<dt><code>&#8211;sequence</code>=<i>memory</i></p>
<dd> use memory buffers for sequencing passes</p>
<dt><code>-p</code>, <code>&#8211;sequence</code>=<i>pipe</i></p>
<dd> use pipe machinery for sequencing passes</dl>
<h3>Fine tuning:</h3>
<dl>
<dt><code>-s</code>, <code>&#8211;strict</code></p>
<dd> use strict mappings, even loose characters</p>
<dt><code>-d</code>, <code>&#8211;diacritics</code></p>
<dd> convert only diacritics or alike for HTML/LaTeX</p>
<dt><code>-S</code>, <code>&#8211;source</code>[=<i>LN</i>]</p>
<dd> limit recoding to strings and comments as for LN</p>
<dt><code>-c</code>, <code>&#8211;colons</code></p>
<dd> use colons instead of double quotes for diaeresis</p>
<dt><code>-g</code>, <code>&#8211;graphics</code></p>
<dd> approximate IBMPC rulers by ASCII graphics</p>
<dt><code>-x</code>, <code>&#8211;ignore</code>=<i>CHARSET</i></p>
<dd> ignore CHARSET while choosing a recoding path</dl>
<p> Option <code>-l</code> with no FORMAT nor CHARSET list available charsets and surfaces. FORMAT is `decimal&#8217;, `octal&#8217;, `hexadecimal&#8217; or `full&#8217; (or one of `dohf&#8217;). Unless DEFAULT_CHARSET is set in environment, CHARSET defaults to the locale dependent encoding, determined by LC_ALL, LC_CTYPE, LANG. With <code>-k</code>, possible before charsets are listed for the given after CHARSET, both being tabular charsets, with PAIRS of the form `BEF1:AFT1,BEF2:AFT2,&#8230;&#8217; and BEFs and AFTs being codes are given as decimal numbers. LN is some language, it may be `c&#8217;, `perl&#8217; or `po&#8217;; `c&#8217; is the default. </p>
<p> REQUEST is SUBREQUEST[,SUBREQUEST]&#8230;; SUBREQUEST is ENCODING[..ENCODING]&#8230; ENCODING is [CHARSET][/[SURFACE]]&#8230;; REQUEST often looks like BEFORE..AFTER, with BEFORE and AFTER being charsets. An omitted CHARSET implies the usual charset; an omitted [/SURFACE]&#8230; means the implied surfaces for CHARSET; a / with an empty surface name means no surfaces at all. See the manual. </p>
<p> If none of <code>-i</code> and <code>-p</code> are given, presume <code>-p</code> if no FILE, else <code>-i</code>. Each FILE is recoded over itself, destroying the original. If no FILE is specified, then act as a filter and recode stdin to stdout.</p>
<h2>AUTHOR</h2>
<p> Written by Franc,ois Pinard &lt;pinard [at] iro.umontreal.ca&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;recode-bugs [at] iro.umontreal.ca&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1990, 92, 93, 94, 96, 97, 99 Free Software Foundation, Inc.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>recode</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>recode</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info recode</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
