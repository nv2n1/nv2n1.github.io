---
title: "acpid(8)"
name: "acpid"
section: "8"
letter: "a"
url: "/docs/linux/man/8-acpid/"
description: "acpid – Advanced Configuration and Power Interface event daemon"
---

<p>acpid &#8211; Advanced Configuration and Power Interface event daemon</p>
<h2>Synopsis</h2>
<p><code>acpid</code> [<i>options</i>] </p>
<h2>Description</h2>
<p><code>acpid</code> is designed to notify user-space programs of ACPI events. <code>acpid</code> should be started during the system boot, and will run as a background process, by default. It will open an events file (<i>/proc/acpi/event</i> by default) and attempt to read whole lines which represent ACPI events. If the events file does not exist, <code>acpid</code> will attempt to connect to the Linux kernel via the input layer and netlink. When an ACPI event is received from one of these sources, <code>acpid</code> will examine a list of rules, and execute the rules that match the event. <code>acpid</code> will ignore all incoming ACPI events if a lock file exists (<i>/var/lock/acpid</i> by default). </p>
<p> <i>Rules</i> are defined by simple configuration files. <code>acpid</code> will look in a configuration directory (<i>/etc/acpi/events</i> by default), and parse all regular files with names that consist entirely of upper and lower case letters, digits, underscores, and hyphens (similar to <code><a href="/docs/linux/man/8-run-parts/">run-parts</a></code>(8)) that do not begin with a period (&#8216;.&#8217;) or end with a tilde (~). Each file must define two things: an <i>event</i> and an <i>action</i>. Any blank lines, or lines where the first character is a hash (&#8216;#&#8217;) are ignored. Extraneous lines are flagged as warnings, but are not fatal. Each line has three tokens: the key, a literal equal sign, and the value. The key can be up to 63 characters, and is case-insensitive (but whitespace matters). The value can be up to 511 characters, and is case and whitespace sensitive. </p>
<p> The event value is a regular expression (see <code><a href="/docs/linux/man/3-regcomp/">regcomp</a></code>(3)), against which events are matched. </p>
<p> The action value is a commandline, which will be invoked via <i>/bin/sh</i> whenever an event matching the rule in question occurs. The commandline may include shell-special characters, and they will be preserved. The only special characters in an action value are &quot;%&quot; escaped. The string &quot;%e&quot; will be replaced by the literal text of the event for which the action was invoked. This string may contain spaces, so the commandline must take care to quote the &quot;%e&quot; if it wants a single token. The string &quot;%%&quot; will be replaced by a literal &quot;%&quot;. All other &quot;%&quot; escapes are reserved, and will cause a rule to not load. </p>
<p> This feature allows multiple rules to be defined for the same event (though no ordering is guaranteed), as well as one rule to be defined for multiple events. To force <code>acpid</code> to reload the rule configuration, send it a SIGHUP. </p>
<p> The pseudo-action <i>&lt;drop&gt;</i> causes the event to be dropped completely and no further processing undertaken; clients connecting via the UNIX domain socket (see below) will not be notified of the event. This may be useful on some machines, such as certain laptops which generate spurious battery events at frequent intervals. The name of this pseudo-action may be redefined with a commandline option. </p>
<p> In addition to rule files, <code>acpid</code> also accepts connections on a UNIX domain socket (<i>/var/run/acpid.socket</i> by default). Any application may connect to this socket. Once connected, <code>acpid</code> will send the text of all ACPI events to the client. The client has the responsibility of filtering for messages about which it cares. <code>acpid</code> will not close the client socket except in the case of a SIGHUP or <code>acpid</code> exiting. </p>
<p> For faster startup, this socket can be passed in as stdin so that <code>acpid</code> need not create the socket. In addition, if a socket is passed in as stdin, <code>acpid</code> will not daemonize. It will be run in foreground. This behavior is provided to support <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1). </p>
<p> <code>acpid</code> will log all of its activities, as well as the stdout and stderr of any actions, to syslog. </p>
<p> All the default files and directories can be changed with commandline options.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code><i></i>, <code>&#8211;confdir</code><i> directory</i></p>
<dd>This option changes the directory in which <code>acpid</code> looks for rule configuration files. Default is <i>/etc/acpi/events</i>.</p>
<dt><code>-C</code><i></i>, <code>&#8211;clientmax</code><i> number</i></p>
<dd>This option changes the maximum number of non-root socket connections which can be made to the <code>acpid</code> socket. Default is <i>256</i>.</p>
<dt><code>-d</code><i></i>, <code>&#8211;debug</code></p>
<dd>This option increases the <code>acpid</code> debug level by one.</p>
<dt><code>-e</code><i></i>, <code>&#8211;eventfile</code><i> filename</i></p>
<dd>This option changes the event file from which <code>acpid</code> reads events. Default is <i>/proc/acpi/event</i>.</p>
<dt><code>-n</code><i></i>, <code>&#8211;netlink</code></p>
<dd>This option forces <code>acpid</code> to use the Linux kernel input layer and netlink interface for ACPI events.</p>
<dt><code>-f</code><i></i>, <code>&#8211;foreground</code></p>
<dd>This option keeps <code>acpid</code> in the foreground by not forking at startup, and makes it log to stderr instead of syslog.</p>
<dt><code>-l</code><i></i>, <code>&#8211;logevents</code></p>
<dd>This option tells <code>acpid</code> to log information about all events and actions.</p>
<dt><code>-L</code><i></i>, <code>&#8211;lockfile</code><i> filename</i></p>
<dd>This option changes the lock file used to stop event processing. Default is <i>/var/lock/acpid</i>.</p>
<dt><code>-g</code><i></i>, <code>&#8211;socketgroup</code><i> groupname</i></p>
<dd>This option changes the group ownership of the UNIX domain socket to which <code>acpid</code> publishes events.</p>
<dt><code>-m</code><i></i>, <code>&#8211;socketmode</code><i> mode</i></p>
<dd>This option changes the permissions of the UNIX domain socket to which <code>acpid</code> publishes events. Default is <i>0666</i>.</p>
<dt><code>-s</code><i></i>, <code>&#8211;socketfile</code><i> filename</i></p>
<dd>This option changes the name of the UNIX domain socket which <code>acpid</code> opens. Default is <i>/var/run/acpid.socket</i>.</p>
<dt><code>-S</code><i></i>, <code>&#8211;nosocket</code></p>
<dd>This option tells <code>acpid</code> not to open a UNIX domain socket. This overrides the <i>-s</i> option, and negates all other socket options.</p>
<dt><code>-p</code><i></i>, <code>&#8211;pidfile</code><i> filename</i></p>
<dd>This option tells <code>acpid</code> to use the specified file as its pidfile. If the file exists, it will be removed and over-written. Default is <i>/var/run/acpid.pid</i>.</p>
<dt><code>-r</code><i></i>, <code>&#8211;dropaction</code><i> action</i></p>
<dd>This option defines the pseudo-action which tells <code>acpid</code> to abort all processing of an event, including client notifications. Default is <i>&lt;drop&gt;</i>.</p>
<dt><code>-t</code><i></i>, <code>&#8211;tpmutefix</code></p>
<dd>This option enables special handling of the mute button for certain ThinkPad models with mute LEDs that get out of sync with the mute state when the mute button is held down. With this option, the mute button will generate the following events in sync with the number of presses (and, by extension, the state of the LED):</p>
<dd>button/mute MUTE (key pressed) K<br />
 button/mute MUTE (key released) K</p>
