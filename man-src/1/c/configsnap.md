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
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> print debug info</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> print version</dd>
<dt><code>-s</code>, <code>&#8211;silent</code></dt>
<dd> no output to stdout</dd>
<dt><code>-t</code> TAG, <code>&#8211;tag</code>=<i>TAG</i></dt>
<dd> tag identifer (e.g. a ticket number)</dd>
<dt><code>-d</code> BASEDIR, <code>&#8211;basedir</code>=<i>BASEDIR</i></dt>
<dd> base directory to store output</dd>
<dt><code>-p</code> PHASE, <code>&#8211;phase</code>=<i>PHASE</i></dt>
<dd> phase this is being used for. Can be any string. Phases containing post or rollback will perform diffs </dd>
</dl>
