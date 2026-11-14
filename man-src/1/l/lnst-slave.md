---
title: "lnst-slave(1)"
name: "lnst-slave"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lnst-slave/"
description: "lnst-slave – Linux Network Stack Test slave daemon"
---

<h2 class="name">NAME</h2>
<p> lnst-slave &#8211; Linux Network Stack Test slave daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>lnst-slave</code> [<code>-d</code>] [<code>-e</code>] [<code>-h</code>] [<code>-i </code><i>pidfile</i>] [<code>-p </code><i>port_number</i>]</p>
<h2>DESCRIPTION</h2>
<p> Linux Network Stack Test is a tool that supports development and execution of automated and portable network tests. For detailed description of the architecture of LNST please refer to project website (link listed on <code>INTERNET RESOURCES</code> bellow). </p>
<p> <code>lnst-slave</code> is a daemon script that runs in the background and waits for incomming commands from a controller.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d, &#8211;debug</code></p>
<dd> Toggle emitting debugging messages.</p>
<dt><code>-e, &#8211;daemonize</code></p>
<dd> Detach from parent process and run in background.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display usage of this command.</p>
<dt><code>-i, &#8211;pidfile</code><i>=file</i></p>
<dd> File to write damonized process&#8217; PID to.</p>
<dt><code>-m, &#8211;no-colours</code></p>
<dd> Disable coloured terminal output.</p>
<dt><code>-p, &#8211;port</code><i>=port_number</i></p>
<dd> The port number <code>lnst-slave</code> should listen on for incomming commands.</dl>
<h2>CONFIGURATION</h2>
<p> <code>lnst-slave</code> will look for configuration in the following location: </p>
<p> <i>/etc/lnst-slave.conf</i> </p>
<p> For further description of file format or configuration options available, please refer to the configuration file itself, where each option is documented.</p>
<h2>FILES</h2>
<p> Apart from configuration, there are few important locations that <code>lnst-slave</code> works with. All bellow mentioned paths can be changed in the configuration file.</p>
<h3>Log Path</h3>
<p> Every test exectution and all the commands run by <code>lnst-slave</code> during the test are logged to the following location: </p>
<p> <i>/var/log/lnst</i></p>
<h3>Cache Location</h3>
<p> Test modules and tools used by the controllers with this slave are cached in resources cache. The cache is by default located at: </p>
<p> <i>/var/cache/lnst</i> </p>
<p> The cache is fully under control of the <code>lnst-slave</code> daemon and is managed automatically. Making any modifications by hand is not recommended.</p>
<h2>INTERNET RESOURCES</h2>
<p> Project Homepage: <a rel="nofollow" href="http://lnst-project.org/">http://lnst-project.org/</a><br />
 Online Documentation: <a rel="nofollow" href="https://github.com/jpirko/lnst/wiki#learn">https://github.com/jpirko/lnst/wiki#learn</a><br />
 Git Source Tree: <a rel="nofollow" href="https://github.com/jpirko/lnst">https://github.com/jpirko/lnst</a><br />
 Mailing List: &lt;lnst-developers [at] lists.fedorahosted.org&gt; </p>
<h2>AUTHORS</h2>
<p> <code>Jiri Pirko</code> &lt;jiri [at] resnulli.us&gt;<br />
 <code>Jan Tluka</code> &lt;jtluka [at] redhat.com&gt;<br />
 <code>Ondrej Lichtner</code> &lt;olichtne [at] redhat.com&gt;<br />
 <code>Jiri Prochazka</code> &lt;jprochaz [at] redhat.com&gt;<br />
 <code>Jiri Zupka</code> &lt;jzupka [at] redhat.com&gt;<br />
 <code>Radek Pazdera</code> &lt;radek [at] pazdera.co.uk&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2011-2015 Red Hat, Inc. </p>
<p> LNST is distributed under GNU General Public License version 2. See the file &quot;COPYING&quot; in the source distribution for information on terms &amp; conditions for accessing and otherwise using LNST. </p>
<h2>Index</h2>
