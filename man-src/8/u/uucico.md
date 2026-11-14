---
title: "uucico(8)"
name: "uucico"
section: "8"
letter: "u"
url: "/docs/linux/man/8-uucico/"
description: "uucico – UUCP file transfer daemon"
---

<p>uucico &#8211; UUCP file transfer daemon</p>
<h2>Synopsis</h2>
<p><code>uucico</code> [ options ]</p>
<h2>Description</h2>
<p>The <i>uucico</i> daemon processes file transfer requests queued by <i>uucp</i> (1) and <i>uux</i> (1). It is started when <i>uucp</i> or <i>uux</i> is run (unless they are given the <code>-r</code> option). It is also typically started periodically using entries in the <i>crontab</i> table(s). </p>
<p> When invoked with <code>-r1,</code> <code>&#8211;master,</code> <code>-s,</code> <code>&#8211;system,</code> or <code>-S,</code> the daemon will place a call to a remote system, running in master mode. Otherwise the daemon will start in slave mode, accepting a call from a remote system. Typically a special login name will be set up for UUCP which automatically invokes <i>uucico</i> when a call is made. </p>
<p> When <i>uucico</i> terminates, it invokes the <i>uuxqt</i> (8) daemon, unless the <code>-q</code> or <code>&#8211;nouuxqt</code> option is given; <i>uuxqt</i> (8) executes any work orders created by <i>uux</i> (1) on a remote system, and any work orders created locally which have received remote files for which they were waiting. </p>
<p> If a call fails, <i>uucico</i> will normally refuse to retry the call until a certain (configurable) amount of time has passed. This may be overriden by the <code>-f,</code> <code>&#8211;force,</code> or <code>-S</code> option. </p>
<p> The <code>-l,</code> <code>&#8211;prompt,</code> <code>-e,</code> or <code>&#8211;loop</code> options may be used to force <i>uucico</i> to produce its own prompts of &quot;login: &quot; and &quot;Password:&quot;. When another daemon calls in, it will see these prompts and log in as usual. The login name and password will normally be checked against a separate list kept specially for <i>uucico</i> rather than the <i>/etc/passwd</i> file; it is possible on some systems to direct <i>uucico</i> to use the <i>/etc/passwd</i> file. The <code>-l</code> or <code>&#8211;prompt</code> option will prompt once and then exit; in this mode the UUCP administrator or the superuser may use the <code>-u</code> or <code>&#8211;login</code> option to force a login name, in which case <i>uucico</i> will not prompt for one. The <code>-e</code> or <code>&#8211;loop</code> option will prompt again after the first session is over; in this mode <i>uucico</i> will permanently control a port. </p>
<p> If <i>uucico</i> receives a SIGQUIT, SIGTERM or SIGPIPE signal, it will cleanly abort any current conversation with a remote system and exit. If it receives a SIGHUP signal it will abort any current conversation, but will continue to place calls to (if invoked with <code>-r1</code> or <code>&#8211;master)</code> and accept calls from (if invoked with <code>-e</code> or <code>&#8211;loop)</code> other systems. If it receives a SIGINT signal it will finish the current conversation, but will not place or accept any more calls.</p>
<h2>Options</h2>
<p>The following options may be given to <i>uucico.</i></p>
<dl>
<dt><code>-r1, &#8211;master</code></p>
<dd>Start in master mode (call out to a system); implied by <code>-s,</code> <code>&#8211;system,</code> or <code>-S.</code> If no system is specified, call any system for which work is waiting to be done.</p>
<dt><code>-r0, &#8211;slave</code></p>
<dd>Start in slave mode. This is the default.</p>
<dt><code>-s system, &#8211;system system</code></p>
<dd>Call the named system.</p>
<dt><code>-S system</code></p>
<dd>Call the named system, ignoring any required wait. This is equivalent to <code>-s system -f.</code></p>
<dt><code>-f, &#8211;force</code></p>
<dd>Ignore any required wait for any systems to be called.</p>
<dt><code>-l, &#8211;prompt</code></p>
<dd>Prompt for login name and password using &quot;login: &quot; and &quot;Password:&quot;. This allows <i>uucico</i> to be easily run from <i>inetd</i> (8). The login name and password are checked against the UUCP password file, which probably has no connection to the file <i>/etc/passwd.</i> The <code>&#8211;login </code> option may be used to force a login name, in which cause <i>uucico</i> will only prompt for a password.</p>
<dt><code>-p port, &#8211;port port</code></p>
<dd>Specify a port to call out on or to listen to.</p>
<dt><code>-e, &#8211;loop</code></p>
<dd>Enter endless loop of login/password prompts and slave mode daemon execution. The program will not stop by itself; you must use <i>kill</i> (1) to shut it down.</p>
<dt><code>-w, &#8211;wait</code></p>
<dd>After calling out (to a particular system when <code>-s,</code> <code>&#8211;system,</code> or <code>-S</code> is specifed, or to all systems which have work when just <code>-r1</code> or <code>&#8211;master</code> is specifed), begin an endless loop as with <code>&#8211;loop.</code></p>
<dt><code>-q, &#8211;nouuxqt</code></p>
<dd>Do not start the <i>uuxqt</i> (8) daemon when finished.</p>
<dt><code>-c, &#8211;quiet</code></p>
<dd>If no calls are permitted at this time, then don&#8217;t make the call, but also do not put an error message in the log file and do not update the system status (as reported by <i>uustat</i> (1)). This can be convenient for automated polling scripts, which may want to simply attempt to call every system rather than worry about which particular systems may be called at the moment. This option also suppresses the log message indicating that there is no work to be done.</p>
<dt><code>-C, &#8211;ifwork</code></p>
<dd>Only call the system named by <code>-s,</code> <code>&#8211;system</code> or <code>-S</code> if there is work for that system.</p>
<dt><code>-D, &#8211;nodetach</code></p>
<dd>Do not detach from the controlling terminal. Normally <i>uucico</i> detaches from the terminal before each call out to another system and before invoking <i>uuxqt.</i> This option prevents this.</p>
<dt><code>-u name, &#8211;login name</code></p>
<dd>Set the login name to use instead of that of the invoking user. This option may only be used by the UUCP administrator or the superuser. If used with <code>&#8211;prompt,</code> this will cause <i>uucico</i> to prompt only for the password, not the login name.</p>
<dt><code>-z, &#8211;try-next</code></p>
<dd>If a call fails after the remote system is reached, try the next alternate rather than simply exiting.</p>
<dt><code>-i type, &#8211;stdin type</code></p>
<dd>Set the type of port to use when using standard input. The only support port type is TLI, and this is only available on machines which support the TLI networking interface. Specifying <code>-iTLI</code> causes <i>uucico</i> to use TLI calls to perform I/O.</p>
<dt><code>-x type, -X type, &#8211;debug type</code></p>
<dd>Turn on particular debugging types. The following types are recognized: abnormal, chat, handshake, uucp-proto, proto, port, config, spooldir, execute, incoming, outgoing. </p>
<p> Multiple types may be given, separated by commas, and the <code>&#8211;debug</code> option may appear multiple times. A number may also be given, which will turn on that many types from the foregoing list; for example, <code>&#8211;debug 2</code> is equivalent to <code>&#8211;debug abnormal,chat.</code> </p>
<p> The debugging output is sent to the debugging file, which may be printed using <i>uulog -D.</i></p>
<dt><code>-I file, &#8211;config file</code></p>
<dd>Set configuration file to use. This option may not be available, depending upon how <i>uucico</i> was compiled.</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Report version information and exit.</p>
<dt><code>&#8211;help</code></p>
<dd>Print a help message and exit.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-kill/">kill</a>(1), <a href="/docs/linux/man/1-uucp/">uucp</a>(1), <a href="/docs/linux/man/1-uux/">uux</a>(1), <a href="/docs/linux/man/1-uustat/">uustat</a>(1), <a href="/docs/linux/man/8-uuxqt/">uuxqt</a>(8)</p>
<h2>Author</h2>
<p>Ian Lance Taylor &lt;ian [at] airs.com&gt;</p>
