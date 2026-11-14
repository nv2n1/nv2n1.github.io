---
title: "smokeping_upgrade(7)"
name: "smokeping_upgrade"
section: "7"
letter: "s"
url: "/docs/linux/man/7-smokeping_upgrade/"
description: "smokeping_upgrade – Notes on upgrading Smokeping"
---

<p>smokeping_upgrade &#8211; Notes on upgrading Smokeping</p>
<h2>Overview</h2>
<p>This document tries to list incompatible or otherwise user-visible changes in Smokeping versions, with instructions on how to fix any possible problems. It also sporadically mentions new features and the like. </p>
<p> The document currently starts with changes from 1.34 to 1.37. If you run into problems with upgrading from earlier versions, please send a description of the problems, preferably with notes on how to fix them, to the <tt>&quot;smokeping-users&quot;</tt> mailing list, so they can be added to this document. The same applies to any problems you find with current versions that are not documented here, of course. Patch submissions against the <font SIZE="-1">POD</font> source of this file are most appreciated. </p>
<p> If a version is not listed, there are no known problems in upgrading to it from the previous release. </p>
<p> An official list of changes with each release can be found in the <font SIZE="-1">CHANGES</font> file in the Smokeping distribution. This document tries to complement that with upgrading instructions etc.</p>
<h2>2.4.2 to 2.4.3</h2>
<p>To fix zooming for <font SIZE="-1">FF3.5 I</font> prototype and scriptaculous have been updated. To complete the fix you have to update your basepage.html too and include effects in the scriptaculous load line </p>
<pre> cropper/lib/scriptaculous.js?load=builder,effects,dragdrop</pre>
<h2>2.3.6 to 2.4.0</h2>
<p>The new SmokeTrace tool was added to SmokePing. For setup instructions read the smoketrace manual page.</p>
<h2>2.3.3 to 2.3.4</h2>
<p>The communication protocol between master and slave has been made more secure. This requires that <font SIZE="-1">BOTH</font> master and slave are upgraded to continue working.</p>
<h2>2.2.x to 2.3.x</h2>
<p>2.3.0 is mainly about new features. Check out the reference documentation on <i>hierarchies</i> and the target properties <i>parents</i>, <i>hidden</i> and <i>nomasterpoll</i>. </p>
<p> The only thing you have to take a look at, is the file <i>basepage.html.dist</i> which got some new css properties. Without them the results of the new filter function will look quite bad.</p>
<h2>2.1.x to 2.2.0</h2>
<h3><font SIZE="-1">LWP</font> Dependency</h3>
<p>The new master/slave functionality needs the LWP::UserAgent module from <font SIZE="-1">CPAN.</font> Currently the dependency is not optional; you&#8217;ll need the module even if you are only running one Smokeping instance.</p>
<h2>2.0.9 to 2.1.0</h2>
<h3>Echoping 6 support</h3>
<p>This is the first Smokeping version that fully supports echoping 6. Earlier versions of the EchoPingHttp probes don&#8217;t work with echoping 6 because of a command line incompatibility. (Echoping 5 is still supported, of course.) </p>
<p> This version also introduces three new probes using the new echoping plugin interface introduced in version 6:</p>
<dl>
<dt>&bull;</p>
<dd>EchoPingDNS</p>
<dt>&bull;</p>
<dd>EchoPingLDAP</p>
<dt>&bull;</p>
<dd>EchoPingWhois</dl>
<p> See the smokeping_examples document for simple examples of using these probes.</p>
<h3>New method in base.pm (if you write your own probes)</h3>
<p>The <i>base.pm</i> module defines the method ProbeUnit. Override this if your Probe does not return &#8216;Seconds&#8217;. See the <i>FTPtransfer.pm</i> for inspiration.</p>
<h2>2.0.8 to 2.0.9</h2>
<h3>FPing</h3>
<p>The &#8216;timeout&#8217; variable removed in 2.0.5 has been brought back. It is used to give the <tt>&quot;fping&quot;</tt> command the <tt>&quot;-t&quot;</tt> parameter, which apparently affects the timeout of the last ping in the counting (<tt>&quot;-C&quot;</tt>) mode used by Smokeping.</p>
<h2>2.0.5 to 2.0.6</h2>
<h3><font SIZE="-1">CGI</font> self-referring links (again)</h3>
<p>The way Smokeping creates the self-referring links was changed once more. See the section under &#8216;2.0.4 to 2.0.5&#8217; for a description of the previous change. </p>
<p> The behaviour is now customizable via the <tt>&quot;linkstyle&quot;</tt> variable in the <tt>&quot;General&quot;</tt> section of the configuration file. The default is now <tt>&quot;relative&quot;</tt>, creating links like &lt;a href=&#8220;?foo=bar&#8221;&gt;. I hope this works for everybody, but if it doesn&#8217;t, see smokeping_config for the alternatives.</p>
<h2>2.0.4 to 2.0.5</h2>
<h3>FPing</h3>
<p>The &#8216;timeout&#8217; variable has been removed. It was used to give the <tt>&quot;fping&quot;</tt> command the <tt>&quot;-t&quot;</tt> parameter, but as this parameter is only effective in <tt>&quot;fping&quot;</tt>&#8216;s <i>default</i> mode, while Smokeping uses the <i>counting</i> mode (<tt>&quot;-c&quot;</tt>), it never actually did anything.</p>
<h3><font SIZE="-1">CGI</font> self-referring links</h3>
<p>The way Smokeping creates the self-referring links was changed. The old behaviour used the script name but not the host part, resulting in links like &lt;a href=&#8220;/path/smokeping.cgi?foo=bar&#8221;&gt;. The new behaviour uses the <tt>&quot;cgiurl&quot;</tt> variable: the links are always absolute like &lt;a href=&#8220;<a rel="nofollow" href="http://some.host/path/smokeping.cgi?foo=bar''">http://some.host/path/smokeping.cgi?foo=bar&#8221;</a>&gt;.</p>
<h2>2.0.1 to 2.0.2</h2>
<h3>Edge-triggered alerts</h3>
<p>The alert notifications can now optionally be sent only when the state of the alert changes. This means that only the first match of the alert generates a notification, subsequent matches don&#8217;t. When the alert is cleared, ie. there&#8217;s no match anymore, another notification is sent. </p>
<p> This behaviour is enabled by the <tt>&quot;edgetrigger&quot;</tt> variable in the <tt>&quot;Alerts&quot;</tt> section. The old behaviour (which sends a notification on each match) is the default.</p>
<h2>1.40 to 2.0</h2>
<p>The biggest change with the 2.0 release is that the configuration file is now parsed much more strictly. This should result in (hopefully understandable) error messages making the configuration less of the trial-and-error variety than it used to be. It also automates the generation of the configuration documentation from the source code, so the docs are now more accurate. </p>
<p> A smaller change worth mentioning is the inclusion of the tSmoke script (contributed by Dan McGinn-Combs) for sending summary emails on daily and weekly system status. Note that it needs the new &#8216;tmail&#8217; variable to be defined in the config file.</p>
<h3><font SIZE="-1">CONFIGURATION</font></h3>
<p>The configuration syntax has stayed mostly the same, except for the issues below.</p>
<dl>
<dt><font SIZE="-1">PROBE_CONF</font></p>
<dd>The <font SIZE="-1">PROBE_CONF</font> subsections have been deprecated. All the target-specific variables are now configured in the same section as the target is. Just deleting the </p>
<p> ++ <font SIZE="-1">PROBE_CONF</font> </p>
<p> lines should fix this (for any number of &#8216;+&#8217;, obviously.) </p>
<p> The existence of a <font SIZE="-1">PROBE_CONF</font> section makes smokeping exit with an error message at parse time. </p>
<p> Note for distributors: these lines could easily be removed automatically during upgrade.</p>
<dt>Variable order</p>
<dd>The <tt>&quot;probe&quot;</tt> variable must now be set before any variables that depend on the selected probe. This is because setting <tt>&quot;probe&quot;</tt> modifies the grammar of the rest of the section dynamically at parse time. </p>
<p> Additionally, <tt>&quot;probe&quot;</tt> must now precede <tt>&quot;host&quot;</tt>, for reasons that have to do with the current implementation of mandatory variable checking. </p>
<p> Both of these errors are recognized at parse time and produce error messages accordingly. </p>
<p> Note for distributors: the <tt>&quot;smokeping&quot;</tt> command now has a new &#8216;&#8211;check&#8217; option that can be used to verify the syntax of the configuration file. It might be a good idea to do this on upgrade and give the user an explanatory note if the verification fails.</p>
<dt>Target-specific variables in the Probes section</p>
<dd>This is not an incompatible change, but it is mentioned here nevertheless. Target-specific variables can now be specified in the Probes section as well, and the values given become defaults for all the targets.</p>
<dt>Timeouts</p>
<dd>The <tt>&quot;timeout&quot;</tt> variable in the Probes section is now the maximum time expected for <code>one</code> ping to take. Previously it was the maximum time allowed for all the pings to one target. This is an incompatible change, but the code now works in the way it was documented to work even in 1.38. </p>
<p> Those probes offering a target-specific <tt>&quot;timeout&quot;</tt> variable will get a default for it from the Probes section, as noted in the previous item. This should ensure that probes that enforce the ping timeout themselves (most do) will not get killed due to timeout before they have a chance to do it.</p>
<dt>Matchers</p>
<dd>The matcher modules have been renamed to start with a capital letter, to differentiate the actual modules from the base classes. You have to capitalize the matcher name in the pattern definition accordingly.</p>
<dt>Minimum number of pings</p>
<dd>The <tt>&quot;pings&quot;</tt> variable now has an enforced minimum value of 3, as the whole design of Smokeping is based on the idea of sending several probes and measuring and visualizing the variation between them.</p>
<dt><font SIZE="-1">RRD</font> parameter checking</p>
<dd>Smokeping now checks at startup that the parameters of any existing <font SIZE="-1">RRD</font> files match those specified in the configuration file. If there is a discrepancy, it will try to fix the situation and refuse to start if it can&#8217;t. </p>
<p> This situation is most likely to happen if you have modified the <tt>&quot;pings&quot;</tt> variable in your configuration file. You&#8217;ll then have to delete the old <font SIZE="-1">RRD</font> file or somehow convert it to use the new parameters. The <tt>&quot;rrdtune&quot;</tt> command might be helpful here.</p>
<dt>Configurable location for DYNAMIC-related files</p>
<dd>There is now a new configuration variable, <tt>&quot;dyndir&quot;</tt>, that can be used to specify the location of the DYNAMIC-related files (.adr and .snmp). These files used to be kept under <tt>&quot;datadir&quot;</tt> along with the <font SIZE="-1">RRD</font> files, but since they need to be writable by the web server, it may be useful to separate these. </p>
<p> If <tt>&quot;dyndir&quot;</tt> is not specified, Smokeping will use the <tt>&quot;datadir&quot;</tt> value as the default. This should ensure that no existing setups will break.</dl>
<p> In addition to this, some probes have had minor incompatible changes to their configuration.</p>
<dl>
<dt>RemoteFPing</p>
<dd>The <tt>&quot;rbinary&quot;</tt> variable is now mandatory. This is a side effect from a bigger change: the probe is now derived from the FPing probe and supports all the variables FPing does.</p>
<dt>FPing6</p>
<dd>This probe is also now derived from FPing and supports all the variables FPing does.</p>
<dt>Curl</p>
<dd>The <font SIZE="-1">URL</font> that will be used is now specified with the variable <tt>&quot;urlformat&quot;</tt> instead of <tt>&quot;url&quot;</tt>. The new variable can (and usually should) include a placeholder for the <tt>&quot;host&quot;</tt> variable of each target as <tt>&quot;%host%&quot;</tt>, eg. <tt>&quot;urlformat = <a rel="nofollow" href="http://%host%/">http://%host%/</a>&quot;</tt>. The new variable is mandatory. </p>
<p> The change was made to fix the confusing situation where the <tt>&quot;host&quot;</tt> variable was required for each actual target, but it didn&#8217;t actually have any effect (as the server to be probed came from the <tt>&quot;url&quot;</tt> variable.) </p>
<p> Timeouts are now recognized properly by looking at the curl exit code. The default timeout of this probe has been raised to 10 seconds. </p>
<p> The command line is now executed without an intervening /bin/sh, and so quotes are not needed anymore around the User-Agent string (the <tt>&quot;agent&quot;</tt> parameter). Smokeping will complain if it notices quotes around the string. </p>
<p> Any extra arguments for <tt>&quot;curl&quot;</tt> can now be specified in the <tt>&quot;extraargs&quot;</tt> variable.</p>
<dt>EchoPingHttp</p>
<dd>The default timeout of this probe has been raised to 10 seconds.</p>
<dt>EchoPingHttps</p>
<dd>The default timeout of this probe has been raised to 10 seconds.</p>
<dt>EchoPingIcp</p>
<dd>The <tt>&quot;url&quot;</tt> variable is now mandatory, as the old default &#8220;/&#8221; didn&#8217;t make sense because it&#8217;s relative rather than absolute.</p>
<dt><font SIZE="-1">LDAP</font></p>
<dd>The <tt>&quot;filter&quot;</tt> variable is now mandatory, as Net::LDAP bails out without it. </p>
<p> The <tt>&quot;sleeptime&quot;</tt> variable was changed to <tt>&quot;mininterval&quot;</tt> and its semantics were changed accordingly (it&#8217;s now the minimum time between two queries rather than the time slept between the end of one and the start of the another.)</p>
<dt>Radius</p>
<dd>The <tt>&quot;sleeptime&quot;</tt> variable was changed to <tt>&quot;mininterval&quot;</tt> and its semantics were changed accordingly. See the <font SIZE="-1">LDAP</font> explanation above.</p>
<dt>AnotherDNS</p>
<dd>The <tt>&quot;sleeptime&quot;</tt> variable was changed to <tt>&quot;mininterval&quot;</tt> and its semantics were changed accordingly. See the <font SIZE="-1">LDAP</font> explanation above. Additionally, the time is now specified in seconds rather than microseconds.</p>
<dt>AnotherSSH</p>
<dd>The <tt>&quot;sleeptime&quot;</tt> variable was changed to <tt>&quot;mininterval&quot;</tt> and its semantics were changed accordingly. See the <font SIZE="-1">LDAP</font> explanation above. Additionally, the time is now specified in seconds rather than microseconds.</p>
<dt>TelnetIOSPing</p>
<dd>The name of this probe was changed: it now starts with a capital letter like all the others do. </p>
<p> The <tt>&quot;target&quot;</tt> variable was removed. The target should now be specified in the <tt>&quot;host&quot;</tt> variable, like it is with all the other probes.</dl>
<h3>CGI::Carp module version</h3>
<p>The recommended version for CGI::Carp is now at least 1.24, included in <font SIZE="-1">CGI</font>.pm-2.82 and the Perl standard distribution starting from 5.8.1. See the smokeping_install document.</p>
<h2>1.38 to 1.40</h2>
<dl>
<dt>The new navigation feature</p>
<dd>The big visible difference between 1.38 and 1.40 is the new browser navigation feature: when clicking on the graphs in detail view you can select different time ranges for the graph. The creation of this feature has been sponsored by BeverlyCorp.com.</dl>
<h2>1.34 to 1.37</h2>
<dl>
<dt>The RemoteFPing probe</p>
<dd>The configuration of this probe was moved from the Targets section to the Probes section, as all the variables are really probe-specific. The moved variables were <tt>&quot;rhost&quot;</tt>, <tt>&quot;rbinary&quot;</tt> and <tt>&quot;rhost&quot;</tt>.</p>
<dt>Logging changes</p>
<dd>The <tt>&quot;smokeping&quot;</tt> daemon now warns at startup if syslog support is not turned on in the config file. This is because many diagnostic messages will otherwise get lost.</p>
<dt>Concurrent probes</p>
<dd>Each probe now runs in its own process, instead of them all running sequentially in one process. This makes it possible to specify different step lengths for different probes. You can get the old behaviour back by setting &#8216;concurrentprobes = no&#8217;.</dl>
<h2>Copyright</h2>
<p>Copyright 2005 by Niko Tyni.</p>
<h2>License</h2>
<p>This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font></p>
<h2>Author</h2>
<p>Niko Tyni &lt;ntyni [at] iki.fi&gt;</p>
<h2>See Also</h2>
<p>The other Smokeping documents, especially smokeping_config. </p>
