---
title: "innd(8)"
name: "innd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-innd/"
description: "innd – InterNetNews daemon"
---

<p>innd &#8211; InterNetNews daemon</p>
<h2>Synopsis</h2>
<p><code>innd</code> [<code>-aCdfNrsSu</code>] [<code>-4</code> <i>address</i>] [<code>-6</code> <i>address</i>] [<code>-c</code> <i>days</i>] [<code>-H</code> <i>count</i>] [<code>-i</code> <i>count</i>] [<code>-l</code> <i>size</i>] [<code>-m</code> <i>mode</i>] [<code>-n</code> <i>flag</i>] [<code>-o</code> <i>count</i>] [<code>-P</code> <i>port</i>] [<code>-t</code> <i>timeout</i>] [<code>-T</code> <i>count</i>] [<code>-X</code> <i>seconds</i>]</p>
<h2>Description</h2>
<p><code>innd</code>, the InterNetNews daemon, handles all incoming <font SIZE="-1">NNTP</font> feeds, coordinates the storage, retransmission, and overview generation for all accepted articles, and manages the <i><a href="/docs/linux/man/5-active/">active</a></i>(5) and <i><a href="/docs/linux/man/5-history/">history</a></i>(5) databases. It handles incoming connections on the <font SIZE="-1">NNTP</font> port, and also creates and listens to a local Unix-domain stream socket in order to receive articles from local processes such as <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8) and <i><a href="/docs/linux/man/1-rnews/">rnews</a></i>(1). </p>
<p> As the master daemon, <code>innd</code> should generally be started at boot and be always running. It listens to a Unix-domain datagram socket for commands to control its activities, commands that can be sent using <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8). The current status of <code>innd</code> can be obtained by running <tt>&quot;ctlinnd mode&quot;</tt>, or for more detailed output, <i><a href="/docs/linux/man/8-innstat/">innstat</a></i>(8). </p>
<p> <code>innd</code> can be in one of three operating modes: running, paused, or throttled. Running is the normal mode; when the server is throttled, it closes connections and rejects new ones. Paused is like a temporary throttle, suspending <code>innd</code>&#8216;s activities but not causing the server to shut down existing connections. The mode is normally changed via <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), either by various automated processes (such as nightly article expiration) or manually by the news administrator, but <code>innd</code> will also throttle itself if it encounters <font SIZE="-1">ENOSPC</font> errors in writing data or an excessive number of I/O errors (among other problems). </p>
<p> <code>innd</code> normally takes care of spawning <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8) to handle connections from news reading clients, but it can be run on a separate port from <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8) so that feed connections and news reading connections are handled separately (this can often be faster). Normally, <code>innd</code> listens on port 119, the assigned port for <font SIZE="-1">NNTP</font>; if it is desirable to run <code>innd</code> and <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8) on separate ports, it&#8217;s recommended that <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8) be given port 119 (since many news reading clients connect only to that port) and that port 433 be used for <code>innd</code>. </p>
<p> The primary configuration files that control <code>innd</code>&#8216;s activities are <i>incoming.conf</i>, which specifies what remote sites <code>innd</code> will accept connections from, <i>newsfeeds</i>, which specifies what is to be done with incoming articles besides storing them, and <i>inn.conf</i>, which sets a wide variety of configuration parameters. Some parameters in <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5) can also be set with command-line flags; for these, the command-line flags take precedence if used. </p>
<p> <code>innd</code> must be run as the news user and news group. It will check for this at startup and fail to start if not run properly. Normally it should be started via <i><a href="/docs/linux/man/8-rc-news/">rc.news</a></i>(8) as part of the system boot up process. It relies on the setuid root helper program <i><a href="/docs/linux/man/8-innbind/">innbind</a></i>(8) to listen on a privileged port (119, 433 or 563).</p>
<h2>Options</h2>
<p>For the options below that override <i>inn.conf</i> settings, see <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5) for the default values if neither the <i>inn.conf</i> setting nor the command-line option is given.</p>
<dl>
<dt><code>-4</code> <i>address</i></p>
<dd>Normally, <code>innd</code> binds to all local <font SIZE="-1">IP</font> addresses (unless <i>bindaddress</i> is set in <i>inn.conf</i>). If this option is given, it specifies the <font SIZE="-1">IP</font> address that <font SIZE="-1">INN</font> should bind as. This is only relevant for servers with multiple local <font SIZE="-1">IP</font> addresses. The <font SIZE="-1">IP</font> address must be in dotted-quad (<tt>&quot;nnn.nnn.nnn.nnn&quot;</tt>) format. </p>
<p> If this option is specified, it&#8217;s the same as setting <i>bindaddress</i> in <i>inn.conf</i> and may cause changes in whether <font SIZE="-1">INN</font> binds to an IPv6 address as well. See <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5) for more details and also the <code>-6</code> flag for <code>innd</code>.</p>
<dt><code>-6</code> <i>address</i></p>
<dd>Only applies when <font SIZE="-1">INN</font> has been built with IPv6 support. Normally <code>innd</code> binds to all local <font SIZE="-1">IP</font> addresses (unless <i>bindaddress6</i> is set in <i>inn.conf</i>). If this option is given, it specifies the IPv6 address that <font SIZE="-1">INN</font> should bind to. The IPv6 address must be in colon-separated <font SIZE="-1">RFC</font>&nbsp;<wbr>4291 format (<tt>&quot;n:n:n:n:n:n:n:n&quot;</tt>). </p>
<p> If this option is specified, it&#8217;s the same as setting <i>bindaddress6</i> in <i>inn.conf</i> and may cause changes in whether <font SIZE="-1">INN</font> binds to an IPv4 address as well. See <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5) for more details and also the <code>-4</code> flag for <code>innd</code>.</p>
<dt><code>-a</code></p>
<dd>By default, if a host connects to <code>innd</code> but is not listed in <i>incoming.conf</i>, the connection is handed off to <code>nnrpd</code> (or rejected if <i>noreader</i> is set in <i>inn.conf</i>). If <code>-a</code> is given, <i>incoming.conf</i> is ignored and any host can connect and transfer articles. This flag should never be used with an accessible server connected to Usenet; it would open the server up for all sorts of abuse.</p>
<dt><code>-c</code> <i>days</i></p>
<dd><code>innd</code> normally rejects any article that is older (in days) than the value of <i>artcutoff</i> in <i>inn.conf</i>. This option, if given, overrides the value of that setting. If <i>days</i> is 0, this check is suppressed and <code>innd</code> will accept articles regardless of how old they are.</p>
<dt><code>-C</code></p>
<dd>This flag tells <code>innd</code> to accept and propagate but not actually process cancel or supersedes messages. This is intended for sites concerned about abuse of cancels, or that wish to use another cancel mechanism with stronger authentication.</p>
<dt><code>-d</code>, <code>-f</code></p>
<dd><code>innd</code> normally puts itself into the background, points its standard output and error to log files, and disassociates itself from the terminal. Using <code>-d</code> prevents all of this, resulting in log messages being written to standard output; this is generally useful only for debugging. Using <code>-f</code> prevents the backgrounding and disassociation but still redirects output; it may be useful if you want to monitor <code>innd</code> with a program that would be confused by forks.</p>
<dt><code>-H</code> <i>count</i>, <code>-T</code> <i>count</i>, <code>-X</code> <i>seconds</i></p>
<dd>These flags control the number of connections per <i>seconds</i> seconds that are allowed. This code is meant to protect your server from newsreader clients that make too many connections per minute (and therefore these flags are probably only useful when <code>innd</code> is spawning <code>nnrpd</code>). You probably should not use these options unless you&#8217;re having problems. The table used for this check is fixed at 128 entries and is used as a ring; the size was chosen to make calculating the index easy and to be fairly sure that it won&#8217;t run out of space. In practice, it is unlikely that even half the table will be used at any given moment. </p>
<p> The <code>-H</code> flag limits the number of times a host is allowed to connect to the server per the time interval given by <code>-X</code>. The default is <tt>2</tt>. </p>
<p> The <code>-T</code> flag limits the total number of incoming connections per the time interval given by <code>-X</code>. The maximum value is <tt>128</tt>, and the default is <tt>60</tt>. </p>
<p> Note that the time interval given by <code>-X</code> is set to <tt>0</tt> by default, that is to say no control is done on the number of connections.</p>
<dt><code>-i</code> <i>count</i></p>
<dd><code>innd</code> normally allows a maximum number of concurrent <font SIZE="-1">NNTP</font> connections given by the value of <i>maxconnections</i> in <i>inn.conf</i>. This option, if given, overrides the value of that setting. If <i>count</i> is <tt>0</tt>, this check is suppressed.</p>
<dt><code>-l</code> <i>size</i></p>
<dd><code>innd</code> normally rejects any article larger than the value of <i>maxartsize</i> in <i>inn.conf</i>. This option, if given, overrides the value of that setting and specifies a maximum article size of <i>size</i>. If <i>size</i> is <tt>0</tt>, this check is suppressed.</p>
<dt><code>-m</code> <i>mode</i></p>
<dd>Normally, <code>innd</code> starts in the <tt>&quot;running&quot;</tt> mode. If this option is given, it specifies what mode <code>innd</code> should start in. <i>mode</i> should begin with one of <tt>&quot;g&quot;</tt>, <tt>&quot;p&quot;</tt>, or <tt>&quot;t&quot;</tt>, and the starting mode will be set to <tt>&quot;running&quot;</tt>, <tt>&quot;paused&quot;</tt>, or <tt>&quot;throttled&quot;</tt>, respectively, based on that initial letter. (<tt>&quot;g&quot;</tt> is short for <tt>&quot;go&quot;</tt>.)</p>
<dt><code>-N</code></p>
<dd>If this option is given, any filters (Perl or Python) are disabled before <code>innd</code> starts (normally, filters default to being enabled). The filters can be enabled after <code>innd</code> has started with <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8).</p>
<dt><code>-n</code> <i>flag</i></p>
<dd>Whether <code>innd</code> allows (and hands off to <code>nnrpd</code>) reader connections while paused or throttled is normally determined by the value of <i>readerswhenstopped</i> in <i>inn.conf</i>. This option, if given, overrides that value. If <i>flag</i> is <tt>&quot;n&quot;</tt>, <code>innd</code> will not allow readers if it is paused or throttled. If <i>flag</i> is <tt>&quot;y&quot;</tt>, readers will be allowed regardless of <code>innd</code>&#8216;s operating mode.</p>
<dt><code>-o</code> <i>count</i></p>
<dd>This flag limits the number of file descriptors that are available for outgoing file feeds. The default is the number of available file descriptors minus some reserved for internal use (which could potentially starve <code>innd</code> of descriptors to use for accepting new connections). If <code>innd</code> has more file feeds than <i>count</i>, some of them will be buffered and only written out periodically. </p>
<p> Normally you never need to use this option, since the number of outgoing feeds is fixed, being the number of file feeds configured in <i>newsfeeds</i>, and is generally small (particularly given that <i><a href="/docs/linux/man/8-innfeed/">innfeed</a></i>(8) is now used for most outgoing feeds at large sites).</p>
<dt><code>-P</code> <i>port</i></p>
<dd>The port <code>innd</code> should listen on is normally given by the value of <i>port</i> in <i>inn.conf</i>. This option, if given, overrides that value and specifies the port that <code>innd</code> should bind to.</p>
<dt><code>-r</code></p>
<dd>Instructs <code>innd</code> to renumber the <i>active</i> file after starting, just as if a <tt>&quot;ctlinnd renumber&quot;</tt> command were sent.</p>
<dt><code>-s</code></p>
<dd>Just check the syntax of the <i>newsfeeds</i> file and exit. <code>innd</code> will exit with a non-zero status if any errors are found; the actual errors will be reported via <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3).</p>
<dt><code>-S</code></p>
<dd>Report errors found in <i>incoming.conf</i> via <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3) and exit normally. (Yes, this is less useful than it should be.)</p>
<dt><code>-t</code> <i>seconds</i></p>
<dd>Normally, <code>innd</code> will flush any changes to history and the <i>active</i> file after 300 seconds of inactivity. This option changes that timeout to <i>seconds</i>.</p>
<dt><code>-u</code></p>
<dd>The news log (the trace information for every article accepted by <code>innd</code>) is normally buffered. This option changes the log to be unbuffered.</dl>
<h2>Control Messages</h2>
<p>Arriving articles that have a Control: header are called &#8220;control messages&#8221;. Except for cancel messages, these messages are handled by <i><a href="/docs/linux/man/8-controlchan/">controlchan</a></i>(8) via a feed set up in <i>newsfeeds</i>. </p>
<p> (Cancel messages update the history database, so they must be handled internally; the cost of syncing, locking, then unlocking would be too high given the number of cancel messages that are received. Note that if an article is cancelled before it is received by the news server, it will be rejected when it arrives since the history database has been updated; it is useful for rejecting spam before it arrives.) </p>
<p> The distribution of control messages is different than that of standard articles. Control messages are normally filed into the pseudo-newsgroup named <tt>&quot;control&quot;</tt> regardless of which newsgroup they were actually posted to. If, however, a <tt>&quot;control.&quot;</tt><i>command</i> newsgroup exists that matches the control command, the control message will be filed into that group instead. For example, a newgroup control message will be filed in <tt>&quot;control.newgroup&quot;</tt> if that group exists; otherwise, it will be filed in <tt>&quot;control&quot;</tt>. </p>
<p> If you want to specifically feed all control messages to a given site regardless of whether the control messages would affect the newsgroups you&#8217;re feeding that site, you can put the appropriate control newsgroup in the subscription list. For example, to feed all cancel messages to a given remote site (normally a bad idea), add <tt>&quot;control.cancel&quot;</tt> to its subscription list. Normally it&#8217;s best to exclude the control newsgroups from feeds to keep from sending your peers more control messages than they care about. That&#8217;s why the <i>newsfeeds</i> pattern <tt>&quot;!control,!control.*&quot;</tt> is as often as not specified (adding this pattern do not prevent control messages which affect the newsgroups fed to a site from being sent to it). </p>
<p> checkgroups, newgroup and rmgroup control messages receive additional special treatment. If one of these control messages is approved and posted to the newsgroup being created or removed (or to the admin group to which the checkgroups is posted), the message will be sent to all sites whose subscription patterns would cause them to receive articles posted to that group. For example, if a newgroup control message for a nonexistent newsgroup <tt>&quot;news.admin.meow&quot;</tt> is received, it will be sent to any site whose subscription pattern would cause it to receive <tt>&quot;news.admin.meow&quot;</tt> if that newsgroup existed (such as a pattern of <tt>&quot;news.admin.*&quot;</tt>). For this reason, it is correct to post newgroup messages to the newsgroup that the control message would create. It is <i>not</i> generally correct to crosspost newgroup messages to some &#8220;well-propagated&#8221; newsgroup; not only will this not actually improve their propagation to sites that want such control messages, but it will also cause sites that do not want those control messages to receive them. Therefore, assuming that a newgroup control message is sent to the group <tt>&quot;news.admin.meow&quot;</tt> (specified in the Newsgroups: header) in order to create the group <tt>&quot;news.admin.meow&quot;</tt>, the sites with the following subscription patterns will receive it: </p>
<pre> *,@news.*
 news.*
 news.*,!control,!control.*
 control,control.*</pre>
