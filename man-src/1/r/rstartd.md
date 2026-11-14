---
title: "rstartd(1)"
name: "rstartd"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rstartd/"
description: "rstartd – a sample implementation of a Remote Start rsh helper"
---

<h2 class="name">NAME</h2>
<p> rstartd &#8211; a sample implementation of a Remote Start rsh helper </p>
<h2>SYNOPSIS</h2>
<p> <code>rstartd</code> </p>
<p> <code>rstartd.real</code> [-c <i>configfilename</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>Rstartd</i> is an implementation of a Remote Start &quot;helper&quot; as defined in &quot;A Flexible Remote Execution Protocol Based on <code>rsh</code>&quot;. </p>
<p> This document describes the peculiarities of <i>rstartd</i> and how it is configured.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c </code><i>configfilename</i></p>
<dd> This option specifies the &quot;global&quot; configuration file that <i>rstartd</i> is to read. Normally, <i>rstartd</i> is a shell script that invokes <i>rstartd.real</i> with the <code>-c</code> switch, allowing local configuration of the location of the configuration file. If <i>rstartd.real</i> is started without the -c option, it reads <i>/X11/rstart/config</i>.</dl>
<h2>INSTALLATION</h2>
<p> It is critical to successful interoperation of the Remote Start protocol that <i>rstartd</i> be installed in a directory which is in the &quot;default&quot; search path, so that default rsh requests and the ilk will be able to find it.</p>
<h2>CONFIGURATION AND OPERATION</h2>
<p> <i>Rstartd</i> is by design highly configurable. One would like things like configuration file locations to be fixed, so that users and administrators can find them without searching, but reality is that no two vendors will agree on where things should go, and nobody thinks the original location is &quot;right&quot;. Thus, <i>rstartd</i> allows one to relocate <code>all</code> of its files and directories. </p>
<p> <i>Rstartd</i> has a hierarchy of configuration files which are executed in order when a request is made. They are: </p>
<pre>
global config
per-user (&quot;local&quot;) config
global per-context config
per-user (&quot;local&quot;) per-context config
config from request
</pre>
<p> As you might guess from the presence of &quot;config from request&quot;, all of the config files are in the format of an <i>rstart</i> request. <i>Rstartd</i> defines a few additional keywords with the INTERNAL- prefix for specifying its configuration. </p>
<p> <i>Rstartd</i> starts by reading and executing the global config file. This file will normally specify the locations of the other configuration files and any systemwide defaults. </p>
<p> <i>Rstartd</i> will then read the user&#8217;s local config file, default name $HOME/.rstart. </p>
<p> <i>Rstartd</i> will then start interpreting the request. </p>
<p> Presumably one of the first lines in the request will be a CONTEXT line. The context name is converted to lower case. </p>
<p> <i>Rstartd</i> will read the global config file for that context, default name /usr/lib/X11/rstart/contexts/&lt;name&gt;, if any. </p>
<p> It will then read the user&#8217;s config file for that context, default name $HOME/.rstart.contexts/&lt;name&gt;, if any. </p>
<p> (If neither of these exists, <i>rstartd</i> aborts with a Failure message.) </p>
<p> <i>Rstartd</i> will finish interpreting the request, and execute the program specified. </p>
<p> This allows the system administrator and the user a large degree of control over the operation of <i>rstartd</i>. The administrator has final say, because the global config file doesn&#8217;t need to specify a per-user config file. If it does, however, the user can override anything from the global file, and can even completely replace the global context config files. </p>
<p> The config files have a somewhat more flexible format than requests do; they are allowed to contain blank lines and lines beginning with &quot;#&quot; are comments and ignored. (#s in the middle of lines are data, not comment markers.) </p>
<p> Any commands run are provided a few useful pieces of information in environment variables. The exact names are configurable, but the supplied defaults are: </p>
<table>
<tr VALIGN=top>
<td>$RSTART_CONTEXT</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>$RSTART_GLOBAL_CONTEXTS</td>
<td>the global contexts directory
</td>
</tr>
<tr VALIGN=top>
<td>$RSTART_LOCAL_CONTEXTS</td>
<td>the local contexts directory
</td>
</tr>
<tr VALIGN=top>
<td>$RSTART_GLOBAL_COMMANDS</td>
<td>the global generic commands directory
</td>
</tr>
<tr VALIGN=top>
<td>$RSTART_LOCAL_COMMANDS</td>
<td>the local generic commands directory
</td>
</tr>
</table>
<p> $RSTART_{GLOBAL,LOCAL}_CONTEXTS should contain one special file, @List, which contains a list of the contexts in that directory in the format specified for ListContexts. The supplied version of ListContexts will cat both the global and local copies of @List. </p>
<p> Generic commands are searched for in several places: (defaults) </p>
<pre>
per-user per-context directory ($HOME/.rstart.commands/&lt;context&gt;)
global per-context directory (/usr/lib/X11/rstart/commands/&lt;context&gt;)
per-user all-contexts directory ($HOME/.rstart.commands)
global all-contexts directory (/usr/lib/X11/rstart/commands)
</pre>
<p> (Yes, this means you can&#8217;t have an all-contexts generic command with the same name as a context. It didn&#8217;t seem like a big deal.) </p>
<p> Each of these directories should have a file called @List that gives the names and descriptions of the commands in that directory in the format specified for ListGenericCommands.</p>
<h2>CONFIGURATION KEYWORDS</h2>
<p> There are several &quot;special&quot; <i>rstart</i> keywords defined for <i>rstartd</i> configuration. Unless otherwise specified, there are no defaults; related features are disabled in this case. </p>
<dl>
<dt><code>INTERNAL-REGISTRIES name &#8230;</code></p>
<dd> Gives a space-separated list of &quot;MISC&quot; registries that this system understands. (Registries other than this are accepted but generate a Warning.)</p>
<dt><code>INTERNAL-LOCAL-DEFAULT relative_filename</code></p>
<dd> Gives the name ($HOME relative) of the per-user config file.</p>
<dt><code>INTERNAL-GLOBAL-CONTEXTS absolute_directory_name</code></p>
<dd> Gives the name of the system-wide contexts directory.</p>
<dt><code>INTERNAL-LOCAL-CONTEXTS relative_directory_name</code></p>
<dd> Gives the name ($HOME relative) of the per-user contexts directory.</p>
<dt><code>INTERNAL-GLOBAL-COMMANDS absolute_directory_name</code></p>
<dd> Gives the name of the system-wide generic commands directory.</p>
<dt><code>INTERNAL-LOCAL-COMMANDS relative_directory_name</code></p>
<dd> Gives the name ($HOME relative) of the per-user generic commands directory.</p>
<dt><code>INTERNAL-VARIABLE-PREFIX prefix</code></p>
<dd> Gives the prefix for the configuration environment variables <i>rstartd</i> passes to its kids.</p>
<dt><code>INTERNAL-AUTH-PROGRAM authscheme program argv[0] argv[1] &#8230;</code></p>
<dd> Specifies the program to run to set up authentication for the specified authentication scheme. &quot;program argv[0] &#8230;&quot; gives the program to run and its arguments, in the same form as the EXEC keyword.</p>
<dt><code>INTERNAL-AUTH-INPUT authscheme</code></p>
<dd> Specifies the data to be given to the authorization program as its standard input. Each argument is passed as a single line. $n, where n is a number, is replaced by the n&#8217;th argument to the &quot;AUTH authscheme arg1 arg2 &#8230;&quot; line.</p>
<dt><code>INTERNAL-PRINT arbitrary text</code></p>
<dd> Prints its arguments as a Debug message. Mostly for <i>rstartd</i> debugging, but could be used to debug config files.</dl>
<h2>NOTES</h2>
<p> When using the C shell, or any other shell which runs a script every time the shell is started, the script may get run several times. In the worst case, the script may get run <code>three</code> times: </p>
<pre>
By rsh, to run <i>rstartd</i>
By <i>rstartd</i>, to run the specified command
By the command, eg <i>xterm</i>
</pre>
<p> <i>rstartd</i> currently limits lines, both from config files and requests, to BUFSIZ bytes. </p>
<p> DETACH is implemented by redirecting file descriptors 0,1, and 2 to /dev/null and forking before executing the program. </p>
<p> CMD is implemented by invoking $SHELL (default /bin/sh) with &quot;-c&quot; and the specified command as arguments. </p>
<p> POSIX-UMASK is implemented in the obvious way. </p>
<p> The authorization programs are run in the same context as the target program &#8211; same environment variables, path, etc. Long term this might be a problem. </p>
<p> In the X context, GENERIC-CMD Terminal runs xterm. In the OpenWindows context, GENERIC-CMD Terminal runs cmdtool. </p>
<p> In the X context, GENERIC-CMD LoadMonitor runs xload. In the OpenWindows context, GENERIC-CMD LoadMonitor runs perfmeter. </p>
<p> <code>GENERIC-CMD ListContexts</code> lists the contents of @List in both the system-wide and per-user contexts directories. It is available in all contexts. </p>
<p> <code>GENERIC-CMD ListGenericCommands</code> lists the contents of @List in the system-wide and per-user commands directories, including the per-context subdirectories for the current context. It is available in all contexts. </p>
<p> <code>CONTEXT None</code> is not implemented. </p>
<p> <code>CONTEXT Default</code> is really dull. </p>
<p> For installation ease, the &quot;contexts&quot; directory in the distribution contains a file &quot;@Aliases&quot; which lists a context name and aliases for that context. This file is used to make symlinks in the contexts and commands directories. </p>
<p> All <code>MISC</code> values are passed unmodified as environment variables. </p>
<p> One can mistreat <i>rstartd</i> in any number of ways, resulting in anything from stupid behavior to core dumps. Other than by explicitly running programs I don&#8217;t think it can write or delete any files, but there&#8217;s no guarantee of that. The important thing is that (a) it probably won&#8217;t do anything REALLY stupid and (b) it runs with the user&#8217;s permissions, so it can&#8217;t do anything catastrophic. </p>
<p> @List files need not be complete; contexts or commands which are dull or which need not or should not be advertised need not be listed. In particular, per-user @List files should not list things which are in the system-wide @List files. In the future, perhaps ListContexts and ListGenericCommands will automatically suppress lines from the system-wide files when there are per-user replacements for those lines. </p>
<p> Error handling is OK to weak. In particular, no attempt is made to properly report errors on the exec itself. (Perversely, exec errors could be reliably reported when detaching, but not when passing the stdin/out socket to the app.) </p>
<p> If compiled with -DODT1_DISPLAY_HACK, <i>rstartd</i> will work around a bug in SCO ODT version 1. (1.1?) (The bug is that the X clients are all compiled with a bad library that doesn&#8217;t know how to look host names up using DNS. The fix is to look up a host name in $DISPLAY and substitute an IP address.) This is a trivial example of an incompatibility that <i>rstart</i> can hide.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rstart/">rstart</a>(1), <a href="/docs/linux/man/1-rsh/">rsh</a>(1), A Flexible Remote Execution Protocol Based on <code>rsh</code></p>
<h2>AUTHOR</h2>
<p> Jordan Brown, Quarterdeck Office Systems </p>
<h2>Index</h2>
