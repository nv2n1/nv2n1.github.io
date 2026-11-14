---
title: "in-ntalkd(8)"
name: "in-ntalkd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-in-ntalkd/"
description: "talkd – remote user communication server"
---

<p><code>talkd</code> &#8211; remote user communication server</p>
<h2>Synopsis</h2>
<p><code>talkd</code> [-<code>dp</code> ]</p>
<h2>Description</h2>
<p><code>Talkd</code> is the server that notifies a user that someone else wants to initiate a conversation. It acts a repository of invitations, responding to requests by clients wishing to rendezvous to hold a conversation. In normal operation, a client, the caller, initiates a rendezvous by sending a <code>CTL_MSG</code> to the server of type <code>LOOK_UP</code> (see Aq Pa protocols/talkd.h ) . This causes the server to search its invitation tables to check if an invitation currently exists for the caller (to speak to the callee specified in the message). If the lookup fails, the caller then sends an <code>ANNOUNCE</code> message causing the server to broadcast an announcement on the callee&#8217;s login ports requesting contact. When the callee responds, the local server uses the recorded invitation to respond with the appropriate rendezvous address and the caller and callee client programs establish a stream connection through which the conversation takes place.</p>
<h2>Options</h2>
<p>[-<code>d</code> ] Debug mode; writes copious logging and debugging information to /var/log/talkd.log </p>
<p> [-<code>p</code> ] Packet logging mode; writes copies of malformed packets to /var/log/talkd.packets This is useful for debugging interoperability problems.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-talk/">talk</a>(1), <a href="/docs/linux/man/1-write/">write</a>(1)</p>
<h2>History</h2>
<p>The <code>talkd</code> command appeared in BSD 4.3</p>
