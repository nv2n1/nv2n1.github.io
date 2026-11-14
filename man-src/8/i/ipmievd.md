---
title: "ipmievd(8)"
name: "ipmievd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipmievd/"
description: "ipmievd – IPMI event daemon for sending events to syslog"
---

<p>ipmievd &#8211; IPMI event daemon for sending events to syslog</p>
<h2>Synopsis</h2>
<p>ipmievd [<code>-c</code>|<code>-h</code>|<code>-d </code><i>N</i>|<code>-v</code>|<code>-V</code>] <code>-I</code> <i>open</i> &lt;<i>open</i> | <i>sel</i>&gt; [&lt;<i>option</i>&gt;] </p>
<p> ipmievd [<code>-c</code>|<code>-h</code>|<code>-v</code>|<code>-V</code>] <code>-I</code> <i>lan</i> <code>-H</code> &lt;<i>hostname</i>&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-p</code>&nbsp;<wbr>&lt;<i>port</i>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-U</code>&nbsp;<wbr>&lt;<i>username</i>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-A</code>&nbsp;<wbr>&lt;<i>authtype</i>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-L</code>&nbsp;<wbr>&lt;<i>privlvl</i>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-a</code>|<code>-E</code>|<code>-P</code>|<code>-f</code>&nbsp;<wbr>&lt;<i>password</i>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-o</code>&nbsp;<wbr>&lt;<i>oemtype</i>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-O</code>&nbsp;<wbr>&lt;<i>sel oem</i>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr><i>sel</i>&nbsp;<wbr>[&lt;<i>option</i>&gt;] </p>
<p> ipmievd [<code>-c</code>|<code>-h</code>|<code>-v</code>|<code>-V</code>] <code>-I</code> <i>lanplus</i> <code>-H</code> &lt;<i>hostname</i>&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-p</code>&nbsp;<wbr>&lt;<i>port</i>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-U</code>&nbsp;<wbr>&lt;<i>username</i>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-L</code>&nbsp;<wbr>&lt;<i>privlvl</i>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-a</code>|<code>-E</code>|<code>-P</code>|<code>-f</code>&nbsp;<wbr>&lt;<i>password</i>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-o</code>&nbsp;<wbr>&lt;<i>oemtype</i>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-O</code>&nbsp;<wbr>&lt;<i>sel oem</i>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-C</code>&nbsp;<wbr>&lt;<i>ciphersuite</i>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr><i>sel</i>&nbsp;<wbr>[&lt;<i>option</i>&gt;]</p>
<h2>Description</h2>
<p><code>ipmievd</code> is a daemon which will listen for events from the BMC that are being sent to the SEL and also log those messages to syslog. It is able to run in one of two modes: either using the Event Message Buffer and asynchronous event notification from the OpenIPMI kernel driver or actively polling the contents of the SEL for new events. Upon receipt of an event via either mechanism it will be logged to syslog with the <i>LOG_LOCAL4</i> facility. </p>
<p> It is based on the <code>ipmitool</code> utility and shares the same IPMI interface support and session setup options. Please see the <code>ipmitool</code> manpage for more information on supported IPMI interfaces.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>Prompt for the remote server password.</p>
<dt><code>-A</code> &lt;<i>authtype</i>&gt;</p>
<dd>Specify an authentication type to use during IPMIv1.5 <i>lan</i> session activation. Supported types are NONE, PASSWORD, MD2, MD5, or OEM.</p>
<dt><code>-c</code></p>
<dd>Present output in CSV (comma separated variable) format. This is not available with all commands.</p>
<dt><code>-C</code> &lt;<i>ciphersuite</i>&gt;</p>
<dd>The remote server authentication, integrity, and encryption algorithms to use for IPMIv2 <i>lanplus</i> connections. See table 22-19 in the IPMIv2 specification. The default is 3 which specifies RAKP-HMAC-SHA1 authentication, HMAC-SHA1-96 integrity, and AES-CBC-128 encryption algorightms.</p>
<dt><code>-E</code></p>
<dd>The remote server password is specified by the environment variable <i>IPMI_PASSWORD</i>.</p>
<dt><code>-f</code> &lt;<i>password_file</i>&gt;</p>
<dd>Specifies a file containing the remote server password. If this option is absent, or if password_file is empty, the password will default to NULL.</p>
<dt><code>-h</code></p>
<dd>Get basic usage help from the command line.</p>
<dt><code>-H</code> &lt;<i>address</i>&gt;</p>
<dd>Remote server address, can be IP address or hostname. This option is required for <i>lan</i> and <i>lanplus</i> interfaces.</p>
<dt><code>-I</code> &lt;<i>interface</i>&gt;</p>
<dd>Selects IPMI interface to use. Supported interfaces that are compiled in are visible in the usage help output.</p>
<dt><code>-L</code> &lt;<i>privlvl</i>&gt;</p>
<dd>Force session privilege level. Can be CALLBACK, USER, OPERATOR, ADMIN. Default is ADMIN.</p>
<dt><code>-m</code> &lt;<i>local_address</i>&gt;</p>
<dd>Set the local IPMB address. The default is 0x20 and there should be no need to change it for normal operation.</p>
<dt><code>-o</code> &lt;<i>oemtype</i>&gt;</p>
<dd>Select OEM type to support. This usually involves minor hacks in place in the code to work around quirks in various BMCs from various manufacturers. Use <i>-o list</i> to see a list of current supported OEM types.</p>
<dt><code>-O</code> &lt;<i>sel oem</i>&gt;</p>
<dd>Open selected file and read OEM SEL event descriptions to be used during SEL listings. See examples in contrib dir for file format.</p>
<dt><code>-p</code> &lt;<i>port</i>&gt;</p>
<dd>Remote server UDP port to connect to. Default is 623.</p>
<dt><code>-P</code> &lt;<i>password</i>&gt;</p>
<dd>Remote server password is specified on the command line. If supported it will be obscured in the process list. <code>Note!</code> Specifying the password as a command line option is not recommended.</p>
<dt><code>-S</code> &lt;<i>sdr_cache_file</i>&gt;</p>
<dd>Use local file for remote SDR cache. Using a local SDR cache can drastically increase performance for commands that require knowledge of the entire SDR to perform their function.</p>
<dt><code>-t</code> &lt;<i>target_address</i>&gt;</p>
<dd>Bridge IPMI requests to the remote target address.</p>
<dt><code>-U</code> &lt;<i>username</i>&gt;</p>
<dd>Remote server username, default is NULL user.</p>
<dt><code>-d </code><i>N</i></p>
<dd>Use device number N to specify the /dev/ipmiN (or /dev/ipmi/N or /dev/ipmidev/N) device to use for in-band BMC communication. Used to target a specific BMC on a multi-node, multi-BMC system through the ipmi device driver interface. Default is 0.</p>
<dt><code>-v</code></p>
<dd>Increase verbose output level. This option may be specified multiple times to increase the level of debug output. If given three times you will get hexdumps of all incoming and outgoing packets.</p>
<dt><code>-V</code></p>
<dd>Display version information. </p>
</dl>
<p> If no password method is specified then ipmievd will prompt the user for a password. If no password is entered at the prompt, the remote server password will default to NULL.</p>
<h2>Commands</h2>
<dl>
<dt><i>help</i></p>
<dd>This can be used to get command-line help. It may also be placed at the end of commands to get option usage help. </p>
<p> &gt; ipmievd help<br />
 Commands:<br />
