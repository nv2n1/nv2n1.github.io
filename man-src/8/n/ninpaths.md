---
title: "ninpaths(8)"
name: "ninpaths"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ninpaths/"
description: "ninpaths – Report Usenet Path: statistics (new inpaths)"
---

<p>ninpaths &#8211; Report Usenet Path: statistics (new inpaths)</p>
<h2>Synopsis</h2>
<p><code>ninpaths</code> <code>-p</code> <code>-d</code> <i>dumpfile</i> </p>
<p> <code>ninpaths</code> <code>-r</code> <i>site</i> <code>-u</code> <i>dumpfile</i> [<code>-u</code> <i>dumpfile</i> &#8230;] <code>-v</code> <i>level</i></p>
<h2>Description</h2>
<p>This is an efficient and space-saving <code>inpaths</code> reporting program. It works as follows: you feed it the Path: lines via an <font SIZE="-1">INN</font> channel feed or some other similar method, and from time to time the program writes all its internal counters accumulated so far to a dump file. Another instance of the program picks up all the dump files, adds them up and formats them into the report. The purpose of the final report is to summarize the frequency of occurrence of sites in the Path: headers of articles. </p>
<p> Some central sites accumulate the Path: data from many news servers running this program or one like it, and then report statistics on the most frequently seen news servers in Usenet article Path: lines. The <code>sendinpaths</code> script can be run daily to mail the accumulated statistics to such a site and remove the old dump files. </p>
<p> You can get a working setup by doing the following:</p>
<dl>
<dt>1.</p>
<dd>Create a directory at <i>pathlog</i>/path (replacing <i>pathlog</i> here and in all steps that follow with the full path to your <font SIZE="-1">INN</font> log directory). Do not change the name of the <tt>&quot;path&quot;</tt> subdirectory because it is used by <code>sendinpaths</code>.</p>
<dt>2.</p>
<dd>Set up a channel feed using an entry like: </p>
<pre> inpaths!:*:Tc,WP:&lt;pathbin&gt;/ninpaths -p -d &lt;pathlog&gt;/path/inpaths.%d</pre>
<p>if your version of <font SIZE="-1">INN</font> supports <tt>&quot;WP&quot;</tt> (2.0 and later all do). Replace &lt;pathbin&gt; with the full path to your <font SIZE="-1">INN</font> binaries directory, and &lt;pathlog&gt; with the full path to your <font SIZE="-1">INN</font> log directory. </p>
<p> Note that the naming convention of the generated inpaths dump files should not be changed. <code>sendinpaths</code> explicitly searches files whose name starts with <tt>&quot;inpaths.&quot;</tt> in the &lt;pathlog&gt;/path directory.</p>
<dt>3.</p>
<dd>Run the following command to start logging these statistics: </p>
<pre> ctlinnd reload newsfeeds 'inpaths feed setup'</pre>
<dt>4.</p>
<dd>Enter into your news user crontab these two lines: </p>
<pre> 6 6 * * * &lt;pathbin&gt;/ctlinnd flush inpaths!
 10 6 * * * &lt;pathbin&gt;/sendinpaths</pre>
<p>(the actual time doesn&#8217;t matter). This will force <code>ninpaths</code> to generate a dump file once a day. Then, a few minutes later, <code>sendinpaths</code> collects the dumps, makes a report, sends the collected statistics, and deletes the old dumps. </p>
<p> Note that you can manually generate a report without mailing it, and without deleting processed dump files, with <tt>&quot;sendinpaths -n&quot;</tt>. Another useful command is <tt>&quot;sendinpaths -c&quot;</tt> so as to receive a copy of the e-mail sent by <code>sendinpaths</code> and therefore make sure that everything is properly set.</p>
<dt>5.</p>
<dd>In a couple of days, check that your daily statistics properly appear in &lt;<a rel="nofollow" href="http://top1000.anthologeek.net/">http://top1000.anthologeek.net/</a>&gt;.</dl>
<h2>Options</h2>
<dl>
<dt><code>-d</code> <i>dumpfile</i></p>
<dd>Save dumps in <i>dumpfile</i>. Any <tt>%d</tt> in <i>dumpfile</i> will be replaced with the current system time when the dump is made. This option should be used with <code>-p</code>. </p>
<p> The format of these dump files is described below.</p>
<dt><code>-p</code></p>
<dd>Read Path: lines from standard input.</p>
<dt><code>-r</code> <i>site</i></p>
<dd>Generate a report for <i>site</i>. Generally <i>site</i> should be the value of <i>pathhost</i> from <i>inn.conf</i>.</p>
<dt><code>-u</code> <i>dumpfile</i></p>
<dd>Read data from <i>dumpfile</i>. This option can be repeated to read data from multiple dump files.</p>
<dt><code>-v</code> <i>level</i></p>
<dd>Set the verbosity level of the report. Valid values for <i>level</i> are <tt>0</tt>, <tt>1</tt>, and <tt>2</tt>, with <tt>2</tt> being the default.</dl>
<h2>Dump File Format</h2>
<p>The format of the generated dump files is: </p>
<pre> !!NINP &lt;version&gt; &lt;start-time&gt; &lt;end-time&gt; &lt;nb-sites&gt; &lt;nb-articles&gt; &lt;average-time&gt;
 &lt;site_0&gt; &lt;count_0&gt; &lt;site_1&gt; &lt;count_1&gt; &lt;site_2&gt; &lt;count_2&gt; ...
 !!NLREC
 :&lt;site_a&gt;!&lt;site_b&gt;,&lt;count_ab&gt;:&lt;site_c&gt;!&lt;site_d&gt;,&lt;count_cd&gt; ...
 !!NEND &lt;nb-relations&gt;</pre>
<p>where times are <font SIZE="-1">UNIX</font> timestamps. Then, <i>nb-sites</i> records follow. Each record is separated by a space or a new line, and consists of a host name <i>site_n</i> followed by a number of appearances <i>count_n</i>. The number of processed Path: header lines is <i>nb-articles</i>. </p>
<p> Afterwards, <i>nb-relations</i> relations follow. In 3.0.x versions, the relations are separated by a space or a new line, and their syntax is <tt>&quot;</tt>site_a<tt>!</tt>site_b<tt>!</tt>count_ab<tt>&quot;</tt> where <i>site_a</i> and <i>site_b</i> are numbers of the site records starting at 0. </p>
<p> In 3.1.x versions, the relations begin with a colon and are separated by either nothing or a new line. Their syntax is <tt>&quot;:</tt>site_a<tt>!</tt>site_b<tt>,</tt>count_ab<tt>&quot;</tt> with the same meaning as in previous versions. The count can be omitted when it is <tt>1</tt>. More than two sites can be specified in the relation (<tt>&quot;:</tt>site_a<tt>!</tt>site_b<tt>!</tt>site_c<tt>,</tt>count_abc<tt>&quot;</tt>). </p>
<p> For instance: </p>
<pre> !!NINP 3.1.1 1302944821 1302944838 5 2 1302944826
 newsgate.cistron.nl 1 news.trigofacile.com 2 news.ecp.fr 2 usenet.stanford.edu 1
 bleachbot 1
 !!NLREC
 :3!2:2!1,2:4!0:0!2
 !!NLEND 4</pre>
<p>where the two processed Path: headers are: </p>
<pre> Path: news.trigofacile.com!news.ecp.fr!usenet.stanford.edu!not-for-mail
 Path: news.trigofacile.com!news.ecp.fr!newsgate.cistron.nl!bleachbot!not-for-mail</pre>
<h2>Notes</h2>
<p>If your <font SIZE="-1">INN</font> doesn&#8217;t have the <tt>&quot;WP&quot;</tt> feed flag (1.5 does not, 1.6 and 1.7 do, 2.0 and later all do), use the following <i>newsfeeds</i> entry: </p>
<pre> inpaths!:*:Tc,WH:&lt;pathbin&gt;/ginpaths</pre>
<p>where <code>ginpaths</code> is the following script: </p>
<pre> #!/bin/sh
 exec egrep '^Path: ' | &lt;pathbin&gt;/ninpaths -p -d &lt;pathlog&gt;/path/inpaths.%d</pre>
<p>replacing &lt;pathbin&gt; and &lt;pathlog&gt; as above.</p>
<h2>History</h2>
<p>This is a slightly modified version of Olaf Titz&#8217;s original <code>ninpaths</code> program, which is posted to alt.sources and kept on his <font SIZE="-1">WWW</font> archive under &lt;<a rel="nofollow" href="http://sites.inka.de/~bigred/sw/">http://sites.inka.de/~bigred/sw/</a>&gt;. </p>
<p> The idea and some implementation details for <code>ninpaths</code> come from the original <code>inpaths</code> program, but most of the code has been rewritten for clarity. This program is in the public domain. </p>
<p> <tt>$Id:</tt> ninpaths.pod 9384 2011-12-25 20:57:03Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/8-sendinpaths/">sendinpaths</a></i>(8). </p>
