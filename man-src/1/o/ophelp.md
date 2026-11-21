---
title: "ophelp(1)"
name: "ophelp"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ophelp/"
description: "ophelp – list OProfile events"
---

<h2>SYNOPSIS</h2>
<p> <code>ophelp</code> [ <i>options</i> ] [event name]</p>
<h2>DESCRIPTION</h2>
<p> By default, <code>ophelp</code> lists the available performance counter options. If you give it a symbolic event name, it will return the hardware value (e.g. &quot;ophelp DATA_MEM_REFS&quot;). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;cpu-type / -c</code></dt>
<dd> Show the events for the given numerical CPU type. </dd>
<dt><code>&#8211;get-cpu-type / -r</code></dt>
<dd> Show the symbolic CPU name. </dd>
<dt><code>&#8211;get-default-event / -d</code></dt>
<dd>
 Show the default event for the specified CPU type.</dd>
<dt><code>&#8211;check-events / -e [events]</code></dt>
<dd> Check the given space-separated event descriptions for validity. If the events are valid, show which pmu counter each event would be assigned to. </dd>
<dt><code>&#8211;callgraph [callgraph_depth]</code></dt>
<dd> Use the callgraph depth to compute the higher minimum sampling intervals for the events. </dd>
<dt><code>&#8211;unit-mask / -u [event]</code></dt>
<dd> Show the default unit mask for the given event. </dd>
<dt><code>&#8211;symbolic-unit-mask / -U [event]</code></dt>
<dd> Show the numerical unit and extra mask for given event. </dd>
<dt><code>&#8211;extra-mask / -E [event]</code></dt>
<dd> Show the extra unit mask for given event. </dd>
<dt><code>&#8211;xml / -X</code></dt>
<dd> List events in XML format. </dd>
<dt><code>&#8211;help / -? / &#8211;usage</code></dt>
<dd> Show help message. </dd>
<dt><code>&#8211;version / -v</code></dt>
<dd> Show version. </dd>
</dl>
<h2>ENVIRONMENT</h2>
<p> No special environment variables are recognised by ophelp. </p>
<h2>FILES</h2>
<dl>
<dt><i>$prefix/share/oprofile/</i></dt>
<dd> Event description files used by OProfile.</dd>
<dt><i>/var/lib/oprofile/samples/</i></dt>
<dd> The location of the generated sample files. </dd>
</dl>
<h2>VERSION</h2>
<dl>
<dt>This man page is current for oprofile-0.9.9.</dt>
<dd>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>/usr/share/doc/oprofile/,</code> <code><a href="/docs/linux/man/1-oprofile/">oprofile</a>(1)</code> </p>
