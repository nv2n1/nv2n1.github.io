---
title: "fence_bullpap(8)"
name: "fence_bullpap"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_bullpap/"
description: "fence_bullpap – I/O Fencing agent for Bull FAME architecture controlled by a PAP management console."
---

<p>fence_bullpap &#8211; I/O Fencing agent for Bull FAME architecture controlled by a PAP management console.</p>
<h2>Synopsis</h2>
<p><code>fence_bullpap</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>fence_bullpap is an I/O Fencing agent which can be used with Bull&#8217;s NovaScale machines controlled by PAP management consoles. This agent calls Bull&#8217;s support software provided by the NSMasterHW RPM available from Bull. fence_bullpap accepts options on the command line as well as from stdin. fenced sends the options through stdin when it execs the agent. fence_bullpap can be run by itself with command line options which is useful for testing. Vendor URL: <a rel="nofollow" href="http://www.bull.com">http://www.bull.com</a> </p>
<h2>Options</h2>
<dl>
<dt><code>-a</code> <i>IPaddress</i></p>
<dd>IP address or hostname of the PAP management console.</p>
<dt><code>-h</code></p>
<dd>Print out a help message describing available options, then exit.</p>
<dt><code>-l</code> <i>login</i></p>
<dd>Login with administrative privileges.</p>
<dt><code>-d</code> <i>domain</i></p>
<dd>This is the domain name of the Bull machine to power-cycle.</p>
<dt><code>-o</code> <i>option</i></p>
<dd>Action to perform (on, off, reboot, status).</p>
<dt><code>-p</code> <i>password</i></p>
<dd>Password for login.</p>
<dt><code>-S</code> <i>path</i></p>
<dd>Full path to an executable to generate the password for login.</p>
<dt><code>-q</code></p>
<dd>Quiet operation. Only print out error messages.</p>
<dt><code>-V</code></p>
<dd>Print out a version message, then exit. </p>
</dl>
<h2>Stdin Parameters</h2>
<dl>
<dt><i>ipaddr = &lt; hostname | ip &gt;</i></p>
<dd>IP address or hostname of the PAP management console.</p>
<dt><i>login= &lt; param &gt;</i></p>
<dd>Login with administrative privileges.</p>
<dt><i>domain = &lt; param &gt;</i></p>
<dd>This is the domain name of the Bull machine to power-cycle.</p>
<dt><i>option = &lt; param &gt;</i></p>
<dd>Action to perform (on, off, reboot, status).</p>
<dt><i>passwd = &lt; param &gt;</i></p>
<dd>Password for login.</p>
<dt><i>passwd_script = &lt; param &gt;</i></p>
<dd>Full path to an executable to generate the password for login. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fence/">fence</a>(8), <a href="/docs/linux/man/8-fence_node/">fence_node</a>(8) </p>
