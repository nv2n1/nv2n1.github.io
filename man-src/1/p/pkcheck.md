---
title: "pkcheck(1)"
name: "pkcheck"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkcheck/"
description: "pkcheck – Check whether a process is authorized"
---

<h2 class="name">NAME</h2>
<p> pkcheck &#8211; Check whether a process is authorized </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pkcheck</code> [<code>&#8211;version</code>] [<code>&#8211;help</code>]</p>
<dt> <code>pkcheck</code> [<code>&#8211;list-temp</code>]</p>
<dt> <code>pkcheck</code> [<code>&#8211;revoke-temp</code>]</p>
<dt> <code>pkcheck</code> <code>&#8211;action-id</code>&nbsp;<i>action</i> {<code>&#8211;process</code>&nbsp;{&nbsp;<i>pid</i>&nbsp;|&nbsp;<i>pid,pid-start-time</i>&nbsp;|&nbsp;<i>pid,pid-start-time,uid</i>&nbsp;} | <code>&#8211;system-bus-name</code>&nbsp;<i>busname</i>} [<code>&#8211;allow-user-interaction</code>] [<code>&#8211;enable-internal-agent</code>] [<code>&#8211;detail</code>&nbsp;<i>key</i>&nbsp;<i>value</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>pkcheck</code></p>
<dd>is used to check whether a process, specified by either <code>&#8211;process</code> (see below) or <code>&#8211;system-bus-name</code>, is authorized for <i>action</i>. The <code>&#8211;detail</code> option can be used zero or more times to pass details about <i>action</i>. If <code>&#8211;allow-user-interaction</code> is passed, <code>pkcheck</code> blocks while waiting for authentication. </p>
<p> The invocation <code>pkcheck &#8211;list-temp</code> will list all temporary authorizations for the current session and <code>pkcheck &#8211;revoke-temp</code> will revoke all temporary authorizations for the current session. </p>
<p> This command is a simple wrapper around the PolicyKit D-Bus interface; see the D-Bus interface documentation for details.</p>
<h2>RETURN VALUE</h2>
<p> If the specified process is authorized, <code>pkcheck</code> exits with a return value of 0. If the authorization result contains any details, these are printed on standard output as key/value pairs using environment style reporting, e.g. first the key followed by a an equal sign, then the value followed by a newline. </p>
<dl>
<dt>
<dd>
<pre>
KEY1=VALUE1
KEY2=VALUE2
KEY3=VALUE3
...
</pre>
</dl>
<p> Octects that are not in [a-zA-Z0-9_] are escaped using octal codes prefixed with <i>\</i>. For example, the UTF-8 string <i>føl,你好</i> will be printed as <i>f\303\270l\54\344\275\240\345\245\275</i>. </p>
<p> If the specificied process is not authorized, <code>pkcheck</code> exits with a return value of 1 and a diagnostic message is printed on standard error. Details are printed on standard output. </p>
<p> If the specificied process is not authorized because no suitable authentication agent is available or if the <code>&#8211;allow-user-interaction</code> wasn&#8217;t passed, <code>pkcheck</code> exits with a return value of 2 and a diagnostic message is printed on standard error. Details are printed on standard output. </p>
<p> If the specificied process is not authorized because the authentication dialog / request was dismissed by the user, <code>pkcheck</code> exits with a return value of 3 and a diagnostic message is printed on standard error. Details are printed on standard output. </p>
<p> If an error occured while checking for authorization, <code>pkcheck</code> exits with a return value of 127 with a diagnostic message printed on standard error. </p>
<p> If one or more of the options passed are malformed, <code>pkcheck</code> exits with a return value of 126. If stdin is a tty, then this manual page is also shown.</p>
<h2>NOTES</h2>
<p> Do not use either the bare <i>pid</i> or <i>pid,start-time</i> syntax forms for <code>&#8211;process</code>. There are race conditions in both. New code should always use <i>pid,pid-start-time,uid</i>. The value of <i>start-time</i> can be determined by consulting e.g. the <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) file system depending on the operating system. If fewer than 3 arguments are passed, <code>pkcheck</code> will attempt to look up them up internally, but note that this may be racy. </p>
<p> If your program is a daemon with e.g. a custom Unix domain socket, you should determine the <i>uid</i> parameter via operating system mechanisms such as PEERCRED.</p>
<h2>AUTHENTICATION AGENT</h2>
<p> <code>pkcheck</code>, like any other PolicyKit application, will use the authentication agent registered for the process in question. However, if no authentication agent is available, then <code>pkcheck</code> can register its own textual authentication agent if the option <code>&#8211;enable-internal-agent</code> is passed.</p>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen &lt;davidz [at] redhat.com&gt; with a lot of help from many others.</p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution or the polkit-devel mailing list, see the link m[blue]<code><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/polkit-devel">http://lists.freedesktop.org/mailman/listinfo/polkit-devel</a></code>m[] on how to subscribe.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8), <code><a href="/docs/linux/man/1-pkaction/">pkaction</a></code>(1), <code><a href="/docs/linux/man/1-pkexec/">pkexec</a></code>(1), <code><a href="/docs/linux/man/1-pkttyagent/">pkttyagent</a></code>(1) </p>
<h2>Index</h2>
