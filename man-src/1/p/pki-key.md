---
title: "pki-key(1)"
name: "pki-key"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pki-key/"
description: "pki-key – Command-Line Interface for managing Certificate System keys."
---

<h2 class="name">NAME</h2>
<p> pki-key &#8211; Command-Line Interface for managing Certificate System keys.</p>
<h2>SYNOPSIS</h2>
<pre><code>
pki[CLI options]&lt;subsystem&gt; - key pki[CLI options]&lt;subsystem&gt; - key - find[command options] pki[CLI options]&lt;subsystem&gt; - key - show&lt;Key ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - key - request - find[command options] pki[CLI options]&lt;subsystem&gt; - key - request - show&lt;Request ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - key - mod&lt;Key ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - key - template - find[command options] pki[CLI options]&lt;subsystem&gt; - key - template - show&lt;Template ID&gt;[command options] pki[CLI options]&lt;subsystem&gt; - key - archive[command options] pki[CLI options]&lt;subsystem&gt; - key - retrieve[command options] pki[CLI options]&lt;subsystem&gt; - key - generate&lt;Client Key ID&gt; --key - algorithm&lt;algorithm&gt;[command options] pki[CLI options]&lt;subsystem&gt; - key - recover[command options] pki[CLI options]&lt;subsystem&gt; - key - request - review&lt;Request ID&gt; --action&lt;action&gt;[command options]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pki-key</code> commands provide command-line interfaces to manage keys on the KRA. </p>
<p> The only valid subsystem is <code>kra</code>. The <code>kra-</code> prefix may be omitted. </p>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-key</code></p>
<dl>
<dt>
<dd> This command is to list available key commands.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-key-find</code> [command options]</p>
<dl>
<dt>
<dd> This command is to list keys.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-key-show</code> &lt;Key ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to view the details of a key in the KRA.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-key-request-find</code> [command options]</p>
<dl>
<dt>
<dd> This command is to list key requests.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-key-request-show</code> &lt;Request ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to view the details of a key request submitted to the KRA.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-key-mod</code> &lt;Key ID&gt; &#8211;status &lt;status&gt;[command options]</p>
<dl>
<dt>
<dd> This command is to modify the status of a particular key in the KRA.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-key-template-find</code> [command options]</p>
<dl>
<dt>
<dd> This command is to list the templates for all types of requests in the system.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-key-template-show</code> &lt;Template ID&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to view details of the template of a specific key request.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-key-archive</code> [command options]</p>
<dl>
<dt>
<dd> This command is to archive a secret in the DRM.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-key-retrieve</code> [command options]</p>
<dl>
<dt>
<dd> This command is to retrieve a secret stored in the DRM.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-key-generate</code> &lt;Client Key ID&gt; &#8211;key-algorithm &lt;algorithm&gt; [command options]</p>
<dl>
<dt>
<dd> This command is to generate a key in the DRM.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-key-recover</code> [command options]</p>
<dl>
<dt>
<dd> This command is to recover details of a key in the DRM.</dl>
<p> <code>pki</code> [CLI options] <code>&lt;subsystem&gt;-key-request-review</code> [command options]</p>
<dl>
<dt>
<dd> This command is to review a key request submitted ot the DRM.</dl>
<h2>OPTIONS</h2>
<p> The CLI options are described in <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1). </p>
<h2>OPERATIONS</h2>
<p> To view available key commands, type <code>pki &lt;subsystem&gt;-key</code>. To view each command&#8217;s usage, type <code> pki &lt;subsystem&gt;-key-&lt;command&gt; &#8211;help</code>. </p>
<p> All the key commands require agent authentication. </p>
<h3>Viewing the keys</h3>
<p> To view the keys stored in DRM: </p>
<p> <code>pki &lt;agent authentication&gt; key-find</code> </p>
<p> To view all active keys for a specific client key ID: </p>
<p> <code>pki &lt;agent authentication&gt; key-find &#8211;clientKeyID &lt;Client Key ID&gt; &#8211;status active</code> </p>
<p> To view details of a specific key: </p>
<p> <code>pki &lt;agent authentication&gt; key-show &lt;KeyID&gt;</code> </p>
<h3>Archiving a key</h3>
<p> To archive a passphrase in the DRM: </p>
<p> <code>pki &lt;agent authentication&gt; key-archive &#8211;clientKeyID &lt;Client Key ID&gt; &#8211;passphrase &lt;Passphrase&gt;</code> </p>
<p> A symmetric key can be archived using the &quot;archiveKey&quot; request template. </p>
<p> To archive a secret using the request template stored in a file: </p>
<p> <code>pki &lt;agent authentication&gt; key-archive &#8211;input &lt;path to the template file&gt;</code> </p>
<h3>Retrieving a key</h3>
<p> To retrieve a key using the key ID: </p>
<p> <code>pki &lt;agent authentication&gt; key-retrieve &#8211;keyID &lt;Key Identifier&gt;</code> </p>
<p> To retrieve a key using a recovery request template: </p>
<p> <code>pki &lt;agent authentication&gt; key-retrieve &#8211;input &lt;path_to_the_template_file&gt;</code> </p>
<p> To retrieve a key encrypted in a custom password: </p>
<p> <code>pki &lt;agent authentication&gt; key-retrieve &#8211;keyID &lt;Key Identifier&gt; &#8211;passphrase &lt;passphrase&gt;</code> </p>
<p> The returned output contains the secret wrapped in the provided passphrase, using DES3 algorithm, and the nonce used for encryption. </p>
<p> To store the key information to an output file, use the &#8211;output option for the command. </p>
<h3>Recovering a key</h3>
<p> To initiate a key recovery: </p>
<p> <code>pki &lt;agent authentication&gt; key-recover &#8211;keyID &lt;Key Identifier&gt;</code> </p>
<p> The request ID returned by this operation must be approved using the <code>key-request-review</code> command before the actual key retrieval. </p>
<p> This step is performed internally by the key-retrieve command. </p>
<h3>Generating a Symmetric Key</h3>
<p> To generate a symmetric key using the DES3 algorithm: </p>
<p> <code>pki &lt;agent authentication&gt; key-generate &lt;Client Key ID&gt; &#8211;key-algorithm DES3 &#8211;usages wrap,unwrap</code> </p>
<p> There are other algorithms to generate symmetric keys such as the AES, DES, DESede, RC2, RC4. </p>
<p> In case of using any of the AES/RC2/RC4 algorithms, the key size has to be specified using the key-size option of the command. </p>
<p> Generation of asymmetric keys is currently not implemented. </p>
<h3>Reviewing a key request</h3>
<p> To approve a key request: </p>
<p> <code>pki &lt;agent authentication&gt; key-request-review &lt;Request ID&gt; &#8211;action approve</code> </p>
<p> On successful authentication, the request with the given request ID will be approved. </p>
<p> There other actions that can be performed by an agent are reject/cancel. </p>
<h3>Viewing a request template</h3>
<p> To list all the key request templates: </p>
<p> <code>pki &lt;agent authentication&gt; key-template-find</code> </p>
<p> To view a key archival request template: </p>
<p> <code>pki &lt;agent authentication&gt; key-template-show archiveKey</code> </p>
<h2>EXAMPLES</h2>
<p> The following pki client examples show the usage of the above operations for a basic CA and KRA server installation. </p>
<p> A basic installation of CA and KRA servers can be done by running pkispawn in interactive mode and selecting the default parameters (see the section <code>INTERACTIVE MODE</code> in <a href="/docs/linux/man/8-pkispawn/">pkispawn</a>(8)) </p>
<p> or using a configuration file with basic parameters(see the section <code>EXAMPLES</code> in <a href="/docs/linux/man/8-pkispawn/">pkispawn</a>(8)). </p>
<p> Only an agent can perform operations on the <code>key</code> resource. An agent certificate must be used for authentication. This can be done by importing an agent certificate into an NSS database and passing the values to relevant options provided by the pki CLI framework. </p>
<p> Running the following commands will set up the NSS database for use by a pki client and import the agent&#8217;s certificate into the database and list information( including the nickname) of the certificate stored in the database. </p>
<p>&nbsp;<wbr>&#8211; certutil -N -d&nbsp;<wbr>&lt;CERT_DB_DIR_PATH&gt; </p>
<p>&nbsp;<wbr>&#8211; pk12util -i&nbsp;<wbr>&lt;Agent_Cert_P12_FILE_PATH&gt;&nbsp;<wbr>-d&nbsp;<wbr>&lt;CERT_DB_DIR_PATH&gt; </p>
<p>&nbsp;<wbr>&#8211; certutil -L -d&nbsp;<wbr>&lt;CERT_DB_DIR_PATH&gt; </p>
<p> The first command creates an NSS database. It asks to enter a password for the database. The second command imports the agent certificate in a PKCS12 format into the database. It prompts for the passwords of the PKCS12 file and the NSS database. The third command shows the information about the imported certificate.(including the nickname) </p>
<p> For demonstration purposes, the administrator certificate can be used to perform agent authentication. In a basic installation setup, the admin cert can be found at /root/.dogtag/pki-tomcat/ca_admin_cert.p12. Since the installation can only be performed by a root user, this file must be copied to a location where other users can access it, with valid permissions. </p>
<p> On completion of the setup, and, when issuing the first command using the authentication parameters, a user may be greeted with a warning message which indicates that an untrusted issuer was encountered. Simply reply &#8216;Y&#8217; to import the CA certificate, and, presuming that the displayed CA server URI is valid, press the carriage return. </p>
<p> To list all the keys and key requests stored in KRA: </p>
<p> <code>pki -d &lt;CERT_DB_DIR_PATH&gt; -c &lt;CERT_DB_PWD&gt; -n &lt;Certificate_Nickname&gt; key-find</code> </p>
<p> <code>pki -d &lt;CERT_DB_DIR_PATH&gt; -c &lt;CERT_DB_PWD&gt; -n &lt;Certificate_Nickname&gt; key-request-find</code> </p>
<p> To view information of a specific key or a key request stored in KRA: </p>
<p> <code>pki -d &lt;CERT_DB_DIR_PATH&gt; -c &lt;CERT_DB_PWD&gt; -n &lt;Certificate_Nickname&gt; key-show &lt;Key ID&gt;</code> </p>
<p> <code>pki -d &lt;CERT_DB_DIR_PATH&gt; -c &lt;CERT_DB_PWD&gt; -n &lt;Certificate_Nickname&gt; key-request-show &lt;Request ID&gt;</code> </p>
<p> Creating a request for archiving/retrieving/recovering a key </p>
<p> <code>pki -d &lt;CERT_DB_DIR_PATH&gt; -c &lt;CERT_DB_PWD&gt; -n &lt;Certificate_Nickname&gt; key-archive &#8211;clientKeyID vek12345 &#8211;passphrase SampleSecret</code> </p>
<p> <code>pki -d &lt;CERT_DB_DIR_PATH&gt; -c &lt;CERT_DB_PWD&gt; -n &lt;Certificate_Nickname&gt; key-retrieve &#8211;keyID &lt;Key ID of the archived secret&gt;</code> </p>
<p> <code>pki -d &lt;CERT_DB_DIR_PATH&gt; -c &lt;CERT_DB_PWD&gt; -n &lt;Certificate_Nickname&gt; key-recover &#8211;keyID &lt;Key ID of the archived secret&gt;</code> </p>
<p> Generating a symmetric key </p>
<p> <code>pki -d &lt;CERT_DB_DIR_PATH&gt; -c &lt;CERT_DB_PWD&gt; -n &lt;Certificate_Nickname&gt; key-generate vek123456 &#8211;key-algorithm DES3 &#8211;usages encrypt,decrypt</code> </p>
<p> Reviewing a key request </p>
<p> <code>pki -d &lt;CERT_DB_DIR_PATH&gt; -c &lt;CERT_DB_PWD&gt; -n &lt;Certificate_Nickname&gt; key-request-review &lt;Request ID&gt; &#8211;action &lt;approve/reject/cancel&gt;</code> </p>
<h2>Using templates for creating requests (for advanced users)</h2>
<p> The messages for communication between the CLI framework and KRA for accessing the key resource are always encrypted. </p>
<p> In the case of the above mentioned examples, the encryption and decryption of the secrets is done internally by the Dogtag client API. </p>
<p> But, applications using the CLI framework to create various requests and also use local encryption, so the xml templates can be used to supply data to the create a request. </p>
<p> All the templates can be listed by executing: </p>
<p> <code>pki key-template-find</code> </p>
<h3>Creating a key-archival request</h3>
<p> To fetch the template for key archival: </p>
<p> <code>pki key-template-show archiveKey &#8211;output &lt;output file&gt;</code> </p>
<p> This command gets the template for a key archival request and stores it in an output file. </p>
<p> Following is the description of the various parameters in the key archival template: </p>
<p>&nbsp;<wbr>&#8212; clientKeyID &#8211; Unique identifier for the secret.<br />
&nbsp;<wbr>&#8212; dataType &#8211; Type of the data to be stored which can be passphrase/symmetricKey/asymmetricKey.<br />
&nbsp;<wbr>&#8212; keyAlgorithm &#8211; Algorithm used to create a symmetric key.&nbsp;<wbr>(Not required if the dataType is passphrase)<br />
&nbsp;<wbr>&#8212; keySize &#8211; Size used to generate the symmetric key.&nbsp;<wbr>(Not required if the dataType is passphrase)<br />
&nbsp;<wbr>&#8212; algorithmOID &#8211; Key Algorithm object identifier<br />
&nbsp;<wbr>&#8212; symmetricAlgorithmParams &#8211; Base64 encoded nonce data. Nonce used while encrypting the secret.<br />
&nbsp;<wbr>&#8212; wrappedPrivateData &#8211; Secret encrypted using a session key(A symmetric key)&nbsp;<wbr>encoded using Base64. This entity contains the secret which is encrypted using a session key.<br />
&nbsp;<wbr>&#8212; transWrappedSessionKey &#8211; The session key used to encrypt the secret, wrapped using the DRM transport key, and encoded in Base64 format.<br />
&nbsp;<wbr>&#8212; pkiArchiveOptions &#8211; An object of type PKIArchiveOptions provided by the NSS/JSS library to securely transport a secret encoded in Base64 format. </p>
<p> To create an archival request using the template file: </p>
<p> <code>pki -d &lt;CERT_DB_DIR_PATH&gt; -c &lt;CERT_DB_PWD&gt; -n &lt;Certificate_Nickname&gt; key-archive &#8211;input &lt;Path_to_template_file&gt;</code> </p>
<h3>Creating a key-retrieval request</h3>
<p> To fetch the template for key retrieval: </p>
<p> <code>pki key-template-show retrieveKey &#8211;output &lt;output file&gt;</code> </p>
<p> This command gets the template for a key retrieval request and stores it in an output file. </p>
<p> Following is the description of the various parameters in the key retrieval template: </p>
<p>&nbsp;<wbr>&#8212; keyID &#8211; Key identifier<br />
&nbsp;<wbr>&#8212; requestID &#8211; Key request identifier<br />
&nbsp;<wbr>&#8212; nonceData &#8211; Base64 encoded string of nonce used during encryption<br />
&nbsp;<wbr>&#8212; passphrase &#8211; passphrase to encrypt the secret with/&nbsp;<wbr>passphrase for the PKCS12 file returned<br />
&nbsp;<wbr>&#8212; sessionWrappedpassphrase &#8211; Base64 encoded string of &#8211; Passphrase encrypted with a session key.<br />
&nbsp;<wbr>&#8212; transWrapedSessionKey &#8211; Base64 encoded string of &#8211; session key encrypted with KRA&#8217;s transport key.<br />
&nbsp;<wbr>&#8212; certificate &#8211; Base64 encoded certificate for recovering the key. </p>
<p> To create a retrieval request using the template file: </p>
<p> <code>pki -d &lt;CERT_DB_DIR_PATH&gt; -c &lt;CERT_DB_PWD&gt; -n &lt;Certificate_Nickname&gt; key-retrieve &#8211;input &lt;Path_to_template_file&gt;</code> </p>
<h3>Creating a symmetric key generation request</h3>
<p> To fetch the template for symmetric key generation: </p>
<p> <code>pki key-template-show generateKey &#8211;output &lt;output file&gt;</code> </p>
<p> This command gets the template for a symmetric key generation request and stores it in an output file. </p>
<p> Following is the description of the various parameters in the key retrieval template: </p>
<p>&nbsp;<wbr>&#8212; clientKeyID &#8211; Client specified unique key identifier<br />
&nbsp;<wbr>&#8212; keyAlgorithm &#8211; Algorithm to be used to generate key&nbsp;<wbr>(AES/DES/DES3/DESede/RC2/RC4)<br />
&nbsp;<wbr>&#8212; keySize &#8211; Value for the size of the key to be generated.<br />
&nbsp;<wbr>&#8212; keyUsage &#8211; usages of the generated key<br />
&nbsp;<wbr>&nbsp;<wbr>useful for Symmetric Keys&nbsp;<wbr>(DES3,AES,etc)&nbsp;<wbr>(wrap,unwrap,encrypt,decrypt)<br />
&nbsp;<wbr>&nbsp;<wbr>useful for Asymmetric Keys&nbsp;<wbr>(RSA, EC,etc)&nbsp;<wbr>(wrap,unwrap,encrypt,decrypt,sign,verify,sign_recover,verify_recover) </p>
<p> To create a key generation request using the template file: </p>
<p> <code>pki -d &lt;CERT_DB_DIR_PATH&gt; -c &lt;CERT_DB_PWD&gt; -n &lt;Certificate_Nickname&gt; key-generate &#8211;input &lt;Path_to_template_file&gt;</code> </p>
<h2>AUTHORS</h2>
<p> Ade Lee &lt;alee [at] redhat.com&gt;, Endi Dewata &lt;edewata [at] redhat.com&gt;, Matthew Harmsen &lt;mharmsen [at] redhat.com&gt; and Abhishek Koneru &lt;akoneru [at] redhat.com&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2014 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-pkispawn/">pkispawn</a>(8),</code> <code><a href="/docs/linux/man/1-pki/">pki</a>(1)</code> </p>
<h2>Index</h2>
