---
title: "upstart-socket-bridge(8)"
name: "upstart-socket-bridge"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upstart-socket-bridge/"
description: "upstart-socket-bridge – Bridge between Upstart and sockets"
---

<p>upstart-socket-bridge &#8211; Bridge between Upstart and sockets</p>
<h2>Synopsis</h2>
<p><code>upstart-socket-bridge</code> [<i>OPTIONS</i>]&#8230;</p>
<h2>Description</h2>
<p>The <code>upstart-socket-bridge</code> queries the Upstart <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon for all job configurations which <code>start on</code> or <code>stop on</code> the socket event. It then waits for an incoming connection on each specified <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) and when detected emits the socket event (<code>socket-event</code> (7)), setting a number of environment variables for the job to query.</p>
<h2>Author</h2>
<p>Written by Scott James Remnant &lt;<code>scott [at] netsplit.com</code>&gt; </p>
<p> Manual page written by James Hunt &lt;<code>james.hunt [at] ubuntu.com</code>&gt;</p>
<h2>Bugs</h2>
<p>Report bugs at &lt;<code><a rel="nofollow" href="https://launchpad.net/upstart/+bugs">https://launchpad.net/upstart/+bugs</a></code>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011 Canonical Ltd. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-init/">init</a></code>(5) <code><a href="/docs/linux/man/8-init/">init</a></code>(8) <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) <code><a href="/docs/linux/man/7-socket-event/">socket-event</a></code>(7) </p>