<p>but the sites with the following subscription patterns will not receive it: </p>
<pre> *,@news.*,!control,!control.*
 comp.*,@news.*</pre>
<p>If a control message is posted to a group whose name ends with the four characters <tt>&quot;.ctl&quot;</tt>, this suffix is stripped off and the control message is propagated as if it were posted to the base group. For example, a cancel message posted to <tt>&quot;news.admin.ctl&quot;</tt> will be sent to all sites that subscribe to <tt>&quot;control.cancel&quot;</tt> (or <tt>&quot;control&quot;</tt> if that newsgroup doesn&#8217;t exist) or <tt>&quot;news.admin&quot;</tt>. This behavior is present for historical compatibility reasons and should be considered obsolete; support for the <tt>&quot;.ctl&quot;</tt> suffix may be removed in a future version of <font SIZE="-1">INN</font>. </p>
<p> Finally, articles posted to newsgroups beginning with <tt>&quot;to.&quot;</tt> are treated specially. Provided that either that newsgroup exists in the <i>active</i> file or <i>mergetogroups</i> is set in <i>inn.conf</i>, the remainder of the newsgroup is taken to be a site name, as configured in <i>newsfeeds</i>, and the article is sent to that site. If <i>mergetogroups</i> is set, the article will be filed in the group named <tt>&quot;to&quot;</tt> (which must exist in the <i>active</i> file). For example, with <i>mergetogroups</i> set, an article posted to <tt>&quot;to.uunet&quot;</tt> will be filed in <tt>&quot;to&quot;</tt> and sent to the site <tt>&quot;uunet&quot;</tt>.</p>
<h2>Protocol Differences</h2>
<p><code>innd</code> implements the <font SIZE="-1">NNTP</font> commands defined in <font SIZE="-1">RFC</font>&nbsp;<wbr>3977 (<font SIZE="-1">NNTP</font>), <font SIZE="-1">RFC</font>&nbsp;<wbr>4643 (<font SIZE="-1">NNTP</font> authentication), <font SIZE="-1">RFC</font>&nbsp;<wbr>4644 (streaming <font SIZE="-1">NNTP</font> feeds) and <font SIZE="-1">RFC</font>&nbsp;<wbr>6048 (<font SIZE="-1">NNTP</font> <font SIZE="-1">LIST</font> additions) with the following differences:</p>
<dl>
<dt>1.</p>
<dd>A batch transfer command, <font SIZE="-1">XBATCH</font> <i>byte-count</i>, is provided. This command will read <i>byte-count</i> bytes and store them for later processing by <i><a href="/docs/linux/man/1-rnews/">rnews</a></i>(1) (which must be run separately, probably from cron). See <i><a href="/docs/linux/man/8-innxbatch/">innxbatch</a></i>(8) and <code>sendxbatches</code> for more details on this extension.</p>
<dt>2.</p>
<dd>As <font SIZE="-1">INN</font> is a mode-switching news server, <code>innd</code> implements a limited subset of the protocol useful for transferring news. The remaining commands are mostly only useful for readers and are implemented by <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8). Use of the <font SIZE="-1">MODE</font> <font SIZE="-1">READER</font> command will cause <code>innd</code> to pass the connection to <code>nnrpd</code>.</p>
<dt>3.</p>
<dd><code>innd</code> allows a wider syntax for wildmats.</p>
<dt>4.</p>
<dd>Three commands (<font SIZE="-1">IHAVE</font>, <font SIZE="-1">CHECK</font> and <font SIZE="-1">TAKETHIS</font>) will continue, for interoperability reasons, to return a reject code (respectively <tt>435</tt>, <tt>438</tt> and <tt>439</tt>) when the command contains a syntax error (which normally leads to <tt>501</tt>).</dl>
<h2>Header Modifications</h2>
<p><code>innd</code> modifies as few article headers as possible, although it could be better in this area. </p>
<p> Empty headers and headers that consist of nothing but whitespace are dropped. </p>
<p> The local site&#8217;s name (as set with the <i>pathhost</i> parameter in <i>inn.conf</i>) and an exclamation point are prepended to the Path: header, provided the first site name in the Path: header is different from the local one. In addition, <i>pathalias</i> and <i>pathcluster</i> may be similarly respectively prepended and appended to the Path: header; see <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5) for the details. </p>
<p> The Xref: header is removed and a new one created. </p>
<p> <code>innd</code> does not rewrite incorrect headers. For example, it will not replace an incorrect Lines: header, though it may reject such an article depending on the value of <i>linecountfuzz</i> in <i>inn.conf</i>.</p>
<h2>Cancel Feeds</h2>
<p>In order to efficiently apply a large number of local cancels (such as from processing NoCeMs or from some other external source), <font SIZE="-1">INN</font> supports a special feed mode available only to connections to the local Unix-domain socket (not to connections to any network sockets). </p>
<p> To enter this mode, connect to the Unix-domain socket (<i>pathrun</i>/nntpin) and send the command <font SIZE="-1">MODE</font> <font SIZE="-1">CANCEL</font>. The response will have code <tt>284</tt>. Every subsequent line sent on that connection should consist of a single message-ID. An attempt will be made to cancel that message-ID, and the server will reply <tt>289</tt> for success or <tt>484</tt> for failure. (Failure can occur, for example, if the server is paused or throttled, or the message-ID is corrupt. Failure does <i>not</i> occur if the article to be cancelled does not exist.)</p>
<h2>Logging</h2>
<p><code>innd</code> reports all incoming articles in its log file (<i>pathlog</i>/news). This is a text file with a variable number of space-separated fields in one of the following formats: </p>
<pre> mon dd hh:mm:ss.mmm + feed &lt;message-id&gt; site ...
 mon dd hh:mm:ss.mmm j feed &lt;message-id&gt; site ...
 mon dd hh:mm:ss.mmm c feed &lt;message-id&gt; Cancelling &lt;message-id&gt;
 mon dd hh:mm:ss.mmm - feed &lt;message-id&gt; reason
 mon dd hh:mm:ss.mmm ? feed &lt;message-id&gt; reason</pre>
