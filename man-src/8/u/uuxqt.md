---
title: "uuxqt(8)"
name: "uuxqt"
section: "8"
letter: "u"
url: "/docs/linux/man/8-uuxqt/"
description: "uuxqt – UUCP execution daemon"
---

<p>uuxqt &#8211; UUCP execution daemon</p>
<h2>Synopsis</h2>
<p><code>uuxqt</code> [ options ]</p>
<h2>Description</h2>
<p>The <i>uuxqt</i> daemon executes commands requested by <i>uux</i> (1) from either the local system or from remote systems. It is started automatically by the <i>uucico</i> (8) daemon (unless <i>uucico</i> (8) is given the <code>-q</code> or <code>&#8211;nouuxqt</code> option). </p>
<p> There is normally no need to run this command, since it will be invoked by <i>uucico</i> (8). However, it can be used to provide greater control over the processing of the work queue. </p>
<p> Multiple invocations of <i>uuxqt</i> may be run at once, as controlled by the <i>max-uuxqts</i> configuration command.</p>
<h2>Options</h2>
<p>The following options may be given to <i>uuxqt.</i></p>
<dl>
<dt><code>-c command, &#8211;command command</code></p>
<dd>Only execute requests for the specified command. For example: </p>
<pre>uuxqt --command rmail</pre>
<dt><code>-s system, &#8211;system system</code></p>
<dd>Only execute requests originating from the specified system.</p>
<dt><code>-x type, &#8211;debug type</code></p>
<dd>Turn on particular debugging types. The following types are recognized: abnormal, chat, handshake, uucp-proto, proto, port, config, spooldir, execute, incoming, outgoing. Only abnormal, config, spooldir and execute are meaningful for <i>uuxqt.</i> </p>
<p> Multiple types may be given, separated by commas, and the <code>&#8211;debug</code> option may appear multiple times. A number may also be given, which will turn on that many types from the foregoing list; for example, <code>&#8211;debug 2</code> is equivalent to <code>&#8211;debug abnormal,chat.</code> </p>
<p> The debugging output is sent to the debugging file, which may be printed using <i>uulog -D.</i></p>
<dt><code>-I file, &#8211;config </code></p>
<dd>Set configuration file to use. This option may not be available, depending upon how <i>uuxqt</i> was compiled.</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Report version information and exit.</p>
<dt><code>&#8211;help</code></p>
<dd>Print a help message and exit.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-uucp/">uucp</a>(1), <a href="/docs/linux/man/1-uux/">uux</a>(1), <a href="/docs/linux/man/8-uucico/">uucico</a>(8)</p>
<h2>Author</h2>
<p>Ian Lance Taylor (ian [at] airs.com)</p>
