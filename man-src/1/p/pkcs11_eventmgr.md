---
title: "pkcs11_eventmgr(1)"
name: "pkcs11_eventmgr"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkcs11_eventmgr/"
description: "pkcs11_eventmgr – SmartCard PKCS#11 Event Manager"
---

<h2>NAME</h2>
<p> pkcs11_eventmgr &#8211; SmartCard PKCS#11 Event Manager</p>
<h2>SYNTAX</h2>
<p> pkcs11_eventmgr [<i>[no]debug</i>] [<i>[no]daemon</i>] [<i>polling_time=&lt;secs&gt;</i> ] [<i>expire_time=&lt;secs&gt;</i>] [<i>pkcs11_module=&lt;module&gt;</i> ] [<i>config_file=&lt;filename&gt;</i>]</p>
<h2>DESCRIPTION</h2>
<p> card_eventmgr is a SmartCard Monitoring that listen to the status of the card reader and dispatch actions on several events. card_eventmgr can be used to several actions, like lock screen on card removal<br />
 Three events are supported: card insert, card removal and timeout on removed card. Actions to take are specified in the configuration file</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>[no]debug</code></p>
<dd> Enable debugging output. Default is no debug</p>
<dt><code>[no]daemon</code></p>
<dd> Runs in background. If debug is unset, dettach also from tty. Default: no daemon</p>
<dt><code>polling_time=&lt;secs&gt;</code></p>
<dd> Set polling timeout in secs. Defaults to 1 sec</p>
<dt><code>expire_time=&lt;secs&gt;</code></p>
<dd> Set timeout on card removed. Defaults to 0 (never)</p>
<dt><code>config_file=&lt;configuration file&gt;</code></p>
<dd> Sets de configuration file. Defaults to /etc/pam_pkcs11/card_eventmgr.conf</p>
<dt><code>pkcs11_module=&lt;pkcs11.so library&gt;</code></p>
<dd> Sets the pkcs#11 library module to use. Defaults to /usr/lib/pkcs11/opensc-pkcs11.so</dl>
<h2>FILES</h2>
<p> <i>/etc/pam_pkcs11/card_eventmgr.conf</i> </p>
<p> <i>/usr/lib/pkcs11/opensc-pkcs11.so</i></p>
<h2>EXAMPLES</h2>
<p> To run this program the standard way type: </p>
<p> pkcs11_eventmgr </p>
<p> Alternativly you can specify options: </p>
<p> pkcs11_eventmgr nodebug nodaemon polling_time=5 config_file=${HOME}/.pkcs11_eventmgr.conf</p>
<h2>BUGS</h2>
<p> Some PKCS#11 Libraries fails on card removal and re-insert. to avoid this, pkcs11_eventmgr try to re-initialize stuff by calling C_Finalize() and C_Initialize() on card removal<br />
 Some apps like [<i>xscreensaver-command</i>] may fail due to external events ( eg: try to unlock an unlocked session ). In this case, command incorrectly returns error code.<br />
 User shoult take care on this circumstance</p>
<h2>AUTHORS</h2>
<p> Juan Antonio Martinez &lt;jonsito [at] teleline.es&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-pam_pkcs11/">pam_pkcs11</a>(8), <a href="/docs/linux/man/5-card_eventmgr/">card_eventmgr</a>(5)<br />
 README.eventmgr<br />
 PAM-PKCS11 User Manual </p>
<h2>Index</h2>