<p>There may also be hostname and/or size fields after the message-ID depending on the settings of <i>nntplinklog</i> and <i>logartsize</i> in <i>inn.conf</i>. </p>
<p> The first three fields are the date and time to millisecond resolution. The fifth field is the site that sent the article (based on the Path: header) and the sixth field is the article&#8217;s message-ID; they will be a question mark if the information is not available. </p>
<p> The fourth field indicates whether the article was accepted or not. If it is a plus sign, then the article was accepted. If it is the letter <tt>&quot;j&quot;</tt>, then the article was accepted, providing all of the newsgroups to which the article was posted were set to status <tt>&quot;j&quot;</tt> in the <i>active</i> file (or not listed in the <i>active</i> file and <i>wanttrash</i> was set in <i>inn.conf</i>), and then the article was filed into the <tt>&quot;junk&quot;</tt> newsgroup. In both of these cases, the article has been accepted and the <tt>&quot;site ...&quot;</tt> field contains the space-separated list of sites to which the article is being sent. </p>
<p> If the fourth field is the letter <tt>&quot;c&quot;</tt>, then a cancel message was accepted before the original article arrived, and a history entry for the cancelled message was created so that <code>innd</code> will reject that message if it arrives later. </p>
<p> If the fourth field is a minus sign, then the article was rejected. The reasons for rejection generated by <code>innd</code> include: </p>
<pre> &quot;%s&quot; header too long
 Article exceeds local limit of %s bytes
 Article posted in the future -- &quot;%s&quot;
 Bad &quot;%s&quot; header
 Can't write history
 Duplicate
 Duplicate &quot;%s&quot; header
 EOF in headers
 Linecount %s != %s +- %s
 Missing %s header
 No body
 No colon-space in &quot;%s&quot; header
 No matching newsgroups in cancel &lt;%s&gt;
 No space
 Space before colon in &quot;%s&quot; header
 Too old -- &quot;%s&quot;
 Unapproved for &quot;%s&quot;
 Unwanted newsgroup &quot;%s&quot;
 Unwanted distribution &quot;%s&quot;
 Whitespace in &quot;Newsgroups&quot; header -- &quot;%s&quot;</pre>
