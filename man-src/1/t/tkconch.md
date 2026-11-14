---
title: "tkconch(1)"
name: "tkconch"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tkconch/"
description: "tkconch – connect to SSH servers graphically"
---

<h2>NAME</h2>
<p> tkconch &#8211; connect to SSH servers graphically</p>
<h2>SYNOPSIS</h2>
<p> <code>conch [-l </code><i>user</i>] [-i <i>identity</i> [ -i <i>identity</i> &#8230; ]] [-c <i>cipher</i>] [-m <i>MAC</i>] [-p <i>port</i>] [-n] [-t] [-T] [-V] [-C] [-N] [-s] [arg [&#8230;]] </p>
<p> <code>conch &#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>&#8211;help</code> prints out a usage message to standard output.</p>
<dl>
<dt><code>-l</code>, <code>&#8211;user</code> &lt;user&gt;</p>
<dd> Log in using this user name.</p>
<dt><code>-e</code>, <code>&#8211;escape</code> &lt;escape character&gt;</p>
<dd> Set escape character; &#8216;none&#8217; = disable (default: ~)</p>
<dt><code>-i</code>, <code>&#8211;identity</code> &lt;identity&gt;</p>
<dd> Add an identity file for public key authentication (default: ~/.ssh/identity)</p>
<dt><code>-c</code>, <code>&#8211;cipher</code> &lt;cipher&gt;</p>
<dd> Cipher algorithm to use.</p>
<dt><code>-m</code>, <code>&#8211;macs</code> &lt;mac&gt;</p>
<dd> Specify MAC algorithms for protocol version 2.</p>
<dt><code>-p</code>, <code>&#8211;port</code> &lt;port&gt;</p>
<dd> Port to connect to.</p>
<dt><code>-L</code>, <code>&#8211;localforward</code> &lt;listen-port:host:port&gt;</p>
<dd> Forward local port to remote address.</p>
<dt><code>-R</code>, <code>&#8211;remoteforward</code> &lt;listen-port:host:port&gt;</p>
<dd> Forward remote port to local address.</p>
<dt><code>-t</code>, <code>&#8211;tty</code></p>
<dd> Allocate a tty even if command is given.</p>
<dt><code>-n</code>, <code>&#8211;notty</code></p>
<dd> Do not allocate a tty.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version number only.</p>
<dt><code>-C</code>, <code>&#8211;compress</code></p>
<dd> Enable compression.</p>
<dt><code>-a</code>, <code>&#8211;ansilog</code></p>
<dd> Print the received data to stdout.</p>
<dt><code>-N</code>, <code>&#8211;noshell</code></p>
<dd> Do not execute a shell or command.</p>
<dt><code>-s</code>, <code>&#8211;subsystem</code></p>
<dd> Invoke command (mandatory) as SSH2 subsystem.</p>
<dt><code>&#8211;log</code></p>
<dd> Print the receieved data to stderr.</dl>
<h2>DESCRIPTION</h2>
<p> Open an SSH connection to specified server, and either run the command given there or open a remote interactive shell.</p>
<h2>AUTHOR</h2>
<p> Written by Moshe Zadka, based on conch&#8217;s help messages</p>
<h2>REPORTING BUGS</h2>
<p> To report a bug, visit <i><a rel="nofollow" href="http://twistedmatrix.com/bugs/">http://twistedmatrix.com/bugs/</a></i></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2008 Twisted Matrix Laboratories.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ssh/">ssh</a>(1) </p>
<h2>Index</h2>
