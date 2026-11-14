---
title: "rrdcached(1)"
name: "rrdcached"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdcached/"
description: "rrdcached – Data caching daemon for rrdtool"
---

<h2 class="name">NAME</h2>
<p> rrdcached &#8211; Data caching daemon for rrdtool </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdcached</code> [<code>-P</code>&nbsp;<wbr><i>permissions</i>] [<code>-l</code>&nbsp;<wbr><i>address</i>] [<code>-s</code>&nbsp;<wbr><i>group</i>] [<code>-w</code>&nbsp;<wbr><i>timeout</i>] [<code>-z</code>&nbsp;<wbr><i>delay</i>] [<code>-f</code>&nbsp;<wbr><i>timeout</i>] [<code>-p</code>&nbsp;<wbr><i>pid_file</i>] [<code>-t</code>&nbsp;<wbr><i>write_threads</i>] [<code>-j</code>&nbsp;<wbr><i>journal_dir</i>] [-F] [-g] [<code>-b</code>&nbsp;<wbr><i>base_dir</i>&nbsp;<wbr>[<code>-B</code>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>rrdcached</code> is a daemon that receives updates to existing <font SIZE="-1">RRD</font> files, accumulates them and, if enough have been received or a defined time has passed, writes the updates to the <font SIZE="-1">RRD</font> file. A <i>flush</i> command may be used to force writing of values to disk, so that graphing facilities and similar can work with up-to-date data. </p>
<p> The daemon was written with big setups in mind. Those setups usually run into <font SIZE="-1">IO</font>&nbsp;<wbr>related problems sooner or later for reasons that are beyond the scope of this document. Check the wiki at the RRDtool homepage for details. Also check &#8220;<font SIZE="-1">SECURITY</font> <font SIZE="-1">CONSIDERATIONS</font>&#8221; below before using this daemon! A detailed description of how the daemon operates can be found in the &#8220;<font SIZE="-1">HOW</font> <font SIZE="-1">IT</font> <font SIZE="-1">WORKS</font>&#8221; section below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code> <i>address</i></p>
<dd> Tells the daemon to bind to <i>address</i> and accept incoming connections on that socket. If <i>address</i> begins with <tt>&quot;unix:&quot;</tt>, everything following that prefix is interpreted as the path to a <font SIZE="-1">UNIX</font> domain socket. Otherwise the address or node name are resolved using <tt>&quot;getaddrinfo()&quot;</tt>. </p>
<p> For network sockets, a port may be specified by using the form <tt>&quot;</tt>[<tt></tt>address<tt></tt>]:<tt></tt>port<tt>&quot;</tt>. If the address is an IPv4 address or a fully qualified domain name (i. e. the address contains at least one dot (<tt>&quot;.&quot;</tt>)), the square brackets can be omitted, resulting in the (simpler) <tt>&quot;</tt>address<tt></tt>:<tt></tt>port<tt>&quot;</tt> pattern. The default port is <code>42217/tcp</code>. If you specify a network socket, it is mandatory to read the &#8220;<font SIZE="-1">SECURITY</font> <font SIZE="-1">CONSIDERATIONS</font>&#8221; section. </p>
<p> The following formats are accepted. Please note that the address of the <font SIZE="-1">UNIX</font> domain socket <code>must</code> start with a slash in the second case! </p>
<pre>
   unix:&lt;/path/to/unix.sock&gt;
   /&lt;path/to/unix.sock&gt;
   &lt;hostname-or-ip&gt;
   [&lt;hostname-or-ip&gt;]:&lt;port&gt;
   &lt;hostname-or-ipv4&gt;:&lt;port&gt;
