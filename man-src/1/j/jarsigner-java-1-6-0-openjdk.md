---
title: "jarsigner-java-1-6-0-openjdk(1)"
name: "jarsigner-java-1-6-0-openjdk"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jarsigner-java-1-6-0-openjdk/"
description: "jarsigner – JAR Signing and Verification Tool"
---

<p>jarsigner &#8211; JAR Signing and Verification Tool </p>
<dl>
<dd>Generates signatures for Java ARchive (JAR) files, and verifies the signatures of signed JAR files. </p>
</dl>
<h2>Synopsis</h2>
<pre><code>jarsigner</code> [ options ] jar-file alias
<code>jarsigner</code> -verify [ options ] jar-file </pre>
<h2>Description</h2>
<p>The <code>jarsigner</code> tool is used for two purposes: </p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>to sign Java ARchive (JAR) files, and</p>
<dt>2.</p>
<dd>to verify the signatures and integrity of signed JAR files.</dl>
</dl>
<p> The JAR feature enables the packaging of class files, images, sounds, and other digital data in a single file for faster and easier distribution. A tool named <code>jar</code> enables developers to produce JAR files. (Technically, any zip file can also be considered a JAR file, although when created by <code>jar</code> or processed by <code>jarsigner</code>, JAR files also contain a META-INF/MANIFEST.MF file.) </p>
<p> A <i>digital signature</i> is a string of bits that is computed from some data (the data being &quot;signed&quot;) and the private key of an entity (a person, company, etc.). Like a handwritten signature, a digital signature has many useful characteristics: </p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>Its authenticity can be verified, via a computation that uses the public key corresponding to the private key used to generate the signature.</p>
<dt>o</p>
<dd>It cannot be forged, assuming the private key is kept secret.</p>
<dt>o</p>
<dd>It is a function of the data signed and thus can&#8217;t be claimed to be the signature for other data as well.</p>
<dt>o</p>
<dd>The signed data cannot be changed; if it is, the signature will no longer verify as being authentic.</dl>
</dl>
<p> In order for an entity&#8217;s signature to be generated for a file, the entity must first have a public/private key pair associated with it, and also one or more certificates authenticating its public key. A <i>certificate</i> is a digitally signed statement from one entity, saying that the public key of some other entity has a particular value. </p>
<p> <code>jarsigner</code> uses key and certificate information from a <i>keystore</i> to generate digital signatures for JAR files. A keystore is a database of private keys and their associated X.509 certificate chains authenticating the corresponding public keys. The <code>keytool</code> utility is used to create and administer keystores. </p>
<p> <code>jarsigner</code> uses an entity&#8217;s private key to generate a signature. The signed JAR file contains, among other things, a copy of the certificate from the keystore for the public key corresponding to the private key used to sign the file. <code>jarsigner</code> can verify the digital signature of the signed JAR file using the certificate inside it (in its signature block file). </p>
<p> Starting in J2SE 5.0, <code>jarsigner</code> can generate signatures that include a timestamp, thus enabling systems/deployer (including Java Plug-in) to check whether the JAR file was signed while the signing certificate was still valid. In addition, APIs were added in J2SE 5.0 to allow applications to obtain the timestamp information. </p>
<p> At this time, <code>jarsigner</code> can only sign JAR files created by the SDK <code>jar</code> tool or zip files. (JAR files are the same as zip files, except they also have a META-INF/MANIFEST.MF file. Such a file will automatically be created when <code>jarsigner</code> signs a zip file.) </p>
<p> The default <code>jarsigner</code> behavior is to <i>sign</i> a JAR (or zip) file. Use the <i>-verify</i> option to instead have it <i>verify</i> a signed JAR file. </p>
<h3>Compatibility with JDK 1.1</h3>
<dl>
<dd>The <code>keytool</code> and <code>jarsigner</code> tools completely replace the <code>javakey</code> tool provided in JDK 1.1. These new tools provide more features than <code>javakey</code>, including the ability to protect the keystore and private keys with passwords, and the ability to verify signatures in addition to generating them. </p>
<p> The new keystore architecture replaces the identity database that <code>javakey</code> created and managed. There is no backwards compatibility between the keystore format and the database format used by <code>javakey</code> in 1.1. However, </p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>It is possible to import the information from an identity database into a keystore, via the <code>keytool</code> <i>-identitydb</i> command.</p>
<dt>o</p>
<dd><code>jarsigner</code> can sign JAR files also previously signed using <code>javakey</code>.</p>
<dt>o</p>
<dd><code>jarsigner</code> can verify JAR files signed using <code>javakey</code>. Thus, it recognizes and can work with signer aliases that are from a JDK 1.1 identity database rather than a Java 2 SDK keystore.</dl>
</dl>
<p> The following table explains how JAR files that were signed in JDK 1.1.x are treated in the Java 2 platform. </p>
<pre><br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<code>JAR File Type</code><code>Identity in 1.1 database</code><code>Privileges Granted</code>
Signed JARNONONO
Unsigned JARNONONO
Signed JARNOYESNO
Signed JARYES/UntrustedNONO
Signed JARYES/UntrustedNOYES
Signed JARNOYESYES
Signed JARYES/TrustedYESYES
Signed JARYES/TrustedNONOAll privileges
Signed JARYES/TrustedYESNOAll privileges (1)
Signed JARYES/TrustedNOYESAll privileges (1)
Notes:
<dl><dt><dd><dl><dt>1.<dd>If an identity/alias is mentioned in the policy file, it must be imported into the keystore for the policy file to have any effect on privileges granted. 
<dt>2.<dd>The policy file/keystore combination has precedence over a trusted identity in the identity database. 
<dt>3.<dd>Untrusted identities are ignored in the Java 2 platform. 
<dt>4.<dd>Only trusted identities can be imported into Java 2 SDK keystores. 
</dl></dl>
</dl></pre>
<h3>Keystore Aliases</h3>
<dl>
<dd>All keystore entities are accessed via unique <i>aliases</i>. </p>
<p> When using <code>jarsigner</code> to sign a JAR file, you must specify the alias for the keystore entry containing the private key needed to generate the signature. For example, the following will sign the JAR file named &quot;MyJARFile.jar&quot;, using the private key associated with the alias &quot;duke&quot; in the keystore named &quot;mystore&quot; in the &quot;working&quot; directory. Since no output file is specified, it overwrites MyJARFile.jar with the signed JAR file. </p>
<pre><code> jarsigner -keystore /working/mystore -storepass myspass
 -keypass dukekeypasswd MyJARFile.jar duke </code></pre>
