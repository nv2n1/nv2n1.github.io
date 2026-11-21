---
title: "ps_mem(1)"
name: "ps_mem"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ps_mem/"
description: "ps_mem – Memory profiling tool"
---

<h2>NAME</h2>
<p> ps_mem &#8211; Memory profiling tool</p>
<h2>SYNOPSIS</h2>
<p> <code>ps_mem</code> [-h|&#8211;help] [-s|&#8211;show-cmdline] [-p PID] [-w N]</p>
<h2>DESCRIPTION</h2>
<p> The ps_mem tool can determine how much RAM is used per program (not per process). </p>
<p> In detail it reports: </p>
<dl>
<dt>
</dt><dd> sum(private RAM for program processes) + sum(Shared RAM for program processes).
</dd></dl>
<p> The shared RAM is problematic to calculate, and the tool automatically selects the most accurate method available for the running kernel.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-h &#8211;help</dt>
<dd> Show this help</dd>
<dt>-s &#8211;show-cmdline</dt>
<dd> Show complete program path with options</dd>
<dt>-p &lt;pid&gt;[,pid2,&#8230;pidN]</dt>
<dd> Only show memory usage PIDs in the specified list</dd>
<dt>-w N</dt>
<dd> Measure and show process memory every N seconds</dd></dl>
<h2>AUTHOR</h2>
<p> Pádraig Brady &lt;P@draigBrady.com&gt; </p>
