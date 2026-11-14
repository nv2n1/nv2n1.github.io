---
title: "incrontab(1)"
name: "incrontab"
section: "1"
letter: "i"
url: "/docs/linux/man/1-incrontab/"
description: "incrontab – table manipulator for inotify cron (incron)"
---

<h2>NAME</h2>
<p> incrontab &#8211; table manipulator for inotify cron (incron)</p>
<h2>SYNOPSIS</h2>
<p> <code>incrontab</code> [<code>-u</code> <i>user</i>] [<code>-f</code> <i>config</i>] <i>file</i> </p>
<p> <code>incrontab</code> [<code>-u</code> <i>user</i>] [<code>-f</code> <i>config</i>] [<code>-l</code> | <code>-r</code> | <code>-e</code> | <code>-t</code> | <code>-d</code>]</p>
<h2>DESCRIPTION</h2>
<p> incrontab is a table manipulator for the inotify cron (incron) system. It creates, removes, modifies and lists user tables (<i><a href="/docs/linux/man/5-incrontab/">incrontab</a></i>(5)). </p>
<p> Each user (including system users even they haven&#8217;t home directories) has an incron table which can&#8217;t be manipulated directly (only root can effectively change these tables and is NOT recommended to do so). </p>
<p> All informational messages of this program are printed to the standard error output (stderr). </p>
<p> If <i>/etc/incron.allow</i> exists only users listed here may use incron. Otherwise if <i>/etc/incron.deny</i> exists only users NOT listed here may use incron. If none of these files exists everyone is allowed to use incron. (<code>Important note:</code> This behavior is insecure and will be probably changed to be compatible with the style used by ISC Cron.) Location of these files can be changed in the configuration. </p>
<p> The first form of this command imports a file, validates it and stores to the table. &quot;-&quot; can be used for loading from the standard input. </p>
<p> <code>-u</code> (or <code>&#8211;user</code>) option overrides the current (real) user to the given one. This option is intended for manipulation with system users&#8217; tables (such as apache, postfix, daemon etc.). It can be used only if the current user has root&#8217;s effective rights. </p>
<p> <code>-l</code> (or <code>&#8211;list</code>) option causes the current table is printed to the standard output. </p>
<p> <code>-r</code> (or <code>&#8211;remove</code>) option causes the current table (if any) is permanently remove without any warning or confirmation. Use with caution! </p>
<p> <code>-e</code> (or <code>&#8211;edit</code>) option causes executing an editor for editing the user table (see below for the information about editor selection). You can edit your incron table now. If the table is changed it stores the modified version. </p>
<p> <code>-t</code> (or <code>&#8211;types</code>) option causes the list of supported event types (delimited by commas) is printed to the standard output. This feature is intended for front-end applications to find out which event types was compiled in. </p>
<p> <code>-d</code> (or <code>&#8211;reload</code>) option causes reloading the current table by <i><a href="/docs/linux/man/8-incrond/">incrond</a></i>(8). It is done through &quot;touching&quot; the table (writing into it without modifying it). This feature is intended e.g. for creating watches on newly created files (with already existing rules) or for rearming IN_ONESHOT watches. </p>
<p> <code>-f &lt;FILE&gt;</code> (or <code>&#8211;config=&lt;FILE&gt;</code>) option specifies another location for the configuration file (/etc/incron.conf is used by default). This feature requires root privileges. </p>
<p> There is a few complex algorithm how to determine which editor will be user for editing. If any of the following rule succeeds the appropriate editor is used: </p>
<p> 1. EDITOR environment variable </p>
<p> 2. VISUAL environment variable </p>
<p> 3. configuration value </p>
<p> 4. etc/alternatives/editor </p>
<p> 5. hard-wired editor (<i>vim</i> by default) </p>
<p> It&#8217;s not recommended to use graphical editors (such as gVim, KEdit etc.) due to possible problems with connecting to the X server.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-incrond/">incrond</a>(8), <a href="/docs/linux/man/5-incrontab/">incrontab</a>(5), <a href="/docs/linux/man/5-incron-conf/">incron.conf</a>(5)</p>
<h2>AUTHOR</h2>
<p> Lukas Jelinek &lt;lukas [at] aiken.cz&gt; (please report bugs to <a rel="nofollow" href="http://bts.aiken.cz">http://bts.aiken.cz</a> or &lt;bugs [at] aiken.cz&gt;).</p>
<h2>COPYING</h2>
<p> This program is free software. It can be used, redistributed and/or modified under the terms of the GNU General Public License, version 2. </p>
<h2>Index</h2>