<p>Keystores are protected with a password, so the store password (in this case &quot;myspass&quot;) must be specified. You will be prompted for it if you don&#8217;t specify it on the command line. Similarly, private keys are protected in a keystore with a password, so the private key&#8217;s password (in this case &quot;dukekeypasswd&quot;) must be specified, and you will be prompted for it if you don&#8217;t specify it on the command line and it isn&#8217;t the same as the store password. </p>
</dl>
<h3>Keystore Location</h3>
<dl>
<dd><code>jarsigner</code> has a <i>-keystore</i> option for specifying the URL of the keystore to be used. The keystore is by default stored in a file named <i>.keystore</i> in the user&#8217;s home directory, as determined by the <i>user.home</i> system property. On Solaris systems <i>user.home</i> defaults to the user&#8217;s home directory. </p>
<p> Note that the input stream from the <i>-keystore</i> option is passed to the <i>KeyStore.load</i> method. If <i>NONE</i> is specified as the URL, then a null stream is passed to the <i>KeyStore.load</i> method. <i>NONE</i> should be specified if the <i>KeyStore</i> is not file-based, for example, if it resides on a hardware token device. </p>
</dl>
<h3>Keystore Implementation</h3>
<dl>
<dd>The <i>KeyStore</i> class provided in the <i>java.security</i> package supplies well-defined interfaces to access and modify the information in a keystore. It is possible for there to be multiple different concrete implementations, where each implementation is that for a particular <i>type</i> of keystore. </p>
<p> Currently, there are two command-line tools that make use of keystore implementations (<code>keytool</code> and <code>jarsigner</code>), and also a GUI-based tool named <code>Policy Tool</code>. Since <i>KeyStore</i> is publicly available, Java 2 SDK users can write additional security applications that use it. </p>
<p> There is a built-in default implementation, provided by Sun Microsystems. It implements the keystore as a file, utilizing a proprietary keystore type (format) named &quot;JKS&quot;. It protects each private key with its individual password, and also protects the integrity of the entire keystore with a (possibly different) password. </p>
<p> Keystore implementations are provider-based. More specifically, the application interfaces supplied by <i>KeyStore</i> are implemented in terms of a &quot;Service Provider Interface&quot; (SPI). That is, there is a corresponding abstract <i>KeystoreSpi</i> class, also in the <i>java.security</i> package, which defines the Service Provider Interface methods that &quot;providers&quot; must implement. (The term &quot;provider&quot; refers to a package or a set of packages that supply a concrete implementation of a subset of services that can be accessed by the Java Security API.) Thus, to provide a keystore implementation, clients must implement a provider and supply a KeystoreSpi subclass implementation, as described in <i>How to Implement a Provider for the Java Cryptography Architecture</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/technotes/guides/security/HowToImplAProvider.html.">http://java.sun.com/javase/6/docs/technotes/guides/security/HowToImplAProvider.html.</a> </p>
<p> Applications can choose different <i>types</i> of keystore implementations from different providers, using the &quot;getInstance&quot; factory method supplied in the <i>KeyStore</i> class. A keystore type defines the storage and data format of the keystore information, and the algorithms used to protect private keys in the keystore and the integrity of the keystore itself. Keystore implementations of different types are not compatible. </p>
<p> <code>keytool</code> works on any file-based keystore implementation. (It treats the keytore location that is passed to it at the command line as a filename and converts it to a FileInputStream, from which it loads the keystore information.) The <code>jarsigner</code> and <code>policytool</code> tools, on the other hand, can read a keystore from any location that can be specified using a URL. </p>
<p> For <code>jarsigner</code> and <code>keytool</code>, you can specify a keystore type at the command line, via the <i>-storetype</i> option. For <code>Policy Tool</code>, you can specify a keystore type via the &quot;Change Keystore&quot; command in the Edit menu. </p>
<p> If you don&#8217;t explicitly specify a keystore type, the tools choose a keystore implementation based simply on the value of the <i>keystore.type</i> property specified in the security properties file. The security properties file is called <i>java.security</i>, and it resides in the SDK security properties directory, <i>java.home</i>/lib/security, where <i>java.home</i> is the runtime environment&#8217;s directory (the <i>jre</i> directory in the SDK or the top-level directory of the Java 2 Runtime Environment). </p>
<p> Each tool gets the <i>keystore.type</i> value and then examines all the currently-installed providers until it finds one that implements keystores of that type. It then uses the keystore implementation from that provider. </p>
<p> The <i>KeyStore</i> class defines a static method named <i>getDefaultType</i> that lets applications and applets retrieve the value of the <i>keystore.type</i> property. The following line of code creates an instance of the default keystore type (as specified in the <i>keystore.type</i> property): </p>
<pre><code> KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());</code></pre>
<p>The default keystore type is &quot;jks&quot; (the proprietary type of the keystore implementation provided by Sun). This is specified by the following line in the security properties file: </p>
<pre><code> keystore.type=jks</code></pre>
<p>Note: Case doesn&#8217;t matter in keystore type designations. For example, &quot;JKS&quot; would be considered the same as &quot;jks&quot;. </p>
<p> To have the tools utilize a keystore implementation other than the default, change that line to specify a different keystore type. For example, if you have a provider package that supplies a keystore implementation for a keystore type called &quot;pkcs12&quot;, change the line to </p>
<pre><code> keystore.type=pkcs12</code></pre>
<p>Note that if you us the PKCS#11 provider package, you should refer to the <i>KeyTool and JarSigner</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/technotes/guides/security/p11guide.html#keytooljarsigner">http://java.sun.com/javase/6/docs/technotes/guides/security/p11guide.html#keytooljarsigner</a> section of the Java PKCS#11 Reference Guide for details. </p>
</dl>
<h3>Supported Algorithms</h3>
<dl>
<dd>By default, <code>jarsigner</code> signs a JAR file using either </p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>DSA (Digital Signature Algorithm) with the SHA-1 digest algorithm, or</p>
<dt>o</p>
<dd>the RSA algorithm with the MD5 digest algorithm.</dl>
</dl>
<p> That is, if the signer&#8217;s public and private keys are DSA keys, <code>jarsigner</code> will sign the JAR file using the &quot;SHA1withDSA&quot; algorithm. If the signer&#8217;s keys are RSA keys, <code>jarsigner</code> will attempt to sign the JAR file using the &quot;MD5withRSA&quot; algorithm. </p>
<p> These default signature algorithms can be overridden using the <i>-sigalg</i> option. </p>
</dl>
<h3>The Signed JAR File</h3>
<dl>
<dd>When <code>jarsigner</code> is used to sign a JAR file, the output signed JAR file is exactly the same as the input JAR file, except that it has two additional files placed in the META-INF directory: </p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>a signature file, with a .SF extension, and</p>
<dt>o</p>
<dd>a signature block file, with a .DSA extension.</dl>
</dl>
<p> The base file names for these two files come from the value of the <i>-sigFile</i> option. For example, if the option appears as </p>
<pre><code> -sigFile MKSIGN</code></pre>
<p>the files are named &quot;MKSIGN.SF&quot; and &quot;MKSIGN.DSA&quot;. </p>
<p> If no <i>-sigfile</i> option appears on the command line, the base file name for the .SF and .DSA files will be the first 8 characters of the alias name specified on the command line, all converted to upper case. If the alias name has fewer than 8 characters, the full alias name is used. If the alias name contains any characters that are not allowed in a signature file name, each such character is converted to an underscore (&quot;_&quot;) character in forming the file name. Legal characters include letters, digits, underscores, and hyphens. </p>
<p> <code>The Signature (.SF) File</code> </p>
<dl>
<dd>A signature file (the .SF file) looks similar to the manifest file that is always included in a JAR file when <code>jarsigner</code> is used to sign the file. That is, for each source file included in the JAR file, the .SF file has three lines, just as in the manifest file, listing the following: </p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>the file name,</p>
<dt>o</p>
<dd>the name of the digest algorithm used (SHA), and</p>
<dt>o</p>
<dd>a SHA digest value.</dl>
</dl>
<p> In the manifest file, the SHA digest value for each source file is the digest (hash) of the binary data in the source file. In the .SF file, on the other hand, the digest value for a given source file is the hash of the three lines in the manifest file for the source file. </p>
<p> The signature file also, by default, includes a header containing a hash of the whole manifest file. The presence of the header enables verification optimization, as described in JAR File Verification. </p>
</dl>
<p> <code>The Signature Block (.DSA) File</code> </p>
<dl>
<dd>The .SF file is signed and the signature is placed in the .DSA file. The .DSA file also contains, encoded inside it, the certificate or certificate chain from the keystore which authenticates the public key corresponding to the private key used for signing. </p>
</dl>
</dl>
<h3>Signature Timestamp</h3>
<dl>
<dd>As of the J2SE 5.0 release, the <i>jarsigner</i> tool can now generate and store a signature timestamp when signing a JAR file. In addition, <i>jarsigner</i> supports alternative signing mechanisms. This behavior is optional and is controlled by the user at the time of signing through these options: </p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd><i>-tsa url</i></p>
<dt>o</p>
<dd><i>-tsacert alias</i></p>
<dt>o</p>
<dd><i>-altsigner class</i></p>
<dt>o</p>
<dd><i>-altsignerpath classpathlist</i></dl>
</dl>
<p> Each of these options is detailed in the Options section below. </p>
</dl>
<h3>JAR File Verification</h3>
<dl>
<dd>A successful JAR file verification occurs if the signature(s) are valid, and none of the files that were in the JAR file when the signatures were generated have been changed since then. JAR file verification involves the following steps: </p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Verify the signature of the .SF file itself.</dl>
<p> That is, the verification ensures that the signature stored in each signature block (.DSA) file was in fact generated using the private key corresponding to the public key whose certificate (or certificate chain) also appears in the .DSA file. It also ensures that the signature is a valid signature of the corresponding signature (.SF) file, and thus the .SF file has not been tampered with.</p>
<dl>
<dt>2.</p>
<dd>Verify the digest listed in each entry in the .SF file with each corresponding section in the manifest.</dl>
<p> The .SF file by default includes a header containing a hash of the entire manifest file. When the header is present, then the verification can check to see whether or not the hash in the header indeed matches the hash of the manifest file. If that is the case, verification proceeds to the next step. </p>
<p> If that is not the case, a less optimized verification is required to ensure that the hash in each source file information section in the .SF file equals the hash of its corresponding section in the manifest file (see The Signature (.SF) File). </p>
<p> One reason the hash of the manifest file that is stored in the .SF file header may not equal the hash of the current manifest file would be because one or more files were added to the JAR file (using the <i>jar</i> tool) after the signature (and thus the .SF file) was generated. When the <i>jar</i> tool is used to add files, the manifest file is changed (sections are added to it for the new files), but the .SF file is not. A verification is still considered successful if none of the files that were in the JAR file when the signature was generated have been changed since then, which is the case if the hashes in the non-header sections of the .SF file equal the hashes of the corresponding sections in the manifest file.</p>
<dl>
<dt>3.</p>
<dd>Read each file in the JAR file that has an entry in the .SF file. While reading, compute the file&#8217;s digest, and then compare the result with the digest for this file in the manifest section. The digests should be the same, or verification fails.</dl>
</dl>
<p> If any serious verification failures occur during the verification process, the process is stopped and a security exception is thrown. It is caught and displayed by <code>jarsigner</code>. </p>
</dl>
<h3>Multiple Signatures for a JAR File</h3>
<dl>
<dd>A JAR file can be signed by multiple people simply by running the <code>jarsigner</code> tool on the file multiple times, specifying the alias for a different person each time, as in: </p>
<pre><code> jarsigner myBundle.jar susan
 jarsigner myBundle.jar kevin</code></pre>
