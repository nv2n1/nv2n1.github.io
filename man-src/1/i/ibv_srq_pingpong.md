---

title: "ibv_srq_pingpong(1)"
name: "ibv_srq_pingpong"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibv_srq_pingpong/"
description: "ibv_srq_pingpong – simple InfiniBand shared receive queue test"
---

<p> ibv_srq_pingpong &#8211; simple InfiniBand shared receive queue test</p>
<h2>SYNOPSIS</h2>
<p> <code>ibv_srq_pingpong</code> [-p port] [-d device] [-i ib port] [-s size] [-q num QPs] [-r rx depth] [-n iters] [-l sl] [-e] <code>HOSTNAME</code> </p>
<p> <code>ibv_srq_pingpong</code> [-p port] [-d device] [-i ib port] [-s size] [-q num QPs] [-r rx depth] [-n iters] [-l sl] [-e] </p>
<h2>DESCRIPTION</h2>
<p> Run a simple ping-pong test over InfiniBand via the reliable connected (RC) transport, using multiple queue pairs (QPs) and a single shared receive queue (SRQ). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></dt>
<dd> use TCP port <i>PORT</i> for initial synchronization (default 18515)</dd>
<dt><code>-d</code>, <code>&#8211;ib-dev</code>=<i>DEVICE</i></dt>
<dd> use IB device <i>DEVICE</i> (default first device found)</dd>
<dt><code>-i</code>, <code>&#8211;ib-port</code>=<i>PORT</i></dt>
<dd> use IB port <i>PORT</i> (default port 1)</dd>
<dt><code>-s</code>, <code>&#8211;size</code>=<i>SIZE</i></dt>
<dd> ping-pong messages of size <i>SIZE</i> (default 4096)</dd>
<dt><code>-q</code>, <code>&#8211;num-qp</code>=<i>NUM</i></dt>
<dd> use <i>NUM</i> queue pairs for test (default 16)</dd>
<dt><code>-r</code>, <code>&#8211;rx-depth</code>=<i>DEPTH</i></dt>
<dd> post <i>DEPTH</i> receives at a time (default 1000)</dd>
<dt><code>-n</code>, <code>&#8211;iters</code>=<i>ITERS</i></dt>
<dd> perform <i>ITERS</i> message exchanges (default 1000)</dd>
<dt><code>-l</code>, <code>&#8211;sl</code>=<i>SL</i></dt>
<dd> use <i>SL</i> as the service level value of the QPs (default 0)</dd>
<dt><code>-e</code>, <code>&#8211;events</code></dt>
<dd> sleep while waiting for work completion events (default is to poll for completions) </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ibv_rc_pingpong/">ibv_rc_pingpong</a></code>(1), <code><a href="/docs/linux/man/1-ibv_uc_pingpong/">ibv_uc_pingpong</a></code>(1), <code><a href="/docs/linux/man/1-ibv_ud_pingpong/">ibv_ud_pingpong</a></code>(1) </p>
<h2>AUTHORS</h2>
<dl>
<dt>Roland Dreier</dt>
<dd> &lt;<i>rolandd [at] cisco.com</i>&gt; </dd>
</dl>
<h2>BUGS</h2>
<p> The network synchronization between client and server instances is weak, and does not prevent incompatible options from being used on the two instances. The method used for retrieving work completions is not strictly correct, and race conditions may cause failures on some systems. </p>
