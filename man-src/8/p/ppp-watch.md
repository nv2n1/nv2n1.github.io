---
title: "ppp-watch(8)"
name: "ppp-watch"
section: "8"
letter: "p"
url: "/docs/linux/man/8-ppp-watch/"
description: "ppp-watch – daemon to make PPP interfaces act more like other interfaces"
---

<p>ppp-watch &#8211; daemon to make PPP interfaces act more like other interfaces</p>
<h2>Synopsis</h2>
<p><code>ppp-watch</code> <i>interface-name</i> [boot]</p>
<h2>Description</h2>
<p><code>ppp-watch</code> manages one PPP connection, including starting, stopping, and redialing. It makes starting and stopping the connection synchronous activities. </p>
<p> <code>ppp-watch</code> is not really meant to be called directly. It should only be used from within the ifup-ppp script.</p>
<h2>Options</h2>
<dl>
<dt><i>interface-name</i></p>
<dd>The name of the PPP interface to bring up.</p>
<dt>boot</p>
<dd>ppp-watch is being called at boot time and should time out after a while if the PPP connection does not come up in order not to hang the boot sequence. </p>
</dl>
