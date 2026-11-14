---
title: "pump(1)"
name: "pump"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pump/"
description: "pump – accelerate remote compilation with distcc"
---

<h2>NAME</h2>
<p> pump &#8211; accelerate remote compilation with distcc</p>
<h2>SYNOPSIS</h2>
<p> <code>pump</code> <i>BUILD-COMMAND [ARGS]</i> &#8230; </p>
<p> eval ` <code>pump</code> &#8211;startup `; <i>BUILD-COMMAND [ARGS]</i> &#8230; ; <code>pump</code> &#8211;shutdown</p>
<h2>DESCRIPTION</h2>
<p> <code>pump</code> is part of distcc. It is used for distcc&#8217;s pump mode. Distcc&#8217;s pump mode accelerates remote compilation with distcc by also distributing preprocessing to the servers. </p>
<p> For a detailed description of pump mode, including most notably some <code>important restrictions,</code> see the <code><a href="/docs/linux/man/1-distcc/">distcc</a>(1)</code> man page, in particular the <code>HOW PUMP-MODE WORKS</code> section and the <code>RESTRICTIONS ON PUMP MODE</code> section. </p>
<p> The simplest usage is the form</p>
<dl>
<dt>
<dd> <code>pump</code> <i>COMMAND [ARG]</i> &#8230;</dl>
<p> This will start an include server for distcc&#8217;s &quot;pump&quot; mode; optionally run <code>lsdistcc</code> to compute the distcc host list; set some auxiliary environment variables; change PATH to use the distcc client in the same directory as the &quot;pump&quot; script; execute <i>COMMAND</i> with the specified <i>ARG(s)</i> ; and then shut down the include server. The <i>COMMAND</i> is typically a parallel build command, such as &quot;make -j80&quot;, that will do many concurrent invocations of distcc. </p>
<p> An alternative way of invoking <code>pump</code> is to explicitly invoke &quot;pump &#8211;startup&quot; to start the include server and &quot;pump &#8211;shutdown&quot; to stop the include server. The &quot;pump &#8211;startup&quot; command will start up the include server, and will print out some environment variable settings. These environment variables are used to communicate between the pump-mode &quot;distcc&quot; client and the include server, and to communicate between &quot;pump &#8211;startup&quot; and &quot;pump &#8211;shutdown&quot;. The caller of &quot;pump &#8211;startup&quot; is responsible for setting those environment variables before invoking &quot;distcc&quot; or &quot;pump &#8211;shutdown&quot;. </p>
<p> For example:</p>
<dl>
<dt>
<dd> eval `pump &#8211;startup`<br />
 make -j80<br />
 pump &#8211;shutdown</dl>
<p> Note that distcc&#8217;s pump-mode assumes that sources files will not be<br />
&nbsp;<wbr>modified during the lifetime of the include server, so modifying source files during a build may cause inconsistent results.</p>
<h2>INVOKING LSDISTCC</h2>
<p> When invoked in either the simple &quot; <code>pump</code> <i>COMMAND [ARG]</i> &#8230; &quot; form, or as &quot; <code>pump &#8211;startup</code> &quot;, the <code>pump</code> script will invoke <code>lsdistcc</code> whenever DISTCC_POTENTIAL_HOSTS is set and DISTCC_HOSTS isn&#8217;t. It will pass the value of DISTCC_POTENTIAL_HOSTS to <code>lsdistcc</code> and use the output of <code>lsdistcc</code> to set DISTCC_HOSTS.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Displays summary instructions.</p>
<dt><code>&#8211;startup</code></p>
<dd> Starts an include server, and outputs the environment variable settings needed for <code><a href="/docs/linux/man/1-distcc/">distcc</a>(1)</code> or <code>pump &#8211;shutdown</code> to access it.</p>
<dt><code>&#8211;shutdown</code></p>
<dd> Shuts down an include server started up by <code>pump &#8211;startup.</code></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables are all optional.</p>
<dl>
<dt><code>DISTCC_LOCATION</code></p>
<dd> The location of the distcc bin directory, which is normally inferred from the link-resolved dirname of argv[0]. If this location is in fact the bin directory inside an installation (as will be the case when the pump script in the installation executes), then Python executables and distcc itself will be retrieved from the parent directory of the location.</p>
<dt><code>DISTCC_MAX_DISCREPANCY</code></p>
<dd> see the <code><a href="/docs/linux/man/1-distcc/">distcc</a>(1)</code> man page.</p>
<dt><code>DISTCC_POTENTIAL_HOSTS</code></p>
<dd> The distcc servers that will be queried by lsdistcc in order to produce a value for DISTCC_HOSTS. This value may be unset or null. In such cases, lsdistcc will not be invoked, and distcc will use DISTCC_HOSTS or the distcc hosts configuration file, as described in the &quot;Host Specifications&quot; section of <code><a href="/docs/linux/man/1-distcc/">distcc</a>(1).</code></p>
<dt><code>DISTCC_HOSTS</code></p>
<dd> This variable is passed through to distcc but only if DISTCC_POTENTIAL_HOSTS is not set.</p>
<dt><code>LSDISTCC_ARGS</code></p>
<dd> Extra arguments to pass to lsdistcc. See <code>lsdistcc &#8211;help</code> for more details.</p>
<dt><code>INCLUDE_SERVER_ARGS</code></p>
<dd> Extra arguments to pass to the include server.</p>
<dt><code>PYTHONOPTIMIZE</code></p>
<dd> If set to &quot;&quot;, then Python optimization is disabled.</dl>
<h2>EXAMPLE</h2>
<p> <code>pump make -j20</code></p>
<h2>BUGS</h2>
<p> If you think you have found a distcc bug, please see the file <i>reporting-bugs.txt</i> in the documentation directory for information on how to report it.</p>
<h2>AUTHORS</h2>
<p> The pump script and distcc&#8217;s pump mode were written by Nils Klarlund, Manos Renieris, Fergus Henderson, and Craig Silverstein. Please report bugs to &lt;distcc [at] lists.samba.org&gt;.</p>
<h2>LICENCE</h2>
<p> <code>pump</code> is part of distcc. You are free to use distcc. distcc (including this manual) may be copied, modified or distributed only under the terms of the GNU General Public Licence version 2 or later. distcc comes with absolutely no warranty. A copy of the GPL is included in the file COPYING.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-distcc/">distcc</a></code>(1), <code><a href="/docs/linux/man/1-distccd/">distccd</a></code>(1), <code><a href="/docs/linux/man/1-include_server/">include_server</a></code>(1), <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1), and <code><a href="/docs/linux/man/1-make/">make</a></code>(1) </p>
<h2>Index</h2>
