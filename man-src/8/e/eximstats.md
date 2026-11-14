---
title: "eximstats(8)"
name: "eximstats"
section: "8"
letter: "e"
url: "/docs/linux/man/8-eximstats/"
description: "eximstats – generates statistics from Exim mainlog or syslog files."
---

<p>eximstats &#8211; generates statistics from Exim mainlog or syslog files.</p>
<h2>Synopsis</h2>
<pre> eximstats [Output] [Options] mainlog1 mainlog2 ...
 eximstats -merge [Options] report.1.txt report.2.txt ... &gt; weekly_report.txt</pre>
<h3>Output:</h3>
<dl>
<dt><code>-txt</code></p>
<dd>Output the results in plain text to <font SIZE="-1">STDOUT.</font></p>
<dt><code>-txt</code>=<i>filename</i></p>
<dd>Output the results in plain text. Filename &#8216;-&#8216; for <font SIZE="-1">STDOUT</font> is accepted.</p>
<dt><code>-html</code></p>
<dd>Output the results in <font SIZE="-1">HTML</font> to <font SIZE="-1">STDOUT.</font></p>
<dt><code>-html</code>=<i>filename</i></p>
<dd>Output the results in <font SIZE="-1">HTML.</font> Filename &#8216;-&#8216; for <font SIZE="-1">STDOUT</font> is accepted.</p>
<dt><code>-xls</code></p>
<dd>Output the results in Excel compatible Format to <font SIZE="-1">STDOUT.</font> Requires the Spreadsheet::WriteExcel <font SIZE="-1">CPAN</font> module.</p>
<dt><code>-xls</code>=<i>filename</i></p>
<dd>Output the results in Excel compatible format. Filename &#8216;-&#8216; for <font SIZE="-1">STDOUT</font> is accepted.</dl>
<h3>Options:</h3>
<dl>
<dt><code>-h</code><i>number</i></p>
<dd>histogram divisions per hour. The default is 1, and 0 suppresses histograms. Valid values are: </p>
<p> 0, 1, 2, 3, 5, 10, 15, 20, 30 or 60.</p>
<dt><code>-ne</code></p>
<dd>Don&#8217;t display error information.</p>
<dt><code>-nr</code></p>
<dd>Don&#8217;t display relaying information.</p>
<dt><code>-nr</code><i>/pattern/</i></p>
<dd>Don&#8217;t display relaying information that matches.</p>
<dt><code>-nt</code></p>
<dd>Don&#8217;t display transport information.</p>
<dt><code>-nt</code><i>/pattern/</i></p>
<dd>Don&#8217;t display transport information that matches</p>
<dt><code>-q</code><i>list</i></p>
<dd>List of times for queuing information single 0 item suppresses.</p>
<dt><code>-t</code><i>number</i></p>
<dd>Display top &lt;number&gt; sources/destinations default is 50, 0 suppresses top listing.</p>
<dt><code>-tnl</code></p>
<dd>Omit local sources/destinations in top listing.</p>
<dt><code>-t_remote_users</code></p>
<dd>Include remote users in the top source/destination listings.</p>
<dt><code>-include_original_destination</code></p>
<dd>Include the original destination email addresses rather than just using the final ones. Useful for finding out which of your mailing lists are receiving mail.</p>
<dt><code>-show_dt</code><i>list</i></p>
<dd>Show the delivery times (<font SIZE="-1"><code>DT</code></font>)for all the messages. </p>
<p> Exim must have been configured to use the +deliver_time logging option for this option to work. </p>
<p> <i>list</i> is an optional list of times. Eg -show_dt1,2,4,8 will show the number of messages with delivery times under 1 second, 2 seconds, 4 seconds, 8 seconds, and over 8 seconds.</p>
<dt><code>-show_rt</code><i>list</i></p>
<dd>Show the receipt times for all the messages. The receipt time is defined as the Completed hh:mm:ss &#8211; queue_time_overall &#8211; the Receipt hh:mm:ss. These figures will be skewed by pipelined messages so might not be that useful. </p>
<p> Exim must have been configured to use the +queue_time_overall logging option for this option to work. </p>
<p> <i>list</i> is an optional list of times. Eg -show_rt1,2,4,8 will show the number of messages with receipt times under 1 second, 2 seconds, 4 seconds, 8 seconds, and over 8 seconds.</p>
<dt><code>-byhost</code></p>
<dd>Show results by sending host. This may be combined with <code>-bydomain</code> and/or <code>-byemail</code> and/or <code>-byedomain</code>. If none of these options are specified, then <code>-byhost</code> is assumed as a default.</p>
<dt><code>-bydomain</code></p>
<dd>Show results by sending domain. May be combined with <code>-byhost</code> and/or <code>-byemail</code> and/or <code>-byedomain</code>.</p>
<dt><code>-byemail</code></p>
<dd>Show results by sender&#8217;s email address. May be combined with <code>-byhost</code> and/or <code>-bydomain</code> and/or <code>-byedomain</code>.</p>
<dt><code>-byemaildomain</code> or <code>-byedomain</code></p>
<dd>Show results by sender&#8217;s email domain. May be combined with <code>-byhost</code> and/or <code>-bydomain</code> and/or <code>-byemail</code>.</p>
<dt><code>-pattern</code> <i>Description</i> <i>/Pattern/</i></p>
<dd>Look for the specified pattern and count the number of lines in which it appears. This option can be specified multiple times. Eg: </p>
<pre> -pattern 'Refused connections' '/refused connection/'</pre>
<dt><code>-merge</code></p>
<dd>This option allows eximstats to merge old eximstat reports together. Eg: </p>
<pre> eximstats mainlog.sun &gt; report.sun.txt
 eximstats mainlog.mon &gt; report.mon.txt
 eximstats mainlog.tue &gt; report.tue.txt
 eximstats mainlog.wed &gt; report.web.txt
 eximstats mainlog.thu &gt; report.thu.txt
 eximstats mainlog.fri &gt; report.fri.txt
 eximstats mainlog.sat &gt; report.sat.txt
 eximstats -merge report.*.txt &gt; weekly_report.txt
 eximstats -merge -html report.*.txt &gt; weekly_report.html</pre>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>You can merge text or html reports and output the results as text or html.</p>
