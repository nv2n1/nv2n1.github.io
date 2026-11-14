---
title: "perf-help(1)"
name: "perf-help"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-help/"
description: "perf-help – display help information about perf"
---

<h2 class="name">NAME</h2>
<p> perf-help &#8211; display help information about perf </p>
<h2>SYNOPSIS</h2>
<p> <i>perf help</i> [-a|&#8211;all] [COMMAND]</p>
<h2>DESCRIPTION</h2>
<p> With no options and no COMMAND given, the synopsis of the <i>perf</i> command and a list of the most commonly used perf commands are printed on the standard output. </p>
<p> If the option <i>&#8211;all</i> or <i>-a</i> is given, then all available commands are printed on the standard output. </p>
<p> If a perf command is named, a manual page for that command is brought up. The <i>man</i> program is used by default for this purpose, but this can be overridden by other options or configuration variables. </p>
<p> Note that perf &#8211;help &#8230; is identical to perf help &#8230; because the former is internally converted into the latter.</p>
<h2>OPTIONS</h2>
<p> -a, &#8211;all</p>
<dl>
<dt>
<dd> Prints all the available commands on the standard output. This option supersedes any other option.</dl>
<h2>PERF</h2>
<p> Part of the <code><a href="/docs/linux/man/1-perf/">perf</a></code>(1) suite </p>
<h2>Index</h2>
