---
title: "xinit(1)"
name: "xinit"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xinit/"
description: "xinit – X Window System initializer"
---

<h2 class="name">NAME</h2>
<p> xinit &#8211; X Window System initializer </p>
<h2>SYNOPSIS</h2>
<p> <code>xinit</code> [ [ <i>client</i> ] <i>options</i> &#8230; ] [ <code>&#8212;</code> [ <i>server</i> ] [ <i>display</i> ] <i>options</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>xinit</code> program is used to start the X Window System server and a first client program on systems that are not using a display manager such as <code><a href="/docs/linux/man/1-xdm/">xdm</a></code>(1) or in environments that use multiple window systems. When this first client exits, <code>xinit</code> will kill the X server and then terminate. </p>
<p> If no specific client program is given on the command line, <code>xinit</code> will look for a file in the user&#8217;s home directory called <i>.xinitrc</i> to run as a shell script to start up client programs. If no such file exists, <code>xinit</code> will use the following as a default: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>xterm -geometry +1+1 -n login -display :0</p>
<p> If no specific server program is given on the command line, <code>xinit</code> will look for a file in the user&#8217;s home directory called <i>.xserverrc</i> to run as a shell script to start up the server. If no such file exists, <i>xinit</i> will use the following as a default: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>X :0</p>
<p> Note that this assumes that there is a program named <i>X</i> in the current search path. The site administrator should, therefore, make a link to the appropriate type of server on the machine, or create a shell script that runs <code>xinit</code> with the appropriate server. </p>
<p> Note, when using a <i>.xserverrc</i> script be sure to &#8220;exec&#8221; the real X server. Failing to do this can make the X server slow to start and exit. For example: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>exec Xdisplaytype</p>
<p> An important point is that programs which are run by <i>.xinitrc</i> should be run in the background if they do not exit right away, so that they don&#8217;t prevent other programs from starting up. However, the last long-lived program started (usually a window manager or terminal emulator) should be left in the foreground so that the script won&#8217;t exit (which indicates that the user is done and that <code>xinit</code> should exit). </p>
<p> An alternate client and/or server may be specified on the command line. The desired client program and its arguments should be given as the first command line arguments to <code>xinit</code>. To specify a particular server command line, append a double dash (&#8211;) to the <code>xinit</code> command line (after any client and arguments) followed by the desired server command. </p>
<p> Both the client program name and the server program name must begin with a slash (/) or a period (.). Otherwise, they are treated as an arguments to be appended to their respective startup lines. This makes it possible to add arguments (for example, foreground and background colors) without having to retype the whole command line. </p>
<p> If an explicit server name is not given and the first argument following the double dash (&#8211;) is a colon followed by a digit, <code>xinit</code> will use that number as the display number instead of zero. All remaining arguments are appended to the server command line. </p>
<h2>EXAMPLES</h2>
<p> Below are several examples of how command line arguments in <code>xinit</code> are used.</p>
<dl>
<dt><code>xinit</code></p>
<dd> This will start up a server named <i>X</i> and run the user&#8217;s <i>.xinitrc</i>, if it exists, or else start an <i>xterm</i>.</p>
<dt><code>xinit &#8212; /usr/bin/Xvnc :1</code></p>
<dd> This is how one could start a specific type of server on an alternate display.</p>
<dt><code>xinit -geometry =80&#215;65+10+10 -fn 8&#215;13 -j -fg white -bg navy</code></p>
<dd> This will start up a server named <i>X</i>, and will append the given arguments to the default <i>xterm</i> command. It will ignore <i>.xinitrc</i>.</p>
<dt><code>xinit -e widgets &#8212; ./Xorg -l -c</code></p>
<dd> This will use the command <i>./Xorg -l -c</i> to start the server and will append the arguments <i>-e widgets</i> to the default <i>xterm</i> command.</p>
<dt><code>xinit /usr/ucb/rsh fasthost cpupig -display ws:1 &#8212; :1 -a 2 -t 5</code></p>
<dd> This will start a server named <i>X</i> on display 1 with the arguments <i>-a 2 -t 5</i>. It will then start a remote shell on the machine <code>fasthost</code> in which it will run the command <i>cpupig</i>, telling it to display back on the local workstation.</dl>
<p> Below is a sample <i>.xinitrc</i> that starts a clock, several terminals, and leaves the window manager running as the &#8220;last&#8221; application. Assuming that the window manager has been configured properly, the user then chooses the &#8220;Exit&#8221; menu item to shut down X. </p>
<pre>
xrdb -load $HOME/.Xresources
xsetroot -solid gray &amp;
xclock -g 50x50-0+0 -bw 0 &amp;
xload -g 50x50-50+0 -bw 0 &amp;
xterm -g 80x24+0+0 &amp;
xterm -g 80x24+0-0 &amp;
twm
</pre>
<p> Sites that want to create a common startup environment could simply create a default <i>.xinitrc</i> that references a site-wide startup file: </p>
<pre>
#!/bin/sh
. /etc/X11/xinit/site.xinitrc
</pre>
<p> Another approach is to write a script that starts <code>xinit</code> with a specific shell script. Such scripts are usually named <i>x11</i>, <i>xstart</i>, or <i>startx</i> and are a convenient way to provide a simple interface for novice users: </p>
<pre>
#!/bin/sh
xinit /etc/X11/xinit/site.xinitrc -- /usr/bin/X -br
</pre>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> This variable gets set to the name of the display to which clients should connect.</p>
<dt><code>XINITRC</code></p>
<dd> This variable specifies an init file containing shell commands to start up the initial windows. By default, <i>.xinitrc</i> in the home directory will be used.</dl>
<h2>FILES</h2>
<dl>
<dt><i>.xinitrc</i></p>
<dd> default client script</p>
<dt><i>xterm</i></p>
<dd> client to run if <i>.xinitrc</i> does not exist</p>
<dt><i>.xserverrc</i></p>
<dd> default server script</p>
<dt><i>X</i></p>
<dd> server to run if <i>.xserverrc</i> does not exist</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-x/">X</a></code>(7), <code><a href="/docs/linux/man/1-startx/">startx</a></code>(1), <code><a href="/docs/linux/man/1-xserver/">Xserver</a></code>(1), <code><a href="/docs/linux/man/1-xorg/">Xorg</a></code>(1), <code><a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a></code>(5), <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Bob Scheifler, MIT Laboratory for Computer Science </p>
<h2>Index</h2>
