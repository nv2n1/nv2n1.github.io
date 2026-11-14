---
title: "spawn-fcgi(1)"
name: "spawn-fcgi"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spawn-fcgi/"
description: "spawn-fcgi – Spawns FastCGI processes"
---

<h2>NAME</h2>
<p> spawn-fcgi &#8211; Spawns FastCGI processes</p>
<h2>SYNOPSIS</h2>
<p> <code>spawn-fcgi</code> [options] [ &#8212; &lt;fcgiapp&gt; [fcgi app arguments]] </p>
<p> <code>spawn-fcgi</code> -v </p>
<p> <code>spawn-fcgi</code> -h</p>
<h2>DESCRIPTION</h2>
<p> <i>spawn-fcgi</i> is used to spawn remote and local FastCGI processes. </p>
<p> While it is obviously needed to spawn remote FastCGI backends (the web server can only spawn local ones), it is recommended to spawn local backends with spawn-fcgi, too. </p>
<p> Reasons why you may want to use spawn-fcgi instead of something else:</p>
<dl>
<dt>*</p>
<dd> Privilege separation without needing a suid-binary or running a server as root.</p>
<dt>*</p>
<dd> You can restart your web server and the FastCGI applications without restarting the others.</p>
<dt>*</p>
<dd> You can run them in different chroot()s.</p>
<dt>*</p>
<dd> Running your FastCGI applications doesn&#8217;t depend on the web server you are running, which allows for easier testing of other web servers.</dl>
<h2>OPTIONS</h2>
<p> <i>spawn-fcgi</i> accepts the following options:</p>
<dl>
<dt><code>-f &lt;path&gt;</code></p>
<dd> Filename of the FastCGI application to spawn. This option is deprecated and it is recommend to always specify the application (absolute path) and its parameters after &quot;&#8211;&quot;; the fcgiapp parameter is directly used for the exec() call, while for starting the binary given with -f /bin/sh is needed (which may not be available in a chroot).</p>
<dt>
<dd> This option is ignored if fcgiapp is given.</p>
<dt><code>-d &lt;path&gt;</code></p>
<dd> Change the current directory before spawning the application.</p>
<dt><code>-a &lt;address&gt;</code></p>
<dd> IPv4/IPv6 address to bind to; only used if -p is given too. Defaults to &quot;0.0.0.0&quot; (IPv4).</p>
<dt><code>-p &lt;port&gt;</code></p>
<dd> TCP port to bind to; you cannot combine this with the -s option.</p>
<dt><code>-s &lt;path&gt;</code></p>
<dd> Path to the Unix domain socket to bind to; you cannot combine this with the -p option.</p>
<dt><code>-C &lt;children&gt;</code></p>
<dd> (PHP only) Number of children to spawn by setting the PHP_FCGI_CHILDREN environment variable. Default is not to overwrite the environment variable; php will spawn no children if the variable is not set (same as setting it to 0).</p>
<dt><code>-F &lt;children&gt;</code></p>
<dd> Number of children to fork, defaults to 1. This option doesn&#8217;t work with -n, have a look at <code><a href="/docs/linux/man/1-multiwatch/">multiwatch</a>(1)</code> if you want to supervise multiple forks on the same socket.</p>
<dt><code>-P &lt;path&gt;</code></p>
<dd> Name of the PID file for spawned processes (ignored in no-fork mode)</p>
<dt><code>-n</code></p>
<dd> No forking should take place (for daemontools)</p>
<dt><code>-M &lt;mode&gt;</code></p>
<dd> Change file mode of the Unix domain socket; only used if -s is given too.</p>
<dt><code>-?, -h</code></p>
<dd> General usage instructions</p>
<dt><code>-v</code></p>
<dd> Shows version information and exits</dl>
<p> The following options are only available if you invoke spawn-fcgi as root:</p>
<dl>
<dt><code>-c &lt;directory&gt;</code></p>
<dd> Chroot to specified directory; the Unix domain socket is created inside the chroot unless -S is given.</p>
<dt><code>-S</code></p>
<dd> Create Unix domain socket before chroot().</p>
<dt><code>-u</code></p>
<dd> User ID to change to.</p>
<dt><code>-g</code></p>
<dd> Group ID to change to. Defaults to primary group of the user given for -u.</p>
<dt><code>-U</code></p>
<dd> Change user of the Unix domain socket, defaults to the value of -u. (only used if -s is given)</p>
<dt><code>-G</code></p>
<dd> Change group of the Unix domain socket, defaults to the primary group of the user given for -U; if -U wasn&#8217;t given, defaults to the value of -g. (only used if -s is given)</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-svc/">svc</a>(8),</code> <code><a href="/docs/linux/man/8-supervise/">supervise</a>(8),</code> see <a rel="nofollow" href="http://cr.yp.to/daemontools.html">http://cr.yp.to/daemontools.html</a> </p>
<p> <code><a href="/docs/linux/man/1-multiwatch/">multiwatch</a>(1),</code> see <a rel="nofollow" href="http://cgit.stbuehler.de/gitosis/multiwatch/about/">http://cgit.stbuehler.de/gitosis/multiwatch/about/</a> </p>
<h2>Index</h2>
