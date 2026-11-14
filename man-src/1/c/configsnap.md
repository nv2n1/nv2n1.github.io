---
title: "configsnap(1)"
name: "configsnap"
section: "1"
letter: "c"
url: "/docs/linux/man/1-configsnap/"
description: "configsnap – manual page for configsnap 0.11"
---

<h2>NAME</h2>
<p> configsnap &#8211; manual page for configsnap 0.11</p>
<h2>SYNOPSIS</h2>
<p> <code>configsnap</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> Record useful system state information, and compare to previous state if run with PHASE containing &quot;post&quot; or &quot;rollback&quot;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> print debug info</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> print version</p>
<dt><code>-s</code>, <code>&#8211;silent</code></p>
<dd> no output to stdout</p>
<dt><code>-t</code> TAG, <code>&#8211;tag</code>=<i>TAG</i></p>
<dd> tag identifer (e.g. a ticket number)</p>
<dt><code>-d</code> BASEDIR, <code>&#8211;basedir</code>=<i>BASEDIR</i></p>
<dd> base directory to store output</p>
<dt><code>-p</code> PHASE, <code>&#8211;phase</code>=<i>PHASE</i></p>
<dd> phase this is being used for. Can be any string. Phases containing post or rollback will perform diffs </p>
</dl>
<h2>Index</h2>
