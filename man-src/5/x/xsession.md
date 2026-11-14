---
title: "xsession(5)"
name: "xsession"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xsession/"
description: "Xsession – initialize X session"
---

<p>Xsession &#8211; initialize X session</p>
<h2>Synopsis</h2>
<p>Xsession [ <i>session-type</i> ]</p>
<h2>Description</h2>
<p><i>/etc/X11/Xsession</i> is a Bourne shell (<code><a href="/docs/linux/man/1-sh/">sh</a></code>(1)) script which is run when an X Window System session is begun by <code><a href="/docs/linux/man/1-startx/">startx</a></code>(1) or a display manager such as <code><a href="/docs/linux/man/1-xdm/">xdm</a></code>(1). (Some display managers only invoke <i>Xsession</i> when specifically directed to so by the user; see the documentation for your display manager to find out more.) Administrators unfamiliar with the Bourne shell will likely find the <code><a href="/docs/linux/man/5-xsession-options/">Xsession.options</a></code>(5) configuration file easier to deal with than <i>Xsession</i> itself. </p>
<p> <i>Xsession</i> is not intended to be invoked directly by the user; to be effective it needs to run in a special environment associated with X server initialization. <code>startx</code>, <code>xdm</code>, <code><a href="/docs/linux/man/1-xinit/">xinit</a></code>(1), and other similar programs handle this. </p>
<p> By default on a Debian system, <i>Xsession</i> is used by both common methods of starting the X Window System, <code>xdm</code> (or another X display manager) and <code>startx</code>. To change this for <code>xdm,</code> edit the &#8216;DisplayManager*session&#8217; resource in the <i>/etc/X11/xdm/xdm-config</i> file &#8212; for other display managers, consult their documentation. To stop <code>startx</code> from using <i>Xsession</i> by default, replace the contents of the <i>/etc/X11/xinit/xinitrc</i> file. </p>
<p> The <i>Xsession</i> script is quite flexible, and extensive customization of the X startup procedure is possible without modifying the script itself. See &#8220;CUSTOMIZING THE STARTUP PROCEDURE&#8221; below.</p>
<h3>Session Types</h3>
<p><i>Xsession</i> may optionally be passed a single argument indicating the type of X session to be started. It is up to the display manager to set the argument. To pass <i>Xsession</i> an argument from <code>startx</code> or <code>xinit</code>, <i>/etc/X11/Xsession</i> (or <i>/etc/X11/xinit/xinitrc</i>) must be called explicitly with a path, as in <code>startx /etc/X11/Xsession</code> <code>failsafe</code>. By default, three different arguments are supported:</p>
<dl>
<dt><code>failsafe</code></p>
<dd>invokes a session consisting solely of an <code><a href="/docs/linux/man/1-x-terminal-emulator/">x-terminal-emulator</a></code>(1) (no window manager is launched). If the <code>x-terminal-emulator program cannot</code> be found, the session exits. The &#8216;failsafe&#8217; argument is ignored if there is no &#8216;allow-failsafe&#8217; line in <i>Xsession.options</i>.</p>
<dt><code>default</code></p>
<dd>produces the same behavior as if no session type argument had been given at all.</p>
<dt><i>program</i></p>
<dd>starts <i>program</i> if it can be found in the $PATH. This is usually a session manager or a very featureful window manager. If <i>program</i> is not found, the <i>Xsession</i> script proceeds with its default behavior. This argument is ignored if there is no &#8216;allow-user-xsession&#8217; line in <i>Xsession.options</i>. (If the administrator does not want users writing their own <i>.xsession</i> files, it makes little sense to permit them to specify the names of arbitrary programs to run.) Note that the restriction may be easy to bypass, e.g. by using a <i>.gnomerc</i> file instead.</dl>
<h3>Default Startup Procedure</h3>
<p>Initially, <i>Xsession</i> performs some housekeeping. It declares a set of built-in functions (see &#8220;BUILT-IN SHELL FUNCTIONS&#8221; below) and variables, then attempts to create a log file for the X session, or append to an existing one. Historically this is called an &#8216;error&#8217; file, but it catches all sorts of diagnostic output from various X clients run in the user&#8217;s session, not just error messages. If it is impossible to write to an error file, the script (and thus the X session) aborts. For convenience, once the error file is successfully opened, <i>Xsession</i> reports the fact that the session has started, the invoking username, and the date to the error file. This makes it easier to discern which X session produced a particular line of output in the file. </p>
<p> <i>Xsession</i> next confirms that its script directory, <i>Xsession.d</i>, exists. If it does not, the script aborts. After the script directory is confirmed to be present, <i>Xsession</i> uses <code><a href="/docs/linux/man/1-run-parts/">run-parts</a></code>(1) to identify files in that directory that should be sourced (executed) in the shell&#8217;s environment. Only files named in a certain way are sourced; see the <code>run-parts</code> manual page for a description of valid characters in the filename. (This restriction enables the administrator to move experimental or problematic files out of the way of the script but keep them in an obvious place, for instance by renaming them with &#8216;.old&#8217; or &#8216;.broken&#8217; appended to the filename.)</p>
<h3>Supplied Scripts</h3>
<p>Five shell script portions are supplied by default to handle the details of the session startup procedure.</p>
<dl>
<dt><i>/etc/X11/Xsession.d/20&#215;11-common_process-args</i></p>
<dd>Arguments are processed as described in &#8220;SESSION TYPES&#8221; above. The startup program, if one is identified at this point, is merely stored for later reference, and not immediately executed.</p>
<dt><i>/etc/X11/Xsession.d/30&#215;11-common_xresources</i></p>
<dd>X resources are merged. <code>run-parts</code> is again used, this time to identify files in the <i>/etc/X11/Xresources</i> directory that should be processed with &#8216;xrdb -merge&#8217;. Next, if the line &#8216;allow-user-resources&#8217; is present in <i>Xsession.options</i>, the user&#8217;s <i>$HOME/.Xresources</i> file is merged in the same way.</p>
<dt><i>/etc/X11/Xsession.d/35&#215;11-common_xhost-local</i></p>
<dd>Give access to the X server to the same user on the local host. If the <i>xhost</i> command is available, it will use it to allow any process of the same user running on the local host to access the X server.</p>
<dt><i>/etc/X11/Xsession.d/40&#215;11-common_xsessionrc</i></p>
<dd>Source global environment variables. This script will source anything in <i>$HOME/.xsessionrc</i> if the file is present. This allows the user to set global environment variables for their X session, such as locale information.</p>
<dt><i>/etc/X11/Xsession.d/50&#215;11-common_determine-startup</i></p>
<dd>Determine startup program. The X client to launch as the controlling process (the one that, upon exiting, causes the X server to exit as well) is determined next. If a program or failsafe argument was given and is allowed (see above), it is used as the controlling process. Otherwise, if the line &#8216;allow-user-xsession&#8217; is present in <i>Xsession.options</i>, a user-specified session program or script is used. In the latter case, two historically popular names for user X session scripts are searched for: <i>$HOME/.xsession</i> and <i>$HOME/.Xsession</i> (note the difference in case). The first one found is used. If the script is not executable, it is marked to be executed with the Bourne shell interpreter, <code>sh</code>. Finally, if none of the above succeeds, the following programs are searched for: <i>/usr/bin/x-session-manager</i>, <i>/usr/bin/x-window-manager</i>, and <i>/usr/bin/x-terminal-emulator</i>. The first one found is used. If none are found, <i>Xsession</i> aborts with an error.</p>
<dt><i>/etc/X11/Xsession.d/90&#215;11-common_ssh-agent</i></p>
<dd>Start <code><a href="/docs/linux/man/1-ssh-agent/">ssh-agent</a></code>(1), if needed. If the line &#8216;use-ssh-agent&#8217; is present in <i>Xsession.options</i>, and no SSH agent process appears to be running already, <code>ssh-agent</code> is marked to be used to execute the startup program determined previously. <code>Note:</code> this functionality may move to the ssh package in the future.</p>
<dt><i>/etc/X11/Xsession.d/99&#215;11-common_start</i></p>
<dd>Start the X session. The startup program is executed, inside a Bourne shell if it is not executable, and inside an ssh-agent if necessary. The shell&#8217;s <code>exec</code> command is used to spare a slot in the process table.</dl>
<h3>Customizing The Startup Procedure</h3>
<p>Of course, any of the existing files can be edited in place. </p>
<p> Because the order in which the various scripts in <i>/etc/X11/Xsession.d</i> are executed is important, files to be added to this directory should have a well-formed name. The following format is recommended: </p>
<p> * a two-digit number denoting sequence; </p>
<p> * the name of the package providing the script (or &#8216;custom&#8217; for locally-created scripts); </p>
<p> * an underscore; </p>
<p> * a description of the script&#8217;s basic function, using only characters allowed by <code>run-parts</code>. </p>
<p> Here is an example of how one might write a script, named <i>40custom_load-xmodmap</i>, to invoke <code><a href="/docs/linux/man/1-xmodmap/">xmodmap</a></code>(1): </p>
<pre>SYSMODMAP=&quot;/etc/X11/Xmodmap&quot;
USRMODMAP=&quot;$HOME/.Xmodmap&quot;
if [ -x /usr/bin/X11/xmodmap ]; then
 if [ -f &quot;$SYSMODMAP&quot; ]; then
 xmodmap &quot;$SYSMODMAP&quot;
 fi
fi
if [ -x /usr/bin/X11/xmodmap ]; then
 if [ -f &quot;$USRMODMAP&quot; ]; then
 xmodmap &quot;$USRMODMAP&quot;
 fi
fi</pre>
<p>Those writing scripts for <i>Xsession</i> to execute should avail themselves of its built-in shell functions, described below.</p>
<h3>Built-In Shell Functions</h3>
<p><code>message</code> is used for communicating with the user. It is a wrapper for the <code><a href="/docs/linux/man/1-echo/">echo</a></code>(1) command and relies upon <code>echo</code> for its argument processing. This function may be given an arbitrarily long message string, which is formatted to the user&#8217;s terminal width (breaking lines at whitespace) and sent to standard error. If the <i>DISPLAY</i> environment variable is set and the <code><a href="/docs/linux/man/1-xmessage/">xmessage</a></code>(1) program is available, <code>xmessage</code> is also used to display the message. </p>
<p> <code>message_nonl</code> is used for communicating with the user when a trailing newline is undesirable; it omits a trailing newline from the message text. It otherwise works as <code>message</code>. </p>
<p> <code>errormsg</code> is used for indicating an error condition and aborting the script. It works as <code>message</code>, above, except that after displaying the message, it will exit <i>Xsession</i> with status 1.</p>
<h2>Environment</h2>
<p>The following environment variables affect the execution of <i>Xsession</i>:</p>
<dl>
<dt><code>HOME</code></p>
<dd>specifies the user&#8217;s home directory; various files are searched for here.</p>
<dt><code>TMPDIR</code></p>
<dd>names a default directory for temporary files; if the standard X session error file cannot be opened, this variable is used to locate a place for one.</p>
<dt><code>COLUMNS</code></p>
<dd>indicates the width of terminal device in character cells. This value is used for formatting diagnostic messages.</dl>
<h2>Input Files</h2>
<dl>
<dt><i>/etc/X11/Xsession.d/</i></p>
<dd>is a directory containing Bourne shell scripts to be executed by <i>Xsession</i>. Files in this directory are matched using <code>run-parts</code> and are <code>source</code>d, not executed in a subshell.</p>
<dt><i>/etc/X11/Xresources/</i></p>
<dd>is a directory containing files corresponding to Debian package names, each of which contains system-wide X resource settings for X clients from the corresponding package. The settings are loaded with <code>xrdb -merge</code>. Files in this directory are matched using <code>run-parts</code>.</p>
<dt><i>/etc/X11/Xsession.options</i></p>
<dd>contains configuration options for the <i>/etc/X11/Xsession</i> script. See <code><a href="/docs/linux/man/5-xsession-options/">Xsession.options</a></code>(5) for more information.</p>
<dt><i>$HOME/.Xresources</i></p>
<dd>contains X resources specific to the invoking user&#8217;s environment. The settings are loaded with <code>xrdb -merge</code>. Note that <i>$HOME/.Xdefaults</i> is a relic from X Version 10 (and X11R1) days, before app-defaults files were implemented. It has been deprecated for over ten years at the time of this writing. <i>.Xresources</i> should be used instead.</p>
<dt><i>$HOME/.xsession</i></p>
<dd>is a sequence of commands invoking X clients (or a session manager such as <code><a href="/docs/linux/man/1-xsm/">xsm</a></code>(1)). See the manual page for <code>xinit</code> for tips on writing an <i>.xsession</i> file.</dl>
<h2>Output Files</h2>
<dl>
<dt><i>$HOME/.xsession-errors</i></p>
<dd>is where standard output and standard error for <i>Xsession</i> script and all X client processes are directed by default.</p>
<dt><i>$TMPDIR/filename</i></p>
<dd>is where the X session error file is placed if <i>$HOME/.xsession-errors</i> cannot be opened. For security reasons, the exact filename is randomly generated by <code><a href="/docs/linux/man/1-tempfile/">tempfile</a></code>(1).</dl>
<h2>Authors</h2>
<p>Stephen Early, Mark Eichin, and Branden Robinson developed Debian&#8217;s X session handling scripts. Branden Robinson wrote this manual page.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-xsession-options/">Xsession.options</a></code>(5), <code><a href="/docs/linux/man/7-x/">X</a></code>(7), <code><a href="/docs/linux/man/1-run-parts/">run-parts</a></code>(1), <code><a href="/docs/linux/man/1-ssh-agent/">ssh-agent</a></code>(1), <code><a href="/docs/linux/man/1-startx/">startx</a></code>(1), <code><a href="/docs/linux/man/1-tempfile/">tempfile</a></code>(1), <code><a href="/docs/linux/man/1-xdm/">xdm</a></code>(1), <code><a href="/docs/linux/man/1-xmessage/">xmessage</a></code>(1), <code><a href="/docs/linux/man/1-xmodmap/">xmodmap</a></code>(1), <code><a href="/docs/linux/man/1-xrdb/">xrdb</a></code>(1), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) </p>
