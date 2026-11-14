---
title: "sa(8)"
name: "sa"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sa/"
description: "sa – summarizes accounting information"
---

<p>sa &#8211; summarizes accounting information</p>
<h2>Synopsis</h2>
<dl>
<dt><code>sa</code></p>
<dd>[ <code>-a</code> | <code>&#8211;list-all-names</code> ]<br />
 [ <code>-b</code> | <code>&#8211;sort-sys-user-div-calls </code> ]<br />
 [ <code>-c</code> | <code>&#8211;percentages</code> ] [ <code>-d</code> | <code>&#8211;sort-avio</code> ]<br />
 [ <code>-D</code> | <code>&#8211;sort-tio</code> ] [ <code>-f</code> | <code>&#8211;not-interactive</code> ]<br />
 [ <code>-i</code> | <code>&#8211;dont-read-summary-files</code> ]<br />
 [ <code>-j</code> | <code>&#8211;print-seconds</code> ] [ <code>-k</code> | <code>&#8211;sort-cpu-avmem</code> ]<br />
 [ <code>-K</code> | <code>&#8211;sort-ksec</code> ] [ <code>-l</code> | <code>&#8211;separate-times</code> ]<br />
 [ <code>-m</code> | <code>&#8211;user-summary</code> ] [ <code>-n</code> | <code>&#8211;sort-num-calls</code> ]<br />
 [ <code>-p</code> | <code>&#8211;show-paging</code> ] [ <code>-P</code> | <code>&#8211;show-paging-avg</code> ]<br />
 [ <code>-r</code> | <code>&#8211;reverse-sort</code> ] [ <code>-s</code> | <code>&#8211;merge</code> ]<br />
 [ <code>-t</code> | <code>&#8211;print-ratio</code> ] [ <code>-u</code> | <code>&#8211;print-users</code> ]<br />
 [ <code>-v</code><i> num</i> | <code>&#8211;threshold</code><i> num</i> ] [ <code>&#8211;sort-real-time</code> ]<br />
 [ <code>&#8211;debug</code> ] [ <code>-V</code> | <code>&#8211;version</code> ] [ <code>-h</code> | <code>&#8211;help </code> ]<br />
 [ <code>&#8211;other-usracct-file </code><i>filename</i> ] [ <code>&#8211;ahz</code><i> hz</i> ]<br />
 [ <code>&#8211;other-savacct-file </code><i>filename</i> ]<br />
 [ [ <code>&#8211;other-acct-file </code> ] <i>filename</i> ]</dl>
<h2>Description</h2>
<p><code>sa</code> summarizes information about previously executed commands as recorded in the <i>acct</i> file. In addition, it condenses this data into a summary file named <i>savacct</i> which contains the number of times the command was called and the system resources used. The information can also be summarized on a per-user basis; <code>sa</code> will save this information into a file named <i>usracct.</i> </p>
<p> If no arguments are specified, <code>sa </code> will print information about all of the commands in the <i>acct</i> file. </p>
<p> If called with a file name as the last argument, <code>sa </code> will use that file instead of the system&#8217;s default <i>acct</i> file. </p>
<p> By default, <code>sa </code> will sort the output by sum of user and system time. If command names have unprintable characters, or are only called once, <code>sa </code> will sort them into a group called `***other&#8217;. If more than one sorting option is specified, the list will be sorted by the one specified last on the command line. </p>
<p> The output fields are labeled as follows:</p>
<dl>
<dt><i>cpu</i></p>
<dd>&nbsp;<wbr>sum of system and user time in cpu minutes</p>
<dt><i>re</i></p>
<dd>&nbsp;<wbr>&quot;elapsed time&quot;&nbsp;<wbr>in minutes</p>
<dt><i>k</i></p>
<dd>&nbsp;<wbr>cpu-time averaged core usage, in 1k units</p>
<dt><i>avio</i></p>
<dd>&nbsp;<wbr>average number of I/O operations per execution</p>
<dt><i>tio</i></p>
<dd>&nbsp;<wbr>total number of I/O operations</p>
<dt><i>k*sec</i></p>
<dd>&nbsp;<wbr>cpu storage integral&nbsp;<wbr>(kilo-core seconds)</p>
<dt><i>u</i></p>
<dd>&nbsp;<wbr>user cpu time in cpu seconds</p>
<dt><i>s</i></p>
<dd>&nbsp;<wbr>system time in cpu seconds</dl>
<p> Note that these column titles do not appear in the first row of the table, but after each numeric entry (as units of measurement) in every row. For example, you might see `79.29re&#8217;, meaning 79.29 cpu seconds of &quot;real time&quot;. </p>
<p> An asterisk will appear after the name of commands that forked but didn&#8217;t call <code>exec.</code> </p>
<p> GNU <code>sa</code> takes care to implement a number of features not found in other versions. For example, most versions of <code>sa </code> don&#8217;t pay attention to flags like `&#8211;print-seconds&#8217; and `&#8211;sort-num-calls&#8217; when printing out commands when combined with the `&#8211;user-summary&#8217; or `&#8211;print-users&#8217; flags. GNU <code>sa </code> pays attention to these flags if they are applicable. Also, MIPS&#8217; <code>sa</code> stores the average memory use as a short rather than a double, resulting in some round-off errors. GNU <code>sa </code> uses double the whole way through.</p>
<h2>Options</h2>
<p>The availability of these program options depends on your operating system. In specific, the members that appear in the <code>struct acct</code> of your system&#8217;s process accounting header file (usually <i>acct.h</i> ) determine which flags will be present. For example, if your system&#8217;s <code>struct acct</code> doesn&#8217;t have the `ac_mem&#8217; field, the installed version of <code>sa</code> will not support the `&#8211;sort-cpu-avmem&#8217;, `&#8211;sort-ksec&#8217;, `-k&#8217;, or `-K&#8217; options. </p>
<p> In short, all of these flags may not be available on your machine.</p>
<dl>
<dd><code>-a, &#8211;list-all-names</code> Force <code>sa </code> not to sort those command names with unprintable characters and those used only once into the <i>***other</i> group.</p>
<dt><code>-b, &#8211;sort-sys-user-div-calls</code></p>
<dd>Sort the output by the sum of user and system time divided by the number of calls.</p>
<dt><code>-c, &#8211;percentages</code></p>
<dd>Print percentages of total time for the command&#8217;s user, system, and real time values.</p>
<dt><code>-d, &#8211;sort-avio</code></p>
<dd>Sort the output by the average number of disk I/O operations.</p>
<dt><code>-D, &#8211;sort-tio</code></p>
<dd>Print and sort the output by the total number of disk I/O operations.</p>
<dt><code>-f, &#8211;not-interactive</code></p>
<dd>When using the `&#8211;threshold&#8217; option, assume that all answers to interactive queries will be affirmative.</p>
<dt><code>-i, &#8211;dont-read-summary-files</code></p>
<dd>Don&#8217;t read the information in the system&#8217;s default <i>savacct</i> file.</p>
<dt><code>-j, &#8211;print-seconds</code></p>
<dd>Instead of printing total minutes for each category, print seconds per call.</p>
<dt><code>-k, &#8211;sort-cpu-avmem</code></p>
<dd>Sort the output by cpu time average memory usage.</p>
<dt><code>-K, &#8211;sort-ksec</code></p>
<dd>Print and sort the output by the cpu-storage integral.</p>
<dt><code>-l, &#8211;separate-times</code></p>
<dd>Print separate columns for system and user time; usually the two are added together and listed as `cpu&#8217;.</p>
<dt><code>-m, &#8211;user-summary</code></p>
<dd>Print the number of processes and number of CPU minutes on a per-user basis.</p>
<dt><code>-n, &#8211;sort-num-calls</code></p>
<dd>Sort the output by the number of calls. This is the default sorting method.</p>
<dt><code>-p, &#8211;show-paging</code></p>
<dd>Print the number of minor and major pagefaults and swaps.</p>
<dt><code>-P, &#8211;show-paging-avg</code></p>
<dd>Print the number of minor and major pagefaults and swaps divided by the number of calls.</p>
<dt><code>-r, &#8211;reverse-sort</code></p>
<dd>Sort output items in reverse order.</p>
<dt><code>-s, &#8211;merge</code></p>
<dd>Merge the summarized accounting data into the summary files <i>savacct</i> and <i>usracct.</i></p>
<dt><code>-t, &#8211;print-ratio</code></p>
<dd>For each entry, print the ratio of real time to the sum of system and user times. If the sum of system and user times is too small to report&#8211;the sum is zero&#8211;`*ignore*&#8217; will appear in this field.</p>
<dt><code>-u, &#8211;print-users</code></p>
<dd>For each command in the accounting file, print the userid and command name. After printing all entries, quit. *Note*: this flag supersedes all others.</p>
<dt><code>-v</code><i> num </i><code>&#8211;threshold</code><i> num</i></p>
<dd>Print commands which were executed <i>num </i> times or fewer and await a reply from the terminal. If the response begins with `y&#8217;, add the command to the `**junk**&#8217; group.</p>
<dt><code>&#8211;separate-forks</code></p>
<dd>It really doesn&#8217;t make any sense to me that the stock version of <code>sa </code> separates statistics for a particular executable depending on whether or not that command forked. Therefore, GNU <code>sa </code> lumps this information together unless this option is specified.</p>
<dt><code>&#8211;ahz</code><i> hz</i></p>
<dd>Use this flag to tell the program what <code>AHZ</code> should be (in hertz). This option is useful if you are trying to view an <i>acct</i> file created on another machine which has the same byte order and file format as your current machine, but has a different value for <code>AHZ.</code></p>
<dt><code>&#8211;debug</code></p>
<dd>Print verbose internal information.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Print the version number of <code>sa.</code></p>
<dt><code>-h, &#8211;help</code></p>
<dd>Prints the usage string and default locations of system files to standard output and exits.</p>
<dt><code>&#8211;sort-real-time</code></p>
<dd>Sort the output by the &quot;real time&quot; field.</p>
<dt><code>&#8211;other-usracct-file</code><i> filename</i></p>
<dd>Write summaries by user ID to <i>filename</i> rather than the system&#8217;s default <i>usracct</i> file.</p>
<dt><code>&#8211;other-savacct-file</code><i> filename</i></p>
<dd>Write summaries by command name to <i>filename</i> rather than the system&#8217;s default <i>SAVACCT</i> file.</p>
<dt><code>&#8211;other-acct-file</code><i> filename</i></p>
<dd>Read from the file <i>filename </i> instead of the system&#8217;s default <i>ACCT</i> file.</dl>
<h2>Files</h2>
<dl>
<dt><i>acct</i></p>
<dd>The raw system wide process accounting file. See <code><a href="/docs/linux/man/5-acct/">acct</a></code>(5) for further details.</p>
<dt><i>savacct</i></p>
<dd>A summary of system process accounting sorted by command.</p>
<dt><i>usracct</i></p>
<dd>A summary of system process accounting sorted by user ID.</dl>
<h2>Bugs</h2>
<p>There is not yet a wide experience base for comparing the output of GNU <code>sa </code> with versions of <code>sa</code> in many other systems. The problem is that the data files grow big in a short time and therefore require a lot of disk space. </p>
<h2>Author</h2>
<p>The GNU accounting utilities were written by Noel Cragg &lt;noel [at] gnu.ai.mit.edu&gt;. The man page was adapted from the accounting texinfo page by Susan Kleinmann &lt;sgk [at] sgk.tiac.net&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-acct/">acct</a></code>(5), <code><a href="/docs/linux/man/1-ac/">ac</a></code>(1) </p>
