---
title: "auditverify(1)"
name: "auditverify"
section: "1"
letter: "a"
url: "/docs/linux/man/1-auditverify/"
description: "AuditVerify – Command-Line utility for verifying Certificate System signed audit logs."
---

<p>AuditVerify &#8211; Command-Line utility for verifying Certificate System signed audit logs.</p>
<h2>Synopsis</h2>
<pre><code>AuditVerify</code> -d &lt;dbdir&gt; -n &lt;signing_certificate_nickname&gt; -a &lt;logListFile&gt; [-P cert/key_db_prefix] [-v]</pre>
<h2>Description</h2>
<p>The <code>AuditVerify</code> command provides command-line utility to verify that signed audit logs were signed with the appropriate CS audit private signing key and that the audit logs have not been compromised. Auditors can verify the authenticity and integrity of signed audit logs using the <code>AuditVerify</code> tool. This tool uses the public key of the signed audit log signing certificate to verify the digital signatures embedded in a signed audit log file. The tool result indicates either that the signed audit log was successfully verified or that the signed audit log was not successfully verified. An unsuccessful verification warns the auditor that the signature failed to verify, indicating the log file may have been tampered with (compromised). </p>
<p> <code>Note: An auditor can be any user that has the privilege to peruse the pki audit logs.</code> </p>
<h2>Options</h2>
<dl>
<dt><code>-d &lt;dbdir&gt;</code></p>
<dd>Specifies the directory containing the security databases with the imported audit log signing certificate. This directory is almost always the auditor&#8217;s own personal certificate databases in a personal directory, such as ~jsmith/auditVerifyDir/. </p>
<dt><code>-n &lt;signing_certificate_nickname&gt;</code></p>
<dd>Gives the nickname of the certificate used to sign the log files. The nickname is whatever was used when the log signing certificate was imported into that database. </p>
<dt><code>[-P cert/key_db_prefix]</code></p>
<dd>Optional. The prefix to prepend to the certificate and key database filenames. If used, a value of empty quotation marks (“”) should be specified for this argument, since the auditor is using separate certificate and key databases from the Certificate System instance and it is unlikely that the prefix should be prepended to the new audit security database files. </p>
<dt><code>-a &lt;logListFile&gt;</code></p>
<dd>Specifies the file which contains the comma-separate list of file paths (in chronological order) of the signed audit logs to be verified. This file should be created in a directory which is writeable by the auditor, such as a special auditing directory like ~jsmith/auditDir. The contents of the logListFile are the full paths to the audit logs. For example:</dl>
<pre> /var/log/pki/pki-ca/ca/signedAudit/ca_audit,/var/log/pki/pki-ca/ca/signedAudit/ca_audit.20030227102711,/var/log/pki/pki-ca/ca/signedAudit/ca_audit.20030226094015</pre>
<dl>
<dt><code>[-v]</code></p>
<dd>Optional. Specifies verbose output. </p>
</dl>
<h2>Setting up the Auditor&#8217;s Database</h2>
<p><code>AuditVerify</code> needs access to a set of security databases (usually the auditor&#8217;s personal security databases) containing the signed audit log signing certificate and its chain of issuing certificates. One of the CA certificates in the issuance chain must be marked as trusted in the database. </p>
<p> Auditors should import the audit signing certificate into their personal certificate database before running <code>AuditVerify</code>. The auditor should not use the security databases of the Certificate System instance that generated the signed audit log files. If there are no readily accessible certificate and key database, the auditor must create a set of certificate and key databases and import the signed audit log signing certificate chain. </p>
<p> To create the security databases and import the certificate chain: </p>
<h3>Create a special directory in the auditor&#8217;s home directory to use to perform the verification. For example:</h3>
<p>mkdir ~jsmith/auditVerifyDir </p>
<h3>Use the certutil tool to create an empty set of certificate databases in the auditor&#8217;s home directory.</h3>
<p>certutil -d ~jsmith/auditVerifyDir -N </p>
<h3>Download the CA certificate from the CA&#8217;s Retrieval page. The certificates can be obtained from the CA in ASCII format.</h3>
<p><a rel="nofollow" href="https://server.example.com:ca_https_port/ca/ee/ca/">https://server.example.com:ca_https_port/ca/ee/ca/</a> </p>
<h3>Import the CA certificate and log signing certificate into the databases and set trust of the certificates</h3>
<p>If the CA certificate is in a file called cacert.txt and the log signing certificate is in a file called logsigncert.txt, then the certutil can be used to set the trust for the new audit security database directory pointing to those files, as follows: </p>
<p> certutil -d ~jsmith/auditVerifyDir/ -A -n &quot;CA Certificate&quot; -t &quot;CT,CT,CT&quot; -a -i cacert.txt </p>
<p> certutil -d ~jsmith/auditVerifyDir -A -n &quot;Log Signing Certificate&quot; -t &quot;,,P&quot; -a -i logsigncert.txt </p>
<p> <code>Note: The signedAudit directory kept by the subsystem is not writeable by any user, including auditors. </code> </p>
<h2>Operation</h2>
<p>After a separate audit database directory has been configured, do the following:</p>
<h3>Create a text file containing a comma-separated list of the log files to be verified. The name of this file is referenced in the AuditVerify command.</h3>
<p>For example, this file could be logListFile in the ~jsmith/auditVerifyDir/ directory. The contents are the comma-separated list of audit logs to be verified, such as &quot;auditlog.1213, auditlog.1214, auditlog.1215.&quot; </p>
<h3>If the audit databases do not contain prefixes and are located in the user home directory, such as ~jsmith/.mozilla, and the signing certificate nickname is Log Signing Certificate, the AuditVerify command is run as follows:</h3>
<p>AuditVerify -d ~jsmith/auditVerifyDir -n Log Signing Certificate -a ~jsmith/auditVerifyDir/logListFile -P &quot;&quot; -v </p>
<p> <i>Note: It has been observed that if audit signing is enabled after system is first started, the first audit signature would not be verified. What happens is that the signature starts calculating from it&#8217;s in-memory audit log message when it signs, and since log signing is turned on mid-way (not from a fresh new log file), the previous content were not signed along for calculating the first signature (and rightfully so). When AuditVerify is run, it does not know where the log signing begins, so it assumes it starts from the beginning of the file till the first signature. This is why the first signature (if signing is turned on mid-way) will always appear to be incorrect.</i> </p>
<h2>Authors</h2>
<p>Christina Fu &lt;cfu [at] redhat.com&gt;. </p>
<h2>Copyright</h2>
<p>Copyright (c) 2016 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pki/">pki</a>(1)</code></p>
