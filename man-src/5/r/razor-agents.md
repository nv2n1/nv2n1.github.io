---
title: "razor-agents(5)"
name: "razor-agents"
section: "5"
letter: "r"
url: "/docs/linux/man/5-razor-agents/"
description: "Razor-Agents – Collection of files for checking, reporting, and revoking spam"
---

<p>Razor-Agents &#8211; Collection of files for checking, reporting, and revoking spam</p>
<h2>Description</h2>
<p>Vipul&#8217;s Razor is a distributed, collaborative, spam detection, reporting, and filtering network. The primary focus of the system is to identify and remove all email spam from the internet. Visit the website at <a rel="nofollow" href="http://razor.sourceforge.net/.">http://razor.sourceforge.net/.</a></p>
<h2>Usage</h2>
<p>First a razorhome directory should be created where log, conf, and cached server information will live. This is done via <tt>&quot;-create&quot;</tt> option to <i><a href="/docs/linux/man/1-razor-admin/">razor-admin</a></i>(1). See man page for details. </p>
<p> You can immediately check spam using <i><a href="/docs/linux/man/1-razor-check/">razor-check</a></i>(1). See man page for details. </p>
<p> To report spam, an identity must be registered. This is done via <tt>&quot;-register&quot;</tt> option to <i><a href="/docs/linux/man/1-razor-admin/">razor-admin</a></i>(1). After that, <i><a href="/docs/linux/man/1-razor-report/">razor-report</a></i>(1) and <i><a href="/docs/linux/man/1-razor-revoke/">razor-revoke</a></i>(1) will work flawlessly.</p>
<h2>Configuration</h2>
<p>All Razor-Agents share a configuration file. The contents of the configuration file are detailed in the <i><a href="/docs/linux/man/5-razor-agent-conf/">razor-agent.conf</a></i>(5) manpage. </p>
<p> Config file is computed before razorhome, in the following order: </p>
<pre> -conf=/path/file.conf used if readable, else
 &lt;home&gt;/.razor/razor-agent.conf used if readable, else
 /etc/razor/razor-agent.conf used if readable, else
 all defaults are used.</pre>
<p>To see configuration defaults, do<br />
&nbsp;<wbr>&nbsp;<wbr>razor-admin -create -conf=/tmp/razor2-defaults.conf</p>
<h2>Razorhome</h2>
<p>All Razor-Agents also share a razorhome directory, where identity, logging, and cached information about servers is stored. Razorhome is computed after configuration file, in the following order. </p>
<pre> -home=/tmp/razor/ used if readable, else
 'razorhome' from configuration file used if readable, else
 &lt;home&gt;/.razor/ used if readable, else
 &lt;home&gt;/.razor/ is created. if that fails, 
 no razorhome.
 NOTE: If there is no razorhome, razor-report and razor-revoke will 
 not work unless you specify -ident=/path/identity 
 razor-check will still work.</pre>
<h2>Files</h2>
<p>Besides those listed at the end with their own manpages, Razor Agents also has the following files.</p>
<dl>
<dt><code>razorhome/identity</code></p>
<dd>Usually a symlink to identity file containing user+pass. Used by <i><a href="/docs/linux/man/1-razor-report/">razor-report</a></i>(1) and <i><a href="/docs/linux/man/1-razor-revoke/">razor-revoke</a></i>(1).</p>
<dt><code>razorhome/razor-agent.log</code></p>
<dd>Default log file. To change, edit <i><a href="/docs/linux/man/5-razor-agent-conf/">razor-agent.conf</a></i>(5).</p>
<dt><code>razorhome/servers.*.lst</code></p>
<dd>Cached list of Razor Servers. If more than one, they are ordered by closest ping time.</p>
<dt><code>razorhome/server.&lt;name&gt;.lst</code></p>
<dd>Cached info for &lt;name&gt; server. The <tt>&quot;srl&quot;</tt> key in this file is compared against the server greeting, and if server&#8217;s is greater, new cache info is retrieved from the server.</dl>
<h2>Examples</h2>
<dl>
<dt>razor-check -d -debuglevel=9 mbox</p>
<dd>Checks spam in mbox. prints numbers for those found to be spam. -d logs to stdout, -debuglevel=9 is verbose logging</p>
<dt>razor-admin -create -home=/home/chad/.razor -d -s</p>
<dd>Creates razorhome in /home/chad/.razor, log to stdout, does not connect to server (-s simulate).</p>
<dt>razor-report spam -debuglevel=0</p>
<dd>sends spam to server, with no log msgs.</dl>
<h2>Authors</h2>
<p>Vipul Ved Prakash, &lt;mail [at] vipul.net&gt; and Chad Norwood &lt;chad [at] samo.org&gt;</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-razor-agent-conf/">razor-agent.conf</a></i>(5), <i><a href="/docs/linux/man/1-razor-check/">razor-check</a></i>(1), <i><a href="/docs/linux/man/1-razor-admin/">razor-admin</a></i>(1), <i><a href="/docs/linux/man/1-razor-report/">razor-report</a></i>(1), <i><a href="/docs/linux/man/1-razor-revoke/">razor-revoke</a></i>(1), <i><a href="/docs/linux/man/5-razor-whitelist/">razor-whitelist</a></i>(5) </p>
