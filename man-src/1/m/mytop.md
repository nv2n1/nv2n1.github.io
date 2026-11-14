---
title: "mytop(1)"
name: "mytop"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mytop/"
description: "mytop – display MySQL server performance info like `top’"
---

<h2 class="name">NAME</h2>
<p> mytop &#8211; display MySQL server performance info like `top&#8217; </p>
<h2>SYNOPSIS</h2>
<p> <code>mytop</code> [options]</p>
<h2>AVAILABILITY</h2>
<p> The latest version of <code>mytop</code> is available from <a rel="nofollow" href="http://jeremy.zawodny.com/mysql/mytop/">http://jeremy.zawodny.com/mysql/mytop/</a> it <code>might</code> also be on <font SIZE="-1">CPAN</font> as well.</p>
<h2>REQUIREMENTS</h2>
<p> In order for <code>mytop</code> to function properly, you must have the following: </p>
<pre>
  * Perl 5.005 or newer
  * Getopt::Long
  * DBI and DBD::mysql
  * Term::ReadKey from CPAN
</pre>
<p> Most systems are likely to have all of those installed&#8212;except for Term::ReadKey. You will need to pick that up from the <font SIZE="-1">CPAN.</font> You can pick up Term::ReadKey here: </p>
<pre>
    <a rel="nofollow" href="http://search.cpan.org/search?dist=TermReadKey">http://search.cpan.org/search?dist=TermReadKey</a>
</pre>
<p> And you obviously need access to a MySQL server (version 3.22.x or 3.23.x) with the necessary security to run the <i></i><font SIZE="-1"><i>SHOW PROCESSLIST</i></font><i></i> and <i></i><font SIZE="-1"><i>SHOW GLOBAL STATUS</i></font><i></i> commands. </p>
<p> If you are a Windows user, using ActiveState&#8217;s Perl, you can use <font SIZE="-1">PPM </font>(the Perl Package Manager) to install the MySQL and Term::ReadKey modules.</p>
<h3>Optional Color Support</h3>
<p> In additon, if you want a color <code>mytop</code> (recommended), install Term::ANSIColor from the <font SIZE="-1">CPAN:</font> </p>
<pre>
    <a rel="nofollow" href="http://search.cpan.org/search?dist=ANSIColor">http://search.cpan.org/search?dist=ANSIColor</a>
</pre>
<p> Once you do, <code>mytop</code> will automatically use it. However, color is not yet working on Windows. Patches welcome. :-)</p>
<h3>Optional Hi-Res Timing</h3>
<p> If you want <code>mytop</code> to provide more accurate real-time queries-per-second statistics, install the Time::HiRes module from <font SIZE="-1">CPAN. </font><code>mytop</code> will automatically notice that you have it and use it rather than the standard timing mechanism.</p>
<h3>Platforms</h3>
<p> <code>mytop</code> is known to work on: </p>
<pre>
  * Linux (2.2.x, 2.4.x)
  * FreeBSD (2.2, 3.x, 4.x)
  * Mac OS X
  * BSDI 4.x
  * Solaris 2.x
  * Windows NT 4.x (ActivePerl)
