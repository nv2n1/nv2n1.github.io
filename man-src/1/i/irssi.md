---

title: "irssi(1)"
name: "irssi"
section: "1"
letter: "i"
url: "/docs/linux/man/1-irssi/"
description: "Irssi – a modular IRC client for UNIX"
---

<p> Irssi &#8211; a modular IRC client for UNIX</p>
<h2>SYNOPSIS</h2>
<p> <code>irssi</code> [-dv!?] [-c server] [-p port] [-n nickname] [-w password] [-h hostname]</p>
<h2>DESCRIPTION</h2>
<p> <code>Irssi</code> is a modular Internet Relay Chat client. It is highly extensible and very secure. Being a fullscreen, termcap based client with many features, <code>Irssi</code> is easily extensible through scripts and modules.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;config=FILE</code></dt>
<dd> use <i>FILE</i> instead of ~/.irssi/config.</dd>
<dt><code>&#8211;home=PATH</code></dt>
<dd> <i>PATH </i> specifies the home directory of Irssi. Default is <code>~/.irssi</code></dd>
<dt><code>-c, &#8211;connect=SERVER</code></dt>
<dd> connects to <i>SERVER</i></dd>
<dt><code>-w, &#8211;password=PASSWORD</code></dt>
<dd> use <i>PASSWORD </i> for authentication.</dd>
<dt><code>-p, &#8211;port=PORT</code></dt>
<dd> automatically connect to <i>PORT </i> on server.</dd>
<dt><code>-!, &#8211;noconnect</code></dt>
<dd> disables autoconnecting.</dd>
<dt><code>-n, &#8211;nick=NICKNAME</code></dt>
<dd> specify <i>NICKNAME </i> as your nick.</dd>
<dt><code>-h, &#8211;hostname=HOSTNAME</code></dt>
<dd> use <i>HOSTNAME</i> for your irc session.</dd>
<dt><code>-d, &#8211;dummy</code></dt>
<dd> use dummy terminal mode.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> display the version of Irssi.</dd>
<dt><code>-?, &#8211;help</code></dt>
<dd> show a help message.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>Irssi</code> has been supplied with a huge amount of documentation. Check /help or look at the files contained by /usr/share/doc/irssi*</p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/irssi.conf</i></dt>
<dd> Global configuration file</dd>
<dt><i>~/.irssi/config</i></dt>
<dd> Personal configuration file</dd>
<dt><i>~/.irssi/config.autosave</i></dt>
<dd> Automatic save of the personal config file when it was changed externally</dd>
<dt><i>~/.irssi/default.theme</i></dt>
<dd> Default irssi theme</dd>
<dt><i>~/.irssi/away.log</i></dt>
<dd> Logged messages in away status</dd>
<dt><i>/usr/share/irssi/help/</i></dt>
<dd> Directory including many help files</dd>
<dt><i>/usr/share/irssi/scripts/</i></dt>
<dd> Global scripts directory</dd>
<dt><i>/usr/share/irssi/themes/</i></dt>
<dd> Global themes directory</dd>
<dt><i>~/.irssi/scripts/</i></dt>
<dd> Default scripts directory</dd>
<dt><i>~/.irssi/scripts/autorun/</i></dt>
<dd> Directory containing links to scripts that should be loaded automatically on startup</dd>
<dt><i>~/.irssi/startup</i></dt>
<dd> File containing a list of commands to execute on startup</dd></dl>
<h2>AUTHORS/CREDITS</h2>
<p> <code>Irssi</code> was written by Timo Sirainen <code>&lt;cras [at] irssi.org&gt;</code> </p>
<p> This manpage was written by Istvan Sebestyen <code>&lt;stevee [at] alphanet.ch&gt;</code> and Stefan Tomanek <code>&lt;stefan [at] pico.ruhr.de&gt;</code> </p>
