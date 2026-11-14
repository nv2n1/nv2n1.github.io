---
title: "kismet_drone(1)"
name: "kismet_drone"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kismet_drone/"
description: "kismet_drone – Wireless sniffing and monitoring remote drone"
---

<h2>NAME</h2>
<p> <code>kismet_drone </code>&#8211; Wireless sniffing and monitoring remote drone</p>
<h2>SYNOPSIS</h2>
<pre><code>
kismet_drone[-svh][-f config - file][-c capture - source]
            [-C enable - capture - sources][-p port][-a allowed - hosts]
            [-N server - name]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>kismet_drone</code> supports all the capture sources available to Kismet. Instead of processing packets locally, kismet_drone makes them available via TCP to a remote kismet_server using the &#8216;drone&#8217; capture source.</p>
<h2>USAGE</h2>
<p> <code>kismet_drone</code> should be configured as you would <code>kismet_server</code>. All logging, packet dissection, etc will take place on the remote kismet server using the &#8216;drone&#8217; capture source. </p>
<p> <code>kismet_monitor</code> should be used to place capture sources into rfmonitor mode as needed, and <code>kismet_hopper</code> should be used for channel hopping. </p>
<p> <code>kismet_drone</code> is controlled by the <code>kismet_drone.conf</code> config file.</p>
<h2>ENCRYPTION</h2>
<p> It may be desireable to encrypt the packet stream between the remote drone and the kismet system. Standard SSH packet tunneling or any other tunneling/forwarding system may be used, and is recommended.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kismet/">kismet</a></code>(1), <code><a href="/docs/linux/man/5-kismet_drone-conf/">kismet_drone.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Mike Kershaw </p>
<h2>Index</h2>
