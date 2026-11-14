---
title: "ipsec_addconn(8)"
name: "ipsec_addconn"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_addconn/"
description: "ipsec_addconn – load a given policy into the pluto IKE daemon"
---

<p>ipsec_addconn &#8211; load a given policy into the pluto IKE daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>addconn</i> &#8211;configsetup [&#8211;rootdir&nbsp;<wbr><i>dir</i>] [&#8211;config&nbsp;<wbr><i>filename</i>] [&#8211;ctlbase&nbsp;<wbr><i>socketfile</i>] [&#8211;verbose] [&#8211;noexport] [&#8211;warningsfatal]</p>
<dt> <code>ipsec</code> <i>addconn</i> &#8211;liststack [&#8211;rootdir&nbsp;<wbr><i>dir</i>] [&#8211;config&nbsp;<wbr><i>filename</i>] [&#8211;ctlbase&nbsp;<wbr><i>socketfile</i>] [&#8211;verbose] [&#8211;noexport] [&#8211;warningsfatal]</p>
<dt> <code>ipsec</code> <i>addconn</i> &#8211;checkconfig [&#8211;rootdir&nbsp;<wbr><i>dir</i>] [&#8211;config&nbsp;<wbr><i>filename</i>] [&#8211;ctlbase&nbsp;<wbr><i>socketfile</i>] [&#8211;verbose] [&#8211;warningsfatal]</p>
<dt> <code>ipsec</code> <i>addconn</i> &#8211;autoall [&#8211;rootdir&nbsp;<wbr><i>dir</i>] [&#8211;config&nbsp;<wbr><i>filename</i>] [&#8211;ctlbase&nbsp;<wbr><i>socketfile</i>] [&#8211;verbose] [&#8211;warningsfatal]</p>
<dt> <code>ipsec</code> <i>addconn</i> [&#8211;rootdir&nbsp;<wbr><i>dir</i>] [&#8211;config&nbsp;<wbr><i>filename</i>] [&#8211;ctlbase&nbsp;<wbr><i>socketfile</i>] [&#8211;verbose] [&#8211;warningsfatal] <i>name1</i> [<i>name2 ..</i>]</p>
<dt> <code>ipsec</code> <i>addconn</i> [&#8211;listall] [&#8211;liststart] [&#8211;listroute] [&#8211;listadd] [&#8211;listignore] [&#8211;rootdir&nbsp;<wbr><i>dir</i>] [&#8211;config&nbsp;<wbr><i>filename</i>] [&#8211;ctlbase&nbsp;<wbr><i>socketfile</i>] [&#8211;verbose] [&#8211;warningsfatal]</p>
<dt> <code>ipsec</code> <i>addconn &#8211;help</i></dl>
<h2>Description</h2>
<p><i>ipsec addconn</i></p>
<dd>takes a config file (or stdin) containing the format of ipsec.conf, or the format of individual &quot;conn&quot; sections, and uses that information to load named or all connections defined in that configuration file into the running libreswan pluto IKE daemon. If no configuration file is specified, the default configuration file is used. If no pluto socket is specified, the default socket location will be used. </p>
<p> When <i>&#8211;addall</i> is used, all connections defined in the config file will be operated on. Otherwise, only the specified connection names will be affected. </p>
<p> When addcon is run, connections that have the <i>auto=</i> option set to <i>add</i>, <i>start</i> or <i>route</i> will be loaded, routed or initiated. If a connection was loaded or initiated already, it will be replaced. </p>
<p> When <i>&#8211;configsetup</i> is specified, the configuration file is parsed for the <i>config setup</i> section and printed to the terminal usable as a shell script. These are prefaced with <i>export </i> unless <i>&#8211;noexport</i> is specified. </p>
<p> When <i>&#8211;checkconfig</i> is specified, the configuration file is parsed and all sections are checked for correct syntax. If an error is found, information about it is printed to the terminal. </p>
<p> When <i>&#8211;listroute</i> or <i>&#8211;liststart</i> is specified, no connections are added or replaced, only shown. This command can be used to verify which connections the addcon command would act upon, without actually performing any action.</p>
<h2>History</h2>
<p>Man page written for the Libreswan project &lt;m[blue]<code><a rel="nofollow" href="http://www.libreswan.org/">http://www.libreswan.org/</a></code>m[]&gt; by Paul Wouters</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
