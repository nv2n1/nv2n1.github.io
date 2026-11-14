---
title: "irrecord(1)"
name: "irrecord"
section: "1"
letter: "i"
url: "/docs/linux/man/1-irrecord/"
description: "irrecord – application for recording IR-codes for usage with LIRC"
---

<h2>NAME</h2>
<p> irrecord &#8211; application for recording IR-codes for usage with LIRC</p>
<h2>SYNOPSIS</h2>
<p> <code>irrecord [-f] [-n] [-H driver] [-d device] [file]</code><br />
 <code>irrecord -a &lt;file&gt;</code><br />
 <code>irrecord -l</code><br />
 <code>irrecord &#8211;help | &#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> This program will record the signals from your remote control and create a config file for lircd. A proper config file for lircd is maybe the most vital part of this package, so you should invest some time to create a working config file. Although I put a good deal of effort in this program it is often not possible to automatically recognize all features of a remote control. </p>
<p> If the program fails to recognize the protocol of the remote control you should use the &#8211;force option to at least create a config file in raw mode. </p>
<p> If <i>file</i> is not specified it defaults to &quot;irrecord.conf&quot; </p>
<p> If <i>file</i> already exists and contains a valid config irrecord will use the protocol description found there and will only try to record the buttons. This is very useful if you want to learn a remote where config files of the same brand are already available. Of course this will only work if the remotes use the same protocol but it&#8217;s worth a try. You will find template files for the most common protocols in the remotes/generic/ directory of this package. The name of the new file is created by appending .conf to the given filename in this case.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> display this message</p>
<dt><code>-v</code> <code>&#8211;version</code></p>
<dd> display version</p>
<dt><code>-a</code> <code>&#8211;analyse</code></p>
<dd> Analyse a raw_codes config file, trying to convert it to a regular configuration.</p>
<dt><code>-f</code> <code>&#8211;force</code></p>
<dd> Force raw mode. Use this if recording fails otherwise. This creates a raw codes configuration file which can be used as-is or converted using the -a option.</p>
<dt><code>-n</code> <code>&#8211;disable-namespace</code></p>
<dd> disables namespace checks</p>
<dt><code>-l</code> <code>&#8211;list-namespace</code></p>
<dd> list valid button names</p>
<dt><code>-H</code> <code>&#8211;driver</code>=<i>driver</i></p>
<dd> Use given driver. -H help lists available drivers.</p>
<dt><code>-d</code> <code>&#8211;device</code>=<i>device</i></p>
<dd> read from given device</p>
<dt><code>-D</code> <code>&#8211;loglevel</code>=<i>level</i></p>
<dd> Determine the amount of logging information. [level] can be a symbolic syslog level: &#8216;error&#8217;,&#8217;warning, &#8216;info&#8217;, &#8216;notice&#8217; or &#8216;debug&#8217;. lircd also defines three additional levels &#8216;trace&#8217;, &#8216;trace1&#8217; and &#8216;trace2&#8217; which gives even more messages (&#8216;trace2&#8217; bringing the most). However, in the log these messages are marked as &#8216;debug&#8217;. The level can also be an integer in the range 3 (almost no messages) to 10.</dl>
<h2>DRIVER LOAD PATH</h2>
<p> Drivers are loaded dynamically. This is done from a traditional *ux &#8216;:&#8217;-separated path where each component in the path is searched (leading part first, trailing last). </p>
<p> The path used for this is determined by (falling priority):</p>
<dl>
<dt>&#8211;</p>
<dd> The &#8211;plugindir option.</p>
<dt>&#8211;</p>
<dd> The &#8216;plugindir&#8217; entry in the [lircd] section of the lirc_options.conf file.</p>
<dt>&#8211;</p>
<dd> The environment variable LIRC_PLUGINDIR.</p>
<dt>&#8211;</p>
<dd> A hardcoded default (usually /usr/lib[64]/lirc/plugins). </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/lirc/lirc_options.conf</code></p>
<dd> The options file. irrecord mostly handles the values under the [irrecord] section, but some values such as debug and plugindir are inherited from the [lircd] section.</p>
<dt>&#8211;</p>
<dd> The location of this file can be changed using the -O/&#8211;options-file command-line option or using the environment variable LIRC_OPTIONS_PATH. The values here are used as defaults for any option not present on command line. </p>
<dt><code>~/.cache/irrecord.log</code></p>
<dd> Debug output. Setting the XDG_CACHE_HOME environment variable relocates this file to $XDG_CACHE_HOME/irrecord.log </p>
</dl>
<h2>SEE ALSO</h2>
<p> The documentation for <code>lirc</code> is maintained as html pages. They are located under html/ in the documentation directory. </p>
<p> Further information on this topic is available in section &quot;Adding new remote controls&quot; in html/help.html </p>
<h2>Index</h2>
