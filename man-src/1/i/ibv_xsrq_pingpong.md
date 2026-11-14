---
title: "ibv_xsrq_pingpong(1)"
name: "ibv_xsrq_pingpong"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibv_xsrq_pingpong/"
description: "ibv_xsrq_pingpong – simple InfiniBand shared receive queue test"
---

<h2 class="name">NAME</h2>
<p> ibv_xsrq_pingpong &#8211; simple InfiniBand shared receive queue test</p>
<h2>SYNOPSIS</h2>
<p> <code>ibv_xsrq_pingpong</code> [-p port] [-d device] [-i ib port] [-s size] [-m mtu] [-c clients] [-n num_tests] [-l sl] [-e] <code>HOSTNAME</code> </p>
<p> <code>ibv_xsrq_pingpong</code> [-p port] [-d device] [-i ib port] [-s size] [-m mtu] [-c clients] [-n num_tests] [-l sl] [-e] </p>
<h2>DESCRIPTION</h2>
<p> Run a simple ping-pong test over InfiniBand via the extended reliable connected (XRC) transport service, using a shared receive queue (SRQ). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></p>
<dd> use TCP port <i>PORT</i> for initial synchronization (default 18515)</p>
<dt><code>-d</code>, <code>&#8211;ib-dev</code>=<i>DEVICE</i></p>
<dd> use IB device <i>DEVICE</i> (default first device found)</p>
<dt><code>-i</code>, <code>&#8211;ib-port</code>=<i>PORT</i></p>
<dd> use IB port <i>PORT</i> (default port 1)</p>
<dt><code>-s</code>, <code>&#8211;size</code>=<i>SIZE</i></p>
<dd> ping-pong messages of size <i>SIZE</i> (default 4096)</p>
<dt><code>-m</code>, <code>&#8211;mtu</code>=<i>MTU</i></p>
<dd> use path mtu of size <i>MTU</i> (default 2048)</p>
<dt><code>-c</code>, <code>&#8211;clients</code>=<i>CLIENTS</i></p>
<dd> number of clients <i>CLIENTS</i> (on server only, default 1)</p>
<dt><code>-n</code>, <code>&#8211;num-tests</code>=<i>NUM_TESTS</i></p>
<dd> perform <i>NUM_TESTS</i> tests per client (default 5)</p>
<dt><code>-l</code>, <code>&#8211;sl</code>=<i>SL</i></p>
<dd> use <i>SL</i> as the service level value (default 0)</p>
<dt><code>-e</code>, <code>&#8211;events</code></p>
<dd> sleep while waiting for work completion events (default is to poll for completions) </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ibv_rc_pingpong/">ibv_rc_pingpong</a></code>(1), <code><a href="/docs/linux/man/1-ibv_uc_pingpong/">ibv_uc_pingpong</a></code>(1), <code><a href="/docs/linux/man/1-ibv_ud_pingpong/">ibv_ud_pingpong</a></code>(1) <code><a href="/docs/linux/man/1-ibv_srq_pingpong/">ibv_srq_pingpong</a></code>(1) </p>
<h2>AUTHORS</h2>
<dl>
<dt>Roland Dreier</p>
<dd> &lt;<i>roland [at] purestorage.com</i>&gt;</p>
<dt>Jarod Wilson</p>
<dd> &lt;<i>jarod [at] redhat.com</i>&gt; </p>
</dl>
<h2>BUGS</h2>
<p> The network synchronization between client and server instances is weak, and does not prevent incompatible options from being used on the two instances. The method used for retrieving work completions is not strictly correct, and race conditions may cause failures on some systems. </p>
<h2>Index</h2>
