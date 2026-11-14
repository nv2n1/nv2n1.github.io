---
title: "atmarpd(8)"
name: "atmarpd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-atmarpd/"
description: "atmarpd – ATMARP demon"
---

<p>atmarpd &#8211; ATMARP demon</p>
<h2>Synopsis</h2>
<p><code>atmarpd</code> [<code>-b</code>] [<code>-d</code>] [<code>-D&nbsp;<wbr></code><i>directory</i>] [<code>-l&nbsp;<wbr></code><i>logfile</i>] [<code>-m</code>] [<code>-n</code>]<br />
 <code>atmarpd</code> <code>-V</code></p>
<h2>Description</h2>
<p><code>atmarpd</code> implements the ATMARP protocol as specified in RFC1577 and RFC1755. Address resolution requests are sent from the kernel (using a comparably simple protocol) to the ATMARP demon, which then performs the dialog with the network. </p>
<p> <code>atmarpd</code> can operate as an ATMARP client and as an ATMARP server. If also supports the concurrent use of several IP over ATM interfaces. </p>
<p> <code>atmarpd</code> is configured from the command line using the <code>atmarp</code> program. Unless debugging is enabled, the ATMARP table is written after every change to the file <code>/var/run/atmarpd.table</code> (or to a file with the same name in a different directory, if the <code>-D</code> option is used). </p>
<p> Note that <code>atmarpd</code> disables support for SVCs if signaling is not available at start time, i.e. if <code>atmsigd</code> is not running.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code></p>
<dd>Run in background (i.e. in a forked child process) after initializing.</p>
<dt><code>-d</code></p>
<dd>Enables (lots of) debugging output. By default, <code>atmarpd</code> is comparably quiet.</p>
<dt><code>-D&nbsp;<wbr></code><i>dump_dir</i></p>
<dd>Changes the directory where <code>atmarpd</code> writes its table (<code>atmarpd.table</code>). By default, <code>/var/run</code> is used.</p>
<dt><code>-l&nbsp;<wbr></code><i>logfile</i></p>
<dd>Write diagnostic messages to the specified file instead of to standard error. The special name <code>syslog</code> is used to send diagnostics to the system logger.</p>
<dt><code>-m</code></p>
<dd>Enables merging of incoming calls if the address is known. An incoming connection on which no InARP reply has been received yet, but which originates from an ATM address for which an ATMARP entry already exists, is automatically added to that entry. This assumes that there is a 1:1 mapping between IP addresses and ATMARP addresses. By default, this assumption is not made, which frequently results in the setup of duplicate connections. Note that RFC1577 requires that an ATMARP server sends an InARP request on an incoming connection. Merging may therefore violate RFC1577 in this case.</p>
<dt><code>-n</code></p>
<dd>Prints addresses in numeric format only, i.e. no address to name translation is attempted.</p>
<dt><code>-V</code></p>
<dd>Prints the version number of <code>atmarpd</code> on standard output and exits.</dl>
<h2>Files</h2>
<dl>
<dt><code>/var/run/atmarpd.table</code></p>
<dd>ATMARP table</p>
<dt><code>/proc/atm/arp</code></p>
<dd>table of currently active IP over ATM VCs</dl>
<h2>Bugs</h2>
<p><code>atmarpd</code> removes ATMARP entries from the kernel table while refreshing them.</p>
<h2>Author</h2>
<p>Werner Almesberger, EPFL ICA &lt;werner.almesberger [at] epfl.ch&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-atmarp/">atmarp</a>(8), <a href="/docs/linux/man/8-atmsigd/">atmsigd</a>(8) </p>