</pre>
<p> If you find that it works on another platform, please let me know. Given that it is all Perl code, I expect it to be rather portable to Unix and Unix-like systems. Heck, it <i>might</i> even work on Win32 systems.</p>
<h2>DESCRIPTION</h2>
<p> Help is always welcome in improving this software. Feel free to contact the author (see &#8220;<font SIZE="-1">AUTHOR&#8221;</font> below) with bug reports, fixes, suggestions, and comments. Additionally &#8220;<font SIZE="-1">BUGS&#8221;</font> will provide a list of things this software is not able to do yet. </p>
<p> Having said that, here are the details on how it works and what you can do with it.</p>
<h3>The Basics</h3>
<p> <code>mytop</code> was inspired by the system monitoring tool <code>top</code>. I routinely use <code>top</code> on Linux, FreeBSD, and Solaris. You are likely to notice features from each of them here. </p>
<p> <code>mytop</code> will connect to a MySQL server and periodically run the <i></i><font SIZE="-1"><i>SHOW PROCESSLIST</i></font><i></i> and <i></i><font SIZE="-1"><i>SHOW GLOBAL STATUS</i></font><i></i> commands and attempt to summarize the information from them in a useful format.</p>
<h3>The Display</h3>
<p> The <code>mytop</code> display screen is really broken into two parts. The top 4 lines (header) contain summary information about your MySQL server. For example, you might see something like: </p>
<p> MySQL on localhost (4.0.13-log) up 1+11:13:00 [23:29:11]<br />
&nbsp;<wbr>Queries: 19.3M&nbsp;<wbr>&nbsp;<wbr>qps:&nbsp;<wbr>&nbsp;<wbr>160 Slow:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Se/In/Up/De(%):&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>00/80/03/17<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>qps now:&nbsp;<wbr>&nbsp;<wbr>219 Slow qps: 0.0&nbsp;<wbr>&nbsp;<wbr>Threads:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>(&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1/&nbsp;<wbr>&nbsp;<wbr>16)&nbsp;<wbr>00/74/00/25<br />
&nbsp;<wbr>Key Efficiency: 99.3%&nbsp;<wbr>&nbsp;<wbr>Bps in/out: 30.5k/162.8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Now in/out: 32.7k/&nbsp;<wbr>3.3k </p>
<p> The first line identifies the hostname of the server (localhost) and the version of MySQL it is running. The right had side shows the uptime of the MySQL server process in days+hours:minutes:seconds format (much like FreeBSD&#8217;s top) as well as the current time. </p>
<p> The second line displays the total number of queries the server has processed, the average number of queries per second, the number of slow queries, and the percentage of Select, Insert, Update, and Delete queries. </p>
<p> The third real-time values. First is the number of queries per second, then the number of slow queries, followed by query precentages (like on the previous line). </p>
<p> And the fourth line displays key buffer efficiency (how often keys are read from the buffer rather than disk) and the number of bytes that MySQL has sent and received, both over all and in the last cycle. </p>
<p> You can toggle the header by hitting <code>h</code> when running <code>mytop</code>. </p>
<p> The second part of the display lists as many threads as can fit on screen. By default they are sorted according to their idle time (least idle first). The display looks like: </p>
<pre><code>
Id User Host Dbase Time Cmd Query or State-- -- -- -- -- -- -- - -- -- -- - -- -- -- -- -- -- --61 jzawodn localhost music 0 Query show processlist
</code></pre>
<p> As you can see, the thread id, username, host from which the user is connecting, database to which the user is connected, number of seconds of idle time, the command the thread is executing, and the query info are all displayed. </p>
<p> Often times the query info is what you are really interested in, so it is good to run <code>mytop</code> in an xterm that is wider than the normal 80 columns if possible. </p>
<p> The thread display color-codes the threads if you have installed color support. The current color scheme only works well in a window with a dark (like black) background. The colors are selected according to the <tt>&quot;Command&quot;</tt> column of the display: </p>
<pre>
    Query   -  Yellow
    Sleep   -  White
    Connect -  Green
</pre>
<p> Those are purely arbitrary and will be customizable in a future release. If they annoy you just start <code>mytop</code> with the <code>-nocolor</code> flag or adjust your config file appropriately.</p>
<h3>Arguments</h3>
<p> <code>mytop</code> handles long and short command-line arguments. Not all options have both long and short formats, however. The long arguments can start with one or two dashes `-&#8216; or `&#8211;&#8216;. They are shown here with just one.</p>
<dl>
<dt><code>-u</code> or <code>-user</code> username</p>
<dd> Username to use when logging in to the MySQL server. Default: &#8220;root&#8221;.</p>
<dt><code>-p</code> or <code>-pass</code> or <code>-password</code> password</p>
<dd> Password to use when logging in to the MySQL server. Default: none.</p>
<dt><code>-h</code> or <code>-host</code> hostname[:port]</p>
<dd> Hostname of the MySQL server. The hostname may be followed by an option port number. Note that the port is specified separate from the host when using a config file. Default: &#8220;localhost&#8221;.</p>
<dt><code>-port</code> or <code>-P</code> port</p>
<dd> If you&#8217;re running MySQL on a non-standard port, use this to specify the port number. Default: 3306.</p>
<dt><code>-s</code> or <code>-delay</code> seconds</p>
<dd> How long between display refreshes. Default: 5</p>
<dt><code>-d</code> or <code>-db</code> or <code>-database</code> database</p>
<dd> Use if you&#8217;d like <code>mytop</code> to connect to a specific database by default. Default: &#8220;test&#8221;.</p>
<dt><code>-b</code> or <code>-batch</code> or <code>-batchmode</code></p>
<dd> In batch mode, mytop runs only once, does not clear the screen, and places no limit on the number of lines it will print. This is suitable for running periodically (perhaps from cron) to capture the information into a file for later viewing. You might use batch mode in a <font SIZE="-1">CGI</font> script to occasionally display your MySQL server status on the web. </p>
<p> Default: unset.</p>
<dt><code>-S</code> or <code>-socket</code> /path/to/socket</p>
<dd> If you&#8217;re running <code>mytop</code> on the same host as MySQL, you may wish to have it use the MySQL socket directly rather than a standard <font SIZE="-1">TCP/IP</font> connection. If you do,just specify one. </p>
<p> Note that specifying a socket will make <code>mytop</code> ignore any host and/or port that you might have specified. If the socket does not exist (or the file specified is not a socket), this option will be ignored and <code>mytop</code> will use the hostname and port number instead. </p>
<p> Default: none.</p>
<dt><code>-header</code> or <code>-noheader</code></p>
<dd> Sepcify if you want the header to display or not. You can toggle this with the <code>h</code> key while <code>mytop</code> is running. </p>
<p> Default: header.</p>
<dt><code>-color</code> or <code>-nocolor</code></p>
<dd> Specify if you want a color display. This has no effect if you don&#8217;t have color support available. </p>
<p> Default: If you have color support, <code>mytop</code> will try color unless you tell it not to.</p>
<dt><code>-i</code> or <code>-idle</code> or <code>-noidle</code></p>
<dd> Specify if you want idle (sleeping) threads to appear in the list. If sleeping threads are omitted, the default sorting order is reversed so that the longest running queries appear at the top of the list. </p>
<p> Default: idle.</p>
<dt><code>-prompt</code> or <code>-noprompt</code></p>
<dd> Specify if you want to be prompted to type in your database password. This provides a little bit more security since it not only prevents the password from viewable in a process list, but also doesn&#8217;t require the password to be stored in plain text in your ~/.mytop config file. You will <code>only</code> be prompted if a password has not been specified in your config file or through another command line option. </p>
<p> Default: noprompt.</p>
<dt><code>-resolve</code></p>
<dd> If you have skip-resolve set on MySQL (to keep it from doing a reverse <font SIZE="-1">DNS</font> lookup on each inbound connection), mytop can replace <font SIZE="-1">IP</font> addresses with hostnames but toggling this option. </p>
<p> Default: noresolve</dl>
<p> Command-line arguments will always take precedence over config file options. That happens because the config file is read <i></i><font SIZE="-1"><i>BEFORE</i></font><i></i> the command-line arguments are applied.</p>
<h3>Config File</h3>
<p> Instead of always using bulky command-line parameters, you can also use a config file in your home directory (<tt>&quot;~/.mytop&quot;</tt>). If present, <code>mytop</code> will read it automatically. It is read <i>before</i> any of your command-line arguments are processed, so your command-line arguments will override directives in the config file. </p>
<p> Here is a sample config file <tt>&quot;~/.mytop&quot;</tt> which implements the defaults described above. </p>
<pre>
  user=root
  pass=
  host=localhost
  db=test
  delay=5
  port=3306
  socket=
  batchmode=0
  header=1
  color=1
  idle=1
</pre>
<p> Using a config file will help to ensure that your database password isn&#8217;t visible to users on the command-line. Just make sure that the permissions on <tt>&quot;~/.mytop&quot;</tt> are such that others cannot read it (unless you want them to, of course). </p>
<p> You may have white space on either side of the <tt>&quot;=&quot;</tt> in lines of the config file.</p>
<h3>Shortcut Keys</h3>
<p> The following keys perform various actions while <code>mytop</code> is running. Those which have not been implemented are listed as such. They are included to give the user idea of what is coming.</p>
<dl>
<dt><code>?</code></p>
<dd> Display help.</p>
<dt><code>c</code></p>
<dd> Show &#8220;command counters&#8221; based on the Com_* values in <font SIZE="-1">SHOW GLOBAL STATUS. </font> This is a new feature. Feedback welcome.</p>
<dt><code>d</code></p>
<dd> Show only threads connected to a particular database.</p>
<dt><code>f</code></p>
<dd> Given a thread id, display the entire query that thread was (and still may be) running.</p>
<dt><code>F</code></p>
<dd> Disable all filtering (host, user, and db).</p>
<dt><code>h</code></p>
<dd> Only show queries from a particular host.</p>
<dt><code>H</code></p>
<dd> Toggle the header display. You can also specify either <tt>&quot;header=0&quot;</tt> or <tt>&quot;header=1&quot;</tt> in your config file to set the default behavior.</p>
<dt><code>i</code></p>
<dd> Toggle the display of idle (sleeping) threads. If sleeping threads are filtered, the default sorting order is reversed so that the longest running queries appear at the top of the list.</p>
<dt><code>I</code></p>
<dd> Switch to InnoDB Status mode. The output of &#8220;<font SIZE="-1">SHOW INNODB STATUS&#8221;</font> will be displayed every cycle. In a future version, this may actually summarize that data rather than producing raw output.</p>
<dt><code>k</code></p>
<dd> Kill a thread.</p>
<dt><code>m</code></p>
<dd> Toggle modes. Currently this switches from `top&#8217; mode to `qps&#8217; (Queries Per Second Mode). In this mode, mytop will write out one integer per second. The number written reflects the number of queries executed by the server in the previous one second interval. </p>
<p> More modes may be added in the future.</p>
<dt><code>o</code></p>
<dd> Reverse the default sort order.</p>
<dt><code>p</code></p>
<dd> Pause display.</p>
<dt><code>q</code></p>
<dd> Quit <code>mytop</code></p>
<dt><code>r</code></p>
<dd> Reset the server&#8217;s status counters via a <i></i><font SIZE="-1"><i>FLUSH STATUS</i></font><i></i> command.</p>
<dt><code>s</code></p>
<dd> Change the sleep time (number of seconds between display refreshes).</p>
<dt><code>u</code></p>
<dd> Show only threads owned by a giver user.</dl>
<p> The <code>s</code> key has a command-line counterpart: <code>-s</code>. </p>
<p> The <code>h</code> key has two command-line counterparts: <code>-header</code> and <code>-noheader</code>.</p>
<h2>BUGS</h2>
<p> This is more of a <font SIZE="-1">BUGS +</font> WishList. </p>
<p> Some performance information is not available when talking to a version 3.22.x MySQL server. Additional information (about threads mostly) was added to the output of <i></i><font SIZE="-1"><i>SHOW STATUS</i></font><i></i> in MySQL 3.23.x and <code>mytop</code> makes use of it. If the information is not available, you will simply see zeros where the real numbers should be. </p>
<p> Simply running this program will increase your overall counters (such as the number of queries run). But you may or may not view that as a bug. </p>
<p> <code>mytop</code> consumes too much <font SIZE="-1">CPU</font> time when running (verified on older versions of Linux and FreeBSD). It&#8217;s likely a problem related to Term::ReadKey. I haven&#8217;t had time to investigate yet, so <code>mytop</code> now automatically lowers its priority when you run it. You may also think about running <code>mytop</code> on another workstation instead of your database server. However, <tt>&quot;mytop&quot;</tt> on Solaris does <code>not</code> have this problem. Newer versions of Linux and FreeBSD seem to have fixed this. </p>
<p> You can&#8217;t specify the maximum number of threads to list. If you have many threads and a tall xterm, <code>mytop</code> will always try to display as many as it can fit. </p>
<p> The size of most of the columns in the display has a small maximum width. If you have fairly long database/user/host names the display may appear odd. I have no good idea as to how best to deal with that yet. Suggestions are welcome. </p>
<p> It&#8217;d be nice if you could just add <code>mytop</code> configuration directives in your <tt>&quot;my.cnf&quot;</tt> file instead of having a separate config file. </p>
<p> You should be able to specify the columns you&#8217;d like to see in the display and the order in which they appear. If you only have one username that connects to your database, it&#8217;s probably not worth having the User column appear, for example.</p>
<h2>AUTHOR</h2>
<p> mytop was developed and is maintained by Jeremy D. Zawodny (Jeremy [at] Zawodny.com). </p>
<p> If you wish to e-mail me regarding this software, <font SIZE="-1"><code>PLEASE</code></font> subscribe to the <code>mytop</code> mailing list. See the <code>mytop</code> homepage for details.</p>
<h2>DISCLAIMER</h2>
<p> While I use this software in my job at Yahoo!, I am solely responsible for it. Yahoo! does not necessarily support this software in any way. It is merely a personal idea which happened to be very useful in my job.</p>
<h2>RECRUITING</h2>
<p> If you hack Perl and grok MySQL, come work at Yahoo! Contact me for details. Or just send me your resume. Er, unless we just had layoffs, in which case we&#8217;re not hiring. :-(</p>
<h2>SEE ALSO</h2>
<p> Please check the MySQL manual if you&#8217;re not sure where some of the output of <code>mytop</code> is coming from.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2001, Jeremy D. Zawodny.</p>
<h2>CREDITS</h2>
<p> Fix a bug. Add a feature. See your name here! </p>
<p> Many thanks go to these fine folks:</p>
<dl>
<dt>Sami Ahlroos (sami [at] avis-net.de)</p>
<dd> Suggested the idle/noidle stuff.</p>
<dt>Jan Willamowius (jan [at] janhh.shnet.org)</p>
<dd> Mirnor bug report. Documentation fixes.</p>
<dt>Alex Osipov (alex [at] acky.net)</p>
<dd> Long command-line options, Unix socket support.</p>
<dt>Stephane Enten (tuf [at] grolier.fr)</p>
<dd> Suggested batch mode.</p>
<dt>Richard Ellerbrock (richarde [at] eskom.co.za)</p>
<dd> Bug reports and usability suggestions.</p>
<dt>William R. Mattil (wrm [at] newton.irngtx.tel.gte.com)</p>
<dd> Bug report about empty passwords not working.</p>
<dt>Benjamin Pflugmann (philemon [at] spin.de)</p>
<dd> Suggested -P command-line flag as well as other changes.</p>
<dt>Justin Mecham &lt;justin [at] aspect.net&gt;</p>
<dd> Suggested setting <tt>$0</tt> to `mytop&#8217;.</p>
<dt>Thorsten Kunz &lt;thorsten.kunz [at] de.tiscali.com&gt;</p>
<dd> Provided a fix for cases when we try remove the domain name from the display even if it is actually an <font SIZE="-1">IP</font> address.</p>
<dt>Sasha Pachev &lt;sasha [at] mysql.com&gt;</p>
<dd> Provided the idea of real-time queries per second in the main display.</p>
<dt>Paul DuBois &lt;paul [at] snake.net&gt;</p>
<dd> Pointed out some option-handling bugs.</p>
<dt>Mike Wexler &lt;mwexler [at] tias.com&gt;</p>
<dd> Suggested that we don&#8217;t mangle (normalize) whitespace in query info by default.</p>
<dt>Mark Zweifel &lt;markez [at] yahoo-inc.com&gt;</p>
<dd> Make the &#8211;idle command-line argument negatable.</p>
<dt>Axel Schwenke &lt;schwenke [at] jobpilot.de&gt;</p>
<dd> Noticed the inccorect formula for query cache hit percentages in version 1.2.</p>
<dt>Steven Roussey &lt;sroussey [at] network54.com&gt;</p>
<dd> Supplied a patch to help filter binary junk in queries so that terminals don&#8217;t freak out.</p>
<dt>jon r. luini &lt;falcon [at] chime.com&gt;</p>
<dd> Supplied a patch that formed the basis for <tt>&quot;-prompt&quot;</tt> support. Sean Leach &lt;sleach [at] wiggum.com&gt; submitted a similar patch.</p>
<dt>Yogish Baliga &lt;baliga [at] yahoo-inc.com&gt;</p>
<dd> Supplied a patch that formed the basis for <tt>&quot;-resolve&quot;</tt> support.</p>
<dt>Per Andreas Buer &lt;perbu [at] linpro.no&gt;</p>
<dd> Supplied an excellent patch to tidy up the top display. This includes showing most values in short form, such as 10k rather than 10000.</dl>
<p> See the Changes file on the <code>mytop</code> distribution page for more details on what has changed.</p>
<h2>LICENSE</h2>
<p> <code>mytop</code> is licensed under the <font SIZE="-1">GNU</font> General Public License version 2. For the full license information, please visit <a rel="nofollow" href="http://www.gnu.org/copyleft/gpl.html">http://www.gnu.org/copyleft/gpl.html</a> </p>
<h2>Index</h2>
