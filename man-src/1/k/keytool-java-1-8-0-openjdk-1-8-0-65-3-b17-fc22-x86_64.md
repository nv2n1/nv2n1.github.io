---
title: "keytool-java-1-8-0-openjdk-1-8-0-65-3-b17-fc22-x86_64(1)"
name: "keytool-java-1-8-0-openjdk-1-8-0-65-3-b17-fc22-x86_64"
section: "1"
letter: "k"
url: "/docs/linux/man/1-keytool-java-1-8-0-openjdk-1-8-0-65-3-b17-fc22-x86_64/"
description: "keytool – Manages a keystore (database) of cryptographic keys, X.509 certificate chains, and trusted certificates."
---

<p>keytool &#8211; Manages a keystore (database) of cryptographic keys, X.509 certificate chains, and trusted certificates.</p>
<h2>Synopsis</h2>
<pre><code>keytool</code> [<i>commands</i>]</pre>
<dl>
<dt><i>commands</i></p>
<dd>See Commands. These commands are categorized by task as follows:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Create or Add Data to the Keystore</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>-gencert</p>
<dt>&bull;</p>
<dd>-genkeypair</p>
<dt>&bull;</p>
<dd>-genseckey</p>
<dt>&bull;</p>
<dd>-importcert</p>
<dt>&bull;</p>
<dd>-importpassword</dl>
</dl>
<dt>&bull;</p>
<dd>Import Contents From Another Keystore</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>-importkeystore</dl>
</dl>
<dt>&bull;</p>
<dd>Generate Certificate Request</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>-certreq</dl>
</dl>
<dt>&bull;</p>
<dd>Export Data</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>-exportcert</dl>
</dl>
<dt>&bull;</p>
<dd>Display Data</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>-list</p>
<dt>&bull;</p>
<dd>-printcert</p>
<dt>&bull;</p>
<dd>-printcertreq</p>
<dt>&bull;</p>
<dd>-printcrl</dl>
</dl>
<dt>&bull;</p>
<dd>Manage the Keystore</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>-storepasswd</p>
<dt>&bull;</p>
<dd>-keypasswd</p>
<dt>&bull;</p>
<dd>-delete</p>
<dt>&bull;</p>
<dd>-changealias</dl>
</dl>
<dt>&bull;</p>
<dd>Get Help</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>-help</dl>
</dl>
</dl>
</dl>
</dl>
<h2>Description</h2>
<p>The <code>keytool</code> command is a key and certificate management utility. It enables users to administer their own public/private key pairs and associated certificates for use in self-authentication (where the user authenticates himself or herself to other users and services) or data integrity and authentication services, using digital signatures. The <code>keytool</code> command also enables users to cache the public keys (in the form of certificates) of their communicating peers. </p>
<p> A certificate is a digitally signed statement from one entity (person, company, and so on.), that says that the public key (and some other information) of some other entity has a particular value. (See Certificate.) When data is digitally signed, the signature can be verified to check the data integrity and authenticity. Integrity means that the data has not been modified or tampered with, and authenticity means the data comes from whoever claims to have created and signed it. </p>
<p> The <code>keytool</code> command also enables users to administer secret keys and passphrases used in symmetric encryption and decryption (DES). </p>
<p> The <code>keytool</code> command stores the keys and certificates in a keystore. See KeyStore aliases.</p>
<h2>Command And Option Notes</h2>
<p>See Commands for a listing and description of the various commands.</p>
<dl>
<dt>&bull;</p>
<dd>All command and option names are preceded by a minus sign (-).</p>
<dt>&bull;</p>
<dd>The options for each command can be provided in any order.</p>
<dt>&bull;</p>
<dd>All items not italicized or in braces or brackets are required to appear as is.</p>
<dt>&bull;</p>
<dd>Braces surrounding an option signify that a default value will be used when the option is not specified on the command line. See Option Defaults. Braces are also used around the <code>-v</code>, <code>-rfc</code>, and <code>-J</code> options, which only have meaning when they appear on the command line. They do not have any default values other than not existing.</p>
<dt>&bull;</p>
<dd>Brackets surrounding an option signify that the user is prompted for the values when the option is not specified on the command line. For the <code>-keypass</code> option, if you do not specify the option on the command line, then the <code>keytool</code> command first attempts to use the keystore password to recover the private/secret key. If this attempt fails, then the <code>keytool</code> command prompts you for the private/secret key password.</p>
<dt>&bull;</p>
<dd>Items in italics (option values) represent the actual values that must be supplied. For example, here is the format of the <code>-printcert</code> command: </p>
<pre><code>keytool -printcert {-file </code><i>cert_file</i>} {-v}</pre>
<p>When you specify a <code>-printcert</code> command, replace <i>cert_file</i> with the actual file name, as follows: <code>keytool -printcert -file VScert.cer</code></p>
<dt>&bull;</p>
<dd>Option values must be put in quotation marks when they contain a blank (space).</p>
<dt>&bull;</p>
<dd>The <code>-help</code> option is the default. The <code>keytool</code> command is the same as <code>keytool -help</code>.</dl>
<h2>Option Defaults</h2>
<p>The following examples show the defaults for various option values. </p>
<pre><code>-alias &quot;mykey&quot;</code></pre>
<pre><code>-keyalg</code></pre>
<pre><code> &quot;DSA&quot; (when using -genkeypair)</code></pre>
<pre><code> &quot;DES&quot; (when using -genseckey)</code></pre>
<pre><code>-keysize</code></pre>
<pre><code> 2048 (when using -genkeypair and -keyalg is &quot;RSA&quot;)</code></pre>
<pre><code> 1024 (when using -genkeypair and -keyalg is &quot;DSA&quot;)</code></pre>
<pre><code> 256 (when using -genkeypair and -keyalg is &quot;EC&quot;)</code></pre>
<pre><code> 56 (when using -genseckey and -keyalg is &quot;DES&quot;)</code></pre>
<pre><code> 168 (when using -genseckey and -keyalg is &quot;DESede&quot;)</code></pre>
<pre><code>-validity 90</code></pre>
<pre><code>-keystore &lt;the file named .keystore in the user's home directory&gt;</code></pre>
<pre><code>-storetype &lt;the value of the &quot;keystore.type&quot; property in the</code></pre>
<pre><code> security properties file, which is returned by the static</code></pre>
<pre><code> getDefaultType method in java.security.KeyStore&gt;</code></pre>
<pre><code>-file</code></pre>
<pre><code> stdin (if reading)</code></pre>
<pre><code> stdout (if writing)</code></pre>
<pre><code>-protected false</code></pre>
<p>In generating a public/private key pair, the signature algorithm (<code>-sigalg</code> option) is derived from the algorithm of the underlying private key:</p>
<dl>
<dt>&bull;</p>
<dd>If the underlying private key is of type DSA, then the <code>-sigalg</code> option defaults to SHA1withDSA.</p>
<dt>&bull;</p>
<dd>If the underlying private key is of type RSA, then the <code>-sigalg</code> option defaults to SHA256withRSA.</p>
<dt>&bull;</p>
<dd>If the underlying private key is of type EC, then the <code>-sigalg</code> option defaults to SHA256withECDSA.</dl>
<p> For a full list of <code>-keyalg</code> and <code>-sigalg</code> arguments, see Java Cryptography Architecture (JCA) Reference Guide at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html#AppA">http://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html#AppA</a></p>
<h2>Common Options</h2>
<p>The <code>-v</code> option can appear for all commands except <code>-help</code>. When the <code>-v</code> option appears, it signifies verbose mode, which means that more information is provided in the output. </p>
<p> There is also a <code>-Jjavaoption</code> argument that can appear for any command. When the <code>-Jjavaoption</code> appears, the specified <code>javaoption</code> string is passed directly to the Java interpreter. This option does not contain any spaces. It is useful for adjusting the execution environment or memory usage. For a list of possible interpreter options, type <code>java -h</code> or <code>java -X</code> at the command line. </p>
<p> These options can appear for all commands operating on a keystore:</p>
<dl>
<dt>-storetype <i>storetype</i></p>
<dd>This qualifier specifies the type of keystore to be instantiated.</p>
<dt>-keystore <i>keystore</i></p>
<dd>The keystore location. </p>
<p> If the JKS <code>storetype</code> is used and a keystore file does not yet exist, then certain <code>keytool</code> commands can result in a new keystore file being created. For example, if <code>keytool -genkeypair</code> is called and the <code>-keystore</code> option is not specified, the default keystore file named <code>.keystore</code> in the user&#8217;s home directory is created when it does not already exist. Similarly, if the <code>-keystore ks_file</code> option is specified but ks_file does not exist, then it is created. For more information on the JKS <code>storetype</code>, see the <i>KeyStore Implementation</i> section in KeyStore aliases. </p>
<p> Note that the input stream from the <code>-keystore</code> option is passed to the <code>KeyStore.load</code> method. If <code>NONE</code> is specified as the URL, then a null stream is passed to the <code>KeyStore.load</code> method. <code>NONE</code> should be specified if the keystore is not file-based. For example, when it resides on a hardware token device.</p>
<dt>-storepass[:<i>env</i>| :<i>file</i>] argument</p>
<dd>The password that is used to protect the integrity of the keystore. </p>
<p> If the modifier <code>env</code> or <code>file</code> is not specified, then the password has the <code>value</code> argument, which must be at least 6 characters long. Otherwise, the password is retrieved as follows:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>env</code>: Retrieve the password from the environment variable named <code>argument</code>.</p>
<dt>&bull;</p>
<dd><code>file</code>: Retrieve the password from the file named argument.</dl>
</dl>
<p> <i>Note:</i> All other options that require passwords, such as <code>-keypass</code>, <code>-srckeypass</code>, &#8211;<code>destkeypass</code>, <code>-srcstorepass</code>, and <code>-deststorepass</code>, accept the <i>env</i> and <i>file</i> modifiers. Remember to separate the password option and the modifier with a colon (:). </p>
<p> The password must be provided to all commands that access the keystore contents. For such commands, when the <code>-storepass</code> option is not provided at the command line, the user is prompted for it. </p>
<p> When retrieving information from the keystore, the password is optional. If no password is specified, then the integrity of the retrieved information cannot be verified and a warning is displayed.</p>
<dt>-providerName <i>provider_name</i></p>
<dd>Used to identify a cryptographic service provider&#8217;s name when listed in the security properties file.</p>
<dt>-providerClass <i>provider_class_name</i></p>
<dd>Used to specify the name of a cryptographic service provider&#8217;s master class file when the service provider is not listed in the security properties file.</p>
<dt>-providerArg <i>provider_arg</i></p>
<dd>Used with the <code>-providerClass</code> option to represent an optional string input argument for the constructor of <code>provider_class_name</code>.</p>
<dt>-protected</p>
<dd>Either <code>true</code> or <code>false</code>. This value should be specified as <code>true</code> when a password must be specified by way of a protected authentication path such as a dedicated PIN reader.Because there are two keystores involved in the <code>-importkeystore</code> command, the following two options <code>-srcprotected</code> and &#8211;<code>destprotected</code> are provided for the source keystore and the destination keystore respectively.</p>
<dt>-ext <i>{name{:critical} {=value}}</i></p>
<dd>Denotes an X.509 certificate extension. The option can be used in <code>-genkeypair</code> and <code>-gencert</code> to embed extensions into the certificate generated, or in <code>-certreq</code> to show what extensions are requested in the certificate request. The option can appear multiple times. The <code>name</code> argument can be a supported extension name (see Named Extensions) or an arbitrary OID number. The <code>value</code> argument, when provided, denotes the argument for the extension. When <i>value</i> is omitted, that means that the default value of the extension or the extension requires no argument. The <code>:critical</code> modifier, when provided, means the extension&#8217;s <code>isCritical</code> attribute is <code>true</code>; otherwise, it is <code>false</code>. You can use <code>:c</code> in place of <code>:critical</code>.</dl>
<h2>Named Extensions</h2>
<p>The <code>keytool</code> command supports these named extensions. The names are not case-sensitive).</p>
<dl>
<dt>BC or BasicContraints</p>
<dd><i>Values</i>: The full form is: <code>ca:{true|false}[,pathlen:&lt;len&gt;]</code> or <code>&lt;len&gt;</code>, which is short for <code>ca:true,pathlen:&lt;len&gt;</code>. When &lt;<code>len</code>&gt; is omitted, you have <code>ca:true</code>.</p>
<dt>KU or KeyUsage</p>
<dd><i>Values</i>: <code>usage</code>(,<code>usage</code>)*, where <i>usage</i> can be one of <code>digitalSignature</code>, <code>nonRepudiation</code> (contentCommitment), <code>keyEncipherment</code>, <code>dataEncipherment</code>, <code>keyAgreement</code>, <code>keyCertSign</code>, <code>cRLSign</code>, <code>encipherOnly</code>, <code>decipherOnly</code>. The <i>usage</i> argument can be abbreviated with the first few letters (<code>dig</code> for <code>digitalSignature</code>) or in camel-case style (<code>dS</code> for <code>digitalSignature</code> or <code>cRLS</code> for <code>cRLSign</code>), as long as no ambiguity is found. The <code>usage</code> values are case-sensitive.</p>
<dt>EKU or ExtendedKeyUsage</p>
<dd><i>Values</i>: <code>usage</code>(,<code>usage</code>)*, where <i>usage</i> can be one of <code>anyExtendedKeyUsage</code>, <code>serverAuth</code>, <code>clientAuth</code>, <code>codeSigning</code>, <code>emailProtection</code>, <code>timeStamping</code>, <code>OCSPSigning</code>, or any <i>OID string</i>. The <i>usage</i> argument can be abbreviated with the first few letters or in camel-case style, as long as no ambiguity is found. The <code>usage</code> values are case-sensitive.</p>
<dt>SAN or SubjectAlternativeName</p>
<dd><i>Values</i>: <code>type</code>:<code>value</code>(,t<code>ype:value</code>)*, where <code>type</code> can be <code>EMAIL</code>, <code>URI</code>, <code>DNS</code>, <code>IP</code>, or <code>OID</code>. The <code>value</code> argument is the string format value for the <code>type</code>.</p>
<dt>IAN or IssuerAlternativeName</p>
<dd><i>Values</i>: Same as <code>SubjectAlternativeName</code>.</p>
<dt>SIA or SubjectInfoAccess</p>
<dd><i>Values</i>: <code>method</code>:<code>location-type</code>:<code>location-value</code> (,<code>method:location-type</code>:<code>location-value</code>)*, where <code>method</code> can be <code>timeStamping</code>, <code>caRepository</code> or any OID. The <code>location-type</code> and <code>location-value</code> arguments can be any <code>type</code>:<code>value</code> supported by the <code>SubjectAlternativeName</code> extension.</p>
<dt>AIA or AuthorityInfoAccess</p>
<dd><i>Values</i>: Same as <code>SubjectInfoAccess</code>. The <code>method</code> argument can be <code>ocsp</code>,<code>caIssuers</code>, or any OID.</dl>
<p> When <code>name</code> is OID, the value is the hexadecimal dumped DER encoding of the <code>extnValue</code> for the extension excluding the OCTET STRING type and length bytes. Any extra character other than standard hexadecimal numbers (0-9, a-f, A-F) are ignored in the HEX string. Therefore, both 01:02:03:04 and 01020304 are accepted as identical values. When there is no value, the extension has an empty value field. </p>
<p> A special name <code>honored</code>, used in <code>-gencert</code> only, denotes how the extensions included in the certificate request should be honored. The value for this name is a comma separated list of <code>all</code> (all requested extensions are honored), <code>name{:[critical|non-critical]}</code> (the named extension is honored, but using a different <code>isCritical</code> attribute) and <code>-name</code> (used with <code>all</code>, denotes an exception). Requested extensions are not honored by default. </p>
<p> If, besides the<code>-ext honored</code> option, another named or OID <code>-ext</code> option is provided, this extension is added to those already honored. However, if this name (or OID) also appears in the honored value, then its value and criticality overrides the one in the request. </p>
<p> The <code>subjectKeyIdentifier</code> extension is always created. For non-self-signed certificates, the <code>authorityKeyIdentifier</code> is created. </p>
<p> <i>Note:</i> Users should be aware that some combinations of extensions (and other certificate fields) may not conform to the Internet standard. See Certificate Conformance Warning.</p>
<h2>Commands</h2>
<dl>
<dt>-gencert</p>
<dd>
<pre><code>{-rfc} {-infile </code><i>infile</i>} {-outfile <i>outfile</i>} {-alias <i>alias</i>} {-sigalg <i>sigalg</i>}</pre>
<pre><code>{-dname </code><i>dname</i>} {-startdate <i>startdate</i> {-ext <i>ext</i>}* {-validity <i>valDays</i>}</pre>
<pre><code>[-keypass </code><i>keypass</i>] {-keystore <i>keystore</i>} [-storepass <i>storepass</i>]</pre>
<pre><code>{-storetype </code><i>storetype</i>} {-providername <i>provider_name</i>}</pre>
<pre><code>{-providerClass </code><i>provider_class_name</i> {-providerArg <i>provider_arg</i>}}</pre>
<pre><code>{-v} {-protected} {-Jjavaoption}</code></pre>
<p>Generates a certificate as a response to a certificate request file (which can be created by the <code>keytool</code><code>-certreq</code> command). The command reads the request from <i>infile</i> (if omitted, from the standard input), signs it using alias&#8217;s private key, and outputs the X.509 certificate into <i>outfile</i> (if omitted, to the standard output). When<code>-rfc</code> is specified, the output format is Base64-encoded PEM; otherwise, a binary DER is created. </p>
<p> The <code>sigalg</code> value specifies the algorithm that should be used to sign the certificate. The <code>startdate</code> argument is the start time and date that the certificate is valid. The <code>valDays</code> argument tells the number of days for which the certificate should be considered valid. </p>
<p> When <code>dname</code> is provided, it is used as the subject of the generated certificate. Otherwise, the one from the certificate request is used. </p>
<p> The <code>ext</code> value shows what X.509 extensions will be embedded in the certificate. Read Common Options for the grammar of <code>-ext</code>. </p>
<p> The <code>-gencert</code> option enables you to create certificate chains. The following example creates a certificate, <code>e1</code>, that contains three certificates in its certificate chain. </p>
<p> The following commands creates four key pairs named <code>ca</code>, <code>ca1</code>, <code>ca2</code>, and <code>e1</code>: </p>
<pre><code>keytool -alias ca -dname CN=CA -genkeypair</code></pre>
<pre><code>keytool -alias ca1 -dname CN=CA -genkeypair</code></pre>
<pre><code>keytool -alias ca2 -dname CN=CA -genkeypair</code></pre>
<pre><code>keytool -alias e1 -dname CN=E1 -genkeypair</code></pre>
<p>The following two commands create a chain of signed certificates; <code>ca</code> signs <code>ca1</code> and <code>ca1</code> signs <code>ca2</code>, all of which are self-issued: </p>
<pre><code>keytool -alias ca1 -certreq |</code></pre>
<pre><code> keytool -alias ca -gencert -ext san=dns:ca1 |</code></pre>
<pre><code> keytool -alias ca1 -importcert</code></pre>
<pre><code>keytool -alias ca2 -certreq |</code></pre>
<pre><code> $KT -alias ca1 -gencert -ext san=dns:ca2 |</code></pre>
<pre><code> $KT -alias ca2 -importcert</code></pre>
<p>The following command creates the certificate <code>e1</code> and stores it in the file <code>e1.cert</code>, which is signed by <code>ca2</code>. As a result, <code>e1</code> should contain <code>ca</code>, <code>ca1</code>, and <code>ca2</code> in its certificate chain: </p>
<pre><code>keytool -alias e1 -certreq | keytool -alias ca2 -gencert &gt; e1.cert</code></pre>
<dt>-genkeypair</p>
<dd>
<pre><code>{-alias </code><i>alias</i>} {-keyalg <i>keyalg</i>} {-keysize <i>keysize</i>} {-sigalg <i>sigalg</i>}</pre>
<pre><code>[-dname </code><i>dname</i>] [-keypass <i>keypass</i>] {-startdate <i>value</i>} {-ext <i>ext</i>}*</pre>
<pre><code>{-validity </code><i>valDays</i>} {-storetype <i>storetype</i>} {-keystore <i>keystore</i>}</pre>
<pre><code>[-storepass </code><i>storepass</i>]</pre>
<pre><code>{-providerClass </code><i>provider_class_name</i> {-providerArg <i>provider_arg</i>}}</pre>
<pre><code>{-v} {-protected} {-Jjavaoption}</code></pre>
<p>Generates a key pair (a public key and associated private key). Wraps the public key into an X.509 v3 self-signed certificate, which is stored as a single-element certificate chain. This certificate chain and the private key are stored in a new keystore entry identified by alias. </p>
<p> The <code>keyalg</code> value specifies the algorithm to be used to generate the key pair, and the <code>keysize</code> value specifies the size of each key to be generated. The <code>sigalg</code> value specifies the algorithm that should be used to sign the self-signed certificate. This algorithm must be compatible with the <code>keyalg</code> value. </p>
<p> The <code>dname</code> value specifies the X.500 Distinguished Name to be associated with the value of <code>alias</code>, and is used as the issuer and subject fields in the self-signed certificate. If no distinguished name is provided at the command line, then the user is prompted for one. </p>
<p> The value of <code>keypass</code> is a password used to protect the private key of the generated key pair. If no password is provided, then the user is prompted for it. If you press <i>the Return key</i> at the prompt, then the key password is set to the same password as the keystore password. The <code>keypass</code> value must be at least 6 characters. </p>
<p> The value of <code>startdate</code> specifies the issue time of the certificate, also known as the &quot;Not Before&quot; value of the X.509 certificate&#8217;s Validity field. </p>
<p> The option value can be set in one of these two forms: </p>
<p> <code>([+-]nnn[ymdHMS])+</code> </p>
<p> <code>[yyyy/mm/dd] [HH:MM:SS]</code> </p>
<p> With the first form, the issue time is shifted by the specified value from the current time. The value is a concatenation of a sequence of subvalues. Inside each subvalue, the plus sign (+) means shift forward, and the minus sign (-) means shift backward. The time to be shifted is <code>nnn</code> units of years, months, days, hours, minutes, or seconds (denoted by a single character of <code>y</code>, <code>m</code>, <code>d</code>, <code>H</code>, <code>M</code>, or <code>S</code> respectively). The exact value of the issue time is calculated using the <code>java.util.GregorianCalendar.add(int field, int amount)</code> method on each subvalue, from left to right. For example, by specifying, the issue time will be: </p>
<pre><code>Calendar c = new GregorianCalendar();</code></pre>
<pre><code>c.add(Calendar.YEAR, -1);</code></pre>
<pre><code>c.add(Calendar.MONTH, 1);</code></pre>
<pre><code>c.add(Calendar.DATE, -1);</code></pre>
<pre><code>return c.getTime()</code></pre>
<p>With the second form, the user sets the exact issue time in two parts, year/month/day and hour:minute:second (using the local time zone). The user can provide only one part, which means the other part is the same as the current date (or time). The user must provide the exact number of digits as shown in the format definition (padding with 0 when shorter). When both the date and time are provided, there is one (and only one) space character between the two parts. The hour should always be provided in 24 hour format. </p>
<p> When the option is not provided, the start date is the current time. The option can be provided at most once. </p>
<p> The value of <code>valDays</code> specifies the number of days (starting at the date specified by <code>-startdate</code>, or the current date when <code>-startdate</code> is not specified) for which the certificate should be considered valid. </p>
<p> This command was named <code>-genkey</code> in earlier releases. The old name is still supported in this release. The new name, <code>-genkeypair</code>, is preferred going forward.</p>
<dt>-genseckey</p>
<dd>
<pre><code>{-alias </code><i>alias</i>} {-keyalg <i>keyalg</i>} {-keysize <i>keysize</i>} [-keypass <i>keypass</i>]</pre>
<pre><code>{-storetype </code><i>storetype</i>} {-keystore <i>keystore</i>} [-storepass <i>storepass</i>]</pre>
<pre><code>{-providerClass </code><i>provider_class_name</i> {-providerArg <i>provider_arg</i>}} {-v}</pre>
<pre><code>{-protected} {-Jjavaoption}</code></pre>
<p>Generates a secret key and stores it in a new <code>KeyStore.SecretKeyEntry</code> identified by <code>alias</code>. </p>
<p> The value of <code>keyalg</code> specifies the algorithm to be used to generate the secret key, and the value of <code>keysize</code> specifies the size of the key to be generated. The <code>keypass</code> value is a password that protects the secret key. If no password is provided, then the user is prompted for it. If you press the Return key at the prompt, then the key password is set to the same password that is used for the <code>keystore</code>. The <code>keypass</code> value must be at least 6 characters.</p>
<dt>-importcert</p>
<dd>
<pre><code>{-alias </code><i>alias</i>} {-file <i>cert_file</i>} [-keypass <i>keypass</i>] {-noprompt} {-trustcacerts}</pre>
<pre><code>{-storetype </code><i>storetype</i>} {-keystore <i>keystore</i>} [-storepass <i>storepass</i>]</pre>
<pre><code>{-providerName </code><i>provider_name</i>}</pre>
<pre><code>{-providerClass </code><i>provider_class_name</i> {-providerArg <i>provider_arg</i>}}</pre>
<pre><code>{-v} {-protected} {-Jjavaoption}</code></pre>
<p>Reads the certificate or certificate chain (where the latter is supplied in a PKCS#7 formatted reply or a sequence of X.509 certificates) from the file <code>cert_file</code>, and stores it in the <code>keystore</code> entry identified by <code>alias</code>. If no file is specified, then the certificate or certificate chain is read from <code>stdin</code>. </p>
<p> The <code>keytool</code> command can import X.509 v1, v2, and v3 certificates, and PKCS#7 formatted certificate chains consisting of certificates of that type. The data to be imported must be provided either in binary encoding format or in printable encoding format (also known as Base64 encoding) as defined by the Internet RFC 1421 standard. In the latter case, the encoding must be bounded at the beginning by a string that starts with <code>&#8211;</code><code>&#8212;-BEGIN</code>, and bounded at the end by a string that starts with <code>&#8212;&#8211;END</code>. </p>
<p> You import a certificate for two reasons: To add it to the list of trusted certificates, and to import a certificate reply received from a certificate authority (CA) as the result of submitting a Certificate Signing Request to that CA (see the <code>-certreq</code> option in Commands). </p>
<p> Which type of import is intended is indicated by the value of the <code>-alias</code> option. If the alias does not point to a key entry, then the <code>keytool</code> command assumes you are adding a trusted certificate entry. In this case, the alias should not already exist in the keystore. If the alias does already exist, then the <code>keytool</code> command outputs an error because there is already a trusted certificate for that alias, and does not import the certificate. If the alias points to a key entry, then the <code>keytool</code> command assumes you are importing a certificate reply.</p>
<dt>-importpassword</p>
<dd>
<pre><code>{-alias </code><i>alias</i>} [-keypass <i>keypass</i>] {-storetype <i>storetype</i>} {-keystore <i>keystore</i>}</pre>
<pre><code>[-storepass </code><i>storepass</i>]</pre>
<pre><code>{-providerClass </code><i>provider_class_name</i> {-providerArg <i>provider_arg</i>}}</pre>
<pre><code>{-v} {-protected} {-Jjavaoption}</code></pre>
<p>Imports a passphrase and stores it in a new <code>KeyStore.SecretKeyEntry</code> identified by <code>alias</code>. The passphrase may be supplied via the standard input stream; otherwise the user is prompted for it. <code>keypass</code> is a password used to protect the imported passphrase. If no password is provided, the user is prompted for it. If you press the Return key at the prompt, the key password is set to the same password as that used for the <code>keystore</code>. <code>keypass</code> must be at least 6 characters long.</p>
<dt>-importkeystore</p>
<dd>
<pre><code>{-srcstoretype </code><i>srcstoretype</i>} {-deststoretype <i>deststoretype</i>}</pre>
<pre><code>[-srcstorepass </code><i>srcstorepass</i>] [-deststorepass <i>deststorepass</i>] {-srcprotected}</pre>
<pre><code>{-destprotected} </code></pre>
<pre><code>{-srcalias </code><i>srcalias</i> {-destalias <i>destalias</i>} [-srckeypass <i>srckeypass</i>]} </pre>
<pre><code>[-destkeypass </code><i>destkeypass</i>] {-noprompt}</pre>
<pre><code>{-srcProviderName </code><i>src_provider_name</i>} {-destProviderName <i>dest_provider_name</i>}</pre>
<pre><code>{-providerClass </code><i>provider_class_name</i> {-providerArg <i>provider_arg</i>}} {-v}</pre>
<pre><code>{-protected} {-Jjavaoption}</code></pre>
<p>Imports a single entry or all entries from a source keystore to a destination keystore. </p>
<p> When the <code>-srcalias</code> option is provided, the command imports the single entry identified by the alias to the destination keystore. If a destination alias is not provided with <code>destalias</code>, then <code>srcalias</code> is used as the destination alias. If the source entry is protected by a password, then <code>srckeypass</code> is used to recover the entry. If <i>srckeypass</i> is not provided, then the <code>keytool</code> command attempts to use <code>srcstorepass</code> to recover the entry. If <code>srcstorepass</code> is either not provided or is incorrect, then the user is prompted for a password. The destination entry is protected with <code>destkeypass</code>. If <code>destkeypass</code> is not provided, then the destination entry is protected with the source entry password. For example, most third-party tools require <code>storepass</code> and <code>keypass</code> in a PKCS #12 keystore to be the same. In order to create a PKCS #12 keystore for these tools, always specify a <code>-destkeypass</code> to be the same as <code>-deststorepass</code>. </p>
<p> If the <code>-srcalias</code> option is not provided, then all entries in the source keystore are imported into the destination keystore. Each destination entry is stored under the alias from the source entry. If the source entry is protected by a password, then <code>srcstorepass</code> is used to recover the entry. If <code>srcstorepass</code> is either not provided or is incorrect, then the user is prompted for a password. If a source keystore entry type is not supported in the destination keystore, or if an error occurs while storing an entry into the destination keystore, then the user is prompted whether to skip the entry and continue or to quit. The destination entry is protected with the source entry password. </p>
<p> If the destination alias already exists in the destination keystore, then the user is prompted to either overwrite the entry or to create a new entry under a different alias name. </p>
<p> If the <code>-noprompt</code> option is provided, then the user is not prompted for a new destination alias. Existing entries are overwritten with the destination alias name. Entries that cannot be imported are skipped and a warning is displayed.</p>
<dt>-printcertreq</p>
<dd>
<pre><code>{-file </code><i>file</i>}</pre>
<p>Prints the content of a PKCS #10 format certificate request, which can be generated by the <code>keytool</code><code>-certreq</code> command. The command reads the request from file. If there is no file, then the request is read from the standard input.</p>
<dt>-certreq</p>
<dd>
<pre><code>{-alias </code><i>alias</i>} {-dname <i>dname</i>} {-sigalg <i>sigalg</i>} {-file <i>certreq_file</i>}</pre>
<pre><code>[-keypass </code><i>keypass</i>] {-storetype <i>storetype</i>} {-keystore <i>keystore</i>}</pre>
<pre><code>[-storepass </code><i>storepass</i>] {-providerName <i>provider_name</i>}</pre>
<pre><code>{-providerClass </code><i>provider_class_name</i> {-providerArg <i>provider_arg</i>}}</pre>
<pre><code>{-v} {-protected} {-Jjavaoption}</code></pre>
<p>Generates a Certificate Signing Request (CSR) using the PKCS #10 format. </p>
<p> A CSR is intended to be sent to a certificate authority (CA). The CA authenticates the certificate requestor (usually off-line) and will return a certificate or certificate chain, used to replace the existing certificate chain (which initially consists of a self-signed certificate) in the keystore. </p>
<p> The private key associated with alias is used to create the PKCS #10 certificate request. To access the private key, the correct password must be provided. If <code>keypass</code> is not provided at the command line and is different from the password used to protect the integrity of the keystore, then the user is prompted for it. If <code>dname</code> is provided, then it is used as the subject in the CSR. Otherwise, the X.500 Distinguished Name associated with alias is used. </p>
<p> The <code>sigalg</code> value specifies the algorithm that should be used to sign the CSR. </p>
<p> The CSR is stored in the file certreq_file. If no file is specified, then the CSR is output to <code>stdout</code>. </p>
<p> Use the <code>importcert</code> command to import the response from the CA.</p>
<dt>-exportcert</p>
<dd>
<pre><code>{-alias </code><i>alias</i>} {-file <i>cert_file</i>} {-storetype <i>storetype</i>} {-keystore <i>keystore</i>}</pre>
<pre><code>[-storepass </code><i>storepass</i>] {-providerName <i>provider_name</i>}</pre>
<pre><code>{-providerClass </code><i>provider_class_name</i> {-providerArg <i>provider_arg</i>}}</pre>
<pre><code>{-rfc} {-v} {-protected} {-Jjavaoption}</code></pre>
<p>Reads from the keystore the certificate associated with <i>alias</i> and stores it in the cert_file file. When no file is specified, the certificate is output to <code>stdout</code>. </p>
<p> The certificate is by default output in binary encoding. If the <code>-rfc</code> option is specified, then the output in the printable encoding format defined by the Internet RFC 1421 Certificate Encoding Standard. </p>
<p> If <code>alias</code> refers to a trusted certificate, then that certificate is output. Otherwise, <code>alias</code> refers to a key entry with an associated certificate chain. In that case, the first certificate in the chain is returned. This certificate authenticates the public key of the entity addressed by <code>alias</code>. </p>
<p> This command was named <code>-export</code> in earlier releases. The old name is still supported in this release. The new name, <code>-exportcert</code>, is preferred going forward.</p>
<dt>-list</p>
<dd>
<pre><code>{-alias </code><i>alias</i>} {-storetype <i>storetype</i>} {-keystore <i>keystore</i>} [-storepass <i>storepass</i>]</pre>
<pre><code>{-providerName </code><i>provider_name</i>}</pre>
<pre><code>{-providerClass </code><i>provider_class_name</i> {-providerArg <i>provider_arg</i>}}</pre>
<pre><code>{-v | -rfc} {-protected} {-Jjavaoption}</code></pre>
<p>Prints to <code>stdout</code> the contents of the keystore entry identified by <code>alias</code>. If no <code>alias</code> is specified, then the contents of the entire keystore are printed. </p>
<p> This command by default prints the SHA1 fingerprint of a certificate. If the <code>-v</code> option is specified, then the certificate is printed in human-readable format, with additional information such as the owner, issuer, serial number, and any extensions. If the <code>-rfc</code> option is specified, then the certificate contents are printed using the printable encoding format, as defined by the Internet RFC 1421 Certificate Encoding Standard. </p>
<p> You cannot specify both <code>-v</code> and <code>-rfc</code>.</p>
<dt>-printcert</p>
<dd>
<pre><code>{-file </code><i>cert_file</i> | -sslserver <i>host</i>[:<i>port</i>]} {-jarfile <i>JAR_file</i> {-rfc} {-v}</pre>
<pre><code>{-Jjavaoption}</code></pre>
<p>Reads the certificate from the file cert_file, the SSL server located at host:port, or the signed JAR file <code>JAR_file</code> (with the <code>-jarfile</code> option and prints its contents in a human-readable format. When no port is specified, the standard HTTPS port 443 is assumed. Note that <code>-sslserver</code> and -file options cannot be provided at the same time. Otherwise, an error is reported. If neither option is specified, then the certificate is read from <code>stdin</code>. </p>
<p> When<code>-rfc</code> is specified, the <code>keytool</code> command prints the certificate in PEM mode as defined by the Internet RFC 1421 Certificate Encoding standard. See Internet RFC 1421 Certificate Encoding Standard. </p>
<p> If the certificate is read from a file or <code>stdin</code>, then it might be either binary encoded or in printable encoding format, as defined by the RFC 1421 Certificate Encoding standard. </p>
<p> If the SSL server is behind a firewall, then the <code>-J-Dhttps.proxyHost=proxyhost</code> and <code>-J-Dhttps.proxyPort=proxyport</code> options can be specified on the command line for proxy tunneling. See Java Secure Socket Extension (JSSE) Reference Guide at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/security/jsse/JSSERefGuide.html">http://docs.oracle.com/javase/8/docs/technotes/guides/security/jsse/JSSERefGuide.html</a> </p>
<p> <i>Note:</i> This option can be used independently of a keystore.</p>
<dt>-printcrl</p>
<dd>
<pre><code>-file </code><i>crl_</i> {-v}</pre>
<p>Reads the Certificate Revocation List (CRL) from the file <code>crl_</code>. A CRL is a list of digital certificates that were revoked by the CA that issued them. The CA generates the <code>crl_</code> file. </p>
<p> <i>Note:</i> This option can be used independently of a keystore.</p>
<dt>-storepasswd</p>
<dd>
<pre><code>[-new </code><i>new_storepass</i>] {-storetype <i>storetype</i>} {-keystore <i>keystore</i>}</pre>
<pre><code>[-storepass </code><i>storepass</i>] {-providerName <i>provider_name</i>}</pre>
<pre><code>{-providerClass </code><i>provider_class_name</i> {-providerArg <i>provider_arg</i>}}</pre>
<pre><code>{-v} {-Jjavaoption}</code></pre>
<p>Changes the password used to protect the integrity of the keystore contents. The new password is <code>new_storepass</code>, which must be at least 6 characters.</p>
<dt>-keypasswd</p>
<dd>
<pre><code>{-alias </code><i>alias</i>} [-keypass <i>old_keypass</i>] [-new <i>new_keypass</i>] {-storetype <i>storetype</i>}</pre>
<pre><code>{-keystore </code><i>keystore</i>} [-storepass <i>storepass</i>] {-providerName <i>provider_name</i>}</pre>
<pre><code>{-providerClass </code><i>provider_class_name</i> {-providerArg <i>provider_arg</i>}} {-v}</pre>
<pre><code>{-Jjavaoption}</code></pre>
<p>Changes the password under which the private/secret key identified by <code>alias</code> is protected, from <code>old_keypass</code> to <code>new_keypass</code>, which must be at least 6 characters. </p>
<p> If the <code>-keypass</code> option is not provided at the command line, and the key password is different from the keystore password, then the user is prompted for it. </p>
<p> If the <code>-new</code> option is not provided at the command line, then the user is prompted for it</p>
<dt>-delete</p>
<dd>
<pre><code>[-alias </code><i>alias</i>] {-storetype <i>storetype</i>} {-keystore <i>keystore</i>} [-storepass <i>storepass</i>]</pre>
<pre><code>{-providerName </code><i>provider_name</i>} </pre>
<pre><code>{-providerClass </code><i>provider_class_name</i> {-providerArg <i>provider_arg</i>}}</pre>
<pre><code>{-v} {-protected} {-Jjavaoption}</code></pre>
<p>Deletes from the keystore the entry identified by <code>alias</code>. The user is prompted for the alias, when no alias is provided at the command line.</p>
<dt>-changealias</p>
<dd>
<pre><code>{-alias </code><i>alias</i>} [-destalias <i>destalias</i>] [-keypass <i>keypass</i>] {-storetype <i>storetype</i>}</pre>
<pre><code>{-keystore </code><i>keystore</i>} [-storepass <i>storepass</i>] {-providerName <i>provider_name</i>}</pre>
<pre><code>{-providerClass </code><i>provider_class_name</i> {-providerArg <i>provider_arg</i>}} {-v}</pre>
<pre><code>{-protected} {-Jjavaoption}</code></pre>
<p>Move an existing keystore entry from the specified <code>alias</code> to a new alias, <code>destalias</code>. If no destination alias is provided, then the command prompts for one. If the original entry is protected with an entry password, then the password can be supplied with the <code>-keypass</code> option. If no key password is provided, then the <code>storepass</code> (if provided) is attempted first. If the attempt fails, then the user is prompted for a password.</p>
<dt>-help</p>
<dd>Lists the basic commands and their options. </p>
<p> For more information about a specific command, enter the following, where <code>command_name</code> is the name of the command: <code>keytool -command_name -help</code>.</dl>
<h2>Examples</h2>
<p>This example walks through the sequence of steps to create a keystore for managing public/private key pair and certificates from trusted entities.</p>
<h3>Generate The Key Pair</h3>
<p>First, create a keystore and generate the key pair. You can use a command such as the following typed as a single line: </p>
<pre><code>keytool -genkeypair -dname &quot;cn=Mark Jones, ou=Java, o=Oracle, c=US&quot;</code></pre>
<pre><code> -alias business -keypass &lt;new password for private key&gt;</code></pre>
<pre><code> -keystore /working/mykeystore</code></pre>
<pre><code> -storepass &lt;new password for keystore&gt; -validity 180</code></pre>
<p>The command creates the keystore named <code>mykeystore</code> in the working directory (assuming it does not already exist), and assigns it the password specified by <code>&lt;new password for keystore&gt;</code>. It generates a public/private key pair for the entity whose distinguished name has a common name of Mark Jones, organizational unit of Java, organization of Oracle and two-letter country code of US. It uses the default DSA key generation algorithm to create the keys; both are 1024 bits. </p>
<p> The command uses the default SHA1withDSA signature algorithm to create a self-signed certificate that includes the public key and the distinguished name information. The certificate is valid for 180 days, and is associated with the private key in a keystore entry referred to by the alias <code>business</code>. The private key is assigned the password specified by <code>&lt;new password for private key&gt;</code>. </p>
<p> The command is significantly shorter when the option defaults are accepted. In this case, no options are required, and the defaults are used for unspecified options that have default values. You are prompted for any required values. You could have the following: </p>
<pre><code>keytool -genkeypair</code></pre>
<p>In this case, a keystore entry with the alias <code>mykey</code> is created, with a newly generated key pair and a certificate that is valid for 90 days. This entry is placed in the keystore named <code>.keystore</code> in your home directory. The keystore is created when it does not already exist. You are prompted for the distinguished name information, the keystore password, and the private key password. </p>
<p> The rest of the examples assume you executed the <code>-genkeypair</code> command without options specified, and that you responded to the prompts with values equal to those specified in the first <code>-genkeypair</code> command. For example, a distinguished name of <code>cn=Mark Jones</code>, <code>ou=Java</code>, <code>o=Oracle</code>, <code>c=US</code>).</p>
<h3>Request A Signed Certificate From A Ca</h3>
<p>Generating the key pair created a self-signed certificate. A certificate is more likely to be trusted by others when it is signed by a Certification Authority (CA). To get a CA signature, first generate a Certificate Signing Request (CSR), as follows: </p>
<pre><code>keytool -certreq -file MarkJ.csr</code></pre>
<p>This creates a CSR for the entity identified by the default alias <code>mykey</code> and puts the request in the file named MarkJ.csr. Submit this file to a CA, such as VeriSign. The CA authenticates you, the requestor (usually off-line), and returns a certificate, signed by them, authenticating your public key. In some cases, the CA returns a chain of certificates, each one authenticating the public key of the signer of the previous certificate in the chain.</p>
<h3>Import A Certificate For The Ca</h3>
<p>You now need to replace the self-signed certificate with a certificate chain, where each certificate in the chain authenticates the public key of the signer of the previous certificate in the chain, up to a root CA. </p>
<p> Before you import the certificate reply from a CA, you need one or more trusted certificates in your keystore or in the <code>cacerts</code> keystore file. See <code>-importcert</code> in Commands.</p>
<dl>
<dt>&bull;</p>
<dd>If the certificate reply is a certificate chain, then you need the top certificate of the chain. The root CA certificate that authenticates the public key of the CA.</p>
<dt>&bull;</p>
<dd>If the certificate reply is a single certificate, then you need a certificate for the issuing CA (the one that signed it). If that certificate is not self-signed, then you need a certificate for its signer, and so on, up to a self-signed root CA certificate.</dl>
<p> The <code>cacerts</code> keystore file ships with several VeriSign root CA certificates, so you probably will not need to import a VeriSign certificate as a trusted certificate in your keystore. But if you request a signed certificate from a different CA, and a certificate authenticating that CA&#8217;s public key was not added to <code>cacerts</code>, then you must import a certificate from the CA as a trusted certificate. </p>
<p> A certificate from a CA is usually either self-signed or signed by another CA, in which case you need a certificate that authenticates that CA&#8217;s public key. Suppose company ABC, Inc., is a CA, and you obtain a file named A<code>BCCA.cer</code> that is supposed to be a self-signed certificate from ABC, that authenticates that CA&#8217;s public key. Be careful to ensure the certificate is valid before you import it as a trusted certificate. View it first with the <code>keytool -printcert</code> command or the <code>keytool -importcert</code> command without the <code>-noprompt</code> option, and make sure that the displayed certificate fingerprints match the expected ones. You can call the person who sent the certificate, and compare the fingerprints that you see with the ones that they show or that a secure public key repository shows. Only when the fingerprints are equal is it guaranteed that the certificate was not replaced in transit with somebody else&#8217;s (for example, an attacker&#8217;s) certificate. If such an attack takes place, and you did not check the certificate before you imported it, then you would be trusting anything the attacker has signed. </p>
<p> If you trust that the certificate is valid, then you can add it to your keystore with the following command: </p>
<pre><code>keytool -importcert -alias abc -file ABCCA.cer</code></pre>
<p>This command creates a trusted certificate entry in the keystore, with the data from the file ABCCA.cer, and assigns the alias <code>abc</code> to the entry.</p>
<h3>Import The Certificate Reply From The Ca</h3>
<p>After you import a certificate that authenticates the public key of the CA you submitted your certificate signing request to (or there is already such a certificate in the cacerts file), you can import the certificate reply and replace your self-signed certificate with a certificate chain. This chain is the one returned by the CA in response to your request (when the CA reply is a chain), or one constructed (when the CA reply is a single certificate) using the certificate reply and trusted certificates that are already available in the keystore where you import the reply or in the <code>cacerts</code> keystore file. </p>
<p> For example, if you sent your certificate signing request to VeriSign, then you can import the reply with the following, which assumes the returned certificate is named VSMarkJ.cer: </p>
<pre><code>keytool -importcert -trustcacerts -file VSMarkJ.cer</code></pre>
<h3>Export A Certificate That Authenticates The Public Key</h3>
<p>If you used the <code>jarsigner</code> command to sign a Java Archive (JAR) file, then clients that want to use the file will want to authenticate your signature. One way the clients can authenticate you is by first importing your public key certificate into their keystore as a trusted entry. </p>
<p> You can export the certificate and supply it to your clients. As an example, you can copy your certificate to a file named MJ.cer with the following command that assumes the entry has an alias of <code>mykey</code>: </p>
<pre><code>keytool -exportcert -alias mykey -file MJ.cer</code></pre>
<p>With the certificate and the signed JAR file, a client can use the <code>jarsigner</code> command to authenticate your signature.</p>
<h3>Import Keystore</h3>
<p>The command <code>importkeystore</code> is used to import an entire keystore into another keystore, which means all entries from the source keystore, including keys and certificates, are all imported to the destination keystore within a single command. You can use this command to import entries from a different type of keystore. During the import, all new entries in the destination keystore will have the same alias names and protection passwords (for secret keys and private keys). If the <code>keytool</code> command cannot recover the private keys or secret keys from the source keystore, then it prompts you for a password. If it detects alias duplication, then it asks you for a new alias, and you can specify a new alias or simply allow the <code>keytool</code> command to overwrite the existing one. </p>
<p> For example, to import entries from a typical JKS type keystore key.jks into a PKCS #11 type hardware-based keystore, use the command: </p>
<pre><code>keytool -importkeystore</code></pre>
<pre><code> -srckeystore key.jks -destkeystore NONE</code></pre>
<pre><code> -srcstoretype JKS -deststoretype PKCS11</code></pre>
<pre><code> -srcstorepass &lt;src keystore password&gt;</code></pre>
<pre><code> -deststorepass &lt;destination keystore pwd&gt;</code></pre>
<p>The <code>importkeystore</code> command can also be used to import a single entry from a source keystore to a destination keystore. In this case, besides the options you see in the previous example, you need to specify the alias you want to import. With the <code>-srcalias</code> option specified, you can also specify the destination alias name in the command line, as well as protection password for a secret/private key and the destination protection password you want. The following command demonstrates this: </p>
<pre><code>keytool -importkeystore</code></pre>
<pre><code> -srckeystore key.jks -destkeystore NONE</code></pre>
<pre><code> -srcstoretype JKS -deststoretype PKCS11</code></pre>
<pre><code> -srcstorepass &lt;src keystore password&gt;</code></pre>
<pre><code> -deststorepass &lt;destination keystore pwd&gt;</code></pre>
<pre><code> -srcalias myprivatekey -destalias myoldprivatekey</code></pre>
<pre><code> -srckeypass &lt;source entry password&gt;</code></pre>
<pre><code> -destkeypass &lt;destination entry password&gt;</code></pre>
<pre><code> -noprompt</code></pre>
<h3>Generate Certificates For An Ssl Server</h3>
<p>The following are <code>keytool</code> commands to generate key pairs and certificates for three entities: Root CA (<code>root</code>), Intermediate CA (<code>ca</code>), and SSL server (<code>server</code>). Ensure that you store all the certificates in the same keystore. In these examples, RSA is the recommended the key algorithm. </p>
<pre><code>keytool -genkeypair -keystore root.jks -alias root -ext bc:c</code></pre>
<pre><code>keytool -genkeypair -keystore ca.jks -alias ca -ext bc:c</code></pre>
<pre><code>keytool -genkeypair -keystore server.jks -alias server</code></pre>
<pre><code>keytool -keystore root.jks -alias root -exportcert -rfc &gt; root.pem</code></pre>
<pre><code>keytool -storepass &lt;storepass&gt; -keystore ca.jks -certreq -alias ca |</code></pre>
<pre><code> keytool -storepass &lt;storepass&gt; -keystore root.jks</code></pre>
<pre><code> -gencert -alias root -ext BC=0 -rfc &gt; ca.pem</code></pre>
<pre><code>keytool -keystore ca.jks -importcert -alias ca -file ca.pem</code></pre>
<pre><code>keytool -storepass &lt;storepass&gt; -keystore server.jks -certreq -alias server |</code></pre>
<pre><code> keytool -storepass &lt;storepass&gt; -keystore ca.jks -gencert -alias ca</code></pre>
<pre><code> -ext ku:c=dig,kE -rfc &gt; server.pem</code></pre>
<pre><code>cat root.pem ca.pem server.pem |</code></pre>
<pre><code> keytool -keystore server.jks -importcert -alias server</code></pre>
<h2>Terms</h2>
<dl>
<dt>Keystore</p>
<dd>A keystore is a storage facility for cryptographic keys and certificates.</p>
<dt>Keystore entries</p>
<dd>Keystores can have different types of entries. The two most applicable entry types for the <code>keytool</code> command include the following: </p>
<p> <i>Key entries</i>: Each entry holds very sensitive cryptographic key information, which is stored in a protected format to prevent unauthorized access. Typically, a key stored in this type of entry is a secret key, or a private key accompanied by the certificate chain for the corresponding public key. See Certificate Chains. The <code>keytool</code> command can handle both types of entries, while the <code>jarsigner</code> tool only handles the latter type of entry, that is private keys and their associated certificate chains. </p>
<p> <i>Trusted certificate entries</i>: Each entry contains a single public key certificate that belongs to another party. The entry is called a trusted certificate because the keystore owner trusts that the public key in the certificate belongs to the identity identified by the subject (owner) of the certificate. The issuer of the certificate vouches for this, by signing the certificate.</p>
<dt>KeyStore aliases</p>
<dd>All keystore entries (key and trusted certificate entries) are accessed by way of unique aliases. </p>
<p> An alias is specified when you add an entity to the keystore with the <code>-genseckey</code> command to generate a secret key, the <code>-genkeypair</code> command to generate a key pair (public and private key), or the <code>-importcert</code> command to add a certificate or certificate chain to the list of trusted certificates. Subsequent <code>keytool</code> commands must use this same alias to refer to the entity. </p>
<p> For example, you can use the alias <code>duke</code> to generate a new public/private key pair and wrap the public key into a self-signed certificate with the following command. See Certificate Chains. </p>
<pre><code>keytool -genkeypair -alias duke -keypass dukekeypasswd</code></pre>
<p>This example specifies an initial password of <code>dukekeypasswd</code> required by subsequent commands to access the private key associated with the alias <code>duke</code>. If you later want to change Duke&#8217;s private key password, use a command such as the following: </p>
<pre><code>keytool -keypasswd -alias duke -keypass dukekeypasswd -new newpass</code></pre>
<p>This changes the password from <code>dukekeypasswd</code> to <code>newpass</code>. A password should not be specified on a command line or in a script unless it is for testing purposes, or you are on a secure system. If you do not specify a required password option on a command line, then you are prompted for it.</p>
<dt>KeyStore implementation</p>
<dd>The <code>KeyStore</code> class provided in the <code>java.security</code> package supplies well-defined interfaces to access and modify the information in a keystore. It is possible for there to be multiple different concrete implementations, where each implementation is that for a particular type of keystore. </p>
<p> Currently, two command-line tools (<code>keytool</code> and <code>jarsigner</code>) and a GUI-based tool named Policy Tool make use of keystore implementations. Because the <code>KeyStore</code> class is <code>public</code>, users can write additional security applications that use it. </p>
<p> There is a built-in default implementation, provided by Oracle. It implements the keystore as a file with a proprietary keystore type (format) named JKS. It protects each private key with its individual password, and also protects the integrity of the entire keystore with a (possibly different) password. </p>
<p> Keystore implementations are provider-based. More specifically, the application interfaces supplied by <code>KeyStore</code> are implemented in terms of a Service Provider Interface (SPI). That is, there is a corresponding abstract <code>KeystoreSpi</code> class, also in the <code>java.security package</code>, which defines the Service Provider Interface methods that providers must implement. The term <i>provider</i> refers to a package or a set of packages that supply a concrete implementation of a subset of services that can be accessed by the Java Security API. To provide a keystore implementation, clients must implement a provider and supply a <code>KeystoreSpi</code> subclass implementation, as described in How to Implement a Provider in the Java Cryptography Architecture at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/HowToImplAProvider.html">http://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/HowToImplAProvider.html</a> </p>
<p> Applications can choose different types of keystore implementations from different providers, using the <code>getInstance</code> factory method supplied in the <code>KeyStore</code> class. A keystore type defines the storage and data format of the keystore information, and the algorithms used to protect private/secret keys in the keystore and the integrity of the keystore. Keystore implementations of different types are not compatible. </p>
<p> The <code>keytool</code> command works on any file-based keystore implementation. It treats the keystore location that is passed to it at the command line as a file name and converts it to a <code>FileInputStream</code>, from which it loads the keystore information.)The <code>jarsigner</code> and <code>policytool</code> commands can read a keystore from any location that can be specified with a URL. </p>
<p> For <code>keytool</code> and <code>jarsigner</code>, you can specify a keystore type at the command line, with the <code>-storetype</code> option. For Policy Tool, you can specify a keystore type with the <i>Keystore</i> menu. </p>
<p> If you do not explicitly specify a keystore type, then the tools choose a keystore implementation based on the value of the <code>keystore.type</code> property specified in the security properties file. The security properties file is called <code>java.security</code>, and resides in the security properties directory, <code>java.home\lib\security</code> on Windows and <code>java.home/lib/security</code> on Oracle Solaris, where <code>java.home</code> is the runtime environment directory. The <code>jre</code> directory in the SDK or the top-level directory of the Java Runtime Environment (JRE). </p>
<p> Each tool gets the <code>keystore.type</code> value and then examines all the currently installed providers until it finds one that implements a keystores of that type. It then uses the keystore implementation from that provider.The <code>KeyStore</code> class defines a static method named <code>getDefaultType</code> that lets applications and applets retrieve the value of the <code>keystore.type</code> property. The following line of code creates an instance of the default keystore type as specified in the <code>keystore.type</code> property: </p>
<pre><code>KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());</code></pre>
<p>The default keystore type is <code>jks</code>, which is the proprietary type of the keystore implementation provided by Oracle. This is specified by the following line in the security properties file: </p>
<pre><code>keystore.type=jks</code></pre>
<p>To have the tools utilize a keystore implementation other than the default, you can change that line to specify a different keystore type. For example, if you have a provider package that supplies a keystore implementation for a keystore type called <code>pkcs12</code>, then change the line to the following: </p>
<pre><code>keystore.type=pkcs12</code></pre>
<p><i>Note:</i> Case does not matter in keystore type designations. For example, JKS would be considered the same as jks.</p>
<dt>Certificate</p>
<dd>A certificate (or public-key certificate) is a digitally signed statement from one entity (the issuer), saying that the public key and some other information of another entity (the subject) has some specific value. The following terms are related to certificates: </p>
<p> <i>Public Keys</i>: These are numbers associated with a particular entity, and are intended to be known to everyone who needs to have trusted interactions with that entity. Public keys are used to verify signatures. </p>
<p> <i>Digitally Signed</i>: If some data is digitally signed, then it is stored with the identity of an entity and a signature that proves that entity knows about the data. The data is rendered unforgeable by signing with the entity&#8217;s private key. </p>
<p> <i>Identity</i>: A known way of addressing an entity. In some systems, the identity is the public key, and in others it can be anything from an Oracle Solaris UID to an email address to an X.509 distinguished name. </p>
<p> <i>Signature</i>: A signature is computed over some data using the private key of an entity. The signer, which in the case of a certificate is also known as the issuer. </p>
<p> <i>Private Keys</i>: These are numbers, each of which is supposed to be known only to the particular entity whose private key it is (that is, it is supposed to be kept secret). Private and public keys exist in pairs in all public key cryptography systems (also referred to as public key crypto systems). In a typical public key crypto system, such as DSA, a private key corresponds to exactly one public key. Private keys are used to compute signatures. </p>
<p> <i>Entity</i>: An entity is a person, organization, program, computer, business, bank, or something else you are trusting to some degree. </p>
<p> Public key cryptography requires access to users&#8217; public keys. In a large-scale networked environment, it is impossible to guarantee that prior relationships between communicating entities were established or that a trusted repository exists with all used public keys. Certificates were invented as a solution to this public key distribution problem. Now a Certification Authority (CA) can act as a trusted third party. CAs are entities such as businesses that are trusted to sign (issue) certificates for other entities. It is assumed that CAs only create valid and reliable certificates because they are bound by legal agreements. There are many public Certification Authorities, such as VeriSign, Thawte, Entrust, and so on. </p>
<p> You can also run your own Certification Authority using products such as Microsoft Certificate Server or the Entrust CA product for your organization. With the <code>keytool</code> command, it is possible to display, import, and export certificates. It is also possible to generate self-signed certificates. </p>
<p> The <code>keytool</code> command currently handles X.509 certificates.</p>
<dt>X.509 Certificates</p>
<dd>The X.509 standard defines what information can go into a certificate and describes how to write it down (the data format). All the data in a certificate is encoded with two related standards called ASN.1/DER. Abstract Syntax Notation 1 describes data. The Definite Encoding Rules describe a single way to store and transfer that data. </p>
<p> All X.509 certificates have the following data, in addition to the signature: </p>
<p> <i>Version</i>: This identifies which version of the X.509 standard applies to this certificate, which affects what information can be specified in it. Thus far, three versions are defined. The <code>keytool</code> command can import and export v1, v2, and v3 certificates. It generates v3 certificates. </p>
<p> X.509 Version 1 has been available since 1988, is widely deployed, and is the most generic. </p>
<p> X.509 Version 2 introduced the concept of subject and issuer unique identifiers to handle the possibility of reuse of subject or issuer names over time. Most certificate profile documents strongly recommend that names not be reused and that certificates should not make use of unique identifiers. Version 2 certificates are not widely used. </p>
<p> X.509 Version 3 is the most recent (1996) and supports the notion of extensions where anyone can define an extension and include it in the certificate. Some common extensions are: KeyUsage (limits the use of the keys to particular purposes such as <code>signing-only</code>) and AlternativeNames (allows other identities to also be associated with this public key, for example. DNS names, email addresses, IP addresses). Extensions can be marked critical to indicate that the extension should be checked and enforced or used. For example, if a certificate has the KeyUsage extension marked critical and set to <code>keyCertSign</code>, then when this certificate is presented during SSL communication, it should be rejected because the certificate extension indicates that the associated private key should only be used for signing certificates and not for SSL use. </p>
<p> <i>Serial number</i>: The entity that created the certificate is responsible for assigning it a serial number to distinguish it from other certificates it issues. This information is used in numerous ways. For example, when a certificate is revoked its serial number is placed in a Certificate Revocation List (CRL). </p>
<p> <i>Signature algorithm identifier</i>: This identifies the algorithm used by the CA to sign the certificate. </p>
<p> <i>Issuer name</i>: The X.500 Distinguished Name of the entity that signed the certificate. See X.500 Distinguished Names. This is typically a CA. Using this certificate implies trusting the entity that signed this certificate. In some cases, such as root or top-level CA certificates, the issuer signs its own certificate. </p>
<p> <i>Validity period</i>: Each certificate is valid only for a limited amount of time. This period is described by a start date and time and an end date and time, and can be as short as a few seconds or almost as long as a century. The validity period chosen depends on a number of factors, such as the strength of the private key used to sign the certificate, or the amount one is willing to pay for a certificate. This is the expected period that entities can rely on the public value, when the associated private key has not been compromised. </p>
<p> <i>Subject name</i>: The name of the entity whose public key the certificate identifies. This name uses the X.500 standard, so it is intended to be unique across the Internet. This is the X.500 Distinguished Name (DN) of the entity. See X.500 Distinguished Names. For example, </p>
<pre><code>CN=Java Duke, OU=Java Software Division, O=Oracle Corporation, C=US</code></pre>
<p>These refer to the subject&#8217;s common name (CN), organizational unit (OU), organization (O), and country (C). </p>
<p> <i>Subject public key information</i>: This is the public key of the entity being named with an algorithm identifier that specifies which public key crypto system this key belongs to and any associated key parameters.</p>
<dt>Certificate Chains</p>
<dd>The <code>keytool</code> command can create and manage keystore key entries that each contain a private key and an associated certificate chain. The first certificate in the chain contains the public key that corresponds to the private key. </p>
<p> When keys are first generated, the chain starts off containing a single element, a self-signed certificate. See <code>-genkeypair</code> in Commands. A self-signed certificate is one for which the issuer (signer) is the same as the subject. The subject is the entity whose public key is being authenticated by the certificate. Whenever the <code>-genkeypair</code> command is called to generate a new public/private key pair, it also wraps the public key into a self-signed certificate. </p>
<p> Later, after a Certificate Signing Request (CSR) was generated with the <code>-certreq</code> command and sent to a Certification Authority (CA), the response from the CA is imported with <code>-importcert</code>, and the self-signed certificate is replaced by a chain of certificates. See the <code>-certreq</code> and <code>-importcert</code> options in Commands. At the bottom of the chain is the certificate (reply) issued by the CA authenticating the subject&#8217;s public key. The next certificate in the chain is one that authenticates the CA&#8217;s public key. </p>
<p> In many cases, this is a self-signed certificate, which is a certificate from the CA authenticating its own public key, and the last certificate in the chain. In other cases, the CA might return a chain of certificates. In this case, the bottom certificate in the chain is the same (a certificate signed by the CA, authenticating the public key of the key entry), but the second certificate in the chain is a certificate signed by a different CA that authenticates the public key of the CA you sent the CSR to. The next certificate in the chain is a certificate that authenticates the second CA&#8217;s key, and so on, until a self-signed root certificate is reached. Each certificate in the chain (after the first) authenticates the public key of the signer of the previous certificate in the chain. </p>
<p> Many CAs only return the issued certificate, with no supporting chain, especially when there is a flat hierarchy (no intermediates CAs). In this case, the certificate chain must be established from trusted certificate information already stored in the keystore. </p>
<p> A different reply format (defined by the PKCS #7 standard) includes the supporting certificate chain in addition to the issued certificate. Both reply formats can be handled by the <code>keytool</code> command. </p>
<p> The top-level (root) CA certificate is self-signed. However, the trust into the root&#8217;s public key does not come from the root certificate itself, but from other sources such as a newspaper. This is because anybody could generate a self-signed certificate with the distinguished name of, for example, the VeriSign root CA. The root CA public key is widely known. The only reason it is stored in a certificate is because this is the format understood by most tools, so the certificate in this case is only used as a vehicle to transport the root CA&#8217;s public key. Before you add the root CA certificate to your keystore, you should view it with the <code>-printcert</code> option and compare the displayed fingerprint with the well-known fingerprint obtained from a newspaper, the root CA&#8217;s Web page, and so on.</p>
<dt>The cacerts Certificates File</p>
<dd>A certificates file named <code>cacerts</code> resides in the security properties directory, <code>java.home\lib\security</code> on Windows and <code>java.home/lib/security</code> on Oracle Solaris, where <code>java.home</code> is the runtime environment&#8217;s directory, which would be the <code>jre</code> directory in the SDK or the top-level directory of the JRE. </p>
<p> The <code>cacerts</code> file represents a system-wide keystore with CA certificates. System administrators can configure and manage that file with the <code>keytool</code> command by specifying <code>jks</code> as the keystore type. The <code>cacerts</code> keystore file ships with a default set of root CA certificates. You can list the default certificates with the following command: </p>
<pre><code>keytool -list -keystore java.home/lib/security/cacerts</code></pre>
<p>The initial password of the <code>cacerts</code> keystore file is <code>changeit</code>. System administrators should change that password and the default access permission of that file upon installing the SDK. </p>
<p> <i>Note:</i> It is important to verify your <code>cacerts</code> file. Because you trust the CAs in the <code>cacerts</code> file as entities for signing and issuing certificates to other entities, you must manage the <code>cacerts</code> file carefully. The <code>cacerts</code> file should contain only certificates of the CAs you trust. It is your responsibility to verify the trusted root CA certificates bundled in the <code>cacerts</code> file and make your own trust decisions. </p>
<p> To remove an untrusted CA certificate from the <code>cacerts</code> file, use the <code>delete</code> option of the <code>keytool</code> command. You can find the <code>cacerts</code> file in the JRE installation directory. Contact your system administrator if you do not have permission to edit this file</p>
<dt>Internet RFC 1421 Certificate Encoding Standard</p>
<dd>Certificates are often stored using the printable encoding format defined by the Internet RFC 1421 standard, instead of their binary encoding. This certificate format, also known as Base64 encoding, makes it easy to export certificates to other applications by email or through some other mechanism. </p>
<p> Certificates read by the <code>-importcert</code> and <code>-printcert</code> commands can be in either this format or binary encoded. The <code>-exportcert</code> command by default outputs a certificate in binary encoding, but will instead output a certificate in the printable encoding format, when the <code>-rfc</code> option is specified. </p>
<p> The <code>-list</code> command by default prints the SHA1 fingerprint of a certificate. If the <code>-v</code> option is specified, then the certificate is printed in human-readable format. If the <code>-rfc</code> option is specified, then the certificate is output in the printable encoding format. </p>
<p> In its printable encoding format, the encoded certificate is bounded at the beginning and end by the following text: </p>
<pre><code>-----BEGIN CERTIFICATE-----</code></pre>
<pre><code>encoded certificate goes here. </code></pre>
<pre><code>-----END CERTIFICATE-----</code></pre>
<dt>X.500 Distinguished Names</p>
<dd>X.500 Distinguished Names are used to identify entities, such as those that are named by the <code>subject</code> and <code>issuer</code> (signer) fields of X.509 certificates. The <code>keytool</code> command supports the following subparts: </p>
<p> <i>commonName</i>: The common name of a person such as Susan Jones. </p>
<p> <i>organizationUnit</i>: The small organization (such as department or division) name. For example, Purchasing. </p>
<p> <i>localityName</i>: The locality (city) name, for example, Palo Alto. </p>
<p> <i>stateName</i>: State or province name, for example, California. </p>
<p> <i>country</i>: Two-letter country code, for example, CH. </p>
<p> When you supply a distinguished name string as the value of a <code>-dname</code> option, such as for the <code>-genkeypair</code> command, the string must be in the following format: </p>
<pre><code>CN=cName, OU=orgUnit, O=org, L=city, S=state, C=countryCode</code></pre>
<p>All the italicized items represent actual values and the previous keywords are abbreviations for the following: </p>
<pre><code>CN=commonName</code></pre>
<pre><code>OU=organizationUnit</code></pre>
<pre><code>O=organizationName</code></pre>
<pre><code>L=localityName</code></pre>
<pre><code>S=stateName</code></pre>
<pre><code>C=country</code></pre>
<p>A sample distinguished name string is: </p>
<pre><code>CN=Mark Smith, OU=Java, O=Oracle, L=Cupertino, S=California, C=US</code></pre>
<p>A sample command using such a string is: </p>
<pre><code>keytool -genkeypair -dname &quot;CN=Mark Smith, OU=Java, O=Oracle, L=Cupertino,</code></pre>
<pre><code>S=California, C=US&quot; -alias mark</code></pre>
<p>Case does not matter for the keyword abbreviations. For example, CN, cn, and Cn are all treated the same. </p>
<p> Order matters; each subcomponent must appear in the designated order. However, it is not necessary to have all the subcomponents. You can use a subset, for example: </p>
<pre><code>CN=Steve Meier, OU=Java, O=Oracle, C=US</code></pre>
<p>If a distinguished name string value contains a comma, then the comma must be escaped by a backslash (\) character when you specify the string on a command line, as in: </p>
<pre><code>cn=Peter Schuster, ou=Java\, Product Development, o=Oracle, c=US</code></pre>
<p>It is never necessary to specify a distinguished name string on a command line. When the distinguished name is needed for a command, but not supplied on the command line, the user is prompted for each of the subcomponents. In this case, a comma does not need to be escaped by a backslash (\).</dl>
<h2>Warnings</h2>
<h3>Importing Trusted Certificates Warning</h3>
<p><i>Important</i>: Be sure to check a certificate very carefully before importing it as a trusted certificate. </p>
<p> Windows Example: </p>
<p> View the certificate first with the <code>-printcert</code> command or the <code>-importcert</code> command without the <code>-noprompt</code> option. Ensure that the displayed certificate fingerprints match the expected ones. For example, suppose sends or emails you a certificate that you put it in a file named <code>	mp
