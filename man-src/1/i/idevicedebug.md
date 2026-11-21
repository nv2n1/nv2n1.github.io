---
title: "idevicedebug(1)"
name: "idevicedebug"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idevicedebug/"
description: "idevicedebug – Interact with the debugserver service of a device."
---

<h2>NAME</h2>
<p> idevicedebug &#8211; Interact with the debugserver service of a device.</p>
<h2>SYNOPSIS</h2>
<p> <code>idevicedebug</code> [OPTIONS] COMMAND </p>
<h2>DESCRIPTION</h2>
<p> Interact with the debug service of a device. Currently the only implemented command is &quot;run&quot; and allows execution of developer apps and watch the stdout/stderr of the process. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e, &#8211;env NAME=VALUE</code></dt>
<dd> set environment variable NAME to VALUE.</dd>
<dt><code>-u, &#8211;udid UDID</code></dt>
<dd> target specific device by its 40-digit device UDID.</dd>
<dt><code>-d, &#8211;debug</code></dt>
<dd> enable communication debugging.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> prints usage information. </dd>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>run BUNDLEID [ARGS&#8230;]</code></dt>
<dd> run app with BUNDLEID and optional ARGS on device. </dd>
</dl>
<h2>AUTHORS</h2>
<p> Martin Szulecki </p>