<p>When a JAR file is signed multiple times, there are multiple .SF and .DSA files in the resulting JAR file, one pair for each signature. Thus, in the example above, the output JAR file includes files with the following names: </p>
<pre><code> SUSAN.SF
 SUSAN.DSA
 KEVIN.SF
 KEVIN.DSA</code></pre>
<p>Note: It is also possible for a JAR file to have mixed signatures, some generated by the JDK 1.1 <code>javakey</code> tool and others by <code>jarsigner</code>. That is, <code>jarsigner</code> can be used to sign JAR files already previously signed using <code>javakey</code>. </p>
</dl>
<h2>Options</h2>
<p>The various <code>jarsigner</code> options are listed and described below. Note: </p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>All option names are preceded by a minus sign (-).</p>
<dt>o</p>
<dd>The options may be provided in any order.</p>
<dt>o</p>
<dd>Items in italics (option values) represent the actual values that must be supplied.</p>
<dt>o</p>
<dd>The <i>-keystore</i>, <i>-storepass</i>, <i>-keypass</i>, <i>-sigfile</i>, <i>-sigalg</i>, <i>-digestalg</i>, and <i>-signedjar</i> options are only relevant when signing a JAR file, not when verifying a signed JAR file. Similarly, an alias is only specified on the command line when signing a JAR file.</dl>
</dl>
<dl>
<dd>
<dl>
<dt>-keystore url</p>
<dd>Specifies the URL that tells the keystore location. This defaults to the file <i>.keystore</i> in the user&#8217;s home directory, as determined by the &quot;user.home&quot; system property.</dl>
<p> A keystore is required when signing, so you must explicitly specify one if the default keystore does not exist (or you want to use one other than the default). </p>
<p> A keystore is <i>not</i> required when verifying, but if one is specified, or the default exists, and the <i>-verbose</i> option was also specified, additional information is output regarding whether or not any of the certificates used to verify the JAR file are contained in that keystore. </p>
<p> Note: the <i>-keystore</i> argument can actually be a file name (and path) specification rather than a URL, in which case it will be treated the same as a &quot;file:&quot; URL. That is, </p>
<pre><code> -keystore </code><tt>filePathAndName</tt></pre>
<p>is treated as equivalent to </p>
<pre><code> -keystore file:</code><tt>filePathAndName</tt></pre>
<p>If the Sun PKCS#11 provider has been configured in the <i>java.security</i> security properties file (located in the JRE&#8217;s <i>$JAVA_HOME/lib/security</i> directory), then keytool and jarsigner can operate on the PKCS#11 token by specifying these options:</p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd><i>-keystore NONE</i></p>
<dt>o</p>
<dd><i>-storetype PKCS11</i></dl>
</dl>
<p> For example, this command lists the contents of the configured PKCS#11 token:</p>
<dl>
<dd>
<pre><code> jarsigner -keystore NONE -storetype PKCS11 -list
 </code></pre>
