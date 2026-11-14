---
title: "innfeed(1)"
name: "innfeed"
section: "1"
letter: "i"
url: "/docs/linux/man/1-innfeed/"
description: "innfeed – multi-host, multi-connection, streaming NNTP feeder."
---

<h2 class="name">NAME</h2>
<p> innfeed &#8211; multi-host, multi-connection, streaming NNTP feeder. </p>
<h2>SYNOPSIS</h2>
<p> <code>innfeed</code> [ <code>-a spool-dir</code> ] [ <code>-b</code><i> directory</i> ] [ <code>-C</code> ] [ <code>-c</code><i> filename</i> ] [ <code>-d</code><i> num</i> ] [ <code>-e</code><i> bytes</i> ] [ <code>-h</code> ] [ <code>-l</code><i> filename</i> ] [ <code>-m</code> ] [ <code>-M</code> ] [ <code>-o bytes</code> ] [ <code>-p file</code> ] [ <code>-S file</code> ] [ <code>-x </code> ] [ <code>-y</code> ] [ <code>-z </code> ] [ <code>-v</code> ] [ file ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Innfeed</i> implements the NNTP protocol for transferring news between computers. It handles the standard IHAVE protocol as well as the CHECK/TAKETHIS streaming extension. Innfeed can feed any number of remote hosts at once and will open multiple connections to each host if configured to do so. The only limitations are the process limits for open file descriptors and memory. </p>
<p> As an alternative to using NNTP, INN may also be fed to an IMAP server. This is done by using an executable called imapfeed, which is identical to innfeed except for the delivery process. The new version has two types of connections: an LMTP connection to deliver regular messages and an IMAP connection to handle control messages.</p>
<h2>MODES</h2>
<p> <i>Innfeed</i> has three modes of operation: channel, funnel-file and batch. </p>
<p> Channel mode is used when no filename is given on the command line, the &#8220;input-file&#8221; keyword is <i>not</i> given in the config file, <i>and</i> the &#8220;<i>-x</i>&#8221; option is <i>not</i> given. In channel mode innfeed runs with stdin connected via a pipe to innd. Whenever innd closes this pipe (and it has several reasons during normal processing to do so), innfeed will exit. It first will try to finish sending all articles it was in the middle of transmitting, before issuing a QUIT command. This means innfeed may take a while to exit depending on how slow your peers are. It never (well, almost never) just drops the connection. </p>
<p> The recommended way to restart innfeed when run in channel mode is therefore to tell innd to close the pipe and spawn a new innfeed process. This can be done with &#8220;ctlinnd flush &lt;feed&gt;&#8221; where &lt;feed&gt; is the name of the innfeed channel feed in &#8220;<i>newsfeeds</i>&#8221;. </p>
<p> Funnel-file mode is used when a filename is given as an argument or the &#8220;input-file&#8221; keyword is given in the config file. In funnel file mode it reads the specified file for the same formatted information as innd would give in channel mode. It is expected that innd is continually writing to this file, so when innfeed reaches the end of the file it will check periodically for new information. To prevent the funnel file from growing without bounds, you will need to periodically move the file to the side (or simply remove it) and have innd flush the file. Then, after the file is flushed by innd, you can send innfeed a SIGALRM, and it too will close the file and open the new file created by innd. Something like: </p>
<dl>
<dt>
<dd>
<pre>
innfeed -p /var/run/news/innfeed.pid my-funnel-file &amp;
while true; do
        sleep 43200
        rm -f my-funnel-file
        ctlinnd flush funnel-file-site
        kill -ALRM `cat /var/run/news/innfeed.pid`
done
</pre>
</dl>
<p> Batch mode is used when the &#8220;<i>-x</i>&#8221; flag is used. In batch mode innfeed will ignore stdin, and will simply process any backlog created by a previously running innfeed. This mode is not normally needed as innfeed will take care of backlog processing.</p>
<h2>CONFIGURATION</h2>
<p> Innfeed expects a couple of things to be able to run correctly: a directory where it can store backlog files and a configuration file to describe which peers it should handle. </p>
<p> The configuration file is described in <i><a href="/docs/linux/man/5-innfeed-conf/">innfeed.conf</a></i>(5). The &#8220;<i>-c</i>&#8221; option can be used to specify a different file. </p>
<p> For each peer (say, &#8220;<i>foo</i>&#8221;), innfeed manages up to 4 files in the backlog directory: a &#8220;<i>foo.lock</i>&#8221; file, which prevents other instances of innfeed from interfering with this one; a &#8220;<i>foo.input</i>&#8221; file which has old article information innfeed is reading for re-processing; a &#8220;<i>foo.output</i>&#8221; file where innfeed is writing information on articles that couldn&#8217;t be processed (normally due to a slow or blocked peer); and a &#8220;<i>foo</i>&#8221; file. </p>
<p> This last file (&#8220;<i>foo</i>&#8221;) is never created by innfeed, but if innfeed notices it, it will rename it to &#8220;<i>foo.input</i>&#8221; at the next opportunity and will start reading from it. This lets you create a batch file and put it in a place where innfeed will find it. You should never alter the .input or .output files of a running innfeed. </p>
<p> The format of these last three files is one of the following: </p>
<dl>
<dt>
<dd>
<pre>
/path/to/article &lt;message-id&gt;
@token@ &lt;message-id&gt;
</pre>
</dl>
<p> This is the same as the first two fields of the lines innd feeds to innfeed, and the same as the first two fields of the lines of the batch file innd will write if innfeed is unavailable for some reason. When innfeed processes its own batch files it ignores everything after the first two whitespace separated fields, so moving the innd-created batch file to the appropriate spot will work, even though the lines have extra fields. </p>
<p> The first field can also be a storage API token. The two types of lines can be intermingled; innfeed will use the storage manager if appropriate and otherwise treat the first field as a filename to read directly. </p>
<p> Innfeed writes its current status to the file &#8220;<i>innfeed.status</i>&#8221; (or the file given by the &#8220;<i>-S</i>&#8221; option). This file contains details on the process as a whole, and on each peer this instance of innfeed is managing. </p>
<p> If innfeed is told to send an article to a host it is not managing, then the article information will be put into a file matching the pattern &#8220;<i>innfeed-dropped.*</i>&#8221;, with part of the file name matching the pid of the innfeed process that is writing to it. Innfeed will not process this file except to write to it. If nothing is written to the file then it will be removed if innfeed exits normally.</p>
<h2>SIGNALS</h2>
<p> Upon receipt of a SIGALRM innfeed will close the funnel-file specified on the command line, and will reopen it (see funnel file description above). </p>
<p> Innfeed with catch SIGINT and will write a large debugging snapshot of the state of the running system. </p>
<p> Innfeed will catch SIGHUP and will reload the config file. See <i><a href="/docs/linux/man/5-innfeed-conf/">innfeed.conf</a></i>(5) for more details. </p>
<p> Innfeed will catch SIGCHLD and will close and reopen all backlog files. </p>
<p> Innfeed will catch SIGTERM and will do an orderly shutdown. </p>
<p> Upon receipt of a SIGUSR1 innfeed will increment the debugging level by one; receipt of a SIGUSR2 will decrement it by one. The debugging level starts at zero (unless the &#8220;-d&#8221; option it used), in which case no debugging information is emitted. A larger value for the level means more debugging information. Numbers up to 5 are currently useful.</p>
<h2>SYSLOG ENTRIES</h2>
<p> There are 3 different categories of syslog entries for statistics: Host, Connection and Global. </p>
<p> The Host statistics are generated for a given peer at regular intervals after the first connection is made (or, if the remote is unreachable, after spooling starts). The Host statistics give totals over all Connections that have been active during the given time frame. For example (broken here to fit the page, with &#8220;vixie&#8221; being the peer): </p>
<pre>
  May 23 12:49:08 data innfeed[16015]: vixie checkpoint
                seconds 1381 offered 2744 accepted 1286 
                refused 1021 rejected 437 missing 0 spooled 990
                on_close 0 unspooled 240 deferred 10 requeued 25
                queue 42.1/100:14,35,13,4,24,10
</pre>
<p> These meanings of these fields are:</p>
<dl>
<dt>seconds</p>
<dd> The time since innfeed connected to the host or since the statistics were reset by a &#8220;final&#8221; log entry.</p>
<dt>offered</p>
<dd> The number of IHAVE commands sent to the host if it is not in streaming mode. The sum of the number of TAKETHIS commands sent when no-CHECK mode is in effect plus the number CHECK commands sent in streaming mode (when no-CHECK mode is not in effect).</p>
<dt>accepted</p>
<dd> The number of articles which were sent to the remote host and accepted by it.</p>
<dt>refused</p>
<dd> The number of articles offered to the host that it it indicated it didn&#8217;t want because it had already seen the Message-ID. The remote host indicates this by sending a 435 response to an IHAVE command or a 438 response to a CHECK command.</p>
<dt>rejected</p>
<dd> The number of articles transferred to the host that it did not accept because it determined either that it already had the article or it did not want it because of the article&#8217;s Newsgroups: or Distribution: headers, etc. The remote host indicates that it is rejecting the article by sending a 437 or 439 response after innfeed sent the entire article.</p>
<dt>missing</p>
<dd> The number of articles which innfeed was told to offer to the host but which were not present in the article spool. These articles were probably cancelled or expired before innfeed was able to offer them to the host.</p>
<dt>spooled</p>
<dd> The number of article entries that were written to the .output backlog file because the articles could not either be sent to the host or be refused by it. Articles are generally spooled either because new articles are arriving more quickly than they can be offered to the host, or because innfeed closed all the connections to the host and pushed all the articles currently in progress to the .output backlog file.</p>
<dt>on_close</p>
<dd> The number of articles that were spooled when innfeed closed all the connections to the host.</p>
<dt>unspooled</p>
<dd> The number of article entries that were read from the .input backlog file.</p>
<dt>deferred</p>
<dd> The number of articles that the host told innfeed to retry later by sending a 431 or 436 response. Innfeed immediately puts these articles back on the tail of the queue.</p>
<dt>requeued</p>
<dd> The number of articles that were in progress on connections when innfeed dropped those connections and put the articles back on the queue. These connections may have been broken by a network problem or became unresponsive causing innfeed to time them out.</p>
<dt>queue</p>
<dd> The first number is the average (mean) queue size during the previous logging interval. The second number is the maximum allowable queue size. The third number is the percentage of the time that the queue was empty. The fourth through seventh numbers are the percentages of the time that the queue was &gt;0% to 25% full, 25% to 50% full, 50% to 75% full, and 75% to &lt;100% full. The last number is the percentage of the time that the queue was totally full.</dl>
<p> If the &#8220;<i>-z</i>&#8221; option is used (see below), then when the peer stats are generated, each Connection will log its stats too. For example, for connection number zero (from a set of five): </p>
<pre>
  May 23 12:49:08 data innfeed[16015]: vixie:0 checkpoint
                seconds 1381 offered 596 accepted 274 
                refused 225 rejected 97
</pre>
<p> If you only open a maximum of one Connection to a remote, then there will be a close correlation between Connection numbers and Host numbers, but in general you can&#8217;t tie the two sets of number together in any easy or very meaningful way. When a Connection closes it will always log its stats. </p>
<p> If all Connections for a Host get closed together, then the Host logs its stats as &#8220;final&#8221; and resets its counters. If the feed is so busy that there&#8217;s always at least one Connection open and running, then after some amount of time (set via the config file), the Host stats are logged as final and reset. This is to make generating higher level stats from log files, by other programs, easier. </p>
<p> There is one log entry that is emitted for a Host just after its last Connection closes and innfeed is preparing to exit. This entry contains counts over the entire life of the process. The &#8220;seconds&#8221; field is from the first time a Connection was successfully built, or the first time spooling started. If a Host has been completely idle, it will have no such log entry. </p>
<pre>
  May 23 12:49:08 data innfeed[16015]: decwrl global 
                seconds 1381 offered 34 accepted 22 
                refused 3 rejected 7 missing 0
</pre>
<p> The final log entry is emitted immediately before exiting. It contains a summary of the statistics over the entire life of the process. </p>
<pre>
  Feb 13 14:43:41 data innfeed-0.9.4[22344]: ME global
                seconds 15742 offered 273441 accepted 45750
                refused 222008 rejected 3334 missing 217
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> The &#8220;<i>-a</i>&#8221; flag is used to specify the top of the article spool tree. Innfeed does a <a href="/docs/linux/man/2-chdir/">chdir</a>(2) to this directory, so it should probably be an absolute path. The default is &lt;patharticles in inn.conf&gt;.</p>
<dt><code>-b</code></p>
<dd> The &#8220;<i>-b</i>&#8221; flag may be used to specify a different directory for backlog file storage and retrieval. If the path is relative then it is relative to &lt;pathspool in inn.conf&gt;. The default is &#8220;<i>innfeed</i>&#8221;.</p>
<dt><code>-c</code></p>
<dd> The &#8220;<i>-c</i>&#8221; flag may be used to specify a different config file from the default value. If the path is relative then it is relative to &lt;pathetc in inn.conf&gt;. The default is &#8220;<i>innfeed.conf</i>&#8221;.</p>
<dt><code>-C </code></p>
<dd> The &#8220;<i>-C</i>&#8221; flag is used to have innfeed simply check the config file, report on any errors and then exit.</p>
<dt><code>-d </code></p>
<dd> The &#8220;<i>-d</i>&#8221; flag may be used to specify the initial logging level. All debugging messages go to stderr (which may not be what you want, see the &#8220;<i>-l</i>&#8221; flag below).</p>
<dt><code>-e</code></p>
<dd> The &#8220;<i>-e</i>&#8221; flag may be used to specify the size limit (in bytes) for the <i>.output</i> backlog files innfeed creates. If the output file gets bigger than 10% more than the given number, innfeed will replace the output file with the tail of the original version. The default value is 0, which means there is no limit.</p>
<dt><code>-h</code></p>
<dd> Use the &#8220;<i>-h</i>&#8221; flag to print the usage message.</p>
<dt><code>-l</code></p>
<dd> The &#8220;<i>-l</i>&#8221; flag may be used to specify a different log file from stderr. As innd starts innfeed with stderr attached to /dev/null, using this option can be useful in catching any abnormal error messages, or any debugging messages (all &#8220;normal&#8221; errors messages go to syslog).</p>
<dt><code>-M</code></p>
<dd> If innfeed has been built with mmap support, then the &#8220;<i>-M</i>&#8221; flag turns OFF the use of mmap(); otherwise it has no effect.</p>
<dt><code>-m</code></p>
<dd> The &#8220;<i>-m</i>&#8221; flag is used to turn on logging of all missing articles. Normally if an article is missing, innfeed keeps a count, but logs no further information. When this flag is used, details about message-id and expected pathname are logged.</p>
<dt><code>-o</code></p>
<dd> The &#8220;<i>-o</i>&#8221; flag sets a value of the maximum number of bytes of article data innfeed is supposed to keep in memory. This doesn&#8217;t work properly yet.</p>
<dt><code>-p </code></p>
<dd> The &#8220;<i>-p</i>&#8221; flag is used to specify the filename to write the pid of the process into. A relative path is relative to &lt;pathrun in inn.conf&gt;. The default is &#8220;<i>innfeed.pid</i>&#8221;.</p>
<dt><code>-S</code></p>
<dd> The &#8220;<i>-S</i>&#8221; flag specifies the name of the file to write the periodic staus to. If the path is relative it is considered relative to &lt;pathlog in inn.conf&gt;. The default is &#8220;<i>innfeed.status</i>&#8221;.</p>
<dt><code>-v</code></p>
<dd> When the &#8220;<i>-v</i>&#8221; flag is given, version information is printed to stderr and then innfeed exits.</p>
<dt><code>-x</code></p>
<dd> The &#8220;<i>-x</i>&#8221; flag is used to tell innfeed not to expect any article information from innd but just to process any backlog files that exist and then exit.</p>
<dt><code>-y</code></p>
<dd> The &#8220;<i>-y</i>&#8221; flag is used to allow dynamic peer binding. If this flag is used and article information is received from innd that specifies an unknown peer, then the peer name is taken to be the IP name too, and an association with it is created. Using this it is possible to only have the global defaults in the <i>innfeed.conf</i> file, provided the peername as used by innd is the same as the ip name. Note that <i>innfeed</i> with &#8220;<i>-y</i>&#8221; and no peer in <i>innfeed.conf</i> would cause a problem that <i>innfeed</i> drops the first article.</p>
<dt><code>-z</code></p>
<dd> The &#8220;<i>-z</i>&#8221; flag is used to cause each connection, in a parallel feed configuration, to report statistics when the controller for the connections prints its statistics.</p>
<dt>
<dd></dl>
<h2>BUGS</h2>
<p> When using the &#8220;-x&#8221; option, the config file entry&#8217;s &#8220;initial-connections&#8221; field will be the total number of connections created and used, no matter how many big the batch file, and no matter how big the &#8220;max-connectiond&#8221; field specifies. Thus a value of 0 for &#8220;initial-connections&#8221; means nothing will happen in &#8220;-x&#8221; mode. </p>
<p> Innfeed does not automatically grab the file out of out.going&#8211;this needs to be prepared for it by external means. </p>
<p> Probably too many other bugs to count.</p>
<h2>FILES</h2>
<p> innfeed.conf<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>config file.</p>
<p> innfeed<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>directory for backlog files.</p>
<h2>HISTORY</h2>
<p> Written by James Brister &lt;brister [at] vix.com&gt; for InterNetNews. This is revision 7799, dated 2008-04-26.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-innfeed-conf/">innfeed.conf</a>(5)</i> </p>
<h2>Index</h2>
