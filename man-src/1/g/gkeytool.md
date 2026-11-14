---
title: "gkeytool(1)"
name: "gkeytool"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gkeytool/"
description: "gkeytool – Manage private keys and public certificates"
---

<h2 class="name">NAME</h2>
<p> gkeytool &#8211; Manage private keys and public certificates </p>
<h2>SYNOPSIS</h2>
<p> keytool [<i></i><font SIZE="-1"><i>COMMAND</i></font><i></i>] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> Cryptographic credentials, in a Java environment, are usually stored in a <i>Key Store</i>. The Java <font SIZE="-1">SDK</font> specifies a <i>Key Store</i> as a persistent container of two types of objects: <i>Key Entries</i> and <i>Trusted Certificates</i>. The security tool <code>keytool</code> is a Java-based application for managing those types of objects. </p>
<p> A <i>Key Entry</i> represents the private key part of a key-pair used in Public-Key Cryptography, and a signed X.509 certificate which authenticates the public key part for a known entity; i.e. the owner of the key-pair. The X.509 certificate itself contains the public key part of the key-pair. </p>
<p> A <i>Trusted Certificate</i> is a signed X.509 certificate issued by a trusted entity. The <i>Trust</i> in this context is relative to the User of the <code>keytool</code>. In other words, the existence of a <i>Trusted Certificate</i> in the <i>Key Store</i> processed by a <code>keytool</code> command implies that the User trusts the <i>Issuer</i> of that <i>Trusted Certificate</i> to also sign, and hence authenticates, other <i>Subjects</i> the tool may process. </p>
<p> <i>Trusted Certificates</i> are important because they allow the tool to mechanically construct <i>Chains of Trust</i> starting from one of the <i>Trusted Certificates</i> in a <i>Key Store</i> and ending with a certificate whose <i>Issuer</i> is potentially unknown. A valid chain is an ordered list, starting with a <i>Trusted Certificate</i> (also called the <i>anchor</i>), ending with the target certificate, and satisfying the condition that the <i>Subject</i> of certificate <tt>&quot;#i&quot;</tt> is the <i>Issuer</i> of certificate <tt>&quot;#i + 1&quot;</tt>. </p>
<p> The <code>keytool</code> is invoked from the command line as follows: </p>
<pre>
        keytool [COMMAND] ...
</pre>
<p> Multiple <i></i><font SIZE="-1"><i>COMMAND</i></font><i></i>s may be specified at once, each complete with its own options. <code>keytool</code> will parse all the arguments, before processing, and executing, each <tt>&quot;COMMAND&quot;</tt>. If an exception occurs while executing one <i></i><font SIZE="-1"><i>COMMAND</i></font><i></i> <code>keytool</code> will abort. Note however that because the implementation of the tool uses code to parse command line options that also supports GNU-style options, you have to separate each command group with a double-hyphen; e.g </p>
<pre>
        keytool -list -- -printcert -alias mykey
