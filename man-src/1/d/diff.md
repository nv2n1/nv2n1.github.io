---

title: "diff(1)"
name: "diff"
section: "1"
letter: "d"
url: "/docs/linux/man/1-diff/"
description: "diff – compare files line by line"
---

<p> <code>diff</code> [<i>OPTION</i>]&#8230; <i>FILES</i></p>
<p> Compare FILES line by line. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>&#8211;normal</code></dt>
<dd> output a normal diff (the default)</dd>
<dt><code>-q</code>, <code>&#8211;brief</code></dt>
<dd> report only when files differ</dd>
<dt><code>-s</code>, <code>&#8211;report-identical-files</code></dt>
<dd> report when two files are the same</dd>
<dt><code>-c</code>, <code>-C</code> NUM, <code>&#8211;context</code>[=<i>NUM</i>]</dt>
<dd> output NUM (default 3) lines of copied context</dd>
<dt><code>-u</code>, <code>-U</code> NUM, <code>&#8211;unified</code>[=<i>NUM</i>]</dt>
<dd> output NUM (default 3) lines of unified context</dd>
<dt><code>-e</code>, <code>&#8211;ed</code></dt>
<dd> output an ed script</dd>
<dt><code>-n</code>, <code>&#8211;rcs</code></dt>
<dd> output an RCS format diff</dd>
<dt><code>-y</code>, <code>&#8211;side-by-side</code></dt>
<dd> output in two columns</dd>
<dt><code>-W</code>, <code>&#8211;width</code>=<i>NUM</i></dt>
<dd> output at most NUM (default 130) print columns</dd>
<dt><code>&#8211;left-column</code></dt>
<dd> output only the left column of common lines</dd>
<dt><code>&#8211;suppress-common-lines</code></dt>
<dd> do not output common lines</dd>
<dt><code>-p</code>, <code>&#8211;show-c-function</code></dt>
<dd> show which C function each change is in</dd>
<dt><code>-F</code>, <code>&#8211;show-function-line</code>=<i>RE</i></dt>
<dd> show the most recent line matching RE</dd>
<dt><code>&#8211;label</code> LABEL</dt>
<dd> use LABEL instead of file name and timestamp (can be repeated)</dd>
<dt><code>-t</code>, <code>&#8211;expand-tabs</code></dt>
<dd> expand tabs to spaces in output</dd>
<dt><code>-T</code>, <code>&#8211;initial-tab</code></dt>
<dd> make tabs line up by prepending a tab</dd>
<dt><code>&#8211;tabsize</code>=<i>NUM</i></dt>
<dd> tab stops every NUM (default 8) print columns</dd>
<dt><code>&#8211;suppress-blank-empty</code></dt>
<dd> suppress space or tab before empty output lines</dd>
<dt><code>-l</code>, <code>&#8211;paginate</code></dt>
<dd> pass output through &#8216;pr&#8217; to paginate it</dd>
<dt><code>-r</code>, <code>&#8211;recursive</code></dt>
<dd> recursively compare any subdirectories found</dd>
<dt><code>&#8211;no-dereference</code></dt>
<dd> don&#8217;t follow symbolic links</dd>
<dt><code>-N</code>, <code>&#8211;new-file</code></dt>
<dd> treat absent files as empty</dd>
<dt><code>&#8211;unidirectional-new-file</code></dt>
<dd> treat absent first files as empty</dd>
<dt><code>&#8211;ignore-file-name-case</code></dt>
<dd> ignore case when comparing file names</dd>
<dt><code>&#8211;no-ignore-file-name-case</code></dt>
<dd> consider case when comparing file names</dd>
<dt><code>-x</code>, <code>&#8211;exclude</code>=<i>PAT</i></dt>
<dd> exclude files that match PAT</dd>
<dt><code>-X</code>, <code>&#8211;exclude-from</code>=<i>FILE</i></dt>
<dd> exclude files that match any pattern in FILE</dd>
<dt><code>-S</code>, <code>&#8211;starting-file</code>=<i>FILE</i></dt>
<dd> start with FILE when comparing directories</dd>
<dt><code>&#8211;from-file</code>=<i>FILE1</i></dt>
<dd> compare FILE1 to all operands; FILE1 can be a directory</dd>
<dt><code>&#8211;to-file</code>=<i>FILE2</i></dt>
<dd> compare all operands to FILE2; FILE2 can be a directory</dd>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></dt>
<dd> ignore case differences in file contents</dd>
<dt><code>-E</code>, <code>&#8211;ignore-tab-expansion</code></dt>
<dd> ignore changes due to tab expansion</dd>
<dt><code>-Z</code>, <code>&#8211;ignore-trailing-space</code></dt>
<dd> ignore white space at line end</dd>
<dt><code>-b</code>, <code>&#8211;ignore-space-change</code></dt>
<dd> ignore changes in the amount of white space</dd>
<dt><code>-w</code>, <code>&#8211;ignore-all-space</code></dt>
<dd> ignore all white space</dd>
<dt><code>-B</code>, <code>&#8211;ignore-blank-lines</code></dt>
<dd> ignore changes where lines are all blank</dd>
<dt><code>-I</code>, <code>&#8211;ignore-matching-lines</code>=<i>RE</i></dt>
<dd> ignore changes where all lines match RE</dd>
<dt><code>-a</code>, <code>&#8211;text</code></dt>
<dd> treat all files as text</dd>
<dt><code>&#8211;strip-trailing-cr</code></dt>
<dd> strip trailing carriage return on input</dd>
<dt><code>-D</code>, <code>&#8211;ifdef</code>=<i>NAME</i></dt>
<dd> output merged file with &#8216;#ifdef NAME&#8217; diffs</dd>
<dt><code>&#8211;GTYPE-group-format</code>=<i>GFMT</i></dt>
<dd> format GTYPE input groups with GFMT</dd>
<dt><code>&#8211;line-format</code>=<i>LFMT</i></dt>
<dd> format all input lines with LFMT</dd>
<dt><code>&#8211;LTYPE-line-format</code>=<i>LFMT</i></dt>
<dd> format LTYPE input lines with LFMT</dd>
<dt>
</dt><dd> These format options provide fine-grained control over the output</dd>
<dt>
</dt><dd> of diff, generalizing <code>-D</code>/&#8211;ifdef.</dd>
<dt>LTYPE is &#8216;old&#8217;, &#8216;new&#8217;, or &#8216;unchanged&#8217;.</dt>
<dd> GTYPE is LTYPE or &#8216;changed&#8217;.</dd>
<dt>
</dt><dd> GFMT (only) may contain:</dd>
<dt>%&lt;</dt>
<dd> lines from FILE1</dd>
<dt>%&gt;</dt>
<dd> lines from FILE2</dd>
<dt>%=</dt>
<dd> lines common to FILE1 and FILE2</dd>
<dt>%[-][WIDTH][.[PREC]]{doxX}LETTER</dt>
<dd> printf-style spec for LETTER</dd>
<dt>
</dt><dd> LETTERs are as follows for new group, lower case for old group:</dd>
<dt>F</dt>
<dd> first line number</dd>
<dt>L</dt>
<dd> last line number</dd>
<dt>N</dt>
<dd> number of lines = L-F+1</dd>
<dt>E</dt>
<dd> F-1</dd>
<dt>M</dt>
<dd> L+1</dd>
<dt>%(A=B?T:E)</dt>
<dd> if A equals B then T else E</dd>
<dt>
</dt><dd> LFMT (only) may contain:</dd>
<dt>%L</dt>
<dd> contents of line</dd>
<dt>%l</dt>
<dd> contents of line, excluding any trailing newline</dd>
<dt>%[-][WIDTH][.[PREC]]{doxX}n</dt>
<dd> printf-style spec for input line number</dd>
<dt>
</dt><dd> Both GFMT and LFMT may contain:</dd>
<dt>%%</dt>
<dd> %</dd>
<dt>%c&#8217;C&#8217;</dt>
<dd> the single character C</dd>
<dt>%c&#8217;\OOO&#8217;</dt>
<dd> the character with octal code OOO</dd>
<dt>C</dt>
<dd> the character C (other characters represent themselves)</dd>
<dt><code>-d</code>, <code>&#8211;minimal</code></dt>
<dd> try hard to find a smaller set of changes</dd>
<dt><code>&#8211;horizon-lines</code>=<i>NUM</i></dt>
<dd> keep NUM lines of the common prefix and suffix</dd>
<dt><code>&#8211;speed-large-files</code></dt>
<dd> assume large files and many scattered small changes</dd>
<dt><code>&#8211;color</code>[=<i>WHEN</i>]</dt>
<dd> color output; WHEN is &#8216;never&#8217;, &#8216;always&#8217;, or &#8216;auto&#8217;; plain <code>&#8211;color</code> means <code>&#8211;color=</code>&#8216;auto&#8217;</dd>
<dt><code>&#8211;palette</code>=<i>PALETTE</i></dt>
<dd> the colors to use when <code>&#8211;color</code> is active; PALETTE is a colon-separated list of terminfo capabilities</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
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
</dt><dd> <code>info diff</code></dd></dl>
<p> should give you access to the complete manual. </p>
