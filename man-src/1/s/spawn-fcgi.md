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
<dt>*</dt>
<dd> Privilege separation without needing a suid-binary or running a server as root.</dd>
<dt>*</dt>
<dd> You can restart your web server and the FastCGI applications without restarting the others.</dd>
<dt>*</dt>
<dd> You can run them in different chroot()s.</dd>
<dt>*</dt>
<dd> Running your FastCGI applications doesn&#8217;t depend on the web server you are running, which allows for easier testing of other web servers.</dd></dl>
<h2>OPTIONS</h2>
<p> <i>spawn-fcgi</i> accepts the following options:</p>
<dl>
<dt><code>-f &lt;path&gt;</code></dt>
<dd> Filename of the FastCGI application to spawn. This option is deprecated and it is recommend to always specify the application (absolute path) and its parameters after &quot;&#8211;&quot;; the fcgiapp parameter is directly used for the exec() call, while for starting the binary given with -f /bin/sh is needed (which may not be available in a chroot).</dd>
<dt>
</dt><dd> This option is ignored if fcgiapp is given.</dd>
<dt><code>-d &lt;path&gt;</code></dt>
<dd> Change the current directory before spawning the application.</dd>
<dt><code>-a &lt;address&gt;</code></dt>
<dd> IPv4/IPv6 address to bind to; only used if -p is given too. Defaults to &quot;0.0.0.0&quot; (IPv4).</dd>
<dt><code>-p &lt;port&gt;</code></dt>
<dd> TCP port to bind to; you cannot combine this with the -s option.</dd>
<dt><code>-s &lt;path&gt;</code></dt>
<dd> Path to the Unix domain socket to bind to; you cannot combine this with the -p option.</dd>
<dt><code>-C &lt;children&gt;</code></dt>
<dd> (PHP only) Number of children to spawn by setting the PHP_FCGI_CHILDREN environment variable. Default is not to overwrite the environment variable; php will spawn no children if the variable is not set (same as setting it to 0).</dd>
<dt><code>-F &lt;children&gt;</code></dt>
<dd> Number of children to fork, defaults to 1. This option doesn&#8217;t work with -n, have a look at <code>multiwatch(1)</code> if you want to supervise multiple forks on the same socket.</dd>
<dt><code>-P &lt;path&gt;</code></dt>
<dd> Name of the PID file for spawned processes (ignored in no-fork mode)</dd>
<dt><code>-n</code></dt>
<dd> No forking should take place (for daemontools)</dd>
<dt><code>-M &lt;mode&gt;</code></dt>
<dd> Change file mode of the Unix domain socket; only used if -s is given too.</dd>
<dt><code>-?, -h</code></dt>
<dd> General usage instructions</dd>
<dt><code>-v</code></dt>
<dd> Shows version information and exits</dd></dl>
<p> The following options are only available if you invoke spawn-fcgi as root:</p>
<dl>
<dt><code>-c &lt;directory&gt;</code></dt>
<dd> Chroot to specified directory; the Unix domain socket is created inside the chroot unless -S is given.</dd>
<dt><code>-S</code></dt>
<dd> Create Unix domain socket before chroot().</dd>
<dt><code>-u</code></dt>
<dd> User ID to change to.</dd>
<dt><code>-g</code></dt>
<dd> Group ID to change to. Defaults to primary group of the user given for -u.</dd>
<dt><code>-U</code></dt>
<dd> Change user of the Unix domain socket, defaults to the value of -u. (only used if -s is given)</dd>
<dt><code>-G</code></dt>
<dd> Change group of the Unix domain socket, defaults to the primary group of the user given for -U; if -U wasn&#8217;t given, defaults to the value of -g. (only used if -s is given)</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>svc(8),</code> <code>supervise(8),</code> see <a rel="nofollow" href="http://cr.yp.to/daemontools.html">http://cr.yp.to/daemontools.html</a> </p>
<p> <code>multiwatch(1),</code> see <a rel="nofollow" href="http://cgit.stbuehler.de/gitosis/multiwatch/about/">http://cgit.stbuehler.de/gitosis/multiwatch/about/</a> </p>
<h2>Index</h2>
