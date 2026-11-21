---

title: "abrt-action-notify(1)"
name: "abrt-action-notify"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-action-notify/"
---

abrt-action-notify - Announces a new occurrence of problem via all accessible channels 

<h2>SYNOPSIS</h2>

 

 <i>abrt-action-notify</i> [-h] -d PROBLEM_DIR [-v] [-a] [-e AUTOREPORTING_EVENT]

<h2>DESCRIPTION</h2>

 

 The current implementation emits a D-Bus signal on System bus in path /org/freedesktop/problems of org.freedesktop.problems interface for Crash member.

<h3>Integration with ABRT events</h3>

 

 <i>abrt-action-notify</i> is used to notify new problems and consecutive occurrences of a single problem for all crash types. 

<dl>
<dt>
</dt><dd> <pre>
EVENT=notify package!=
    abrt-action-notify
</pre></dd></dl>

<h2>OPTIONS</h2>

 

 -v, --verbose
<dl>
<dt>
</dt><dd> Be verbose</dd></dl>
 

 -d, --problem-dir PROBLEM_DIR
<dl>
<dt>
</dt><dd> Problem directory [Default: current directory]</dd></dl>
 

 -h, --help
<dl>
<dt>
</dt><dd> Show help message</dd></dl>
 

 -a, --autoreporting
<dl>
<dt>
</dt><dd> Force to run autoreporting event</dd></dl>
 

 -e, --autoreporting-event AUTOREPORTING_EVENT
<dl>
<dt>
</dt><dd> Overwrite autoreporting event name</dd></dl>

<h2>ENVIRONMENT</h2>

 

 ABRT_VERBOSE
<dl>
<dt>
</dt><dd> ABRT verbosity level</dd></dl>

<h2>FILES</h2>

 

 /etc/abrt/abrt.conf 

 AutoreportingEnabled
<dl>
<dt>
</dt><dd> If enabled, abrt-action-notify runs AutoreportingEvent</dd></dl>
 

 AutoreportingEvent
<dl>
<dt>
</dt><dd> Name of event to be run if autoreporting is enabled</dd></dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5)

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>