<p>where <tt>%s</tt>, above, is replaced by more specific information. (The Perl and Python filters, if used, may reject articles with other reasons.) </p>
<p> If the fourth field is the letter <tt>&quot;?&quot;</tt>, the article contains strange strings, such as <font SIZE="-1">CR</font> without <font SIZE="-1">LF</font> or <font SIZE="-1">LF</font> without <font SIZE="-1">CR</font>. (These characters should never occur in isolation, only together as <font SIZE="-1">CRLF</font> to indicate the end of a line.) This log message is just informational, to give an idea of how widespread such articles are; <code>innd</code> does not reject such articles. </p>
<p> Note that when <i>wanttrash</i> is set to true in <i>inn.conf</i> and an article is received that isn&#8217;t posted to any valid newsgroups, it will be accepted and logged with two lines, a <tt>&quot;j&quot;</tt> line and a minus sign line, unless the <i>logtrash</i> parameter is set to false (in which case only the <tt>&quot;j&quot;</tt> line is written). </p>
<p> <code>innd</code> also makes extensive reports through <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3). The first word of the log message will be the name of the site if the entry is site-specific (such as a &#8220;connected&#8221; message). The first word will be <tt>&quot;SERVER&quot;</tt> if the message relates to the server itself, such as when a read error occurs. </p>
<p> If the second word is the four letters <tt>&quot;cant&quot;</tt>, then an error is being reported. (The absence of an apostrophe is intentional; it makes it easier to grep from the command line and easier to find error messages in FAQs using a search engine. However, <tt>&quot;can't&quot;</tt> is also used at a few places.) In this case, the next two words generally name the system call or library routine that failed and the object upon which the action was being performed. The rest of the line may contain other information. </p>
<p> In other cases, the second word attempts to summarize what change has been made, while the rest of the line gives more specific information. The word <tt>&quot;internal&quot;</tt> generally indicates an internal logic error.</p>
<h2>Signals</h2>
<p><code>innd</code> will catch <font SIZE="-1">SIGTERM</font> and <font SIZE="-1">SIGHUP</font> and shut down. If <code>-d</code> is used, <font SIZE="-1">SIGINT</font> will also be caught and will result in an orderly shutdown. </p>
<p> <code>innd</code> will catch the <font SIZE="-1">SIGUSR1</font> signal and recreate the control channel used by <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8).</p>
<h2>Bugs</h2>
<p><code>innd</code> normally attempts to strip <font SIZE="-1">IP</font> options from incoming connections, since it uses IP-based authentication and source routing can confuse that. However, this doesn&#8217;t work on all systems, and it doesn&#8217;t work at all in the presence of IPv6 support (and is disabled in that case). Hence, if using <code>innd</code> with IPv6 support, make sure that your kernel or router disables source routing.</p>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. </p>
<p> <tt>$Id:</tt> innd.pod 9267 2011-07-17 18:41:42Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/3-dbz/">dbz</a></i>(3), <i><a href="/docs/linux/man/5-history/">history</a></i>(5), <i><a href="/docs/linux/man/5-incoming-conf/">incoming.conf</a></i>(5), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innbind/">innbind</a></i>(8), <i><a href="/docs/linux/man/8-innfeed/">innfeed</a></i>(8), <i><a href="/docs/linux/man/8-innstat/">innstat</a></i>(8), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8), <i><a href="/docs/linux/man/1-rnews/">rnews</a></i>(1), <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3). </p>
