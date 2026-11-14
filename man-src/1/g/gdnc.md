---
title: "gdnc(1)"
name: "gdnc"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdnc/"
description: "gdnc – GNUstep Distributed Notification Center"
---

<h2>NAME</h2>
<p> gdnc &#8211; GNUstep Distributed Notification Center</p>
<h2>SYNOPSIS</h2>
<p> <code>gdnc</code> </p>
<h2>DESCRIPTION</h2>
<p> The gdnc daemon is used by GNUstep programs to send notifications and messages to one another. By default it uses private inter-process communications accessible only to the curtrent user on the machine on which it is running (where the operating system supports them). </p>
<p> Every user needs to have his own instance of <code>gdnc</code> running. While <code>gdnc</code> will be started automatically as soon as it is needed, it is recommended to start <code>gdnc</code> in a personal login script like ~/.bashrc or ~/.cshrc. Alternatively (if you have no command-line tools which use distributed notifications) you can launch gdnc when your windowing system or the window manager is started. For example, on systems with X11 you can launch <code>gdnc</code> from your .xinitrc script or alternatively &#8211; if you are running Window Maker &#8211; put it in Window Maker&#8217;s autostart script. See the <i>GNUstep Build Guide</i> for a sample startup script. </p>
<h2>OPTIONS</h2>
<p> To attach <code>gdnc</code> to a remote session use the</p>
<dl>
<dt><code>-NSHost </code><i>hostname</p>
<dd> argument.</dl>
<p> To run a copy of the server to handle public notifications (available to all users on the local machine)</p>
<dl>
<dt></i><code>-GSPublic YES</p>
<dd></dl>
<p> To run a copy of the server to handle network-public notifications (available to all users able to connect to the local machine on the network)</p>
<dl>
<dt>-GSNetwork YES</p>
<dd></dl>
<p> </code></p>
<h2>DIAGNOSTICS</h2>
<p> <code>gdomap -L GDNCServer</code> will lookup instances of gdnc which were launched with the NSHost, GSPublic, or GSNetwork command line arguments. </p>
<p> Alternatively, <code>gdomap -N</code> will list all registered names on the local host. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-gdomap/">gdomap</a>(8), <a href="/docs/linux/man/7-gnustep/">GNUstep</a>(7), <a href="/docs/linux/man/1-gpbs/">gpbs</a>(1) </p>
<p> <i>The GNUstep Build Guide</i> example startup script: &lt;<a rel="nofollow" href="http://gnustep.made-it.com/BuildGuide/index.html#GNUSTEP.SERVICES">http://gnustep.made-it.com/BuildGuide/index.html#GNUSTEP.SERVICES</a>&gt; </p>
<h2>HISTORY</h2>
<p> Work on <code>gdnc</code> started October 1998. </p>
<p> This manual page first appeared in gnustep-base 1.7.2 (July 2003). </p>
<h2>AUTHORS</h2>
<p> <code>gdnc </code> was written by Richard Frith-Macdonald &lt;rfm [at] gnu.org&gt;. </p>
<p> This man page was written by Martin Brecher &lt;martin [at] mb-itconsulting.com&gt;. </p>
<h2>Index</h2>
