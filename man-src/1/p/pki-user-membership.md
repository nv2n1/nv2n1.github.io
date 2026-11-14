---
title: "pki-user-membership(1)"
name: "pki-user-membership"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-user-membership/"
description: "pki-user-membership – Command-Line Interface for managing Certificate System user memberships."
---

<h2 class="name">NAME</h2>
<p> pki-user-membership &#8211; Command-Line Interface for managing Certificate System user memberships.</p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options]&lt;subsystem&gt; - user - membership pki[CLI options]&lt;subsystem&gt; - user - membership - find&lt;user ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - user - membership - add&lt;user ID&gt;&lt;group ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - user - membership - del&lt;user ID&gt;&lt;group ID&gt;[command options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki-user-membership</code> commands provide command-line interfaces to manage user memberships on the specified subsystem. </p>
<p> Valid subsystems are <code>ca</code>, <code>kra</code>, <code>ocsp</code>, <code>tks</code>, and <code>tps</code>. If the <code>&lt;subsystem&gt;-</code> prefix is omitted, it will default to <code>ca</code>. </p>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-user-membership</code></p>
<dl>
<dt>
<dd> This command is to list available user membership commands for the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-user-membership-find</code> &lt;user ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to list groups in which the subsystem user is a member.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-user-membership-add</code> &lt;user ID&gt; &lt;group ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to add the subsystem user into a group.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-user-membership-del</code> &lt;user ID&gt; &lt;group ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to delete the subsystem user from a group.</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available user membership commands, type <code>pki &lt;subsystem&gt;-user-membership</code>. To view each command&#8217;s usage, type <code> pki &lt;subsystem&gt;-user-membership-&lt;command&gt; &#8211;help</code>. </p>
<p> All user membership commands must be executed as the subsystem administrator. </p>
<p> For example, to list groups in which a CA user is a member execute the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-membership-find testuser</code> </p>
<p> The results can be paged by specifying the (0-based) index of the first entry to return and the maximum number of entries returned: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-membership-find testuser &#8211;start 20 &#8211;size 10</code> </p>
<p> The above command will return entries #20 to #29. </p>
<p> To add a CA user into a group, specify the user ID and the group ID in the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-membership-add testuser Administrators</code> </p>
<p> To delete a CA user from a group, specify the user ID and the group ID in the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-membership-del testuser Administrators</code> </p>
<h2>AUTHORS</h2>
<p> Endi S. Dewata &lt;edewata [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2015 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>Index</h2>
