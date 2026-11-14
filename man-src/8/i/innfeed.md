---
title: "innfeed(8)"
name: "innfeed"
section: "8"
letter: "i"
url: "/docs/linux/man/8-innfeed/"
description: "innfeed, imapfeed – Multi-host, multi-connection, streaming NNTP feeder"
---

<p>innfeed, imapfeed &#8211; Multi-host, multi-connection, streaming NNTP feeder</p>
<h2>Synopsis</h2>
<p><code>innfeed</code> [<code>-ChmMvxyz</code>] [<code>-a</code> <i>spool-dir</i>] [<code>-b</code> <i>directory</i>] [<code>-c</code> <i>config-file</i>] [<code>-d</code> <i>log-level</i>] [<code>-e</code> <i>bytes</i>] [<code>-l</code> <i>logfile</i>] [<code>-o</code> <i>bytes</i>] [<code>-p</code> <i>pid-file</i>] [<code>-s</code> <i>command</i>] [<code>-S</code> <i>status-file</i>] [<i>file</i>]</p>
<h2>Description</h2>
<p><code>innfeed</code> implements the <font SIZE="-1">NNTP</font> protocol for transferring news between computers. It handles the standard <font SIZE="-1">IHAVE</font> protocol as well as the <font SIZE="-1">CHECK/TAKETHIS</font> streaming extension. <code>innfeed</code> can feed any number of remote hosts at once and will open multiple connections to each host if configured to do so. The only limitations are the process limits for open file descriptors and memory. </p>
<p> As an alternative to using <font SIZE="-1">NNTP</font>, <font SIZE="-1">INN</font> may also be fed to an <font SIZE="-1">IMAP</font> server. This is done by using an executable called <code>imapfeed</code>, which is identical to <code>innfeed</code> except for the delivery process. The new version has two types of connections: an <font SIZE="-1">LMTP</font> connection to deliver regular messages and an <font SIZE="-1">IMAP</font> connection to handle control messages.</p>
<h2>Modes</h2>
<p><code>innfeed</code> has three modes of operation: channel, funnel-file and batch. </p>
<p> Channel mode is used when no filename is given on the command line, the <i>input-file</i> keyword is <i>not</i> given in the config file, <i>and</i> the <code>-x</code> option is <i>not</i> given. In channel mode, <code>innfeed</code> runs with stdin connected via a pipe to <code>innd</code>. Whenever <code>innd</code> closes this pipe (and it has several reasons during normal processing to do so), <code>innfeed</code> will exit. It first will try to finish sending all articles it was in the middle of transmitting, before issuing a <font SIZE="-1">QUIT</font> command. This means <code>innfeed</code> may take a while to exit depending on how slow your peers are. It never (well, almost never) just drops the connection. The recommended way to restart <code>innfeed</code> when run in channel mode is therefore to tell <code>innd</code> to close the pipe and spawn a new <code>innfeed</code> process. This can be done with <tt>&quot;ctlinnd flush </tt>feed<tt>&quot;</tt> where <i>feed</i> is the name of the <code>innfeed</code> channel feed in the <i>newsfeeds</i> file. </p>
<p> Funnel-file mode is used when a filename is given as an argument or the <i>input-file</i> keyword is given in the config file. In funnel-file mode, it reads the specified file for the same formatted information as <code>innd</code> would give in channel mode. It is expected that <code>innd</code> is continually writing to this file, so when <code>innfeed</code> reaches the end of the file, it will check periodically for new information. To prevent the funnel file from growing without bounds, you will need to periodically move the file to the side (or simply remove it) and have <code>innd</code> flush the file. Then, after the file is flushed by <code>innd</code>, you can send <code>innfeed</code> a <font SIZE="-1">SIGALRM</font>, and it too will close the file and open the new file created by <code>innd</code>. Something like: </p>
<pre> innfeed -p &lt;pathrun in inn.conf&gt;/innfeed.pid my-funnel-file &amp;
 while true; do
 sleep 43200
 rm -f my-funnel-file
 ctlinnd flush funnel-file-site
 kill -ALRM `cat &lt;pathrun&gt;/innfeed.pid`
 done</pre>
