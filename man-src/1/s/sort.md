---
title: "sort(1)"
name: "sort"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sort/"
description: "sort – sort lines of text files"
---

<h2 class="name">NAME</h2>
<p> sort &#8211; sort lines of text files </p>
<h2>SYNOPSIS</h2>
<p> <code>sort</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;<br />
 <code>sort</code> [<i>,OPTION/</i>]&#8230; <i>,&#8211;files0-from=F/</i></p>
<h2>DESCRIPTION</h2>
<p> Write sorted concatenation of all FILE(s) to standard output. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too. Ordering options:</p>
<dl>
<dt><code>-b</code>, <code>&#8211;ignore-leading-blanks</code></p>
<dd> ignore leading blanks</p>
<dt><code>-d</code>, <code>&#8211;dictionary-order</code></p>
<dd> consider only blanks and alphanumeric characters</p>
<dt><code>-f</code>, <code>&#8211;ignore-case</code></p>
<dd> fold lower case to upper case characters</p>
<dt><code>-g</code>, <code>&#8211;general-numeric-sort</code></p>
<dd> compare according to general numerical value</p>
<dt><code>-i</code>, <code>&#8211;ignore-nonprinting</code></p>
<dd> consider only printable characters</p>
<dt><code>-M</code>, <code>&#8211;month-sort</code></p>
<dd> compare (unknown) &lt; &#8216;JAN&#8217; &lt; &#8230; &lt; &#8216;DEC&#8217;</p>
<dt><code>-h</code>, <code>&#8211;human-numeric-sort</code></p>
<dd> compare human readable numbers (e.g., 2K 1G)</p>
<dt><code>-n</code>, <code>&#8211;numeric-sort</code></p>
<dd> compare according to string numerical value</p>
<dt><code>-R</code>, <code>&#8211;random-sort</code></p>
<dd> shuffle, but group identical keys. See <a href="/docs/linux/man/1-shuf/">shuf</a>(1)</p>
<dt><code>&#8211;random-source</code>=<i>,FILE/</i></p>
<dd> get random bytes from FILE</p>
<dt><code>-r</code>, <code>&#8211;reverse</code></p>
<dd> reverse the result of comparisons</p>
<dt><code>&#8211;sort</code>=<i>,WORD/</i></p>
<dd> sort according to WORD: general-numeric <code>-g</code>, human-numeric <code>-h</code>, month <code>-M</code>, numeric <code>-n</code>, random <code>-R</code>, version <code>-V</code></p>
<dt><code>-V</code>, <code>&#8211;version-sort</code></p>
<dd> natural sort of (version) numbers within text</dl>
<p> Other options:</p>
<dl>
<dt><code>&#8211;batch-size</code>=<i>,NMERGE/</i></p>
<dd> merge at most NMERGE inputs at once; for more use temp files</p>
<dt><code>-c</code>, <code>&#8211;check</code>, <code>&#8211;check</code>=<i>,diagnose-first/</i></p>
<dd> check for sorted input; do not sort</p>
<dt><code>-C</code>, <code>&#8211;check</code>=<i>,quiet/</i>, <code>&#8211;check</code>=<i>,silent/</i></p>
<dd> like <code>-c</code>, but do not report first bad line</p>
<dt><code>&#8211;compress-program</code>=<i>,PROG/</i></p>
<dd> compress temporaries with PROG; decompress them with PROG <code>-d</code></p>
<dt><code>&#8211;debug</code></p>
<dd> annotate the part of the line used to sort, and warn about questionable usage to stderr</p>
<dt><code>&#8211;files0-from</code>=<i>,F/</i></p>
<dd> read input from the files specified by NUL-terminated names in file F; If F is &#8211; then read names from standard input</p>
<dt><code>-k</code>, <code>&#8211;key</code>=<i>,KEYDEF/</i></p>
<dd> sort via a key; KEYDEF gives location and type</p>
<dt><code>-m</code>, <code>&#8211;merge</code></p>
<dd> merge already sorted files; do not sort</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></p>
<dd> write result to FILE instead of standard output</p>
<dt><code>-s</code>, <code>&#8211;stable</code></p>
<dd> stabilize sort by disabling last-resort comparison</p>
<dt><code>-S</code>, <code>&#8211;buffer-size</code>=<i>,SIZE/</i></p>
<dd> use SIZE for main memory buffer</p>
<dt><code>-t</code>, <code>&#8211;field-separator</code>=<i>,SEP/</i></p>
<dd> use SEP instead of non-blank to blank transition</p>
<dt><code>-T</code>, <code>&#8211;temporary-directory</code>=<i>,DIR/</i></p>
<dd> use DIR for temporaries, not $TMPDIR or <i>,/tmp/</i>; multiple options specify multiple directories</p>
<dt><code>&#8211;parallel</code>=<i>,N/</i></p>
<dd> change the number of sorts run concurrently to N</p>
<dt><code>-u</code>, <code>&#8211;unique</code></p>
<dd> with <code>-c</code>, check for strict ordering; without <code>-c</code>, output only the first of an equal run</p>
<dt><code>-z</code>, <code>&#8211;zero-terminated</code></p>
<dd> line delimiter is NUL, not newline</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> KEYDEF is F[.C][OPTS][,F[.C][OPTS]] for start and stop position, where F is a field number and C a character position in the field; both are origin 1, and the stop position defaults to the line&#8217;s end. If neither <code>-t</code> nor <code>-b</code> is in effect, characters in a field are counted from the beginning of the preceding whitespace. OPTS is one or more single-letter ordering options [bdfgiMhnRrV], which override global ordering options for that key. If no key is given, use the entire line as the key. Use <code>&#8211;debug</code> to diagnose incorrect key usage. </p>
<p> SIZE may be followed by the following multiplicative suffixes: % 1% of memory, b 1, K 1024 (default), and so on for M, G, T, P, E, Z, Y. </p>
<p> *** WARNING *** The locale specified by the environment affects sort order. Set LC_ALL=C to get the traditional sort order that uses native byte values.</p>
<h2>AUTHOR</h2>
<p> Written by Mike Haertel and Paul Eggert.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-shuf/">shuf</a>(1), <a href="/docs/linux/man/1-uniq/">uniq</a>(1) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/sort">https://www.gnu.org/software/coreutils/sort</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) sort invocation&#8217; </p>
<h2>Index</h2>
