---
title: "pkttyagent(1)"
name: "pkttyagent"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkttyagent/"
description: "pkttyagent – Textual authentication helper"
---

<h2 class="name">NAME</h2>
<p> pkttyagent &#8211; Textual authentication helper </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pkttyagent</code> [<code>&#8211;version</code>] [<code>&#8211;help</code>]</p>
<dt> <code>pkttyagent</code> [<code>&#8211;process</code>&nbsp;{&nbsp;<i>pid</i>&nbsp;|&nbsp;<i>pid,pid-start-time</i>&nbsp;} | <code>&#8211;system-bus-name</code>&nbsp;<i>busname</i>] [<code>&#8211;notify-fd</code>&nbsp;<i>fd</i>] [<code>&#8211;fallback</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>pkttyagent</code></p>
<dd>is used to start a textual authentication agent for the subject specified by either <code>&#8211;process</code> or <code>&#8211;system-bus-name</code>. If neither of these options are given, the parent process is used. </p>
<p> To get notified when the authentication agent has been registered either listen to the Changed D-Bus signal or use <code>&#8211;notify-fd</code> to pass the number of a file descriptor that has been passed to the program. This file descriptor will then be closed when the authentication agent has been successfully registered. </p>
<p> If <code>&#8211;fallback</code> is used, the textual authentication agent will not replace an existing authentication agent.</p>
<h2>RETURN VALUE</h2>
<p> If the authentication agent could not be registered, <code>pkttyagent</code> exits with an exit code of 127. Diagnostic messages are printed on standard error. </p>
<p> If one or more of the options passed are malformed, <code>pkttyagent</code> exits with an exit code of 126. If stdin is a tty, then this manual page is also shown. </p>
<p> If the authentication agent was successfully registered, <code>pkttyagent</code> will keep running, interacting with the user as needed. When its services are no longer needed, the process can be killed.</p>
<h2>NOTES</h2>
<p> Since process identifiers can be recycled, the caller should always use <i>pid,pid-start-time</i> when using the <code>&#8211;process</code> option. The value of <i>pid-start-time</i> can be determined by consulting e.g. the <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) file system depending on the operating system. If only <i>pid</i> is passed to the <code>&#8211;process</code> option, then <code>pkttyagent</code> will look up the start time itself but note that this may be racy.</p>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen &lt;davidz [at] redhat.com&gt; with a lot of help from many others.</p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution or the polkit-devel mailing list, see the link m[blue]<code><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/polkit-devel">http://lists.freedesktop.org/mailman/listinfo/polkit-devel</a></code>m[] on how to subscribe.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8), <code><a href="/docs/linux/man/1-pkaction/">pkaction</a></code>(1), <code><a href="/docs/linux/man/1-pkcheck/">pkcheck</a></code>(1), <code><a href="/docs/linux/man/1-pkexec/">pkexec</a></code>(1) </p>
<h2>Index</h2>
