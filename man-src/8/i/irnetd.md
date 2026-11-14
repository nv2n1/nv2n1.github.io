---
title: "irnetd(8)"
name: "irnetd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-irnetd/"
description: "irnetd – Handle automatically incoming IrNET connections"
---

<p>irnetd &#8211; Handle automatically incoming IrNET connections</p>
<h2>Synopsis</h2>
<p><code>irnetd [</code><i>ppp-options</i><code>]</code></p>
<h2>Description</h2>
<p><code>Irnetd</code> is a very simple daemon automatically handling <i>incoming IrNET connections</i>. Every time a peer attempt to connect to the local computer, <code>irnetd</code> generates the relevant <i><a href="/docs/linux/man/8-pppd/">pppd</a></i>(8) command to starts an IrNET server handling this peer.</p>
<h2>Parameters</h2>
<dl>
<dt><i>ppp-options</i></p>
<dd>Override the default <i><a href="/docs/linux/man/8-pppd/">pppd</a></i>(8) options. These options will just be passed on the command line of <i><a href="/docs/linux/man/8-pppd/">pppd</a></i>(8). The default options are <i>noauth nolock connect-delay 0 idle 10</i> which should fit most usages.</dl>
<h2>Author</h2>
<p>Jean Tourrilhes &#8211; jt [at] hpl.hp.com</p>
<h2>Files</h2>
<p><i>/dev/irnet</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-irda/">irda</a></code>(7), <code><a href="/docs/linux/man/4-irnet/">irnet</a></code>(4), <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8), <code><a href="/docs/linux/man/8-irattach/">irattach</a></code>(8), <code><a href="/docs/linux/man/8-irdadump/">irdadump</a></code>(8). </p>
