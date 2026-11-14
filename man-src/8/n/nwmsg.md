---
title: "nwmsg(8)"
name: "nwmsg"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nwmsg/"
description: "nwmsg – Deliver NetWare user broadcast messages"
---

<p>nwmsg &#8211; Deliver NetWare user broadcast messages</p>
<h2>Synopsis</h2>
<p><code>nwmsg</code> <i>mount-point</i></p>
<h2>Description</h2>
<p><code>nwmsg</code> is called by kerneld when a broadcast message arrives from a NetWare server. <code>nwmsg</code> fetches this message via the mount point and delivers it to the user using the same way <a href="/docs/linux/man/1-write/">write</a>(1) uses. Please note that <i>kerneld</i> must run when broadcast messages should be delivered to users. NetWare servers can send asynchronous broadcast messages to users, either on explicit request by another user, or when the server is shutdown. The client workstation is informed about this event by an IPX packet on a special socket, the message socket. This can happen at any time, so the user has to be informed about this event whenever it appears. I chose to use the kerneld feature of the Linux kernel to call the program nwmsg. For nwmsg, I used the relevant parts of the <i>write</i> program, so you can expect the NetWare broadcast messages to appear where user messages would appear. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ncpmount/">ncpmount</a>(8), <a href="/docs/linux/man/8-kerneld/">kerneld</a>(8), <a href="/docs/linux/man/1-write/">write</a>(1)</p>
