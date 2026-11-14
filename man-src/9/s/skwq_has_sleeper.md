---
title: "skwq_has_sleeper(9)"
name: "skwq_has_sleeper"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skwq_has_sleeper/"
description: "skwq_has_sleeper – check if there are any waiting processes"
---

<p>skwq_has_sleeper &#8211; check if there are any waiting processes</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool skwq_has_sleeper(struct socket_wq&nbsp;<wbr>*&nbsp;<wbr></code><i>wq</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>wq</i></p>
<dl>
<dd>
<dd>struct socket_wq</dl>
<h2>Description</h2>
<p>Returns true if socket_wq has waiting processes The purpose of the skwq_has_sleeper and sock_poll_wait is to wrap the memory barrier call. They were added due to the race found within the tcp code. Consider following tcp code paths: CPU1 CPU2 </p>
<pre><code>sys_select receive packet...... __add_wait_queue update tp-&gt;rcv_nxt...... tp-&gt;rcv_nxt check sock_def_readable...
{
    schedule
        rcu_read_lock;
    wq = rcu_dereference(sk-&gt;sk_wq);
    if (wq &amp;&amp; waitqueue_active(wq-&gt;wait))
        wake_up_interruptible(wq-&gt;wait)...
}</code></pre>
<p> The race for tcp fires when the __add_wait_queue changes done by CPU1 stay in its cache, and so does the tp-&gt;rcv_nxt update on CPU2 side. The CPU1 could then endup calling schedule and sleep forever if there are no more data on the socket.</p>
<h2>Copyright</h2>
