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
<dt><code>-h</code>, <code>-?</code>, <code>&#8211;help</code></dt>
<dd> Print help about usage and exit.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print the version of <code>icuinfo</code> and exit.</dd>
<dt><code>-c</code>, <code>&#8211;copyright</code></dt>
<dd> Embeds the standard ICU copyright into the <i>output-file</i>.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Display extra informative messages during execution.</dd>
<dt><code>-i</code>, <code>&#8211;icudatadir</code><i> directory</i></dt>
<dd> Look for any necessary ICU data files in <i>directory</i>. For example, the file <code>pnames.icu</code> must be located when ICU&#8217;s data is not built as a shared library. The default ICU data directory is specified by the environment variable <code>ICU_DATA</code>. Most configurations of ICU do not require this argument.</dd>
<dt><code>-L</code>, <code>&#8211;list-plugins</code></dt>
<dd> If specified, list and diagnose issues with ICU plugins.</dd>
<dt><code>-K</code>, <code>&#8211;cleanup</code></dt>
<dd> Attempt to unload plugins before exiting.</dd>
<dt><code>-m</code>, <code>&#8211;milisecond-time</code></dt>
<dd> Print the current UTC time in milliseconds.</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010 International Business Machines Corporation and others </p>
<h2>Index</h2>
