---

title: "tkconch(1)"
name: "tkconch"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tkconch/"
description: "tkconch – connect to SSH servers graphically"
---

<p> tkconch &#8211; connect to SSH servers graphically</p>
<h2>SYNOPSIS</h2>
<p> <code>conch [-l </code><i>user</i>] [-i <i>identity</i> [ -i <i>identity</i> &#8230; ]] [-c <i>cipher</i>] [-m <i>MAC</i>] [-p <i>port</i>] [-n] [-t] [-T] [-V] [-C] [-N] [-s] [arg [&#8230;]] </p>
<p> <code>conch &#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>&#8211;help</code> prints out a usage message to standard output.</p>
<dl>
<dt><code>-l</code>, <code>&#8211;user</code> &lt;user&gt;</dt>
<dd> Log in using this user name.</dd>
<dt><code>-e</code>, <code>&#8211;escape</code> &lt;escape character&gt;</dt>
<dd> Set escape character; &#8216;none&#8217; = disable (default: ~)</dd>
<dt><code>-i</code>, <code>&#8211;identity</code> &lt;identity&gt;</dt>
<dd> Add an identity file for public key authentication (default: ~/.ssh/identity)</dd>
<dt><code>-c</code>, <code>&#8211;cipher</code> &lt;cipher&gt;</dt>
<dd> Cipher algorithm to use.</dd>
<dt><code>-m</code>, <code>&#8211;macs</code> &lt;mac&gt;</dt>
<dd> Specify MAC algorithms for protocol version 2.</dd>
<dt><code>-p</code>, <code>&#8211;port</code> &lt;port&gt;</dt>
<dd> Port to connect to.</dd>
<dt><code>-L</code>, <code>&#8211;localforward</code> &lt;listen-port:host:port&gt;</dt>
<dd> Forward local port to remote address.</dd>
<dt><code>-R</code>, <code>&#8211;remoteforward</code> &lt;listen-port:host:port&gt;</dt>
<dd> Forward remote port to local address.</dd>
<dt><code>-t</code>, <code>&#8211;tty</code></dt>
<dd> Allocate a tty even if command is given.</dd>
<dt><code>-n</code>, <code>&#8211;notty</code></dt>
<dd> Do not allocate a tty.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Display version number only.</dd>
<dt><code>-C</code>, <code>&#8211;compress</code></dt>
<dd> Enable compression.</dd>
<dt><code>-a</code>, <code>&#8211;ansilog</code></dt>
<dd> Print the received data to stdout.</dd>
<dt><code>-N</code>, <code>&#8211;noshell</code></dt>
<dd> Do not execute a shell or command.</dd>
<dt><code>-s</code>, <code>&#8211;subsystem</code></dt>
<dd> Invoke command (mandatory) as SSH2 subsystem.</dd>
<dt><code>&#8211;log</code></dt>
<dd> Print the receieved data to stderr.</dd></dl>
<h2>DESCRIPTION</h2>
<p> Open an SSH connection to specified server, and either run the command given there or open a remote interactive shell.</p>
<h2>AUTHOR</h2>
<p> Written by Moshe Zadka, based on conch&#8217;s help messages</p>
<h2>REPORTING BUGS</h2>
<p> To report a bug, visit <i><a rel="nofollow" href="http://twistedmatrix.com/bugs/">http://twistedmatrix.com/bugs/</a></i></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2008 Twisted Matrix Laboratories.<br/>
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ssh/">ssh</a>(1) </p>