</dl>
<dl>
<dt>-storetype storetype</p>
<dd>Specifies the type of keystore to be instantiated. The default keystore type is the one that is specified as the value of the &quot;keystore.type&quot; property in the security properties file, which is returned by the static <i>getDefaultType</i> method in <i>java.security.KeyStore</i>.</dl>
<p> The PIN for a PCKS#11 token can also be specified using the <i>-storepass</i> option. If none has been specified, keytool and jarsigner will prompt for the token PIN. If the token has a protected authentication path (such as a dedicated PIN-pad or a biometric reader), then the <i>-protected</i> option must be specified and no password options can be specified.</p>
<dl>
<dt>-storepass password</p>
<dd>Specifies the password which is required to access the keystore. This is only needed when signing (not verifying) a JAR file. In that case, if a <i>-storepass</i> option is not provided at the command line, the user is prompted for the password.</dl>
<p> Note: The password shouldn&#8217;t be specified on the command line or in a script unless it is for testing purposes, or you are on a secure system. Also, when typing in a password at the password prompt, the password is echoed (displayed exactly as typed), so be careful not to type it in front of anyone.</p>
<dl>
<dt>-keypass password</p>
<dd>Specifies the password used to protect the private key of the keystore entry addressed by the alias specified on the command line. The password is required when using <code>jarsigner</code> to sign a JAR file. If no password is provided on the command line, and the required password is different from the store password, the user is prompted for it.</dl>
<p> Note: The password shouldn&#8217;t be specified on the command line or in a script unless it is for testing purposes, or you are on a secure system. Also, when typing in a password at the password prompt, the password is echoed (displayed exactly as typed), so be careful not to type it in front of anyone.</p>
<dl>
<dt>-sigfile file</p>
<dd>Specifies the base file name to be used for the generated .SF and .DSA files. For example, if <i>file</i> is &quot;DUKESIGN&quot;, the generated .SF and .DSA files will be named &quot;DUKESIGN.SF&quot; and &quot;DUKESIGN.DSA&quot;, and will be placed in the &quot;META-INF&quot; directory of the signed JAR file.</dl>
<p> The characters in <i>file</i> must come from the set &quot;a-zA-Z0-9_-&quot;. That is, only letters, numbers, underscore, and hyphen characters are allowed. Note: All lowercase characters will be converted to uppercase for the .SF and .DSA file names. </p>
<p> If no <i>-sigfile</i> option appears on the command line, the base file name for the .SF and .DSA files will be the first 8 characters of the alias name specified on the command line, all converted to upper case. If the alias name has fewer than 8 characters, the full alias name is used. If the alias name contains any characters that are not legal in a signature file name, each such character is converted to an underscore (&quot;_&quot;) character in forming the file name.</p>
<dl>
<dt>-sigalg algorithm</p>
<dd>
<dl>
<dd>Specifies the name of the signature algorithm to use to sign the JAR file. </p>
<p> See <i>Appendix A</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/technotes/guides/security/crypto/CryptoSpec.html#appa">http://java.sun.com/javase/6/docs/technotes/guides/security/crypto/CryptoSpec.html#appa</a> of the Java Cryptography Architecture for a list of standard signature algorithm names. This algorithm must be compatible with the private key used to sign the JAR file. If this option is not specified, SHA1withDSA or MD5withRSA will be used depending on the type of private key. There must either be a statically installed provider supplying an implementation of the specified algorithm or the user must specify one with the <i>-providerClass</i> option, otherwise the command will not succeed. </p>
</dl>
<dt>-digestalg algorithm</p>
<dd>
<dl>
<dd>Specifies the name of the message digest algorithm to use when digesting the entries of a jar file. </p>
<p> See <i>Appendix A</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/technotes/guides/security/crypto/CryptoSpec.html#appa">http://java.sun.com/javase/6/docs/technotes/guides/security/crypto/CryptoSpec.html#appa</a> of the Java Cryptography Architecture for a list of standard message digest algorithm names. If this option is not specified, SHA-1 will be used. There must either be a statically installed provider supplying an implementation of the specified algorithm or the user must specify one with the <i>-providerClass</i> option, otherwise the command will not succeed. </p>
</dl>
<dt>-signedjar file</p>
<dd>Specifies the name to be used for the signed JAR file.</dl>
<p> If no name is specified on the command line, the name used is the same as the input JAR file name (the name of the JAR file to be signed); in other words, that file is overwritten with the signed JAR file.</p>
<dl>
<dt>-verify</p>
<dd>If this appears on the command line, the specified JAR file will be verified, not signed. If the verification is successful, &quot;jar verified&quot; will be displayed. If you try to verify an unsigned JAR file, or a JAR file signed with an unsupported algorithm (e.g., RSA when you don&#8217;t have an RSA provider installed), the following is displayed: &quot;jar is unsigned. (signatures missing or not parsable)&quot;</dl>
<p> It is possible to verify JAR files signed using either <code>jarsigner</code> or the JDK 1.1 <code>javakey</code> tool, or both. </p>
<p> For further information on verification, see JAR File Verification.</p>
<dl>
<dt>-certs</p>
<dd>If this appears on the command line, along with the <i>-verify</i> and <i>-verbose</i> options, the output includes certificate information for each signer of the JAR file. This information includes</p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>the name of the type of certificate (stored in the .DSA file) that certifies the signer&#8217;s public key</p>
<dt>o</p>
<dd>if the certificate is an X.509 certificate (more specifically, an instance of <i>java.security.cert.X509Certificate</i>): the distinguished name of the signer</dl>
</dl>
</dl>
<p> The keystore is also examined. If no keystore value is specified on the command line, the default keystore file (if any) will be checked. If the public key certificate for a signer matches an entry in the keystore, then the following information will also be displayed:</p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>in parentheses, the alias name for the keystore entry for that signer. If the signer actually comes from a JDK 1.1 identity database instead of from a keystore, the alias name will appear in brackets instead of parentheses.</dl>
</dl>
<dl>
<dt>-verbose</p>
<dd>If this appears on the command line, it indicates &quot;verbose&quot; mode, which causes <code>jarsigner</code> to output extra information as to the progress of the JAR signing or verification.</p>
<dt>-internalsf</p>
<dd>In the past, the .DSA (signature block) file generated when a JAR file was signed used to include a complete encoded copy of the .SF file (signature file) also generated. This behavior has been changed. To reduce the overall size of the output JAR file, the .DSA file by default doesn&#8217;t contain a copy of the .SF file anymore. But if <i>-internalsf</i> appears on the command line, the old behavior is utilized. <code>This option is mainly useful for testing; in practice, it should not be used, since doing so eliminates a useful optimization.</code></p>
<dt>-sectionsonly</p>
<dd>If this appears on the command line, the .SF file (signature file) generated when a JAR file is signed does <i>not</i> include a header containing a hash of the whole manifest file. It just contains information and hashes related to each individual source file included in the JAR file, as described in The Signature (.SF) File .</dl>
<p> By default, this header is added, as an optimization. When the header is present, then whenever the JAR file is verified, the verification can first check to see whether or not the hash in the header indeed matches the hash of the whole manifest file. If so, verification proceeds to the next step. If not, it is necessary to do a less optimized verification that the hash in each source file information section in the .SF file equals the hash of its corresponding section in the manifest file. </p>
<p> For further information, see JAR File Verification. </p>
<p> <code>This option is mainly useful for testing; in practice, it should not be used, since doing so eliminates a useful optimization.</code></p>
<dl>
<dt>-protected</p>
<dd>Either <i>true</i> or <i>false</i>. This value should be specified as <i>true</i> if a password must be given via a protected authentication path such as a dedicated PIN reader.</dl>
</dl>
<dl>
<dd>
<dl>
<dt>-provider provider-class-name</p>
<dd>Used to specify the name of cryptographic service provider&#8217;s master class file when the service provider is not listed in the security properties file, <i>java.security</i>.</dl>
<p> Used in conjunction with the <i>-providerArg</i> <i>ConfigFilePath</i> option, keytool and jarsigner will install the provider dynamically (where <i>ConfigFilePath</i> is the path to the token configuration file). Here&#8217;s an example of a command to list a PKCS#11 keystore when the Sun PKCS#11 provider has not been configured in the security properties file.</p>
<dl>
<dd>
<pre><code>jarsigner -keystore NONE -storetype PKCS11 \
 -providerClass sun.security.pkcs11.SunPKCS11 \
 -providerArg /foo/bar/token.config \
 -list</code></pre>
</dl>
<dl>
<dt>-providerName providerName</p>
<dd>If more than one provider has been configured in the <i>java.security</i> security properties file, you can use the <i>-providerName</i> option to target a specific provider instance. The argument to this option is the name of the provider.</dl>
<p> For the Sun PKCS#11 provider, <i>providerName</i> is of the form <i>SunPKCS11-</i><i>TokenName</i>, where <i>TokenName</i> is the name suffix that the provider instance has been configured with, as detailed in the <i>configuration attributes table</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/technotes/guides/security/p11guide.html#KeyToolJarSigner#ATTRS.">http://java.sun.com/javase/6/docs/technotes/guides/security/p11guide.html#KeyToolJarSigner#ATTRS.</a> For example, the following command lists the contents of the PKCS#11 keystore provider instance with name suffix <i>SmartCard</i>:</p>
<dl>
<dd>
<pre><code>jarsigner -keystore NONE -storetype PKCS11 \
 -providerName SunPKCS11-SmartCard \
 -list</code></pre>
</dl>
<dl>
<dt>-Jjavaoption</p>
<dd>Passes through the specified <i>javaoption</i> string directly to the Java interpreter. (<code>jarsigner</code> is actually a &quot;wrapper&quot; around the interpreter.) This option should not contain any spaces. It is useful for adjusting the execution environment or memory usage. For a list of possible interpreter options, type <i>java -h</i> or <i>java -X</i> at the command line.</dl>
<dl>
<dt>-tsa url</p>
<dd>If <i>&quot;-tsa <a rel="nofollow" href="http://example.tsa.url">http://example.tsa.url</a>&quot;</i> appears on the command line when signing a JAR file then a timestamp is generated for the signature. The URL, <i><a href="http://example.tsa.url">http://example.tsa.url</a></i>, identifies the location of the Time Stamping Authority (TSA). It overrides any URL found via the <i>-tsacert</i> option. The <i>-tsa</i> option does not require the TSA&#8217;s public key certificate to be present in the keystore.</dl>
<p> To generate the timestamp, <i>jarsigner</i> communicates with the TSA using the Time-Stamp Protocol (TSP) defined in <i>RFC 3161</i> @ <a rel="nofollow" href="http://www.ietf.org/rfc/rfc3161.txt.">http://www.ietf.org/rfc/rfc3161.txt.</a> If successful, the timestamp token returned by the TSA is stored along with the signature in the signature block file. </p>
<dl>
<dt>-tsacert alias</p>
<dd>If <i>&quot;-tsacert alias&quot;</i> appears on the command line when signing a JAR file then a timestamp is generated for the signature. The <i>alias</i> identifies the TSA&#8217;s public key certificate in the keystore that is currently in effect. The entry&#8217;s certificate is examined for a Subject Information Access extension that contains a URL identifying the location of the TSA.</dl>
<p> The TSA&#8217;s public key certificate must be present in the keystore when using <i>-tsacert</i>. </p>
<dl>
<dt>-altsigner class</p>
<dd>Specifies that an alternative signing mechanism be used. The fully-qualified class name identifies a class file that extends the <i>com.sun.jarsigner.ContentSigner abstract class</i>. The path to this class file is defined by the <i>-altsignerpath</i> option. If the <i>-altsigner</i> option is used, <i>jarsigner</i> uses the signing mechanism provided by the specified class. Otherwise, <i>jarsigner</i> uses its default signing mechanism.</dl>
<p> For example, to use the signing mechanism provided by a class named <i>com.sun.sun.jarsigner.AuthSigner</i>, use the <i>jarsigner</i> option <i>&quot;-altsigner com.sun.jarsigner.AuthSigner&quot;</i> </p>
<dl>
<dt>-altsignerpath classpathlist</p>
<dd>Specifies the path to the class file (the class file name is specified with the <i>-altsigner</i> option described above) and any JAR files it depends on. If the class file is in a JAR file, then this specifies the path to that JAR file, as shown in the example below.</dl>
<p> An absolute path or a path relative to the current directory may be specified. If <i>classpathlist</i> contains multiple paths or JAR files, they should be separated with a colon (<i>:</i>) on Solaris and a semi-colon (<i>;</i>) on Windows. This option is not necessary if the class is already in the search path. </p>
<p> Example of specifying the path to a jar file that contains the class file:</p>
<dl>
<dd><i>-altsignerpath /home/user/lib/authsigner.jar</i> </p>
</dl>
<p> Note that the JAR file name is included. </p>
<p> Example of specifying the path to the jar file that contains the class file:</p>
<dl>
<dd><i>-altsignerpath /home/user/classes/com/sun/tools/jarsigner/</i> </p>
</dl>
<p> Note that the JAR file name is omitted.</dl>
<h2>Examples</h2>
<h3>Signing a JAR File</h3>
<dl>
<dd>Suppose you have a JAR file named &quot;bundle.jar&quot; and you&#8217;d like to sign it using the private key of the user whose keystore alias is &quot;jane&quot; in the keystore named &quot;mystore&quot; in the &quot;working&quot; directory. Suppose the keystore password is &quot;myspass&quot; and the password for <i>jane</i>&#8216;s private key is &quot;j638klm&quot;. You can use the following to sign the JAR file and name the signed JAR file &quot;sbundle.jar&quot;: </p>
<pre><code> jarsigner -keystore /working/mystore -storepass myspass
 -keypass j638klm -signedjar sbundle.jar bundle.jar jane </code></pre>
<p>Note that there is no <i>-sigfile</i> specified in the command above, so the generated .SF and .DSA files to be placed in the signed JAR file will have default names based on the alias name. That is, they will be named <i>JANE.SF</i> and <i>JANE.DSA</i>. </p>
<p> If you want to be prompted for the store password and the private key password, you could shorten the above command to </p>
<pre><code> jarsigner -keystore /working/mystore
 -signedjar sbundle.jar bundle.jar jane </code></pre>
<p>If the keystore to be used is the default keystore (the one named &quot;.keystore&quot; in your home directory), you don&#8217;t need to specify a keystore, as in: </p>
<pre><code> jarsigner -signedjar sbundle.jar bundle.jar jane </code></pre>
<p>Finally, if you want the signed JAR file to simply overwrite the input JAR file (<i>bundle.jar</i>), you don&#8217;t need to specify a <i>-signedjar</i> option: </p>
<pre><code> jarsigner bundle.jar jane </code></pre>
</dl>
<h3>Verifying a Signed JAR File</h3>
<dl>
<dd>To verify a signed JAR file, that is, to verify that the signature is valid and the JAR file has not been tampered with, use a command such as the following: </p>
<pre><code> jarsigner -verify sbundle.jar </code></pre>
<p>If the verification is successful, </p>
<pre><code> jar verified.</code></pre>
<p>is displayed. Otherwise, an error message appears. </p>
<p> You can get more information if you use the <i>-verbose</i> option. A sample use of <code>jarsigner</code> with the <i>-verbose</i> option is shown below, along with sample output: </p>
<pre><code> jarsigner -verify -verbose sbundle.jar
 198 Fri Sep 26 16:14:06 PDT 1997 META-INF/MANIFEST.MF
 199 Fri Sep 26 16:22:10 PDT 1997 META-INF/JANE.SF
 1013 Fri Sep 26 16:22:10 PDT 1997 META-INF/JANE.DSA
 smk 2752 Fri Sep 26 16:12:30 PDT 1997 AclEx.class
 smk 849 Fri Sep 26 16:12:46 PDT 1997 test.class
 s = signature was verified
 m = entry is listed in manifest
 k = at least one certificate was found in keystore
 jar verified.</code></pre>
</dl>
<h3>Verification with Certificate Information</h3>
<p>If you specify the <i>-certs</i> option when verifying, along with the <i>-verify</i> and <i>-verbose</i> options, the output includes certificate information for each signer of the JAR file, including the certificate type, the signer distinguished name information (iff it&#8217;s an X.509 certificate), and, in parentheses, the keystore alias for the signer if the public key certificate in the JAR file matches that in a keystore entry. For example, </p>
<pre><code> jarsigner -keystore /working/mystore -verify -verbose -certs myTest.jar
 198 Fri Sep 26 16:14:06 PDT 1997 META-INF/MANIFEST.MF
 199 Fri Sep 26 16:22:10 PDT 1997 META-INF/JANE.SF
 1013 Fri Sep 26 16:22:10 PDT 1997 META-INF/JANE.DSA
 208 Fri Sep 26 16:23:30 PDT 1997 META-INF/JAVATEST.SF
 1087 Fri Sep 26 16:23:30 PDT 1997 META-INF/JAVATEST.DSA
 smk 2752 Fri Sep 26 16:12:30 PDT 1997 Tst.class
 X.509, CN=Test Group, OU=Java Software, O=Sun Microsystems, L=CUP, S=CA, C=US (javatest)
 X.509, CN=Jane Smith, OU=Java Software, O=Sun, L=cup, S=ca, C=us (jane)
 s = signature was verified
 m = entry is listed in manifest
 k = at least one certificate was found in keystore
 jar verified.</code></pre>
<p>If the certificate for a signer is not an X.509 certificate, there is no distinguished name information. In that case, just the certificate type and the alias are shown. For example, if the certificate is a PGP certificate, and the alias is &quot;bob&quot;, you&#8217;d get </p>
<pre><code> PGP, (bob)</code></pre>
<h3>Verification of a JAR File that Includes Identity Database Signers</h3>
<p>If a JAR file has been signed using the JDK 1.1 <code>javakey</code> tool, and thus the signer is an alias in an identity database, the verification output includes an &quot;i&quot; symbol. If the JAR file has been signed by both an alias in an identity database and an alias in a keystore, both &quot;k&quot; and &quot;i&quot; appear. </p>
<p> When the <i>-certs</i> option is used, any identity database aliases are shown in square brackets rather than the parentheses used for keystore aliases. For example: </p>
<pre><code> jarsigner -keystore /working/mystore -verify -verbose -certs writeFile.jar
 198 Fri Sep 26 16:14:06 PDT 1997 META-INF/MANIFEST.MF
 199 Fri Sep 26 16:22:10 PDT 1997 META-INF/JANE.SF
 1013 Fri Sep 26 16:22:10 PDT 1997 META-INF/JANE.DSA
 199 Fri Sep 27 12:22:30 PDT 1997 META-INF/DUKE.SF
 1013 Fri Sep 27 12:22:30 PDT 1997 META-INF/DUKE.DSA
 smki 2752 Fri Sep 26 16:12:30 PDT 1997 writeFile.html
 X.509, CN=Jane Smith, OU=Java Software, O=Sun, L=cup, S=ca, C=us (jane)
 X.509, CN=Duke, OU=Java Software, O=Sun, L=cup, S=ca, C=us [duke]
 s = signature was verified
 m = entry is listed in manifest
 k = at least one certificate was found in keystore
 i = at least one certificate was found in identity scope
 jar verified.</code></pre>
<p>Note that the alias &quot;duke&quot; is in brackets to denote that it is an identity database alias, not a keystore alias. </p>
<h2>See Also</h2>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>jar tool documentation</p>
<dt>o</p>
<dd>keytool tool documentation</p>
<dt>o</p>
<dd>the <tt>Security</tt> @ <a rel="nofollow" href="http://java.sun.com/docs/books/tutorial/security1.2/index.html">http://java.sun.com/docs/books/tutorial/security1.2/index.html</a> trail of the <tt>Java Tutorial</tt> @ <a rel="nofollow" href="http://java.sun.com/docs/books/tutorial/trailmap.html">http://java.sun.com/docs/books/tutorial/trailmap.html</a> for examples of the use of the <code>jarsigner</code> tool</dl>
</dl>
<p>&nbsp;<wbr></p>