<p>Batch mode is used when the <code>-x</code> flag is used. In batch mode, <code>innfeed</code> will ignore stdin, and will simply process any backlog created by a previously running <code>innfeed</code>. This mode is not normally needed as <code>innfeed</code> will take care of backlog processing.</p>
<h2>Configuration</h2>
<p><code>innfeed</code> expects a couple of things to be able to run correctly: a directory where it can store backlog files and a configuration file to describe which peers it should handle. </p>
<p> The configuration file is described in <i><a href="/docs/linux/man/5-innfeed-conf/">innfeed.conf</a></i>(5). The <code>-c</code> option can be used to specify a different file. For each peer (say, <tt>&quot;foo&quot;</tt>), <code>innfeed</code> manages up to 4 files in the backlog directory:</p>
<dl>
<dt>&bull;</p>
<dd>A <i>foo.lock</i> file, which prevents other instances of <code>innfeed</code> from interfering with this one.</p>
<dt>&bull;</p>
<dd>A <i>foo.input</i> file which has old article information <code>innfeed</code> is reading for re-processing.</p>
<dt>&bull;</p>
<dd>A <i>foo.output</i> file where <code>innfeed</code> is writing information on articles that could not be processed (normally due to a slow or blocked peer).</p>
<dt>&bull;</p>
<dd>A <i>foo</i> file that is never created by <code>innfeed</code>, but if <code>innfeed</code> notices it, it will rename it to <i>foo.input</i> at the next opportunity and will start reading from it. This lets you create a batch file and put it in a place where <code>innfeed</code> will find it.</dl>
<p> You should never alter the <i>foo.input</i> or <i>foo.output</i> files of a running <code>innfeed</code>. The format of these last three files is one of the following: </p>
<pre> /path/to/article &lt;message-id&gt;
 @token@ &lt;message-id&gt;</pre>
<p>This is the same as the first two fields of the lines <code>innd</code> feeds to <code>innfeed</code>, and the same as the first two fields of the lines of the batch file <code>innd</code> will write if <code>innfeed</code> is unavailable for some reason. When <code>innfeed</code> processes its own batch files, it ignores everything after the first two whitespace separated fields, so moving the <code>innd</code>-created batch file to the appropriate spot will work, even though the lines have extra fields. </p>
<p> The first field can also be a storage <font SIZE="-1">API</font> token. The two types of lines can be intermingled; <code>innfeed</code> will use the storage manager if appropriate, and otherwise treat the first field as a filename to read directly. </p>
<p> <code>innfeed</code> writes its current status to the file <i>innfeed.status</i> (or the file given by the <code>-S</code> option). This file contains details on the process as a whole, and on each peer this instance of <code>innfeed</code> is managing. </p>
<p> If <code>innfeed</code> is told to send an article to a host it is not managing, then the article information will be put into a file matching the pattern <i>innfeed-dropped.*</i>, with part of the file name matching the pid of the <code>innfeed</code> process that is writing to it. <code>innfeed</code> will not process this file except to write to it. If nothing is written to the file, then it will be removed if <code>innfeed</code> exits normally. Otherwise, the file remains, and <code>procbatch</code> can be invoked to process it afterwards.</p>
<h2>Signals</h2>
<p>Upon receipt of a <font SIZE="-1">SIGALRM</font>, <code>innfeed</code> will close the funnel file specified on the command line, and will reopen it (see funnel file description above). </p>
<p> <code>innfeed</code> with catch <font SIZE="-1">SIGINT</font> and will write a large debugging snapshot of the state of the running system. </p>
<p> <code>innfeed</code> will catch <font SIZE="-1">SIGHUP</font> and will reload both the config and the log files. See <i><a href="/docs/linux/man/5-innfeed-conf/">innfeed.conf</a></i>(5) for more details. </p>
<p> <code>innfeed</code> will catch <font SIZE="-1">SIGCHLD</font> and will close and reopen all backlog files. </p>
<p> <code>innfeed</code> will catch <font SIZE="-1">SIGTERM</font> and will do an orderly shutdown. </p>
<p> Upon receipt of a <font SIZE="-1">SIGUSR1</font>, <code>innfeed</code> will increment the debugging level by one; receipt of a <font SIZE="-1">SIGUSR2</font> will decrement it by one. The debugging level starts at zero (unless the <code>-d</code> option it used), in which case no debugging information is emitted. A larger value for the level means more debugging information. Numbers up to 5 are currently useful.</p>
<h2>Syslog Entries</h2>
<p>There are 3 different categories of syslog entries for statistics: host, connection and global. </p>
<p> The host statistics are generated for a given peer at regular intervals after the first connection is made (or, if the remote is unreachable, after spooling starts). The host statistics give totals over all connections that have been active during the given time frame. For example (broken here to fit the page, with <tt>&quot;vixie&quot;</tt> being the peer): </p>
<pre> May 23 12:49:08 news innfeed[16015]: vixie checkpoint
 seconds 1381 offered 2744 accepted 1286 refused 1021 rejected 437
 missing 0 accsize 8506220 rejsize 142129 spooled 990
 on_close 0 unspooled 240 deferred 10/15.3 requeued 25
 queue 42.1/100:14,35,13,4,24,10</pre>