</pre>
<p> If the <code>-l</code> option is not specified the default address, <tt>&quot;unix:/tmp/rrdcached.sock&quot;</tt>, will be used.</p>
<dt><code>-s</code> <i>group_name</i>|<i>gid</i></p>
<dd> Set the group permissions of a <font SIZE="-1">UNIX</font> domain socket. The option accepts either a numeric group id or group name. That group will then have both read and write permissions (the socket will have file permissions 0750) for the socket and, therefore, is able to send commands to the daemon. This may be useful in cases where you cannot easily run all <font SIZE="-1">RRD</font> processes with the same user privileges (e.g. graph generating <font SIZE="-1">CGI</font> scripts that typically run in the permission context of the web server). </p>
<p> This option affects the <i>following</i> <font SIZE="-1">UNIX</font> socket addresses (the following <code>-l</code> options) or the default socket (if no <code>-l</code> options have been specified), i.e., you may specify different settings for different sockets. </p>
<p> The default is not to change ownership or permissions of the socket and, thus, use the system default.</p>
<dt><code>-m</code> <i>mode</i></p>
<dd> Set the file permissions of a <font SIZE="-1">UNIX</font> domain socket. The option accepts an octal number representing the bit pattern for the mode (see <i><a href="/docs/linux/man/1-chmod/">chmod</a></i>(1) for details). </p>
<p> Please note that not all systems honor this setting. On Linux, read/write permissions are required to connect to a <font SIZE="-1">UNIX</font> socket. However, many BSD-derived systems ignore permissions for <font SIZE="-1">UNIX</font> sockets. See <i><a href="/docs/linux/man/7-unix/">unix</a></i>(7) for details. </p>
<p> This option affects the <i>following</i> <font SIZE="-1">UNIX</font> socket addresses (the following <code>-l</code> options) or the default socket (if no <code>-l</code> options have been specified), i.e., you may specify different settings for different sockets. </p>
<p> The default is not to change ownership or permissions of the socket and, thus, use the system default.</p>
<dt><code>-P</code> <i>command</i>[,<i>command</i>[,&#8230;]]</p>
<dd> Specifies the commands accepted via a network socket. This allows administrators of <i>RRDCacheD</i> to control the actions accepted from various sources. </p>
<p> The arguments given to the <code>-P</code> option is a comma separated list of commands. For example, to allow the <tt>&quot;FLUSH&quot;</tt> and <tt>&quot;PENDING&quot;</tt> commands one could specify: </p>
<pre>
  rrdcached -P FLUSH,PENDING $MORE_ARGUMENTS
</pre>
<p> The <code>-P</code> option affects the <i>following</i> socket addresses (the following <code>-l</code> options) or the default socket (if no <code>-l</code> options have been specified). In the following example, only the IPv4 network socket (address <tt>10.0.0.1</tt>) will be restricted to the <tt>&quot;FLUSH&quot;</tt> and <tt>&quot;PENDING&quot;</tt> commands: </p>
<pre>
  rrdcached -l unix:/some/path -P FLUSH,PENDING -l 10.0.0.1
</pre>
<p> A complete list of available commands can be found in the section &#8220;Valid Commands&#8221; below. There are two minor special exceptions:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The <tt>&quot;HELP&quot;</tt> and <tt>&quot;QUIT&quot;</tt> commands are always allowed.</p>
<dt>&bull;</p>
<dd> If the <tt>&quot;BATCH&quot;</tt> command is accepted, the <code>.</code>&nbsp;<wbr>command will automatically be accepted, too.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Please also read &#8220;<font SIZE="-1">SECURITY</font> <font SIZE="-1">CONSIDERATIONS</font>&#8221; below.</dl>
<dt><code>-w</code> <i>timeout</i></p>
<dd> Data is written to disk every <i>timeout</i> seconds. If this option is not specified the default interval of 300 seconds will be used.</p>
<dt><code>-z</code> <i>delay</i></p>
<dd> If specified, rrdcached will delay writing of each <font SIZE="-1">RRD</font> for a random number of seconds in the range&nbsp;<wbr>[0,<i>delay</i>). This will avoid too many writes being queued simultaneously. This value should be no greater than the value specified in <code>-w</code>. By default, there is no delay.</p>
<dt><code>-f</code> <i>timeout</i></p>
<dd> Every <i>timeout</i> seconds the entire cache is searched for old values which are written to disk. This only concerns files to which updates have stopped, so setting this to a high value, such as 3600 seconds, is acceptable in most cases. This timeout defaults to 3600 seconds.</p>
<dt><code>-p</code> <i>file</i></p>
<dd> Sets the name and location of the PID-file. If not specified, the default, <tt>&quot;</tt>$localststedir<tt>/run/rrdcached.pid&quot;</tt> will be used.</p>
<dt><code>-t</code> <i>write_threads</i></p>
<dd> Specifies the number of threads used for writing <font SIZE="-1">RRD</font> files. The default is 4. Increasing this number will allow rrdcached to have more simultaneous I/O requests into the kernel. This may allow the kernel to re-order disk writes, resulting in better disk throughput.</p>
<dt><code>-j</code> <i>dir</i></p>
<dd> Write updates to a journal in <i>dir</i>. In the event of a program or system crash, this will allow the daemon to write any updates that were pending at the time of the crash. </p>
<p> On startup, the daemon will check for journal files in this directory. If found, all updates therein will be read into memory before the daemon starts accepting new connections. </p>
<p> The journal will be rotated with the same frequency as the flush timer given by <code>-f</code>. </p>
<p> When journaling is enabled, the daemon will use a fast shutdown procedure. Rather than flushing all files to disk, it will make sure the journal is properly written and exit immediately. Although the <font SIZE="-1">RRD</font> data files are not fully up-to-date, no information is lost; all pending updates will be replayed from the journal next time the daemon starts up. </p>
<p> To disable fast shutdown, use the <code>-F</code> option.</p>
<dt><code>-F</code></p>
<dd> <font SIZE="-1">ALWAYS</font> flush all updates to the <font SIZE="-1">RRD</font> data files when the daemon is shut down, regardless of journal setting.</p>
<dt><code>-g</code></p>
<dd> Run in the foreground. The daemon will not <i>fork()</i>.</p>
<dt><code>-b</code> <i>dir</i></p>
<dd> The daemon will change into a specific directory at startup. All files passed to the daemon, that are specified by a <code>relative</code> path, will be interpreted to be relative to this directory. If not given the default, <tt>&quot;/tmp&quot;</tt>, will be used. </p>
<pre><code>
+ -- -- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- --+!Command line !File updated !+-- -- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- --+!foo.rrd ! / tmp / foo.rrd !!foo / bar.rrd ! / tmp / foo / bar.rrd !! / var / lib / rrd / foo.rrd ! / var / lib / rrd / foo.rrd !+-- -- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- --+Paths given on the command line and paths actually
                                                                                                                                                                                                                                                                                                                                                                                                                                  updated by the daemon,
    assuming the base directory
    "/tmp".
</code></pre>
<p> <font SIZE="-1"><code>WARNING:</code></font> The paths up to and including the base directory <font SIZE="-1"><code>MUST</code></font><font SIZE="-1"><code>NOT</code></font><font SIZE="-1"><code>BE</code></font> symbolic links. In other words, if the base directory is specified as: </p>
<pre>
    -b /base/dir/somewhere
</pre>
<p> &#8230; then <font SIZE="-1"><code>NONE</code></font> of the following should be symbolic links: </p>
<pre>
    /base
    /base/dir
    /base/dir/somewhere
</pre>
<dt><code>-B</code></p>
<dd> Only permit writes into the base directory specified in <code>-b</code> (and any sub-directories). This does <font SIZE="-1"><code>NOT</code></font> detect symbolic links. Paths containing <tt>&quot;../&quot;</tt> will also be blocked.</dl>
<h2>AFFECTED RRDTOOL COMMANDS</h2>
<p> The following commands may be made aware of the <code>rrdcached</code> using the command line argument <code>&#8211;daemon</code> or the environment variable <font SIZE="-1"><code>RRDCACHED_ADDRESS</code></font>:</p>
<dl>
<dt>&bull;</p>
<dd> dump</p>
<dt>&bull;</p>
<dd> fetch</p>
<dt>&bull;</p>
<dd> flush</p>
<dt>&bull;</p>
<dd> graph</p>
<dt>&bull;</p>
<dd> graphv</p>
<dt>&bull;</p>
<dd> info</p>
<dt>&bull;</p>
<dd> last</p>
<dt>&bull;</p>
<dd> lastupdate</p>
<dt>&bull;</p>
<dd> update</p>
<dt>&bull;</p>
<dd> xport</dl>
<p> The <code>update</code> command can send values to the daemon instead of writing them to the disk itself. All other commands can send a <font SIZE="-1"><code>FLUSH</code></font> command (see below) to the daemon before accessing the files, so they work with up-to-date data even if the cache timeout is large.</p>
<h2>ERROR REPORTING</h2>
<p> The daemon reports errors in one of two ways: During startup, error messages are printed to <tt>&quot;STDERR&quot;</tt>. One of the steps when starting up is to fork to the background and closing <tt>&quot;STDERR&quot;</tt> &#8211; after this writing directly to the user is no longer possible. Once this has happened, the daemon will send log messages to the system logging daemon using <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3). The facility used is <tt>&quot;LOG_DAEMON&quot;</tt>.</p>
<h2>HOW IT WORKS</h2>
<p> When receiving an update, <code>rrdcached</code> does not write to disk but looks for an entry for that file in its internal tree. If not found, an entry is created including the current time (called &#8220;First&#8221; in the diagram below). This time is <code>not</code> the time specified on the command line but the time the operating system considers to be &#8220;now&#8221;. The value and time of the value (called &#8220;Time&#8221; in the diagram below) are appended to the tree node. </p>
<p> When appending a value to a tree node, it is checked whether it&#8217;s time to write the values to disk. Values are written to disk if <tt>&quot;now()&nbsp;<wbr>- First&nbsp;<wbr>&gt;=&nbsp;<wbr>timeout&quot;</tt>, where <tt>&quot;timeout&quot;</tt> is the timeout specified using the <code>-w</code> option, see &#8220;<font SIZE="-1">OPTIONS</font>&#8221;. If the values are &#8220;old enough&#8221; they will be enqueued in the &#8220;update queue&#8221;, i. e. they will be appended to the linked list shown below. Because the tree nodes and the elements of the linked list are the same data structures in memory, any update to a file that has already been enqueued will be written with the next write to the <font SIZE="-1">RRD</font> file, too. </p>
<p> A separate &#8220;update thread&#8221; constantly dequeues the first element in the update queue and writes all its values to the appropriate file. So as long as the update queue is not empty files are written at the highest possible rate. </p>
<p> Since the timeout of files is checked only when new values are added to the file, &#8220;dead&#8221; files, i. e. files that are not updated anymore, would never be written to disk. Therefore, every now and then, controlled by the <code>-f</code> option, the entire tree is walked and all &#8220;old&#8221; values are enqueued. Since this only affects &#8220;dead&#8221; files and walking the tree is relatively expensive, you should set the &#8220;flush interval&#8221; to a reasonably high value. The default is 3600 seconds (one hour). </p>
<p> The downside of caching values is that they won&#8217;t show up in graphs generated from the <font SIZE="-1">RRD</font>&nbsp;<wbr>files. To get around this, the daemon provides the &#8220;flush command&#8221; to flush specific files. This means that the file is inserted at the <code>head</code> of the update queue or moved there if it is already enqueued. The flush command will return only after the file&#8217;s pending updates have been written to disk. </p>
<p>+ &#8212; &#8212; &#8211;+ +&#8211; &#8212; &#8211;+ +&#8211; &#8212; &#8211;+!head !!root !!tail !+&#8211; -+&#8211;+ +&#8211; -+&#8211;+ +&#8211; -+&#8211;+! /\ !! /  \ !! /\ /\ !! /\/\ \ `&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -&#8230; &#8212; &#8212; &#8212; &#8211;, !V /      `&#8211; &#8212; &#8212; -, !V + &#8212; -+&#8211; &#8211;+&#8211; -+ +&#8211; &#8212; &#8211;+&#8211; &#8212; -+ +&#8211; -+&#8211; &#8211;+&#8211; -+!File:foo !!File:bar !!File:qux !!First:101 !!First:119 !!First:180 !!Next:&amp;bar &#8211; +&#8212;&gt;!Next:&amp;&#8230; &#8211; +&#8212;&gt;&#8230; &#8212;&gt;!Next:NULL ! | Prev:NULL ! &lt; &#8212; -+-Prev:&amp;foo ! &lt; &#8212; -&#8230; &#8212; &#8211;+-Prev:&amp;&#8230;! += == == == == == = + += == == == == == = + += == == == == == = +!Time:100 !!Time:120 !!Time:180 !!Value:10 !!Value:0.1 !!Value:2, 2 !+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+ +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+ +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+!Time:110 !!Time:130 !!Time:190 !!Value:26 !!Value:0.1 !!Value:7, 3 !+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+ +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+ +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+ : : : : ::<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+ +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+ +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+!<br />
                                                                                                                                                                                                                                                Time:230 !!<br />
                                                                                                                                                                                                                                                Time:250 !!<br />
                                                                                                                                                                                                                                                Time:310 !!<br />
                                                                                                                                                                                                                                               Value:42 !!<br />
                                                                                                                                                                                                                                               Value:0.2 !!<br />
                                                                                                                                                                                                                                               Value:1, 2 !+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+ +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+ +&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+</p>
<p> The above diagram demonstrates:</p>
<dl>
<dt>&bull;</p>
<dd> Files/values are stored in a (balanced) tree.</p>
<dt>&bull;</p>
<dd> Tree nodes and entries in the update queue are the same data structure.</p>
<dt>&bull;</p>
<dd> The local time (&#8220;First&#8221;) and the time specified in updates (&#8220;Time&#8221;) may differ.</p>
<dt>&bull;</p>
<dd> Timed out values are inserted at the &#8220;tail&#8221;.</p>
<dt>&bull;</p>
<dd> Explicitly flushed values are inserted at the &#8220;head&#8221;.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">ASCII</font> art rocks.</dl>
<h2>SECURITY CONSIDERATIONS</h2>
<h3>Authentication</h3>
<p> If your rrdtool installation was built without libwrap there is no form of authentication for clients connecting to the rrdcache daemon! </p>
<p> If your rrdtool installation was built with libwrap then you can use hosts_access to restrict client access to the rrdcache daemon (rrdcached). For more information on how to use hosts_access to restrict access to the rrdcache daemon you should read the <i><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></i>(5) man pages. </p>
<p> It is still highly recommended to install a packet filter or similar mechanism to prevent unauthorized connections. Unless you have a dedicated <font SIZE="-1">VLAN</font> or <font SIZE="-1">VPN</font> for this, using network sockets is probably a bad idea!</p>
<h3>Authorization</h3>
<p> There is minimal per-socket authorization. </p>
<p> Authorization is currently done on a per-socket basis. That means each socket has a list of commands it will accept and it will accept. It will accept only those commands explicitly listed but it will (currently) accept these commands from anyone reaching the socket. </p>
<p> If the networking sockets are to be used, it is necessary to restrict the accepted commands to those needed by external clients. If, for example, external clients want to draw graphs of the cached data, they should only be allowed to use the <tt>&quot;FLUSH&quot;</tt> command.</p>
<h3>Encryption</h3>
<p> There is no encryption. </p>
<p> Again, this may be added in the future, but for the time being it is your job to keep your private data private. Install a <font SIZE="-1">VPN</font> or an encrypted tunnel if you statistics are confidential!</p>
<h3>Sanity checking</h3>
<p> There is no sanity checking. </p>
<p> The daemon will blindly write to any file it gets told, so you really should create a separate user just for this daemon. Also it does not do any sanity checks, so if it gets told to write values for a time far in the future, your files will be messed up good!</p>
<h3>Conclusion</h3>
<dl>
<dt>&bull;</p>
<dd> Security is the job of the administrator.</p>
<dt>&bull;</p>
<dd> We recommend to allow write access via <font SIZE="-1">UNIX</font> domain sockets only.</p>
<dt>&bull;</p>
<dd> You have been warned.</dl>
<h2>PROTOCOL</h2>
<p> The daemon communicates with clients using a line based <font SIZE="-1">ASCII</font> protocol which is easy to read and easy to type. This makes it easy for scripts to implement the protocol and possible for users to use telnet to connect to the daemon and test stuff &#8220;by hand&#8221;. </p>
<p> The protocol is line based, this means that each record consists of one or more lines. A line is terminated by the line feed character <tt>0x0A</tt>, commonly written as <tt>&quot;
&quot;</tt>. In the examples below, this character will be written as <tt>&quot;&lt;LF&gt;&quot;</tt> (&#8220;line feed&#8221;). </p>
<p> After the connection has been established, the client is expected to send a &#8220;command&#8221;. A command consists of the command keyword, possibly some arguments, and a terminating newline character. For a list of commands, see &#8220;Valid Commands&#8221; below. </p>
<p> Example: </p>
<pre>
  FLUSH /tmp/foo.rrd&lt;LF&gt;
</pre>
<p> The daemon answers with a line consisting of a status code and a short status message, separated by one or more space characters. A negative status code signals an error, a positive status code or zero signal success. If the status code is greater than zero, it indicates the number of lines that follow the status line. </p>
<p> Examples: </p>
<pre>
 0 Success&lt;LF&gt;
 2 Two lines follow&lt;LF&gt;
 This is the first line&lt;LF&gt;
 And this is the second line&lt;LF&gt;
</pre>
<h3>Valid Commands</h3>
<p> The following commands are understood by the daemon:</p>
<dl>
<dt><font SIZE="-1"><code>FLUSH</code></font> <i>filename</i></p>
<dd> Causes the daemon to put <i>filename</i> to the <code>head</code> of the update queue (possibly moving it there if the node is already enqueued). The answer will be sent <code>after</code> the node has been dequeued.</p>
<dt><font SIZE="-1"><code>FLUSHALL</code></font></p>
<dd> Causes the daemon to start flushing <font SIZE="-1">ALL</font> pending values to disk. This returns immediately, even though the writes may take a long time.</p>
<dt><font SIZE="-1"><code>PENDING</code></font> <i>filename</i></p>
<dd> Shows any &#8220;pending&#8221; updates for a file, in order. The updates shown have not yet been written to the underlying <font SIZE="-1">RRD</font> file.</p>
<dt><font SIZE="-1"><code>FORGET</code></font> <i>filename</i></p>
<dd> Removes <i>filename</i> from the cache. Any pending updates <font SIZE="-1"><code>WILL</code></font><font SIZE="-1"><code>BE</code></font><font SIZE="-1"><code>LOST</code></font>.</p>
<dt><font SIZE="-1"><code>QUEUE</code></font></p>
<dd> Shows the files that are on the output queue. Returns zero or more lines in the following format, where &lt;num_vals&gt; is the number of values to be written for the &lt;file&gt;: </p>
<pre>
    &lt;num_vals&gt; &lt;file&gt;
</pre>
<dt><font SIZE="-1"><code>HELP</code></font> [<i>command</i>]</p>
<dd> Returns a short usage message. If no command is given, or <i>command</i> is <font SIZE="-1"><code>HELP</code></font>, a list of commands supported by the daemon is returned. Otherwise a short description, possibly containing a pointer to a manual page, is returned. Obviously, this is meant for interactive usage and the format in which the commands and usage summaries are returned is not well defined.</p>
<dt><font SIZE="-1"><code>STATS</code></font></p>
<dd> Returns a list of metrics which can be used to measure the daemons performance and check its status. For a description of the values returned, see &#8220;Performance Values&#8221; below. </p>
<p> The format in which the values are returned is similar to many other line based protocols: Each value is printed on a separate line, each consisting of the name of the value, a colon, one or more spaces and the actual value. </p>
<p> Example: </p>
<pre>
 9 Statistics follow
 QueueLength: 0
 UpdatesReceived: 30
 FlushesReceived: 2
 UpdatesWritten: 13
 DataSetsWritten: 390
 TreeNodesNumber: 13
 TreeDepth: 4
 JournalBytes: 190
 JournalRotate: 0
</pre>
<dt><font SIZE="-1"><code>UPDATE</code></font> <i>filename</i> <i>values</i> [<i>values</i> &#8230;]</p>
<dd> Adds more data to a filename. This is <code>the</code> operation the daemon was designed for, so describing the mechanism again is unnecessary. Read &#8220;<font SIZE="-1">HOW</font> <font SIZE="-1">IT</font> <font SIZE="-1">WORKS</font>&#8221; above for a detailed explanation. </p>
<p> Note that rrdcached only accepts absolute timestamps in the update values. Updates strings like &#8220;N:1:2:3&#8221; are automatically converted to absolute time by the <font SIZE="-1">RRD</font> client library before sending to rrdcached.</p>
<dt><font SIZE="-1"><code>WROTE</code></font> <i>filename</i></p>
<dd> This command is written to the journal after a file is successfully written out to disk. It is used during journal replay to determine which updates have already been applied. It is <i>only</i> valid in the journal; it is not accepted from the other command channels.</p>
<dt><font SIZE="-1"><code>BATCH</code></font></p>
<dd> This command initiates the bulk load of multiple commands. This is designed for installations with extremely high update rates, since it permits more than one command to be issued per <i>read()</i> and <i>write()</i>. </p>
<p> All commands are executed just as they would be if given individually, except for output to the user. Messages indicating success are suppressed, and error messages are delayed until the client is finished. </p>
<p> Command processing is finished when the client sends a dot (&#8220;.&#8221;) on its own line. After the client has finished, the server responds with an error count and the list of error messages (if any). Each error messages indicates the number of the command to which it corresponds, and the error message itself. The first user command after <font SIZE="-1"><code>BATCH</code></font> is command number one. </p>
<pre><code>
    client:  BATCH
    server:  0 Go ahead.  End with dot '.' on its own line.
    client:  UPDATE x.rrd 1223661439:1:2:3            &lt;--- command #1
    client:  UPDATE y.rrd 1223661440:3:4:5            &lt;--- command #2
    client:  and so on...
    client:  .
    server:  2 Errors
    server:  1 message for command 1
    server:  12 message for command 12
</code></pre>
<dt><font SIZE="-1"><code>QUIT</code></font></p>
<dd> Disconnect from rrdcached.</dl>
<h3>Performance Values</h3>
<p> The following counters are returned by the <font SIZE="-1"><code>STATS</code></font> command:</p>
<dl>
<dt><code>QueueLength</code> <i>(unsigned 64bit integer)</i></p>
<dd> Number of nodes currently enqueued in the update queue.</p>
<dt><code>UpdatesReceived</code> <i>(unsigned 64bit integer)</i></p>
<dd> Number of <font SIZE="-1">UPDATE</font> commands received.</p>
<dt><code>FlushesReceived</code> <i>(unsigned 64bit integer)</i></p>
<dd> Number of <font SIZE="-1">FLUSH</font> commands received.</p>
<dt><code>UpdatesWritten</code> <i>(unsigned 64bit integer)</i></p>
<dd> Total number of updates, i. e. calls to <tt>&quot;rrd_update_r&quot;</tt>, since the daemon was started.</p>
<dt><code>DataSetsWritten</code> <i>(unsigned 64bit integer)</i></p>
<dd> Total number of &#8220;data sets&#8221; written to disk since the daemon was started. A data set is one or more values passed to the <font SIZE="-1"><code>UPDATE</code></font> command. For example: <tt>&quot;1223661439:123:456&quot;</tt> is one data set with two values. The term &#8220;data set&#8221; is used to prevent confusion whether individual values or groups of values are counted.</p>
<dt><code>TreeNodesNumber</code> <i>(unsigned 64bit integer)</i></p>
<dd> Number of nodes in the cache.</p>
<dt><code>TreeDepth</code> <i>(unsigned 64bit integer)</i></p>
<dd> Depth of the tree used for fast key lookup.</p>
<dt><code>JournalBytes</code> <i>(unsigned 64bit integer)</i></p>
<dd> Total number of bytes written to the journal since startup.</p>
<dt><code>JournalRotate</code> <i>(unsigned 64bit integer)</i></p>
<dd> Number of times the journal has been rotated since startup.</dl>
<h2>SIGNALS</h2>
<dl>
<dt><font SIZE="-1">SIGINT</font> and <font SIZE="-1">SIGTERM</font></p>
<dd> The daemon exits normally on receipt of either of these signals. Pending updates are handled in accordance with the <code>-j</code> and <code>-F</code> options.</p>
<dt><font SIZE="-1">SIGUSR1</font></p>
<dd> The daemon exits <font SIZE="-1">AFTER</font> flushing all updates out to disk. This may take a while.</p>
<dt><font SIZE="-1">SIGUSR2</font></p>
<dd> The daemon exits immediately, without flushing updates out to disk. Pending updates will be replayed from the journal when the daemon starts up again. <font SIZE="-1"><code>WARNING:</code></font><code> if journaling (-j) is </code><font SIZE="-1"><code>NOT</code></font><code> enabled, any pending updates </code><font SIZE="-1"><code>WILL</code></font><font SIZE="-1"><code>BE</code></font><font SIZE="-1"><code>LOST</code></font>.</dl>
<h2>BUGS</h2>
<p> No known bugs at the moment.</p>
<h2>SEE ALSO</h2>
<p> rrdtool, rrdgraph</p>
<h2>AUTHOR</h2>
<p> Florian Forster &lt;octo at verplant.org&gt; </p>
<p> Both <code>rrdcached</code> and this manual page have been written by Florian.</p>
<h2>CONTRIBUTORS</h2>
<p> kevin brintnall &lt;kbrint [at] rufus.net&gt; </p>
<h2>Index</h2>