</pre>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211; Add/Update commands</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>-genkey [</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i><code>]&#8230;</code></p>
<dd> Generate a new <i>Key Entry</i>, eventually creating a new key store.</p>
<dt><code>-import [</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i><code>]&#8230;</code></p>
<dd> Add, to a key store, <i>Key Entries</i> (private keys and certificate chains authenticating the public keys) and <i>Trusted Certificates</i> (3rd party certificates which can be used as <i>Trust Anchors</i> when building chains-of-trust).</p>
<dt><code>-selfcert [</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i><code>]&#8230;</code></p>
<dd> Generate a new self-signed <i>Trusted Certificate</i>.</p>
<dt><code>-cacert [</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i><code>]&#8230;</code></p>
<dd> Import a <font SIZE="-1">CA</font> <i>Trusted Certificate</i>.</p>
<dt><code>-identitydb [</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i><code>]&#8230;</code></p>
<dd> <font SIZE="-1"><code>NOT</code></font><font SIZE="-1"><code>IMPLEMENTED</code></font><font SIZE="-1"><code>YET</code></font>.Import a <font SIZE="-1">JDK</font> 1.1 style Identity Database.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&#8211; Export commands</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>-certreq [</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i><code>]&#8230;</code></p>
<dd> Issue a <i>Certificate Signing Request</i> (<font SIZE="-1">CSR</font>) which can be then sent to a <i>Certification Authority</i> (<font SIZE="-1">CA</font>) to issue a certificate signed (by the <font SIZE="-1">CA</font>) and authenticating the <i>Subject</i> of the request.</p>
<dt><code>-export [</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i><code>]&#8230;</code></p>
<dd> Export a certificate from a key store.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&#8211; Display commands</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>-list [</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i><code>]&#8230;</code></p>
<dd> Print one or all certificates in a key store to <tt>&quot;STDOUT&quot;</tt>.</p>
<dt><code>-printcert [</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i><code>]&#8230;</code></p>
<dd> Print a human-readable form of a certificate, in a designated file, to <tt>&quot;STDOUT&quot;</tt>.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&#8211; Management commands</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>-keyclone [</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i><code>]&#8230;</code></p>
<dd> Clone a <i>Key Entry</i> in a key store.</p>
<dt><code>-storepasswd [</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i><code>]&#8230;</code></p>
<dd> Change the password protecting a key store.</p>
<dt><code>-keypasswd [</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i><code>]&#8230;</code></p>
<dd> Change the password protecting a <i>Key Entry</i> in a key store.</p>
<dt><code>-delete [</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i><code>]&#8230;</code></p>
<dd> Delete a <i>Key Entry</i> or a <i>Trusted Certificate</i> from a key store.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> <i>Common options</i> </p>
<p> The following <font SIZE="-1"><code>OPTION</code></font>s are used in more than one <font SIZE="-1"><code>COMMAND</code></font>. They are described here to reduce redundancy.</p>
<dl>
<dt><code>-alias</code> <i>Alias</i></p>
<dd> Every entry, be it a <i>Key Entry</i> or a <i>Trusted Certificate</i>, in a key store is uniquely identified by a user-defined <i>Alias</i> string. Use this option to specify the <i>Alias</i> to use when referring to an entry in the key store. Unless specified otherwise, a default value of <tt>&quot;mykey&quot;</tt> shall be used when this option is omitted from the command line.</p>
<dt><code>-keyalg</code> <i></i><font SIZE="-1"><i>ALGORITHM</i></font><i></i></p>
<dd> Use this option to specify the canonical name of the key-pair generation algorithm. The default value for this option is <tt>&quot;DSS&quot;</tt> (a synonym for the Digital Signature Algorithm also known as <font SIZE="-1">DSA</font>).</p>
<dt><code>-keysize</code> <i></i><font SIZE="-1"><i>SIZE</i></font><i></i></p>
<dd> Use this option to specify the number of bits of the shared modulus (for both the public and private keys) to use when generating new keys. A default value of <tt>1024</tt> will be used if this option is omitted from the command line.</p>
<dt><code>-validity</code> <i></i><font SIZE="-1"><i>DAY_COUNT</i></font><i></i></p>
<dd> Use this option to specify the number of days a newly generated certificate will be valid for. The default value is <tt>90</tt> (days) if this option is omitted from the command line.</p>
<dt><code>-storetype</code> <i></i><font SIZE="-1"><i>STORE_TYPE</i></font><i></i></p>
<dd> Use this option to specify the type of the key store to use. The default value, if this option is omitted, is that of the property <tt>&quot;keystore.type&quot;</tt> in the security properties file, which is obtained by invoking the static method call <tt>&quot;getDefaultType()&quot;</tt> in <tt>&quot;java.security.KeyStore&quot;</tt>.</p>
<dt><code>-storepass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> Use this option to specify the password protecting the key store. If this option is omitted from the command line, you will be prompted to provide a password.</p>
<dt><code>-keystore</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> Use this option to specify the location of the key store to use. The default value is a file <font SIZE="-1">URL</font> referencing the file named <i>.keystore</i> located in the path returned by the call to <tt>&quot;java.lang.System#getProperty(String)&quot;</tt> using <tt>&quot;user.home&quot;</tt> as argument. </p>
<p> If a <font SIZE="-1">URL</font> was specified, but was found to be malformed &#8211;e.g. missing protocol element&#8212; the tool will attempt to use the <font SIZE="-1">URL</font> value as a file-name (with absolute or relative path-name) of a key store &#8211;as if the protocol was <tt>&quot;file:&quot;</tt>.</p>
<dt><code>-provider</code> <i></i><font SIZE="-1"><i>PROVIDER_CLASS_NAME</i></font><i></i></p>
<dd> A fully qualified class name of a <i>Security Provider</i> to add to the current list of <i>Security Providers</i> already installed in the <font SIZE="-1">JVM</font> in-use. If a provider class is specified with this option, and was successfully added to the runtime &#8211;i.e. it was not already installed&#8212; then the tool will attempt to removed this <i>Security Provider</i> before exiting.</p>
<dt><code>-file</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Use this option to designate a file to use with a command. When specified with this option, the value is expected to be the fully qualified path of a file accessible by the File System. Depending on the command, the file may be used as input or as output. When this option is omitted from the command line, <tt>&quot;STDIN&quot;</tt> will be used instead, as the source of input, and <tt>&quot;STDOUT&quot;</tt> will be used instead as the output destination.</p>
<dt><code>-v</code></p>
<dd> Unless specified otherwise, use this option to enable more verbose output.</dl>
<p> <i>Add/Update commands</i> </p>
<p> The <code>-genkey</code> command </p>
<p> Use this command to generate a new key-pair (both private and public keys), and save these credentials in the key store as a <i>Key Entry</i>, associated with the designated (if was specified with the <code>-alias</code> option) or default (if the <code>-alias</code> option is omitted) <i>Alias</i>. </p>
<p> The private key material will be protected with a user-defined password (see <code>-keypass</code> option). The public key on the other hand will be part of a self-signed X.509 certificate, which will form a 1-element chain and will be saved in the key store.</p>
<dl>
<dt><code>-alias</code> <i></i><font SIZE="-1"><i>ALIAS</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keyalg</code> <i></i><font SIZE="-1"><i>ALGORITHM</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keysize</code> <i></i><font SIZE="-1"><i>KEY_SIZE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-sigalg</code> <i></i><font SIZE="-1"><i>ALGORITHM</i></font><i></i></p>
<dd> The canonical name of the digital signature algorithm to use for signing certificates. If this option is omitted, a default value will be chosen based on the type of the key-pair; i.e., the algorithm that ends up being used by the -keyalg option. If the key-pair generation algorithm is <tt>&quot;DSA&quot;</tt>, the value for the signature algorithm will be <tt>&quot;SHA1withDSA&quot;</tt>. If on the other hand the key-pair generation algorithm is <tt>&quot;RSA&quot;</tt>, then the tool will use <tt>&quot;MD5withRSA&quot;</tt> as the signature algorithm.</p>
<dt><code>-dname</code> <i></i><font SIZE="-1"><i>NAME</i></font><i></i></p>
<dd> This a mandatory value for the command. If no value is specified &#8211;i.e. the <code>-dname</code> option is omitted&#8212; the tool will prompt you to enter a <i>Distinguished Name</i> to use as both the <i>Owner</i> and <i>Issuer</i> of the generated self-signed certificate. </p>
<p> See <i>Common Options</i> for more details.</p>
<dt><code>-keypass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> Use this option to specify the password which the tool will use to protect the newly created <i>Key Entry</i>. </p>
<p> If this option is omitted, you will be prompted to provide a password.</p>
<dt><code>-validity</code> <i></i><font SIZE="-1"><i>DAY_COUNT</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storetype</code> <i></i><font SIZE="-1"><i>STORE_TYPE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keystore</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storepass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-provider</code> <i></i><font SIZE="-1"><i>PROVIDER_CLASS_NAME</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-v</code></p>
<dd> See <i>Common Options</i> for more details.</dl>
<p> The <code>-import</code> command </p>
<p> Use this command to read an X.509 certificate, or a PKCS#7 <i>Certificate Reply</i> from a designated input source and incorporate the certificates into the key store. </p>
<p> If the <i>Alias</i> does not already exist in the key store, the tool treats the certificate read from the input source as a new <i>Trusted Certificate</i>. It then attempts to discover a chain-of-trust, starting from that certificate and ending at another <i>Trusted Certificate</i>, already stored in the key store. If the <code>-trustcacerts</code> option is present, an additional key store, of type <tt>&quot;JKS&quot;</tt> named <i>cacerts</i>, and assumed to be present in <i>${</i><font SIZE="-1"><i>JAVA_HOME</i></font><i>}/lib/security</i> will also be consulted if found &#8212;<tt>&quot;${JAVA_HOME}&quot;</tt> refers to the location of an installed <i>Java Runtime Environment</i> (<font SIZE="-1">JRE</font>). If no chain-of-trust can be established, and unless the <tt>&quot;-noprompt&quot;</tt> option has been specified, the certificate is printed to <tt>&quot;STDOUT&quot;</tt> and the user is prompted for a confirmation. </p>
<p> If <i>Alias</i> exists in the key store, the tool will treat the certificate(s) read from the input source as a <i>Certificate Reply</i>, which can be a chain of certificates, that eventually would replace the chain of certificates associated with the <i>Key Entry</i> of that <i>Alias</i>. The substitution of the certificates only occurs if a chain-of-trust can be established between the bottom certificate of the chain read from the input file and the <i>Trusted Certificates</i> already present in the key store. Again, if the <code>-trustcacerts</code> option is specified, additional <i>Trusted Certificates</i> in the same <i>cacerts</i> key store will be considered. If no chain-of-trust can be established, the operation will abort.</p>
<dl>
<dt><code>-alias</code> <i></i><font SIZE="-1"><i>ALIAS</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-file</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keypass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> Use this option to specify the password which the tool will use to protect the <i>Key Entry</i> associated with the designated <i>Alias</i>, when replacing this <i>Alias</i>&#8216; chain of certificates with that found in the certificate reply. </p>
<p> If this option is omitted, and the chain-of-trust for the certificate reply has been established, the tool will first attempt to unlock the <i>Key Entry</i> using the same password protecting the key store. If this fails, you will then be prompted to provide a password.</p>
<dt><code>-noprompt</code></p>
<dd> Use this option to prevent the tool from prompting the user.</p>
<dt><code>-trustcacerts</code></p>
<dd> Use this option to indicate to the tool that a key store, of type <tt>&quot;JKS&quot;</tt>, named <i>cacerts</i>, and usually located in <i>lib/security</i> in an installed <i>Java Runtime Environment</i> should be considered when trying to establish chain-of-trusts.</p>
<dt><code>-storetype</code> <i></i><font SIZE="-1"><i>STORE_TYPE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keystore</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storepass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-provider</code> <i></i><font SIZE="-1"><i>PROVIDER_CLASS_NAME</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-v</code></p>
<dd> See <i>Common Options</i> for more details.</dl>
<p> The <code>-selfcert</code> command </p>
<p> Use this command to generate a self-signed X.509 version 1 certificate. The newly generated certificate will form a chain of one element which will replace the previous chain associated with the designated <i>Alias</i> (if <code>-alias</code> option was specified), or the default <i>Alias</i> (if <code>-alias</code> option was omitted).</p>
<dl>
<dt><code>-alias</code> <i></i><font SIZE="-1"><i>ALIAS</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-sigalg</code> <i></i><font SIZE="-1"><i>ALGORITHM</i></font><i></i></p>
<dd> The canonical name of the digital signature algorithm to use for signing the certificate. If this option is omitted, a default value will be chosen based on the type of the private key associated with the designated <i>Alias</i>. If the private key is a <tt>&quot;DSA&quot;</tt> one, the value for the signature algorithm will be <tt>&quot;SHA1withDSA&quot;</tt>. If on the other hand the private key is an <tt>&quot;RSA&quot;</tt> one, then the tool will use <tt>&quot;MD5withRSA&quot;</tt> as the signature algorithm.</p>
<dt><code>-dname</code> <i></i><font SIZE="-1"><i>NAME</i></font><i></i></p>
<dd> Use this option to specify the <i>Distinguished Name</i> of the newly generated self-signed certificate. If this option is omitted, the existing <i>Distinguished Name</i> of the base certificate in the chain associated with the designated <i>Alias</i> will be used instead. </p>
<p> See <i>Common Options</i> for more details.</p>
<dt><code>-validity</code> <i></i><font SIZE="-1"><i>DAY_COUNT</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keypass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> Use this option to specify the password which the tool will use to unlock the <i>Key Entry</i> associated with the designated <i>Alias</i>. </p>
<p> If this option is omitted, the tool will first attempt to unlock the <i>Key Entry</i> using the same password protecting the key store. If this fails, you will then be prompted to provide a password.</p>
<dt><code>-storetype</code> <i></i><font SIZE="-1"><i>STORE_TYPE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keystore</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storepass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-provider</code> <i></i><font SIZE="-1"><i>PROVIDER_CLASS_NAME</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-v</code></p>
<dd> See <i>Common Options</i> for more details.</dl>
<p> The <code>-cacert</code> command </p>
<p> Use this command to import, a <font SIZE="-1">CA</font> certificate and add it to the key store as a <i>Trusted Certificate</i>. The <i>Alias</i> for this new entry will be constructed from the <font SIZE="-1">FILE</font>&#8216;s base-name after replacing hyphens and dots with underscores. </p>
<p> This command is useful when used in a script that recursively visits a directory of <font SIZE="-1">CA</font> certificates to populate a <tt>&quot;cacerts.gkr&quot;</tt> <i>Key Store</i> of trusted certificates which can then be used commands that specify the <code>-trustcacerts</code> option.</p>
<dl>
<dt><code>-file</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storetype</code> <i></i><font SIZE="-1"><i>STORE_TYPE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keystore</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storepass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-provider</code> <i></i><font SIZE="-1"><i>PROVIDER_CLASS_NAME</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-v</code></p>
<dd> See <i>Common Options</i> for more details.</dl>
<p> The <code>-identitydb</code> command </p>
<p> <font SIZE="-1"><code>NOT</code></font><font SIZE="-1"><code>IMPLEMENTED</code></font><font SIZE="-1"><code>YET</code></font>. </p>
<p> Use this command to import a <font SIZE="-1">JDK</font> 1.1 style Identity Database.</p>
<dl>
<dt><code>-file</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storetype</code> <i></i><font SIZE="-1"><i>STORE_TYPE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keystore</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storepass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-provider</code> <i></i><font SIZE="-1"><i>PROVIDER_CLASS_NAME</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-v</code></p>
<dd> See <i>Common Options</i> for more details.</dl>
<p> <i>Export commands</i> </p>
<p> The <code>-certreq</code> command </p>
<p> Use this command to generate a PKCS#10 <i>Certificate Signing Request</i> (<font SIZE="-1">CSR</font>) and write it to a designated output destination. The contents of the destination should look something like the following: </p>
<pre><code>
-- -- -BEGIN NEW CERTIFICATE REQUEST-- -- -MI... QAwXzEUMBIGA1UEAwwLcnNuQGdudS5vcmcxGzAZBgNVBAoMElUg
            Q2... A0GA1UEBwwGU3lkbmV5MQwwCgYDVQQIDANOU1cxCzAJBgNVBACC... FC... IVwNVOfQLRX +
        O5kAhQ / a4RTZme2L8PnpvgRwrf7Eg8D6w ==
    -- -- -END NEW CERTIFICATE REQUEST-- -- -
