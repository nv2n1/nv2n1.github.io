---
title: "ophelp(1)"
name: "ophelp"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ophelp/"
description: "ophelp – list OProfile events"
---

<h2 class="name">NAME</h2>
<p> ophelp &#8211; list OProfile events </p>
<h2>SYNOPSIS</h2>
<p> <code>ophelp</code> [ <i>options</i> ] [event name]</p>
<h2>DESCRIPTION</h2>
<p> By default, <code>ophelp</code> lists the available performance counter options. If you give it a symbolic event name, it will return the hardware value (e.g. &quot;ophelp DATA_MEM_REFS&quot;). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;cpu-type / -c</code></p>
<dd> Show the events for the given numerical CPU type. </p>
<dt><code>&#8211;get-cpu-type / -r</code></p>
<dd> Show the symbolic CPU name. </p>
<dt><code>&#8211;get-default-event / -d</code></p>
<dd>
 Show the default event for the specified CPU type.</p>
<dt><code>&#8211;check-events / -e [events]</code></p>
<dd> Check the given space-separated event descriptions for validity. If the events are valid, show which pmu counter each event would be assigned to. </p>
<dt><code>&#8211;callgraph [callgraph_depth]</code></p>
<dd> Use the callgraph depth to compute the higher minimum sampling intervals for the events. </p>
<dt><code>&#8211;unit-mask / -u [event]</code></p>
<dd> Show the default unit mask for the given event. </p>
<dt><code>&#8211;symbolic-unit-mask / -U [event]</code></p>
<dd> Show the numerical unit and extra mask for given event. </p>
<dt><code>&#8211;extra-mask / -E [event]</code></p>
<dd> Show the extra unit mask for given event. </p>
<dt><code>&#8211;xml / -X</code></p>
<dd> List events in XML format. </p>
<dt><code>&#8211;help / -? / &#8211;usage</code></p>
<dd> Show help message. </p>
<dt><code>&#8211;version / -v</code></p>
<dd> Show version. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> No special environment variables are recognised by ophelp. </p>
<h2>FILES</h2>
<dl>
<dt><i>$prefix/share/oprofile/</i></p>
<dd> Event description files used by OProfile.</p>
<dt><i>/var/lib/oprofile/samples/</i></p>
<dd> The location of the generated sample files. </p>
</dl>
<h2>VERSION</h2>
<dl>
<dt>This man page is current for oprofile-0.9.9.</p>
<dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>/usr/share/doc/oprofile/,</code> <code><a href="/docs/linux/man/1-oprofile/">oprofile</a>(1)</code> </p>
<h2>Index</h2>
