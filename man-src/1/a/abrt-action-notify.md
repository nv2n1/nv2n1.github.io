---
title: "abrt-action-notify(1)"
name: "abrt-action-notify"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-notify/"
---

<h2 class="name">NAME</h2>
 

 abrt-action-notify - Announces a new occurrence of problem via all accessible channels 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-notify</i> [-h] -d PROBLEM_DIR [-v] [-a] [-e AUTOREPORTING_EVENT]

<h2>DESCRIPTION</h2>

 

 The current implementation emits a D-Bus signal on System bus in path /org/freedesktop/problems of org.freedesktop.problems interface for Crash member.

<h3>Integration with ABRT events</h3>

 

 <i>abrt-action-notify</i> is used to notify new problems and consecutive occurrences of a single problem for all crash types. 

<dl>
<dt>
<dd> <pre>
EVENT=notify package!=
    abrt-action-notify
</pre></dl>

<h2>OPTIONS</h2>

 

 -v, --verbose
<dl>
<dt>
<dd> Be verbose</dl>
 

 -d, --problem-dir PROBLEM_DIR
<dl>
<dt>
<dd> Problem directory [Default: current directory]</dl>
 

 -h, --help
<dl>
<dt>
<dd> Show help message</dl>
 

 -a, --autoreporting
<dl>
<dt>
<dd> Force to run autoreporting event</dl>
 

 -e, --autoreporting-event AUTOREPORTING_EVENT
<dl>
<dt>
<dd> Overwrite autoreporting event name</dl>

<h2>ENVIRONMENT</h2>

 

 ABRT_VERBOSE
<dl>
<dt>
<dd> ABRT verbosity level</dl>

<h2>FILES</h2>

 

 /etc/abrt/abrt.conf 

 AutoreportingEnabled
<dl>
<dt>
<dd> If enabled, abrt-action-notify runs AutoreportingEvent</dl>
 

 AutoreportingEvent
<dl>
<dt>
<dd> Name of event to be run if autoreporting is enabled</dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5)

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


