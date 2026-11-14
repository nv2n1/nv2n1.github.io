---
title: "emacsclient(1)"
name: "emacsclient"
section: "1"
letter: "e"
url: "/docs/linux/man/1-emacsclient/"
description: "emacsclient – tells a running Emacs to visit a file"
---

<h2 class="name">NAME</h2>
<p> emacsclient &#8211; tells a running Emacs to visit a file </p>
<h2>SYNOPSIS</h2>
<p> <code>emacsclient</code> <i>[options] files &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>emacsclient</code> command. Full documentation is available in the GNU Info format; see below. This manual page was originally written for the Debian GNU/Linux distribution, but is not specific to that system. </p>
<p> <code>emacsclient</code> works in conjunction with the built-in Emacs server. </p>
<p> You can either call <code>emacsclient</code> directly or let other programs run it for you when necessary. On GNU and Unix systems many programs consult the environment variable EDITOR (sometimes also VISUAL) to obtain the command used for editing. Thus, setting this environment variable to &#8217;emacsclient&#8217; will allow these programs to use an already running Emacs for editing. Other operating systems might have their own methods for defining the default editor. </p>
<p> For <code>emacsclient</code> to work, you need an already running Emacs with a server. Within Emacs, call the functions &quot;server-start&quot; or &quot;server-mode&quot;. (Your &quot;.emacs&quot; file can do this automatically if you add either &quot;(server-start)&quot; or &quot;(server-mode 1)&quot; to it.) </p>
<p> When you&#8217;ve finished editing the buffer, type &quot;C-x #&quot; (&quot;server-edit&quot;). This saves the file and sends a message back to the <code>emacsclient</code> program telling it to exit. The programs that use EDITOR wait for the &quot;editor&quot; (actually, <code>emacsclient</code>) to exit. &quot;C-x #&quot; also checks for other pending external requests to edit various files, and selects the next such file. </p>
<p> If you set the variable &quot;server-window&quot; to a window or a frame, &quot;C-x #&quot; displays the server buffer in that window or in that frame. </p>
<h2>OPTIONS</h2>
<p> Most options follow the usual GNU command line syntax, with long options starting with two dashes (&quot;-&quot;).</p>
<dl>
<dt><code>+</code><i>line</i>[<code>:</code>column]</p>
<dd> Go to the specified <i>line</i> and <i>column</i>. A missing <i>column</i> is treated as column 1. This option applies only to the next file specified.</p>
<dt><code>-a, &#8211;alternate-editor=COMMAND</code></p>
<dd> if the Emacs server is not running, run the specified shell command instead. This can also be specified via the ALTERNATE_EDITOR environment variable. If the value of ALTERNATE_EDITOR is the empty string, run &quot;emacs &#8211;daemon&quot; to start Emacs in daemon mode, and try to connect to it.</p>
<dt><code>-c, &#8211;create-frame</code></p>
<dd> create a new frame instead of trying to use the current Emacs frame</p>
<dt><code>-F, &#8211;frame-parameters=ALIST</code></p>
<dd> set the parameters of a newly-created frame.</p>
<dt><code>-d, &#8211;display=DISPLAY</code></p>
<dd> tell the server to display the files on the given display.</p>
<dt><code>-e, &#8211;eval</code></p>
<dd> do not visit files but instead evaluate the arguments as Emacs Lisp expressions.</p>
<dt><code>-f, &#8211;server-file=FILENAME</code></p>
<dd> use TCP configuration file FILENAME for communication. This can also be specified via the EMACS_SERVER_FILE environment variable.</p>
<dt><code>-n, &#8211;no-wait</code></p>
<dd> returns immediately without waiting for you to &quot;finish&quot; the buffer in Emacs.</p>
<dt><code>-nw, -t, &#8211;tty</code></p>
<dd> open a new Emacs frame on the current terminal</p>
<dt><code>-s, &#8211;socket-name=FILENAME</code></p>
<dd> use socket named FILENAME for communication.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> print version information and exit</p>
<dt><code>-H, &#8211;help</code></p>
<dd> print this usage information message and exit</dl>
<h2>EXIT STATUS</h2>
<p> Normally, the exit status is 0. If emacsclient shuts down due to Emacs signaling an error, the exit status is 1.</p>
<h2>SEE ALSO</h2>
<p> The program is documented fully in <i>Using Emacs as a Server</i> available via the Info system.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Stephane Bortzmeyer &lt;bortzmeyer [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others).</p>
<h2>COPYING</h2>
<p> This manual page is in the public domain. </p>
<h2>Index</h2>
