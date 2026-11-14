---
title: "eurephia_init(7)"
name: "eurephia_init"
section: "7"
letter: "e"
url: "/docs/linux/man/7-eurephia_init/"
description: "eurephia_init – Initialisation utility for the eurephia OpenVPN plug-in."
---

<p>eurephia_init &#8211; Initialisation utility for the eurephia OpenVPN plug-in.</p>
<h2>Synopsis</h2>
<p><code>eurephia_init</code> [\-V|\-\-version] [-h|&#8211;help] [\-l|\-\-log &lt;filename&gt;] [\-L|\-\-log\-level &lt;log level&gt;] [\-N|\-\-hash\-threshold\-min &lt;ms&gt;] [\-M|\-\-hash\-threshold\-max &lt;ms&gt;] [\-D|&#8211;database-driver &lt;path&gt;] [\-d|\-\-database-args &lt;args&gt;]</p>
<h2>Description</h2>
<p>This utility is only supposed to be used when installing eurephia. The purpose is to initialise the database eurephia will use, by setting up some standard configuration values and create an administrator account</p>
<h2>Options</h2>
<p>Arguments used by eurephia_init:</p>
<dl>
<dt><code>-V</code> | <code>&#8211;version</code></p>
<dd>Show version information</p>
<dt><code>-h</code> | <code>&#8211;help</code></p>
<dd>This help screen</p>
<dt><code>-l</code> | <code>&#8211;log</code> &lt;filename&gt;</p>
<dd>Log file for debugging</p>
<dt><code>-L</code> | <code>&#8211;log-level</code> &lt;log level&gt;</p>
<dd>Sets the log level</p>
<dt> <code>-N</code> | <code>&#8211;hash-threshold-min</code> &lt;ms&gt; : Benchmarking parameter, see below. Default 95ms</p>
<dt> <code>-M</code> | <code>&#8211;hash-threshold-max</code> &lt;ms&gt; : Benchmarking parameter, see below. Default 200ms</p>
<dt><code>-D</code> | <code>&#8211;database-driver</code> &lt;full path&gt;</p>
<dd>
<dd>Full path to the database driver (Required)</p>
<dt><code>-d</code> | <code>&#8211;database-args</code> &lt;arguments&gt;</p>
<dd>Required database arguments for the driver (Required)</dl>
<h2>Benchmarking</h2>
<dl>
<dt>During the initialisation this utility will benchmark the CPU power by doing multiple SHA512 hash calculations. This is to determinate the optimal rounds the password hashes should use on the current computer. To make it more difficult to brute force passwords, eurephia implements dynamic password hash rounds, based on a random number within in a given range. This benchmark will suggest an optimal range. To do this, two limits are defined, the shortest time and the longest time to be used for calculating a hash. The default values are 95ms and 200ms.</p>
<dd>
<dt>If you want to modify those thresholds, you can do so with the <code>&#8211;hash-threshold-min</code> and <code>&#8211;hash-threshold-max</code> options. By increasing these numbers, you will allow the number of rounds to be increased.</p>
<dd></dl>
<h2>Author</h2>
<p>Copyright (C) 2009-2010 David Sommerseth &lt;dazo [at] users.sourceforge.net&gt;</p>
