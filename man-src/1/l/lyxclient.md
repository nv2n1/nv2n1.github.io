---
title: "lyxclient(1)"
name: "lyxclient"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lyxclient/"
description: "lyxclient – send commands to a running LyX editor"
---

<h2>NAME</h2>
<p> lyxclient &#8211; send commands to a running LyX editor</p>
<h2>SYNOPSIS</h2>
<p> <code>lyxclient</code> [ <i>options</i> ] </p>
<h2>DESCRIPTION</h2>
<p> When LyX starts, it creates a unique, per-process local socket in the temporary directory through which commands can be sent. That is, it can act like a server, accepting connections from clients. <code>lyxclient</code> can be used as such client. <code>lyxclient</code> will take care of all connection and communication protocol details, leaving you (or your app) free to concentrate on what you want to send to LyX.</p>
<h2>SERVER IDENTIFICATION OPTIONS</h2>
<p> <code>lyxclient</code> must first identify to which server (i.e. a running LyX) commands are to be sent. The following options are used to specify the server.</p>
<dl>
<dt>
<dt><code>-p</code><i> pid</i></p>
<dd>
<dd> specify the <i>pid</i> of the running LyX process to which <code>lyxclient</code> should send commands.</p>
<dt><code>-a</code><i> socket_address</i></p>
<dd> specify explicitly which socket special file should be used. These special files are located inside lyx_tmpdir&lt;lyx_pid&gt;&lt;hash&gt;, in the temporary directory. There is one per running LyX process.</p>
<dt><code>-t</code><i> tmp_dir</i></p>
<dd> if LyX is configured to use a temporary directory other than /tmp, you must inform <code>lyxclient</code> of this.</dl>
<p> If neither <code>-a</code> nor <code>-p</code> are invoked, <code>lyxclient</code> will search for sockets in /tmp (or <i>tmp_dir</i> if the <code>-t</code> option is used) and use the first socket to which it can connect. This is safe if you are running only one LyX process at any one time.</p>
<h2>COMMAND MODE OPTIONS</h2>
<p> <code>lyxclient</code> can send commands to LyX from both the command-line and from standard input. LyX commands documentation can be found in LyX Help menu.</p>
<dl>
<dt><code>-c</code><i> command</i></p>
<dd> send a single <i>command</i>, print LyX information to standard output and exit. LYXCMD prefix is needed in the given command.</p>
<dt><code>-g</code><i> file line</i></p>
<dd> this is simply a wrapper for the command &#8216;server-goto-file-row <i>file</i> <i>line</i>&#8216;. It is used by the DVI previewer to elicit inverse DVI search.</dl>
<p> If neither <code>-c</code> nor <code>-g</code> are used, <code>lyxclient</code> will regard any standard input as commands to be sent to LyX, printing LyX&#8217;s responses to standard output. Commands are separated by newlines (the &#8216;
&#8217; character). To finish communication and terminate the <code>lyxclient</code> process, send the command &#8216;BYE:&#8217;.</p>
<h2>MISCELANEOUS OPTIONS</h2>
<dl>
<dt><code>-n</code><i> name</i></p>
<dd> when starting communication, <code>lyxclient</code> sends an idenfifier string to LyX. By default, this string is &quot;PPID&gt;PID&quot;, where PPID is <code>lyxclient</code>&#8216;s parent pid and pid is <code>lyxclient</code>&#8216;s pid. Use this option to override this default.</p>
<dt><code>-h</code></p>
<dd> print the <code>lyxclient</code> version and summarize its usage.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>LYXSOCKET</code></p>
<dd> can be used to specify the socket special file that must be used. LyX sets this variable. It is overridden by the <code>-a</code> option.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-lyx/">lyx</a>(1), <a href="/docs/linux/man/1-xdvi/">xdvi</a>(1), LFUNs.lyx.</p>
<h2>AUTHORS</h2>
<p> Jo&atilde;o Luis M. Assirati &lt;assirati [at] fma.if.usp.br&gt; is the principal author of lyxclient. </p>
<h2>Index</h2>
