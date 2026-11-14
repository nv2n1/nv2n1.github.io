---
title: "columns(1)"
name: "columns"
section: "1"
letter: "c"
url: "/docs/linux/man/1-columns/"
description: "columns – Columnize Input Text"
---

<h2 class="name">NAME</h2>
<p> columns &#8211; Columnize Input Text </p>
<h2>SYNOPSIS</h2>
<p> <code>columns</code> [<code>&#8211;</code><i>flag</i> [<i>value</i>]]&#8230; [<code>&#8212;</code><i>opt-name</i>[[=| ]<i>value</i>]]&#8230; </p>
<p> All arguments must be options.</p>
<h2>DESCRIPTION</h2>
<p> There is no description for this command.</p>
<h2>OPTIONS</h2>
<h3>Specify the output dimensions</h3>
<dl>
<dt><code>-W</code> <i>num</i>, <code>&#8211;width</code>=<i>num</i></p>
<dd> Maximum Line Width. This option takes an integer number as its argument. The value of <i>num</i> is constrained to being: </p>
<pre>
in the range  16 through 4095
</pre>
<p> The default <i>num</i> for this option is:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>79 </p>
<p> This option specifies the full width of the output line, including any start-of-line indentation. The output will fill each line as completely as possible, unless the column width has been explicitly specified. If the maximum width is less than the length of the widest input, you will get a single column of output.</p>
<dt><code>-c</code> <i>count</i>, <code>&#8211;columns</code>=<i>count</i></p>
<dd> Desired number of columns. This option takes an integer number as its argument. The value of <i>count</i> is constrained to being: </p>
<pre>
in the range  1 through 2048
</pre>
<p> The default <i>count</i> for this option is:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>0 </p>
<p> Use this option to specify exactly how many columns to produce. If that many columns will not fit within <code>line_width</code>, then the count will be reduced to the number that fit.</p>
<dt><code>-w</code> <i>num</i>, <code>&#8211;col-width</code>=<i>num</i></p>
<dd> Set width of each column. This option takes an integer number as its argument. The value of <i>num</i> is constrained to being: </p>
<pre>
in the range  1 through 2048
</pre>
<p> The default <i>num</i> for this option is:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>0 </p>
<p> Use this option to specify exactly how many characters are to be allocated for each column. If it is narrower than the widest entry, it will be over-ridden with the required width.</p>
<dt><code>&#8211;tab-width</code>=<i>num</i></p>
<dd> tab width. This option takes an integer number as its argument. The default <i>num</i> for this option is:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>8 </p>
<p> If an indentation string contains tabs, then this value is used to compute the ending column of the prefix string.</dl>
<h3>Specify how to lay out the text</h3>
<dl>
<dt><code>&#8211;spread</code>=<i>num</i></p>
<dd> maximum spread added to column width. This option takes an integer number as its argument. The value of <i>num</i> is constrained to being: </p>
<pre>
in the range  1 through 1024
</pre>
<p> The default <i>num</i> for this option is:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>0 </p>
<p> Use this option to specify exactly how many characters may be added to each column. It allows you to prevent columns from becoming too far apart. Without this option, <i>columns</i> will attempt to widen columns to fill the full width.</p>
<dt><code>&#8211;fill</code></p>
<dd> Fill lines with input. This option must not appear in combination with any of the following options: spread, col_width, by_columns. </p>
<p> Instead of columnizing the input text, fill the output lines with the input lines. Blank lines on input will cause a blank line in the output, unless the output is sorted. With sorted output, blank lines are ignored.</p>
<dt><code>-I</code> <i>l-pfx</i>, <code>&#8211;indent</code>=<i>l-pfx</i></p>
<dd> Line prefix or indentation. </p>
<p> If a number, then this many spaces will be inserted at the start of every line. Otherwise, it is a line prefix that will be inserted at the start of every line.</p>
<dt><code>&#8211;first-indent</code>=<i>l-pfx</i></p>
<dd> First line prefix. This option must appear in combination with the following options: indent. </p>
<p> If a number, then this many spaces will be inserted at the start of the first line. Otherwise, it is a line prefix that will be inserted at the start of that line. If its length exceeds &quot;indent&quot;, then it will be emitted on a line by itself, suffixed by any line separation string. For example: </p>
<pre><code>
$ columns-- first = '#define TABLE' - c 2 - I4-- line = ' ' &lt;&lt; _EOF_
                                                            one
                                                                two
                                                                    three
                                                                        four
                                                                            _EOF_
#define TABLE one two three four
</code></pre>
<dt><code>-f</code> <i>fmt-str</i>, <code>&#8211;format</code>=<i>fmt-str</i></p>
<dd> Formatting string for each input. </p>
<p> If you need to reformat each input text, the argument to this option is interpreted as an <code><a href="/docs/linux/man/3-sprintf/">sprintf</a>(3)</code> format that is used to produce each output entry.</p>
<dt><code>-S</code> <i>sep-str</i>, <code>&#8211;separation</code>=<i>sep-str</i></p>
<dd> Separation string &#8211; follows all but last. </p>
<p> Use this option if, for example, you wish a comma to appear after each entry except the last.</p>
<dt><code>&#8211;line-separation</code>=<i>sep-str</i></p>
<dd> string at end of all lines but last. </p>
<p> Use this option if, for example, you wish a backslash to appear at the end of every line, except the last.</p>
<dt><code>&#8211;ending</code>=<i>end-str</i></p>
<dd> string at end of last line. </p>
<p> This option puts the specified string at the end of the output.</dl>
<h3>Specify the ordering of the entries</h3>
<dl>
<dt><code>&#8211;by-columns</code></p>
<dd> Print entries in column order. </p>
<p> Normally, the entries are printed out in order by rows and then columns. This option will cause the entries to be ordered within columns. The final column, instead of the final row, may be shorter than the others.</p>
<dt><code>-s</code> <i>key-pat</i>, <code>&#8211;sort</code>[<code>=</code><i>key-pat</i>]</p>
<dd> Sort input text. </p>
<p> Causes the input text to be sorted. If an argument is supplied, it is presumed to be a pattern and the sort is based upon the matched text. If the pattern starts with or consists of an asterisk (<code>*</code>), then the sort is case insensitive.</dl>
<h3>Redirecting stdin to an alternate file</h3>
<dl>
<dt><code>-i</code> <i>file</i>, <code>&#8211;input</code>=<i>file</i></p>
<dd> Input file (if not stdin). </p>
<p> This program normally runs as a <code>filter</code>, reading from standard input, columnizing and writing to standard out. This option redirects input to a file.</p>
<dt><code>-?</code>,<code> &#8211;help</code></p>
<dd> Display usage information and exit.</p>
<dt><code>-!</code>,<code> &#8211;more-help</code></p>
<dd> Pass the extended usage information through a pager.</p>
<dt><code>-&gt;</code> [<i>cfgfile</i>],<code> &#8211;save-opts</code>[=<i>cfgfile</i>]</p>
<dd> Save the option state to <i>cfgfile</i>. The default is the <i>last</i> configuration file listed in the <code>OPTION PRESETS</code> section, below. The command will exit after updating the config file.</p>
<dt><code>-&lt;</code> <i>cfgfile</i>,<code> &#8211;load-opts</code>=<i>cfgfile</i>,<code> &#8211;no-load-opts</code></p>
<dd> Load options from <i>cfgfile</i>. The <i>no-load-opts</i> form will disable the loading of earlier config/rc/ini files. <i>&#8211;no-load-opts</i> is handled early, out of order.</p>
<dt><code>-v</code> [{<i>v|c|n</i>}],<code> &#8211;version</code>[={<i>v|c|n</i>}]</p>
<dd> Output version of program and exit. The default mode is `v&#8217;, a simple version. The `c&#8217; mode will print copyright information and `n&#8217; will print the full copyright notice.</dl>
<h2>OPTION PRESETS</h2>
<p> Any option that is not marked as <i>not presettable</i> may be preset by loading values from configuration (&quot;RC&quot; or &quot;.INI&quot;) file(s) and values from environment variables named: </p>
<pre>
  <code>COLUMNS_&lt;option-name&gt;</code> or <code>COLUMNS</code>
</pre>
<p> The environmental presets take precedence (are processed later than) the configuration files. The <i>homerc</i> files are &quot;<i>.</i>&quot;, and &quot;<i>$HOME</i>&quot;. If any of these are directories, then the file <i>.columnsrc</i> is searched for within those directories.</p>
<h2>ENVIRONMENT</h2>
<p> See <code>OPTION PRESETS</code> for configuration environment variables.</p>
<h2>FILES</h2>
<p> See <code>OPTION PRESETS</code> for configuration files.</p>
<h2>EXIT STATUS</h2>
<p> One of the following exit values will be returned:</p>
<dl>
<dt><code>0</code> (EXIT_SUCCESS)</p>
<dd> Successful program execution.</p>
<dt><code>1</code> (EXIT_FAILURE)</p>
<dd> The operation failed or the command syntax was not valid.</p>
<dt><code>66</code> (EX_NOINPUT)</p>
<dd> A specified configuration file could not be loaded.</p>
<dt><code>70</code> (EX_SOFTWARE)</p>
<dd> libopts had an internal operational error. Please report it to autogen-users [at] lists.sourceforge.net. Thank you.</dl>
<h2>SEE ALSO</h2>
<p> This program is documented more fully in the Columns section of the Add-On chapter in the <code>AutoGen</code> Info system documentation.</p>
<h2>AUTHORS</h2>
<p> Bruce Korb</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1999-2012 Bruce Korb all rights reserved. This program is released under the terms of the GNU General Public License, version 3 or later.</p>
<h2>BUGS</h2>
<p> Please send bug reports to: autogen-users [at] lists.sourceforge.net</p>
<h2>NOTES</h2>
<p> This manual page was <i>AutoGen</i>-erated from the <code>columns</code> option definitions. </p>
<h2>Index</h2>
