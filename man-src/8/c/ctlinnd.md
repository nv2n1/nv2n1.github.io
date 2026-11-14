---
title: "ctlinnd(8)"
name: "ctlinnd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-ctlinnd/"
description: "ctlinnd – Control the main InterNetNews daemon"
---

<p>ctlinnd &#8211; Control the main InterNetNews daemon</p>
<h2>Synopsis</h2>
<p><code>ctlinnd</code> [<code>-hs</code>] [<code>-t</code> <i>timeout</i>] [<i>command</i> [<i>argument</i> &#8230;]]</p>
<h2>Description</h2>
<p><code>ctlinnd</code> sends a message to the control channel of <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), the main InterNetNews daemon. </p>
<p> In the normal mode of behavior, the message is sent to the server, which then performs the requested action and sends back a reply with a text message and an exit code for <code>ctlinnd</code>. If the server successfully performed the command, <code>ctlinnd</code> will print the reply on standard output and exit with a status of zero. If the server could not perform the command, it will direct <code>ctlinnd</code> to exit with a status of one. By default, <code>ctlinnd</code> will wait forever for a response from <code>innd</code>; this can be changed with the <code>-t</code> flag. </p>
<p> The <tt>&quot;shutdown&quot;</tt>, <tt>&quot;xabort&quot;</tt>, and <tt>&quot;xexec&quot;</tt> commands do not generate a reply, since they cause <code>innd</code> to exit. After these commands, <code>ctlinnd</code> will always exit silently with a status of zero.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Prints a command summary. If a command is given along with the <code>-h</code> flag, only the usage for that command will be given.</p>
<dt><code>-s</code></p>
<dd>If the command was successful, don&#8217;t print the output from <code>innd</code>.</p>
<dt><code>-t</code> <i>timeout</i></p>
<dd>Specifies how long to wait for the reply from the server, for commands other than <tt>&quot;shutdown&quot;</tt>, <tt>&quot;xabort&quot;</tt>, and <tt>&quot;xexec&quot;</tt>. <i>timeout</i> is the number of seconds to wait. A value of zero says to wait forever, and a value less than zero says not to wait at all but just exit immediately with status zero. When waiting for a reply, <code>ctlinnd</code> will check every two minutes to be sure the server is still running, to make it less likely that <code>ctlinnd</code> will just hang. </p>
<p> The default is zero, indicating that <code>ctlinnd</code> should wait forever.</dl>
<h2>Commands</h2>
<p>Here is the complete list of supported commands. Note that nearly all commands have a fixed number of arguments. If a parameter may be an empty string, it is still necessary to pass the empty string to <code>ctlinnd</code> as an argument (specified in the shell as two adjacent quotes, like <tt>''</tt>).</p>
<dl>
<dt>addhist <i>message-id</i> <i>arrival</i> <i>expires</i> <i>posted</i> <i>token</i></p>
<dd>Add an entry to the history database for <i>message-id</i>. The angle brackets around the message-ID are optional. It should normally be protected from the shell with single quotes. </p>
<p> <i>arrival</i>, <i>expires</i>, and <i>posted</i> should be the number of seconds since epoch and indicate when the article arrived, when it expires (via the Expires: header), and when it was posted (given in the Date: header), respectively. <i>expires</i> should be <tt>0</tt> if the article doesn&#8217;t have an Expires: header. <i>token</i> is the storage <font SIZE="-1">API</font> token for the article, and may be empty. </p>
<p> This command can only be used while the server is running, and will be rejected if the server is paused or throttled.</p>
<dt>allow <i>reason</i></p>
<dd>Allow remote connections, reversing a prior <tt>&quot;reject&quot;</tt> command. <i>reason</i> must be the same text given to the <tt>&quot;reject&quot;</tt> command, or the empty string (which matches any reason).</p>
<dt>begin <i>site</i></p>
<dd>Begin feeding <i>site</i>. The server will rescan the <i>newsfeeds</i> file to find the specified site and set up a newsfeed for it. If the site already existed, a <tt>&quot;drop&quot;</tt> for that site is done first. This command is forwarded; see <font SIZE="-1">NOTES</font> below.</p>
<dt>cancel <i>message-id</i></p>
<dd>Remove the article with the specified message-ID from the local system. This does not generate a cancel control message; it only affects the local system. The angle brackets around the message-ID are optional. It should normally be protected from the shell with single quotes (and not double quotes). For instance: </p>
<pre> ctlinnd cancel 'test [at] foo.bar'</pre>
<p>Note that the history database is updated with the specified message-ID so if an article with the same message-ID is afterwards received, it will be rejected; it is useful for rejecting spam before it arrives. </p>
<p> If the server is throttled manually, this command causes it to briefly open the history database. If the server is paused or throttled for any other reason, this command is rejected.</p>
<dt>changegroup <i>group</i> <i>status</i></p>
<dd>The newsgroup <i>group</i> is changed so that its status (the fourth field in the <i>active</i> file) becomes <i>status</i>. This may be used to make an existing group moderated or unmoderated, for example. </p>
<p> This command, unlike <tt>&quot;newgroup&quot;</tt> or <tt>&quot;rmgroup&quot;</tt>, can only be used while the server is running, and will be rejected if the server is paused or throttled.</p>
<dt>checkfile</p>
<dd>Check the syntax of the <i>newsfeeds</i> file and display a message if any errors are found. The details of the errors are reported to syslog.</p>
<dt>drop <i>site</i></p>
<dd>Flush and drop <i>site</i> from the server&#8217;s list of active feeds. This command is forwarded; see <font SIZE="-1">NOTES</font> below.</p>
<dt>feedinfo <i>site</i></p>
<dd>Print detailed information about the state of the feed to <i>site</i>, or brief status about all feeds if <i>site</i> is the empty string.</p>
<dt>flush <i>site</i></p>
<dd>Flush the buffer for the specified site. The action taken depends on the type of feed the site receives; see <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5) for more information. This is useful when the site is being fed by a file and batching is about to start, or to cleanly shut down and respawn a channel feed. If <i>site</i> is an empty string, all sites are flushed and the <i>active</i> file and history database are also flushed to disk. This command is forwarded; see <font SIZE="-1">NOTES</font> below. </p>
<p> Flushing the <code>innfeed</code> channel feed is the recommended method of restarting <code>innfeed</code> to pick up new configuration. <code>innd</code> will spawn a new <code>innfeed</code> process while the old process shuts down cleanly.</p>
<dt>flushlogs</p>
<dd>Close the news and error log files and rename them to add <tt>&quot;.old&quot;</tt> to the file name, then open fresh news and error logs. The <i>active</i> file and history database are also flushed to disk. Exploder and process channels are reopened so that they properly take into account the new log files.</p>
<dt>go <i>reason</i></p>
<dd>Re-open the history database and start accepting articles again, reversing a previous <tt>&quot;pause&quot;</tt> or <tt>&quot;throttle&quot;</tt> command. <i>reason</i> must be either the empty string or match the text that was given to the earlier <tt>&quot;pause&quot;</tt> or <tt>&quot;throttle&quot;</tt> command. </p>
<p> If a <tt>&quot;reject&quot;</tt> command is in effect, this will also reverse it by doing the equivalent of an <tt>&quot;allow&quot;</tt> command if the reason matches <i>reason</i>. Likewise, if a <tt>&quot;reserve&quot;</tt> command had been given, this will clear the reservation if <i>reason</i> matches the text that was given to <tt>&quot;reserve&quot;</tt>. </p>
<p> The history database is automatically closed on <tt>&quot;throttle&quot;</tt> or <tt>&quot;pause&quot;</tt> and reopened on <tt>&quot;go&quot;</tt>, so the history database can be replaced during the pause or throttle without requiring an explicit <tt>&quot;reload&quot;</tt> command. If any other configuration files or the <i>active</i> file were modified, a <tt>&quot;reload&quot;</tt> command should be given to force the server to re-read those files. </p>
<p> If the server throttled itself because it accumulated too many I/O errors, this command will reset the error count. </p>
<p> If <code>innd</code> was not started with the <code>-n y</code> flag, this command also does the equivalent of a <tt>&quot;readers&quot;</tt> command with <tt>&quot;yes&quot;</tt> as the flag and <i>reason</i> as the text.</p>
<dt>hangup <i>channel</i></p>
<dd>Close the socket for the specified incoming channel. This may be useful when an incoming connection appears to be hung (although <code>innd</code> will close idle connections automatically after a timeout).</p>
<dt>help [<i>command</i>]</p>
<dd>Print a command summary for all commands, or just <i>command</i> if one is specified. This is equivalent to the <code>-h</code> option.</p>
<dt>kill <i>signal</i> <i>site</i></p>
<dd>Signal <i>signal</i> is sent to the process underlying the specified site, which must be a channel or exploder feed. <i>signal</i> may be a numeric signal number or one of <tt>&quot;hup&quot;</tt>, <tt>&quot;int&quot;</tt>, or <tt>&quot;term&quot;</tt>; case is not significant.</p>
<dt>logmode</p>
<dd>Cause the server to log its current operating mode to syslog.</p>
<dt>lowmark <i>file</i></p>
<dd>Reset the low water marks in the <i>active</i> file based on the contents of <i>file</i>. Each line in <i>file</i> must be of the form: </p>
<pre> group low-value</pre>
<p>For example: </p>
<pre> comp.lang.c++ 243</pre>
<p>This command is mostly used by <code>news.daily</code> to update the <i>active</i> file after nightly expiration.</p>
<dt>mode</p>
<dd>Print the server&#8217;s operating mode as a multi-line summary of the parameters and the operating state. The parameters in the output correspond to command-line flags to <code>innd</code> and give the current settings of those parameters that can be overridden by command-line flags.</p>
<dt>name <i>channel</i></p>
<dd>Print the name and relevant information for the given incoming or outgoing channel, or for all channels if <i>channel</i> is an empty string. The response is formatted as: </p>
<pre> &lt;name&gt;:&lt;number&gt;:&lt;type&gt;:&lt;idle&gt;:&lt;status&gt;</pre>
<p>where &lt;name&gt; is the name of the channel, &lt;number&gt; is its number (generally the same as the file descriptor assigned to it), &lt;idle&gt; is the idle time for an <font SIZE="-1">NNTP</font> channel or the process <font SIZE="-1">ID</font> for a process channel, and &lt;status&gt; is the status for <font SIZE="-1">NNTP</font> channels. </p>
<p> The type is one of the following values: </p>
<pre> control Control channel for ctlinnd
 file An outgoing file feed
 localconn Local channel used by nnrpd and rnews for posting
 nntp NNTP channel for remote connections
 proc The process for a process feed
 remconn The channel that accepts new remote connections</pre>
