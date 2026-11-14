---
title: "pki-user-cert(1)"
name: "pki-user-cert"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-user-cert/"
description: "pki-user-cert – Command-Line Interface for managing Certificate System user certificates."
---

<h2 class="name">NAME</h2>
<p> pki-user-cert &#8211; Command-Line Interface for managing Certificate System user certificates.</p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options]&lt;subsystem&gt; - user - cert pki[CLI options]&lt;subsystem&gt; - user - cert - find&lt;user ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - user - cert - show&lt;user ID&gt;&lt;cert ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - user - cert - add&lt;user ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - user - cert - del&lt;user ID&gt;&lt;cert ID&gt;[command options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki-user-cert</code> commands provide command-line interfaces to manage user certificates on the specified subsystem. </p>
<p> Valid subsystems are <code>ca</code>, <code>kra</code>, <code>ocsp</code>, <code>tks</code>, and <code>tps</code>. If the <code>&lt;subsystem&gt;-</code> prefix is omitted, it will default to <code>ca</code>. </p>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-user-cert</code></p>
<dl>
<dt>
<dd> This command is to list available user certificate commands for the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-user-cert-find</code> &lt;user ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to list certificates owned by the subsystem user.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-user-cert-show</code> &lt;user ID&gt; &lt;cert ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to view the details of a certificate owned to the subsystem user.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-user-cert-add</code> &lt;user ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to add a certificate to the subsystem user.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-user-cert-del</code> &lt;user ID&gt; &lt;cert ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to delete a certificate from the subsystem user.</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available user certificate commands, type <code>pki &lt;subsystem&gt;-user-cert</code>. To view each command&#8217;s usage, type <code> pki &lt;subsystem&gt;-user-cert-&lt;command&gt; &#8211;help</code>. </p>
<p> All user certificate commands must be executed as the subsystem administrator. </p>
<p> For example, to list certificates owned by a CA user execute the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-cert-find testuser</code> </p>
<p> The results can be paged by specifying the (0-based) index of the first entry to return and the maximum number of entries returned: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-cert-find testuser &#8211;start 20 &#8211;size 10</code> </p>
<p> The above command will return entries #20 to #29. </p>
<p> To view a certificate owned by a CA user, specify the user ID and the certificate ID in the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-cert-show testuser &#8220;2;11;CN=CA Signing Certificate,O=EXAMPLE;UID=testuser&#8221;</code> </p>
<p> To add a certificate to a CA user from a file, specify the user ID and the input file: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-cert-add testuser &#8211;input testuser.crt</code> </p>
<p> To add a certificate to a CA user from the certificate repository, specify the user ID and the serial number: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-cert-add testuser &#8211;serial 0x80</code> </p>
<p> To delete a certificate from a CA user, specify the user ID and the certificate ID in the following command: </p>
<p> <code>pki &lt;CA admin authentication&gt; ca-user-cert-del testuser &#8220;2;11;CN=CA Signing Certificate,O=EXAMPLE;UID=testuser&#8221;</code> </p>
<h2>AUTHORS</h2>
<p> Endi S. Dewata &lt;edewata [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2015 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>Index</h2>
