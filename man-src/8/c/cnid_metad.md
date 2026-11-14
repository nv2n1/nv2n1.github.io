---
title: "cnid_metad(8)"
name: "cnid_metad"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cnid_metad/"
description: "cnid_metad – start cnid_dbd daemons on request"
---

<p>cnid_metad &#8211; start cnid_dbd daemons on request</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>cnid_metad</code> [-d] [-h&nbsp;<wbr><i>hostname</i>] [-p&nbsp;<wbr><i>port</i>] [-u&nbsp;<wbr><i>user</i>] [-g&nbsp;<wbr><i>group</i>] [-s&nbsp;<wbr><i>cnid_dbdpathname</i>]</dl>
<h2>Description</h2>
<p><code>cnid_metad</code></p>
<dd>waits for requests from <code>afpd</code> to start up instances of the <code>cnid_dbd</code> daemon. It keeps track of the status of a <code>cnid_dbd</code> instance once started and will restart it if necessary. <code>cnid_metad</code> is normally started at boot time from /etc/rc or equivalent and runs until shutdown. <code>afpd</code> needs to be configured with the <code>-cnidserver</code> option in <code>afpd.conf</code> in order to access <code>cnid_metad.</code> It is possible to run more than one instance of <code>cnid_metad</code> on the same machine if different values for the interface and/or port are specified with the <code>-h</code> and <code>-p</code> options.</p>
<h2>Options</h2>
<p><code>-d</code></p>
<dl>
<dd><code>cnid_metad will remain in the foreground and</code> will also leave the standard input, standard output and standard error file descriptors open. Useful for debugging.</dl>
<p> <code>-h</code><i> hostname</i></p>
<dl>
<dd>Use <i>hostname</i> as the network interface for requests as opposed to the default <code>localhost </code>.</dl>
<p> <code>-p</code><i> port</i></p>
<dl>
<dd>Use <i>port</i> as the port number for reqests. Default is 4700.</dl>
<p> <code>-u</code><i> user</i></p>
<dl>
<dd>Switch to the userid of <i>user</i> before serving requests. This userid will be inherited by all <code>cnid_dbd</code> daemon processes started.</dl>
<p> <code>-u</code><i> group</i></p>
<dl>
<dd>Switch to the groupid of <i>group</i> before serving requests. This groupid will be inherited by all <code>cnid_dbd</code> daemon processes started. Both <i>user</i> and <i>group</i> must be specified as strings.</dl>
<p> <code>-s</code><i> cnid_dbd pathname</i></p>
<dl>
<dd>Use <i>cnid_dbd pathname</i> as the pathname of the executeable of the <code>cnid_dbd</code> daemon. The default is <i>/usr/sbin/cnid_dbd.</i></dl>
<h2>Caveats</h2>
<p>The number of <code>cnid_dbd</code> subprocecesses is currently limited to 512. </p>
<p> <code>cnid_metad</code> does not block or catch any signals apart from SIGPIPE. It will therefore exit on most signals received. This will also cause all instances of <code>cnid_dbd&#8217;s</code> started by that <code>cnid_metad</code> to exit gracefully. Since state about and IPC access to the subprocesses is only maintained in memory by <code>cnid_metad</code> this is desired behaviour. As soon as <code>cnid_metad</code> is restarted <code>afpd</code> processes will transparently reconnect.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cnid_dbd/">cnid_dbd</a></code>(8), <code><a href="/docs/linux/man/8-afpd/">afpd</a></code>(8) </p>
