---
title: "irssi(1)"
name: "irssi"
section: "1"
letter: "i"
url: "/docs/linux/man/1-irssi/"
description: "Irssi – a modular IRC client for UNIX"
---

<h2>NAME</h2>
<p> Irssi &#8211; a modular IRC client for UNIX</p>
<h2>SYNOPSIS</h2>
<p> <code>irssi</code> [-dv!?] [-c server] [-p port] [-n nickname] [-w password] [-h hostname]</p>
<h2>DESCRIPTION</h2>
<p> <code>Irssi</code> is a modular Internet Relay Chat client. It is highly extensible and very secure. Being a fullscreen, termcap based client with many features, <code>Irssi</code> is easily extensible through scripts and modules.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;config=FILE</code></p>
<dd> use <i>FILE</i> instead of ~/.irssi/config.</p>
<dt><code>&#8211;home=PATH</code></p>
<dd> <i>PATH </i> specifies the home directory of Irssi. Default is <code>~/.irssi</code></p>
<dt><code>-c, &#8211;connect=SERVER</code></p>
<dd> connects to <i>SERVER</i></p>
<dt><code>-w, &#8211;password=PASSWORD</code></p>
<dd> use <i>PASSWORD </i> for authentication.</p>
<dt><code>-p, &#8211;port=PORT</code></p>
<dd> automatically connect to <i>PORT </i> on server.</p>
<dt><code>-!, &#8211;noconnect</code></p>
<dd> disables autoconnecting.</p>
<dt><code>-n, &#8211;nick=NICKNAME</code></p>
<dd> specify <i>NICKNAME </i> as your nick.</p>
<dt><code>-h, &#8211;hostname=HOSTNAME</code></p>
<dd> use <i>HOSTNAME</i> for your irc session.</p>
<dt><code>-d, &#8211;dummy</code></p>
<dd> use dummy terminal mode.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> display the version of Irssi.</p>
<dt><code>-?, &#8211;help</code></p>
<dd> show a help message.</dl>
<h2>SEE ALSO</h2>
<p> <code>Irssi</code> has been supplied with a huge amount of documentation. Check /help or look at the files contained by /usr/share/doc/irssi*</p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/irssi.conf</i></p>
<dd> Global configuration file</p>
<dt><i>~/.irssi/config</i></p>
<dd> Personal configuration file</p>
<dt><i>~/.irssi/config.autosave</i></p>
<dd> Automatic save of the personal config file when it was changed externally</p>
<dt><i>~/.irssi/default.theme</i></p>
<dd> Default irssi theme</p>
<dt><i>~/.irssi/away.log</i></p>
<dd> Logged messages in away status</p>
<dt><i>/usr/share/irssi/help/</i></p>
<dd> Directory including many help files</p>
<dt><i>/usr/share/irssi/scripts/</i></p>
<dd> Global scripts directory</p>
<dt><i>/usr/share/irssi/themes/</i></p>
<dd> Global themes directory</p>
<dt><i>~/.irssi/scripts/</i></p>
<dd> Default scripts directory</p>
<dt><i>~/.irssi/scripts/autorun/</i></p>
<dd> Directory containing links to scripts that should be loaded automatically on startup</p>
<dt><i>~/.irssi/startup</i></p>
<dd> File containing a list of commands to execute on startup</dl>
<h2>AUTHORS/CREDITS</h2>
<p> <code>Irssi</code> was written by Timo Sirainen <code>&lt;cras [at] irssi.org&gt;</code> </p>
<p> This manpage was written by Istvan Sebestyen <code>&lt;stevee [at] alphanet.ch&gt;</code> and Stefan Tomanek <code>&lt;stefan [at] pico.ruhr.de&gt;</code> </p>
<h2>Index</h2>
