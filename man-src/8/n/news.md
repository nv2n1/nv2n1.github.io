---
title: "news(8)"
name: "news"
section: "8"
letter: "n"
url: "/docs/linux/man/8-news/"
description: "news.daily – Perform daily Usenet maintenance tasks"
---

<p>news.daily &#8211; Perform daily Usenet maintenance tasks</p>
<h2>Synopsis</h2>
<p><code>news.daily</code> [<code>delayrm</code>] [<code>expctl</code>=<i>path</i>] [<code>expdir</code>=<i>path</i>] [<code>expireover</code>] [<code>expireoverflags</code>=<i>args</i>] [<code>flags</code>=<i>args</i>] [<code>lowmark</code>] [<code>mailto</code>=<i>address</i>] [<code>noexpire</code>] [<code>noexpireover</code>] [<code>noexplog</code>] [<code>nologs</code>] [<code>nomail</code>] [<code>noprocbatch</code>] [<code>norenumber</code>] [<code>norm</code>] [<code>norotate</code>] [<code>nostat</code>] [<code>notdaily</code>] [<code>postexec</code>=<i>program</i>] [<code>tmpdir</code>=<i>path</i>] [<i>/path/to/a/program</i>]</p>
<h2>Description</h2>
<p><code>news.daily</code> performs a number of important Usenet administrative functions. This includes:</p>
<dl>
<dt>*</p>
<dd>producing a status report with <code>innstat</code>;</p>
<dt>*</p>
<dd>removing old news articles (with <code>expirerm</code> if the <code>delayrm</code> keyword is specified);</p>
<dt>*</p>
<dd>purging the overview database with <code>expireover</code> if the corresponding eponym keyword is specified;</p>
<dt>*</p>
<dd>processing log files and rotating the archived log files with <code>scanlogs</code>;</p>
<dt>*</p>
<dd>processing <code>innfeed</code> dropped files with <code>procbatch</code>;</p>
<dt>*</p>
<dd>renumbering the <i>active</i> file with <code>ctlinnd</code>;</p>
<dt>*</p>
<dd>rebuilding the <i>history</i> file with <code>expire</code>;</p>
<dt>*</p>
<dd>removing any old socket files found in the <i>pathrun</i> directory;</p>
<dt>*</p>
<dd>collecting all the output and mailing it.</dl>
<p> Please note that this program should be run under the news administrator&#8217;s account (usually <tt>&quot;news&quot;</tt>), not as root. By default, <code>news.daily</code> performs all of its functions and mails the output to the news administrator, which is the user specified with <code>&#8211;with-news-master</code> at configure time (it is <tt>&quot;usenet&quot;</tt> by default). You can also change this behaviour with the <code>mailto</code> keyword. </p>
<p> By specifying keywords on the command line, it is possible to modify the functions performed, as well as change the arguments given to <i><a href="/docs/linux/man/8-expire/">expire</a></i>(8) and <i><a href="/docs/linux/man/8-expireover/">expireover</a></i>(8). <code>news.daily</code> should be run once a day, typically out of <i><a href="/docs/linux/man/8-cron/">cron</a></i>(8). Since it will slow the server down while it is running, it should be run during periods of low server usage, such as in the middle of the night. To run it at 3am, for example, add the following entry to the news user&#8217;s crontab file: </p>
<pre> 0 3 * * * &lt;pathbin in inn.conf&gt;/news.daily expireover lowmark</pre>
<p>If you&#8217;re using any non-CNFS storage methods, add the <code>delayrm</code> keyword to the above option list for <code>news.daily</code>. </p>
<p> It may be run more often, but such invocations should at least use the <code>norotate</code> keyword (or perhaps the <code>notdaily</code> keyword) to prevent the log files from being processed and rotated too fast. The <i><a href="/docs/linux/man/1-shlock/">shlock</a></i>(1) program is used to prevent simultaneous executions. </p>
<p> The program specified by the given path <i>/path/to/a/program</i> is executed just before any expiration is done. A typical use is to specify an alternate expiration program and use the <code>noexpire</code> keyword. Multiple programs may be specified; they will be invoked in order.</p>
<h2>Keywords</h2>
<p>The following keywords may be used:</p>
<dl>
<dt><code>delayrm</code></p>
<dd>This uses the <code>-z</code> flag when invoking <code>expire</code> and <code>expireover</code>. The names of articles to be removed are written to a temporary file, and then renamed after expiration by calling <code>expirerm</code> which in turn calls <code>fastrm</code>.</p>
<dt><code>expctl</code>=<i>path</i></p>
<dd>Specify the file to use as the <i>expire.ctl</i> file for <code>expire</code>.</p>
<dt><code>expdir</code>=<i>path</i></p>
<dd>By default, <code>expire</code> builds the new <i>history</i> file and database in the same directory as the current files. Using this keyword specifies a different location to build the new files (by passing the <code>-d</code> flag to <code>expire</code>), which will then be moved to the right location when finished.</p>
<dt><code>expireover</code></p>
<dd>The <code>expireover</code> program is called after expiration to purge the overview database. If no overview data is created, the <code>expireover</code> keyword is not needed. This is the case when the server runs only for feeders (no reader). By default, <code>expireover</code> is not called by <code>news.daily</code>.</p>
<dt><code>expireoverflags</code>=<i>args</i></p>
<dd>If the <code>expireover</code> keyword is used, this keyword may be used to specify the flags to be passed to <code>expireover</code>. If the <code>delayrm</code> keyword is used, then the default value is <code>-z</code> and the list of deleted files; otherwise, the default value is <code>-s</code>.</p>
<dt><code>flags</code>=<i>args</i></p>
<dd>By default, <code>expire</code> is invoked with argument <code>-v1</code>. Using this keyword changes the arguments to those specified. Be careful to use quotes if multiple arguments are needed. This keyword has no effect if the <code>noexpire</code> keyword is used.</p>
<dt><code>lowmark</code></p>
<dd>If the <code>lowmark</code> keyword is used, <tt>&quot;ctlinnd lowmark&quot;</tt> is used for renumbering <i>active</i>. Normal <tt>&quot;ctlinnd renumber&quot;</tt> operation will take long time. With the <code>lowmark</code> keyword, this will take less time. If the <code>lowmark</code> keyword is used, the <code>norenumber</code> keyword is not needed since <code>news.daily</code> specifies it implicitly.</p>
<dt><code>mailto</code>=<i>address</i></p>
<dd>By default, <code>news.daily</code> mails the report to the newsmaster address specified with <code>&#8211;with-news-master</code> at configure time. The <code>mailto</code> keyword can specify a different address to which to mail the report. Note that using this keyword has no effect if the <code>nomail</code> keyword is also specified.</p>
<dt><code>noexpire</code></p>
<dd>By default, <code>expire</code> is invoked to remove old news articles. Using this keyword disables this function.</p>
<dt><code>noexpireover</code></p>
<dd>By default, <code>expireover</code> is invoked to remove old overview database if <i>enableoverview</i> is set in <i>inn.conf</i>. Using this keyword disables this function.</p>
<dt><code>noexplog</code></p>
<dd><code>expire</code> normally appends information to <i>pathlog</i>/expire.log (see <i><a href="/docs/linux/man/5-newslog/">newslog</a></i>(5)). Using this keyword causes the <code>expire</code> output to be handled as part of <code>news.daily</code>&#8216;s output. It has no effect if the <code>noexpire</code> keyword is used.</p>
<dt><code>nologs</code></p>
<dd>After expiration, <code>scanlogs</code> is invoked to process the log files. Using this keyword disables all log processing functions.</p>
<dt><code>nomail</code></p>
<dd><code>news.daily</code> normally sends a mail message containing the results to the administrator. Using this keyword causes this message to be sent to stdout and stderr instead. Normally, all utilities invoked by the script have their stdout and stderr redirected into a file. If the file is empty, no message is sent.</p>
<dt><code>noprocbatch</code></p>
<dd>This keyword disables the run of <code>procbatch</code> on <code>innfeed</code> dropped files generated in its spool directory. These files contain a list of articles which were not correctly sent to peers. By default, they will be processed and removed afterwards.</p>
<dt><code>norenumber</code></p>
<dd>This keyword disables the <tt>&quot;ctlinnd renumber&quot;</tt> operation. Normally, the low water marks for all newsgroups are reset in the <i>active</i> file.</p>
<dt><code>norm</code></p>
<dd>By default, any <code>ctlinnd</code> socket that has not been modified for two days will be removed. Using this keyword disables this function.</p>
<dt><code>norotate</code></p>
<dd>By default, log processing includes rotating and cleaning out log files. Using this keyword disables the rotating and cleaning aspect of the log processing: the logs files are only scanned for information and no contents are altered. This keyword has no effect if the <code>nologs</code> keyword is used. The <code>norotate</code> keyword is passed on to <code>scanlogs</code> if it is invoked.</p>
<dt><code>nostat</code></p>
<dd>This keyword disables the status report generated by <code>innstat</code>. Without this keyword, the status report is the first function performed, just prior to obtaining the <code>news.daily</code> lock.</p>
<dt><code>notdaily</code></p>
<dd>By default, <code>news.daily</code> expects to be run only once a day, and it does various things (like rotating logs) that normally should only be done on daily basis. Use this keyword any extra times <code>news.daily</code> is run in the day and the normal log files processing (and rotation) will not be done. This keyword implies <code>nologs</code>.</p>
<dt><code>postexec</code>=<i>program</i></p>
<dd>The program specified by the given path <i>program</i> is executed just after all expiration is done. Multiple programs may be specified; they will be invoked in order.</p>
<dt><code>tmpdir</code>=<i>path</i></p>
<dd>Overrides the <i>pathtmp</i> setting in <i>inn.conf</i> by setting the environment variable <tt>$TMPDIR</tt> to the specified path. Various parts of the expire process, such as sort, will then use this path as the directory for temporary files.</dl>
<h2>History</h2>
<p><code>news.daily</code> and this manual page were written by Landon Curt Noll &lt;chongo [at] toad.com&gt; and Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. It was converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> $Id: news.daily.pod 8468 2009-05-16 12:28:24Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/8-expire/">expire</a></i>(8), <i><a href="/docs/linux/man/5-expire-ctl/">expire.ctl</a></i>(5), <i><a href="/docs/linux/man/8-expireover/">expireover</a></i>(8), <i><a href="/docs/linux/man/8-expirerm/">expirerm</a></i>(8), <i><a href="/docs/linux/man/8-fastrm/">fastrm</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innstat/">innstat</a></i>(8), <i><a href="/docs/linux/man/5-newslog/">newslog</a></i>(5), <i><a href="/docs/linux/man/8-scanlogs/">scanlogs</a></i>(8), <i><a href="/docs/linux/man/1-shlock/">shlock</a></i>(1). </p>
