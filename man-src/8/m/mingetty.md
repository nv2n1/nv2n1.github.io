---
title: "mingetty(8)"
name: "mingetty"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mingetty/"
description: "mingetty – minimal getty for consoles"
---
<p> mingetty - minimal getty for consoles  </p>
<h2>SYNOPSIS</h2>
<p> <code>mingetty</code> [--noclear] [--nonewline] [--noissue] [--nohangup] [--nohostname] [--long-hostname] [--loginprog=/bin/login] [--nice=10] [--delay=5] [--chdir=/home] [--chroot=/chroot] [--autologin username] [--loginpause] <i>tty</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>mingetty </code> is a minimal getty for use on virtual consoles. Unlike <code><a href="/docs/linux/man/8-agetty/">agetty</a></code>(8), <code>mingetty</code> is not suitable for serial lines. I recommend using <code><a href="/docs/linux/man/8-mgetty/">mgetty</a></code>(8) for this purpose. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>--noclear</code></dt>
<dd> <p> Do not clear the screen before prompting for the login name (the screen is normally cleared). </p>
 </dd>
<dt><code>--nonewline</code></dt>
<dd> <p> Do not print a newline before writing out /etc/issue. </p>
 </dd>
<dt><code>--noissue</code></dt>
<dd> <p> Do not output /etc/issue. </p>
 </dd>
<dt><code>--nohangup</code></dt>
<dd> <p> Do not call vhangup() to disable writing to this tty by other applications. </p>
 </dd>
<dt><code>--nohostname</code></dt>
<dd> <p> Do not print the hostname before the login prompt. </p>
 </dd>
<dt><code>--long-hostname</code></dt>
<dd> <p> By default the hostname is only printed until the first dot. With this option enabled, the full text from gethostname() is shown. </p>
 </dd>
<dt><code>--loginprog /bin/login</code></dt>
<dd> <p> Change the login app. </p>
 </dd>
<dt><code>--nice 10</code></dt>
<dd> <p> Change the priority by calling nice(). </p>
 </dd>
<dt><code>--delay 5</code></dt>
<dd> <p> Sleep this many seconds after startup of mingetty. </p>
 </dd>
<dt><code>--chdir /home</code></dt>
<dd> <p> Change into this directory before calling the login prog. </p>
 </dd>
<dt><code>--chroot /chroot</code></dt>
<dd> <p> Call chroot() with this directory name. </p>
 </dd>
<dt><code>--autologin username</code></dt>
<dd> <p> Log the specified user automatically in without asking for a login name and password. Check the -f option from <code>/bin/login</code> for this. </p>
 </dd>
<dt><code>--loginpause</code></dt>
<dd> <p> Wait for any key before dropping to the login prompt. Can be combined with <code>--autologin</code> to save memory by lazily spawning shells. </p>
 </dd></dl>
<h2>ISSUE ESCAPES</h2>
<p> <code>mingetty </code> recognizes the following escapes sequences which might be embedded in the <i>/etc/issue</i> file: </p>
<dl>
<dt><code>\d</code></dt>
<dd> <p> insert current day (localtime), </p>
 </dd>
<dt><code>\l</code></dt>
<dd> <p> insert line on which <code>mingetty </code> is running, </p>
 </dd>
<dt><code>\m</code></dt>
<dd> <p> inserts machine architecture (uname -m), </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> inserts machine&#8217;s network node hostname (uname -n), </p>
 </dd>
<dt><code>\o</code></dt>
<dd> <p> inserts domain name, </p>
 </dd>
<dt><code>\r</code></dt>
<dd> <p> inserts operating system release (uname -r), </p>
 </dd>
<dt><code>\t</code></dt>
<dd> <p> insert current time (localtime), </p>
 </dd>
<dt><code>\s</code></dt>
<dd> <p> inserts operating system name, </p>
 </dd>
<dt><code>\u</code></dt>
<dd> <p> resp. <code>\U</code> the current number of users which are currently logged in. \U inserts &quot;<i>n</i> users&quot;, where as \u only inserts &quot;<i>n</i>&quot;. </p>
 </dd>
<dt><code>\v</code></dt>
<dd> <p> inserts operating system version (uname -v). </p>
 </dd></dl>
<h2>EXAMPLE</h2>
<p> &quot;<code>Linux eos i386&nbsp;<wbr>#1 Tue Mar 19 21:54:09 MET 1996</code>&quot; was produced by putting &quot;<code>\s&nbsp;<wbr>\n&nbsp;<wbr>\m&nbsp;<wbr>\v</code>&quot; into <i>/etc/issue</i>. </p>
<h2>FILES</h2>
<p> <i>/etc/issue</i>, <i>/var/run/utmp</i>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-mgetty/">mgetty</a></code>(8), <code><a href="/docs/linux/man/8-agetty/">agetty</a></code>(8). </p>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1996 Florian La Roche &lt;laroche [at] redhat.com&gt;. Man-page written by David Frey &lt;David.Frey [at] eos.lugs.ch&gt; and Florian La Roche. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">ISSUE ESCAPES</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">EXAMPLE</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">FILES</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">AUTHOR</a></dt>
<dd>  </dd></dl>
