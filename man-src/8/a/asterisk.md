---
title: "asterisk(8)"
name: "asterisk"
section: "8"
letter: "a"
url: "/docs/linux/man/8-asterisk/"
description: "asterisk – All-purpose telephony server."
---

<p>asterisk &#8211; All-purpose telephony server.</p>
<h2>Synopsis</h2>
<p><code>asterisk</code> [ <code>-tThfdvVqpRgciIn</code> ] [ <code>-C </code><i>file</i> ] [ <code>-U </code><i>user</i> ] [ <code>-G </code><i>group</i> ] [ <code>-x </code><i>command</i> ] [ <code>-M </code><i>value</i> ] <code>asterisk -r</code> [ <code>-v</code> ] [ <code>-x </code><i>command</i> ] [ <code>-s </code><i>socket</i> ] </p>
<h2>Description</h2>
<p><code>asterisk</code> is a full-featured telephony server which provides Private Branch eXchange (PBX), Interactive Voice Response (IVR), Automated Call Distribution (ACD), Voice over IP (VoIP) gatewaying, Conferencing, and a plethora of other telephony applications to a broad range of telephony devices including packet voice (SIP, IAX2, MGCP, Skinny, H.323) devices (both endpoints and proxies), as well as traditional TDM hardware including T1, E1, ISDN PRI, GR-303, RBS, Loopstart, Groundstart, ISDN BRI, and many more. </p>
<p> At start, Asterisk reads the /etc/asterisk/asterisk.conf main configuration file and locates the rest of the configuration files from the configuration in that file. The -C option specifies an alternate main configuration file. Virtually all aspects of the operation of asterisk&#8217;s configuration files can be found in the sample configuration files. The format for those files is generally beyond the scope of this man page. </p>
<p> When running with <code>-c</code>, <code>-r</code> or <code>-R</code> options, Asterisk supplies a powerful command line, including command completion, which may be used to monitors its status, perform a variety of administrative actions and even explore the applications that are currently loaded into the system. </p>
<p> Asterisk is a trademark of Digium, Inc.</p>
<h2>Options</h2>
<dl>
<dt><code>-C </code><i>file</i></p>
<dd>Use <i>file</i> as master configuration file instead of the default, /etc/asterisk/asterisk.conf</p>
<dt><code>-c</code></p>
<dd>Provide a control console on the calling terminal. Specifying this option implies <code>-f</code> and will cause asterisk to no longer fork or detach from the controlling terminal.</p>
<dt><code>-d</code></p>
<dd>Enable extra debugging statements. </p>
<p> Note: This always sets the debug level in the asterisk process, even if it is running in the background. This will affect the size of your log files.</p>
<dt><code>-f</code></p>
<dd>Do not fork or detach from controlling terminal.</p>
<dt><code>-g</code></p>
<dd>Remove resource limit on core size, thus forcing Asterisk to dump core in the unlikely event of a segmentation fault or abort signal. <code>NOTE:</code> in some cases this may be incompatible with the <code>-U</code> or <code>-G</code> flags.</p>
<dt><code>-G </code><i>group</i></p>
<dd>Run as group <i>group</i> instead of the calling group. <code>NOTE:</code> this requires substantial work to be sure that Asterisk&#8217;s environment has permission to write the files required for its operation, including logs, its comm socket, the asterisk database, etc.</p>
<dt><code>-h</code></p>
<dd>Provide brief summary of command line arguments and terminate.</p>
<dt><code>-i</code></p>
<dd>Prompt user to initialize any encrypted private keys for IAX2 secure authentication during startup.</p>
<dt><code>-L </code><i>loadaverage</i></p>
<dd>Limits the maximum load average before rejecting new calls. This can be useful to prevent a system from being brought down by terminating too many simultaneous calls.</p>
<dt><code>-m</code></p>
<dd>Disable log and verbose output to remote (-r) consoles.</p>
<dt><code>-M </code><i>value</i></p>
<dd>Limits the maximum number of calls to the specified value. This can be useful to prevent a system from being brought down by terminating too many simultaneous calls.</p>
<dt><code>-n</code></p>
<dd>Disable ANSI colors even on terminals capable of displaying them.</p>
<dt><code>-p</code></p>
<dd>If supported by the operating system (and executing as root), attempt to run with realtime priority for increased performance and responsiveness within the Asterisk process, at the expense of other programs running on the same machine.</p>
<dt><code>-q</code></p>
<dd>Reduce default console output when running in conjunction with console mode (<code>-c</code>).</p>
<dt><code>-r</code></p>
<dd>Instead of running a new Asterisk process, attempt to connect to a running Asterisk process and provide a console interface for controlling it.</p>
<dt><code>-R</code></p>
<dd>Much like <code>-r</code>. Instead of running a new Asterisk process, attempt to connect to a running Asterisk process and provide a console interface for controlling it. Additionally, if connection to the Asterisk process is lost, attempt to reconnect for as long as 30 seconds.</p>
<dt><code>-s </code><i>socket</i></p>
<dd>Allows to specify the socket file to be used to connect to the Asterisk console. Used in conjunction with <code>-r</code> or <code>-R</code>.</p>
<dt><code>-I</code></p>
<dd>Enable internal timing if DAHDI timer is available The default behaviour is that outbound packets are phase locked to inbound packets. Enabling this switch causes them to be locked to the internal DAHDI timer instead.</p>
<dt><code>-t</code></p>
<dd>When recording files, write them first into a temporary holding directory, then move them into the final location when done.</p>
<dt><code>-T</code></p>
<dd>Add timestamp to all non-command related output going to the console when running with verbose and/or logging to the console.</p>
<dt><code>-U </code><i>user</i></p>
<dd>Run as user <i>user</i> instead of the calling user. <code>NOTE:</code> this requires substantial work to be sure that Asterisk&#8217;s environment has permission to write the files required for its operation, including logs, its comm socket, the asterisk database, etc.</p>
<dt><code>-v</code></p>
<dd>Increase the level of verboseness on the console. The more times <code>-v</code> is specified, the more verbose the output is. Specifying this option implies <code>-f</code> and will cause asterisk to no longer fork or detach from the controlling terminal. This option may also be used in conjunction with <code>-r</code> and <code>-R</code>. </p>
<p> Note: This always sets the verbose level in the asterisk process, even if it is running in the background. This will affect the size of your log files.</p>
<dt><code>-V</code></p>
<dd>Display version information and exit immediately.</p>
<dt><code>-x </code><i>command</i></p>
<dd>Connect to a running Asterisk process and execute a command on a command line, passing any output through to standard out and then terminating when the command execution completes. Implies <code>-r</code> when <code>-R</code> is not explicitly supplied.</dl>
<h2>Examples</h2>
<p><code>asterisk</code> &#8211; Begin Asterisk as a daemon </p>
<p> <code>asterisk -vvvgc</code> &#8211; Run on controlling terminal </p>
<p> <code>asterisk -rx &quot;core show channels&quot;</code> &#8211; Display channels on running server</p>
<h2>Bugs</h2>
<p>Bug reports and feature requests may be filed at <a rel="nofollow" href="http://bugs.digium.com">http://bugs.digium.com</a></p>
<h2>See Also</h2>
<p>*CLI&gt; <code>help</code> &#8211; Help on Asterisk CLI </p>
<p> *CLI&gt; <code>core show applications</code> &#8211; Show loaded dialplan applications </p>
<p> *CLI&gt; <code>core show functions</code> &#8211; Show loaded dialplan functions </p>
<p> *CLI&gt; <code>dialplan show</code> &#8211; Show current dialplan </p>
<p> <a rel="nofollow" href="http://www.asterisk.org">http://www.asterisk.org</a> &#8211; The Asterisk Home Page </p>
<p> <a rel="nofollow" href="http://www.asteriskdocs.org">http://www.asteriskdocs.org</a> &#8211; The Asterisk Documentation Project </p>
<p> <a rel="nofollow" href="http://www.voip-info.org/wiki-Asterisk">http://www.voip-info.org/wiki-Asterisk</a> &#8211; The Asterisk Wiki </p>
<p> <a rel="nofollow" href="http://www.digium.com/">http://www.digium.com/</a> &#8211; Asterisk sponsor and hardware supplier </p>
<p> <a rel="nofollow" href="http://www.markocam.com/">http://www.markocam.com/</a> &#8211; Asterisk author&#8217;s web cam</p>
<h2>Author</h2>
<p>Mark Spencer &lt;markster [at] digium.com&gt; </p>
<p> Countless other contributors, see CREDITS with distribution for more information</p>
