---
title: "kdesu(1)"
name: "kdesu"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kdesu/"
description: "kdesu – Runs a program with elevated privileges"
---

<h2 class="name">NAME</h2>
<p> kdesu &#8211; Runs a program with elevated privileges </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>kdesu</code> [<code>-c</code><i> command</i>] [<code>-d</code>] [<code>-f</code><i> file</i>] [<code>-i</code><i> icon name</i>] [<code>-n</code>] [<code>-p</code><i> priority</i>] [<code>-r</code>] [<code>-s</code>] [<code>-t</code>] [<code>-u</code><i> user</i>] [<code>&#8211;noignorebutton</code>] [<code>&#8211;attach</code><i> winid</i>]</p>
<dt> <code>kdesu</code> [KDE Generic Options] [Qt Generic Options]</dl>
<h2>DESCRIPTION</h2>
<dd>KDE su is a graphical front end for the UNIX&#174;<code>su</code> command for the K Desktop Environment. It allows you to run a program as different user by supplying the password for that user. KDE su is an unprivileged program; it uses the system&#8217;s <code>su</code>. </p>
<p> KDE su has one additional feature: it can optionally remember passwords for you. If you are using this feature, you only need to enter the password once for each command. </p>
<p> This program is meant to be started from the command line or from .desktop files. </p>
<p> Since <code>kdesu</code> is no longer installed in <code> $(kde4-config &#8211;prefix)</code>/bin but in <code>kde4-config &#8211;path libexec</code> and therefore not in your <code>Path</code>, you have to use <code>$(kde4-config &#8211;path libexec)</code><code>kdesu</code> to launch <code>kdesu</code>.</p>
<h2>OPTIONS</h2>
<p> <code>-c </code><i>command</i></p>
<dl>
<dt>
<dd> This specifies the command to run as root. It has to be passed in one argument. So if, for example, you want to start a new file manager, you would enter at the prompt: <code>$(kde4-config &#8211;path libexec)</code><code>kdesu </code><code>-c </code><i> </i><i>Dolphin</i></dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Show debug information.</dl>
<p> <code>-f </code><i>file</i></p>
<dl>
<dt>
<dd> This option allow efficient use of KDE su in .desktop files. It tells KDE su to examine the file specified by <i>file</i>. If this file is writable by the current user, KDE su will execute the command as the current user. If it is not writable, the command is executed as user <i>user</i> (defaults to root). </p>
<p> <i>file</i> is evaluated like this: if <i>file</i> starts with a /, it is taken as an absolute filename. Otherwise, it is taken as the name of a global KDE configuration file.</dl>
<p> <code>-i</code> <i>icon name</i></p>
<dl>
<dt>
<dd> Specify icon to use in the password dialog. You may specify just the name, without any extension.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> Do not keep the password. This disables the keep password checkbox in the password dialog.</dl>
<p> <code>-p</code> <i>priority</i></p>
<dl>
<dt>
<dd> Set priority value. The priority is an arbitrary number between 0 and 100, where 100 means highest priority, and 0 means lowest. The default is 50.</dl>
<p> <code>-r</code></p>
<dl>
<dt>
<dd> Use realtime scheduling.</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Stop the kdesu daemon. This is the daemon that caches successful passwords in the background. This feature may also be disabled with <code>-n</code> when KDE su is initially run.</dl>
<p> <code>-t</code></p>
<dl>
<dt>
<dd> Enable terminal output. This disables password keeping. This is largely for debugging purposes; if you want to run a console mode app, use the standard <code>su</code> instead.</dl>
<p> <code>-u</code> <i> user</i></p>
<dl>
<dt>
<dd> While the most common use for KDE su is to run a command as the superuser, you can supply any user name and the appropriate password.</dl>
<p> <code>&#8211;noignorebutton</code></p>
<dl>
<dt>
<dd> Do not display an ignore button.</dl>
<p> <code>&#8211;attach</code> <i> winid</i></p>
<dl>
<dt>
<dd> Makes the dialog transient for an X app specified by winid.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-su/">su</a>(1) </p>
<p> More detailed user documentation is available from m[blue]<code>help:/kdesu</code>m[] (either enter this URL into Konqueror, or run <code>khelpcenter</code><i>help:/kdesu</i>).</p>
<h2>EXAMPLES</h2>
<p> Run <code>kfmclient</code> as user jim, and show the Konqueror icon in the password dialog: </p>
<dl>
<dt>
<dd>
<pre>
<code>$(kde4-config --path libexec)</code><code>kdesu</code><code>-u jim</code><code>-i konqueror</code><code>kfmclient</code>
</pre>
</dl>
<h2>AUTHORS</h2>
<p> KDE su was written by Geert Jansen&lt;jansen [at] kde.org&gt; and Pietro Iglio&lt;iglio [at] fub.it&gt;.</p>
<h2>AUTHOR</h2>
<p> <code>Lauri Watts</code> &lt;lauri [at] kde.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
