---
title: "qb-blackbox(8)"
name: "qb-blackbox"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qb-blackbox/"
description: "qb-blackbox – Display \"flight data\" from the \"blackbox\"."
---

<p>qb-blackbox &#8211; Display &quot;flight data&quot; from the &quot;blackbox&quot;.</p>
<h2>Synopsis</h2>
<p><code>qb-blackbox &lt;blackbox files&gt;&#8230;</code></p>
<h2>Description</h2>
<p><code>qb-blackbox</code> Print out the logs (including debug logs) that were recorded using libqb&#8217;s blackbox.</p>
<h2>Examples</h2>
<dl>
<dt>Get info to help developers diagnose a crash.</p>
<dd>$ qb-blackbox /var/lib/corosync/fdata<br />
 Dumping the contents of /var/lib/corosync/fdata<br />
 Mar 23 20:58:57 message_handler_orf_token():3677 install seq 0 aru 0 high seq received 0<br />
 Mar 23 20:58:57 message_handler_orf_token():3696 retrans flag count 4 token aru 0 install seq 0 aru 0 0<br />
 Mar 23 20:58:57 old_ring_state_reset():1487 Resetting old ring state<br />
 Mar 23 20:58:57 deliver_messages_from_recovery_to_regular():1693 recovery to regular 1-0<br />
 Mar 23 20:58:57 memb_state_operational_enter():1779 Delivering to app 1 to 0<br />
 Mar 23 20:58:57 sync_abort():594 ENTERING sync_abort()<br />
 Mar 23 20:58:57 sync_save_transitional():586 ENTERING sync_save_transitional()<br />
 Mar 23 20:58:57 member_object_joined():301 Member joined: r(0) ip(192.168.122.1)<br />
 Mar 23 20:58:57 sync_abort():594 ENTERING sync_abort()
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-qblog-h/">qblog.h</a></code>(3),</p>
<h2>Author</h2>
<p>Angus Salkeld</p>
