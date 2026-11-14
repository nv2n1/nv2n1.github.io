---
title: "mingetty(8)"
name: "mingetty"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mingetty/"
description: "mingetty – minimal getty for consoles"
---

<p>mingetty &#8211; minimal getty for consoles</p>
<h2>Synopsis</h2>
<p><code>mingetty</code> [&#8211;noclear] [&#8211;nonewline] [&#8211;noissue] [&#8211;nohangup] [&#8211;nohostname] [&#8211;long-hostname] [&#8211;loginprog=/bin/login] [&#8211;nice=10] [&#8211;delay=5] [&#8211;chdir=/home] [&#8211;chroot=/chroot] [&#8211;autologin username] [&#8211;loginpause] <i>tty</i> </p>
<h2>Description</h2>
<p><code>mingetty </code> is a minimal getty for use on virtual consoles. Unlike <code><a href="/docs/linux/man/8-agetty/">agetty</a></code>(8), <code>mingetty</code> is not suitable for serial lines. I recommend using <code><a href="/docs/linux/man/8-mgetty/">mgetty</a></code>(8) for this purpose. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;noclear</code></p>
<dd>Do not clear the screen before prompting for the login name (the screen is normally cleared).</p>
<dt><code>&#8211;nonewline</code></p>
<dd>Do not print a newline before writing out /etc/issue.</p>
<dt><code>&#8211;noissue</code></p>
<dd>Do not output /etc/issue.</p>
<dt><code>&#8211;nohangup</code></p>
<dd>Do not call vhangup() to disable writing to this tty by other applications.</p>
<dt><code>&#8211;nohostname</code></p>
<dd>Do not print the hostname before the login prompt.</p>
<dt><code>&#8211;long-hostname</code></p>
<dd>By default the hostname is only printed until the first dot. With this option enabled, the full text from gethostname() is shown.</p>
<dt><code>&#8211;loginprog /bin/login</code></p>
<dd>Change the login app.</p>
<dt><code>&#8211;nice 10</code></p>
<dd>Change the priority by calling nice().</p>
<dt><code>&#8211;delay 5</code></p>
<dd>Sleep this many seconds after startup of mingetty.</p>
<dt><code>&#8211;chdir /home</code></p>
<dd>Change into this directory before calling the login prog.</p>
<dt><code>&#8211;chroot /chroot</code></p>
<dd>Call chroot() with this directory name.</p>
<dt><code>&#8211;autologin username</code></p>
<dd>Log the specified user automatically in without asking for a login name and password. Check the -f option from <code>/bin/login</code> for this.</p>
<dt><code>&#8211;loginpause</code></p>
<dd>Wait for any key before dropping to the login prompt. Can be combined with <code>&#8211;autologin</code> to save memory by lazily spawning shells.</dl>
<h2>Issue Escapes</h2>
<p><code>mingetty </code> recognizes the following escapes sequences which might be embedded in the <i>/etc/issue</i> file:</p>
<dl>
<dt><code>\d</code></p>
<dd>insert current day (localtime),</p>
<dt><code>\l</code></p>
<dd>insert line on which <code>mingetty </code> is running,</p>
<dt><code>\m</code></p>
<dd>inserts machine architecture (uname -m),</p>
<dt><code>
</code></p>
<dd>inserts machine&#8217;s network node hostname (uname -n),</p>
<dt><code>\o</code></p>
<dd>inserts domain name,</p>
<dt><code></code></p>
<dd>inserts operating system release (uname -r),</p>
<dt><code>	</code></p>
<dd>insert current time (localtime),</p>
<dt><code>\s</code></p>
<dd>inserts operating system name,</p>
<dt><code>
