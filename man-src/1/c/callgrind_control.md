---
title: "callgrind_control(1)"
name: "callgrind_control"
section: "1"
letter: "c"
url: "/docs/linux/man/1-callgrind_control/"
description: "callgrind_control – observe and control programs being run by Callgrind"
---

<h2 class="name">NAME</h2>
<p> callgrind_control &#8211; observe and control programs being run by Callgrind </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>callgrind_control</code> [<i>options</i>] [<i>pid|program-name</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>callgrind_control</code></p>
<dd>controls programs being run by the Valgrind tool Callgrind. When a <code>pid/program name</code> argument is not specified, all applications currently being run by Callgrind on this system will be used for actions given by the specified option(s). The default action is to give some brief information about the applications being run by Callgrind.</p>
<h2>OPTIONS</h2>
<p> <code>-h &#8211;help</code></p>
<dl>
<dt>
<dd> Show a short description, usage, and summary of options.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show version of callgrind_control.</dl>
<p> <code>-l &#8211;long</code></p>
<dl>
<dt>
<dd> Show also the working directory, in addition to the brief information given by default.</dl>
<p> <code>-s &#8211;stat</code></p>
<dl>
<dt>
<dd> Show statistics information about active Callgrind runs.</dl>
<p> <code>-b &#8211;back</code></p>
<dl>
<dt>
<dd> Show stack/back traces of each thread in active Callgrind runs. For each active function in the stack trace, also the number of invocations since program start (or last dump) is shown. This option can be combined with -e to show inclusive cost of active functions.</dl>
<p> <code>-e [A,B,&#8230;] </code> (default: all)</p>
<dl>
<dt>
<dd> Show the current per-thread, exclusive cost values of event counters. If no explicit event names are given, figures for all event types which are collected in the given Callgrind run are shown. Otherwise, only figures for event types A, B, &#8230; are shown. If this option is combined with -b, inclusive cost for the functions of each active stack frame is provided, too.</dl>
<p> <code>&#8211;dump[=&lt;desc&gt;] </code> (default: no description)</p>
<dl>
<dt>
<dd> Request the dumping of profile information. Optionally, a description can be specified which is written into the dump as part of the information giving the reason which triggered the dump action. This can be used to distinguish multiple dumps.</dl>
<p> <code>-z &#8211;zero</code></p>
<dl>
<dt>
<dd> Zero all event counters.</dl>
<p> <code>-k &#8211;kill</code></p>
<dl>
<dt>
<dd> Force a Callgrind run to be terminated.</dl>
<p> <code>&#8211;instr=&lt;on|off&gt;</code></p>
<dl>
<dt>
<dd> Switch instrumentation mode on or off. If a Callgrind run has instrumentation disabled, no simulation is done and no events are counted. This is useful to skip uninteresting program parts, as there is much less slowdown (same as with the Valgrind tool &quot;none&quot;). See also the Callgrind option <code>&#8211;instr-atstart</code>.</dl>
<p> <code>&#8211;vgdb-prefix=&lt;prefix&gt;</code></p>
<dl>
<dt>
<dd> Specify the vgdb prefix to use by callgrind_control. callgrind_control internally uses vgdb to find and control the active Callgrind runs. If the <code>&#8211;vgdb-prefix</code> option was used for launching valgrind, then the same option must be given to callgrind_control.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-valgrind/">valgrind</a>(1), $INSTALL/share/doc/valgrind/html/index.html or <a rel="nofollow" href="http://www.valgrind.org/docs/manual/index.html.">http://www.valgrind.org/docs/manual/index.html.</a></p>
<h2>AUTHOR</h2>
<p> Josef Weidendorfer &lt;Josef.Weidendorfer [at] gmx.de&gt;. </p>
<h2>Index</h2>