</code></pre>
<p> <font SIZE="-1"><code>IMPORTANT</code></font>: Some documentation (e.g. <font SIZE="-1">RSA</font> examples) claims that the <tt>&quot;Attributes&quot;</tt> field, in the <font SIZE="-1">CSR</font> is <tt>&quot;OPTIONAL&quot;</tt> while <font SIZE="-1">RFC-2986</font> implies the opposite. This implementation considers this field, by default, as <tt>&quot;OPTIONAL&quot;</tt>, unless the option <code>-attributes</code> is specified on the command line.</p>
<dl>
<dt><code>-alias</code> <i></i><font SIZE="-1"><i>ALIAS</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-sigalg</code> <i></i><font SIZE="-1"><i>ALGORITHM</i></font><i></i></p>
<dd> The canonical name of the digital signature algorithm to use for signing the certificate. If this option is omitted, a default value will be chosen based on the type of the private key associated with the designated <i>Alias</i>. If the private key is a <tt>&quot;DSA&quot;</tt> one, the value for the signature algorithm will be <tt>&quot;SHA1withDSA&quot;</tt>. If on the other hand the private key is an <tt>&quot;RSA&quot;</tt> one, then the tool will use <tt>&quot;MD5withRSA&quot;</tt> as the signature algorithm.</p>
<dt><code>-file</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keypass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> Use this option to specify the password which the tool will use to unlock the <i>Key Entry</i> associated with the designated <i>Alias</i>. </p>
<p> If this option is omitted, the tool will first attempt to unlock the <i>Key Entry</i> using the same password protecting the key store. If this fails, you will then be prompted to provide a password.</p>
<dt><code>-storetype</code> <i></i><font SIZE="-1"><i>STORE_TYPE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keystore</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storepass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-provider</code> <i></i><font SIZE="-1"><i>PROVIDER_CLASS_NAME</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-v</code></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-attributes</code></p>
<dd> Use this option to force the tool to encode a <tt>&quot;NULL&quot;</tt> <font SIZE="-1">DER</font> value in the <font SIZE="-1">CSR</font> as the value of the <tt>&quot;Attributes&quot;</tt> field.</dl>
<p> The <code>-export</code> command </p>
<p> Use this command to export a certificate stored in a key store to a designated output destination, either in binary format (if the <code>-v</code> option is specified), or in <font SIZE="-1">RFC-1421</font> compliant encoding (if the <code>-rfc</code> option is specified instead).</p>
<dl>
<dt><code>-alias</code> <i></i><font SIZE="-1"><i>ALIAS</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-file</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storetype</code> <i></i><font SIZE="-1"><i>STORE_TYPE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keystore</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storepass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-provider</code> <i></i><font SIZE="-1"><i>PROVIDER_CLASS_NAME</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-rfc</code></p>
<dd> Use <font SIZE="-1">RFC-1421</font> specifications when encoding the output.</p>
<dt><code>-v</code></p>
<dd> Output the certificate in binary <font SIZE="-1">DER</font> encoding. This is the default output format of the command if neither <code>-rfc</code> nor <tt>&quot;-v&quot;</tt> options were detected on the command line. If both this option and the <code>-rfc</code> option are detected on the command line, the tool will opt for the <font SIZE="-1">RFC-1421</font> style encoding.</dl>
<p> <i>Display commands</i> </p>
<p> The <code>-list</code> command </p>
<p> Use this command to print one or all of a key store entries to <tt>&quot;STDOUT&quot;</tt>. Usually this command will only print a <i>fingerprint</i> of the certificate, unless either the <code>-rfc</code> or the <code>-v</code> option is specified.</p>
<dl>
<dt><code>-alias</code> <i></i><font SIZE="-1"><i>ALIAS</i></font><i></i></p>
<dd> If this option is omitted, the tool will print <font SIZE="-1">ALL</font> the entries found in the key store. </p>
<p> See <i>Common Options</i> for more details.</p>
<dt><code>-storetype</code> <i></i><font SIZE="-1"><i>STORE_TYPE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keystore</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storepass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-provider</code> <i></i><font SIZE="-1"><i>PROVIDER_CLASS_NAME</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-rfc</code></p>
<dd> Use <font SIZE="-1">RFC-1421</font> specifications when encoding the output.</p>
<dt><code>-v</code></p>
<dd> Output the certificate in human-readable format. If both this option and the <code>-rfc</code> option are detected on the command line, the tool will opt for the human-readable form and will not abort the command.</dl>
<p> The <code>-printcert</code> command </p>
<p> Use this command to read a certificate from a designated input source and print it to <tt>&quot;STDOUT&quot;</tt> in a human-readable form.</p>
<dl>
<dt><code>-file</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-v</code></p>
<dd> See <i>Common Options</i> for more details.</dl>
<p> <i>Management commands</i> </p>
<p> The <code>-keyclone</code> command </p>
<p> Use this command to clone an existing <i>Key Entry</i> and store it under a new (different) <i>Alias</i> protecting, its private key material with possibly a new password.</p>
<dl>
<dt><code>-alias</code> <i></i><font SIZE="-1"><i>ALIAS</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-dest</code> <i></i><font SIZE="-1"><i>ALIAS</i></font><i></i></p>
<dd> Use this option to specify the new <i>Alias</i> which will be used to identify the cloned copy of the <i>Key Entry</i>.</p>
<dt><code>-keypass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> Use this option to specify the password which the tool will use to unlock the <i>Key Entry</i> associated with the designated <i>Alias</i>. </p>
<p> If this option is omitted, the tool will first attempt to unlock the <i>Key Entry</i> using the same password protecting the key store. If this fails, you will then be prompted to provide a password.</p>
<dt><code>-new</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> Use this option to specify the password protecting the private key material of the newly cloned copy of the <i>Key Entry</i>.</p>
<dt><code>-storetype</code> <i></i><font SIZE="-1"><i>STORE_TYPE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keystore</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storepass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-provider</code> <i></i><font SIZE="-1"><i>PROVIDER_CLASS_NAME</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-v</code></p>
<dd> See <i>Common Options</i> for more details.</dl>
<p> The <code>-storepasswd</code> command </p>
<p> Use this command to change the password protecting a key store.</p>
<dl>
<dt><code>-new</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> The new, and different, password which will be used to protect the designated key store.</p>
<dt><code>-storetype</code> <i></i><font SIZE="-1"><i>STORE_TYPE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keystore</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storepass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-provider</code> <i></i><font SIZE="-1"><i>PROVIDER_CLASS_NAME</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-v</code></p>
<dd> See <i>Common Options</i> for more details.</dl>
<p> The <code>-keypasswd</code> command </p>
<p> Use this command to change the password protecting the private key material of a designated <i>Key Entry</i>.</p>
<dl>
<dt><code>-alias</code> <i></i><font SIZE="-1"><i>ALIAS</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details. </p>
<p> Use this option to specify the password which the tool will use to unlock the <i>Key Entry</i> associated with the designated <i>Alias</i>. </p>
<p> If this option is omitted, the tool will first attempt to unlock the <i>Key Entry</i> using the same password protecting the key store. If this fails, you will then be prompted to provide a password.</p>
<dt><code>-new</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> The new, and different, password which will be used to protect the private key material of the designated <i>Key Entry</i>.</p>
<dt><code>-storetype</code> <i></i><font SIZE="-1"><i>STORE_TYPE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keystore</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storepass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-provider</code> <i></i><font SIZE="-1"><i>PROVIDER_CLASS_NAME</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-v</code></p>
<dd> See <i>Common Options</i> for more details.</dl>
<p> The <code>-delete</code> command </p>
<p> Use this command to delete a designated key store entry.</p>
<dl>
<dt><code>-alias</code> <i></i><font SIZE="-1"><i>ALIAS</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storetype</code> <i></i><font SIZE="-1"><i>STORE_TYPE</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-keystore</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-storepass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-provider</code> <i></i><font SIZE="-1"><i>PROVIDER_CLASS_NAME</i></font><i></i></p>
<dd> See <i>Common Options</i> for more details.</p>
<dt><code>-v</code></p>
<dd> See <i>Common Options</i> for more details.</dl>
<h2>BUGS</h2>
<h2>SEE ALSO</h2>
<h2>AUTHOR</h2>
<h2>Index</h2>
