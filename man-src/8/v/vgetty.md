---
title: "vgetty(8)"
name: "vgetty"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vgetty/"
description: "vgetty – voice extension to the mgetty+sendfax program"
---

<p>vgetty &#8211; voice extension to the mgetty+sendfax program</p>
<h2>Synopsis</h2>
<p><code>vgetty</code> [<code>options</code>] ttydevice </p>
<p> <code>vgetty</code> is not meant to be run from the command line. </p>
<p> Systems with <code>SysV initscripts</code> should start <code>vgetty</code> from the /etc/inittab file so it can respawn after each call. Here is a typical inittab entry: </p>
<p> S0:345:respawn:/usr/local/sbin/vgetty ttyS0 </p>
<p> If you already have a line in your inittab file which invokes <code>mgetty,</code> replace it with <code>vgetty,</code> since it replaces/extends its functionality. </p>
<p> <code>systemd</code> &#8211; <code>vgetty </code> contains vgetty [at] .service unit file template. It is possible to enable an instance of a vgetty to run on a particular device (e.g. systemctl enable vgetty [at] ttyS0.service). See <a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a>(5) for further details.</p>
<h2>Description</h2>
<p><code>vgetty</code> is an extension to the mgetty+sendfax program which provides an interface to voice-capable modems. Use it to operate your modem as a simple answering machine or build your own sophisticated voice messaging system. <code>vgetty</code> handles all the voice-modem specific protocols, giving application programs a uniform, modem-independent voice library. Supported modems include many common serial modems from 3com/USRobotics, Elsa, Multitech, ZyXEL, and others. Caller ID and Distinctive Ring are supported provided you have subscribed to these services from your phone company. Software-based modems (winmodems) are not supported. </p>
<p> <code>vgetty</code> comes with tools to convert au/wav/voc sound files to/from the format used by most supported modems. Basic editing and filtering of sound files is included as well. See <code><a href="/docs/linux/man/1-pvf/">pvf</a>(1)</code> for more information.</p>
<h2>Options</h2>
<p><code>vgetty</code> accepts the same options as <code>mgetty.</code> The one&#8217;s relevant to voice mode are given here. See <code><a href="/docs/linux/man/8-mgetty/">mgetty</a>(8)</code> for other options related to data and fax modes.</p>
<dl>
<dt><code>-a</code></p>
<dd>Use autobauding (change port speed to modem CONNECT speed). There is no voice modem that needs this, the option is just documented for completeness.</p>
<dt><code>-m &#8216;expect send &#8230;&#8217;</code></p>
<dd>Set the chat sequence that is used to initialize the modem. For an empty expect part, use empty double quotes (&quot;&quot;). Since the sequence contains spaces, you will have to enclose all of it in single quotes (&#8221;). Example: </p>
<p> vgetty -m &#8216;&quot;&quot; ATH0 OK&#8217;</p>
<dt><code>-n &lt;rings&gt;</code></p>
<dd>Set the number of rings after which <code>vgetty</code> will answer the phone</p>
<dt><code>-s &lt;speed&gt;</code></p>
<dd>Set the serial port speed to use, e.g. &quot;-s 38400&quot;. This is the speed of communication between the computer and modem in bits/sec (baud).</p>
<dt><code>-x &lt;log level&gt;</code></p>
<dd>Set the log verbosity level. Zero (0) means no logging, six (6) is really noisy. Use level six (6) when sending problem reports to the maintainer. The log file is <i>/var/log/vgetty.ttyXX.</i></dl>
<h2>Environment</h2>
<p><code>vgetty</code> sets the following environment variables when calling external programs:</p>
<dl>
<dt><code>CALLER_ID</code></p>
<dd>The caller&#8217;s telephone number.</p>
<dt><code>CALLED_ID</code></p>
<dd>The number the caller has dialed. Useful for ISDN with multiple incoming phone numbers on the same physical line.</p>
<dt><code>CONNECT</code></p>
<dd>The connect string as reported by the modem (e.g. &quot;38400/V.32bis/V.42bis &#8230; &quot;, etc.).</p>
<dt><code>DEVICE</code></p>
<dd>The tty device being used (e.g. &quot;ttyS0&quot;). Useful for handling multiple devices (&quot;messages on this line are for work, messages on the other line are personal&quot;).</dl>
<h2>Resources</h2>
<p><code>vgetty</code> is included in the <code>mgetty+sendfax</code> distribution. For the latest release, go to: </p>
<p> <a href="ftp://alpha.greenie.net/mgetty/source">ftp://alpha.greenie.net/mgetty/source</a> </p>
<p> The <code>vgetty</code> maintainer&#8217;s home page is at: </p>
<p> <a rel="nofollow" href="http://www-internal.alphanet.ch/~schaefer/vgetty.html">http://www-internal.alphanet.ch/~schaefer/vgetty.html</a> </p>
<p> Send problem reports to: </p>
<p> vgetty-maintainer [at] alphanet.ch </p>
<p> For information on <code>mgetty,</code> go to: </p>
<p> <a rel="nofollow" href="http://alpha.greenie.net/mgetty">http://alpha.greenie.net/mgetty</a> </p>
<p> The <code>mgetty</code> mailing list is at mgetty [at] muc.de. The mailing list is mirrored to the de.alt.comm.mgetty newsgroup.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/mgetty+sendfax/voice.conf</i></p>
<dd>Main configuration file for <code>vgetty.</code> Many options here override the equivalents found in <i>/etc/mgetty+sendfax/mgetty.config</i></p>
<dt><i>/etc/nologin.ttyXX</i></p>
<dd>If this file exists, <code>vgetty</code> will not answer calls on device ttyXX.</p>
<dt><i>/var/log/vgetty.ttyXX</i></p>
<dd>Debug log file for <code>vgetty.</code></p>
<dt><i>/var/spool/voice/messages/Index</i></p>
<dd>List of greeting messages to use.</p>
<dt><i>/var/spool/voice/.code</i></p>
<dd>Access code for remote playback of messages using the dtmf.sh script</p>
<dt><i>/var/spool/voice/.flag</i></p>
<dd><code>vgetty</code> touches this file when a new message is received</p>
<dt><i>/var/spool/voice/.timestamp</i></p>
<dd>Used by the dtmf.sh script to record last time of message playback </p>
</dl>
<h2>Diagnostics</h2>
<p>If <code>vgetty</code> doesn&#8217;t work they way you think it should, check the log file. By default, it is located in <i>/var/log/vgetty.ttyXX</i> (for the vgetty process handling device ttyXX, e.g. ttyS0).</p>
<h2>Bugs</h2>
<p><code>vgetty</code> supports most standard voice modems, but many modems are not fully compliant with relevant standards or contain firmware bugs. If you have problems, try upgrading your modem to the latest firmware revision. If you discover a bug with how <code>vgetty</code> reacts to your modem, please email the maintainer (vgetty-maintainer [at] alphanet.ch) describing your problem. Include relevant excerpts from the log file (set log level to six first), and details about your modem (including firmware revision) and operating system.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mgetty/">mgetty</a>(8), <a href="/docs/linux/man/1-pvf/">pvf</a>(1)</code></p>
<h2>Copyright</h2>
<p><code>vgetty</code> is Copyright (c) 1997-2001 Marc Schaefer (schaefer [at] alphanet.ch) and many others, before and after. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This man page was written by Barry Stewart &lt;bstewart [at] smyrnacable.net&gt;, and has CVS version: $Id: vgetty.8,v 1.1 2001/12/22 18:43:22 marcs Exp $</p>
