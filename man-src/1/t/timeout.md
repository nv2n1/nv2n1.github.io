---
title: "timeout(1)"
name: "timeout"
section: "1"
letter: "t"
url: "/docs/linux/man/1-timeout/"
description: "timeout – run a command with a time limit"
---

<h2 class="name">NAME</h2>
<p> timeout &#8211; run a command with a time limit </p>
<h2>SYNOPSIS</h2>
<p> <code>timeout</code> [<i>,OPTION/</i>] <i>,DURATION COMMAND /</i>[<i>,ARG/</i>]&#8230;<br />
 <code>timeout</code> [<i>,OPTION/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Start COMMAND, and kill it if still running after DURATION. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt> <code>&#8211;preserve-status</code></p>
<dt>
<dd>
<dd>exit with the same status as COMMAND, even when the</p>
<dt>
<dd> command times out</p>
<dt> <code>&#8211;foreground</code></p>
<dt>
<dd>
<dd>when not running timeout directly from a shell prompt,</p>
<dt>
<dd> allow COMMAND to read from the TTY and get TTY signals; in this mode, children of COMMAND will not be timed out</p>
<dt> <code>-k</code>, <code>&#8211;kill-after</code>=<i>,DURATION/</i></p>
<dt>
<dd>
<dd>also send a KILL signal if COMMAND is still running</p>
<dt>
<dd> this long after the initial signal was sent</p>
<dt> <code>-s</code>, <code>&#8211;signal</code>=<i>,SIGNAL/</i></p>
<dt>
<dd>
<dd>specify the signal to be sent on timeout;</p>
<dt>
<dd> SIGNAL may be a name like &#8216;HUP&#8217; or a number; see &#8216;kill <code>-l</code>&#8216; for a list of signals</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> diagnose to stderr any signal sent upon timeout</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> DURATION is a floating point number with an optional suffix: &#8216;s&#8217; for seconds (the default), &#8216;m&#8217; for minutes, &#8216;h&#8217; for hours or &#8216;d&#8217; for days. A duration of 0 disables the associated timeout. </p>
<p> If the command times out, and <code>&#8211;preserve-status</code> is not set, then exit with status 124. Otherwise, exit with the status of COMMAND. If no signal is specified, send the TERM signal upon timeout. The TERM signal kills any process that does not block or catch that signal. It may be necessary to use the KILL (9) signal, since this signal cannot be caught, in which case the exit status is 128+9 rather than 124.</p>
<h2>BUGS</h2>
<p> Some platforms don&#8217;t currently support timeouts beyond the year 2038.</p>
<h2>AUTHOR</h2>
<p> Written by Padraig Brady.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-kill/">kill</a>(1) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/timeout">https://www.gnu.org/software/coreutils/timeout</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) timeout invocation&#8217; </p>
<h2>Index</h2>
