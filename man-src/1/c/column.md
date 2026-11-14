---
title: "column(1)"
name: "column"
section: "1"
letter: "c"
url: "/docs/linux/man/1-column/"
description: "column – columnate lists"
---

<h2 class="name">NAME</h2>
<p> column &#8211; columnate lists </p>
<h2>SYNOPSIS</h2>
<p> <code>column</code> [options] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <code>column</code> utility formats its input into multiple columns. The util support three modes: </p>
<p> <code>columns are filled before rows</code></p>
<dl>
<dt>
<dd> This is the default mode (required by backward compatibility).</dl>
<p> <code>rows are filled before columns</code></p>
<dl>
<dt>
<dd> This mode is enabled by option <code>-x, &#8211;fillrows</code></dl>
<p> <code>table</code></p>
<dl>
<dt>
<dd> Determine the number of columns the input contains and create a table. This mode is enabled by option <code>-t, &#8211;table</code> and columns formatting is possible to modify by <code>&#8211;table-</code>* options. Use this mode if not sure.</dl>
<p> Input is taken from <i>file</i>, or otherwise from standard input. Empty lines are ignored and all invalid multibyte sequences are encoded by x&lt;hex&gt; convention.</p>
<h2>OPTIONS</h2>
<p> The argument <i>columns</i> for <code>&#8211;table-</code>* options is a comma separated list of the column names as defined by <code>&#8211;table-columns</code> or it&#8217;s column number in order as specified by input. It&#8217;s possible to mix names and numbers. The special placeholder &#8216;0&#8217; (e.g. -R0) may be used to specify all columns. </p>
<p> <code>-J, &#8211;json</code></p>
<dl>
<dt>
<dd> Use JSON output format to print the table, the option <code>&#8211;table-columns</code> is required and the option <code>&#8211;table-name</code> is recommended.</dl>
<p> <code>-c, &#8211;output-width</code> <i>width</i></p>
<dl>
<dt>
<dd> Output is formatted to a width specified as number of characters. The original name of this option is <code>&#8211;columns</code>; this name is deprecated since v2.30. Note that input longer than <i>width</i> is not truncated by default.</dl>
<p> <code>-d, &#8211;table-noheadings</code></p>
<dl>
<dt>
<dd> Do not print header. This option allows the use of logical column names on the command line, but keeps the header hidden when printing the table.</dl>
<p> <code>-o, &#8211;output-separator</code> <i>string</i></p>
<dl>
<dt>
<dd> Specify the columns delimiter for table output (default is two spaces).</dl>
<p> <code>-s, &#8211;separator</code> <i>separators</i></p>
<dl>
<dt>
<dd> Specify the possible input item delimiters (default is whitespace).</dl>
<p> <code>-t, &#8211;table</code></p>
<dl>
<dt>
<dd> Determine the number of columns the input contains and create a table. Columns are delimited with whitespace, by default, or with the characters supplied using the <code>&#8211;output-separator</code> option. Table output is useful for pretty-printing.</dl>
<p> <code>-N, &#8211;table-columns</code> <i>names</i></p>
<dl>
<dt>
<dd> Specify the columns names by comma separated list of names. The names are used for the table header or to address column in option arguments.</dl>
<p> <code>-l, &#8211;table-columns-limit</code> <i>number</i></p>
<dl>
<dt>
<dd> Specify maximal number of the input columns. The last column will contain all remaining line data if the limit is smaller than the number of the columns in the input data.</dl>
<p> <code>-R, &#8211;table-right</code> <i>columns</i></p>
<dl>
<dt>
<dd> Right align text in the specified columns.</dl>
<p> <code>-T, &#8211;table-truncate</code> <i>columns</i></p>
<dl>
<dt>
<dd> Specify columns where text can be truncated when necessary, otherwise very long table entries may be printed on multiple lines.</dl>
<p> <code>-E, &#8211;table-noextreme</code> <i>columns</i></p>
<dl>
<dt>
<dd> Specify columns where is possible to ignore unusually long (longer than average) cells when calculate column width. The option has impact to the width calculation and table formatting, but the printed text is not affected. </p>
<p> The option is used for the last visible column by default.</dl>
<p> <code>-e, &#8211;table-header-repeat</code></p>
<dl>
<dt>
<dd> Print header line for each page.</dl>
<p> <code>-W, &#8211;table-wrap</code> <i>columns</i></p>
<dl>
<dt>
<dd> Specify columns where is possible to use multi-line cell for long text when necessary.</dl>
<p> <code>-H, &#8211;table-hide</code> <i>columns</i></p>
<dl>
<dt>
<dd> Don&#8217;t print specified columns. The special placeholder &#8216;-&#8216; may be used to hide all unnamed columns (see <code>&#8211;table-columns</code>).</dl>
<p> <code>-O, &#8211;table-order</code> <i>columns</i></p>
<dl>
<dt>
<dd> Specify columns order on output.</dl>
<p> <code>-n, &#8211;table-name</code> <i>name</i></p>
<dl>
<dt>
<dd> Specify the table name used for JSON output. The default is &quot;table&quot;.</dl>
<p> <code>-L, &#8211;keep-empty-lines</code></p>
<dl>
<dt>
<dd> Preserve whitespace-only lines in the input. The default is ignore empty lines at all. This option&#8217;s original name was <code>&#8211;table-empty-lines</code> but is now deprecated because it gives the false impression that the option only applies to table mode.</dl>
<p> <code>-r, &#8211;tree</code> <i>column</i></p>
<dl>
<dt>
<dd> Specify column to use tree-like output. Note that the circular dependencies and other anomalies in child and parent relation are silently ignored.</dl>
<p> <code>-i, &#8211;tree-id</code> <i>column</i></p>
<dl>
<dt>
<dd> Specify column with line ID to create child-parent relation.</dl>
<p> <code>-p, &#8211;tree-parent</code> <i>column</i></p>
<dl>
<dt>
<dd> Specify column with parent ID to create child-parent relation.</dl>
<p> <code>-x, &#8211;fillrows</code></p>
<dl>
<dt>
<dd> Fill rows before filling columns.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>ENVIRONMENT</h2>
<p> The environment variable <code>COLUMNS</code> is used to determine the size of the screen if no other information is available.</p>
<h2>HISTORY</h2>
<p> The column command appeared in 4.3BSD-Reno.</p>
<h2>BUGS</h2>
<p> Version 2.23 changed the <code>-s</code> option to be non-greedy, for example: </p>
<dl>
<dt>
<dd>
<pre>
printf &quot;a:b:c
1::3
&quot; | column -t -s ':'
</pre>
</dl>
<p> Old output: </p>
<dl>
<dt>
<dd>
<pre>
a  b  c
1  3
</pre>
</dl>
<p> New output (since util-linux 2.23): </p>
<dl>
<dt>
<dd>
<pre>
a  b  c
1     3
</pre>
</dl>
<p> Historical versions of this tool indicated that &quot;rows are filled before columns&quot; by default, and that the <code>-x</code> option reverses this. This wording did not reflect the actual behavior, and it has since been corrected (see above). Other implementations of <code>column</code> may continue to use the older documentation, but the behavior should be identical in any case.</p>
<h2>EXAMPLES</h2>
<p> Print fstab with header line and align number to the right: </p>
<dl>
<dt>
<dd>
<pre>
sed 's/#.*//' /etc/fstab | column --table --table-columns SOURCE,TARGET,TYPE,OPTIONS,PASS,FREQ --table-right PASS,FREQ
</pre>
</dl>
<p> Print fstab and hide unnamed columns: </p>
<dl>
<dt>
<dd>
<pre>
sed 's/#.*//' /etc/fstab | column --table --table-columns SOURCE,TARGET,TYPE --table-hide -
</pre>
</dl>
<p> Print a tree: </p>
<dl>
<dt>
<dd>
<pre>
echo -e '1 0 A
2 1 AA
3 1 AB
4 2 AAA
5 2 AAB' | column --tree-id 1 --tree-parent 2 --tree 3
1  0  A
2  1  |-AA
4  2  | |-AAA
5  2  | `-AAB
3  1  `-AB
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-colrm/">colrm</a></code>(1), <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), <code><a href="/docs/linux/man/1-paste/">paste</a></code>(1), <code><a href="/docs/linux/man/1-sort/">sort</a></code>(1)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>column</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
