---
title: "wineserver(1)"
name: "wineserver"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wineserver/"
description: "wineserver – the Wine server"
---

<h2 class="name">NAME</h2>
<p> wineserver &#8211; the Wine server </p>
<h2>SYNOPSIS</h2>
<p> <code>wineserver</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>wineserver</code> is a daemon process that provides to Wine roughly the same services that the Windows kernel provides on Windows. </p>
<p> <code>wineserver</code> is normally launched automatically when starting <code><a href="/docs/linux/man/1-wine/">wine</a></code>(1), so you shouldn&#8217;t have to worry about it. In some cases however, it can be useful to start <code>wineserver</code> explicitly with different options, as explained below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>[<i>n</i>], <code>&#8211;debug</code>[<code>=</code><i>n</i>]</p>
<dd> Set the debug level to <i>n</i>. 0 means no debugging information, 1 is the normal level, and 2 is for extra verbose debugging. If <i>n</i> is not specified, the default is 1. The debug output will be sent to stderr. <code><a href="/docs/linux/man/1-wine/">wine</a></code>(1) will automatically enable normal level debugging when starting <code>wineserver</code> if the +server option is set in the <code>WINEDEBUG</code> variable.</p>
<dt><code>-f</code>, <code>&#8211;foreground</code></p>
<dd> Make the server remain in the foreground for easier debugging, for instance when running it under a debugger.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display a help message.</p>
<dt><code>-k</code>[<i>n</i>], <code>&#8211;kill</code>[<code>=</code><i>n</i>]</p>
<dd> Kill the currently running <code>wineserver</code>, optionally by sending signal <i>n</i>. If no signal is specified, sends a <code>SIGINT</code> first and then a <code>SIGKILL</code>. The instance of <code>wineserver</code> that is killed is selected based on the <code>WINEPREFIX</code> environment variable.</p>
<dt><code>-p</code>[<i>n</i>], <code>&#8211;persistent</code>[<code>=</code><i>n</i>]</p>
<dd> Specify the <code>wineserver</code> persistence delay, i.e. the amount of time that the server will keep running when all client processes have terminated. This avoids the cost of shutting down and starting again when programs are launched in quick succession. The timeout <i>n</i> is in seconds, the default value is 0 seconds. If <i>n</i> is not specified, the server stays around forever.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Display version information and exit.</p>
<dt><code>-w</code>, <code>&#8211;wait</code></p>
<dd> Wait until the currently running <code>wineserver</code> terminates.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>WINEPREFIX</code></p>
<dd> If set, the content of this variable is taken as the name of the directory where <code>wineserver</code> stores its data (the default is <i>$HOME/.wine</i>). All <code>wine</code> processes using the same <code>wineserver</code> (i.e.: same user) share certain things like registry, shared memory and kernel objects. By setting <code>WINEPREFIX</code> to different values for different Wine processes, it is possible to run a number of truly independent Wine sessions.</p>
<dt><code>WINESERVER</code></p>
<dd> Specifies the path and name of the <code>wineserver</code> binary that will be launched automatically by <code>wine</code>. If not set, <code>wine</code> will try to load <i>/usr/lib/wine/wineserver</i>, and if this doesn&#8217;t exist it will then look for a file named <i>wineserver</i> in the path and in a few other likely locations.</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.wine</code></p>
<dd> Directory containing user specific data managed by <code>wine</code>.</p>
<dt><code>/tmp/.wine-</code><i>uid</i></p>
<dd> Directory containing the server Unix socket and the lock file. These files are created in a subdirectory generated from the <code>WINEPREFIX</code> directory device and inode numbers.</dl>
<h2>AUTHORS</h2>
<p> The original author of <code>wineserver</code> is Alexandre Julliard. Many other people have contributed new features and bug fixes. For a complete list, see the git commit logs.</p>
<h2>BUGS</h2>
<p> Bugs can be reported on the <code>Wine bug tracker</code></p>
<h2>AVAILABILITY</h2>
<p> <code>wineserver</code> is part of the Wine distribution, which is available through WineHQ, the <code>Wine development headquarters</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wine/">wine</a></code>(1),<br />
 <code>Wine documentation and support</code> </p>
<h2>Index</h2>