<p>The meanings of these fields are:</p>
<dl>
<dt>seconds</p>
<dd>The time since <code>innfeed</code> connected to the host or since the statistics were reset by a <tt>&quot;final&quot;</tt> log entry.</p>
<dt>offered</p>
<dd>The number of <font SIZE="-1">IHAVE</font> commands sent to the host if it is not in streaming mode. The sum of the number of <font SIZE="-1">TAKETHIS</font> commands sent when no-CHECK mode is in effect plus the number of <font SIZE="-1">CHECK</font> commands sent in streaming mode (when no-CHECK mode is not in effect).</p>
<dt>accepted</p>
<dd>The number of articles which were sent to the remote host and accepted by it.</p>
<dt>refused</p>
<dd>The number of articles offered to the host that it indicated it did not want because it had already seen the message-ID. The remote host indicates this by sending a 435 response to an <font SIZE="-1">IHAVE</font> command or a 438 response to a <font SIZE="-1">CHECK</font> command.</p>
<dt>rejected</p>
<dd>The number of articles transferred to the host that it did not accept because it determined either that it already had the article or it did not want it because of the article&#8217;s Newsgroups: or Distribution: header fields, etc. The remote host indicates that it is rejecting the article by sending a 437 or 439 response after <code>innfeed</code> sent the entire article.</p>
<dt>missing</p>
<dd>The number of articles which <code>innfeed</code> was told to offer to the host but which were not present in the article spool. These articles were probably cancelled or expired before <code>innfeed</code> was able to offer them to the host.</p>
<dt>accsize</p>
<dd>The number of bytes of all accepted articles transferred to the host.</p>
<dt>rejsize</p>
<dd>The number of bytes of all rejected articles transferred to the host.</p>
<dt>spooled</p>
<dd>The number of article entries that were written to the <i>.output</i> backlog file because the articles either could not be sent to the host or were refused by it. Articles are generally spooled either because new articles are arriving more quickly than they can be offered to the host, or because <code>innfeed</code> closed all the connections to the host and pushed all the articles currently in progress to the <i>.output</i> backlog file.</p>
<dt>on_close</p>
<dd>The number of articles that were spooled when <code>innfeed</code> closed all the connections to the host.</p>
<dt>unspooled</p>
<dd>The number of article entries that were read from the <i>.input</i> backlog file.</p>
<dt>deferred</p>
<dd>The first number is the number of articles that the host told <code>innfeed</code> to retry later by sending a 431 or 436 response. <code>innfeed</code> immediately puts these articles back on the tail of the queue. </p>
<p> The second number is the average (mean) size of deferred articles during the previous logging interval</p>
<dt>requeued</p>
<dd>The number of articles that were in progress on connections when <code>innfeed</code> dropped those connections and put the articles back on the queue. These connections may have been broken by a network problem or became unresponsive causing <code>innfeed</code> to time them out.</p>
<dt>queue</p>
<dd>The first number is the average (mean) queue size during the previous logging interval. The second number is the maximum allowable queue size. The third number is the percentage of the time that the queue was empty. The fourth through seventh numbers are the percentages of the time that the queue was &gt;0% to 25% full, 25% to 50% full, 50% to 75% full, and 75% to &lt;100% full. The last number is the percentage of the time that the queue was totally full.</dl>
<p> If the <code>-z</code> option is used (see below), then when the peer stats are generated, each connection will log its stats too. For example, for connection number zero (from a set of five): </p>
<pre> May 23 12:49:08 news innfeed[16015]: vixie:0 checkpoint
 seconds 1381 offered 596 accepted 274 refused 225
 rejected 97 accsize 773623 rejsize 86591</pre>
