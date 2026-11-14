---
title: "pki-audit(1)"
name: "pki-audit"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-audit/"
description: "pki-audit – Command-Line Interface for managing Certificate System audit configuration."
---

<h2 class="name">NAME</h2>
<p> pki-audit &#8211; Command-Line Interface for managing Certificate System audit configuration.</p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options]&lt;subsystem&gt; - audit pki[CLI options]&lt;subsystem&gt; - audit - show[command options] pki[CLI options]&lt;subsystem&gt; - audit - mod-- action&lt;action&gt;[command options] pki[CLI options]&lt;subsystem&gt; - audit - mod-- input&lt;input file&gt;[command options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki-audit</code> commands provide command-line interfaces to manage audit configuration in the specified subsystem. Currently the only supported subsystem is <code>tps</code>. </p>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-audit</code></p>
<dl>
<dt>
<dd> This command is to list the available audit commands for the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-audit-show</code> [command options]</p>
<dl>
<dt>
<dd> This command is to show the audit configuration in the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-audit-mod &#8211;action &lt;action&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to change the audit (enabled/disabled) status in the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-audit-mod &#8211;input &lt;input file&gt;</code> [command options]</p>
<dl>
<dt>
<dd> This command is to modify the audit configuration in the subsystem.</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available audit commands, type <code>pki &lt;subsystem&gt;-audit</code>. To view each command&#8217;s usage, type <code> pki &lt;subsystem&gt;-audit-&lt;command&gt; &#8211;help</code>. </p>
<p> All audit commands must be executed with the subsystem&#8217;s admin authentication (the user must be in the Administrators group). See also the Authentication section in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h3>Viewing audit configuration</h3>
<p> To view the audit configuration in TPS execute the following command: </p>
<p> <code>pki &lt;TPS admin authentication&gt; tps-audit-show</code> </p>
<p> To download the audit configuration from TPS into a file execute the following command: </p>
<p> <code>pki &lt;TPS admin authentication&gt; tps-audit-show &#8211;output &lt;output file&gt;</code> </p>
<h3>Changing audit status</h3>
<p> To enable/disable audit in TPS, execute the following command: </p>
<p> <code>pki &lt;TPS admin authentication&gt; tps-audit-mod &#8211;action &lt;action&gt;</code> </p>
<p> where action is enable or disable. </p>
<h3>Modifying audit configuration</h3>
<p> To modify the audit configuration in TPS, download the current configuration using the above <code>tps-audit-show</code> command, edit the file, then execute the following command: </p>
<p> <code>pki &lt;TPS admin authentication&gt; tps-audit-mod &#8211;input &lt;input file&gt;</code> </p>
<p> Optionally, a &#8211;output &lt;output file&gt; option may be specified to download the effective configuration after the modification. </p>
<h2>AUTHORS</h2>
<p> Endi S. Dewata &lt;edewata [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2015 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pki/">pki</a>(1)</code> </p>
<h2>Index</h2>
