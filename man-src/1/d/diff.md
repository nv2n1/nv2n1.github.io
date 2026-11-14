---
title: "diff(1)"
name: "diff"
section: "1"
letter: "d"
url: "/docs/linux/man/1-diff/"
description: "diff – compare files line by line"
---

<h2 class="name">NAME</h2>
<p> diff &#8211; compare files line by line </p>
<h2>SYNOPSIS</h2>
<p> <code>diff</code> [<i>OPTION</i>]&#8230; <i>FILES</i></p>
<h2>DESCRIPTION</h2>
<p> Compare FILES line by line. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>&#8211;normal</code></p>
<dd> output a normal diff (the default)</p>
<dt><code>-q</code>, <code>&#8211;brief</code></p>
<dd> report only when files differ</p>
<dt><code>-s</code>, <code>&#8211;report-identical-files</code></p>
<dd> report when two files are the same</p>
<dt><code>-c</code>, <code>-C</code> NUM, <code>&#8211;context</code>[=<i>NUM</i>]</p>
<dd> output NUM (default 3) lines of copied context</p>
<dt><code>-u</code>, <code>-U</code> NUM, <code>&#8211;unified</code>[=<i>NUM</i>]</p>
<dd> output NUM (default 3) lines of unified context</p>
<dt><code>-e</code>, <code>&#8211;ed</code></p>
<dd> output an ed script</p>
<dt><code>-n</code>, <code>&#8211;rcs</code></p>
<dd> output an RCS format diff</p>
<dt><code>-y</code>, <code>&#8211;side-by-side</code></p>
<dd> output in two columns</p>
<dt><code>-W</code>, <code>&#8211;width</code>=<i>NUM</i></p>
<dd> output at most NUM (default 130) print columns</p>
<dt><code>&#8211;left-column</code></p>
<dd> output only the left column of common lines</p>
<dt><code>&#8211;suppress-common-lines</code></p>
<dd> do not output common lines</p>
<dt><code>-p</code>, <code>&#8211;show-c-function</code></p>
<dd> show which C function each change is in</p>
<dt><code>-F</code>, <code>&#8211;show-function-line</code>=<i>RE</i></p>
<dd> show the most recent line matching RE</p>
<dt><code>&#8211;label</code> LABEL</p>
<dd> use LABEL instead of file name and timestamp (can be repeated)</p>
<dt><code>-t</code>, <code>&#8211;expand-tabs</code></p>
<dd> expand tabs to spaces in output</p>
<dt><code>-T</code>, <code>&#8211;initial-tab</code></p>
<dd> make tabs line up by prepending a tab</p>
<dt><code>&#8211;tabsize</code>=<i>NUM</i></p>
<dd> tab stops every NUM (default 8) print columns</p>
<dt><code>&#8211;suppress-blank-empty</code></p>
<dd> suppress space or tab before empty output lines</p>
<dt><code>-l</code>, <code>&#8211;paginate</code></p>
<dd> pass output through &#8216;pr&#8217; to paginate it</p>
<dt><code>-r</code>, <code>&#8211;recursive</code></p>
<dd> recursively compare any subdirectories found</p>
<dt><code>&#8211;no-dereference</code></p>
<dd> don&#8217;t follow symbolic links</p>
<dt><code>-N</code>, <code>&#8211;new-file</code></p>
<dd> treat absent files as empty</p>
<dt><code>&#8211;unidirectional-new-file</code></p>
<dd> treat absent first files as empty</p>
<dt><code>&#8211;ignore-file-name-case</code></p>
<dd> ignore case when comparing file names</p>
<dt><code>&#8211;no-ignore-file-name-case</code></p>
<dd> consider case when comparing file names</p>
<dt><code>-x</code>, <code>&#8211;exclude</code>=<i>PAT</i></p>
<dd> exclude files that match PAT</p>
<dt><code>-X</code>, <code>&#8211;exclude-from</code>=<i>FILE</i></p>
<dd> exclude files that match any pattern in FILE</p>
<dt><code>-S</code>, <code>&#8211;starting-file</code>=<i>FILE</i></p>
<dd> start with FILE when comparing directories</p>
<dt><code>&#8211;from-file</code>=<i>FILE1</i></p>
<dd> compare FILE1 to all operands; FILE1 can be a directory</p>
<dt><code>&#8211;to-file</code>=<i>FILE2</i></p>
<dd> compare all operands to FILE2; FILE2 can be a directory</p>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></p>
<dd> ignore case differences in file contents</p>
<dt><code>-E</code>, <code>&#8211;ignore-tab-expansion</code></p>
<dd> ignore changes due to tab expansion</p>
<dt><code>-Z</code>, <code>&#8211;ignore-trailing-space</code></p>
<dd> ignore white space at line end</p>
<dt><code>-b</code>, <code>&#8211;ignore-space-change</code></p>
<dd> ignore changes in the amount of white space</p>
<dt><code>-w</code>, <code>&#8211;ignore-all-space</code></p>
<dd> ignore all white space</p>
<dt><code>-B</code>, <code>&#8211;ignore-blank-lines</code></p>
<dd> ignore changes where lines are all blank</p>
<dt><code>-I</code>, <code>&#8211;ignore-matching-lines</code>=<i>RE</i></p>
<dd> ignore changes where all lines match RE</p>
<dt><code>-a</code>, <code>&#8211;text</code></p>
<dd> treat all files as text</p>
<dt><code>&#8211;strip-trailing-cr</code></p>
<dd> strip trailing carriage return on input</p>
<dt><code>-D</code>, <code>&#8211;ifdef</code>=<i>NAME</i></p>
<dd> output merged file with &#8216;#ifdef NAME&#8217; diffs</p>
<dt><code>&#8211;GTYPE-group-format</code>=<i>GFMT</i></p>
<dd> format GTYPE input groups with GFMT</p>
<dt><code>&#8211;line-format</code>=<i>LFMT</i></p>
<dd> format all input lines with LFMT</p>
<dt><code>&#8211;LTYPE-line-format</code>=<i>LFMT</i></p>
<dd> format LTYPE input lines with LFMT</p>
<dt>
<dd> These format options provide fine-grained control over the output</p>
<dt>
<dd> of diff, generalizing <code>-D</code>/&#8211;ifdef.</p>
<dt>LTYPE is &#8216;old&#8217;, &#8216;new&#8217;, or &#8216;unchanged&#8217;.</p>
<dd> GTYPE is LTYPE or &#8216;changed&#8217;.</p>
<dt>
<dd> GFMT (only) may contain:</p>
<dt>%&lt;</p>
<dd> lines from FILE1</p>
<dt>%&gt;</p>
<dd> lines from FILE2</p>
<dt>%=</p>
<dd> lines common to FILE1 and FILE2</p>
<dt>%[-][WIDTH][.[PREC]]{doxX}LETTER</p>
<dd> printf-style spec for LETTER</p>
<dt>
<dd> LETTERs are as follows for new group, lower case for old group:</p>
<dt>F</p>
<dd> first line number</p>
<dt>L</p>
<dd> last line number</p>
<dt>N</p>
<dd> number of lines = L-F+1</p>
<dt>E</p>
<dd> F-1</p>
<dt>M</p>
<dd> L+1</p>
<dt>%(A=B?T:E)</p>
<dd> if A equals B then T else E</p>
<dt>
<dd> LFMT (only) may contain:</p>
<dt>%L</p>
<dd> contents of line</p>
<dt>%l</p>
<dd> contents of line, excluding any trailing newline</p>
<dt>%[-][WIDTH][.[PREC]]{doxX}n</p>
<dd> printf-style spec for input line number</p>
<dt>
<dd> Both GFMT and LFMT may contain:</p>
<dt>%%</p>
<dd> %</p>
<dt>%c&#8217;C&#8217;</p>
<dd> the single character C</p>
<dt>%c&#8217;\OOO&#8217;</p>
<dd> the character with octal code OOO</p>
<dt>C</p>
<dd> the character C (other characters represent themselves)</p>
<dt><code>-d</code>, <code>&#8211;minimal</code></p>
<dd> try hard to find a smaller set of changes</p>
<dt><code>&#8211;horizon-lines</code>=<i>NUM</i></p>
<dd> keep NUM lines of the common prefix and suffix</p>
<dt><code>&#8211;speed-large-files</code></p>
<dd> assume large files and many scattered small changes</p>
<dt><code>&#8211;color</code>[=<i>WHEN</i>]</p>
<dd> color output; WHEN is &#8216;never&#8217;, &#8216;always&#8217;, or &#8216;auto&#8217;; plain <code>&#8211;color</code> means <code>&#8211;color=</code>&#8216;auto&#8217;</p>
<dt><code>&#8211;palette</code>=<i>PALETTE</i></p>
<dd> the colors to use when <code>&#8211;color</code> is active; PALETTE is a colon-separated list of terminfo capabilities</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> FILES are &#8216;FILE1 FILE2&#8217; or &#8216;DIR1 DIR2&#8217; or &#8216;DIR FILE&#8217; or &#8216;FILE DIR&#8217;. If <code>&#8211;from-file</code> or <code>&#8211;to-file</code> is given, there are no restrictions on FILE(s). If a FILE is &#8216;-&#8216;, read standard input. Exit status is 0 if inputs are the same, 1 if different, 2 if trouble.</p>
<h2>AUTHOR</h2>
<p> Written by Paul Eggert, Mike Haertel, David Hayes, Richard Stallman, and Len Tower.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to: bug-diffutils [at] gnu.org<br />
 GNU diffutils home page: &lt;<a rel="nofollow" href="https://www.gnu.org/software/diffutils/">https://www.gnu.org/software/diffutils/</a>&gt;<br />
 General help using GNU software: &lt;<a rel="nofollow" href="https://www.gnu.org/gethelp/">https://www.gnu.org/gethelp/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-wdiff/">wdiff</a>(1), <a href="/docs/linux/man/1-cmp/">cmp</a>(1), <a href="/docs/linux/man/1-diff3/">diff3</a>(1), <a href="/docs/linux/man/1-sdiff/">sdiff</a>(1), <a href="/docs/linux/man/1-patch/">patch</a>(1) </p>
<p> The full documentation for <code>diff</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>diff</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info diff</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
