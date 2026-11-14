---
title: "lircd(8)"
name: "lircd"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lircd/"
description: "lircd – LIRC daemon decodes infrared signals and provides them on a Unix domain socket."
---

<p>lircd &#8211; LIRC daemon decodes infrared signals and provides them on a Unix domain socket.</p>
<h2>Synopsis</h2>
<p><code>lircd</code> [<i>options</i>] [<i>config file</i>]</p>
<h2>Description</h2>
<p>The main task of lircd is to decode the infrared signals and provide an uniform interface for client applications. Clients can connect to lircd through a Unix domain socket which is located in /var/run/lirc/lircd. Using this socket they will get the infrared codes received by lircd and they can send commands to lircd. </p>
<h2>Arguments</h2>
<dl>
<dt><code>config file</code></p>
<dd>The configuration file, by default /etc/lirc/lircd.conf. A relative path is interpreted from /etc/lirc.</p>
<dd>The file is specific for the remote(s) that lircd should decode. The format is described in <a href="/docs/linux/man/5-lircd-conf/">lircd.conf</a>(5). Configuration files could be found using <a href="/docs/linux/man/1-irdb-get/">irdb-get</a>(1) or <a href="/docs/linux/man/1-lirc-setup/">lirc-setup</a>(1). It&#8217;s also possible to generate a config file using <a href="/docs/linux/man/1-irrecord/">irrecord</a>(1) </p>
</dl>
<h2>Options</h2>
<p>Common options:</p>
<dl>
<dt><code>-O, &#8211;options-file &lt;path&gt;</code></p>
<dd>File containing default values for all options. A relative path is interpreted from current directory. See [FILES] below.</p>
<dt><code>-d, &#8211;device &lt;device&gt;</code></p>
<dd>Select the character device which lircd should read from. The default is currently /dev/lirc0 on most systems.</p>
<dd>If you&#8217;re using the devinput driver, you can use <i>name=STRING</i> or <i>phys=STRING</i> to select the device; lircd will look in /dev/input to find a device with a matching description. This is useful in case the device name isn&#8217;t fixed. <i>STRING</i> may contain the &#8216;*&#8217; and &#8216;?&#8217; wildcards and &#8216;\&#8217; to mark them as literal. Use <a href="/docs/linux/man/1-dmesg/">dmesg</a>(1) to find the name and bus address (the names used under /dev/input/by-id are not always usable).</p>
<dt><code>-H, &#8211;driver &lt;driver&gt;</code></p>
<dd>The driver to use. Using <i>&#8211;driver help</i> lists all available drivers, see DRIVER LOADING below.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Displays short thelp message.</p>
<dd>Other options:</p>
<dt><code>-a, &#8211;allow-simulate</code></p>
<dd>Enable the SIMULATE command which can be issued using <a href="/docs/linux/man/1-irsend/">irsend</a>(1). This will allow simulating arbitrary IR events from the command line. Use this option with caution because it will give all users with access to the lircd socket wide control over you system. E.g. if you have configured your system to shut down by a button press on your remote control, everybody will be able to shut down your system from the command line.</p>
<dt><code>-c, &#8211;connect [host[:port]][,[host[:port]]]</code></p>
<dd>Allows you to connect to other lircd servers that provide a network socket at the given host and port number. The number of such connections is currently limited to 100. The connecting lircd instance will receive IR events from the lircd instance it connects to. To connect to multiple servers, add them with a comma separated list.</p>
<dt><code>-D, &#8211;loglevel [level]</code></p>
<dd>Determine the amount of logging information. [level] can be a symbolic syslog level: &#8216;error&#8217;,&#8217;warning, &#8216;info&#8217;, &#8216;notice&#8217; or &#8216;debug&#8217;. lircd also defines three additional levels &#8216;trace&#8217;, &#8216;trace1&#8217; and &#8216;trace2&#8217; which gives even more messages (&#8216;trace2&#8217; bringing the most). However, in the log these messages are marked as &#8216;debug&#8217;.</p>
<dd>The level can also be an integer in the range 3 (almost no messages) to 10.</p>
<dt><code>-A, &#8211;driver-options key:value[|key:value&#8230;]</code></p>
<dd>Set one or more options for the driver. The argument is a list of key:value pairs delimited by &#8216;|&#8217;. The key can not contain spaces, but such are allowed in the value part. Certain characters including &#8216;#&#8217; and &#8216;;&#8217; are used as comment markers in the config file and are not allowed anywhere.</p>
<dt><code>-l, &#8211;listen [[address:]port]]</code></p>
<dd>Let lircd listen for network connections on the given address/port. The default address is 0.0.0.0, which means that connections on all network interfaces will be accepted. The default port is 8765. No security checks are currently implemented. The listening lircd instance will send all IR events to the connecting lircd instances.</p>
<dt><code>-L, &#8211;logfile &lt;logfile path&gt;</code></p>
<dd>Select the lircd daemon log file. logfile is either the string &#8216;syslog&#8217; indicating that <a href="/docs/linux/man/1-syslog/">syslog</a>(1) should be used or a log file path. The default is to use syslog.</p>
<dt><code>-o, &#8211;output &lt;output socket&gt;</code></p>
<dd>Select Unix domain socket, which lircd will write remote key codes to. The default currently is /var/run/lirc/lircd.</p>
<dt><code>-p, &#8211;permission</code></p>
<dd>Gives the file permission of /var/run/lirc/lircd if it has to be created in octal representation. See <a href="/docs/linux/man/1-chmod/">chmod</a>(1). If no &#8211;permission option is given when the socket is initially created the default is to give all users read and write permissions (0666 in octal representation). If /var/run/lirc/lircd already exists this option has no effect.</p>
<dt><code>-p, &#8211;pidfile &lt;path&gt;</code></p>
<dd>Select the lircd daemon pid file, defaults to /var/run/lirc/lircd.pid.</p>
<dt><code>-U &#8211;plugindir</code></p>
<dd>The &#8211;plugindir option sets the directory from which lircd loads it&#8217;s userspace drivers. These are *.so files, by default found as described under DRIVER LOADING.</p>
<dt><code>-r, &#8211;release [suffix]</code></p>
<dd>Enables automatic generation of release events for each button press. lircd will append the given suffix to the button name for each release event. If no suffix is given the default suffix is &#8216;_UP&#8217;.</p>
<dt><code>-R, &#8211;repeat-max &lt;limit&gt;</code></p>
<dd>Sets an upper limit to the number of repeats when sending a signal. The current default is 600. A SEND_START request will repeat the signal this many times. Also, if the number of repeats in a SEND_ONCE request exceeds this number, it will be replaced by this number.</p>
<dt><code>-u, &#8211;uinput</code></p>
<dd>Enable automatic generation of Linux input events. lircd will open /dev/input/uinput and inject key events to the Linux kernel. The key code depends on the name that was given a button in the lircd config file, e.g. if the button is named KEY_1, the &#8216;1&#8217; key code will be generated. You will find a complete list of possible button names in /usr/include/linux/input.h.</p>
<dt><code>-Y, &#8211;dynamic-codes [EXPERIMENTAL]</code></p>
<dd>Allows one to use codes which have been decoded for one remote but are not defined in lircd.conf. New codes are dynamically created with a default name. This feature is experimental and subject to all sorts of changes. It has not ben tested thoroughly.</p>
<dt><code>-e, &#8211;effective-user &lt;uid&gt;</code></p>
<dd>If started as user root, lirc drops it privileges and runs as user &lt;uid&gt; after opening files etc. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/lirc/lircd.conf</code></p>
<dd>Main config file, see <a href="/docs/linux/man/5-lircd-conf/">lircd.conf</a>(5). </p>
<dt><code>/etc/lirc/lirc_options.conf</code></p>
<dd>The options file. lircd handles the values under the [lircd] section in this file. The location can be changed using the -O/&#8211;options-file command-line option or using the environment variable LIRC_OPTIONS_PATH. The values here are used as defaults for any option not present on command line. </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>LIRC_OPTIONS_PATH</code></p>
<dd>Plugin load path, se DRIVER LOADING</p>
<dt><code>LIRC_DEBUG_OPTIONS</code></p>
<dd>If set, enables debugging in early stages when the &#8211;debug parameter is yet not parsed. </p>
</dl>
<h2>Driver Loading</h2>
<p>Drivers are loaded dynamically. This is done from a traditional *ux &#8216;:&#8217;-separated path where each component in the path is searched (leading part first, trailing last). </p>
<p> The path used for this is determined by (falling priority):</p>
<dl>
<dt>&#8211;</p>
<dd>The &#8211;plugindir option.</p>
<dt>&#8211;</p>
<dd>The &#8216;plugindir&#8217; entry in the [lircd] section of the lirc_options.conf file.</p>
<dt>&#8211;</p>
<dd>The environment variable LIRC_PLUGINDIR.</p>
<dt>&#8211;</p>
<dd>A hardcoded default (usually /usr/lib[64]/lirc/plugins). </p>
</dl>
<h2>Signals</h2>
<dl>
<dt><code>HUP</code></p>
<dd>On receiving SIGHUP lircd re-reads the lircd.conf configuration file (but not lirc_options.conf) and adjusts itself if the file has changed.</p>
<dt><code>USR1</code></p>
<dd>On receiving SIGUSR1 lircd makes a clean exit. </p>
</dl>
<h2>Daemons</h2>
<p>lircd is a daemon. You should start it in some init script depending on your system. Besides the preferred systemd setup which is installed by default there are also example scripts for other distros and init systems in the contrib directory.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-irdb-get/">irdb-get</a>(1)<br />
 <a href="/docs/linux/man/1-lirc-setup/">lirc-setup</a>(1)<br />
 <a href="/docs/linux/man/5-lircd-conf/">lircd.conf</a>(5) </p>
