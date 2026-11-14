---
title: "urxvt-mld(1)"
name: "urxvt-mld"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt-mld/"
description: "urxvt-mld – urxvt-ml terminal daemon"
---

<h2 class="name">NAME</h2>
<p> urxvt-mld &#8211; urxvt-ml terminal daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>urxvt-mld</code> [-q|&#8211;quiet] [-o|&#8211;opendisplay] [-f|&#8211;fork] [-m|&#8211;mlock] [-e|&#8211;eval <i>perlstring</i>] </p>
<p> <code>urxvt-mld</code> -q -o -f # for .xsession use</p>
<h2>DESCRIPTION</h2>
<p> This manpage describes the urxvt-mld daemon, which is the same vt102 terminal emulator as urxvt-ml, but runs as a daemon that can open multiple terminal windows within the same process. </p>
<p> You can run it from your X startup scripts, for example, although it is not dependent on a working <font SIZE="-1">DISPLAY</font> and, in fact, can open windows on multiple X displays on the same time. </p>
<p> Advantages of running a urxvt-ml daemon include faster creation time for terminal windows and a lot of saved memory. </p>
<p> The disadvantage is a possible impact on stability &#8211; if the main program crashes, all processes in the terminal windows are terminated. For example, as there is no way to cleanly react to abnormal connection closes, <tt>&quot;xkill&quot;</tt> and server resets/restarts will kill the <code>urxvt-mld</code> instance including all windows it has opened.</p>
<h2>OPTIONS</h2>
<p> <code>urxvt-mld</code> currently understands a few options only. Bundling of options is not yet supported.</p>
<dl>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Normally, <code>urxvt-mld</code> outputs the message <tt>&quot;rxvt-unicode daemon listening on &lt;path&gt;&quot;</tt> after binding to its control socket. This option will suppress this message (errors and warnings will still be logged).</p>
<dt><code>-o</code>, <code>&#8211;opendisplay</code></p>
<dd> This forces <code>urxvt-mld</code> to open a connection to the current <tt>$DISPLAY</tt> and keep it open. </p>
<p> This is useful if you want to bind an instance of <code>urxvt-mld</code> to the lifetime of a specific display/server. If the server does a reset, <code>urxvt-mld</code> will be killed automatically.</p>
<dt><code>-f</code>, <code>&#8211;fork</code></p>
<dd> This makes <code>urxvt-mld</code> fork after it has bound itself to its control socket.</p>
<dt><code>-m</code>, <code>&#8211;mlock</code></p>
<dd> This makes <code>urxvt-mld</code> call <i><a href="/docs/linux/man/2-mlockall/">mlockall</a></i>(2) on itself. This locks <code>urxvt-mld</code> in <font SIZE="-1">RAM</font> and prevents it from being swapped out to disk, at the cost of consuming a lot more memory on most operating systems. </p>
<p> Note: In order to use this feature, your system administrator must have set your user&#8217;s <font SIZE="-1">RLIMIT_MEMLOCK</font> to a size greater than or equal to the size of the <code>urxvt-mld</code> binary (or to unlimited). See <i>/etc/security/limits.conf</i>. </p>
<p> Note 2: There is a known bug in glibc (possibly fixed in 2.8 and later versions) where calloc returns non-zeroed memory when mlockall is in effect. If you experience crashes or other odd behaviour while using &#8211;mlock, try it without it.</p>
<dt><code>-e</code>, <code>&#8211;eval</code> <i>perlstring</i></p>
<dd> Evaluate the given perl code after basic initialisation (requires perl support to be enabled when compiling <code>urxvt-mld</code>). </p>
<p> This can be used for example to configure the internal perl interpreter, which is shared between all terminal instances, or create additional listening sockets for additional protocols. </p>
<p> The code is currently executed <i>before</i> creating the normal listening sockets: this might change in future versions.</dl>
<h2>EXAMPLES</h2>
<p> This is a useful invocation of <code>urxvt-mld</code> in a <i>.xsession</i>-style script: </p>
<pre>
   urxvt-mld -q -f -o
</pre>
<p> This waits till the control socket is available, opens the current display and forks into the background. When you log-out, the server is reset and <code>urxvt-mld</code> is killed.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>RXVT_SOCKET</code></font></p>
<dd> Both <code>urxvt-mlc</code> and <code>urxvt-mld</code> use the environment variable <i></i><font SIZE="-1"><i>RXVT_SOCKET</i></font><i></i> to create a listening socket and to contact the urxvt-mld, respectively. If the variable is missing then <i></i>$HOME<i>/.urxvt/urxvtd-&lt;nodename&gt;</i> is used.</p>
<dt><font SIZE="-1"><code>DISPLAY</code></font></p>
<dd> Only used when the <tt>&quot;--opendisplay&quot;</tt> option is specified. Must contain a valid X display name.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-urxvt-ml/">urxvt-ml</a>(7), <a href="/docs/linux/man/1-urxvt-mlc/">urxvt-mlc</a>(1) </p>
<h2>Index</h2>
