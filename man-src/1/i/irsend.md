---
title: "irsend(1)"
name: "irsend"
section: "1"
letter: "i"
url: "/docs/linux/man/1-irsend/"
description: "irsend – basic LIRC program to send infra-red commands"
---

<h2>NAME</h2>
<p> irsend &#8211; basic LIRC program to send infra-red commands</p>
<h2>SYNOPSIS</h2>
<p> <code>irsend</code> [<i>options</i>] <i>DIRECTIVE REMOTE CODE </i>[<i>CODE</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Asks the <code>lircd</code> daemon to send one or more CIR (Consumer Infra-Red) commands. This is intended for remote control of electronic devices such as TV boxes, HiFi sets, etc. </p>
<p> <i>DIRECTIVE</i> can be: </p>
<pre><code>
SEND_ONCE - send CODE[CODE...] once SEND_START - start repeating CODE SEND_STOP - stop repeating CODE LIST - list configured remote items SET_TRANSMITTERS - set transmitters NUM[NUM...] SIMULATE - simulate IR event
</code></pre>
<p> <i>REMOTE</i> is the name of a remote, as described in the <code>lircd</code> configuration file. </p>
<p> <i>CODE</i> is the name of a remote control key of <i>REMOTE</i>, as it appears in the <code>lircd</code> configuration file. </p>
<p> <i>NUM</i> is the transmitter number of the hardware device. </p>
<p> For the <code>LIST</code> <i>DIRECTIVE</i>, <i>REMOTE</i> and/or <i>CODE</i> can be empty: </p>
<pre>
<dl><dt><dd><code>LIST</code>   &quot;&quot;    &quot;&quot;   - list all configured remote names
<code>LIST</code> <i>REMOTE</i>  &quot;&quot;   - list all codes of <i>REMOTE</i>
<code>LIST</code> <i>REMOTE</i> <i>CODE</i>  - list only <i>CODE</i> of <i>REMOTE</i>
</dl>
</pre>
<p> The <code>SIMULATE</code> command only works if it has been explicitly enabled in lircd.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> display usage summary</p>
<dt><code>-v</code> <code>&#8211;version</code></p>
<dd> display version</p>
<dt><code>-d</code> <code>&#8211;device</code></p>
<dd> use given lircd socket [/var/run/lirc/lircd]</p>
<dt><code>-a</code> <code>&#8211;address</code>=<i>host[</i>:port]</p>
<dd> connect to lircd at this address</p>
<dt>-# <code>&#8211;count</code>=<i>n</i></p>
<dd> send command n times </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>LIRC_SOCKET_PATH</p>
<dd> The lircd socket to connect to, defaults to a hardcoded default value usually /var/run/lirc/lircd</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/lirc/lircd.conf</i></p>
<dd> Default <code>lircd</code> configuration file. It should contain all the remotes, their infra-red codes and the corresponding timing and waveform details. </p>
</dl>
<h2>DIAGNOSTICS</h2>
<p> If <code>lircd</code> is not running (or /var/run/lirc/lircd lacks write permissions) <code>irsend</code> aborts with the following diagnostics: </p>
<pre>
&quot;irsend: could not connect to socket&quot;
&quot;irsend: Connection refused&quot; (or &quot;Permission denied&quot;).
</pre>
<h2>EXAMPLES</h2>
<pre>
<dl><dt><dd>irsend LIST DenonTuner &quot;&quot;
irsend SEND_ONCE  DenonTuner PROG-SCAN
irsend SEND_ONCE  OnkyoAmpli VOL-UP VOL-UP VOL-UP VOL-UP
irsend SEND_START OnkyoAmpli VOL-DOWN ; sleep 3
irsend SEND_STOP  OnkyoAmpli VOL-DOWN
irsend SET_TRANSMITTERS 1
irsend SET_TRANSMITTERS 1 3 4
irsend SIMULATE &quot;0000000000000476 00 OK TECHNISAT_ST3004S&quot;
</dl>
</pre>
<h2>DRIVER LOADING</h2>
<p> Drivers are loaded dynamically. The directory used for this is determined by (falling priority):</p>
<dl>
<dt>&#8211;</p>
<dd> The &#8216;plugindir&#8217; entry in the [lircd] section of the lirc_options.conf file.</p>
<dt>&#8211;</p>
<dd> The environment variable LIRC_PLUGINDIR.</p>
<dt>&#8211;</p>
<dd> A hardcoded default (usually /usr/lib[64]/lirc/plugins).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-lircd/">lircd</a>(8), <a href="/docs/linux/man/1-mode2/">mode2</a>(1), <a href="/docs/linux/man/1-xmode2/">xmode2</a>(1), <a href="/docs/linux/man/1-irrecord/">irrecord</a>(1), <a href="/docs/linux/man/1-irw/">irw</a>(1)</code> </p>
<h2>Index</h2>