<p>Channel status indicates whether the channel is paused or not. Nothing is shown unless the channel is paused, in which case <tt>&quot;paused&quot;</tt> is shown. A channel will be paused automatically if the number of remote connections for that label in <i>incoming.conf</i> is greater than <i>max-connections</i> within <i>hold-time</i> seconds.</p>
<dt>newgroup <i>group</i> [<i>status</i> [<i>creator</i>]]</p>
<dd>Create the specified newsgroup. The <i>status</i> parameter is the fourth field of the <i>active</i> file entry, as described in <i><a href="/docs/linux/man/5-active/">active</a></i>(5). If it is not an equal sign, only the first character is used. <i>creator</i> should be the identity of the person creating the group. If the newsgroup already exists, this is equivalent to the <tt>&quot;changegroup&quot;</tt> command. </p>
<p> <i>creator</i>, encoded in <font SIZE="-1">UTF-8</font> if given, may be omitted; if so, it will default to the newsmaster (as specified at configure time, normally <tt>&quot;usenet&quot;</tt>). <i>status</i> may also be omitted; if so, it will default to <tt>&quot;y&quot;</tt> (a normal, unmoderated group). The combination of defaults make it possible to use the text of the Control: header directly (although don&#8217;t do this without checking the syntactic validity of the header first). </p>
<p> This command can only be done while the server is running or throttled manually. It will update its internal state when a <tt>&quot;go&quot;</tt> command is sent. This command updates the <i>active.times</i> file as well. This command is forwarded; see <font SIZE="-1">NOTES</font> below.</p>
<dt>param <i>letter</i> <i>value</i></p>
<dd>Change the specified server parameter. <i>letter</i> is the <code>innd</code> command-line option to set and <i>value</i> is the new value. For example: </p>
<pre> ctlinnd param i 5</pre>
<p>would direct the server to allow only five incoming connections. To enable or disable the action of the <code>-n</code> flag, use <tt>&quot;n&quot;</tt> for the letter and <tt>&quot;y&quot;</tt> or <tt>&quot;n&quot;</tt>, respectively, for the value. </p>
<p> The supported values for <i>letter</i> are <tt>&quot;a&quot;</tt>, <tt>&quot;c&quot;</tt>, <tt>&quot;H&quot;</tt>, <tt>&quot;i&quot;</tt>, <tt>&quot;l&quot;</tt>, <tt>&quot;n&quot;</tt>, <tt>&quot;o&quot;</tt>, <tt>&quot;T&quot;</tt>, <tt>&quot;t&quot;</tt>, and <tt>&quot;X&quot;</tt>.</p>
<dt>pause <i>reason</i></p>
<dd>Pause the server so that no incoming articles are accepted. No existing connections are closed, but the history database is closed. This should be used for short-term locks, such as when replacing the history database. If the server was not started with the <code>-n y</code> flag, this command also does the equivalent of a <tt>&quot;readers&quot;</tt> command with <tt>&quot;no&quot;</tt> as the flag and <i>reason</i> as the text, encoded in <font SIZE="-1">UTF-8</font>.</p>
<dt>perl <i>flag</i></p>
<dd>Enable or disable Perl filtering. This command is only available if <font SIZE="-1">INN</font> was built with Perl filtering support. If <i>flag</i> starts with <tt>&quot;y&quot;</tt>, filtering is enabled; if it starts with <tt>&quot;n&quot;</tt>, filtering is disabled. </p>
<p> When filtering is disabled, if the <i>filter_innd.pl</i> Perl filter defined a function <tt>&quot;filter_end&quot;</tt>, it will be called prior to the deactivation of the filter.</p>
<dt>python <i>flag</i></p>
<dd>Enable or disable Python filtering. This command is only available if <font SIZE="-1">INN</font> was built with Python filtering support. If <i>flag</i> starts with <tt>&quot;y&quot;</tt>, filtering is enabled; if it starts with <tt>&quot;n&quot;</tt>, filtering is disabled.</p>
<dt>readers <i>flag</i> <i>text</i></p>
<dd>Allow or disallow readers. If <i>flag</i> starts with the letter <tt>&quot;n&quot;</tt>, then reading is disallowed by causing the server to pass <i>text</i> as the value of the <code>-r</code> flag to <code>nnrpd</code>. If <i>flag</i> starts with the letter <tt>&quot;y&quot;</tt> and <i>text</i> is either an empty string or the same string, encoded in <font SIZE="-1">UTF-8</font>, that was used when reading was disabled, reading will be re-enabled. </p>
<p> This command has no effect if <code>nnrpd</code> is being run separately rather than spawned by <code>innd</code>.</p>
<dt>reject <i>reason</i></p>
<dd>Remote connections (those that would not be handed off to <code>nnrpd</code>) are rejected with <i>reason</i> given as the explanation, encoded in <font SIZE="-1">UTF-8</font>. Existing connections are not closed.</p>
<dt>reload <i>what</i> <i>reason</i></p>
<dd>Update the in-memory copy of server configuration files. <i>what</i> identifies what should be reloaded, and <i>reason</i> is reported to syslog in the message noting the reload. </p>
<p> There is no way to reload <i>inn.conf</i>, <i>storage.conf</i>, or other configuration files for the storage or overview backends. To pick up changes to those files, use <tt>&quot;ctlinnd xexec innd&quot;</tt> to restart <code>innd</code>. </p>
<p> If <i>what</i> is the empty string or the word <tt>&quot;all&quot;</tt>, everything is reloaded. If it is the word <tt>&quot;history&quot;</tt>, the history database is closed and re-opened. If it is the word <tt>&quot;incoming.conf&quot;</tt>, the corresponding file is reloaded. If it is the word <tt>&quot;active&quot;</tt> or <tt>&quot;newsfeeds&quot;</tt>, both the <i>active</i> and <i>newsfeeds</i> files are reloaded, which will also cause all outgoing feeds to be flushed and restarted. </p>
<p> If <i>what</i> is the word <tt>&quot;filter.perl&quot;</tt>, the <i>filter_innd.pl</i> file is reloaded. If the Perl filter defined a function <tt>&quot;filter_before_reload&quot;</tt>, it will be called prior to re-reading <i>filter_innd.pl</i>. If the Perl function <tt>&quot;filter_after_reload&quot;</tt> is defined, it will be called after <i>filter_innd.pl</i> has been reloaded. Reloading the Perl filter does not enable filtering if it has been disabled; use <tt>&quot;perl y&quot;</tt> to do this instead. <i>startup_innd.pl</i> cannot be reloaded. This file is not available for reloading unless <font SIZE="-1">INN</font> was compiled with Perl filtering support. </p>
<p> If <i>what</i> is the word <tt>&quot;filter.python&quot;</tt>, the <i>filter_innd.py</i> file is reloaded. If a Python method named <tt>&quot;filter_before_reload&quot;</tt> exists, it will be called prior to re-reading <i>filter_innd.py</i>. If a Python method named <tt>&quot;__init__&quot;</tt> exists, it will be called after <i>filter_innd.py</i> has been reloaded. Reloading the Python filter does not enable filtering if it has been disabled; use <tt>&quot;python y&quot;</tt> to do this. This file is not available for reloading unless <font SIZE="-1">INN</font> was compiled with Python filtering support.</p>
<dt>renumber <i>group</i></p>
<dd>Update the low water and high water marks for <i>group</i> in the <i>active</i> file based on the information in the overview database. Regardless of the contents of the overview database, the high water mark will not be decreased. (Decreasing it may cause duplicate article numbers to be assigned after a crash, which can cause serious problems with the tradspool storage method.) If <i>group</i> is the empty string, all newsgroups are renumbered. Renumber only works if overview data has been created (if <i>enableoverview</i> is set to true in <i>inn.conf</i>).</p>
<dt>renumberlow <i>file</i></p>
<dd>Identical to the <tt>&quot;lowmark&quot;</tt> command.</p>
<dt>reserve <i>reason</i></p>
<dd>Require the next <tt>&quot;pause&quot;</tt> or <tt>&quot;throttle&quot;</tt> command to use <i>reason</i> as its reason, encoded in <font SIZE="-1">UTF-8</font>. This reservation is cleared by giving an empty string for the reason. This is used by programs like <code>expire</code> to coordinate pauses and throttles of the server and avoid trampling on other instances of themselves.</p>
<dt>rmgroup <i>group</i></p>
<dd>Remove the specified newsgroup. The group is removed from the <i>active</i> file and its overview information is purged, making it immediately unavailable to readers. Unlike the <tt>&quot;newgroup&quot;</tt> command, this command does not update the <i>active.times</i> file. </p>
<p> This command can only be done while the server is running or throttled manually. This command is forwarded; see <font SIZE="-1">NOTES</font> below.</p>
<dt>send <i>feed</i> <i>text</i></p>
<dd>The specified <i>text</i> is sent as a control line to the exploder <i>feed</i>.</p>
<dt>shutdown <i>reason</i></p>
<dd>The server is shut down, with the specified reason recorded in the log and sent to all open connections. It is a good idea to send a <tt>&quot;throttle&quot;</tt> command first so that feeds can be shut down more gracefully. </p>
<p> If Perl or Python filtering is compiled in and enabled, certain functions are called at <tt>&quot;throttle&quot;</tt> or <tt>&quot;shutdown&quot;</tt> (to save filter state to disk, for example). Consult the embedded filter documentation for details.</p>
<dt>stathist (off | <i>filename</i>)</p>
<dd>Enable or disable generation of history performance statistics. If the parameter is <tt>&quot;off&quot;</tt>, no statistics are gathered. Otherwise, statistics are written to the specified file. A parser for this file is provided in the contrib tree of the <font SIZE="-1">INN</font> distribution.</p>
<dt>status (off | <i>interval</i>)</p>
<dd>Adjust the frequency with which <code>innd</code> reports status information to syslog. Status reporting is turned off if <tt>&quot;off&quot;</tt> or <tt>0</tt> is given as the argument. Otherwise, status will be reported every <i>interval</i> seconds. See <i>status</i> in <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5) for information on how to set the default.</p>
<dt>throttle <i>reason</i></p>
<dd>Close all existing incoming connections and outgoing feeds and reject new connections. Close the history database. This should be used for long-term locks or for running a large number of <tt>&quot;newgroup&quot;</tt> and <tt>&quot;rmgroup&quot;</tt> commands without restarting all outgoing feeds between each one. (Note that changing the status of existing newsgroups when the server is throttled cannot be done.) </p>
<p> If the server was not started with the <code>-n y</code> flag, then this command also does the equivalent of a <tt>&quot;readers&quot;</tt> command with <tt>&quot;no&quot;</tt> as the flag and <i>reason</i> as the text, encoded in <font SIZE="-1">UTF-8</font>.</p>
<dt>timer (off | <i>interval</i>)</p>
<dd>Adjust the frequency with which <code>innd</code> reports performance information to syslog. Performance monitoring is turned off if <tt>&quot;off&quot;</tt> or <tt>0</tt> is given as the argument. Otherwise, statistics will be reported every <i>interval</i> seconds to syslog. See <i>timer</i> in <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5) for information on how to set the default.</p>
<dt>trace <i>item</i> <i>flag</i></p>
<dd>Turn tracing on or off for the specified <i>item</i>. <i>flag</i> should start with the letter <tt>&quot;y&quot;</tt> or <tt>&quot;n&quot;</tt> to turn tracing on or off, respectively. If <i>item</i> starts with a number, tracing is set up for the specified <code>innd</code> channel, which must be an incoming <font SIZE="-1">NNTP</font> feed. If it starts with the letter <tt>&quot;i&quot;</tt>, general <code>innd</code> tracing is turned on or off. If it starts with the letter <tt>&quot;n&quot;</tt>, future <code>nnrpd</code> processes spawned by <tt>&quot;innd&quot;</tt> will or will not be passed the <code>-t</code> flag, as appropriate. This will not affect any <code>nnrpd</code> processes already running, or <code>nnrpd</code> processes started by some means other than <code>innd</code>.</p>
<dt>xabort <i>reason</i></p>
<dd>Log the specified <i>reason</i> and then abort. On most systems, this will cause <code>innd</code> to dump a core file. This is only useful for debugging.</p>
<dt>xexec <i>path</i></p>
<dd>Shut down the server, but then rather than exiting, exec <code>innd</code> with all of its original arguments except for <code>-r</code>. <i>path</i> may be either <tt>&quot;innd&quot;</tt> or an empty string, both of which are equivalent. Any other value is an error. </p>
<p> This is the easiest way to start a new copy of <code>innd</code> after upgrading or reload configuration files that can&#8217;t be reloaded via the <tt>&quot;reload&quot;</tt> command.</dl>
<h2>Notes</h2>
<p>In addition to being acted on by the server, certain commands can be forwarded to an appropriate child process. If the site receiving the command is an exploder (such as <code>buffchan</code>) or a funnel that feeds into an exploder, the command can be forwarded. In this case, the server will send a command line to the exploder that consists of the <code>ctlinnd</code> command name. If the site funnels into an exploder that has an asterisk (<tt>&quot;*&quot;</tt>) in its <tt>&quot;W&quot;</tt> flag (see <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5) for more information on feed specifications), the site name will be appended to the command; otherwise, no argument is appended.</p>
<h2>Bugs</h2>
<p><code>ctlinnd</code> uses Unix domain sockets on most systems to communicate with <code>innd</code> and is therefore limited by whatever maximum packet size the operating system imposes on Unix domain datagrams. This may mean that server replies are limited to 4&nbsp;<wbr><font SIZE="-1">KB</font> on some systems.</p>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Rewritten in <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> ctlinnd.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/5-active-times/">active.times</a></i>(5), <i><a href="/docs/linux/man/8-buffchan/">buffchan</a></i>(8), <i><a href="/docs/linux/man/5-incoming-conf/">incoming.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/3-inndcomm/">inndcomm</a></i>(3), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8). </p>
