---
title: "pki-securitydomain(1)"
name: "pki-securitydomain"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-securitydomain/"
description: "pki-securitydomain – Command-Line Interface for managing Certificate System security domain."
---

<h2 class="name">NAME</h2>
<p> pki-securitydomain &#8211; Command-Line Interface for managing Certificate System security domain.</p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options] securitydomain
        pki[CLI options] securitydomain -
    show[command options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki-securitydomain</code> commands provide command-line interfaces to manage the security domain. </p>
<p> <code>pki</code> [CLI options] <code>securitydomain</code></p>
<dl>
<dt>
<dd> This command is to list available security domain commands.</dl>
<p> <code>pki</code> [CLI options] <code>securitydomain-show</code> [command options]</p>
<dl>
<dt>
<dd> This command is to show the contents of the security domain.</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available security domain commands, type <code>pki securitydomain</code>. To view each command&#8217;s usage, type <code> pki securitydomain-&lt;command&gt; &#8211;help</code>. </p>
<p> To show the contents of the security domain: </p>
<p> <code>pki &lt;security domain admin authentication&gt; securitydomain-show</code> </p>
<h2>AUTHORS</h2>
<p> Ade Lee &lt;alee [at] redhat.com&gt;, Endi Dewata &lt;edewata [at] redhat.com&gt;, and Matthew Harmsen &lt;mharmsen [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2014 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>Index</h2>
