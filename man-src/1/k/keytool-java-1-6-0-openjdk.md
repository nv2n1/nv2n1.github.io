---
title: "keytool-java-1-6-0-openjdk(1)"
name: "keytool-java-1-6-0-openjdk"
section: "1"
letter: "k"
url: "/docs/linux/man/1-keytool-java-1-6-0-openjdk/"
description: "keytool – Key and Certificate Management Tool"
---

<p>keytool &#8211; Key and Certificate Management Tool </p>
<dl>
<dd>Manages a keystore (database) of cryptographic keys, X.509 certificate chains, and trusted certificates.</dl>
<h2>Synopsis</h2>
<pre><code>keytool</code> [ commands ]</pre>
<p>The keytool command interface has changed in Java SE 6. See the Changes Section for a detailed description. Note that previously defined commands are still supported. </p>
<h2>Description</h2>
<p><code>keytool</code> is a key and certificate management utility. It allows users to administer their own public/private key pairs and associated certificates for use in self-authentication (where the user authenticates himself/herself to other users/services) or data integrity and authentication services, using digital signatures. It also allows users to cache the public keys (in the form of certificates) of their communicating peers. </p>
<p> A <i>certificate</i> is a digitally signed statement from one entity (person, company, etc.), saying that the public key (and some other information) of some other entity has a particular value. (See Certificates.) When data is digitally signed, the signature can be verified to check the data integrity and authenticity. <i>Integrity</i> means that the data has not been modified or tampered with, and <i>authenticity</i> means the data indeed comes from whoever claims to have created and signed it. </p>
<p> <code>keytool</code> also enables users to administer secret keys used in symmetric encryption/decryption (e.g. DES). </p>
<p> <code>keytool</code> stores the keys and certificates in a <i>keystore</i>. </p>
<h2>Command And Option Notes</h2>
<p>The various commands and their options are listed and described below . Note: </p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>All command and option names are preceded by a minus sign (-).</p>
<dt>o</p>
<dd>The options for each command may be provided in any order.</p>
<dt>o</p>
<dd>All items not italicized or in braces or square brackets are required to appear as is.</p>
<dt>o</p>
<dd>Braces surrounding an option generally signify that a default value will be used if the option is not specified on the command line. Braces are also used around the <i>-v</i>, <i>-rfc</i>, and <i>-J</i> options, which only have meaning if they appear on the command line (that is, they don&#8217;t have any &quot;default&quot; values other than not existing).</p>
<dt>o</p>
<dd>Brackets surrounding an option signify that the user is prompted for the value(s) if the option is not specified on the command line. (For a <i>-keypass</i> option, if you do not specify the option on the command line, <code>keytool</code> will first attempt to use the keystore password to recover the private/secret key, and if this fails, will then prompt you for the private/secret key password.)</p>
<dt>o</p>
<dd>Items in italics (option values) represent the actual values that must be supplied. For example, here is the format of the <i>-printcert</i> command: </p>
<pre><code> keytool -printcert {-file </code><tt>cert_file</tt><code>} {-v}</code></pre>
</dl>
<p> When specifying a <i>-printcert</i> command, replace <i>cert_file</i> with the actual file name, as in: </p>
<pre><code> keytool -printcert -file VScert.cer</code></pre>
<dl>
<dt>o</p>
<dd>Option values must be quoted if they contain a blank (space).</p>
<dt>o</p>
<dd>The <i>-help</i> command is the default. Thus, the command line </p>
<pre><code> keytool</code></pre>
<p>is equivalent to </p>
<pre><code> keytool -help</code></pre>
</dl>
</dl>
<h3>Option Defaults</h3>
<dl>
<dd>Below are the defaults for various option values. </p>
<pre><code>-alias &quot;mykey&quot;
-keyalg
 &quot;DSA&quot; (when using </code><code>-genkeypair</code><code>)
 &quot;DES&quot; (when using </code><code>-genseckey</code><code>)
-keysize
 1024 (when using </code><code>-genkeypair</code><code>)
 56 (when using </code><code>-genseckey</code><code> and -keyalg is &quot;DES&quot;)
 168 (when using </code><code>-genseckey</code><code> and -keyalg is &quot;DESede&quot;)
-validity 90
-keystore </code><tt>the file named </tt><tt>.keystore</tt><code> in the user's home directory</code><code>
-storetype </code><tt>the value of the &quot;keystore.type&quot; property in the security properties file,
 which is returned by the static </tt><tt>getDefaultType</tt><code> method in </code><tt>java.security.KeyStore</tt><code>
-file </code><tt>stdin if reading, stdout if writing</tt><code>
-protected false</code></pre>
<p>In generating a public/private key pair, the signature algorithm (<i>-sigalg</i> option) is derived from the algorithm of the underlying private key: If the underlying private key is of type &quot;DSA&quot;, the <i>-sigalg</i> option defaults to &quot;SHA1withDSA&quot;, and if the underlying private key is of type &quot;RSA&quot;, <i>-sigalg</i> defaults to &quot;MD5withRSA&quot;. Please consult the <i>Java Cryptography Architecture API Specification &amp; Reference</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/technotes/guides/security/crypto/CryptoSpec.html#AppA">http://java.sun.com/javase/6/docs/technotes/guides/security/crypto/CryptoSpec.html#AppA</a> for a full list of <i>-keyalg</i> and <i>-sigalg</i> you can choose from.</dl>
<h3>Common Options</h3>
<dl>
<dd>The <i>-v</i> option can appear for all commands except <i>-help</i>. If it appears, it signifies &quot;verbose&quot; mode; more information will be output. </p>
<p> There is also a <i>-J</i><i>javaoption</i> option that may appear for any command. If it appears, the specified <i>javaoption</i> string is passed through directly to the Java interpreter. This option should not contain any spaces. It is useful for adjusting the execution environment or memory usage. For a list of possible interpreter options, type <i>java -h</i> or <i>java -X</i> at the command line. </p>
<p> These options may appear for all commands operating on a keystore: </p>
<dl>
<dd>
<dl>
<dt>-storetype storetype</p>
<dd>This qualifier specifies the type of keystore to be instantiated.</p>
<dt>-keystore keystore</p>
<dd>The keystore location.</dl>
<p> If the JKS storetype is used and a keystore file does not yet exist, then certain <code>keytool</code> commands may result in a new keystore file being created. For example, if <i>keytool -genkeypair</i> is invoked and the <i>-keystore</i> option is not specified, the default keystore file named <i>.keystore</i> in the user&#8217;s home directory will be created if it does not already exist. Similarly, if the <i>-keystore </i><i>ks_file</i> option is specified but <i>ks_file</i> does not exist, then it will be created </p>
<p> Note that the input stream from the <i>-keystore</i> option is passed to the <i>KeyStore.load</i> method. If <i>NONE</i> is specified as the URL, then a null stream is passed to the <i>KeyStore.load</i> method. <i>NONE</i> should be specified if the <i>KeyStore</i> is not file-based (for example, if it resides on a hardware token device).</p>
<dl>
<dt>-storepass storepass</p>
<dd>The password which is used to protect the integrity of the keystore.</dl>
<p> <i>storepass</i> must be at least 6 characters long. It must be provided to all commands that access the keystore contents. For such commands, if a <i>-storepass</i> option is not provided at the command line, the user is prompted for it. </p>
<p> When retrieving information from the keystore, the password is optional; if no password is given, the integrity of the retrieved information cannot be checked and a warning is displayed.</p>
<dl>
<dt>-providerName provider_name</p>
<dd>Used to identify a cryptographic service provider&#8217;s name when listed in the security properties file.</p>
<dt>-providerClass provider_class_name</p>
<dd>Used to specify the name of cryptographic service provider&#8217;s master class file when the service provider is not listed in the security properties file.</p>
<dt>-providerArg provider_arg</p>
<dd>Used in conjunction with <i>-providerClass</i>. Represents an optional string input argument for the constructor of <i>provider_class_name</i>.</p>
<dt>-protected</p>
<dd>Either <i>true</i> or <i>false</i>. This value should be specified as <i>true</i> if a password must be given via a protected authentication path such as a dedicated PIN reader.</dl>
</dl>
</dl>
<h2>Commands</h2>
<h3>Creating or Adding Data to the Keystore</h3>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>-genkeypair {-alias alias} {-keyalg keyalg} {-keysize keysize} {-sigalg sigalg} [-dname dname] [-keypass keypass] {-validity valDays} {-storetype storetype} {-keystore keystore} [-storepass storepass] {-providerClass provider_class_name {-providerArg provider_arg}} {-v} {-protected} {-Jjavaoption}</p>
<dd></dl>
<p> Generates a key pair (a public key and associated private key). Wraps the public key into an X.509 v3 self-signed certificate, which is stored as a single-element certificate chain. This certificate chain and the private key are stored in a new keystore entry identified by <i>alias</i>. </p>
<p> <i>keyalg</i> specifies the algorithm to be used to generate the key pair, and <i>keysize</i> specifies the size of each key to be generated. <i>sigalg</i> specifies the algorithm that should be used to sign the self-signed certificate; this algorithm must be compatible with <i>keyalg</i>. </p>
<p> <i>dname</i> specifies the X.500 Distinguished Name to be associated with <i>alias</i>, and is used as the <i>issuer</i> and <i>subject</i> fields in the self-signed certificate. If no distinguished name is provided at the command line, the user will be prompted for one. </p>
<p> <i>keypass</i> is a password used to protect the private key of the generated key pair. If no password is provided, the user is prompted for it. If you press RETURN at the prompt, the key password is set to the same password as that used for the keystore. <i>keypass</i> must be at least 6 characters long. </p>
<p> <i>valDays</i> tells the number of days for which the certificate should be considered valid. </p>
<p> This command was named <i>-genkey</i> in previous releases. This old name is still supported in this release and will be supported in future releases, but for clarify the new name, <i>-genkeypair</i>, is preferred going forward.</p>
<dl>
<dt>-genseckey {-alias alias} {-keyalg keyalg} {-keysize keysize} [-keypass keypass] {-storetype storetype} {-keystore keystore} [-storepass storepass] {-providerClass provider_class_name {-providerArg provider_arg}} {-v} {-protected} {-Jjavaoption}</p>
<dd></dl>
<p> Generates a secret key and stores it in a new <i>KeyStore.SecretKeyEntry</i> identified by <i>alias</i>. </p>
<p> <i>keyalg</i> specifies the algorithm to be used to generate the secret key, and <i>keysize</i> specifies the size of the key to be generated. <i>keypass</i> is a password used to protect the secret key. If no password is provided, the user is prompted for it. If you press RETURN at the prompt, the key password is set to the same password as that used for the keystore. <i>keypass</i> must be at least 6 characters long.</p>
<dl>
<dt>-importcert {-alias alias} {-file cert_file} [-keypass keypass] {-noprompt} {-trustcacerts} {-storetype storetype} {-keystore keystore} [-storepass storepass] {-providerName provider_name} {-providerClass provider_class_name {-providerArg provider_arg}} {-v} {-protected} {-Jjavaoption}</p>
<dd></dl>
<p> Reads the certificate or certificate chain (where the latter is supplied in a PKCS#7 formatted reply) from the file <i>cert_file</i>, and stores it in the keystore entry identified by <i>alias</i>. If no file is given, the certificate or PKCS#7 reply is read from stdin. </p>
<p> <code>keytool</code> can import X.509 v1, v2, and v3 certificates, and PKCS#7 formatted certificate chains consisting of certificates of that type. The data to be imported must be provided either in binary encoding format, or in printable encoding format (also known as Base64 encoding) as defined by the Internet RFC 1421 standard. In the latter case, the encoding must be bounded at the beginning by a string that starts with &quot;&#8212;&#8211;BEGIN&quot;, and bounded at the end by a string that starts with &quot;&#8212;&#8211;END&quot;. </p>
<p> You import a certificate for two reasons:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>to add it to the list of trusted certificates, or</p>
<dt>2.</p>
<dd>to import a certificate reply received from a CA as the result of submitting a Certificate Signing Request (see the -certreq command) to that CA.</dl>
</dl>
<p> Which type of import is intended is indicated by the value of the <i>-alias</i> option:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd><code>If the alias does not point to a key entry</code>, then <code>keytool</code> assumes you are adding a trusted certificate entry. In this case, the alias should not already exist in the keystore. If the alias does already exist, then <code>keytool</code> outputs an error, since there is already a trusted certificate for that alias, and does not import the certificate.</p>
<dt>2.</p>
<dd><code>If the alias points to a key entry</code>, then <code>keytool</code> assumes you are importing a certificate reply.</dl>
</dl>
<p> <code>Importing a New Trusted Certificate</code></p>
<dl>
<dd>Before adding the certificate to the keystore, <code>keytool</code> tries to verify it by attempting to construct a chain of trust from that certificate to a self-signed certificate (belonging to a root CA), using trusted certificates that are already available in the keystore. </p>
<p> If the <i>-trustcacerts</i> option has been specified, additional certificates are considered for the chain of trust, namely the certificates in a file named &quot;cacerts&quot;. </p>
<p> If <code>keytool</code> fails to establish a trust path from the certificate to be imported up to a self-signed certificate (either from the keystore or the &quot;cacerts&quot; file), the certificate information is printed out, and the user is prompted to verify it, e.g., by comparing the displayed certificate fingerprints with the fingerprints obtained from some other (trusted) source of information, which might be the certificate owner himself/herself. Be very careful to ensure the certificate is valid prior to importing it as a &quot;trusted&quot; certificate! &#8212; see WARNING Regarding Importing Trusted Certificates. The user then has the option of aborting the import operation. If the <i>-noprompt</i> option is given, however, there will be no interaction with the user. </p>
</dl>
<p> <code>Importing a Certificate Reply</code></p>
<dl>
<dd>When importing a certificate reply, the certificate reply is validated using trusted certificates from the keystore, and optionally using the certificates configured in the &quot;cacerts&quot; keystore file (if the <i>-trustcacerts</i> option was specified). </p>
<p> The methods of determining whether the certificate reply is trusted are described in the following: </p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd><code>If the reply is a single X.509 certificate</code>, <code>keytool</code> attempts to establish a trust chain, starting at the certificate reply and ending at a self-signed certificate (belonging to a root CA). The certificate reply and the hierarchy of certificates used to authenticate the certificate reply form the new certificate chain of <i>alias</i>. If a trust chain cannot be established, the certificate reply is not imported. In this case, <code>keytool</code> does not print out the certificate and prompt the user to verify it, because it is very hard (if not impossible) for a user to determine the authenticity of the certificate reply.</p>
<dt>o</p>
<dd><code>If the reply is a PKCS#7 formatted certificate chain</code>, the chain is first ordered (with the user certificate first and the self-signed root CA certificate last), before <code>keytool</code> attempts to match the root CA certificate provided in the reply with any of the trusted certificates in the keystore or the &quot;cacerts&quot; keystore file (if the <i>-trustcacerts</i> option was specified). If no match can be found, the information of the root CA certificate is printed out, and the user is prompted to verify it, e.g., by comparing the displayed certificate fingerprints with the fingerprints obtained from some other (trusted) source of information, which might be the root CA itself. The user then has the option of aborting the import operation. If the <i>-noprompt</i> option is given, however, there will be no interaction with the user.</dl>
</dl>
<p> If the public key in the certificate reply matches the user&#8217;s public key already stored with under <i>alias</i>, the old certificate chain is replaced with the new certificate chain in the reply. The old chain can only be replaced if a valid <i>keypass</i>, the password used to protect the private key of the entry, is supplied. If no password is provided, and the private key password is different from the keystore password, the user is prompted for it. </p>
</dl>
<p> This command was named <i>-import</i> in previous releases. This old name is still supported in this release and will be supported in future releases, but for clarify the new name, <i>-importcert</i>, is preferred going forward.</p>
<dl>
<dt>-importkeystore -srckeystore srckeystore -destkeystore destkeystore {-srcstoretype srcstoretype} {-deststoretype deststoretype} [-srcstorepass srcstorepass] [-deststorepass deststorepass] {-srcprotected} {-destprotected} {-srcalias srcalias {-destalias destalias} [-srckeypass srckeypass] [-destkeypass destkeypass] } {-noprompt} {-srcProviderName src_provider_name} {-destProviderName dest_provider_name} {-providerClass provider_class_name {-providerArg provider_arg}} {-v} {-protected} {-Jjavaoption}</p>
<dd></dl>
<p> Imports a single entry or all entries from a source keystore to a destination keystore. </p>
<p> When the <i>srcalias</i> option is provided, the command imports the single entry identified by the alias to the destination keystore. If a destination alias is not provided with <i>destalias</i>, then <i>srcalias</i> is used as the destination alias. If the source entry is protected by a password, <i>srckeypass</i> will be used to recover the entry. If <i>srckeypass</i> is not provided, then <code>keytool</code> will attempt to use <i>srcstorepass</i> to recover the entry. If <i>srcstorepass</i> is either not provided or is incorrect, the user will be prompted for a password. The destination entry will be protected using <i>destkeypass</i>. If <i>destkeypass</i> is not provided, the destination entry will be protected with the source entry password. </p>
<p> If the <i>srcalias</i> option is not provided, then all entries in the source keystore are imported into the destination keystore. Each destination entry will be stored under the alias from the source entry. If the source entry is protected by a password, <i>srcstorepass</i> will be used to recover the entry. If <i>srcstorepass</i> is either not provided or is incorrect, the user will be prompted for a password. If a source keystore entry type is not supported in the destination keystore, or if an error occurs while storing an entry into the destination keystore, the user will be prompted whether to skip the entry and continue, or to quit. The destination entry will be protected with the source entry password. </p>
<p> If the destination alias already exists in the destination keystore, the user is prompted to either overwrite the entry, or to create a new entry under a different alias name. </p>
<p> Note that if <i>-noprompt</i> is provided, the user will not be prompted for a new destination alias. Existing entries will automatically be overwritten with the destination alias name. Finally, entries that can not be imported are automatically skipped and a warning is output.</dl>
</dl>
<h3>Exporting Data</h3>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>-certreq {-alias alias} {-sigalg sigalg} {-file certreq_file} [-keypass keypass] {-storetype storetype} {-keystore keystore} [-storepass storepass] {-providerName provider_name} {-providerClass provider_class_name {-providerArg provider_arg}} {-v} {-protected} {-Jjavaoption}</p>
<dd></dl>
<p> Generates a Certificate Signing Request (CSR), using the PKCS#10 format. </p>
<p> A CSR is intended to be sent to a certificate authority (CA). The CA will authenticate the certificate requestor (usually off-line) and will return a certificate or certificate chain, used to replace the existing certificate chain (which initially consists of a self-signed certificate) in the keystore. </p>
<p> The private key and X.500 Distinguished Name associated with <i>alias</i> are used to create the PKCS#10 certificate request. In order to access the private key, the appropriate password must be provided, since private keys are protected in the keystore with a password. If <i>keypass</i> is not provided at the command line, and is different from the password used to protect the integrity of the keystore, the user is prompted for it. </p>
<p> <i>sigalg</i> specifies the algorithm that should be used to sign the CSR. </p>
<p> The CSR is stored in the file <i>certreq_file</i>. If no file is given, the CSR is output to stdout. </p>
<p> Use the <i>importcert</i> command to import the response from the CA.</p>
<dl>
<dt>-exportcert {-alias alias} {-file cert_file} {-storetype storetype} {-keystore keystore} [-storepass storepass] {-providerName provider_name} {-providerClass provider_class_name {-providerArg provider_arg}} {-rfc} {-v} {-protected} {-Jjavaoption}</p>
<dd></dl>
<p> Reads (from the keystore) the certificate associated with <i>alias</i>, and stores it in the file <i>cert_file</i>. </p>
<p> If no file is given, the certificate is output to stdout. </p>
<p> The certificate is by default output in binary encoding, but will instead be output in the printable encoding format, as defined by the Internet RFC 1421 standard, if the <i>-rfc</i> option is specified. </p>
<p> If <i>alias</i> refers to a trusted certificate, that certificate is output. Otherwise, <i>alias</i> refers to a key entry with an associated certificate chain. In that case, the first certificate in the chain is returned. This certificate authenticates the public key of the entity addressed by <i>alias</i>. </p>
<p> This command was named <i>-export</i> in previous releases. This old name is still supported in this release and will be supported in future releases, but for clarify the new name, <i>-exportcert</i>, is preferred going forward.</dl>
</dl>
<h3>Displaying Data</h3>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>-list {-alias alias} {-storetype storetype} {-keystore keystore} [-storepass storepass] {-providerName provider_name} {-providerClass provider_class_name {-providerArg provider_arg}} {-v | -rfc} {-protected} {-Jjavaoption}</p>
<dd></dl>
<p> Prints (to stdout) the contents of the keystore entry identified by <i>alias</i>. If no alias is specified, the contents of the entire keystore are printed. </p>
<p> This command by default prints the MD5 fingerprint of a certificate. If the <i>-v</i> option is specified, the certificate is printed in human-readable format, with additional information such as the owner, issuer, serial number, and any extensions. If the <i>-rfc</i> option is specified, certificate contents are printed using the printable encoding format, as defined by the Internet RFC 1421 standard </p>
<p> You cannot specify both <i>-v</i> and <i>-rfc</i>.</p>
<dl>
<dt>-printcert {-file cert_file} {-v} {-Jjavaoption}</p>
<dd></dl>
<p> Internet RFC 1421 standard. </p>
<p> Note: This option can be used independently of a keystore.</dl>
</dl>
<h3>Managing the Keystore</h3>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>-storepasswd [-new new_storepass] {-storetype storetype} {-keystore keystore} [-storepass storepass] {-providerName provider_name} {-providerClass provider_class_name {-providerArg provider_arg}} {-v} {-Jjavaoption}</p>
<dd></dl>
<p> Changes the password used to protect the integrity of the keystore contents. The new password is <i>new_storepass</i>, which must be at least 6 characters long.</p>
<dl>
<dt>-keypasswd {-alias alias} [-keypass old_keypass] [-new new_keypass] {-storetype storetype} {-keystore keystore} [-storepass storepass] {-providerName provider_name} {-providerClass provider_class_name {-providerArg provider_arg}} {-v} {-Jjavaoption}</p>
<dd></dl>
<p> Changes the password under which the private/secret key identified by <i>alias</i> is protected, from <i>old_keypass</i> to <i>new_keypass</i>, which must be at least 6 characters long. </p>
<p> If the <i>-keypass</i> option is not provided at the command line, and the key password is different from the keystore password, the user is prompted for it. </p>
<p> If the <i>-new</i> option is not provided at the command line, the user is prompted for it.</p>
<dl>
<dt>-delete [-alias alias] {-storetype storetype} {-keystore keystore} [-storepass storepass] {-providerName provider_name} {-providerClass provider_class_name {-providerArg provider_arg}} {-v} {-protected} {-Jjavaoption}</p>
<dd></dl>
<p> Deletes from the keystore the entry identified by <i>alias</i>. The user is prompted for the alias, if no alias is provided at the command line.</p>
<dl>
<dt>-changealias {-alias alias} [-destalias destalias] [-keypass keypass] {-storetype storetype} {-keystore keystore} [-storepass storepass] {-providerName provider_name} {-providerClass provider_class_name {-providerArg provider_arg}} {-v} {-protected} {-Jjavaoption}</p>
<dd></dl>
<p> Move an existing keystore entry from the specified <i>alias</i> to a new alias, <i>destalias</i>. If no destination alias is provided, the command will prompt for one. If the original entry is protected with an entry password, the password can be supplied via the &quot;-keypass&quot; option. If no key password is provided, the <i>storepass</i> (if given) will be attempted first. If that attempt fails, the user will be prompted for a password.</dl>
</dl>
<h3>Getting Help</h3>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>-help</p>
<dd></dl>
<p> Lists the basic commands and their options.</dl>
</dl>
<h2>Examples</h2>
<p>Suppose you want to create a keystore for managing your public/private key pair and certificates from entities you trust. </p>
<h3>Generating Your Key Pair</h3>
<dl>
<dd>The first thing you need to do is create a keystore and generate the key pair. You could use a command such as the following: </p>
<pre><code> keytool -genkeypair -dname &quot;cn=Mark Jones, ou=JavaSoft, o=Sun, c=US&quot;
 -alias business -keypass kpi135 -keystore /working/mykeystore
 -storepass ab987c -validity 180</code></pre>
<p>(Please note: This must be typed as a single line. Multiple lines are used in the examples just for legibility purposes.) </p>
<p> This command creates the keystore named &quot;mykeystore&quot; in the &quot;working&quot; directory (assuming it doesn&#8217;t already exist), and assigns it the password &quot;ab987c&quot;. It generates a public/private key pair for the entity whose &quot;distinguished name&quot; has a common name of &quot;Mark Jones&quot;, organizational unit of &quot;JavaSoft&quot;, organization of &quot;Sun&quot; and two-letter country code of &quot;US&quot;. It uses the default &quot;DSA&quot; key generation algorithm to create the keys, both 1024 bits long. </p>
<p> It creates a self-signed certificate (using the default &quot;SHA1withDSA&quot; signature algorithm) that includes the public key and the distinguished name information. This certificate will be valid for 180 days, and is associated with the private key in a keystore entry referred to by the alias &quot;business&quot;. The private key is assigned the password &quot;kpi135&quot;. </p>
<p> The command could be significantly shorter if option defaults were accepted. As a matter of fact, no options are required; defaults are used for unspecified options that have default values, and you are prompted for any required values. Thus, you could simply have the following: </p>
<pre><code> keytool -genkeypair</code></pre>
<p>In this case, a keystore entry with alias &quot;mykey&quot; is created, with a newly-generated key pair and a certificate that is valid for 90 days. This entry is placed in the keystore named &quot;.keystore&quot; in your home directory. (The keystore is created if it doesn&#8217;t already exist.) You will be prompted for the distinguished name information, the keystore password, and the private key password. </p>
<p> The rest of the examples assume you executed the <i>-genkeypair</i> command without options specified, and that you responded to the prompts with values equal to those given in the first <i>-genkeypair</i> command, above (a private key password of &quot;kpi135&quot;, etc.) </p>
</dl>
<h3>Requesting a Signed Certificate from a Certification Authority</h3>
<dl>
<dd>So far all we&#8217;ve got is a self-signed certificate. A certificate is more likely to be trusted by others if it is signed by a Certification Authority (CA). To get such a signature, you first generate a Certificate Signing Request (CSR), via the following: </p>
<pre><code> keytool -certreq -file MarkJ.csr</code></pre>
<p>This creates a CSR (for the entity identified by the default alias &quot;mykey&quot;) and puts the request in the file named &quot;MarkJ.csr&quot;. Submit this file to a CA, such as VeriSign, Inc. The CA will authenticate you, the requestor (usually off-line), and then will return a certificate, signed by them, authenticating your public key. (In some cases, they will actually return a chain of certificates, each one authenticating the public key of the signer of the previous certificate in the chain.)</dl>
<h3>Importing a Certificate for the CA</h3>
<dl>
<dd>You need to replace your self-signed certificate with a certificate chain, where each certificate in the chain authenticates the public key of the signer of the previous certificate in the chain, up to a &quot;root&quot; CA. </p>
<p> Before you import the certificate reply from a CA, you need one or more &quot;trusted certificates&quot; in your keystore or in the <i>cacerts</i> keystore file (which is described in importcert command): </p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>If the certificate reply is a certificate chain, you just need the top certificate of the chain (that is, the &quot;root&quot; CA certificate authenticating that CA&#8217;s public key).</p>
<dt>o</p>
<dd>If the certificate reply is a single certificate, you need a certificate for the issuing CA (the one that signed it), and if that certificate is not self-signed, you need a certificate for its signer, and so on, up to a self-signed &quot;root&quot; CA certificate.</dl>
</dl>
<p> The &quot;cacerts&quot; keystore file ships with five VeriSign root CA certificates, so you probably won&#8217;t need to import a VeriSign certificate as a trusted certificate in your keystore. But if you request a signed certificate from a different CA, and a certificate authenticating that CA&#8217;s public key hasn&#8217;t been added to &quot;cacerts&quot;, you will need to import a certificate from the CA as a &quot;trusted certificate&quot;. </p>
<p> A certificate from a CA is usually either self-signed, or signed by another CA (in which case you also need a certificate authenticating that CA&#8217;s public key). Suppose company ABC, Inc., is a CA, and you obtain a file named &quot;ABCCA.cer&quot; that is purportedly a self-signed certificate from ABC, authenticating that CA&#8217;s public key. </p>
<p> Be very careful to ensure the certificate is valid prior to importing it as a &quot;trusted&quot; certificate! View it first (using the <code>keytool</code> <i>-printcert</i> command, or the <code>keytool</code> <i>-importcert</i> command without the <i>-noprompt</i> option), and make sure that the displayed certificate fingerprint(s) match the expected ones. You can call the person who sent the certificate, and compare the fingerprint(s) that you see with the ones that they show (or that a secure public key repository shows). Only if the fingerprints are equal is it guaranteed that the certificate has not been replaced in transit with somebody else&#8217;s (for example, an attacker&#8217;s) certificate. If such an attack took place, and you did not check the certificate before you imported it, you would end up trusting anything the attacker has signed. </p>
<p> If you trust that the certificate is valid, then you can add it to your keystore via the following: </p>
<pre><code> keytool -importcert -alias abc -file ABCCA.cer</code></pre>
<p>This creates a &quot;trusted certificate&quot; entry in the keystore, with the data from the file &quot;ABCCA.cer&quot;, and assigns the alias &quot;abc&quot; to the entry.</dl>
<h3>Importing the Certificate Reply from the CA</h3>
<dl>
<dd>Once you&#8217;ve imported a certificate authenticating the public key of the CA you submitted your certificate signing request to (or there&#8217;s already such a certificate in the &quot;cacerts&quot; file), you can import the certificate reply and thereby replace your self-signed certificate with a certificate chain. This chain is the one returned by the CA in response to your request (if the CA reply is a chain), or one constructed (if the CA reply is a single certificate) using the certificate reply and trusted certificates that are already available in the keystore where you import the reply or in the &quot;cacerts&quot; keystore file. </p>
<p> For example, suppose you sent your certificate signing request to VeriSign. You can then import the reply via the following, which assumes the returned certificate is named &quot;VSMarkJ.cer&quot;: </p>
<pre><code> keytool -importcert -trustcacerts -file VSMarkJ.cer</code></pre>
</dl>
<h3>Exporting a Certificate Authenticating Your Public Key</h3>
<dl>
<dd>Suppose you have used the <i>jarsigner</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/tooldocs/solaris/jarsigner.html">http://java.sun.com/javase/6/docs/tooldocs/solaris/jarsigner.html</a> tool to sign a Java ARchive (JAR) file. Clients that want to use the file will want to authenticate your signature. </p>
<p> One way they can do this is by first importing your public key certificate into their keystore as a &quot;trusted&quot; entry. You can export the certificate and supply it to your clients. As an example, you can copy your certificate to a file named <i>MJ.cer</i> via the following, assuming the entry is aliased by &quot;mykey&quot;: </p>
<pre><code> keytool -exportcert -alias mykey -file MJ.cer</code></pre>
<p>Given that certificate, and the signed JAR file, a client can use the <code>jarsigner</code> tool to authenticate your signature.</dl>
<h3>Importing Keystore</h3>
<dl>
<dd>The command &quot;importkeystore&quot; is used to import an entire keystore into another keystore, which means all entries from the source keystore, including keys and certificates, are all imported to the destination keystore within a single command. You can use this command to import entries from a different type of keystore. During the import, all new entries in the destination keystore will have the same alias names and protection passwords (for secret keys and private keys). If <code>keytool</code> has difficulties recover the private keys or secret keys from the source keystore, it will prompt you for a password. If it detects alias duplication, it will ask you for a new one, you can specify a new alias or simply allow <code>keytool</code> to overwrite the existing one. </p>
<p> For example, to import entries from a normal JKS type keystore key.jks into a PKCS #11 type hardware based keystore, you can use the command: </p>
<pre><code>keytool -importkeystore
 -srckeystore key.jks -destkeystore NONE
 -srcstoretype JKS -deststoretype PKCS11
 -srcstorepass changeit -deststorepass topsecret</code></pre>
<p>The importkeystore command can also be used to import a single entry from a source keystore to a destination keystore. In this case, besides the options you see in the above example, you need to specify the alias you want to import. With the srcalias option given, you can also specify the desination alias name in the command line, as well as protection password for a secret/private key and the destination protection password you want. In this way, you can issue a <code>keytool</code> command that will never ask you a question. This makes it very convenient to include a <code>keytool</code> command into a script file, like this: </p>
<pre><code>keytool -importkeystore
 -srckeystore key.jks -destkeystore NONE
 -srcstoretype JKS -deststoretype PKCS11
 -srcstorepass changeit -deststorepass topsecret
 -srcalias myprivatekey -destalias myoldprivatekey
 -srckeypass oldkeypass -destkeypass mynewkeypass
 -noprompt</code></pre>
</dl>
<h2>TERMINOLOGY and WARNINGS</h2>
<h3>KeyStore</h3>
<dl>
<dd>A keystore is a storage facility for cryptographic keys and certificates.</dl>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>
<dt>o</p>
<dd><code>KeyStore Entries</code></p>
<dl>
<dd>Keystores may have different types of entries. The two most applicable entry types for <code>keytool</code> include:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd><code>key entries</code> &#8211; each holds very sensitive cryptographic key information, which is stored in a protected format to prevent unauthorized access. Typically, a key stored in this type of entry is a secret key, or a private key accompanied by the certificate &quot;chain&quot; for the corresponding public key. The <code>keytool</code> can handle both types od entry, while <code>jarsigner</code> tool only handle the latter type of entry, that is private keys and their associated certificate chains.</p>
<dt>2.</p>
<dd><code>trusted certificate entries</code> &#8211; each contains a single public key certificate belonging to another party. It is called a &quot;trusted certificate&quot; because the keystore owner trusts that the public key in the certificate indeed belongs to the identity identified by the &quot;subject&quot; (owner) of the certificate. The issuer of the certificate vouches for this, by signing the certificate.</dl>
</dl>
</dl>
<dt>o</p>
<dd><code>KeyStore Aliases</code></p>
<dl>
<dd>All keystore entries (key and trusted certificate entries) are accessed via unique <i>aliases</i>. </p>
<p> An alias is specified when you add an entity to the keystore using the -genseckey command to generate a secret key, -genkeypair command to generate a key pair (public and private key) or the -importcert command to add a certificate or certificate chain to the list of trusted certificates. Subsequent <code>keytool</code> commands must use this same alias to refer to the entity. </p>
<p> For example, suppose you use the alias <i>duke</i> to generate a new public/private key pair and wrap the public key into a self-signed certificate (see Certificate Chains) via the following command: </p>
<pre><code> keytool -genkeypair -alias duke -keypass dukekeypasswd</code></pre>
<p>This specifies an inital password of &quot;dukekeypasswd&quot; required by subsequent commands to access the private key assocated with the alias <i>duke</i>. If you later want to change duke&#8217;s private key password, you use a command like the following: </p>
<pre><code> keytool -keypasswd -alias duke -keypass dukekeypasswd -new newpass</code></pre>
<p>This changes the password from &quot;dukekeypasswd&quot; to &quot;newpass&quot;. </p>
<p> Please note: A password should not actually be specified on a command line or in a script unless it is for testing purposes, or you are on a secure system. If you don&#8217;t specify a required password option on a command line, you will be prompted for it. </p>
</dl>
<dt>o</p>
<dd><code>KeyStore Implementation</code></p>
<dl>
<dd>The <i>KeyStore</i> class provided in the <i>java.security</i> package supplies well-defined interfaces to access and modify the information in a keystore. It is possible for there to be multiple different concrete implementations, where each implementation is that for a particular <i>type</i> of keystore. </p>
<p> Currently, two command-line tools (<code>keytool</code> and <code>jarsigner</code>) and a GUI-based tool named <code>Policy Tool</code> make use of keystore implementations. Since <i>KeyStore</i> is publicly available, users can write additional security applications that use it. </p>
<p> There is a built-in default implementation, provided by Sun Microsystems. It implements the keystore as a file, utilizing a proprietary keystore type (format) named &quot;JKS&quot;. It protects each private key with its individual password, and also protects the integrity of the entire keystore with a (possibly different) password. </p>
<p> Keystore implementations are provider-based. More specifically, the application interfaces supplied by <i>KeyStore</i> are implemented in terms of a &quot;Service Provider Interface&quot; (SPI). That is, there is a corresponding abstract <i>KeystoreSpi</i> class, also in the <i>java.security</i> package, which defines the Service Provider Interface methods that &quot;providers&quot; must implement. (The term &quot;provider&quot; refers to a package or a set of packages that supply a concrete implementation of a subset of services that can be accessed by the Java Security API.) Thus, to provide a keystore implementation, clients must implement a &quot;provider&quot; and supply a KeystoreSpi subclass implementation, as described in How to Implement a Provider for the Java Cryptography Architecture. </p>
<p> Applications can choose different <i>types</i> of keystore implementations from different providers, using the &quot;getInstance&quot; factory method supplied in the <i>KeyStore</i> class. A keystore type defines the storage and data format of the keystore information, and the algorithms used to protect private/secret keys in the keystore and the integrity of the keystore itself. Keystore implementations of different types are not compatible. </p>
<p> <code>keytool</code> works on any file-based keystore implementation. (It treats the keytore location that is passed to it at the command line as a filename and converts it to a FileInputStream, from which it loads the keystore information.) The <code>jarsigner</code> and <code>policytool</code> tools, on the other hand, can read a keystore from any location that can be specified using a URL. </p>
<p> For <code>keytool</code> and <code>jarsigner</code>, you can specify a keystore type at the command line, via the <i>-storetype</i> option. For <code>Policy Tool</code>, you can specify a keystore type via the &quot;Keystore&quot; menu. </p>
<p> If you don&#8217;t explicitly specify a keystore type, the tools choose a keystore implementation based simply on the value of the <i>keystore.type</i> property specified in the security properties file. The security properties file is called <i>java.security</i>, and it resides in the security properties directory, <i>java.home</i>/lib/security, where <i>java.home</i> is the runtime environment&#8217;s directory (the <i>jre</i> directory in the SDK or the top-level directory of the Java 2 Runtime Environment). </p>
<p> Each tool gets the <i>keystore.type</i> value and then examines all the currently-installed providers until it finds one that implements keystores of that type. It then uses the keystore implementation from that provider. </p>
<p> The <i>KeyStore</i> class defines a static method named <i>getDefaultType</i> that lets applications and applets retrieve the value of the <i>keystore.type</i> property. The following line of code creates an instance of the default keystore type (as specified in the <i>keystore.type</i> property): </p>
<pre><code> KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());</code></pre>
<p>The default keystore type is &quot;jks&quot; (the proprietary type of the keystore implementation provided by Sun). This is specified by the following line in the security properties file: </p>
<pre><code> keystore.type=jks</code></pre>
<p>To have the tools utilize a keystore implementation other than the default, you can change that line to specify a different keystore type. </p>
<p> For example, if you have a provider package that supplies a keystore implementation for a keystore type called &quot;pkcs12&quot;, change the line to </p>
<pre><code> keystore.type=pkcs12</code></pre>
<p>Note: case doesn&#8217;t matter in keystore type designations. For example, &quot;JKS&quot; would be considered the same as &quot;jks&quot;.</dl>
</dl>
</dl>
<h3>Certificate</h3>
<dl>
<dd>A <code>certificate</code> (also known as a <code>public-key certificate</code>) is a digitally signed statement from one entity (the <i>issuer</i>), saying that the public key (and some other information) of another entity (the <i>subject</i>) has some specific value.</dl>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>
<dt>o</p>
<dd><code>Certificate Terms</code></p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>Public Keys</p>
<dd>These are numbers associated with a particular entity, and are intended to be known to everyone who needs to have trusted interactions with that entity. Public keys are used to verify signatures.</p>
<dt>Digitally Signed</p>
<dd>If some data is <i>digitally signed</i> it has been stored with the &quot;identity&quot; of an entity, and a signature that proves that entity knows about the data. The data is rendered unforgeable by signing with the entity&#8217;s private key.</p>
<dt>Identity</p>
<dd>A known way of addressing an entity. In some systems the identity is the public key, in others it can be anything from a Unix UID to an Email address to an X.509 Distinguished Name.</p>
<dt>Signature</p>
<dd>A signature is computed over some data using the private key of an entity (the <i>signer</i>, which in the case of a certificate is also known as the <i>issuer</i>).</p>
<dt>Private Keys</p>
<dd>These are numbers, each of which is supposed to be known only to the particular entity whose private key it is (that is, it&#8217;s supposed to be kept secret). Private and public keys exist in pairs in all public key cryptography systems (also referred to as &quot;public key crypto systems&quot;). In a typical public key crypto system, such as DSA, a private key corresponds to exactly one public key. Private keys are used to compute signatures.</p>
<dt>Entity</p>
<dd>An entity is a person, organization, program, computer, business, bank, or something else you are trusting to some degree.</dl>
</dl>
<p> Basically, public key cryptography requires access to users&#8217; public keys. In a large-scale networked environment it is impossible to guarantee that prior relationships between communicating entities have been established or that a trusted repository exists with all used public keys. Certificates were invented as a solution to this public key distribution problem. Now a <i>Certification Authority</i> (CA) can act as a trusted third party. CAs are entities (for example, businesses) that are trusted to sign (issue) certificates for other entities. It is assumed that CAs will only create valid and reliable certificates, as they are bound by legal agreements. There are many public Certification Authorities, such as <i>VeriSign</i> @ <a rel="nofollow" href="http://www.verisign.com/,">http://www.verisign.com/,</a> <i>Thawte</i> @ <a rel="nofollow" href="http://www.thawte.com/,">http://www.thawte.com/,</a> <i>Entrust</i> @ <a rel="nofollow" href="http://www.entrust.com/,">http://www.entrust.com/,</a> and so on. You can also run your own Certification Authority using products such as the Netscape/Microsoft Certificate Servers or the Entrust CA product for your organization. </p>
<p> Using <code>keytool</code>, it is possible to display, import, and export certificates. It is also possible to generate self-signed certificates. </p>
<p> <code>keytool</code> currently handles X.509 certificates. </p>
</dl>
<dt>o</p>
<dd><code>X.509 Certificates</code></p>
<dl>
<dd>The X.509 standard defines what information can go into a certificate, and describes how to write it down (the data format). All the data in a certificate is encoded using two related standards called ASN.1/DER. <i>Abstract Syntax Notation 1</i> describes data. The <i>Definite Encoding Rules</i> describe a single way to store and transfer that data. </p>
<p> All X.509 certificates have the following data, in addition to the signature: </p>
<dl>
<dd>
<dl>
<dt>Version</p>
<dd>This identifies which version of the X.509 standard applies to this certificate, which affects what information can be specified in it. Thus far, three versions are defined. <code>keytool</code> can import and export v1, v2, and v3 certificates. It generates v3 certificates.</dl>
<p> <i>X.509 Version 1</i> has been available since 1988, is widely deployed, and is the most generic. </p>
<p> <i>X.509 Version 2</i> introduced the concept of subject and issuer unique identifiers to handle the possibility of reuse of subject and/or issuer names over time. Most certificate profile documents strongly recommend that names not be reused, and that certificates should not make use of unique identifiers. Version 2 certificates are not widely used. </p>
<p> <i>X.509 Version 3</i> is the most recent (1996) and supports the notion of extensions, whereby anyone can define an extension and include it in the certificate. Some common extensions in use today are: <i>KeyUsage</i> (limits the use of the keys to particular purposes such as &quot;signing-only&quot;) and <i>AlternativeNames</i> (allows other identities to also be associated with this public key, e.g. DNS names, Email addresses, IP addresses). Extensions can be marked <i>critical</i> to indicate that the extension should be checked and enforced/used. For example, if a certificate has the KeyUsage extension marked critical and set to &quot;keyCertSign&quot; then if this certificate is presented during SSL communication, it should be rejected, as the certificate extension indicates that the associated private key should only be used for signing certificates and not for SSL use.</p>
<dl>
<dt>Serial Number</p>
<dd>The entity that created the certificate is responsible for assigning it a serial number to distinguish it from other certificates it issues. This information is used in numerous ways, for example when a certificate is revoked its serial number is placed in a Certificate Revocation List (CRL).</p>
<dt>Signature Algorithm Identifier</p>
<dd>This identifies the algorithm used by the CA to sign the certificate.</p>
<dt>Issuer Name</p>
<dd>The X.500 Distinguished Name of the entity that signed the certificate. This is normally a CA. Using this certificate implies trusting the entity that signed this certificate. (Note that in some cases, such as <i>root or top-level</i> CA certificates, the issuer signs its own certificate.)</p>
<dt>Validity Period</p>
<dd>Each certificate is valid only for a limited amount of time. This period is described by a start date and time and an end date and time, and can be as short as a few seconds or almost as long as a century. The validity period chosen depends on a number of factors, such as the strength of the private key used to sign the certificate or the amount one is willing to pay for a certificate. This is the expected period that entities can rely on the public value, if the associated private key has not been compromised.</p>
<dt>Subject Name</p>
<dd>The name of the entity whose public key the certificate identifies. This name uses the X.500 standard, so it is intended to be unique across the Internet. This is the X.500 Distinguished Name (DN) of the entity, for example, </p>
<pre><code> CN=Java Duke, OU=Java Software Division, O=Sun Microsystems Inc, C=US</code></pre>
<p>(These refer to the subject&#8217;s Common Name, Organizational Unit, Organization, and Country.)</p>
<dt>Subject Public Key Information</p>
<dd>This is the public key of the entity being named, together with an algorithm identifier which specifies which public key crypto system this key belongs to and any associated key parameters.</dl>
</dl>
</dl>
<dt>o</p>
<dd><code>Certificate Chains</code></p>
<dl>
<dd><code>keytool</code> can create and manage keystore &quot;key&quot; entries that each contain a private key and an associated certificate &quot;chain&quot;. The first certificate in the chain contains the public key corresponding to the private key. </p>
<p> When keys are first generated (see the -genkeypair command), the chain starts off containing a single element, a <i>self-signed certificate</i>. A self-signed certificate is one for which the issuer (signer) is the same as the subject (the entity whose public key is being authenticated by the certificate). Whenever the <i>-genkeypair</i> command is called to generate a new public/private key pair, it also wraps the public key into a self-signed certificate. </p>
<p> Later, after a Certificate Signing Request (CSR) has been generated (see the -certreq command) and sent to a Certification Authority (CA), the response from the CA is imported (see -importcert), and the self-signed certificate is replaced by a chain of certificates. At the bottom of the chain is the certificate (reply) issued by the CA authenticating the subject&#8217;s public key. The next certificate in the chain is one that authenticates the <i>CA</i>&#8216;s public key. </p>
<p> In many cases, this is a self-signed certificate (that is, a certificate from the CA authenticating its own public key) and the last certificate in the chain. In other cases, the CA may return a chain of certificates. In this case, the bottom certificate in the chain is the same (a certificate signed by the CA, authenticating the public key of the key entry), but the second certificate in the chain is a certificate signed by a <i>different</i> CA, authenticating the public key of the CA you sent the CSR to. Then, the next certificate in the chain will be a certificate authenticating the second CA&#8217;s key, and so on, until a self-signed &quot;root&quot; certificate is reached. Each certificate in the chain (after the first) thus authenticates the public key of the signer of the previous certificate in the chain. </p>
<p> Many CAs only return the issued certificate, with no supporting chain, especially when there is a flat hierarchy (no intermediates CAs). In this case, the certificate chain must be established from trusted certificate information already stored in the keystore. </p>
<p> A different reply format (defined by the PKCS#7 standard) also includes the supporting certificate chain, in addition to the issued certificate. Both reply formats can be handled by <code>keytool</code>. </p>
<p> The top-level (root) CA certificate is self-signed. However, the trust into the root&#8217;s public key does not come from the root certificate itself (anybody could generate a self-signed certificate with the distinguished name of say, the VeriSign root CA!), but from other sources like a newspaper. The root CA public key is widely known. The only reason it is stored in a certificate is because this is the format understood by most tools, so the certificate in this case is only used as a &quot;vehicle&quot; to transport the root CA&#8217;s public key. Before you add the root CA certificate to your keystore, you should view it (using the <i>-printcert</i> option) and compare the displayed fingerprint with the well-known fingerprint (obtained from a newspaper, the root CA&#8217;s webpage, etc.). </p>
</dl>
<dt>o</p>
<dd><code>The cacerts Certificates File</code></p>
<dl>
<dd>A certificates file named <code>&quot;cacerts&quot;</code> resides in the security properties directory, <i>java.home</i>/lib/security, where <i>java.home</i> is the runtime environment&#8217;s directory (the <i>jre</i> directory in the SDK or the top-level directory of the Java 2 Runtime Environment). </p>
<p> The &quot;cacerts&quot; file represents a system-wide keystore with CA certificates. System administrators can configure and manage that file using <code>keytool</code>, specifying &quot;jks&quot; as the keystore type. The &quot;cacerts&quot; keystore file ships with several root CA certificates with the following aliases and X.500 owner distinguished names: </p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd><code>Alias</code>: thawtepersonalfreemailca<br />
 <code>Owner DN</code>: EmailAddress=personal-freemail [at] thawte.com,<br />
 CN=Thawte Personal Freemail CA,<br />
 OU=Certification Services Division,<br />
 O=Thawte Consulting, L=Cape Town, ST=Western Cape, C=ZA</p>
<dt>*</p>
<dd><code>Alias</code>: thawtepersonalbasicca<br />
 <code>Owner DN</code>: EmailAddress=personal-basic [at] thawte.com,<br />
 CN=Thawte Personal Basic CA,<br />
 OU=Certification Services Division,<br />
 O=Thawte Consulting, L=Cape Town, ST=Western Cape, C=ZA</p>
<dt>*</p>
<dd><code>Alias</code>: thawtepersonalpremiumca<br />
 <code>Owner DN</code>: EmailAddress=personal-premium [at] thawte.com,<br />
 CN=Thawte Personal Premium CA,<br />
 OU=Certification Services Division,<br />
 O=Thawte Consulting, L=Cape Town, ST=Western Cape, C=ZA</p>
<dt>*</p>
<dd><code>Alias</code>: thawteserverca<br />
 <code>Owner DN</code>: EmailAddress=server-certs [at] thawte.com,<br />
 CN=Thawte Server CA, OU=Certification Services Division,<br />
 O=Thawte Consulting cc, L=Cape Town, ST=Western Cape, C=ZA</p>
<dt>*</p>
<dd><code>Alias</code>: thawtepremiumserverca<br />
 <code>Owner DN</code>: EmailAddress=premium-server [at] thawte.com,<br />
 CN=Thawte Premium Server CA,<br />
 OU=Certification Services Division,<br />
 O=Thawte Consulting cc, L=Cape Town, ST=Western Cape, C=ZA</p>
<dt>*</p>
<dd><code>Alias</code>: verisignclass1ca<br />
 <code>Owner DN</code>: OU=Class 1 Public Primary Certification Authority,<br />
 O=&quot;VeriSign, Inc.&quot;, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: verisignclass2ca<br />
 <code>Owner DN</code>: OU=Class 2 Public Primary Certification Authority,<br />
 O=&quot;VeriSign, Inc.&quot;, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: verisignclass3ca<br />
 <code>Owner DN</code>: OU=Class 3 Public Primary Certification Authority,<br />
 O=&quot;VeriSign, Inc.&quot;, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: verisignserverca<br />
 <code>Owner DN</code>: OU=Secure Server Certification Authority,<br />
 O=&quot;RSA Data Security, Inc.&quot;, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: verisignclass1g2ca<br />
 <code>Owner DN</code>: OU=VeriSign Trust Network,<br />
 OU=&quot;(c) 1998 VeriSign, Inc. &#8211; For authorized use only&quot;,<br />
 OU=Class 1 Public Primary Certification Authority &#8211; G2,<br />
 O=&quot;VeriSign, Inc.&quot;, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: verisignclass1g3ca<br />
 <code>Owner DN</code>: CN=VeriSign Class 1 Public Primary Certification Authority &#8211; G3, OU=&quot;(c) 1999 VeriSign, Inc. &#8211; For authorized use only&quot;,<br />
 OU=VeriSign Trust Network,<br />
 O=&quot;VeriSign, Inc.&quot;, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: verisignclass2g2ca<br />
 <code>Owner DN</code>: OU=VeriSign Trust Network,<br />
 OU=&quot;(c) 1998 VeriSign, Inc. &#8211; For authorized use only&quot;,<br />
 OU=Class 2 Public Primary Certification Authority &#8211; G2,<br />
 O=&quot;VeriSign, Inc.&quot;, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: verisignclass2g3ca<br />
 <code>Owner DN</code>: CN=VeriSign Class 2 Public Primary Certification Authority &#8211; G3,<br />
 OU=&quot;(c) 1999 VeriSign, Inc. &#8211; For authorized use only&quot;,<br />
 OU=VeriSign Trust Network,<br />
 O=&quot;VeriSign, Inc.&quot;, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: verisignclass3g2ca<br />
 <code>Owner DN</code>: OU=VeriSign Trust Network,<br />
 OU=&quot;(c) 1998 VeriSign, Inc. &#8211; For authorized use only&quot;,<br />
 OU=Class 3 Public Primary Certification Authority &#8211; G2,<br />
 O=&quot;VeriSign, Inc.&quot;, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: verisignclass3g3ca<br />
 <code>Owner DN</code>: CN=VeriSign Class 3 Public Primary Certification Authority &#8211; G3,<br />
 OU=&quot;(c) 1999 VeriSign, Inc. &#8211; For authorized use only&quot;,<br />
 OU=VeriSign Trust Network,<br />
 O=&quot;VeriSign, Inc.&quot;, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: baltimorecodesigningca<br />
 <code>Owner DN</code>: CN=Baltimore CyberTrust Code Signing Root,<br />
 OU=CyberTrust, O=Baltimore, C=IE</p>
<dt>*</p>
<dd><code>Alias</code>: gtecybertrustglobalca<br />
 <code>Owner DN</code>: CN=GTE CyberTrust Global Root,<br />
 OU=&quot;GTE CyberTrust Solutions, Inc.&quot;, O=GTE Corporation, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: baltimorecybertrustca<br />
 <code>Owner DN</code>: CN=Baltimore CyberTrust Root,<br />
 OU=CyberTrust, O=Baltimore, C=IE</p>
<dt>*</p>
<dd><code>Alias</code>: gtecybertrustca<br />
 <code>Owner DN</code>: CN=GTE CyberTrust Root,<br />
 O=GTE Corporation, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: gtecybertrust5ca<br />
 <code>Owner DN</code>: CN=GTE CyberTrust Root 5,<br />
 OU=&quot;GTE CyberTrust Solutions, Inc.&quot;, O=GTE Corporation, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: entrustclientca<br />
 <code>Owner DN</code>: CN=Entrust.net Client Certification Authority,<br />
 OU=(c) 1999 Entrust.net Limited,<br />
 OU=<a rel="nofollow" href="http://www.entrust.net">www.entrust.net</a>/Client_CA_Info/CPS incorp. by ref. limits liab.,<br />
 O=Entrust.net, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: entrustglobalclientca<br />
 <code>Owner DN</code>: CN=Entrust.net Client Certification Authority,<br />
 OU=(c) 2000 Entrust.net Limited,<br />
 OU=<a rel="nofollow" href="http://www.entrust.net">www.entrust.net</a>/GCCA_CPS incorp. by ref. (limits liab.),<br />
 O=Entrust.net</p>
<dt>*</p>
<dd><code>Alias</code>: entrust2048ca<br />
 <code>Owner DN</code>: CN=Entrust.net Certification Authority (2048),<br />
 OU=(c) 1999 Entrust.net Limited,<br />
 OU=<a rel="nofollow" href="http://www.entrust.net">www.entrust.net</a>/CPS_2048 incorp. by ref. (limits liab.),<br />
 O=Entrust.net</p>
<dt>*</p>
<dd><code>Alias</code>: entrustsslca<br />
 <code>Owner DN</code>: CN=Entrust.net Secure Server Certification Authority,<br />
 OU=(c) 1999 Entrust.net Limited,<br />
 OU=<a rel="nofollow" href="http://www.entrust.net">www.entrust.net</a>/CPS incorp. by ref. (limits liab.),<br />
 O=Entrust.net, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: entrustgsslca<br />
 <code>Owner DN</code>: CN=Entrust.net Secure Server Certification Authority,<br />
 OU=(c) 2000 Entrust.net Limited,<br />
 OU=<a rel="nofollow" href="http://www.entrust.net">www.entrust.net</a>/SSL_CPS incorp. by ref. (limits liab.),<br />
 O=Entrust.net</p>
<dt>*</p>
<dd><code>Alias</code>: godaddyclass2ca<br />
 <code>Owner DN</code>: OU=Go Daddy Class 2 Certification Authority,<br />
 O=&quot;The Go Daddy Group, Inc.&quot;, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: starfieldclass2ca<br />
 <code>Owner DN</code>: OU=Starfield Class 2 Certification Authority,<br />
 O=&quot;Starfield Technologies, Inc.&quot;, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: valicertclass2ca<br />
 <code>Owner DN</code>: EMAILADDRESS=info [at] valicert.com,<br />
 CN=<a rel="nofollow" href="http://www.valicert.com/,">http://www.valicert.com/,</a><br />
 OU=ValiCert Class 2 Policy Validation Authority,<br />
 O=&quot;ValiCert, Inc.&quot;, L=ValiCert Validation Network</p>
<dt>*</p>
<dd><code>Alias</code>: geotrustglobalca<br />
 <code>Owner DN</code>: CN=GeoTrust Global CA,<br />
 O=GeoTrust Inc., C=US</p>
<dt>*</p>
<dd><code>Alias</code>: equifaxsecureca<br />
 <code>Owner DN</code>: OU=Equifax Secure Certificate Authority,<br />
 O=Equifax, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: equifaxsecureebusinessca1<br />
 <code>Owner DN</code>: CN=Equifax Secure eBusiness CA-1,<br />
 O=Equifax Secure Inc., C=US</p>
<dt>*</p>
<dd><code>Alias</code>: equifaxsecureebusinessca2<br />
 <code>Owner DN</code>: OU=Equifax Secure eBusiness CA-2,<br />
 O=Equifax Secure, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: equifaxsecureglobalebusinessca1<br />
 <code>Owner DN</code>: CN=Equifax Secure Global eBusiness CA-1,<br />
 O=Equifax Secure Inc., C=US</p>
<dt>*</p>
<dd><code>Alias</code>: soneraclass1ca<br />
 <code>Owner DN</code>: CN=Sonera Class1 CA, O=Sonera, C=FI</p>
<dt>*</p>
<dd><code>Alias</code>: soneraclass2ca<br />
 <code>Owner DN</code>: CN=Sonera Class2 CA, O=Sonera, C=FI</p>
<dt>*</p>
<dd><code>Alias</code>: comodoaaaca<br />
 <code>Owner DN</code>: CN=AAA Certificate Services,<br />
 O=Comodo CA Limited, L=Salford, ST=Greater Manchester, C=GB</p>
<dt>*</p>
<dd><code>Alias</code>: addtrustclass1ca<br />
 <code>Owner DN</code>: CN=AddTrust Class 1 CA Root,<br />
 OU=AddTrust TTP Network, O=AddTrust AB, C=SE</p>
<dt>*</p>
<dd><code>Alias</code>: addtrustexternalca<br />
 <code>Owner DN</code>: CN=AddTrust External CA Root,<br />
 OU=AddTrust External TTP Network, O=AddTrust AB, C=SE</p>
<dt>*</p>
<dd><code>Alias</code>: addtrustqualifiedca<br />
 <code>Owner DN</code>: CN=AddTrust Qualified CA Root,<br />
 OU=AddTrust TTP Network, O=AddTrust AB, C=SE</p>
<dt>*</p>
<dd><code>Alias</code>: utnuserfirsthardwareca<br />
 <code>Owner DN</code>: CN=UTN-USERFirst-Hardware,<br />
 OU=<a rel="nofollow" href="http://www.usertrust.com,">http://www.usertrust.com,</a> O=The USERTRUST Network,<br />
 L=Salt Lake City, ST=UT, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: utnuserfirstclientauthemailca<br />
 <code>Owner DN</code>: CN=UTN-USERFirst-Client Authentication and Email,<br />
 OU=<a rel="nofollow" href="http://www.usertrust.com,">http://www.usertrust.com,</a> O=The USERTRUST Network,<br />
 L=Salt Lake City, ST=UT, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: utndatacorpsgcca<br />
 <code>Owner DN</code>: CN=UTN &#8211; DATACorp SGC,<br />
 OU=<a rel="nofollow" href="http://www.usertrust.com,">http://www.usertrust.com,</a> O=The USERTRUST Network,<br />
 L=Salt Lake City, ST=UT, C=US</p>
<dt>*</p>
<dd><code>Alias</code>: utnuserfirstobjectca<br />
 <code>Owner DN</code>: CN=UTN-USERFirst-Object,<br />
 OU=<a rel="nofollow" href="http://www.usertrust.com,">http://www.usertrust.com,</a> O=The USERTRUST Network,<br />
 L=Salt Lake City, ST=UT, C=US</dl>
</dl>
<p> The initial password of the &quot;cacerts&quot; keystore file is &quot;changeit&quot;. System administrators should change that password and the default access permission of that file upon installing the SDK. </p>
<dl>
<dd><code>IMPORTANT: Verify Your </code><tt>cacerts</tt><code> File</code> </p>
<p> Since you trust the CAs in the <i>cacerts</i> file as entities for signing and issuing certificates to other entities, you must manage the <i>cacerts</i> file carefully. The <i>cacerts</i> file should contain only certificates of the CAs you trust. It is your responsibility to verify the trusted root CA certificates bundled in the <i>cacerts</i> file and make your own trust decisions. To remove an untrusted CA certificate from the <i>cacerts</i> file, use the delete option of the <i>keytool</i> command. You can find the <i>cacerts</i> file in the JRE installation directory. Contact your system administrator if you do not have permission to edit this file. </p>
</dl>
</dl>
<dt>o</p>
<dd><code>The Internet RFC 1421 Certificate Encoding Standard</code></p>
<dl>
<dd>Certificates are often stored using the printable encoding format defined by the Internet RFC 1421 standard, instead of their binary encoding. This certificate format, also known as &quot;Base 64 encoding&quot;, facilitates exporting certificates to other applications by email or through some other mechanism. </p>
<p> Certificates read by the <i>-importcert</i> and <i>-printcert</i> commands can be in either this format or binary encoded. </p>
<p> The <i>-exportcert</i> command by default outputs a certificate in binary encoding, but will instead output a certificate in the printable encoding format, if the <i>-rfc</i> option is specified. </p>
<p> The <i>-list</i> command by default prints the MD5 fingerprint of a certificate. If the <i>-v</i> option is specified, the certificate is printed in human-readable format, while if the <i>-rfc</i> option is specified, the certificate is output in the printable encoding format. </p>
<p> In its printable encoding format, the encoded certificate is bounded at the beginning by </p>
<pre><code>-----BEGIN CERTIFICATE-----</code></pre>
<p>and at the end by </p>
<pre><code>-----END CERTIFICATE-----</code></pre>
</dl>
</dl>
</dl>
<h3>X.500 Distinguished Names</h3>
<dl>
<dd>X.500 Distinguished Names are used to identify entities, such as those which are named by the <i>subject</i> and <i>issuer</i> (signer) fields of X.509 certificates. <code>keytool</code> supports the following subparts:</p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd><i>commonName</i> &#8211; common name of a person, e.g., &quot;Susan Jones&quot;</p>
<dt>o</p>
<dd><i>organizationUnit</i> &#8211; small organization (e.g, department or division) name, e.g., &quot;Purchasing&quot;</p>
<dt>o</p>
<dd><i>organizationName</i> &#8211; large organization name, e.g., &quot;ABCSystems, Inc.&quot;</p>
<dt>o</p>
<dd><i>localityName</i> &#8211; locality (city) name, e.g., &quot;Palo Alto&quot;</p>
<dt>o</p>
<dd><i>stateName</i> &#8211; state or province name, e.g., &quot;California&quot;</p>
<dt>o</p>
<dd><i>country</i> &#8211; two-letter country code, e.g., &quot;CH&quot;</dl>
</dl>
<p> When supplying a distinguished name string as the value of a <i>-dname</i> option, as for the <i>-genkeypair</i> command, the string must be in the following format: </p>
<pre><code>CN=</code><tt>cName</tt><code>, OU=</code><tt>orgUnit</tt><code>, O=</code><tt>org</tt><code>, L=</code><tt>city</tt><code>, S=</code><tt>state</tt><code>, C=</code><tt>countryCode</tt></pre>
<p>where all the italicized items represent actual values and the above keywords are abbreviations for the following: </p>
<pre><code> CN=commonName
 OU=organizationUnit
 O=organizationName
 L=localityName
 S=stateName
 C=country</code></pre>
<p>A sample distinguished name string is </p>
<pre><code>CN=Mark Smith, OU=JavaSoft, O=Sun, L=Cupertino, S=California, C=US</code></pre>
<p>and a sample command using such a string is </p>
<pre><code>keytool -genkeypair -dname &quot;CN=Mark Smith, OU=JavaSoft, O=Sun, L=Cupertino,
S=California, C=US&quot; -alias mark</code></pre>
<p>Case does not matter for the keyword abbreviations. For example, &quot;CN&quot;, &quot;cn&quot;, and &quot;Cn&quot; are all treated the same. </p>
<p> Order matters; each subcomponent must appear in the designated order. However, it is not necessary to have all the subcomponents. You may use a subset, for example: </p>
<pre><code>CN=Steve Meier, OU=SunSoft, O=Sun, C=US</code></pre>
<p>If a distinguished name string value contains a comma, the comma must be escaped by a &quot;\&quot; character when you specify the string on a command line, as in </p>
<pre><code> cn=peter schuster, o=Sun Microsystems\, Inc., o=sun, c=us</code></pre>
<p>It is never necessary to specify a distinguished name string on a command line. If it is needed for a command, but not supplied on the command line, the user is prompted for each of the subcomponents. In this case, a comma does not need to be escaped by a &quot;\&quot;. </p>
</dl>
<h3>WARNING Regarding Importing Trusted Certificates</h3>
<dl>
<dd>IMPORTANT: Be sure to check a certificate very carefully before importing it as a trusted certificate! </p>
<p> View it first (using the <i>-printcert</i> command, or the <i>-importcert</i> command without the <i>-noprompt</i> option), and make sure that the displayed certificate fingerprint(s) match the expected ones. For example, suppose someone sends or emails you a certificate, and you put it in a file named <i>/tmp/cert</i>. Before you consider adding the certificate to your list of trusted certificates, you can execute a <i>-printcert</i> command to view its fingerprints, as in </p>
<pre><code> keytool -printcert -file /tmp/cert
 Owner: CN=ll, OU=ll, O=ll, L=ll, S=ll, C=ll
 Issuer: CN=ll, OU=ll, O=ll, L=ll, S=ll, C=ll
 Serial Number: 59092b34
 Valid from: Thu Sep 25 18:01:13 PDT 1997 until: Wed Dec 24 17:01:13 PST 1997
 Certificate Fingerprints:
 MD5: 11:81:AD:92:C8:E5:0E:A2:01:2E:D4:7A:D7:5F:07:6F
 SHA1: 20:B6:17:FA:EF:E5:55:8A:D0:71:1F:E8:D6:9D:C0:37:13:0E:5E:FE</code></pre>
<p>Then call or otherwise contact the person who sent the certificate, and compare the fingerprint(s) that you see with the ones that they show. Only if the fingerprints are equal is it guaranteed that the certificate has not been replaced in transit with somebody else&#8217;s (for example, an attacker&#8217;s) certificate. If such an attack took place, and you did not check the certificate before you imported it, you would end up trusting anything the attacker has signed (for example, a JAR file with malicious class files inside). </p>
<p> Note: it is not required that you execute a <i>-printcert</i> command prior to importing a certificate, since before adding a certificate to the list of trusted certificates in the keystore, the <i>-importcert</i> command prints out the certificate information and prompts you to verify it. You then have the option of aborting the import operation. Note, however, this is only the case if you invoke the <i>-importcert</i> command without the <i>-noprompt</i> option. If the <i>-noprompt</i> option is given, there is no interaction with the user. </p>
</dl>
<h3>Warning Regarding Passwords</h3>
<dl>
<dd>Most commands operating on a keystore require the store password. Some commands require a private/secret key password. </p>
<p> Passwords can be specified on the command line (in the <i>-storepass</i> and <i>-keypass</i> options, respectively). However, a password should not be specified on a command line or in a script unless it is for testing purposes, or you are on a secure system. </p>
<p> If you don&#8217;t specify a required password option on a command line, you will be prompted for it. </p>
</dl>
<h2>See Also</h2>
<dl>
<dd>
<dl>
<dt>o</p>
<dd><i>jar</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/tooldocs/solaris/jar.html">http://java.sun.com/javase/6/docs/tooldocs/solaris/jar.html</a> tool documentation</p>
<dt>o</p>
<dd><i>jarsigner</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/tooldocs/solaris/jarsigner.html">http://java.sun.com/javase/6/docs/tooldocs/solaris/jarsigner.html</a> tool documentation</p>
<dt>o</p>
<dd>the <tt>Security</tt> @ <a rel="nofollow" href="http://java.sun.com/docs/books/tutorial/security/index.html">http://java.sun.com/docs/books/tutorial/security/index.html</a> trail of the <tt>Java Tutorial</tt> @ <a rel="nofollow" href="http://java.sun.com/docs/books/tutorial/trailmap.html">http://java.sun.com/docs/books/tutorial/trailmap.html</a> for examples of the use of <code>keytool</code></dl>
</dl>
<h2>Changes</h2>
<p>The command interface for keytool changed in Java SE 6. </p>
<p> <code>keytool</code> no longer displays password input when entered by users. Since password input can no longer be viewed when entered, users will be prompted to re-enter passwords any time a password is being set or changed (for example, when setting the initial keystore password, or when changing a key password). </p>
<p> Some commands have simply been renamed, and other commands deemed obsolete are no longer listed in this document. All previous commands (both renamed and obsolete) are still supported in this release and will continue to be supported in future releases. The following summarizes all of the changes made to the keytool command interface: </p>
<p> Renamed commands: </p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd><i>-export</i>, renamed to <i>-exportcert</i></p>
<dt>o</p>
<dd><i>-genkey</i>, renamed to <i>-genkeypair</i></p>
<dt>o</p>
<dd><i>-import</i>, renamed to <i>-importcert</i></dl>
</dl>
<p> Commands deemed obsolete and no longer documented: </p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd><i>-keyclone</i> @ <a rel="nofollow" href="http://java.sun.com/j2se/1.5.0/docs/tooldocs/solaris/keytool.html#keycloneCmd">http://java.sun.com/j2se/1.5.0/docs/tooldocs/solaris/keytool.html#keycloneCmd</a></p>
<dt>o</p>
<dd><i>-identitydb</i> @ <a rel="nofollow" href="http://java.sun.com/j2se/1.5.0/docs/tooldocs/solaris/keytool.html#identitydbCmd">http://java.sun.com/j2se/1.5.0/docs/tooldocs/solaris/keytool.html#identitydbCmd</a></p>
<dt>o</p>
<dd><i>-selfcert</i> @ <a rel="nofollow" href="http://java.sun.com/j2se/1.5.0/docs/tooldocs/solaris/keytool.html#selfcertCmd">http://java.sun.com/j2se/1.5.0/docs/tooldocs/solaris/keytool.html#selfcertCmd</a></dl>
</dl>
<p>&nbsp;<wbr></p>
