---
title: "card_eventmgr(1)"
name: "card_eventmgr"
section: "1"
letter: "c"
url: "/docs/linux/man/1-card_eventmgr/"
description: "card_eventmgr – PCSC-Lite Event Manager"
---

<h2>NAME</h2>
<p> card_eventmgr &#8211; PCSC-Lite Event Manager</p>
<h2>SYNTAX</h2>
<p> <code>card_eventmgr</code> [<code>debug</code>] [[<code>no</code>]<code>daemon</code>] [<code>timeout=</code><i>&lt;msecs&gt;</i>] [<code>config_file=</code><i>&lt;filename&gt;</i>] [<code>kill</code>] [<code>pidfile=</code><i>&lt;pidfile&gt;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>card_eventmgr</code> is a smart card monitoring tool that listen to the status of the card reader and dispatch actions on several events. <code>card_eventmgr</code> can be used for several actions: like screen lock on card removal. </p>
<p> Three events are supported: card insertion, card removal and timeout on removed card. Actions are specified in a configuration file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>debug</code></p>
<dd> Enable debugging output.</p>
<dt>[<code>no</code>]<code>daemon</code></p>
<dd> Runs in background if daemon or in foreground if nodaemon (default). If debug is unset, the program dettaches itself from the tty.</p>
<dt><code>timeout=</code><i>&lt;msecs&gt;</i></p>
<dd> Set polling timeout in milliseconds. Defaults to 1000 (1 second).</p>
<dt><code>config_file=</code><i>&lt;configuration file&gt;</i></p>
<dd> Sets de configuration file. Default value is <i>/etc/pam_pkcs11/card_eventmgr.conf</i>.</p>
<dt><code>pidfile=</code><i>&lt;pidfile&gt;</i></p>
<dd> Store the <code>card_eventmgr</code> process ID (pid) in the file <i>pidfile</i>.</p>
<dt><code>kill</code></p>
<dd> Read a process id from <i>pidfile</i> and kill that process. You must use the argument <code>pidfile=</code><i>&lt;pidfile&gt;</i> to use <code>kill</code>.</dl>
<h2>FILES</h2>
<p> <i>/etc/pam_pkcs11/card_eventmgr.conf</i></p>
<h2>EXAMPLES</h2>
<p> To run this program the standard way type: </p>
<p>&nbsp;<wbr>card_eventmgr&nbsp;<wbr> </p>
<p> Alternatively you can specify options: </p>
<p>&nbsp;<wbr>card_eventmgr debug nodaemon timeout=500 config_file=$HOME/.card_eventmgr.conf </p>
<p> If you want to start and stop card_eventmgr automatically in an X11 session you can create a <i>~/.xsession</i> file containing:<br />
&nbsp;<wbr>#&nbsp;<wbr>start the card autolock<br />
&nbsp;<wbr>card_eventmgr pidfile=$HOME/.card_eventmgr.pid </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>start Gnome or something else<br />
&nbsp;<wbr>/usr/bin/x-session-manager </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>kill the card autolock<br />
&nbsp;<wbr>card_eventmgr kill pidfile=$HOME/.card_eventmgr.pid</p>
<h2>BUGS</h2>
<p> Some applications like <code>xscreensaver-command</code> may fail due to external events (eg: try to unlock an unlocked session). In this case, the command incorrectly returns error code.</p>
<h2>AUTHORS</h2>
<p> Juan Antonio Martinez &lt;jonsito [at] teleline.es&gt;<br />
 Ludovic Rousseau &lt;ludovic.rousseau [at] free.fr&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-pam_pkcs11/">pam_pkcs11</a></code>(8), <code><a href="/docs/linux/man/1-pkcs11_eventmgr/">pkcs11_eventmgr</a></code>(1), README.eventmgr, PAM-PKCS11 User Manual </p>
<h2>Index</h2>
