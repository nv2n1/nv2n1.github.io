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
<dt><code>-h, &#8211;help</code></p>
<dd>Show a summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd>Show version.</p>
<dt><code>&#8211;reset-known</code></p>
<dd>Reset real-time status of known threads.</p>
<dt><code>&#8211;reset-all</code></p>
<dd>Reset real-time status of all threads.</p>
<dt><code>&#8211;start</code></p>
<dd>Start RealtimeKit if it is not running already.</p>
<dt><code>-k, &#8211;exit</code></p>
<dd>Terminate running RealtimeKit daemon.</dl>
<h2>Author</h2>
<p>RealtimeKit was written by Lennart Poettering &lt;lennart [at] poettering.net&gt;.</p>
