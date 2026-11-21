---

title: "idevicedebugserverproxy(1)"
name: "idevicedebugserverproxy"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idevicedebugserverproxy/"
description: "idevicedebugserverproxy – Remote debugging proxy."
---

<p> idevicedebugserverproxy &#8211; Remote debugging proxy.</p>
<h2>SYNOPSIS</h2>
<p> <code>idevicedebugserverproxy</code> [OPTIONS] PORT </p>
<h2>DESCRIPTION</h2>
<p> Proxy a debugserver connection from a device for remote debugging. After starting up, clients can connect to PORT and communicate with the remote debugserver using the LLVM remote serial debugging protocol. Thus connecting using LLDB or a LLVM based gdb to this port would allow remote debugging. The developer disk image needs to be mounted for this service to be available. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u, &#8211;udid UDID</code></dt>
<dd> target specific device by its 40-digit device UDID.</dd>
<dt><code>-d, &#8211;debug</code></dt>
<dd> enable communication debugging.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> prints usage information. </dd>
</dl>
<h2>USAGE</h2>
<dl>
<dt><code>PORT</code></dt>
<dd> The port under which the proxy should listen for connections from clients. </dd>
</dl>
<h2>AUTHORS</h2>
<p> Martin Szulecki </p>
