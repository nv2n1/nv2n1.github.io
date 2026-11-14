---
title: "startx(1)"
name: "startx"
section: "1"
letter: "s"
url: "/docs/linux/man/1-startx/"
description: "startx – initialize an X session"
---

<h2 class="name">NAME</h2>
<p> startx &#8211; initialize an X session </p>
<h2>SYNOPSIS</h2>
<p> <code>startx</code> [ [ <i>client</i> ] <i>options</i> &#8230; ] [ <code>&#8212;</code> [ <i>server</i> ] [ <i>display</i> ] <i>options</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>startx</code> script is a front end to <code><a href="/docs/linux/man/1-xinit/">xinit</a></code>(1) that provides a somewhat nicer user interface for running a single session of the X Window System. It is often run with no arguments. </p>
<p> Arguments immediately following the <i>startx</i> command are used to start a client in the same manner as <code><a href="/docs/linux/man/1-xinit/">xinit</a></code>(1). The special argument &#8216;&#8211;&#8216; marks the end of client arguments and the beginning of server options. It may be convenient to specify server options with startx to change them on a per-session basis. Some examples of specifying server arguments follow; consult the manual page for your X server to determine which arguments are legal.</p>
<dl>
<dt>
<dd>
<p> startx &#8212; -depth 16 </p>
<p> startx &#8212; -dpi 100 </p>
<p> startx &#8212; -layout Multihead</dl>
<p> Note that in the Debian system, what many people traditionally put in the <i>.xinitrc</i> file should go in <i>.xsession</i> instead; this permits the same X environment to be presented whether <i>startx</i>, <i>xdm</i>, or <i>xinit</i> is used to start the X session. All discussion of the <i>.xinitrc</i> file in the <i><a href="/docs/linux/man/1-xinit/">xinit</a></i>(1) manual page applies equally well to <i>.xsession.</i> Keep in mind that <i>.xinitrc</i> is used only by <i><a href="/docs/linux/man/1-xinit/">xinit</a></i>(1) and completely ignored by <i><a href="/docs/linux/man/1-xdm/">xdm</a></i>(1). </p>
<p> To determine the client to run, <code>startx</code> looks for the following files, in order:</p>
<dl>
<dt>
<dd>
<p> <i>$(HOME)/.startxrc</i> </p>
<p> <i>/usr/lib/x86_64-linux-gnu/sys.startxrc</i> </p>
<p> <i>$(HOME)/.xinitrc</i> </p>
<p> <i>/etc/X11/xinit/xinitrc</i></dl>
<p> If command line client options are given, they override this behavior and revert to the <code><a href="/docs/linux/man/1-xinit/">xinit</a></code>(1) behavior. To determine the server to run, <code>startx</code> first looks for a file called <i>.xserverrc</i> in the user&#8217;s home directory. If that is not found, it uses the file <i>xserverrc</i> in the <i>xinit</i> library directory. If command line server options are given, they override this behavior and revert to the <code><a href="/docs/linux/man/1-xinit/">xinit</a></code>(1) behavior. Users rarely need to provide a <i>.xserverrc</i> file. See the <code><a href="/docs/linux/man/1-xinit/">xinit</a></code>(1) manual page for more details on the arguments. </p>
<p> The system-wide <i>xinitrc</i> and <i>xserverrc</i> files are found in the <i>/etc/X11/xinit</i> directory.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>DISPLAY</p>
<dd> This variable gets set to the name of the display to which clients should connect. Note that this gets <i>set</i>, not read.</p>
<dt>XAUTHORITY</p>
<dd> This variable, if not already defined, gets set to <i>$(HOME)/.Xauthority</i>. This is to prevent the X server, if not given the <i>-auth</i> argument, from automatically setting up insecure host-based authentication for the local host. See the <code><a href="/docs/linux/man/1-xserver/">Xserver</a></code>(1) and <i><a href="/docs/linux/man/7-xsecurity/">Xsecurity</a></i>(7) manual pages for more information on X client/server authentication.</dl>
<h2>FILES</h2>
<dl>
<dt><i>$(HOME)/.xinitrc</i></p>
<dd> Client to run. Typically a shell script which runs many programs in the background.</p>
<dt><i>$(HOME)/.xserverrc</i></p>
<dd> Server to run. The default is <i>X</i>.</p>
<dt><i>/etc/X11/xinit/xinitrc</i></p>
<dd> Client to run if the user has no <i>.xinitrc</i> file.</p>
<dt><i>/etc/X11/xinit/xserverrc</i></p>
<dd> Server to run if the user has no <i>.xserverrc</i> file.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xinit/">xinit</a></code>(1), <code><a href="/docs/linux/man/7-x/">X</a></code>(7), <code><a href="/docs/linux/man/1-xserver/">Xserver</a></code>(1), <code><a href="/docs/linux/man/1-xorg/">Xorg</a></code>(1), <code><a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a></code>(5) </p>
<h2>Index</h2>
