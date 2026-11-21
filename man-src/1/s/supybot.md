---

title: "supybot(1)"
name: "supybot"
section: "1"
letter: "s"
url: "/docs/linux/man/1-supybot/"
description: "supybot – A robust and user friendly Python IRC bot"
---

<p> supybot &#8211; A robust and user friendly Python IRC bot</p>
<h2>SYNOPSIS</h2>
<p> <code>supybot</code> [<i>options</i>]<i> configFile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Supybot</code> is a robust, user-friendly, and programmer-friendly Python IRC bot. It aims to be an adequate replacement for most existing IRC bots. It includes a very flexible and powerful ACL system for controlling access to commands, as well as more than 50 builtin plugins providing around 400 actual commands.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> Show version of program.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>-P</code>, <code>&#8211;profile</code></dt>
<dd> Enable profiling.</dd>
<dt><code>-n</code><i> NICK</i>, &#8211;nick=<i>NICK</i></dt>
<dd> Nick the bot should use.</dd>
<dt><code>-u</code><i> USER</i>, &#8211;user=<i>USER</i></dt>
<dd> Full username the bot should use.</dd>
<dt><code>-i</code><i> IDENT</i>, &#8211;ident=<i>IDENT</i></dt>
<dd> Ident the bot should use.</dd>
<dt><code>-d</code>, <code>&#8211;daemon</code></dt>
<dd> Determines whether the bot will daemonize. This is a no-op on non-POSIX systems.</dd>
<dt><code>&#8211;allow-default-owner</code></dt>
<dd> Determines whether the bot will allow its defaultCapabilities not to include &quot;-owner&quot;, thus giving all users the owner capability by default. This is dumb, hence we require a command-line option to enable it.</dd>
<dt><code>&#8211;allow-root</code></dt>
<dd> Determines whether the bot will be allowed to run as root. You do not want this. Do not do it. Even if you think you want it, you do not.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Determines whether some extra debugging stuff will be logged by this script.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-python/">python</a></i>(1), <i><a href="/docs/linux/man/1-supybot-test/">supybot-test</a></i>(1), <i><a href="/docs/linux/man/1-supybot-botchk/">supybot-botchk</a></i>(1), <i><a href="/docs/linux/man/1-supybot-wizard/">supybot-wizard</a></i>(1), <i><a href="/docs/linux/man/1-supybot-adduser/">supybot-adduser</a></i>(1), <i><a href="/docs/linux/man/1-supybot-plugin-doc/">supybot-plugin-doc</a></i>(1), <i><a href="/docs/linux/man/1-supybot-plugin-create/">supybot-plugin-create</a></i>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by James McCoy &lt;vega dot james at gmail dot com&gt;. Permission is granted to copy, distribute and/or modify this document under the terms of the Supybot license, a BSD-style license. </p>
