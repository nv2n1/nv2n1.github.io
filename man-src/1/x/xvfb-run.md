---
title: "xvfb-run(1)"
name: "xvfb-run"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xvfb-run/"
description: "xvfb-run – run specified X client or command in a virtual X server environment"
---

<h2 class="name">NAME</h2>
<p> xvfb-run &#8211; run specified X client or command in a virtual X server environment </p>
<h2>SYNOPSIS</h2>
<p> <code>xvfb-run</code> [ <i>options</i> ] <i>command</i></p>
<h2>DESCRIPTION</h2>
<p> <code>xvfb-run</code> is a wrapper for the <code><a href="//www.systutorials.com/docs/linux/man/1x-Xvfb/">Xvfb</a></code>(1x) command which simplifies the task of running commands (typically an X client, or a script containing a list of clients to be run) within a virtual X server environment. </p>
<p> <code>xvfb-run</code> sets up an X authority file (or uses an existing user-specified one), writes a cookie to it (see <code><a href="//www.systutorials.com/docs/linux/man/1x-xauth/">xauth</a></code>(1x)) and then starts the <code>Xvfb</code> X server as a background process. The process ID of <code>Xvfb</code> is stored for later use. The specified <i>command</i> is then run using the X display corresponding to the <code>Xvfb</code> server just started and the X authority file created earlier. </p>
<p> When the <i>command</i> exits, its status is saved, the <code>Xvfb</code> server is killed (using the process ID stored earlier), the X authority cookie removed, and the authority file deleted (if the user did not specify one to use). <code>xvfb-run</code> then exits with the exit status of <i>command</i>, except in error conditions (see <font SIZE="-1"><code>EXIT STATUS</code> </font> below). </p>
<p> <code>xvfb-run</code> requires the <code>xauth</code> command to function.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>,<code> &#8211;auto-servernum</code></p>
<dd> Try to get a free server number, starting at 99, or the argument to <code>&#8211;server-num</code>.</p>
<dt><code>-e&nbsp;<wbr></code><i>file</i>,<code>&nbsp;<wbr>&#8211;error-file=</code><i>file</i></p>
<dd> Store output from <code>xauth</code> and <code>Xvfb</code> in <i>file</i>. The default is <i>/dev/null</i>.</p>
<dt><code>-f&nbsp;<wbr></code><i>file</i>,<code>&nbsp;<wbr>&#8211;auth-file=</code><i>file</i></p>
<dd> Store X authentication data in <i>file</i>. By default, a temporary directory called <i>xvfb-run.</i>PID (where PID is the process ID of <code>xvfb-run</code> itself) is created in the directory specified by the environment variable <code>TMPDIR</code> (or <i>/tmp</i> if that variable is null or unset), and the <code><a href="/docs/linux/man/1-tempfile/">tempfile</a></code>(1) command is used to create a file in that temporary directory called <i>Xauthority</i>.</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Display a usage message and exit.</p>
<dt><code>-n&nbsp;<wbr></code><i>servernumber</i>,<code>&nbsp;<wbr>&#8211;server-num=</code><i>servernumber</i></p>
<dd> Use <i>servernumber</i> as the server number (but see the <code>-a</code>,<code> &#8211;auto-servernum</code> option above). The default is 99.</p>
<dt><code>-l</code>,<code> &#8211;listen-tcp</code></p>
<dd> Enable TCP port listening in the X server. For security reasons (to avoid denial-of-service attacks or exploits), TCP port listening is disabled by default.</p>
<dt><code>-p&nbsp;<wbr></code><i>protocolname</i>,<code>&nbsp;<wbr>&#8211;xauth-protocol=</code><i>protocolname</i></p>
<dd> Use <i>protocolname</i> as the X authority protocol to use. The default is &#8216;.&#8217;, which <code>xauth</code> interprets as its own default protocol, which is MIT-MAGIC-COOKIE-1.</p>
<dt><code>-s&nbsp;<wbr></code><i>arguments</i>,<code>&nbsp;<wbr>&#8211;server-args=</code><i>arguments</i></p>
<dd> Pass <i>arguments</i> to the <code>Xvfb</code> server. Be careful to quote any whitespace characters that may occur within <i>arguments</i> to prevent them from regarded as separators for <code>xvfb-run</code>&#8216;s own arguments. Also, note that specification of &#8216;-nolisten tcp&#8217; in <i>arguments</i> may override the function of <code>xvfb-run</code>&#8216;s own <code>-l</code>,<code> &#8211;listen-tcp</code> option, and that specification of the server number (e.g., &#8216;:1&#8217;) may be ignored because of the way the X server parses its argument list. Use the <code>xvfb-run</code> option <code>-n&nbsp;<wbr></code><i>servernumber</i>,<code>&nbsp;<wbr>&#8211;server-num=</code><i>servernumber</i> to achieve the latter function. The default is &#8216;-screen 0 640x480x8&#8217;.</p>
<dt><code>-w&nbsp;<wbr></code><i>delay</i>,<code>&nbsp;<wbr>&#8211;wait=</code><i>delay</i></p>
<dd> Ignored for compatibility with earlier versions.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>COLUMNS</code></p>
<dd> indicates the width of the terminal device in character cells. This value is used for formatting diagnostic messages. If not set, the terminal is queried using <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1) to determine its width. If that fails, a value of &#8217;80&#8217; is assumed.</p>
<dt><code>TMPDIR</code></p>
<dd> specifies the directory in which to place <code>xvfb-run</code>&#8216;s temporary directory for storage of the X authority file; only used if the <code>-f</code> or <code>&#8211;auth-file</code> options are not specified.</dl>
<h2>OUTPUT FILES</h2>
<p> Unless the <code>-f</code> or <code>&#8211;auth-file</code> options are specified, a temporary directory and file within it are created (and deleted) to store the X authority cookies used by the <code>Xvfb</code> server and client(s) run under it. See <code><a href="/docs/linux/man/1-tempfile/">tempfile</a></code>(1). If -f or &#8211;auth-file are used, then the specified X authority file is only written to, not created or deleted (though <code>xauth</code> creates an authority file itself if told to use use that does not already exist). </p>
<p> An error file with a user-specified name is also created if the <code>-e</code> or <code>&#8211;error-file</code> options are specifed; see above.</p>
<h2>EXIT STATUS</h2>
<p> <code>xvfb-run</code> uses its exit status as well as output to standard error to communicate diagnostics.</p>
<dl>
<dt>0</p>
<dd> <code>xvfb-run</code> only uses this exit status if the <code>-h</code>,<code> &#8211;help</code> option is given. In all other situations, this may be interpreted as success of the specified command.</p>
<dt>1</p>
<dd> <code>Xvfb</code> did not start correctly.</p>
<dt>2</p>
<dd> No command to run was specified.</p>
<dt>3</p>
<dd> The <code>xauth</code> command is not available.</p>
<dt>4</p>
<dd> The temporary directory that was going to be used already exists; since <code>xvfb-run</code> produces a uniquely named directory, this may indicate an attempt by another process on the system to exploit a temporary file race condition.</p>
<dt>5</p>
<dd> A problem was encountered while cleaning up the temporary directory.</p>
<dt>6</p>
<dd> A problem was encountered while using <code><a href="/docs/linux/man/1-getopt/">getopt</a></code>(1) to parse the command-line arguments.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>xvfb-run &#8211;auto-servernum &#8211;server-num=1 xlogo</code></p>
<dd> runs the <code><a href="//www.systutorials.com/docs/linux/man/1x-xlogo/">xlogo</a></code>(1x) demonstration client inside the <code>Xvfb</code> X server on the first available server number greater than or equal to 1.</p>
<dt><code>xvfb-run &#8211;server-args=-screen 0 1024x768x24 ico -faces</code></p>
<dd> runs the <code><a href="//www.systutorials.com/docs/linux/man/1x-ico/">ico</a></code>(1x) demonstration client (and passes it the <code>-faces</code> argument) inside the <code>Xvfb</code> X server, configured with a root window of 1024 by 768 pixels and a color depth of 24 bits.</dl>
<p> Note that the demo X clients used in the above examples will not exit on their own, so they will have to be killed before <code>xvfb-run</code> will exit.</p>
<h2>BUGS</h2>
<p> See the Debian Bug Tracking System &lt;URL: <a rel="nofollow" href="http://bugs.debian.org/xvfb">http://bugs.debian.org/xvfb</a> &gt;. If you wish to report a bug in <code>xvfb-run</code>, please use the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>AUTHOR</h2>
<p> <code>xvfb-run</code> was written by Branden Robinson and Jeff Licquia with sponsorship from Progeny Linux Systems.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="//www.systutorials.com/docs/linux/man/1x-Xvfb/">Xvfb</a></code>(1x), <code><a href="//www.systutorials.com/docs/linux/man/1x-xauth/">xauth</a></code>(1x) </p>
<h2>Index</h2>
