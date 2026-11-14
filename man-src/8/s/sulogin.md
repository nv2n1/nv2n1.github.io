---
title: "sulogin(8)"
name: "sulogin"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sulogin/"
description: "sulogin – single-user login"
---

<p>sulogin &#8211; single-user login</p>
<h2>Synopsis</h2>
<p><code>sulogin</code> [options] [<i>tty</i>]</p>
<h2>Description</h2>
<p><code>sulogin</code> is invoked by <code>init</code> when the system goes into single-user mode. </p>
<p> The user is prompted: </p>
<p> Give root password for system maintenance (or type Control-D for normal startup): </p>
<p> If the root account is locked and <code>&#8211;force</code> is specified, no password is required. </p>
<p> <code>sulogin</code> will be connected to the current terminal, or to the optional <i>tty</i> device that can be specified on the command line (typically <i>/dev/console</i>). </p>
<p> When the user exits from the single-user shell, or presses control-D at the prompt, the system will continue to boot.</p>
<h2>Options</h2>
<p><code>-e</code>, <code>&#8211;force</code></p>
<dl>
<dd>If the default method of obtaining the root password from the system via <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a></code>(3) fails, then examine <i>/etc/passwd</i> and <i>/etc/shadow</i> to get the password. If these files are damaged or nonexistent, or when root account is locked by &#8216;!&#8217; or &#8216;*&#8217; at the begin of the password then <code>sulogin</code> will <code>start a root shell without asking for a password</code>. </p>
<p> Only use the <code>-e</code> option if you are sure the console is physically protected against unauthorized access.</dl>
<p> <code>-p</code>, <code>&#8211;login-shell</code></p>
<dl>
<dd>Specifying this option causes <code>sulogin</code> to start the shell process as a login shell.</dl>
<p> <code>-t</code>, <code>&#8211;timeout</code> <i>seconds</i></p>
<dl>
<dd>Specify the maximum amount of time to wait for user input. By default, <code>sulogin</code> will wait forever.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<h2>Environment</h2>
<p><code>sulogin</code> looks for the environment variable <code>SUSHELL</code> or <code>sushell</code> to determine what shell to start. If the environment variable is not set, it will try to execute root&#8217;s shell from <i>/etc/passwd</i>. If that fails, it will fall back to <i>/bin/sh</i>.</p>
<h2>Authors</h2>
<p><code>sulogin</code> was written by Miquel van Smoorenburg for sysvinit and later ported to util-linux by Dave Reisner and Karel Zak.</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>sulogin</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