<p>If you only open a maximum of one connection to a remote, then there will be a close correlation between connection numbers and host numbers, but in general you cannot tie the two sets of number together in any easy or very meaningful way. When a connection closes, it will always log its stats. </p>
<p> If all connections for a host get closed together, then the host logs its stats as <tt>&quot;final&quot;</tt> and resets its counters. If the feed is so busy that there is always at least one connection open and running, then after some amount of time (set via the config file), the host stats are logged as final and reset. This is to make generating higher level stats from log files, by other programs, easier. </p>
<p> There is one log entry that is emitted for a host just after its last connection closes and <code>innfeed</code> is preparing to exit. This entry contains counts over the entire life of the process. The <tt>&quot;seconds&quot;</tt> field is from the first time a connection was successfully built, or the first time spooling started. If a host has been completely idle, it will have no such log entry. </p>
<pre> May 23 12:49:08 news innfeed[16015]: decwrl global
 seconds 1381 offered 34 accepted 22 refused 3 rejected 7
 missing 0 accsize 81277 rejsize 12738 spooled 0 unspooled 0</pre>
<p>The final log entry is emitted immediately before exiting. It contains a summary of the statistics over the entire life of the process. </p>
<pre> Feb 13 14:43:41 news innfeed[22344]: ME global
 seconds 15742 offered 273441 accepted 45750 refused 222008
 rejected 3334 missing 217 accsize 93647166 rejsize 7421839
 spooled 10 unspooled 0</pre>
