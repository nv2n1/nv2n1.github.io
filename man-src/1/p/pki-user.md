---
title: "pki-user(1)"
name: "pki-user"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-user/"
description: "pki-user – Command-Line Interface for managing Certificate System users."
---

<h2 class="name">NAME</h2>
<p> pki-user &#8211; Command-Line Interface for managing Certificate System users.</p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options]&lt;subsystem&gt; - user pki[CLI options]&lt;subsystem&gt; - user - find[command options] pki[CLI options]&lt;subsystem&gt; - user - show&lt;user ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - user - add&lt;user ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - user - mod&lt;user ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - user - del&lt;user ID&gt;[command options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki-user</code> commands provide command-line interfaces to manage users on the specified subsystem. </p>
<p> Valid subsystems are <code>ca</code>, <code>kra</code>, <code>ocsp</code>, <code>tks</code>, and <code>tps</code>. If the <code>&lt;subsystem&gt;-</code> prefix is omitted, it will default to <code>ca</code>. </p>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-user</code></p>
<dl>
<dt>
<dd> This command is to list available user commands for the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-user-find</code> [command options]</p>
<dl>
<dt>
<dd> This command is to list users in the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-user-show</code> &lt;user ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to view a user details in the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-user-add</code> &lt;user ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to add a user into the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-user-mod</code> &lt;user ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to modify a user in the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-user-del</code> &lt;user ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to delete a user from the subsystem.</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available user commands, type <code>pki &lt;subsystem&gt;-user</code>. To view each command&#8217;s usage, type <code> pki &lt;subsystem&gt;-user-&lt;command&gt; &#8211;help</code>. </p>
<p> All user commands must be executed as the subsystem administrator. </p>
<p> For example, to list users in CA execute the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-find</code> </p>
<p> The results can be paged by specifying the (0-based) index of the first entry to return and the maximum number of entries returned: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-find &#8211;start 20 &#8211;size 10</code> </p>
<p> The above command will return entries #20 to #29. </p>
<p> To view the details of a CA user, specify the user ID in the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-show testuser</code> </p>
<p> To add a new CA user, specify the user ID and at least the full name in the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-add testuser &#8211;fullName &#8220;Test User&#8221;</code> </p>
<p> To modify a CA user, specify the user ID and the attributes to be changed in the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-mod testuser &#8211;email testuser [at] example.com &#8211;phone 123-456-7890</code> </p>
<p> To delete a CA user, specify the user ID in the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-del testuser</code> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pki-user-cert/">pki-user-cert</a></code>(1)</p>
<dl>
<dt>
<dd> User certificate management commands</dl>
<h2>AUTHORS</h2>
<p> Ade Lee &lt;alee [at] redhat.com&gt;, Endi Dewata &lt;edewata [at] redhat.com&gt;, and Matthew Harmsen &lt;mharmsen [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2014 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>Index</h2>
