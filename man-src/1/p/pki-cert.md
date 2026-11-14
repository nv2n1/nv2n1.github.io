---
title: "pki-cert(1)"
name: "pki-cert"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-cert/"
description: "pki-cert – Command-Line Interface for managing certificates on the Certificate System server."
---

<h2 class="name">NAME</h2>
<p> pki-cert &#8211; Command-Line Interface for managing certificates on the Certificate System server.</p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options]&lt;subsystem&gt; - cert pki[CLI options]&lt;subsystem&gt; - cert - find[command options] pki[CLI options]&lt;subsystem&gt; - cert - show&lt;certificate ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - cert - revoke&lt;certificate ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - cert - hold&lt;certificate ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - cert - release - hold&lt;certificate ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - cert - request - profile - find[command options] pki[CLI options]&lt;subsystem&gt; - cert - request - profile - show&lt;profile ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - cert - request - submit[command options] pki[CLI options]&lt;subsystem&gt; - cert - request - review&lt;request ID&gt;[command options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki-cert</code> commands provide command-line interfaces to manage certificates on the specified subsystem. </p>
<p> Valid subsystems are <code>ca</code> and <code>tps</code>. If the &lt;subsystem&gt;- prefix is omitted, it will default to <code>ca</code>. </p>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-cert</code></p>
<dl>
<dt>
<dd> This command is to list available certificate commands for the subsystem. Different subsystems may have different certificate commands.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-cert-find</code> [command options]</p>
<dl>
<dt>
<dd> This command is to list certificates in the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-cert-show</code> &lt;certificate ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to view a certificate details in the subsystem.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-cert-revoke</code> &lt;certificate ID&gt;</p>
<dl>
<dt>
<dd> This command is to revoke a certificate.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-cert-hold</code> &lt;certificate ID&gt;</p>
<dl>
<dt>
<dd> This command is to place a certificate on hold temporarily.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-cert-release-hold</code> &lt;certificate ID&gt;</p>
<dl>
<dt>
<dd> This command is to release a certificate that has been placed on hold.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-cert-request-profile-find</code> [command options]</p>
<dl>
<dt>
<dd> This command is to list available certificate request templates.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-cert-request-profile-show</code> &lt;profile ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to view a certificate request template.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-cert-request-submit</code> [command options]</p>
<dl>
<dt>
<dd> This command is to submit a certificate request.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-cert-request-review</code> &lt;request ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to review a certificate request.</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available certificate commands, type <code>pki &lt;subsystem&gt;-cert</code>. To view each command&#8217;s usage, type <code> pki &lt;subsystem&gt;-cert-&lt;command&gt; &#8211;help</code>. </p>
<h3>Viewing Certificates</h3>
<p> Certificates can be viewed anonymously. </p>
<p> To list all certificates in the CA: </p>
<p> <code>pki ca-cert-find</code> </p>
<p> It is also possible to search for and list specific certificates by adding a search filter. Use <code>pki ca-cert-find &#8211;help</code> to see options. For example, to search based on issuance date: </p>
<p> <code>pki ca-cert-find &#8211;issuedOnFrom 2012-06-15</code> </p>
<p> To list certificates with search constraints defined in a file: </p>
<p> <code>pki ca-cert-find &#8211;input &lt;filename&gt;</code> </p>
<p> where the file is in the following format: </p>
<dl>
<dt>
<dd>
<pre>
&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot; standalone=&quot;yes&quot;?&gt;
&lt;CertSearchRequest&gt;
    &lt;serialNumberRangeInUse&gt;true&lt;/serialNumberRangeInUse&gt;
    &lt;serialFrom&gt;&lt;/serialFrom&gt;
    &lt;serialTo&gt;&lt;/serialTo&gt;
    &lt;subjectInUse&gt;false&lt;/subjectInUse&gt;
    &lt;eMail&gt;&lt;/eMail&gt;
    &lt;commonName&gt;&lt;/commonName&gt;
    &lt;userID&gt;&lt;/userID&gt;
    &lt;orgUnit&gt;&lt;/orgUnit&gt;
    &lt;org&gt;&lt;/org&gt;
    &lt;locality&gt;&lt;/locality&gt;
    &lt;state&gt;&lt;/state&gt;
    &lt;country&gt;&lt;/country&gt;
    &lt;matchExactly&gt;false&lt;/matchExactly&gt;
    &lt;status&gt;&lt;/status&gt;
    &lt;revokedByInUse&gt;false&lt;/revokedByInUse&gt;
    &lt;revokedBy&gt;&lt;/revokedBy&gt;
    &lt;revokedOnFrom&gt;false&lt;/revokedOnFrom&gt;
    &lt;revokedOnTo&gt;&lt;/revokedOnTo&gt;
    &lt;revocationReasonInUse&gt;false&lt;/revocationReasonInUse&gt;
    &lt;revocationReason&gt;&lt;/revocationReason&gt;
    &lt;issuedByInUse&gt;false&lt;/issuedByInUse&gt;
    &lt;issuedBy&gt;&lt;/issuedBy&gt;
    &lt;issuedOnInUse&gt;false&lt;/issuedOnInUse&gt;
    &lt;issuedOnFrom&gt;&lt;/issuedOnFrom&gt;
    &lt;issuedOnTo&gt;&lt;/issuedOnTo&gt;
    &lt;validNotBeforeInUse&gt;false&lt;/validNotBeforeInUse&gt;
    &lt;validNotBeforeFrom&gt;&lt;/validNotBeforeFrom&gt;
    &lt;validNotBeforeTo&gt;&lt;/validNotBeforeTo&gt;
    &lt;validNotAfterInUse&gt;false&lt;/validNotAfterInUse&gt;
    &lt;validNotAfterFrom&gt;&lt;/validNotAfterFrom&gt;
    &lt;validNotAfterTo&gt;&lt;/validNotAfterTo&gt;
    &lt;validityLengthInUse&gt;false&lt;/validityLengthInUse&gt;
    &lt;validityOperation&gt;&lt;/validityOperation&gt;
    &lt;validityCount&gt;&lt;/validityCount&gt;
    &lt;validityUnit&gt;&lt;/validityUnit&gt;
    &lt;certTypeInUse&gt;false&lt;/certTypeInUse&gt;
    &lt;certTypeSubEmailCA&gt;&lt;/certTypeSubEmailCA&gt;
    &lt;certTypeSubSSLCA&gt;&lt;/certTypeSubSSLCA&gt;
    &lt;certTypeSecureEmail&gt;&lt;/certTypeSecureEmail&gt;
