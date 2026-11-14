---
title: "xsession-options-d(5)"
name: "xsession-options-d"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xsession-options-d/"
description: "Xsession.options, Xsession.options.d – configuration options for"
---

<p>Xsession.options, Xsession.options.d &#8211; configuration options for <code></p>
<p> <a href="/docs/linux/man/5-xsession/">Xsession</a></code>(5)</p>
<h2>Description</h2>
<p><i>/etc/X11/Xsession.options</i> and <i>/etc/X11/Xsession.options.d/*.conf</i> contain options that determine some of the behavior of the <code><a href="/docs/linux/man/5-xsession/">Xsession</a></code>(5) Bourne shell (<code><a href="/docs/linux/man/1-sh/">sh</a></code>(1)) script. See the <code><a href="/docs/linux/man/5-xsession/">Xsession</a></code>(5) manpage for further information. </p>
<p> These configuration files may contain comments, which begin with a hash mark (&#8216;#&#8217;) and end at the next newline, just like comments in shell scripts. The rest of the file consists of options which are expressed as words separated by hyphens, with only one option per line. Options are enabled by simply placing them in the file; they are disabled by prefixing the option name with &#8216;no-&#8216;. </p>
<p> Options are read from <i>/etc/X11/Xsession.options</i>, followed by <i>/etc/X11/Xsession.options.d/*.conf</i> in sorted order; later occurrences of an option (with or without the &#8216;no-&#8216; prefix) take precedence over earlier occurrences. </p>
<p> Available options are:</p>
<dl>
<dt><code>allow-failsafe</code></p>
<dd>If the &#8216;failsafe&#8217; argument is passed to the <i>Xsession</i> script, an emergency X session is invoked, consisting of only an <code><a href="/docs/linux/man/1-x-terminal-emulator/">x-terminal-emulator</a></code>(1) in the upper-left hand corner of the screen. No window manager is started. If an <code>x-terminal-emulator</code> program is not available, the session exits immediately.</p>
<dt><code>allow-user-resources</code></p>
<dd>If users have a file called <i>.Xresources</i> in their home directories, these resources will be merged with the default X resources when they log in.</p>
<dt><code>allow-user-xsession</code></p>
<dd>If users have an executable file called <i>.xsession</i> in their home directories, it can be used as the startup program for the X session (see <code><a href="/docs/linux/man/5-xsession/">Xsession</a></code>(5)). If the file is present but not executable, it may still be used, but is assumed to be a Bourne shell script, and executed with <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1).</p>
<dt><code>use-session-dbus</code></p>
<dd>If the <code>dbus</code> package is installed, the session bus will be activated at X session launch.</p>
<dt><code>use-ssh-agent</code></p>
<dd>If the <code><a href="/docs/linux/man/1-ssh-agent/">ssh-agent</a></code>(1) program is available and no agent process appears to be running already, the X session will be invoked by exec&#8217;ing <code>ssh-agent</code> with the startup command, instead of the startup command directly.</dl>
<p> All of the above options are enabled by default. Additional options may be supported by the local administrator. <code><a href="/docs/linux/man/5-xsession/">Xsession</a></code>(5) describes how this is accomplished.</p>
<h2>Authors</h2>
<p>Stephen Early, Mark Eichin, and Branden Robinson developed Debian&#8217;s X session handling scripts. Branden Robinson wrote this manual page.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-xsession/">Xsession</a></code>(5), <code><a href="/docs/linux/man/1-ssh-agent/">ssh-agent</a></code>(1), <code><a href="/docs/linux/man/1-x-terminal-emulator/">x-terminal-emulator</a></code>(1) </p>
