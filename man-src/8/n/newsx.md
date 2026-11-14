---
title: "newsx(8)"
name: "newsx"
section: "8"
letter: "n"
url: "/docs/linux/man/8-newsx/"
description: "newsx – news server exchange; post and fetch news articles"
---

<p>newsx &#8211; news server exchange; post and fetch news articles </p>
<h2>Synopsis</h2>
<p><code>newsx</code> [ <i>options</i> ] [ <i>spoolname</i> [ [ <i>hostname</i> ] <i>port</i> ] ] </p>
<h2>Description</h2>
<p><code>newsx</code> is a client connecting to an NNTP server, posting outgoing articles batched by the news system, while also fetching new incoming articles from the same newsserver. It provides the NNTP capabilities required for serving a small local news spool such as those that may be found on installations with NNTP access through limited ISP accounts only, as well as being suitable for exchanging news with supplemental news sources for full scale news servers. </p>
<h2>Operation</h2>
<p>The program would normally be run by user <i>news</i>. </p>
<p> When started, <code>newsx</code> will go through the <i>spoolname</i> outgoing spool queue, and attempt to post all articles therein to the NNTP server <i>hostname</i>. </p>
<p> If a username and password for use with the simple authorization protocol have been supplied, they will be sent to the server first. If the <code>-r</code> option is specified, a <code>MODE READER</code> command will be sent. </p>
<p> When the outgoing transfer is finished, articles will be removed from the outgoing spool queue if successful transfer has been acknowledged by the NNTP host, if the article was specified by the host as a duplicate (already posted), or if a spooled article can no longer be found. </p>
<p> The fetch phase is then initiated. Articles available from the newsserver will be fetched and placed in the incoming spool, ready to be injected into the news system by <code>newsrun</code> (C News) or <i>rnews -U </i> (INN). </p>
<p> The groups are visited in the sequence that they appear in the host incoming state file, see <i><a href="/docs/linux/man/5-in-hosts/">in.hosts</a></i>(5). This may be used actively to prioritize between newsgroups. A tag mechanism controlled by the <code>-e</code> option is available to limit the number of groups that will be fetched. </p>
<p> Group names not present in the <i>active</i> file will not be fetched. Every group name is checked against the <i>spoolname</i> entries in the <code>sys</code> (C News) or <code>newsfeeds</code> (INN) file, as well as any <code>&#8211;groups</code> option, and only groups allowed there will actually be fetched. For C News, the group name is also checked against the <code>ME</code> entry, whereas in INN the <code>ME </code> entry is just prepended to the <i>spoolname</i> entry. </p>
<p> In this way, the sys/newsfeed file is used to control which newsgroups are actually received from the remote site, in the same manner that the local server determines which outgoing article will go where. </p>
<p> If an <code>-e</code> option hasn&#8217;t been specified, the local <code>active</code> file is then traversed to see if there are groups not mentioned in the current host newsrc file. Again, only groups allowed by <code>sys</code> or <code>newsfeeds</code> is actually fetched. Since these groups don&#8217;t have a starting point specified, all available articles will be fetched. </p>
<p> To avoid transferring cross-posted articles more than once, articles with messags IDs already fetched in the same session will not be fetched again. </p>
<p> To make multiple news sources to be used in an efficient manner, articles present in the <i>history</i> database will be skipped. </p>
<p> The pull phase can be omitted entirely by using the <code>-g</code> option. </p>
<p> Statistics on the connection will be logged to syslog (or stderr with <code>-d</code>). The posted article count is the total number of articles actually posted. The duplicate count is how many message IDs from posted messages that were found to already exist on the remote system. The missing count is those posted articles that could no longer be found locally, usually because they were canceled locally, or perhaps since they were expired already. </p>
<p> The connection time and the total number of characters transferred via the NNTP layer is logged, in addition to the average speed of article transfer. The speed given is the net rate, the calculation being based on the actual number of characters belonging to news article head and body parts. </p>
<p> A log file may be specified with the <code>-l</code> option, and a folder of posted messages maintained with the <code>-f</code> option.</p>
<h2>Arguments</h2>
<dl>
<dt><i>options</i></p>
<dd>As detailed below.</p>
<dt><i>spoolname</i></p>
<dd>The name of the outgoing spool queue. If not specified, the value of the NNTPSERVER environment variable will be used.</p>
<dt><i>hostname</i></p>
<dd>The hostname of the remote NNTP server to connect to. If not specified, the name of the spool will be used.</p>
<dt><i>port</i></p>
<dd>The port used for connecting to <i>hostname.</i> Will usually not need to be specified, and port &quot;nntp&quot; will be assumed. The port name &quot;telnet&quot; will receive special treatment. </p>
</dl>
<h2>Options For Logging</h2>
<dl>
<dt><code>-f</code><i> folder</i>, <code>&#8211;posted</code><i> folder</i></p>
<dd>Posted articles will be appended to the standard mail folder indicated. Note that the article will be added to the folder the first time posting of an article is attempted. The actual status of the posting will appear in the log file.</p>
<dt><code>-l</code><i> logfile</i>, <code>&#8211;log</code><i> logfile</i></p>
<dd>Log information about successfully posted articles to the file indicated.</p>
<dt><code>&#8211;stat</code><i> statfile</i></p>
<dd>A summary of article exchange statistics will be logged to the file indicated.</p>
<dt><code>&#8211;scanlogs</code></p>
<dd>Obey locks set by the INN <code>scanlogs</code> utility. This is currently only meaningfull for use with a modified scanlogs that understands newsx logs. </p>
</dl>
<h2>Options For News Access</h2>
<dl>
<dt><code>-a</code><i> authfile</i>, <code>&#8211;auth</code><i> authfile</i></p>
<dd>If specified, the username and password combination found in <i>authfile</i> will be sent to the server as part of the simple authorization protocol when the connection is first made. The file should consist of a line with two blank-separated words, the first being the username, the second the password. Do ensure that this file only has read access only for those users that need to know.</p>
<dt><code>&#8211;authgeneric</code></p>
<dd>Authentication with the server is performed using <code>AUTHINFO GENERIC</code>. This works by spawning a child process via <code>/bin/sh</code> <i>string</i>, where <i>string</i> is set in the environment variable <code>NNTPAUTH</code>. This process is expected to handle the authentication portion of the connection.</p>
<dt><code>-r</code>, <code>&#8211;reader</code></p>
<dd>A <code>MODE READER</code> command is sent to the remote server. This is used when connecting to remote INN hosts that needs it, and is the default state when using <code>&#8211;ihave</code>. With ihave, the command is issued between the ihave and fetch phase, otherwise the command is issued initially.</p>
<dt><code>&#8211;no-reader</code></p>
<dd>No <code>MODE READER</code> command is sent to the remote server. This is the default state when not using <code>&#8211;ihave</code>.</p>
<dt><code>&#8211;readbeforeauth</code></p>
<dd>Send the <code>MODE READER</code> command before attempting to authenticate via an <code>AUTHINFO</code> command. Otherwise, it is sent after the authentication. This option will obviously have no effect unless you also specify both <code>&#8211;reader</code> and one of <code>&#8211;authgeneric</code> or <code>&#8211;auth</code><i> authfile</i>.</p>
<dt><code>-w</code><i> chatfile</i>, <code>&#8211;chat</code><i> chatfile</i></p>
<dd>Use <i>chatfile</i> to control any special connect sequence that may be required before the NNTP protocol is connected. Only implemented for the &quot;telnet&quot; protocol.</p>
<dt><code>-x</code><i> command</i>, <code>&#8211;exec</code><i> command</i></p>
<dd>If specified, the <i>command</i> will be executed after the host port has been opened. This option is used in rare cases when special tricks has to be employed to get an NNTP connection activated.</p>
<dt><code>-y</code><i> program</i>, <code>&#8211;connect</code><i> program</i></p>
<dd>If specified, connect via a bidirectional pipe to <i>program</i> instead of to a socket. The hostname and port arguments will be ignored. </p>
</dl>
<h2>Options For Posting</h2>
<dl>
<dt><code>-p</code>, <code>&#8211;no-post</code></p>
<dd>Do not attempt to do any posting.</p>
<dt><code>&#8211;ihave</code></p>
<dd>Use NNTP IHAVE mechanism for submitting news messages, instead of the default POST. If this is for forwarding news in general, and not necessarily news generated locally, the setting of the &#8211;fail and &#8211;bounce option should be carefully reviewed.</p>
<dt><code>-m</code>, <code>&#8211;no-msgid</code></p>
<dd>Remove any message-ID header field from the posted message. This should cause the receiving end to generate a fresh message-ID. It should never been used together with <code>&#8211;ihave</code>.</p>
<dt><code>-k</code>, <code>&#8212;-keep-path</code></p>
<dd>Keep the <code>Path</code> when posting. In posting mode, the <code>Path</code> is by default stripped together with the <code>NNTP-Posting-Host</code> and <code>Xref</code> header items, so that the path of the news article as posted will appear to start at the actual posting host. With <code>&#8211;ihave</code>, the path is always included.</p>
<dt><code>&#8211;continue</code></p>
<dd>Ignore (but report) errors about non-existing outgoing spools, and continue with news fetching instead.</p>
<dt><code>&#8211;max-path</code><i> len</i></p>
<dd>
<dt>All outgoing articles are checked to see if the length of</p>
<dd>their paths are not too long. This is an extra precaution against inadvertently submitting <i>foreign</i> articles for posting. This option sets the maximum path length allowed. The default value is 1, consistent with a simple, local, newsspool. To disable this feature, set it to an impossibly large value, like 999. </p>
</dl>
<h2>Options For Fetching</h2>
<dl>
<dt><code>-g</code>, <code>&#8211;no-fetch</code></p>
<dd>Do not attempt to fetch any news articles.</p>
<dt><code>-e</code><i> end_tag</i>, <code>&#8211;end</code><i> end_tag</i></p>
<dd>Specify a tag in the incoming host state file, see <i><a href="/docs/linux/man/5-in-hosts/">in.hosts</a></i>(5). News fetching will end when a corresponding tag line has been reached. The tag line consists of a colon followed by the tag itself. This is a useful tool for dividing the newsgroups into several categories. Only a few newsgroups may be fetched during prime time, whereas the full list can be fetched once every night, for instance.</p>
<dt><code>-W</code><i> winsize</i>, <code>&#8211;window</code><i> winsize</i></p>
<dd>Specify the <i>window</i> size with respect to how many outstanding NNTP requests will be allowed at any one time. The default setting is 10. A value of 0 will disable windowing (aka. streaming) completely, making debugging easier. Increasing the window can significantly improve the article transfer speed. The effect is particulary pronounced over slow links and when many of the articles are already present in the local spool, where an improvement in speed of over 10 times has been observed compared to running with windowing disabled. All this at the penalty of an increased host newsserver load, obviously.</p>
<dt><code>-b</code><i> minspool</i>, <code>&#8211;size</code><i> minspool</i></p>
<dd>Specify the minimum incoming spool size. After every new group, if the spool file has reached the byte size specified, a new spool batch will be made. Setting this value to 1 will cause every newsgroup to be placed in a separate spool.</p>
<dt><code>&#8211;rnews</code></p>
<dd>Pipe incoming messages directly to <code>rnews</code> instead of placing them into the in-coming spool.</p>
<dt><code>&#8211;pipe-to</code><i> program</i></p>
<dd>Pipe incoming messages to <i>program</i> instead of placing them into the in-coming spool. A separate program and pipe is initiated for each incoming message.</p>
<dt><code>&#8211;rnews-to</code><i> program</i></p>
<dd>Like <code>&#8211;pipe-to</code>, but the pipe is continuous for each session, with article seperation is in rnews style.</p>
<dt><code>-z</code>, <code>&#8211;sync</code></p>
<dd>Omit actual pulling of news articles. Instead, simply update the host incoming state file to synchronize with the currently highest available article numbers from the server in question. This option can be useful when a fresh local spool is initiated. No article posting will be attempted. See also <i><a href="/docs/linux/man/5-in-hosts/">in.hosts</a></i>(5).</p>
<dt><code>-Z</code>, <code>&#8211;syncnew</code></p>
<dd>Omit actual pulling of news articles in previously unseen groups only. The net effect is that newly added groups will start fetching from <code>now on</code>, instead of from the first article available at the host server.</p>
<dt><code>&#8211;reset</code></p>
<dd>Ignore the latest article information in the host incoming state file and attempt fetching <code>all </code> articles available from the server, subject to the normal history lookup constraints. This option is useful if the remote spool has been reconfigured. See also <i><a href="/docs/linux/man/5-in-hosts/">in.hosts</a></i>(5).</p>
<dt><code>&#8211;filter</code><i> filterprog</i></p>
<dd>Enable message filtering via the program <i>filterprog</i>. Uses the <code>highwind</code> interface model, where each article is given to the filter in NNTP-fashion, and the filter responds with a 335 to accept, and a 435 to reject a message.</p>
<dt><code>&#8211;mfilter</code><i> filterprog</i></p>
<dd>Enable filtering by message ID. The <i>filterprog</i> will be invoked once for each unseen message, with the message ID as a command line argument. A non-zero return status will prevent the message from being transferred. This function is obsolete, and will probably be removed in later versions.</p>
<dt><code>-X</code><i> num</i>, <code>&#8211;maxnew</code><i> num</i></p>
<dd>Fetch at most <i>num</i> articles from each new and previously unseen newsgroup.</p>
<dt><code>&#8211;maxart</code><i> num</i></p>
<dd>Fetch at most <i>num</i> articles from each newsgroup. Note that this might cause articles to be silently lost.</p>
<dt><code>&#8211;no-path</code></p>
<dd>Unless the exclusion pattern is set to <code>newsx</code>, all incoming articles are checked to see if their path is consistent with the exclusions given in <code>/usr/lib/news/newsfeeds</code>. This option omits this check.</p>
<dt><code>&#8211;forget-inactive</code></p>
<dd>Remove information in the incoming hosts state file about newsgroups that are removed from the <code>/usr/lib/news/active</code> file. See also <i><a href="/docs/linux/man/5-in-hosts/">in.hosts</a></i>(5).</p>
<dt><code>&#8211;minfree</code><i> N</i></p>
<dd>Don&#8217;t fetch news if there are less than <i>N</i> kbytes free space in the news spool.</p>
<dt><code>&#8211;group</code><i> list</i></p>
<dd>Specify pattern for groups to be fetched that will apply in addition to the ones in <code>/usr/lib/news/newsfeeds</code>. The syntax is basically the same as for INN <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5). It is recommended to put <i>list</i> in single quotes, since shells may otherwise treat the ! character in strange ways. For a list that specifies only negations, an initial &#8216;*&#8217; clause will be assumed.</p>
<dt>This options is particularily useful to specify unsymmetric behaviour, i.e.</p>
<dd>groups where there will be outgoing traffic, but no incoming articles. For instance, to explicitly avoid fetching of control groups, use:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &#8211;groups &#8216;!control.*&#8217;
</dl>
<p> It can also be useful to specify that only a subset of groups should be fetched for the occasion, e.g:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &#8211;groups &#8216;comp.*,!*.advocacy&#8217;</p>
<p> It is recommended to put the argument for &#8211;groups in single quotes.</p>
<h2>General Options</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;cnews</code></p>
<dd>Set to C News mode as opposed to INN. Controls details regarding handling of spool and lock files.</p>
<dt><code>-i</code>, <code>&#8211;inn</code></p>
<dd>Set to INN mode as opposed to C News. Controls details regarding handling of spool and lock files.</p>
<dt><code>&#8211;newline</code></p>
<dd>Uses single newline character as line terminator instead of the carriage return, line feed sequence.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Display program version. Include this when reporting bugs to <a rel="nofollow" href="http://www.kvaleberg.com/bug/">http://www.kvaleberg.com/bug/</a></p>
<dt><code>&#8211;help</code></p>
<dd>Give a very brief usage summary.</p>
<dt><code>&#8211;no-ps</code></p>
<dd>Do not update the process status display. </p>
</dl>
<h2>Options For Newsgroups</h2>
<p>Note: Unless otherwise specified, these options are <code>in addition to</code> the usual actions and do <code>not</code> imply &#8211;no-post or &#8211;no-fetch. Specify those switches if desired.</p>
<dl>
<dt><code>&#8211;list</code><i> listname</i></p>
<dd>Obtain a list of newsgroups from the newsserver to <i>listname</i>. The list consists of one line per newsgroup, containing the newsgroup name, a blank, and a letter showing the group status (usually &#8216;y&#8217; for an active group, &#8216;m&#8217; for a moderated group).</p>
<dt>If the first character is a &#8216;|&#8217;,</p>
<dd><i>listname </i> is assumed to be a program path which will receive the list as standard input (you will need to put the entire argument in quotes to escape the usual shell interpretation of &#8216;|&#8217;). If it is a single &#8216;-&#8216;, the list will appear on the standard output. Otherwise it will be assumed to be a filename.</p>
<dt><code>&#8211;newlist</code><i> listname</i></p>
<dd>Obtain a list of newsgroups not currently present on the local server from the newsserver to <i>listname</i>. The list is also subject to the limitations of the sys or newsfeeds file. The operation is otherwise as for the <code>&#8211;list</code> option.</p>
<dt><code>&#8211;desc</code><i> descname</i></p>
<dd>Obtain a list of newsgroups descriptions from the newsserver to <i>descname</i>. Only descriptions for locally active newsgroups relevant to the newsfeed in question will be fetched.</p>
<dt>The list consists of one line per newsgroup, containing the newsgroup name,</p>
<dd>a tab, and a short textual description. A pipe may be specified in <i>descname </i> kist as for the <code>&#8211;list</code> option.</p>
<dt><code>&#8211;alldesc</code><i> descname</i></p>
<dd>Obtain a list of all newsgroups descriptions available from the newsserver to <i>descname</i>. The operation is otherwise as for the <code>&#8211;desc</code> option. </p>
</dl>
<h2>Options For Error Handling</h2>
<dl>
<dt><code>-t</code><i> timeout</i>, <code>&#8211;timeout</code><i> timeout</i></p>
<dd>Specify timeout for TCP/IP and lockfile operations, in seconds. The default value is 600.</p>
<dt><code>&#8211;fail</code><i> time</i></p>
<dd>Specify the maximum age of an article. Whenever an attempt of posting an article fails, and the specified time limit is exceeded, the article will be declared as failed, and a bounce message will be generated. The default unit is hours; the suffixes <code>s</code> for seconds, <code>m</code> for minutes, <code>h</code> for hours, <code>d</code> for days and <code>w</code> for weeks would change this. They can also be combined, e.g. &quot;4h30m&quot;. In absence of this option, no fail by age will be performed. Setting the time to zero will bounce messages after the first failed attempt.</p>
<dt><code>&#8211;bounce</code><i> addr</i></p>
<dd>Specify the destination address for messages bounced due to the fail time being exceeded. If <i>addr</i> is specified as <code>none</code>, no bounce will be generated. The default value, <code>poster</code>, causes messages to be returned to the sender. This setting should definitely only be used in situations where <code>newsx</code> is utilized for posting locally generated news.</p>
<dt><code>&#8211;attach</code><i> how</i></p>
<dd>Specifies the way the original message is handled for bounced messages:</p>
<dt><code> mime</code></p>
<dd>Send the original as a Mime attachement. This is the default behaviour.</p>
<dt><code> yes</code></p>
<dd>Append the original to the mail message itself.</p>
<dt><code> no</code></p>
<dd>Do not attach the original message. </p>
</dl>
<h2>Options Mostly For News Gateways</h2>
<p>The following options are not for ordinary use: They would only be used for special configurations where newsx is used as a sort of gateway to inject news messages from other sources.</p>
<dl>
<dt><code>&#8211;inews</code></p>
<dd>Pipe incoming messages directly to <code>inews</code>, inject them into the local spool via the same interface as is used for local new messages.</p>
<dt><code>&#8211;inews-options</code><i> options</i></p>
<dd>Specify command line options for <code>&#8211;inews</code>. The leading &#8216;-&#8216; must be included. The default inews options are &quot;-hOS&quot;.</p>
<dt><code>&#8211;add-header</code><i> header</i></p>
<dd>Add a specific header to incoming messages. The header will be added exactly as specified, adding a trailing newline.</p>
<dt>The exception is for the special 4 letter string &quot;Path&quot;.</p>
<dd>This will be replaced by a header line that says &quot;Path: HOSTNAME!not-for-mail&quot; if the incoming message contains no <code>Path:</code>. This can be quite essential for news gateways to prevent injected messages to be retured back to the source. </p>
</dl>
<h2>Options For Profile Files</h2>
<dl>
<dt><code>&#8211;profile</code> <i>file</i></p>
<dd>Read a <code>newsx</code> profile from <i>file .</i> This file can contain command line options to specify default newsx behaviour. See <i><a href="/docs/linux/man/5-newsx-conf/">newsx.conf</a></i>(5) for an overview of the format.</dl>
<p> Any option may be used in profile files. Some options are really only meaningfull in profile files:</p>
<dl>
<dt><code>&#8211;spoolname</code><i> spoolname</i></p>
<dd>Specify a default <i>spoolname</i>.</p>
<dt><code>&#8211;hostname</code><i> hostname</i></p>
<dd>Specify a default <i>hostname</i>.</p>
<dt><code>&#8211;port</code><i> port</i></p>
<dd>Specify a default <i>port</i> for connecting to <i>hostname</i>. </p>
</dl>
<h2>Options For Configuration</h2>
<p>Configuration to the local news system peculiarities is traditionally done at build-time, but it is possible to specify at runtime in various ways.</p>
<dl>
<dt><code>&#8211;config</code></p>
<dd>Read and obey the standard news configuration file in <code>/usr/lib/news/lib/innshellvars</code>. This allows <code>newsx</code> to adapt to changes in the local newsserver configuration dynamically.</p>
<dt><code>&#8211;config-is</code> <i>configfile</i></p>
<dd>Like <code>&#8211;config</code>, except that the configuration filename is specified. A list of files may also be specified, seperated by colons. In this case, the first file on this list that exists will be used.</p>
<dt><code>&#8211;home</code> <i>newshome</i></p>
<dd>Use <i>newshome</i> as the news home directory instead of the default <code>/usr/lib/news</code>. A full path must be specified.</p>
<dt><code>-s</code><i> spooldir</i>, <code>&#8211;spool</code><i> spooldir</i></p>
<dd>Use <i>spooldir</i> as the news article spool directory instead of the default <code>/var/spool/news</code>. A full path must be specified.</p>
<dt><code>&#8211;togo</code><i> togofile</i></p>
<dd>Specify the name of the C News <i>togo</i> file for outgoing news. No effect in INN mode. Required only if different from the default value <i>/var/spool/news/outgoing/spoolname</i>/togo. A leading &#8216;/&#8217; specifices a full path, a leading &#8216;.&#8217; is relative from the current directory, otherwise the name is relative to <i>/var/spool/news/outgoing/spoolname</i>.</p>
<dt><code>&#8211;batch</code><i> batchdir</i></p>
<dd>Use <i>batchdir</i> as the outgoing news article spool directory instead of the default <code>/usr/lib/newsbin</code>. A leading &#8216;/&#8217; specifices a full path, a leading &#8216;.&#8217; is relative from the current directory, otherwise the name is relative to <i>/var/spool/news</i>.</p>
<dt><code>-h</code><i> historydb</i>, <code>&#8211;history</code><i> historydb</i></p>
<dd>Specify the name of the history database file, used for checking if news articles are already present in the spool. Required only when using a name different from the default <code>/usr/lib/news/history</code>. An empty argument &quot;&quot; will prevent any referrence to the news history database.</p>
<dt><code>&#8211;active</code><i> activefile</i></p>
<dd>Specify the name of the active newsgroup file for incoming news. Required only if different from the default value <i>/usr/lib/news/active</i>. A leading &#8216;/&#8217; specifices a full path, a leading &#8216;.&#8217; specifies a path relative to the current directory, otherwise the name is relative to <i>/usr/lib/news</i>.</p>
<dt><code>&#8211;newsfeeds</code><i> newsfeedsfile</i></p>
<dd>Specify the name of the newsfeed specification file. This will override the default both in C News (sys) and INN (newsfeeds) modes. File name conventions as for <code>&#8211;active</code>.</p>
<dt><code>&#8211;incoming</code><i> incomingdir</i></p>
<dd>Use <i>incomingdir</i> as the incoming news article spool directory instead of the default <code>/var/spool/news/incoming</code>. Fine name conventions as for <code>&#8211;active</code>, except that the default directory is <i>/var/spool/news</i>.</p>
<dt><code>&#8211;inhosts</code><i> inhostsdir</i></p>
<dd>Use <i>inhostsdir</i> as the news host active file directory instead of the default <code>/var/spool/news/inhosts</code>. Name conventions as for <code>&#8211;incoming</code>. See also <i><a href="/docs/linux/man/5-in-hosts/">in.hosts</a></i>(5).</p>
<dt><code>&#8211;hostconfig</code><i> hostconfigdir</i></p>
<dd>Use <i>hostconfigdir</i> as the directory for the host specific profile. instead of the default <code>/var/spool/news/in.hosts</code>. Name conventions as for <code>&#8211;incoming</code>. See also <i>new</i><a href="/docs/linux/man/5-in-hosts/">in.hosts</a><i>(5)</i> and <i><a href="/docs/linux/man/5-newsx-conf/">newsx.conf</a></i>(5). </p>
</dl>
<h2>Options For Testing And Debugging</h2>
<dl>
<dt><code>&#8211;debug</code><i> level</i></p>
<dd>Set debug <i>level</i>. Any level different from zero diverts reporting to stderr instead of syslog, and turns on extra debugging output. Level 2 will output a &#8216;.&#8217; for every new article. Level 3 will log all NNTP commands. Level 4 will produce the same state information that is available via the process status display. Going to level 5 will produce additional debug information, level 6 will include history database debug, while level 7 also will show all communications over the NNTP socket, article content included.</p>
<dt><code>-d</code>, <code>&#8211;verbose</code></p>
<dd>Enable debugging, and sets the debug level according to the number of times it is specified.</p>
<dt><code>-n</code>, <code>&#8211;dry-run</code></p>
<dd>No-action flag, will &quot;fake&quot; an NNTP connection, and leave the outgoing batch untouched. Probably useful only with <code>&#8211;debug</code> for debugging and dry-testing.</p>
<dt><code>&#8211;verify</code></p>
<dd>Used together with <code>&#8211;config</code>or <code>&#8211;config-is</code>, causes the configuration to be verified, but not adapted to.</p>
<dt><code>-o</code>, <code>&#8211;keepold</code></p>
<dd>Keep the previous outgoing spool in an &quot;.old&quot; file. This might seem like a useful option for ordinary use, but the problem is that a non-empty file might cause a news watch program to believe there is a stale outgoing spool.</p>
<dt><code>-u</code>, <code>&#8211;no-force</code></p>
<dd>After the timeout of lockfile operations, just give up and do not attempt to unlock the lockfiles and remove the stale process.</p>
<dt><code>&#8211;no-queue</code></p>
<dd>Do not queue up for access to a news host. If a lock already exists for the specified host, just give up and don&#8217;t queue up for it.</p>
<dt><code>&#8211;locks</code><i> locksdir</i></p>
<dd>Use <i>locksdir</i> as the lock file directory instead of the default <code>/usr/lib/news</code>. Fine name conventions as for <code>&#8211;active</code>, except that the default directory is <i>/usr/lib/news</i>. If the string <code>none</code> is supplied, no locking will occur. All this should of course be used only if you really, really know what you are doing.</p>
<dt><code>-q</code> &quot;<i>msgid</i>&quot;, <code>&#8211;enquire</code> &quot;<i>msgid</i>&quot;</p>
<dd>Enquires whether the <i>msgid</i> is present in the local history database. The <i>msgid</i> should include the angle brackets. Implies <code>&#8211;no-post</code> and <code>&#8211;no-fetch</code>.</p>
<dt><code>&#8211;no-hostlock</code></p>
<dd>Do not implement the newsx host access lock. Should only be used if you really know what you are doing.</p>
<dt><code>&#8211;no-next</code></p>
<dd>Do not use the NNTP NEXT command. This causes newsx not to attempt to use NEXT for filling out gaps in the article sequence.</p>
<dt><code>&#8211;missing</code> &quot;<i>num</i>&quot;</p>
<dd>Tunes the number of missing articles in a row before a NEXT command is issued, instead of a sequential STAT. A value of zero will cause NEXT to be used extensively. The default value is 0 if no window, 2 if a window is specified.</p>
<dt><code>&#8211;keep-fake</code></p>
<dd>Some remote news servers generate <i>faked</i> news articles. Normally, you would want newsx to skip them, but with this option you can actually fetch them. </p>
</dl>
<h2>Special Connect Sequence</h2>
<p>The <code>-w</code> option specifies that a special connect sequence is required, and that a script for this sequence can be found in the <i>chatfile.</i> This file consists of lines that contains pattern receive and send pairs, separated by blanks. The patterns may be enclosed in quotes. The script is currently only available for the &quot;telnet&quot; protocol. </p>
<p> A typical invocation line would be:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>newsx -w chat.acme acme login.acme.net telnet
</dl>
<p> The file chat.acme could look like this:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># login for acme.net NNTP</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>login: myusername</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Password: mypassword</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>$ &quot;exec telnet news.acme.net nntp&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ECHO
</dl>
<p> The script will have to be adapted for local conditions, of course. </p>
<p> The special tag <code>ECHO</code> specifies that line echo should be suppressed, required since the host telnet operates in line mode. </p>
<p> Since this file usually contains passwords and other sensitive information, ensure that read access to it is limited.</p>
<h2>Process Status</h2>
<p>The <code>ps</code> process status will also show the current newsx status. During the actual news transfer phase, it will show which group and article number that is being fetched. A continuous status can be obtained by;</p>
<dl>
<dd>&nbsp;<wbr>newsq -c</dl>
<p> This feature can be disabled via the <code>&#8211;no-ps</code> option.</p>
<h2>Configuration Format</h2>
<p>For INN, the following configuration items will be used:</p>
<dl>
<dt>$INND</p>
<dd>Signals an INN configuration.</p>
<dt>$NEWSBIN</p>
<dd>Directory for INN binaries.</p>
<dt>$NEWSHOME</p>
<dd>News home directory.</p>
<dt>$PATHETC</p>
<dd>Directory for news configuration files. Defaults to $NEWSHOME if not available.</p>
<dt>$SPOOL</p>
<dd>If $SPOOL contains the string &quot;/articles&quot;, the incoming host directory $INHOSTS will be formed by replacing it with &quot;/inhosts&quot;. Otherwise, &quot;$SPOOL/in.hosts&quot; will be used.</p>
<dt>$BATCH</p>
<dd>Outgoing spool.</p>
<dt>$INCOMING</p>
<dd>Incoming spool.</p>
<dt>$ACTIVE</p>
<dd>Active file.</p>
<dt>$HISTORY</p>
<dd>History database.</p>
<dt>$LOCKS</p>
<dd>DIrectory for lockfiles.</p>
<dt>$NEWSFEEDS</p>
<dd>Newsfeeds file.</p>
<dt>$EXTENDEDDBZ</p>
<dd>True is history database in extended format. Only relevant for early INN 2.x where there is no libinn, otherwise ignored.</dl>
<p> For C News:</p>
<dl>
<dt>$NEWSBIN</p>
<dd>
<dt>$NEWSCTL</p>
<dd>Equivalent to INN $NEWSHOME. $ACTIVE will be &quot;$NEWSCTL/active&quot;. $HISTORY will be &quot;$NEWSCTL/history&quot;. $NEWSFEEDS will be &quot;$NEWSCTL/sys&quot;. $LOCKS and $PATHETC will be &quot;$NEWSCTL&quot;.</p>
<dt>$NEWSARTS</p>
<dd>Equivalent to INN $SPOOL. $BATCH will be &quot;$NEWSARTS/out.going&quot;. $INCOMING will be &quot;$NEWSARTS/in.coming&quot;. $INHOSTS will be &quot;$NEWSARTS/in.hosts&quot;. </p>
</dl>
<h2>Log File Format</h2>
<p>The <i>-l</i> log file of posted articles will contain one line for each article. To be compatible with the INN format, each field is separated by a tabstop:</p>
<dl>
<dt>Month</p>
<dd>Standard 3 letter abbreviation.</p>
<dt>Date</p>
<dd>2 digits</p>
<dt>HH:MM:SS</p>
<dd>Local time.</p>
<dt>Year</p>
<dd>4 digits.</p>
<dt>Spool</p>
<dd>Name of outgoing spool.</p>
<dt>&lt;Msgid&gt;</p>
<dd>Within angle brackets.</p>
<dt>Filename</p>
<dd>As it appears in the spool file.</p>
<dt>Sender</p>
<dd>The value of the Sender-field, or From-field if no Sender is available.</p>
<dt>Status</p>
<dd>&quot;OK&quot; for successfully posted items, &quot;Duplicate&quot; for items already posted.</p>
<dt>Lines</p>
<dd>Number of lines in the posting.</p>
<dt>Status</p>
<dd>Message status. &quot;OK&quot; if everything went well, otherwise an error message appears. </p>
</dl>
<h2>Incoming Spool Format</h2>
<p>The incoming spool consists of files with the file name ending by &quot;.t&quot;. Each file can contain many articles. Each article is prefixed by the following header:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#! rnews <code>N</code>
</dl>
<p> The number <code>N</code> is the number of bytes of the article proper, not counting the header line. The article follows after the header line. It appears exactly as received from the news server except that CR/LF sequences are replaced by proper newlines, and the terminating full stop is not included.</p>
<h2>Message Header Handling</h2>
<p>Incoming message headers will pass through without modification, with the exception that the text &quot;newsx&quot; will be added if not there already when the exclusion pattern for the newshost is set to &quot;newsx&quot;. </p>
<p> Most outgoing message header items will also pass through, altough some header items are handled specially:</p>
<dl>
<dt><code>From:</code></p>
<dd>Will be used for indentifying the sender if everything else fails.</p>
<dt><code>Message-ID:</code></p>
<dd>Will be used for logging purposes. The <code>&#8211;no-msgid</code> will remove this item for messages being posted.</p>
<dt><code>NNTP-Posting-Date:</code></p>
<dd>
<dt><code>NNTP-Posting-Host:</code></p>
<dd>Will always be removed for messages being posted.</p>
<dt><code>Path:</code></p>
<dd>Will be removed for messages being posted, unless the <code>&#8212;-keep-path</code> option is given.</p>
<dt><code>Reply-to:</code></p>
<dd>Will be used for indentifying the sender.</p>
<dt><code>Sender:</code></p>
<dd>Will be used for indentifying the sender.</p>
<dt><code>Xref:</code></p>
<dd>Will always be removed from outgoing messages.</p>
<dt><code>X-Server-Date:</code></p>
<dd>
<dt><code>X-Trace:</code></p>
<dd>
<dt><code>X-Complaints-To:</code></p>
<dd>Will always be removed for messages being posted. </p>
</dl>
<h2>Diagnostics</h2>
<p><code>newsx</code> returns error codes as follows:</p>
<dl>
<dd>0 &#8211; Successful completion<br />
 1 &#8211; General system error<br />
 2 &#8211; Incorrect arguments supplied.<br />
 3 &#8211; Error connecting to remote host<br />
 4 &#8211; NNTP Protocol error<br />
 5 &#8211; Errors accessing outgoing spool file.<br />
 6 &#8211; Errors accessing host newsrc file.<br />
 7 &#8211; Errors accessing incoming spool file.<br />
 8 &#8211; Errors accessing local <i>active</i> and <i>sys</i> files.<br />
 9 &#8211; Socket access error (e.g. connection timeout)<br />
 10 &#8211; Errors accessing <i>authinfo</i> file.<br />
 11 &#8211; Connect script failure.<br />
 12 &#8211; Option -q did not find the message ID.<br />
 13 &#8211; Wait for lock timed out.</dl>
<h2>Notes</h2>
<p>Distribution fields are ignored by newsx, and the handling of them left to the news server. </p>
<h2>Bugs</h2>
<p>Report any bugs to <a rel="nofollow" href="http://www.kvaleberg.com/bug/">http://www.kvaleberg.com/bug/</a> </p>
<h2>Files</h2>
<p>See also <i><a href="/docs/linux/man/5-in-hosts/">in.hosts</a></i>(5).</p>
<dl>
<dt>/usr/lib/news/newsx.conf</p>
<dd>Newsx standard profile. If it exists, this profile file will be read before the command line arguments are parsed. See <i><a href="/docs/linux/man/5-newsx-conf/">newsx.conf</a></i>(5).</p>
<dt>/usr/lib/news/lib/innshellvars</p>
<dd>The standard news configuration file.</dl>
<p> For C News:</p>
<dl>
<dt>/var/spool/news/outgoing/<i>spoolname</i>/togo</p>
<dd>Spool file</p>
<dt>/var/spool/news/outgoing/<i>spoolname</i>/togo.old</p>
<dd>Previous spool file</p>
<dt>/var/spool/news/outgoing/<i>spoolname</i>/LOCKb</p>
<dd>Lock file</p>
<dt>/var/spool/news/incoming/.tmp.$$</p>
<dd>Incoming spool, temporary file. <i>$$</i> is the process ID.</p>
<dt>/var/spool/news/incoming/T.$$.S.t</p>
<dd>Incoming spool, when finished and ready for newsrun. <i>T</i> is the current Unix time, <i>$$</i> is the process ID, and, <i>S</i> is a sequence number.</p>
<dt>/usr/lib/news/active</p>
<dd>Local active file, contains a list over all currently active newsgroups in the local spool. This is used as a basis for constructing a list over which newsgroups will actually be requested.</p>
<dt>/usr/lib/news/sys</p>
<dd>Newsserver configuration file. This is used as a filter against the local <i>active</i> list, deciding which newsgroups which will actually be pulled. The basic format of each specification is:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>site</i>/<i>exclusions</i>:<i>grouplist</i>/<i>distlist</i>:<i>flags</i>:<i>cmd</i></p>
<dd>If the <i>exclusions</i> field is set to <code>newsx</code>, newsx will modify the path of incoming news to include the &quot;newsx&quot; pattern.</p>
<dd>The <i>site</i> field identifies the remote news source.</p>
<dd>The <i>grouplist</i> is a comma separated list of group pattern names. A !-prefix signifies exclusions, and the name <code>all</code> matches anything.</p>
<dt>/usr/lib/news/history</p>
<dd>
<dt>/usr/lib/news/history.pag</p>
<dd>
<dt>/usr/lib/news/history.dir</p>
<dd>Local news spool database.</dl>
<p> For INN:</p>
<dl>
<dt>/var/spool/news/outgoing/<i>spoolname</i></p>
<dd>Spool file</p>
<dt>/var/spool/news/outgoing/<i>spoolname</i>.old</p>
<dd>Previous spool file</p>
<dt>/usr/lib/news/LOCK.<i>spoolname</i></p>
<dd>Lock file</p>
<dt>/usr/lib/news/active</p>
<dd>Local active file, contains a list over all currently active newsgroups in the local spool. This is used as a basis for constructing a list over which newsgroups will actually be requested.</p>
<dt>/usr/lib/news/newsfeeds</p>
<dd>Newsserver configuration file. This is used as a filter against the local <i>active</i> list, deciding which newsgroups which will actually be pulled. The basic format of each specification is:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>site</i>/<i>exclusions</i>:<i>grouplist</i>/<i>distlist</i>:<i>flags</i>:<i>param</i></p>
<dd>If the <i>exclusions</i> field is set to <code>newsx</code>, newsx will modify the path of incoming news to include the &quot;newsx&quot; pattern.</p>
<dd>The <i>site</i> field identifies the remote news source.</p>
<dd>The <i>grouplist</i> is a comma separated list of group pattern names. A !-prefix signifies groups <code>not</code> exchanged, and the name <code>*</code> matches anything.</p>
<dt>/usr/lib/news/history</p>
<dd>
<dt>/usr/lib/news/history.pag</p>
<dd>
<dt>/usr/lib/news/history.dir</p>
<dd>Local news spool article database. </p>
</dl>
<h2>Author</h2>
<p>Egil Kvaleberg &lt;egil [at] kvaleberg.no&gt;</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-newsq/">newsq</a></i>(1), <i><a href="/docs/linux/man/5-in-hosts/">in.hosts</a></i>(5) C News: <i><a href="/docs/linux/man/5-news/">news</a></i>(5), <i><a href="/docs/linux/man/5-newsdb/">newsdb</a></i>(5), <i><a href="/docs/linux/man/5-newssys/">newssys</a></i>(5), <i><a href="/docs/linux/man/8-rnews/">rnews</a></i>(8) INN: <i><a href="/docs/linux/man/1-rnews/">rnews</a></i>(1), <i><a href="/docs/linux/man/1-inews/">inews</a></i>(1), <i><a href="/docs/linux/man/3-wildmat/">wildmat</a></i>(3), <i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/5-history/">history</a></i>(5), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8) RFC-977 &#8211; Network News Transfer Protocol (NNTP)<br />
 RFC-1036 &#8211; Usenet Article Format <a rel="nofollow" href="http://www.kvaleberg.com/ISP-Hookup-HOWTO.html">http://www.kvaleberg.com/ISP-Hookup-HOWTO.html</a><br />
 <a rel="nofollow" href="http://www.kvaleberg.com/newsx.html">http://www.kvaleberg.com/newsx.html</a> </p>
