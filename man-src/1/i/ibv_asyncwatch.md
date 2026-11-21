---
title: "ibv_asyncwatch(1)"
name: "ibv_asyncwatch"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibv_asyncwatch/"
description: "ibv_asyncwatch – display asynchronous events"
---

<h2 class="name">NAME</h2>
<p> ibv_asyncwatch &#8211; display asynchronous events</p>
<h2>SYNOPSIS</h2>
<p> <code>ibv_asyncwatch</code> [-d device] [-h] </p>
<h2>DESCRIPTION</h2>
<p> Display asynchronous events forwarded to userspace for an RDMA device. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;ib-dev</code>=<i>DEVICE</i></dt>
<dd> use IB device <i>DEVICE</i> (default first device found)</dd>
<dt><code>-h</code>, <code>&#8211;help</code>=<i>DEVICE</i></dt>
<dd> Print a help text and exit. </dd>
</dl>
<h2>AUTHORS</h2>
<dl>
<dt>Roland Dreier</dt>
<dd> &lt;<i>rolandd [at] cisco.com</i>&gt;</dd>
<dt>Eran Ben Elisha</dt>
<dd> &lt;<i>eranbe [at] mellanox.com</i>&gt; </dd>
</dl>