<h2>Options</h2>
<p><code>innfeed</code> takes the following options.</p>
<dl>
<dt><code>-a</code> <i>spool-dir</i></p>
<dd>The <code>-a</code> flag is used to specify the top of the article spool tree. <code>innfeed</code> does a <i><a href="/docs/linux/man/2-chdir/">chdir</a></i>(2) to this directory, so it should probably be an absolute path. The default is <i>patharticles</i> as set in <i>inn.conf</i>.</p>
<dt><code>-b</code> <i>directory</i></p>
<dd>The <code>-b</code> flag may be used to specify a different directory for backlog file storage and retrieval, as well as for lock files. If the path is relative, then it is relative to <i>pathspool</i> as set in <i>inn.conf</i>. The default is <tt>&quot;innfeed&quot;</tt>.</p>
<dt><code>-c</code> <i>config-file</i></p>
<dd>The <code>-c</code> flag may be used to specify a different config file from the default value. If the path is relative, then it is relative to <i>pathetc</i> as set in <i>inn.conf</i>. The default is <i>innfeed.conf</i>.</p>
<dt><code>-C</code></p>
<dd>The <code>-C</code> flag is used to have <code>innfeed</code> simply check the config file, report on any errors and then exit.</p>
<dt><code>-d</code> <i>log-level</i></p>
<dd>The <code>-d</code> flag may be used to specify the initial logging level. All debugging messages go to stderr (which may not be what you want, see the <code>-l</code> flag below).</p>
<dt><code>-e</code> <i>bytes</i></p>
<dd>The <code>-e</code> flag may be used to specify the size limit (in bytes) for the <i>.output</i> backlog files <code>innfeed</code> creates. If the output file gets bigger than 10% more than the given number, <code>innfeed</code> will replace the output file with the tail of the original version. The default value is <tt>0</tt>, which means there is no limit.</p>
<dt><code>-h</code></p>
<dd>Use the <code>-h</code> flag to print the usage message.</p>
<dt><code>-l</code> <i>logfile</i></p>
<dd>The <code>-l</code> flag may be used to specify a different log file from stderr. As <code>innd</code> starts <code>innfeed</code> with stderr attached to /dev/null, using this option can be useful in catching any abnormal error messages, or any debugging messages (all &#8220;normal&#8221; errors messages go to syslog).</p>
<dt><code>-m</code></p>
<dd>The <code>-m</code> flag is used to turn on logging of all missing articles. Normally, if an article is missing, <code>innfeed</code> keeps a count, but logs no further information. When this flag is used, details about message-IDs and expected path names are logged.</p>
<dt><code>-M</code></p>
<dd>If <code>innfeed</code> has been built with mmap support, then the <code>-M</code> flag turns <font SIZE="-1">OFF</font> the use of <i>mmap()</i>; otherwise, it has no effect.</p>
<dt><code>-o</code> <i>bytes</i></p>
<dd>The <code>-o</code> flag sets a value of the maximum number of bytes of article data <code>innfeed</code> is supposed to keep in memory. This does not work properly yet.</p>
<dt><code>-p</code> <i>pid-file</i></p>
<dd>The <code>-p</code> flag is used to specify the file name to write the pid of the process into. A relative path is relative to <i>pathrun</i> as set in <i>inn.conf</i>. The default is <i>innfeed.pid</i>.</p>
<dt><code>-s</code> <i>command</i></p>
<dd>The <code>-s</code> flag specifies the name of a command to run in a subprocess and read article information from. This is similar to channel mode operation, only that <i>command</i> takes the place usually occupied by <code>innd</code>.</p>
<dt><code>-S</code> <i>status-file</i></p>
<dd>The <code>-S</code> flag specifies the name of the file to write the periodic status to. If the path is relative, it is considered relative to <i>pathlog</i> as set in <i>inn.conf</i>. The default is <i>innfeed.status</i>.</p>
<dt><code>-v</code></p>
<dd>When the <code>-v</code> flag is given, version information is printed to stderr and then <code>innfeed</code> exits.</p>
<dt><code>-x</code></p>
<dd>The <code>-x</code> flag is used to tell <code>innfeed</code> not to expect any article information from <code>innd</code> but just to process any backlog files that exist and then exit.</p>
<dt><code>-y</code></p>
<dd>The <code>-y</code> flag is used to allow dynamic peer binding. If this flag is used and article information is received from <code>innd</code> that specifies an unknown peer, then the peer name is taken to be the <font SIZE="-1">IP</font> name too, and an association with it is created. Using this, it is possible to only have the global defaults in the <i>innfeed.conf</i> file, provided the peer name as used by <code>innd</code> is the same as the <font SIZE="-1">IP</font> name. </p>
<p> Note that <code>innfeed</code> with <code>-y</code> and no peer in <i>innfeed.conf</i> would cause a problem that <code>innfeed</code> drops the first article.</p>
<dt><code>-z</code></p>
<dd>The <code>-z</code> flag is used to cause each connection, in a parallel feed configuration, to report statistics when the controller for the connections prints its statistics.</dl>
<h2>Bugs</h2>
<p>When using the <code>-x</code> option, the config file entry&#8217;s <i>initial-connections</i> field will be the total number of connections created and used, no matter how many big the batch file, and no matter how big the <i>max-connections</i> field specifies. Thus a value of <tt>0</tt> for <i>initial-connections</i> means nothing will happen in <code>-x</code> mode. </p>
<p> <code>innfeed</code> does not automatically grab the file out of <i>pathoutgoing</i>. This needs to be prepared for it by external means. </p>
<p> Probably too many other bugs to count.</p>
<h2>Alternative</h2>
<p>An alternative to <code>innfeed</code> can be <code>innduct</code>, maintained by Ian Jackson and available at <a rel="nofollow" href="http://www.chiark.greenend.org.uk/ucgi/~ian/git-manpage/innduct.git/innduct.8">http://www.chiark.greenend.org.uk/ucgi/~ian/git-manpage/innduct.git/innduct.8</a> &lt;<a href="http://www.chiark.greenend.org.uk/ucgi/~ian/git-manpage/innduct.git/innduct.8">http://www.chiark.greenend.org.uk/ucgi/~ian/git-manpage/innduct.git/innduct.8</a>&gt;. It is intended to solve a design issue in the way <code>innfeed</code> works. As a matter of fact, the program feed protocol spoken between <code>innd</code> and <code>innfeed</code> is lossy: if <code>innfeed</code> dies unexpectedly, articles which <code>innd</code> has written to the pipe to <code>innfeed</code> will be skipped. <code>innd</code> has no way of telling which articles those are, no useful records, and no attempts to resend these articles.</p>
<h2>Files</h2>
<dl>
<dt><i>pathbin</i>/innfeed</p>
<dd>The binary program itself.</p>
<dt><i>pathetc</i>/innfeed.conf</p>
<dd>The configuration file.</p>
<dt><i>pathspool</i>/innfeed</p>
<dd>The directory for backlog files.</dl>
<h2>History</h2>
<p>Written by James Brister &lt;brister [at] vix.com&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> Earlier versions of <code>innfeed</code> (up to 0.10.1) were shipped separately; <code>innfeed</code> is now part of <font SIZE="-1">INN</font> and shares the same version number. </p>
<p> <tt>$Id:</tt> innfeed.pod 9590 2013-12-19 17:48:22Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/5-innfeed-conf/">innfeed.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/8-procbatch/">procbatch</a></i>(8). </p>
