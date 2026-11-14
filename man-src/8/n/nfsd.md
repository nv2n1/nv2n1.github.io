---
title: "nfsd(8)"
name: "nfsd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nfsd/"
description: "rpc.nfsd – NFS server process"
---

<p>rpc.nfsd &#8211; NFS server process</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/rpc.nfsd [</code><i>options</i><code>]</code><i> nproc</i></p>
<h2>Description</h2>
<p>The <code>rpc.nfsd</code> program implements the user level part of the NFS service. The main functionality is handled by the <code>nfsd</code> kernel module. The user space program merely specifies what sort of sockets the kernel service should listen on, what NFS versions it should support, and how many kernel threads it should use. </p>
<p> The <code>rpc.mountd</code> server provides an ancillary service needed to satisfy mount requests by NFS clients.</p>
<h2>Options</h2>
<dl>
<dt><code>-d or &#8211;debug</code></p>
<dd>enable logging of debugging messages</p>
<dt><code>-H or &#8211;host hostname</code></p>
<dd>specify a particular hostname (or address) that NFS requests will be accepted on. By default, <code>rpc.nfsd</code> will accept NFS requests on all known network addresses. Note that <code>lockd</code> (which performs file locking services for NFS) may still accept request on all known network addresses. This may change in future releases of the Linux Kernel. This option can be used multiple time to listen to more than one interface.</p>
<dt><code>-p or &#8211;port port</code></p>
<dd>specify a different port to listen on for NFS requests. By default, <code>rpc.nfsd</code> will listen on port 2049.</p>
<dt><code>-r or &#8211;rdma</code></p>
<dd>specify that NFS requests on the standard RDMA port (&quot;nfsrdma&quot;, port 20049) should be honored.</p>
<dt><code>&#8211;rdma=</code><i>port</i></p>
<dd>Listen for RDMA requests on an alternate port &#8211; may be a number or a name listed in <code>/etc/services</code>.</p>
<dt><code>-N or &#8211;no-nfs-version vers</code></p>
<dd>This option can be used to request that <code>rpc.nfsd</code> does not offer certain versions of NFS. The current version of <code>rpc.nfsd</code> can support major NFS versions 2,3,4 and the minor versions 4.1 and 4.2.</p>
<dt><code>-s or &#8211;syslog</code></p>
<dd>By default, <code>rpc.nfsd</code> logs error messages (and debug messages, if enabled) to stderr. This option makes <code>rpc.nfsd</code> log these messages to syslog instead. Note that errors encountered during option processing will still be logged to stderr regardless of this option.</p>
<dt><code>-T or &#8211;no-tcp</code></p>
<dd>Disable <code>rpc.nfsd </code> from accepting TCP connections from clients.</p>
<dt><code>-U or &#8211;no-udp</code></p>
<dd>Disable <code>rpc.nfsd</code> from accepting UDP connections from clients.</p>
<dt><code>-V or &#8211;nfs-version vers</code></p>
<dd>This option can be used to request that <code>rpc.nfsd</code> offer certain versions of NFS. The current version of <code>rpc.nfsd</code> can support major NFS versions 2,3,4 and the minor versions 4.1 and 4.2.</p>
<dt><code>-L or &#8211;lease-time seconds</code></p>
<dd>Set the lease-time used for NFSv4. This corresponds to how often clients need to confirm their state with the server. Valid range is from 10 to 3600 seconds.</p>
<dt><code>-G or &#8211;grace-time seconds</code></p>
<dd>Set the grace-time used for NFSv4 and NLM (for NFSv2 and NFSv3). New file open requests (NFSv4) and new file locks (NLM) will not be allowed until after this time has passed to allow clients to recover state.</p>
<dt><i>nproc</i></p>
<dd>specify the number of NFS server threads. By default, eight threads are started. However, for optimum performance several threads should be used. The actual figure depends on the number of and the work load created by the NFS clients, but a useful starting point is eight threads. Effects of modifying that number can be checked using the <code><a href="/docs/linux/man/8-nfsstat/">nfsstat</a></code>(8) program.</dl>
<p> Note that if the NFS server is already running, then the options for specifying host, port, and protocol will be ignored. The number of processes given will be the only option considered, and the number of active <code>nfsd</code> processes will be increased or decreased to match this number. In particular <code>rpc.nfsd 0</code> will stop all threads and thus close any open connections.</p>
<h2>Configuration File</h2>
<p>Many of the options that can be set on the command line can also be controlled through values set in the <code>[nfsd]</code> section of the <i>/etc/nfs.conf</i> configuration file. Values recognized include:</p>
<dl>
<dt><code>threads</code></p>
<dd>The number of threads to start.</p>
<dt><code>host</code></p>
<dd>A host name, or comma separated list of host names, that <i>rpc.nfsd</i> will listen on. Use of the <code>&#8211;host</code> option replaces all host names listed here.</p>
<dt><code>grace-time</code></p>
<dd>The grace time, for both NFSv4 and NLM, in seconds.</p>
<dt><code>lease-time</code></p>
<dd>The lease time for NFSv4, in seconds.</p>
<dt><code>port</code></p>
<dd>Set the port for TCP/UDP to bind to.</p>
<dt><code>rdma</code></p>
<dd>Set RDMA port. Use &quot;rdma=nfsrdma&quot; to enable standard port.</p>
<dt><code>UDP</code></p>
<dd>Enable (with &quot;on&quot; or &quot;yes&quot; etc) or disable (&quot;off&quot;, &quot;no&quot;) UDP support.</p>
<dt><code>TCP</code></p>
<dd>Enable or disable TCP support.</p>
<dt><code>vers2</code></p>
<dd>
<dt><code>vers3</code></p>
<dd>
<dt><code>vers4</code></p>
<dd>Enable or disable a major NFS version. 3 and 4 are normally enabled by default.</p>
<dt><code>vers4.1</code></p>
<dd>
<dt><code>vers4.2</code></p>
<dd>Setting these to &quot;off&quot; or similar will disable the selected minor versions. Setting to &quot;on&quot; will enable them. The default values are determined by the kernel, and usually minor versions default to being enabled once the implementation is sufficiently complete. </p>
</dl>
<h2>Notes</h2>
<p>If the program is built with TI-RPC support, it will enable any protocol and address family combinations that are marked visible in the <code>netconfig</code> database. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rpc-mountd/">rpc.mountd</a></code>(8), <code><a href="/docs/linux/man/5-exports/">exports</a></code>(5), <code><a href="/docs/linux/man/8-exportfs/">exportfs</a></code>(8), <code><a href="/docs/linux/man/5-nfs-conf/">nfs.conf</a></code>(5), <code><a href="/docs/linux/man/8-rpc-rquotad/">rpc.rquotad</a></code>(8), <code><a href="/docs/linux/man/8-nfsstat/">nfsstat</a></code>(8), <code><a href="/docs/linux/man/5-netconfig/">netconfig</a>(5).</code></p>
<h2>Author</h2>
<p>Olaf Kirch, Bill Hawes, H. J. Lu, G. Allan Morris III, and a host of others.</p>
