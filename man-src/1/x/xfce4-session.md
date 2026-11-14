---
title: "xfce4-session(1)"
name: "xfce4-session"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xfce4-session/"
description: "xfce4-session – Starts up the Xfce Desktop Environment"
---

<h2 class="name">NAME</h2>
<p> xfce4-session &#8211; Starts up the Xfce Desktop Environment </p>
<h2>SYNOPSIS</h2>
<p> <code>xfce4-session</code> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>xfce4-session</code> command. </p>
<p> The <code>xfce4-session</code> program starts up the Xfce Desktop Environment and is typically executed by your login manager (e.g. xdm, gdm, kdm, wdm or from your X startup scripts). It will load your last session or a default session that includes the standard Xfce programs if no saved session is available. </p>
<p> <code>xfce4-session</code> is an standard X11R6 session manager that can manage any X11R6 SM compliant program, including GNOME and KDE programs. </p>
<p> <code>xfce4-session</code> uses the contents of the ~/.cache/sessions/ directory for starting previously saved sessions. </p>
<h2>OPTIONS</h2>
<p> <code>xfce4-session</code> takes the following command line options:</p>
<dl>
<dt><code>&#8211;disable-tcp</code></p>
<dd> Disable binding to TCP ports in the ICE layer. This is not possible on every platform. If you use this option on a platform that does not support it, <code>xfce4-session</code> will print a warning message and ignore the setting.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a help screen and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> <code>xfce4-session</code>&#8216;s behaviour is affected by the following environment variables. </p>
<dl>
<dt><code>XDG_CONFIG_HOME</code></p>
<dd> Specifies the root for all user-specific configuration files. If this environment variable is unset, it defaults to <i>~/.config/</i></p>
<dt><code>XDG_CONFIG_DIRS</code></p>
<dd> Set of preference ordered base directories relative to which configuration files should be searched in addition to the <code>$XDG_CONFIG_HOME</code> base directory. The directories should be separated with a colon.</p>
<dt><code>XDG_CACHE_HOME</code></p>
<dd> Specifies the root for all user-specific cache data. If this environment variable is unset, it defaults to <i>~/.cache/</i></p>
<dt><code>XFSM_VERBOSE</code></p>
<dd> When defined, this environment variable enables debugging messages to be saved to <i>~/.xfce4-session.verbose-log</i> The log file from the last session run with this environment variable set is retained at <i>~/.xfce4-session.verbose-log.last</i> These debugging messages are useful for troubleshooting and development. </p>
</dl>
<h2>FILES</h2>
<p> <code>xfce4-session</code> reads its configuration from Xfconf. <code>xfce4-session</code> stores its session data into <i>$XDG_CACHE_HOME/sessions/</i>. </p>
<h2>AUTHOR</h2>
<p> <code>xfce4-session</code> was written by Benedikt Meurer &lt;benny [at] xfce.org&gt; as part of the Xfce project. This manual page was written by Oliver M. Bolzer &lt;oliver [at] debian.org&gt; and Benedikt Meurer &lt;benny [at] xfce.org&gt;. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="http://bugzilla.xfce.org/.">http://bugzilla.xfce.org/.</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003-2014 Benedikt Meurer. </p>
<h2>Index</h2>
