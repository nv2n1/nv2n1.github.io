---
title: "pki-group-member(1)"
name: "pki-group-member"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-group-member/"
description: "pki-group-member – Command-Line Interface for managing Certificate System group members."
---

<h2 class="name">NAME</h2>
<p> pki-group-member &#8211; Command-Line Interface for managing Certificate System group members.</p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options]&lt;subsystem&gt; - group - member pki[CLI options]&lt;subsystem&gt; - group - member - find&lt;group ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - group - member - show&lt;group ID&gt;&lt;member ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - group - member - add&lt;group ID&gt;&lt;member ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - group - member - del&lt;group ID&gt;&lt;member ID&gt;[command options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki-group-member</code> commands provide command-line interfaces to manage group members on the specified subsystem. </p>
<p> Valid subsystems are <code>ca</code>, <code>kra</code>, <code>ocsp</code>, <code>tks</code>, and <code>tps</code>. If the <code>&lt;subsystem&gt;-</code> prefix is omitted, it will default to <code>ca</code>. </p>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-group-member</code></p>
<dl>
<dt>
<dd> This command is to list available group member commands for the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-group-member-find</code> &lt;group ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to list group members in the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-group-member-show</code> &lt;group ID&gt; &lt;member ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to view a group member details in the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-group-member-add</code> &lt;group ID&gt; &lt;member ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to add a member to a group in the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-group-member-del</code> &lt;group ID&gt; &lt;member ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to delete a member from a group in the subsystem.</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available group commands, type <code>pki &lt;subsystem&gt;-group-member</code>. To view each command&#8217;s usage, type <code> pki &lt;subsystem&gt;-group-member-&lt;command&gt; &#8211;help</code>. </p>
<p> All group commands must be executed as the subsystem administrator. </p>
<p> For example, to list members of a CA group execute the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-group-member-find testgroup</code> </p>
<p> The results can be paged by specifying the (0-based) index of the first entry to return and the maximum number of entries returned: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-group-member-find &#8211;start 20 &#8211;size 10</code> </p>
<p> The above command will return entries #20 to #29. </p>
<p> To view a member of a CA group, specify the group ID and the member ID in the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-group-member-show testgroup testuser</code> </p>
<p> To add a member to a CA group, specify the group ID and the member ID in the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-group-member-add testgroup testuser</code> </p>
<p> To delete a member from a CA group, specify the group ID and the member ID in the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-group-member-del testgroup testuser</code> </p>
<h2>AUTHORS</h2>
<p> Endi S. Dewata &lt;edewata [at] redhat.com&gt; </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2015 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>Index</h2>
