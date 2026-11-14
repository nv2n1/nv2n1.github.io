---
title: "hh_client(1)"
name: "hh_client"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hh_client/"
description: "hh_client – Interface to Hack language typechecker"
---

<h2 class="name">NAME</h2>
<p> hh_client &#8211; Interface to Hack language typechecker</p>
<h2>SYNOPSIS</h2>
<p> <code>hh_client</code> [<i>MODE</i>] [<i>OPTIONS</i>] [<i>DIRECTORY</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-hh_client/">hh_client</a></code>(1) is an interface to a static analysis tool which is what enforces most of the Hack language&#8217;s type system. Code must pass validation of this tool in order to be considered valid code in the Hack language. </p>
<p> There are several possible <i>MODE</i>s for <code><a href="/docs/linux/man/1-hh_client/">hh_client</a></code>(1) (see below). By default, it will invoke the <code>check</code> mode, with the current directory as <i>DIRECTORY</i>. These are reasonable defaults, meaning that most users can simply invoke the command as </p>
<pre>
<dl><dt><dd>hh_client
</dl>
</pre>
<p> with no arguments to get a list of type errors across the entire project. </p>
<p> All of the <i>MODE</i>s accept a <i>DIRECTORY</i> as an optional final argument. This denotes the project upon which to operate. <code><a href="/docs/linux/man/1-hh_client/">hh_client</a></code>(1) walks up the filesystem from the <i>DIRECTORY</i> until it finds a file called <i>.hhconfig</i> and then operates on the body of Hack language code rooted in this directory. If no <i>DIRECTORY</i> is specified, it uses the current directory by default. This means you may run <code><a href="/docs/linux/man/1-hh_client/">hh_client</a></code>(1) in any subdirectory of your project and get type errors for the whole project without ever specifying a <i>DIRECTORY</i> explicitly. </p>
<p> <code><a href="/docs/linux/man/1-hh_client/">hh_client</a></code>(1) implements very little logic itself, but rather serves as an interface to the <code><a href="/docs/linux/man/1-hh_server/">hh_server</a></code>(1) daemon. The server will automatically be started and restarted as needed. </p>
<h2>MODES</h2>
<h3>check</h3>
<p> The default <i>MODE</i> if none is specified. With no <i>OPTIONS</i> specified, it prints a list of type errors on standard output, or prints &quot;No errors!&quot; if there were none. </p>
<p> Many <i>OPTIONS</i> affect the output of <code>check</code> mode, sometimes causing it to do completely different things. (Those can be considered &quot;sub-modes&quot; of <code>check</code> mode.) Many of these options are undergoing considerable revision and so are not documented here; read the source for a full list. </p>
<p> Widely-useful <i>OPTIONS</i> for <code>check</code> mode include: </p>
<dl>
<dt><code>&#8211;color</code><i> FILE</i></p>
<dd> Sub-mode which prints out information on what parts of <i>FILE</i> are actually typechecked and which are not. Due to Hack&#8217;s partial mode and PHP interoperability, the type system may not know the types of parts of a program. In this case, it trusts the programmer and carries on. The <code>&#8211;color</code> mode prints out a file with ANSI terminal colors, where green code is actually fully checked, and red code cannot be fully checked due to such missing type information. </p>
<dt><code>&#8211;help</code></p>
<dd> Prints information about <code><a href="/docs/linux/man/1-hh_client/">hh_client</a></code>(1) and its command line options, and then exits. Many of the options described there are experimental, especially if they are not described in this man page. </p>
<dt><code>&#8211;from</code><i> EDITOR</i></p>
<dd> Prints output in the format expected by a specific editor. Valid values of <i>EDITOR</i> are <code>emacs</code> and <code>vim</code>. For usage by other tools, try <code>&#8211;json</code> instead. </p>
<dt><code>&#8211;json</code></p>
<dd> Prints output in a JSON format intended for machine consumption, instead of the output intended for human consumption that is output by default. </p>
<dt><code>&#8211;retries</code><i> NUM</i></p>
<dd> If the typechecker daemon is busy, try <i>NUM</i> times to connect to it before giving up. Set <i>NUM</i> to 0 to disable retries if the server is not immediately available. </p>
<dt><code>&#8211;status</code></p>
<dd> Prints human-readable type error information to standard out and then exits. The default sub-mode of <code>check</code> if none is specified. This output is not intended for usage by tools, but only for human consumption. For output intended for tool usage, see the <code>&#8211;json</code> and/or <code>&#8211;from</code> options. </p>
<dt><code>&#8211;version</code></p>
<dd> Prints the current client version, including build ID and build date, and then exits. </p>
<dt><code>&#8211;auto-complete</code></p>
<dd> Autocompletes text on STDIN where the cursor is replaced with <i>AUTO332.</i> Returns a newline-separated list. </p>
<dt><code>&#8211;search</code><i> STRING</i></p>
<dd> Fuzzy search symbol definitions for <i>STRING.</i> Returns a newline-separated list. </p>
</dl>
<h3>start</h3>
<p> Explicitly starts the <code><a href="/docs/linux/man/1-hh_server/">hh_server</a></code>(1) daemon if it is not already running. This is not normally necessary, since <code>check</code> mode will start it as needed if it is not running. </p>
<h3>stop</h3>
<p> Explicitly stops the <code><a href="/docs/linux/man/1-hh_server/">hh_server</a></code>(1) daemon if it is running. This is not normally necessary, since the daemon will exit if it has not been used for an extended period of time. </p>
<h3>restart</h3>
<p> Explicitly stops and then starts again the <code><a href="/docs/linux/man/1-hh_server/">hh_server</a></code>(1) daemon. Fails if the daemon is not currently running. Restarting the daemon is not normally necessary, since it updates its state in the background, and <code><a href="/docs/linux/man/1-hh_client/">hh_client</a></code>(1) will restart it automatically if the typechecker binaries have been updated. </p>
<h2>EXIT STATUS</h2>
<p> For <code>check</code> mode in the <code>&#8211;status</code> sub-mode, <code><a href="/docs/linux/man/1-hh_client/">hh_client</a></code>(1) returns 0 if there are no type errors, and non-zero otherwise. </p>
<p> Exit statuses for any other invocations are currently undefined and subject to change. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>USER</code></p>
<dd> Used in combination with the path to the project root in order to locate the socket for communicating with the running <code><a href="/docs/linux/man/1-hh_server/">hh_server</a></code>(1) daemon. Normally set by your login environment, but may be unset in some nonstandard setups. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>.hhconfig</i></p>
<dd> When determining where the project root is in order to figure out what files to actually typecheck, <code><a href="/docs/linux/man/1-hh_client/">hh_client</a></code>(1) walks up the directory tree from the specified <i>DIRECTORY</i> until it finds this file. The set of files recursively included in the directory with the <i>.hhconfig</i> file is the set of files typechecked. </p>
<dt><i>/tmp/hh_server_</i><code>$USER</code><i>/</i></p>
<dd> The client looks inside this directory for sockets to communicate with the <code><a href="/docs/linux/man/1-hh_server/">hh_server</a></code>(1) daemon. The sockets are named based on a hash of the absolute path of the project root. </p>
</dl>
<h2>BUGS</h2>
<p> The Hack language is part of the HHVM project. Known bugs can be found at that tracker, and new ones should be reported there as well: <i><a rel="nofollow" href="https://github.com/facebook/hhvm/issues">https://github.com/facebook/hhvm/issues</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-hh_server/">hh_server</a></code>(1),<code>&nbsp;<a href="/docs/linux/man/1-hackificator/">hackificator</a></code>(1),<code>&nbsp;<a href="/docs/linux/man/1-hack_remove_soft_types/">hack_remove_soft_types</a></code>(1).<br />
 <i><a rel="nofollow" href="http://docs.hhvm.com/hack/typechecker/setup">http://docs.hhvm.com/hack/typechecker/setup</a></i><br />
 <i><a rel="nofollow" href="http://www.hacklang.org/">http://www.hacklang.org/</a></i> </p>
<h2>Index</h2>
