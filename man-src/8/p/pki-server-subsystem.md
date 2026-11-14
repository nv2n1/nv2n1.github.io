---
title: "pki-server-subsystem(8)"
name: "pki-server-subsystem"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pki-server-subsystem/"
description: "pki-server-subsystem – Command-Line Interface for managing Certificate System subsystems."
---

<p>pki-server-subsystem &#8211; Command-Line Interface for managing Certificate System subsystems.</p>
<h2>Synopsis</h2>
<pre><code>pki-server [CLI options] subsystem</code>
<code>pki-server [CLI options] subsystem-find</code> -i &lt;instance ID&gt;
<code>pki-server [CLI options] subsystem-show</code> -i &lt;instance ID&gt; &lt;subsystem ID&gt;
<code>pki-server [CLI options] subsystem-enable</code> -i &lt;instance ID&gt; &lt;subsystem ID&gt;
<code>pki-server [CLI options] subsystem-disable</code> -i &lt;instance ID&gt; &lt;subsystem ID&gt;
<code>pki-server [CLI options] subsystem-cert-find</code> -i &lt;instance ID&gt; &lt;subsystem ID&gt;
<code>pki-server [CLI options] subsystem-cert-show</code> -i &lt;instance ID&gt; &lt;subsystem ID&gt; &lt;cert ID&gt;
<code>pki-server [CLI options] subsystem-cert-export</code> -i &lt;instance ID&gt; &lt;subsystem ID&gt; &lt;cert ID&gt;
<code>pki-server [CLI options] subsystem-cert-update</code> -i &lt;instance ID&gt; &lt;subsystem ID&gt; &lt;cert ID&gt;</pre>
<h2>Description</h2>
<p>The <code>pki-server subsystem</code> commands provide command-line interfaces to manage Certificate Server (CS) subsystems. A Certificate Server instance consists of a single Apache Tomcat instance that contains one or more CS subsystems. Valid subsystem identifiers are &#8216;<code>ca</code>&#8216;, &#8216;<code>kra</code>&#8216;, &#8216;<code>tks</code>&#8216;, &#8216;<code>ocsp</code>&#8216; and &#8216;<code>tps</code>&#8216;. No instance may have more than one of each type of subsystem. <code>pki-server subsystem</code> commands perform operations on a specific subsystem within a CS instance. Consequently, all <code>pki-server subsystem</code> commands require specification of the instance ID to completely identify the target subsystem. Operations that are available include: listing subsystems in an instance; showing details about a subsystem; and enabling and disabling subsystems. <code>pki-server [CLI options] subsystem</code></p>
<dl>
<dd>This command is to list available subsystem commands.</dl>
<p> <code>pki-server [CLI options] subsystem-find</code> -i &lt;instance ID&gt;</p>
<dl>
<dd>This command is to list subsystems within a specific instance.</dl>
<p> <code>pki-server [CLI options] subsystem-show</code> -i &lt;instance ID&gt; &lt;subsystem ID&gt;</p>
<dl>
<dd>This command is to view the details about a particular subsystem.</dl>
<p> <code>pki-server [CLI options] subsystem-enable</code> -i &lt;instance ID&gt; &lt;subsystem ID&gt;</p>
<dl>
<dd>This command is to enable a particular subsystem. Each subsystem consists of a web application within the Apache Tomcat instance. Enabling a subsystem means deploying the web application so that the application initializes and is accessible via the HTTP and HTTPS ports for the Apache Tomcat instance. <code>Note:</code> Each subsystem runs a set of self-tests on startup. If these self-tests fail, the subsystem will be disabled by undeploying the web application. The deployment status (enabled/disabled) of the subsystem can be determined from the output of <code>pki-server subsystem-show</code>. Once the underlying problem is fixed, the subsystem should be re-enabled using <code>pki-server subsystem-enable</code>.</dl>
<p> <code>pki-server [CLI options] subsystem-disable</code> -i &lt;instance ID&gt; &lt;subsystem ID&gt;</p>
<dl>
<dd>This command is to disable a subsystem by undeploying the web application corresponding to the subsystem. The subsystem will no longer be accessible through the web interfaces. This is useful when specific subsystems need to be made inaccessible for maintenance as Apache Tomcat allows web applications to be deployed/undeployed while the instance is still running (hot deployment).</dl>
<p> <code>pki-server [CLI options] subsystem-cert-find</code> -i &lt;instance ID&gt; &lt;subsystem ID&gt;</p>
<dl>
<dd>This command is to list system certificates in a particular subsystem.</dl>
<p> <code>pki-server [CLI options] subsystem-cert-show</code> -i &lt;instance ID&gt; &lt;subsystem ID&gt; &lt;cert ID&gt;</p>
<dl>
<dd>This command is to view the details about a system certificate in a particular subsystem.</dl>
<p> <code>pki-server [CLI options] subsystem-cert-export</code> -i &lt;instance ID&gt; &lt;subsystem ID&gt; &lt;cert ID&gt;</p>
<dl>
<dd>This command is to export a system certificate in a particular subsystem.</dl>
<p> <code>pki-server [CLI options] subsystem-cert-update</code> -i &lt;instance ID&gt; &lt;subsystem ID&gt; &lt;cert ID&gt;</p>
<dl>
<dd>This command is to update a system certificate in a particular subsystem.</dl>
<h2>Options</h2>
<p>The CLI options are described in <code><a href="/docs/linux/man/8-pki-server/">pki-server</a></code>(8).</p>
<h2>Operations</h2>
<p>To view available subsystem management commands, type <code>pki-server subsystem</code>. To view each command&#8217;s usage, type <code> pki-server subsystem-&lt;command&gt; &#8211;help</code>. </p>
<p> All pki-server commands must be executed as the system administrator.</p>
<h2>Authors</h2>
<p>Ade Lee &lt;alee [at] redhat.com&gt;</p>
<h2>Copyright</h2>
<p>Copyright (c) 2015 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
