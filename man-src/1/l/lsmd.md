---

title: "lsmd(1)"
name: "lsmd"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lsmd/"
description: "Daemon – lsmd"
---

<h2>NAME</h2>
<p> Daemon &#8211; lsmd</p>
<p> libStorageMgmt plug-in daemon. Plug-ins execute in their own process space for fault isolation and to accommodate different plug-in licensing requirements. Runs as an unprivileged user. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;plugindir</code> = The directory where the plugins are located</p>
<dl>
<dt> <code>&#8211;socketdir</code> = The directory for IPC sockets</dt>
<dt> <code>&#8211;confdir</code> = The directory where the config file are located</dt>
<dt> <code>-v</code> = Verbose logging</dt>
<dt><code>-d</code></dt>
<dd> = New style daemon (systemd) non-forking </dd>
</dl>
<h2>BUGS</h2>
<dd>Please report bugs to &lt;libstoragemgmt-devel [at] lists.fedorahosted.org&gt;</dd>
<h2>AUTHOR</h2>
<p> Tony Asleson &lt;tasleson [at] redhat.com&gt; </p>
