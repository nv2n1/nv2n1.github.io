---
title: "numfmt(1)"
name: "numfmt"
section: "1"
letter: "n"
url: "/docs/linux/man/1-numfmt/"
description: "numfmt – Convert numbers from/to human-readable strings"
---

<h2 class="name">NAME</h2>
<p> numfmt &#8211; Convert numbers from/to human-readable strings </p>
<h2>SYNOPSIS</h2>
<p> <code>numfmt</code> [<i>,OPTION/</i>]&#8230; [<i>,NUMBER/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Reformat NUMBER(s), or the numbers from standard input if none are specified. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>&#8211;debug</code></p>
<dd> print warnings about invalid input</p>
<dt><code>-d</code>, <code>&#8211;delimiter</code>=<i>,X/</i></p>
<dd> use X instead of whitespace for field delimiter</p>
<dt><code>&#8211;field</code>=<i>,FIELDS/</i></p>
<dd> replace the numbers in these input fields (default=1) see FIELDS below</p>
<dt><code>&#8211;format</code>=<i>,FORMAT/</i></p>
<dd> use printf style floating-point FORMAT; see FORMAT below for details</p>
<dt><code>&#8211;from</code>=<i>,UNIT/</i></p>
<dd> auto-scale input numbers to UNITs; default is &#8216;none&#8217;; see UNIT below</p>
<dt><code>&#8211;from-unit</code>=<i>,N/</i></p>
<dd> specify the input unit size (instead of the default 1)</p>
<dt><code>&#8211;grouping</code></p>
<dd> use locale-defined grouping of digits, e.g. 1,000,000 (which means it has no effect in the C/POSIX locale)</p>
<dt><code>&#8211;header</code>[=<i>,N/</i>]</p>
<dd> print (without converting) the first N header lines; N defaults to 1 if not specified</p>
<dt><code>&#8211;invalid</code>=<i>,MODE/</i></p>
<dd> failure mode for invalid numbers: MODE can be: abort (default), fail, warn, ignore</p>
<dt><code>&#8211;padding</code>=<i>,N/</i></p>
<dd> pad the output to N characters; positive N will right-align; negative N will left-align; padding is ignored if the output is wider than N; the default is to automatically pad if a whitespace is found</p>
<dt><code>&#8211;round</code>=<i>,METHOD/</i></p>
<dd> use METHOD for rounding when scaling; METHOD can be: up, down, from-zero (default), towards-zero, nearest</p>
<dt><code>&#8211;suffix</code>=<i>,SUFFIX/</i></p>
<dd> add SUFFIX to output numbers, and accept optional SUFFIX in input numbers</p>
<dt><code>&#8211;to</code>=<i>,UNIT/</i></p>
<dd> auto-scale output numbers to UNITs; see UNIT below</p>
<dt><code>&#8211;to-unit</code>=<i>,N/</i></p>
<dd> the output unit size (instead of the default 1)</p>
<dt><code>-z</code>, <code>&#8211;zero-terminated</code></p>
<dd> line delimiter is NUL, not newline</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h3>UNIT options:</h3>
<dl>
<dt>none</p>
<dd> no auto-scaling is done; suffixes will trigger an error</p>
<dt>auto</p>
<dd> accept optional single/two letter suffix:</p>
<dt>
<dd> 1K = 1000, 1Ki = 1024, 1M = 1000000, 1Mi = 1048576,</p>
<dt>si</p>
<dd> accept optional single letter suffix:</p>
<dt>
<dd> 1K = 1000, 1M = 1000000, &#8230;</p>
<dt>iec</p>
<dd> accept optional single letter suffix:</p>
<dt>
<dd> 1K = 1024, 1M = 1048576, &#8230;</p>
<dt>iec-i</p>
<dd> accept optional two-letter suffix:</p>
<dt>
<dd> 1Ki = 1024, 1Mi = 1048576, &#8230;</dl>
<h3>FIELDS supports <a href="/docs/linux/man/1-cut/">cut</a>(1) style field ranges:</h3>
<dl>
<dt>N</p>
<dd> N&#8217;th field, counted from 1</p>
<dt>N-</p>
<dd> from N&#8217;th field, to end of line</p>
<dt>N-M</p>
<dd> from N&#8217;th to M&#8217;th field (inclusive)</p>
<dt><code>-M</code></p>
<dd> from first to M&#8217;th field (inclusive)</p>
<dt>&#8211;</p>
<dd> all fields</dl>
<p> Multiple fields/ranges can be separated with commas </p>
<p> FORMAT must be suitable for printing one floating-point argument &#8216;%f&#8217;. Optional quote (%&#8217;f) will enable <code>&#8211;grouping</code> (if supported by current locale). Optional width value (%10f) will pad output. Optional zero (%010f) width will zero pad the number. Optional negative values (%-10f) will left align. Optional precision (%.1f) will override the input determined precision. </p>
<p> Exit status is 0 if all input numbers were successfully converted. By default, numfmt will stop at the first conversion error with exit status 2. With <code>&#8211;invalid=</code>&#8216;fail&#8217; a warning is printed for each conversion error and the exit status is 2. With <code>&#8211;invalid=</code>&#8216;warn&#8217; each conversion error is diagnosed, but the exit status is 0. With <code>&#8211;invalid=</code>&#8216;ignore&#8217; conversion errors are not diagnosed and the exit status is 0.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> <tt>$ numfmt --to=si 1000</tt></p>
<dt>
<dd> -&gt; &quot;1.0K&quot;</p>
<dt>
<dd> <tt>$ numfmt --to=iec 2048</tt></p>
<dt>
<dd> -&gt; &quot;2.0K&quot;</p>
<dt>
<dd> <tt>$ numfmt --to=iec-i 4096</tt></p>
<dt>
<dd> -&gt; &quot;4.0Ki&quot;</p>
<dt>
<dd> <tt>$ echo 1K | numfmt --from=si</tt></p>
<dt>
<dd> -&gt; &quot;1000&quot;</p>
<dt>
<dd> <tt>$ echo 1K | numfmt --from=iec</tt></p>
<dt>
<dd> -&gt; &quot;1024&quot;</p>
<dt>
<dd> <tt>$ df -B1 | numfmt --header --field 2-4 --to=si</tt><br />
 <tt>$ ls -l | numfmt --header --field 5 --to=iec</tt><br />
 <tt>$ ls -lh | numfmt --header --field 5 --from=iec --padding=10</tt><br />
 <tt>$ ls -lh | numfmt --header --field 5 --from=iec --format %10f</tt></dl>
<h2>AUTHOR</h2>
<p> Written by Assaf Gordon.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/numfmt">https://www.gnu.org/software/coreutils/numfmt</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) numfmt invocation&#8217; </p>
<h2>Index</h2>
