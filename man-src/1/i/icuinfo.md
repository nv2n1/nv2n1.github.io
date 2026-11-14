---
title: "icuinfo(1)"
name: "icuinfo"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icuinfo/"
description: "icuinfo – Shows some basic info about the current ICU"
---

<h2 class="name">NAME</h2>
<p> <code>icuinfo</code> &#8211; Shows some basic info about the current ICU </p>
<h2>SYNOPSIS</h2>
<p> <code>icuinfo</code> [ <code>-h</code>, <code>-?</code>, <code>&#8211;help</code> ] [ <code>-V</code>, <code>&#8211;version</code> ] [ <code>-c</code>, <code>&#8211;copyright</code> ] [ <code>-i</code>, <code>&#8211;icudatadir</code><i> directory</i> ] [ <code>-v</code>, <code>&#8211;verbose</code> ] [ <code>-L</code>, <code>&#8211;list-plugins</code> ] [ <code>-m</code>, <code>&#8211;milisecond-time</code> ] [ <code>-K</code>, <code>&#8211;cleanup</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>icuinfo</code> prints basic information about the current version of ICU.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></p>
<dd> Print help about usage and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version of <code>icuinfo</code> and exit.</p>
<dt><code>-c</code>, <code>&#8211;copyright</code></p>
<dd> Embeds the standard ICU copyright into the <i>output-file</i>.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display extra informative messages during execution.</p>
<dt><code>-i</code>, <code>&#8211;icudatadir</code><i> directory</i></p>
<dd> Look for any necessary ICU data files in <i>directory</i>. For example, the file <code>pnames.icu</code> must be located when ICU&#8217;s data is not built as a shared library. The default ICU data directory is specified by the environment variable <code>ICU_DATA</code>. Most configurations of ICU do not require this argument.</p>
<dt><code>-L</code>, <code>&#8211;list-plugins</code></p>
<dd> If specified, list and diagnose issues with ICU plugins.</p>
<dt><code>-K</code>, <code>&#8211;cleanup</code></p>
<dd> Attempt to unload plugins before exiting.</p>
<dt><code>-m</code>, <code>&#8211;milisecond-time</code></p>
<dd> Print the current UTC time in milliseconds.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010 International Business Machines Corporation and others </p>
<h2>Index</h2>
