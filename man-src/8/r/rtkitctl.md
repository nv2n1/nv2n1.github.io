---
title: "rtkitctl(8)"
name: "rtkitctl"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rtkitctl/"
description: "rtkitctl – Realtime Policy and Watchdog daemon control"
---

<p>rtkitctl &#8211; Realtime Policy and Watchdog daemon control</p>
<h2>Synopsis</h2>
<p><code>rtkitctl</code> [<i>options</i>]</p>
<h2>Description</h2>
<p><code>RealtimeKit</code> is a D-Bus system service that changes the scheduling policy of user processes/threads to SCHED_RR (i.e. realtime scheduling mode) on request. It is intended to be used as a secure mechanism to allow real-time scheduling to be used by normal user processes.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Show a summary of options.</dd>
<dt><code>&#8211;version</code></dt>
<dd>Show version.</dd>
<dt><code>&#8211;reset-known</code></dt>
<dd>Reset real-time status of known threads.</dd>
<dt><code>&#8211;reset-all</code></dt>
<dd>Reset real-time status of all threads.</dd>
<dt><code>&#8211;start</code></dt>
<dd>Start RealtimeKit if it is not running already.</dd>
<dt><code>-k, &#8211;exit</code></dt>
<dd>Terminate running RealtimeKit daemon.</dd></dl>
<h2>Author</h2>
<p>RealtimeKit was written by Lennart Poettering &lt;lennart [at] poettering.net&gt;.</p>