<dt><code>-v</code><i></i>, <code>&#8211;version</code></p>
<dd>Print version information and exit.</p>
<dt><code>-h</code><i></i>, <code>&#8211;help</code></p>
<dd>Show help and exit.</dl>
<h2>Example</h2>
<p>This example will shut down your system if you press the power button. </p>
<pre><code>Create a file named /etc/acpi/events/power that contains the following:



event=button/power

action=/etc/acpi/power.sh &quot;%e&quot;</code></pre>
<p> Then create a file named /etc/acpi/power.sh that contains the following:</p>
<dl>
<dd>/sbin/shutdown -h now &quot;Power button pressed&quot;</dl>
<p> Now, when <code>acpid</code> is running, a press of the power button will cause the rule in /etc/acpi/events/power to trigger the script in /etc/acpi/power.sh. The script will then shut down the system.</p>
<h2>Troubleshooting</h2>
<p><code>acpid</code> is a simple program that runs scripts in response to ACPI events from the kernel. When there&#8217;s trouble, the problem is rarely with <code>acpid</code> itself. The following are some suggestions for finding the most common sources of ACPI-related problems. </p>
<p> When troubleshooting <code>acpid</code>, it is important to be aware that other parts of a system might be handling ACPI events. <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) is capable of handling the power switch and various other events that are commonly handled by <code>acpid</code>. See the description of HandlePowerKey in <code><a href="/docs/linux/man/5-logind-conf/">logind.conf</a></code>(5) for more. Some window managers also take over <code>acpid</code>&#8216;s normal handling of the power button and other events. </p>
<p> <code><a href="/docs/linux/man/8-kacpimon/">kacpimon</a></code>(8) can be used to verify that the expected ACPI events are coming in. See the man page for <code><a href="/docs/linux/man/8-kacpimon/">kacpimon</a></code>(8) for the proper procedure. If the events aren&#8217;t coming in, you&#8217;ve probably got a kernel driver issue. </p>
<p> If the expected events are coming in, then you&#8217;ll need to check and see if your window manager is responsible for handling these events. Some are, some aren&#8217;t. (E.g. in Ubuntu 14.04 (Unity/GNOME), there are settings for the laptop lid in the System Settings &gt; Power &gt; &quot;When the lid is closed&quot; fields.) If your window manager is responsible for handling the problematic event, and you&#8217;ve got it configured properly, then you may have a window manager issue. </p>
<p> Lastly, take a look in <i>/etc/acpi/events</i> (see above). Is there a configuration file in there for the event in question (e.g. /etc/acpi/events/lidbtn for laptop lid open/close events)? Is it properly connected to a script (e.g. /etc/acpi/lid.sh)? Is that script working? It&#8217;s not unusual for an <code>acpid</code> script to check and see if there is a window manager running, then do nothing if there is. This means it is up to the window manager to handle this event.</p>
<h2>Dependencies</h2>
<p><code>acpid</code> should work on any linux kernel released since 2003.</p>
<h2>Files</h2>
<p><code>/proc/acpi/event</code><br />
 <code>/dev/input/event*</code><br />
 <code>/etc/acpi/</code><br />
 <code>/var/run/acpid.socket</code><br />
 <code>/var/run/acpid.pid</code><br />
 <code>/var/lock/acpid</code></p>
<h2>Bugs</h2>
<p>There are no known bugs. To file bug reports, see <code>PROJECT WEBSITE</code> below.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-regcomp/">regcomp</a></code>(3) <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) <code><a href="/docs/linux/man/1-init/">init</a></code>(1) <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) <code><a href="/docs/linux/man/8-acpi_listen/">acpi_listen</a></code>(8) <code><a href="/docs/linux/man/8-kacpimon/">kacpimon</a></code>(8)</p>
<h2>Project Website</h2>
<p><a rel="nofollow" href="http://sourceforge.net/projects/acpid2/">http://sourceforge.net/projects/acpid2/</a></p>
<h2>Authors</h2>
<p>Ted Felix &lt;ted [at] tedfelix.com&gt;<br />
 Tim Hockin &lt;thockin [at] hockin.org&gt;<br />
 Andrew Henroid</p>
