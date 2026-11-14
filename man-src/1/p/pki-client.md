---
title: "pki-client(1)"
name: "pki-client"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-client/"
description: "pki-client – Command-Line Interface for managing the security database on Certificate System client."
---

<h2 class="name">NAME</h2>
<p> pki-client &#8211; Command-Line Interface for managing the security database on Certificate System client. </p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options] client
        pki[CLI options] client -
    init[command options] pki[CLI options] client - cert - find[command options] pki[CLI options] client - cert - request[subject DN][command options] pki[CLI options] client - cert - import[nickname][command options] pki[CLI options] client - cert - mod&lt;nickname&gt;[command options] pki[CLI options] client - cert - show&lt;nickname&gt;[command options] pki[CLI options] client - cert - del&lt;nickname&gt;[command options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki-client</code> commands provide command-line interfaces to manage the security database on the client&#8217;s machine. </p>
<p> <code>pki</code> [CLI options] <code>client</code></p>
<dl>
<dt>
<dd> This command is to list available client commands.</dl>
<p> <code>pki</code> [CLI options] <code>client-init</code> [command options]</p>
<dl>
<dt>
<dd> This command is to create a new security database for the client.</dl>
<p> <code>pki</code> [CLI options] <code>client-cert-find</code> [command options]</p>
<dl>
<dt>
<dd> This command is to list certificates in the client security database.</dl>
<p> <code>pki</code> [CLI options] <code>client-cert-request</code> [subject DN] [command options]</p>
<dl>
<dt>
<dd> This command is to generate and submit a certificate request.</dl>
<p> <code>pki</code> [CLI options] <code>client-cert-import</code> [nickname] [command options]</p>
<dl>
<dt>
<dd> This command is to import a certificate into the client security database.</dl>
<p> <code>pki</code> [CLI options] <code>client-cert-mod</code> &lt;nickname&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to modify a certificate in the client security database.</dl>
<p> <code>pki</code> [CLI options] <code>client-cert-show</code> &lt;nickname&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to view a certificate in the client security database.</dl>
<p> <code>pki</code> [CLI options] <code>client-cert-del</code> &lt;nickname&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to delete a certificate from the client security database.</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available client commands, type <code>pki client</code>. To view each command&#8217;s usage, type <code> pki client-&lt;command&gt; &#8211;help</code>. </p>
<p> To create a new database execute the following command: </p>
<p> <code>pki -d &lt;security database location&gt; -c &lt;security database password&gt; client-init</code> </p>
<p> To list certificates in the security database: </p>
<p> <code>pki -d &lt;security database location&gt; -c &lt;security database password&gt; client-cert-find</code> </p>
<p> To request a certificate: </p>
<p> <code>pki -d &lt;security database location&gt; -c &lt;security database password&gt; client-cert-request [subject DN]</code> </p>
<p> The subject DN requirement depends on the certificate profile being requested. Some profiles may require the user to provide a subject DN in a certain format. Some other profiles may generate their own subject DN. </p>
<p> Certain profiles may also require additional authentication. To authenticate, a username and a password can be specified using the &#8211;username and &#8211;password options, respectively. If the subject DN is not specififed the CLI may use the username to generate a default subject DN &quot;UID=&lt;username&gt;&quot;. </p>
<p> To import a certificate from a file into the security database: </p>
<p> <code>pki -d &lt;security database location&gt; -c &lt;security database password&gt; client-cert-import &lt;nickname&gt; &#8211;cert &lt;path&gt;</code> </p>
<p> To import a CA certificate from a file into the security database: </p>
<p> <code>pki -d &lt;security database location&gt; -c &lt;security database password&gt; client-cert-import &lt;nickname&gt; &#8211;ca-cert &lt;path&gt;</code> </p>
<p> To import certificates and private keys from a PKCS #12 file into the security database: </p>
<p> <code>pki -d &lt;security database location&gt; -c &lt;security database password&gt; client-cert-import &#8211;pkcs12 &lt;path&gt; &#8211;pkcs12-password &lt;password&gt;</code> </p>
<p> To import a certificate from CA server into the security database: </p>
<p> <code>pki -d &lt;security database location&gt; -c &lt;security database password&gt; client-cert-import &lt;nickname&gt; &#8211;serial &lt;serial number&gt;</code> </p>
<p> To import a CA certificate from CA server into the security database: </p>
<p> <code>pki -d &lt;security database location&gt; -c &lt;security database password&gt; client-cert-import &lt;nickname&gt; &#8211;ca-server</code> </p>
<p> To modify a certificate&#8217;s trust attributes in the security database: </p>
<p> <code>pki -d &lt;security database location&gt; -c &lt;security database password&gt; client-cert-mod &lt;nickname&gt; &#8211;trust &lt;trust attributes&gt;</code> </p>
<p> To display a certificate in the security database: </p>
<p> <code>pki -d &lt;security database location&gt; -c &lt;security database password&gt; client-cert-show &lt;nickname&gt;</code> </p>
<p> To export a certificate from the security database into a PEM file: </p>
<p> <code>pki -d &lt;security database location&gt; -c &lt;security database password&gt; client-cert-show &lt;nickname&gt; &#8211;cert &lt;path&gt;</code> </p>
<p> To export a certificate chain with the private key from the security database into a PKCS #12 file: </p>
<p> <code>pki -d &lt;security database location&gt; -c &lt;security database password&gt; client-cert-show &lt;nickname&gt; &#8211;pkcs12 &lt;path&gt; &#8211;pkcs12-password &lt;password&gt;</code> </p>
<p> To export a certificate chain with the private key with a password file: </p>
<p> <code>pki -d &lt;security database location&gt; -c &lt;security database password&gt; client-cert-show &lt;nickname&gt; &#8211;pkcs12 &lt;path&gt; &#8211;pkcs12-password-file &lt;path&gt;</code> </p>
<p> To export a client certificate with the private key from the security database into a PEM file: </p>
<p> <code>pki -d &lt;security database location&gt; -c &lt;security database password&gt; client-cert-show &lt;nickname&gt; &#8211;client-cert &lt;path&gt;</code> </p>
<p> To delete a certificate from the security database: </p>
<p> <code>pki -d &lt;security database location&gt; -c &lt;security database password&gt; client-cert-del &lt;nickname&gt;</code> </p>
<h2>AUTHORS</h2>
<p> Ade Lee &lt;alee [at] redhat.com&gt;, Endi Dewata &lt;edewata [at] redhat.com&gt;, and Matthew Harmsen &lt;mharmsen [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2014 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>Index</h2>
