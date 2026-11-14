---
title: "lspcmcia(8)"
name: "lspcmcia"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lspcmcia/"
description: "pccardctl – PCMCIA card control utility lspcmcia – display extended PCMCIA debugging information"
---

<p>pccardctl &#8211; PCMCIA card control utility<br />
 lspcmcia &#8211; display extended PCMCIA debugging information</p>
<h2>Synopsis</h2>
<p><code>pccardctl</code> [<code>-V</code>] [<code>-v &#8230;</code>] <i>command</i> [<i>socket</i>]<br />
 <code>lspcmcia</code> [<code>-V</code>] [<code>-v &#8230;</code>] [<i>socket</i>] </p>
<h2>Description</h2>
<p><code>pccardctl</code> is used to monitor and control the state of PCMCIA sockets. If a socket number is specified, the command will be applied to just one socket; otherwise, all sockets will be affected. If <code>pccardctl</code> is executed by root, all commands are available. If it is executed by an unpriviledged user, only the informational commands are accessible. <code>lspcmcia</code> is an alias for <code>pccardctl ls</code>, provided for convenience. </p>
<h2>Commands</h2>
<dl>
<dt><code>status</code></p>
<dd>Display the current socket status flags.</p>
<dt><code>config</code></p>
<dd>Display the socket configuration, including power settings, interrupt and I/O window settings, and configuration registers. &#8211;not yet implemented</p>
<dt><code>ident</code></p>
<dd>Display card identification information, including product identification strings, manufacturer ID codes, and function ID codes. Not yet implemented for cardbus cards. Use lspci instead.</p>
<dt><code>info</code></p>
<dd>Much like the <code>ident</code> command, but its output is formatted as a series of Bourne-stype shell variable definitions for use in scripts. Not yet implemented for cardbus cards.</p>
<dt><code>ls</code></p>
<dd>Display extended debugging information about the PCMCIA sockets and devices present in the system.</p>
<dt><code>suspend</code></p>
<dd>Shut down and then disable power for a socket.</p>
<dt><code>resume</code></p>
<dd>Restore power to a socket, and re-configure for use.</p>
<dt>
<dt><code>eject</code></p>
<dd>
<dd>Notify all client drivers that this card will be ejected, then cut power to the socket.</p>
<dt><code>insert</code></p>
<dd>Notify all client drivers that this card has just been inserted. </p>
</dl>
<h2>Options</h2>
<dl>
<dt><code>-V</code></p>
<dd>Show version information and exit.</p>
<dt><code>-v</code></p>
<dd>Increase the verbosity of the <code>ls</code> command. Giving this option twice increases verbosity further. </p>
</dl>
<h2>Author</h2>
<p>Daniel Ritz &#8211; daniel.ritz [at] gmx.ch<br />
 based upon the original cardctl man page by<br />
 David Hinds &#8211; dahinds [at] users.sourceforge.net</p>