<dt>&bull;</p>
<dd>You can use all the normal eximstat output options, but only data included in the original reports can be shown!</p>
<dt>&bull;</p>
<dd>When merging reports, some loss of accuracy may occur in the top <i>n</i> lists. This will be towards the ends of the lists.</p>
<dt>&bull;</p>
<dd>The order of items in the top <i>n</i> lists may vary when the data volumes round to the same value.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>-charts</code></p>
<dd>Create graphical charts to be displayed in <font SIZE="-1">HTML</font> output. Only valid in combination with <i>-html</i>. </p>
<p> This requires the following modules which can be obtained from <a rel="nofollow" href="http://www.cpan.org/modules/01modules.index.html">http://www.cpan.org/modules/01modules.index.html</a></p>
<dl>
<dd>
<dl>
<dt><font SIZE="-1">GD</font></p>
<dd>
<dt>GDTextUtil</p>
<dd>
<dt>GDGraph</p>
<dd></dl>
</dl>
<dl>
<dd>To install these, download and unpack them, then use the normal perl installation procedure: </p>
<pre> perl Makefile.PL
 make
 make test
 make install</pre>
</dl>
<dt><code>-chartdir</code>I &lt;dir&gt;</p>
<dd>Create the charts in the directory &lt;dir&gt;</p>
<dt><code>-chartrel</code>I &lt;dir&gt;</p>
<dd>Specify the relative directory for the &#8220;img src=&#8221; tags from where to include the charts</p>
<dt><code>-emptyok</code></p>
<dd>Specify that it&#8217;s <font SIZE="-1">OK</font> to not find any valid log lines. Without this we will output an error message if we don&#8217;t find any.</p>
<dt><code>-d</code></p>
<dd>Debug flag. This outputs the <i>eval()</i>&#8216;d parser onto <font SIZE="-1">STDOUT</font> which makes it easier to trap errors in the eval section. Remember to add 1 to the line numbers to allow for the title!</dl>
<h2>Description</h2>
<p>Eximstats parses exim mainlog and syslog files to output a statistical analysis of the messages processed. By default, a text analysis is generated, but you can request other output formats using flags. See the help (<code>-help</code>) to learn about how to create charts from the tables.</p>
<h2>Author</h2>
<p>There is a web site at <a rel="nofollow" href="http://www.exim.org">http://www.exim.org</a> &#8211; this contains details of the mailing list exim-users [at] exim.org.</p>
<h2>To Do</h2>
<p>This program does not perfectly handle messages whose received and delivered log lines are in different files, which can happen when you have multiple mail servers and a message cannot be immediately delivered. Fixing this could be tricky&#8230; </p>
<p> Merging of xls files is not (yet) possible. Be free to implement :)</p>
