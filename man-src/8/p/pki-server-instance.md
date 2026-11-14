---
title: "pki-server-instance(8)"
name: "pki-server-instance"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pki-server-instance/"
description: "pki-server-instance – Command-Line Interface for managing Certificate System instances."
---

<p>pki-server-instance &#8211; Command-Line Interface for managing Certificate System instances.</p>
<h2>Synopsis</h2>
<pre><code>pki-server [CLI options] instance</code>
<code>pki-server [CLI options] instance-cert</code>
<code>pki-server [CLI options] instance-cert-export</code>
<code>pki-server [CLI options] instance-find</code>
<code>pki-server [CLI options] instance-show</code> &lt;instance ID&gt;
<code>pki-server [CLI options] instance-start</code> &lt;instance ID&gt;
<code>pki-server [CLI options] instance-stop</code> &lt;instance ID&gt;
<code>pki-server [CLI options] instance-migrate</code> --tomcat &lt;version&gt; &lt;instance ID&gt;
<code>pki-server [CLI options] instance-nuxwdog-enable</code> &lt;instance ID&gt;
<code>pki-server [CLI options] instance-nuxwdog-disable</code> &lt;instance ID&gt;
<code>pki-server [CLI options] instance-externalcert-add</code> -i &lt;instance ID&gt;
 --cert-file &lt;path&gt; --trust-args &lt;args&gt; --nickname &lt;nickname&gt; --token &lt;token&gt;
<code>pki-server [CLI options] instance-externalcert-del</code> -i &lt;instance ID&gt;
 --nickname &lt;nickname&gt; --token &lt;token&gt;</pre>
<h2>Description</h2>
<p>The <code>pki-server instance</code> commands provide command-line interfaces to manage Certificate Server (CS) instances. A Certificate Server instance consists of a single Apache Tomcat instance that contains one or more CS subsystems. Operations that are available include: listing and showing details about local instances; starting and stopping instances; performing instance migrations; and enabling or disabling password prompted instance startup using <code>nuxwdog</code>. <code>pki-server [CLI options] instance</code></p>
<dl>
<dd>This command is to list available instance commands.</dl>
<p> <code>pki-server [CLI options] instance-cert</code></p>
<dl>
<dd>This command is to list available instance certificate commands.</dl>
<p> <code>pki-server [CLI options] instance-cert-export</code></p>
<dl>
<dd>This command is to export system certificates and keys to a PKCS #12 file. The output filename and either a password or a password file are required. If no nicknames are specified, all the system certificates will be exported. Otherwise, it is possible to extract individual certificates (with or without their keys and trust arguments), and to append to an existing PKCS #12 file.</dl>
<p> <code>pki-server [CLI options] instance-find</code></p>
<dl>
<dd>This command is to list local CS instances.</dl>
<p> <code>pki-server [CLI options] instance-show</code> &lt;instance ID&gt;</p>
<dl>
<dd>This command is to view a details about a particular instance.</dl>
<p> <code>pki-server [CLI options] instance-start</code> &lt;instance ID&gt;</p>
<dl>
<dd>This command is to start a CS instance. Note that currently this command cannot be used to start <code>nuxwdog</code>-enabled instances.</dl>
<p> <code>pki-server [CLI options] instance-stop</code> &lt;instance ID&gt;</p>
<dl>
<dd>This command is to stop a CS instance. Note that currently this command cannot be used to stop <code>nuxwdog</code>-enabled instances.</dl>
<p> <code>pki-server [CLI options] instance-migrate</code> &#8211;tomcat &lt;version&gt; &lt;instance_ID&gt;</p>
<dl>
<dd>There are differences in configuration between Apache Tomcat 7 and Apache Tomcat 8. This command reconfigures a CS instance to match the specified Tomcat version. This command can be used to migrate initially created under Tomcat 7 when Tomcat is upgraded.. See <code>pki-server <a href="/docs/linux/man/8-migrate/">migrate</a></code>(8) for further details.</dl>
<p> <code>pki-server [CLI options] instance-nuxwdog-enable</code> &lt;instance ID&gt;</p>
<dl>
<dd>This command is to convert a CS instance to start without access to a password file, using the <code>nuxwdog</code> daemon. See <code>pki-server <a href="/docs/linux/man/8-nuxwdog/">nuxwdog</a></code>(8) for further details.</dl>
<p> <code>pki-server [CLI options] instance-nuxwdog-disable</code> &lt;instance ID&gt;</p>
<dl>
<dd>This command is to convert a CS instance to start with access to a password file, rather than using the <code>nuxwdog</code> daemon. See <code>pki-server <a href="/docs/linux/man/8-nuxwdog/">nuxwdog</a></code>(8) for further details.</dl>
<p> <code>pki-server [CLI options] instance-externalcert-add</code> -i &lt;instance ID&gt;<br />
&nbsp;<wbr>&#8211;cert-file&nbsp;<wbr>&lt;path&gt;&nbsp;<wbr>&#8211;trust-args&nbsp;<wbr>&lt;args&gt;&nbsp;<wbr>&#8211;nickname&nbsp;<wbr>&lt;nickname&gt;&nbsp;<wbr>&#8211;token&nbsp;<wbr>&lt;token&gt;</p>
<dl>
<dd>This command is to add a certificate to the certificate database for a CS instance. The certificate will be kept track of in the configuration file <code>external_certs.conf</code>, and will automatically be exported when the system certificates are exported. To update a certificate, the old one needs to be removed first using the delete command below. The trust arguments are those defined for NSS databases eg. &quot;C,c,c&quot;. See <code><a href="/docs/linux/man/1-certutil/">certutil</a>(1)</code> for more details.</dl>
<p> <code>pki-server [CLI options] instance-externalcert-del</code> -i &lt;instance ID&gt;<br />
&nbsp;<wbr>&#8211;nickname&nbsp;<wbr>&lt;nickname&gt;&nbsp;<wbr>&#8211;token&nbsp;<wbr>&lt;token&gt;</p>
<dl>
<dd>This command is to remove a certificate from the certificate database for a CS instance.</dl>
<h2>Options</h2>
<p>The CLI options are described in <code><a href="/docs/linux/man/8-pki-server/">pki-server</a></code>(8).</p>
<h2>Operations</h2>
<p>To view available instance management commands, type <code>pki-server instance</code>. To view each command&#8217;s usage, type <code> pki-server instance-&lt;command&gt; &#8211;help</code>. </p>
<p> All pki-server commands must be executed as the system administrator.</p>
<h2>Authors</h2>
<p>Ade Lee &lt;alee [at] redhat.com&gt;</p>
<h2>Copyright</h2>
<p>Copyright (c) 2015 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
