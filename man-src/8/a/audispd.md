---
title: "audispd(8)"
name: "audispd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-audispd/"
description: "audispd – an event multiplexor"
---

<p>audispd &#8211; an event multiplexor</p>
<h2>Synopsis</h2>
<p><code>audispd</code></p>
<h2>Description</h2>
<p><code>audispd</code> is an audit event multiplexor. It has to be started by the audit daemon in order to get events. It takes audit events and distributes them to child programs that want to analyze events in realtime. When the audit daemon receives a SIGTERM or SIGHUP, it passes that signal to the dispatcher, too. The dispatcher in turn passes those signals to its child processes. </p>
<p> The child programs install a configuration file in a plugins directory, <i>/etc/audisp/plugins.d</i>. Filenames are not allowed to have more than one &#8216;.&#8217; in the name or it will be treated as a backup copy and skipped. Options are given one per line with an equal sign between the keyword and its value. The available options are as follows: </p>
<dl>
<dt><i>active</i></dt>
<dd>The options for this are <i>yes</i> or <i>no.</i></dd>
<dt><i>direction</i></dt>
<dd>The option is dictated by the plugin. <i>In</i> or <i>out</i> are the only choices. You cannot make a plugin operate in a way it wasn&#8217;t designed just by changing this option.This option is to give a clue to the event dispatcher about which direction events flow. NOTE: inbound events are not supported yet.</dd>
<dt><i>path</i></dt>
<dd>This is the absolute path to the plugin executable. In the case of internal plugins, it would be the name of the plugin.</dd>
<dt><i>type</i></dt>
<dd>This tells the dispatcher how the plugin wants to be run. Choices are <i>builtin</i> and <i>always.</i> <i>Builtin</i> should always be given for plugins that are internal to the audit event dispatcher. These are af_unix and syslog. The option <i>always</i> should be given for most if not all plugins. The default setting is <i>always.</i></dd>
<dt><i>args</i></dt>
<dd>This allows you to pass arguments to the child program. Generally plugins do not take arguments and have their own config file that instructs them how they should be configured. At the moment, there is a limit of 2 args.</dd>
<dt><i>format</i></dt>
<dd>The valid options for this are <i>binary</i> and <i>string.</i> <i>Binary</i> passes the data exactly as the audit event dispatcher gets it from the audit daemon. The <i>string</i> option tells the dispatcher to completely change the event into a string suitable for parsing with the audit parsing library. The default value is <i>string.</i><br />
&nbsp;<wbr></dd></dl>
<h2>Files</h2>
<p>/etc/audisp/audispd.conf /etc/audisp/plugins.d</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-audispd-conf/">audispd.conf</a></code>(5), <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8).</p>
<h2>Author</h2>
<p>Steve Grubb</p>
