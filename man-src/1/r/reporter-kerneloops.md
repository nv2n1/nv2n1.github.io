---
title: "reporter-kerneloops(1)"
name: "reporter-kerneloops"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reporter-kerneloops/"
---

<h2 class="name">NAME</h2>
 

 reporter-kerneloops - Reports kernel oops to kerneloops.org (or similar) site. 

<h2>SYNOPSIS</h2>

 

 <i>reporter-kerneloops</i> [-v] [-c CONFFILE]... [-d DIR]

<h2>DESCRIPTION</h2>

 

 The tool is used to report the crash to the Kerneloops tracker.

<h3>Configuration file</h3>

 

 Configuration file contains entries in a format &quot;Option = Value&quot;. 

 The options are: 

 <i>SubmitURL</i>
<dl>
<dt>
<dd> The URL of the kerneloops tracker, the default is &quot;<a rel="nofollow" HREF="http://submit.kerneloops.org/submitoops.php">http://submit.kerneloops.org/submitoops.php</a>&quot;.</dl>

<h3>Integration with ABRT events</h3>

 

 <i>reporter-kerneloops</i> can be used as a reporter, to allow users to report problems to the Kerneloops tracker. This usage is pre-configured in /etc/libreport/events.d/koops_event.conf: 

<dl>
<dt>
<dd> <pre>
EVENT=report_Kerneloops analyzer=Kerneloops reporter-kerneloops
</pre></dl>
 

 It can be also used automatically and immediately without user interaction. When this is desired, modify the event configuration file to run the tool on the <i>post-create</i> event: 

<dl>
<dt>
<dd> <pre>
EVENT=post-create analyzer=Kerneloops  reporter-kerneloops
</pre></dl>

<h2>OPTIONS</h2>

 

 -v
<dl>
<dt>
<dd> Be more verbose. Can be given multiple times.</dl>
 

 -d DIR
<dl>
<dt>
<dd> Path to problem directory.</dl>
 

 -c CONFFILE
<dl>
<dt>
<dd> Path to configuration file. When used in ABRT event system, the file contains site-wide configuration. Users can change the values via environment variables.</dl>

<h2>ENVIRONMENT VARIABLES</h2>

 

 Environment variables take precedence over values provided in the configuration file. 

 <i>KerneloopsReporter_SubmitURL</i>
<dl>
<dt>
<dd> The URL of the kerneloops tracker.</dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/5-koops_event-conf/">koops_event.conf</a>(5)

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


