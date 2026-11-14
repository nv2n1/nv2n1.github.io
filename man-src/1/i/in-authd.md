---
title: "in-authd(1)"
name: "in-authd"
section: "1"
letter: "i"
url: "/docs/linux/man/1-in-authd/"
description: "in.authd – manual page for in.authd authd-1.4.3:"
---

<p>in.authd &#8211; manual page for in.authd authd-1.4.3:</p>
<h2>Description</h2>
<p>in.authd [options]&#8230; [request]&#8230;</p>
<dl>
<dt><code>-d</code></p>
<dd>Output debug messages</p>
<dt><code>-E[cipher]</code></p>
<dd>Encrypt username using [AES-128-CBC]</p>
<dt><code>-e</code></p>
<dd>Send UNKNOWN-ERROR for common error messages</p>
<dt><code>-l[mask]</code></p>
<dd>Log to syslog, [mask] for priority levels</p>
<dt><code>-m[reps]</code></p>
<dd>Allow at most [unlimited] requests/connection</p>
<dt><code>-N[basename]</code></p>
<dd>Hide users with ~/[.noident] file</p>
<dt><code>-n</code></p>
<dd>Send uid number instead of username</p>
<dt><code>-o</code></p>
<dd>Send OTHER instead of the operating system</p>
<dt><code>-t[secs]</code></p>
<dd>Timeout request after [60] seconds</p>
<dt><code>-V</code></p>
<dd>Print program and version information</p>
<dt><code>&#8211;abrupt</code></p>
<dd>Disconnect without displaying error msgs</p>
<dt><code>&#8211;codeset</code>=<i>rfc1340</i></p>
<dd>Send [charset] if reply is not ASCII</p>
<dt><code>&#8211;fn</code>[=<i>fields</i>]</p>
<dd>Use [all] gecos fields instead of username</p>
<dt><code>&#8211;hybrid</code></p>
<dd>Use hybrid notation (ex. ::127.0.0.1) for IPv6</p>
<dt><code>&#8211;ident</code>[=<i>basename</i>]</p>
<dd>Hide users with no ~/[.ident]</p>
<dt><code>&#8211;lang</code>=<i>lc</i></p>
<dd>Localize messages, charsets, &amp; time to [locale]</p>
<dt><code>&#8211;mapped</code>=<i>ipv6</i></p>
<dd>Map addresses with same top 96 bits to IPv4</p>
<dt><code>&#8211;os</code>[=<i>rfc1340</i>]</p>
<dd>Use [uname], not UNIX, as OS name</p>
<dt><code>&#8211;passwd</code>=<i>pathname</i></p>
<dd>Use line 1 of [/etc/ident.key] for crypto</p>
<dt><code>&#8211;resolve</code></p>
<dd>Use host and service names if available</p>
<dt><code>&#8211;username</code>[=<i>login</i>]</p>
<dd>Use [nobody] as username</p>
<dt><code>&#8211;verbose</code></p>
<dd>Add real uid, addresses/ports, &amp; timestamps</p>
<dt><code>&#8211;xerror</code></p>
<dd>Send more helpful error messages for rare errors</p>
<dd>$Revision: 1.18 $ $Date: 2004/07/28 16:04:05 $ <a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a> </p>
</dl>
