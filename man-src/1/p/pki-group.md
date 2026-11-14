---
title: "pki-group(1)"
name: "pki-group"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-group/"
description: "pki-group – Command-Line Interface for managing Certificate System groups."
---

<h2 class="name">NAME</h2>
<p> pki-group &#8211; Command-Line Interface for managing Certificate System groups.</p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options]&lt;subsystem&gt; - group pki[CLI options]&lt;subsystem&gt; - group - find[command options] pki[CLI options]&lt;subsystem&gt; - group - show&lt;group ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - group - add&lt;group ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - group - mod&lt;group ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - group - del&lt;group ID&gt;[command options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki-group</code> commands provide command-line interfaces to manage groups on the specified subsystem. </p>
<p> Valid subsystems are <code>ca</code>, <code>kra</code>, <code>ocsp</code>, <code>tks</code>, and <code>tps</code>. If the <code>&lt;subsystem&gt;-</code> prefix is omitted, it will default to <code>ca</code>. </p>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-group</code></p>
<dl>
<dt>
<dd> This command is to list available group commands for the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-group-find</code> [command options]</p>
<dl>
<dt>
<dd> This command is to list groups in the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-group-show</code> &lt;group ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to view a group details in the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-group-add</code> &lt;group ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to add a group into the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-group-mod</code> &lt;group ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to modify a group in the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-group-del</code> &lt;group ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to delete a group from the subsystem.</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available group commands, type <code>pki &lt;subsystem&gt;-group</code>. To view each command&#8217;s usage, type <code> pki &lt;subsystem&gt;-group-&lt;command&gt; &#8211;help</code>. </p>
<p> All group commands must be executed as the subsystem administrator. </p>
<p> For example, to list groups in CA execute the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-group-find</code> </p>
<p> The results can be paged by specifying the (0-based) index of the first entry to return and the maximum number of entries returned: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-group-find &#8211;start 20 &#8211;size 10</code> </p>
<p> The above command will return entries #20 to #29. </p>
<p> To view a CA group, specify the group ID in the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-group-show testgroup</code> </p>
<p> To add a CA group, specify the group ID in the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-group-add testgroup</code> </p>
<p> To modify a CA group, specify the group ID and the attributes to be modified in the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-group-mod testgroup &#8211;description &#8220;Test Group&#8221;</code> </p>
<p> To delete a CA group, specify the group ID in the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-group-del testgroup</code> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pki-group-member/">pki-group-member</a></code>(1)</p>
<dl>
<dt>
<dd> Group member management commands</dl>
<h2>AUTHORS</h2>
<p> Ade Lee &lt;alee [at] redhat.com&gt;, Endi Dewata &lt;edewata [at] redhat.com&gt;, and Matthew Harmsen &lt;mharmsen [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2014 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>Index</h2>