&lt;/CertSearchRequest&gt;
</pre>
</dl>
<p> To view a particular certificate: </p>
<p> <code>pki ca-cert-show &lt;certificate ID&gt;</code> </p>
<h3>Revoking Certificates</h3>
<p> Revoking, holding, or releasing a certificate must be executed as an agent user. To revoke a certificate: </p>
<p> <code>pki &lt;agent authentication&gt; ca-cert-revoke &lt;certificate ID&gt;</code> </p>
<p> To place a certificate on hold temporarily: </p>
<p> <code>pki &lt;agent authentication&gt; ca-cert-hold &lt;certificate ID&gt;</code> </p>
<p> To release a certificate that has been placed on hold: </p>
<p> <code>pki &lt;agent authentication&gt; ca-cert-release-hold &lt;certificate ID&gt;</code> </p>
<h3>Certificate Requests</h3>
<p> To request a certificate, first generate a certificate signing request (CSR), then submit it with a certificate profile. The list of available profiles can be viewed using the following command: </p>
<p> <code>pki ca-cert-request-profile-find</code> </p>
<p> To generate a CSR, use the certutil, PKCS10Client, or CRMFPopClient, and store it into a file. </p>
<p> Basic requests can be submitted using the following command: </p>
<p> <code>pki ca-cert-request-submit &#8211;profile &lt;profile ID&gt; &#8211;request-type &lt;type&gt; &#8211;csr-file &lt;CSR file&gt; &#8211;subject &lt;subject DN&gt;</code> </p>
<p> To submit more advanced requests, download a template of the request file for a particular profile using the following command: </p>
<p> <code>pki ca-cert-request-profile-show &lt;profile ID&gt; &#8211;output &lt;request file&gt;</code> </p>
<p> Then, edit the request file, fill in the input attributes required by the profile, and submit the request using the following command: </p>
<p> <code>pki ca-cert-request-submit &lt;request file&gt;</code> </p>
<p> Depending on the profile, the command may require authentication (see the profile configuration file). The CLI currently supports client certificate authentication and directory-based authentication. </p>
<p> Also depending on the profile, an agent may need to review and approve the request by running the following command: </p>
<p> <code>pki &lt;agent authentication&gt; ca-cert-request-review &lt;request ID&gt; &#8211;file &lt;file to store the certificate request&gt;</code> </p>
<p> The &#8211;file &lt;filename&gt; and &#8211;action &lt;action&gt; options are mutually exclusive (i. e. &#8211; only one or the other may be specified during command invocation). </p>
<p> If the &#8211;file &lt;filename&gt; option is specified, the certificate request, as well as the defaults and constraints of the enrollment profile, will be retrieved and stored in the output file provided by the &#8211;file option. The agent can examine the file and override any values if necessary. To process the request, enter the appropriate action when prompted: </p>
<p> <code>Action (approve/reject/cancel/update/validate/assign/unassign):</code> </p>
<p> The request in the file will be read in, and the specified action will be applied against it. </p>
<p> Alternatively, when no changes to the request are necessary, the agent can process the request in a single step using the &#8211;action &lt;action&gt; option with the following command: </p>
<p> <code>pki &lt;agent authentication&gt; ca-cert-request-review &lt;request ID&gt; &#8211;action &lt;action&gt;</code> </p>
<h2>AUTHORS</h2>
<p> Ade Lee &lt;alee [at] redhat.com&gt;, Endi Dewata &lt;edewata [at] redhat.com&gt;, and Matthew Harmsen &lt;mharmsen [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2014 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>Index</h2>