&nbsp;<wbr>open&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Use OpenIPMI for asyncronous notification of events<br />
&nbsp;<wbr>sel&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Poll SEL for notification of events </p>
<dt><i>open</i></p>
<dd>This command starts ipmievd with the OpenIPMI event watching mechanism which relies on the Event Message Buffer feature of IPMI. This requires a properly installed and configured OpenIPMI driver on Linux and is only valid to be run through the <i>open</i> interface. See the <code>ipmitool</code> manpage and associated documentation for more information on setting up the OpenIPMI driver. </p>
<p> <code>Note</code>: Some BMC do not support the Event Message Buffer required for this command. Other BMCs claim to support it but do not actually deliver events to it. If this is the case please use the <i>sel</i> method. </p>
<dl>
<dd>
<dl>
<dt><i>daemon</i></p>
<dd>Launch process as a daemon and reparent to init process. All messages will be sent to syslog. This is the default action.</p>
<dt><i>nodaemon</i></p>
<dd>Do NOT become a daemon, instead log all messages to stderr.</p>
<dt><i>pidfile</i>=&lt;<code>filename</code>&gt;</p>
<dd>Save process ID to this file when in daemon mode. Defaults to /var/run/ipmievd.pid<i>N</i> (where <i>N</i> is the ipmi device number &#8212; defaults to 0).</dl>
</dl>
<dt><i>sel</i></p>
<dd>This command starts ipmievd with the SEL Polling event watching mechanism. This will poll the SEL periodically to determine if new events have been logged. This command should work with all BMCs and is capable of using the LAN interface as well to monitor a remote system and log its events to a local syslog. </p>
<dl>
<dd>
<dl>
<dt><i>daemon</i></p>
<dd>Launch process as a daemon and reparent to init process. All messages will be sent to syslog. This is the default action.</p>
<dt><i>nodaemon</i></p>
<dd>Do NOT become a daemon, instead log all messages to stderr.</p>
<dt><i>pidfile</i>=&lt;<code>filename</code>&gt;</p>
<dd>Save process ID to this file when in daemon mode. Defaults to /var/run/ipmievd.pid<i>N</i> (where <i>N</i> is the ipmi device number &#8212; defaults to 0).</p>
<dt><i>timeout</i>=&lt;<code>seconds</code>&gt;</p>
<dd>Time between checks for SEL polling method. Default is 10 seconds.</dl>
</dl>
</dl>
<h2>Examples</h2>
<dl>
<dt><i>Example 1</i>: Daemon process watching OpenIPMI for events</p>
<dd>&gt; ipmievd -I open open daemon</p>
<dt><i>Example 2</i>: Local non-daemon process checking remote SEL every 30 seconds</p>
<dd>&gt; ipmievd -I lan -H 1.2.3.4 -f passfile sel nodaemon timeout=30<br />
 Reading Sensors&#8230;<br />
 Waiting for Events&#8230;
</dl>
<h2>Author</h2>
<p>Duncan Laurie &lt;duncan [at] iceblink.org&gt;</p>
<h2>See Also</h2>
<dl>
<dt>IPMItool Homepage</p>
<dd><a rel="nofollow" href="http://ipmitool.sourceforge.net">http://ipmitool.sourceforge.net</a></p>
<dt>Intelligent Platform Management Interface Specification</p>
<dd><a rel="nofollow" href="http://www.intel.com/design/servers/ipmi">http://www.intel.com/design/servers/ipmi</a></p>
<dt>OpenIPMI Homepage</p>
<dd><a rel="nofollow" href="http://openipmi.sourceforge.net">http://openipmi.sourceforge.net</a> </p>
