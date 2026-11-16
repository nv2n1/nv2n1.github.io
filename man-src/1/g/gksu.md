---
title: "gksu(1)"
name: "gksu"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gksu/"
description: "gksu – GTK+ frontend for su and sudo"
---

<h2 class="name">NAME</h2>
<p> gksu &#8211; GTK+ frontend for su and sudo </p>
<h2>SYNOPSIS</h2>
<p> <code>gksu</code> </p>
<p> <code>gksu</code> [<i>-u &lt;user&gt;</i>] [<i>options</i>] <i>&lt;command&gt;</i> </p>
<p> <code>gksudo</code> [<i>-u &lt;user&gt;</i>] [<i>options</i>] <i>&lt;command&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly <code>gksu</code> and <code>gksudo</code> </p>
<p> gksu is a frontend to su and gksudo is a frontend to sudo. Their primary purpose is to run graphical commands that need root without the need to run an X terminal emulator and using su directly. </p>
<p> Notice that all the magic is done by the underlying library, libgksu. Also notice that the library will decide if it should use su or sudo as backend using the <code>/apps/gksu/sudo-mode</code> gconf key, if you call the <code>gksu</code> command. You can force the backend by using the <code>gksudo</code> command, or by using the <code>&#8211;sudo-mode</code> and <code>&#8211;su-mode</code> options. </p>
<p> If no command is given, the <code>gksu</code> program will display a small window that allows you to type in a command to be run, and to select what user the program should be run as. The other options are disregarded, right now, in this mode.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;debug</code>, <code>-d</code></p>
<dl>
<dt>
</dt><dd> Print information on the screen that might be useful for diagnosing and/or solving problems.</dd>
<dt> <code>&#8211;user</code> &lt;user&gt;, <code>-u</code> &lt;user&gt;</dt>
<dd>Call &lt;command&gt; as the specified user.</dd>
<dt> <code>&#8211;disable-grab</code>, <code>-g</code></dt>
<dd>Disable the &quot;locking&quot; of the keyboard, mouse, and focus done by the program when asking for password.</dd>
<dt> <code>&#8211;prompt</code>, <code>-P</code></dt>
<dd>Ask the user if they want to have their keyboard and mouse grabbed before doing so.</dd>
<dt> <code>&#8211;preserve-env</code>, <code>-k</code></dt>
<dd>Preserve the current environments, does not set $HOME nor $PATH, for example.</dd>
<dt> <code>&#8211;login</code>, <code>-l</code></dt>
<dd>Make this a login shell. Beware this may cause problems with the Xauthority magic. Run xhost to allow the target user to open windows on your display!</dd>
<dt> <code>&#8211;description</code> &lt;description|file&gt;, <code>-D</code> &lt;description|file&gt;</dt>
<dd>Provide a descriptive name for the command to be used in the default message, making it nicer. You can also provide the absolute path for a .desktop file. The Name key for will be used in this case.</dd>
<dt> <code>&#8211;message</code> &lt;message&gt;, <code>-m</code> &lt;message&gt;</dt>
<dd>Replace the standard message shown to ask for password for the argument passed to the option. Only use this if <code>&#8211;description</code> does not suffice.</dd>
<dt> <code>&#8211;print-pass</code>, <code>-p</code></dt>
<dd>Ask gksu to print the password to stdout, just like ssh-askpass. Useful to use in scripts with programs that accept receiving the password on stdin.</dd></dl>
<dl>
<dt> <code>&#8211;su-mode</code>, <code>-w</code></dt>
<dd>Force gksu to use <a href="/docs/linux/man/1-su/">su</a>(1) as its backend for running the programs.</dd>
<dt> <code>&#8211;sudo-mode</code>, <code>-S</code></dt>
<dd>Force gksu to use <a href="/docs/linux/man/1-sudo/">sudo</a>(1) as its backend for running the programs.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-su/">su</a></code>(1), <code><a href="/docs/linux/man/1-sudo/">sudo</a></code>(1) </p>
<h2>Index</h2>
