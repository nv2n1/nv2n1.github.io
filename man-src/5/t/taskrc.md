---
title: "taskrc(5)"
name: "taskrc"
section: "5"
letter: "t"
url: "/docs/linux/man/5-taskrc/"
description: "taskrc – Configuration details for the"
---

<p>taskrc &#8211; Configuration details for the </p>
<p><a href="/docs/linux/man/1-task/">task</a>(1) command </p>
<h2>Synopsis</h2>
<p><code>$HOME/.taskrc</code><br />
 <code>task rc:&lt;directory-path&gt;/.taskrc &#8230;</code><br />
 <code>TASKRC=&lt;directory-path&gt;/.taskrc task &#8230;</code> </p>
<h2>Description</h2>
<p><code>Taskwarrior</code> obtains its configuration data from a file called <i>.taskrc</i> . This file is normally located in the user&#8217;s home directory:</p>
<dl>
<dd>$HOME/.taskrc</dl>
<p> The default location can be overridden using the <i>rc:</i> attribute when running task:</p>
<dl>
<dd>$ task rc:&lt;directory-path&gt;/.taskrc &#8230;</dl>
<p> or using the TASKRC environment variable:</p>
<dl>
<dd>$ TASKRC=/tmp/.taskrc task &#8230;</dl>
<p> Individual options can be overridden by using the <i>rc.&lt;name&gt;:</i> attribute when running task:</p>
<dl>
<dd>$ task rc.&lt;name&gt;:&lt;value&gt; &#8230;</dl>
<p> or</p>
<dl>
<dd>$ task rc.&lt;name&gt;=&lt;value&gt; &#8230;</dl>
<p> If <code>Taskwarrior</code> is run without an existing configuration file it will ask if it should create a default, sample <i>.taskrc</i> file in the user&#8217;s home directory. The .taskrc file follows a very simply syntax defining name/value pairs:</p>
<dl>
<dd>&lt;name&gt; = &lt;value&gt;</dl>
<p> There may be whitespace around &lt;name&gt;, &#8216;=&#8217; and &lt;value&gt;, and it is ignored. Whitespace within the &lt;value&gt; is left intact. Whitespace is not permitted in comma-separated lists. The entry must be on a single line, no continuations. Values support UTF8 as well as JSON encoding, such as 
