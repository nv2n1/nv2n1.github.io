---
title: "signtool(1)"
name: "signtool"
section: "1"
letter: "s"
url: "/docs/linux/man/1-signtool/"
description: "signtool – Digitally sign objects and files."
---

<h2 class="name">NAME</h2>
<p> signtool &#8211; Digitally sign objects and files. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>signtool</code> [[-b basename]] [[-c Compression Level]] [[-d cert-dir]] [[-e extension]] [[-f filename]] [[-i installer script]] [[-h]] [[-H]] [[-v]] [[-w]] [[-G nickname]] [[-J]] [[-j directory]] [-k keyName] [[&#8211;keysize | -s size]] [[-l]] [[-L]] [[-M]] [[-m metafile]] [[&#8211;norecurse]] [[-O]] [[-o]] [[&#8211;outfile]] [[-p password]] [[-t|&#8211;token tokenname]] [[-z]] [[-X]] [[-x name]] [[&#8211;verbose value]] [[&#8211;leavearc]] [[-Z jarfile]] [directory-tree] [archive]</dl>
<h2>STATUS</h2>
<dd>This documentation is still work in progress. Please contribute to the initial review in m[blue]<code>Mozilla NSS bug 836477</code>m[]<font SIZE="-2">[1]</font></p>
<h2>DESCRIPTION</h2>
<p> The Signing Tool, <code>signtool</code>, creates digital signatures and uses a Java Archive (JAR) file to associate the signatures with files in a directory. Electronic software distribution over any network involves potential security problems. To help address some of these problems, you can associate digital signatures with the files in a JAR archive. Digital signatures allow SSL-enabled clients to perform two important operations: </p>
<p> * Confirm the identity of the individual, company, or other entity whose digital signature is associated with the files </p>
<p> * Check whether the files have been tampered with since being signed </p>
<p> If you have a signing certificate, you can use Netscape Signing Tool to digitally sign files and package them as a JAR file. An object-signing certificate is a special kind of certificate that allows you to associate your digital signature with one or more files. </p>
<p> An individual file can potentially be signed with multiple digital signatures. For example, a commercial software developer might sign the files that constitute a software product to prove that the files are indeed from a particular company. A network administrator manager might sign the same files with an additional digital signature based on a company-generated certificate to indicate that the product is approved for use within the company. </p>
<p> The significance of a digital signature is comparable to the significance of a handwritten signature. Once you have signed a file, it is difficult to claim later that you didn&#8217;t sign it. In some situations, a digital signature may be considered as legally binding as a handwritten signature. Therefore, you should take great care to ensure that you can stand behind any file you sign and distribute. </p>
<p> For example, if you are a software developer, you should test your code to make sure it is virus-free before signing it. Similarly, if you are a network administrator, you should make sure, before signing any code, that it comes from a reliable source and will run correctly with the software installed on the machines to which you are distributing it. </p>
<p> Before you can use Netscape Signing Tool to sign files, you must have an object-signing certificate, which is a special certificate whose associated private key is used to create digital signatures. For testing purposes only, you can create an object-signing certificate with Netscape Signing Tool 1.3. When testing is finished and you are ready to disitribute your software, you should obtain an object-signing certificate from one of two kinds of sources: </p>
<p> * An independent certificate authority (CA) that authenticates your identity and charges you a fee. You typically get a certificate from an independent CA if you want to sign software that will be distributed over the Internet. </p>
<p> * CA server software running on your corporate intranet or extranet. Netscape Certificate Management System provides a complete management solution for creating, deploying, and managing certificates, including CAs that issue object-signing certificates. </p>
<p> You must also have a certificate for the CA that issues your signing certificate before you can sign files. If the certificate authority&#8217;s certificate isn&#8217;t already installed in your copy of Communicator, you typically install it by clicking the appropriate link on the certificate authority&#8217;s web site, for example on the page from which you initiated enrollment for your signing certificate. This is the case for some test certificates, as well as certificates issued by Netscape Certificate Management System: you must download the the CA certificate in addition to obtaining your own signing certificate. CA certificates for several certificate authorities are preinstalled in the Communicator certificate database. </p>
<p> When you receive an object-signing certificate for your own use, it is automatically installed in your copy of the Communicator client software. Communicator supports the public-key cryptography standard known as PKCS #12, which governs key portability. You can, for example, move an object-signing certificate and its associated private key from one computer to another on a credit-card-sized device called a smart card.</p>
<h2>OPTIONS</h2>
<p> -b basename</p>
<dl>
<dt>
<dd> Specifies the base filename for the .rsa and .sf files in the META-INF directory to conform with the JAR format. For example, <i>-b signatures</i> causes the files to be named signatures.rsa and signatures.sf. The default is signtool.</dl>
<p> -c#</p>
<dl>
<dt>
<dd> Specifies the compression level for the -J or -Z option. The symbol # represents a number from 0 to 9, where 0 means no compression and 9 means maximum compression. The higher the level of compression, the smaller the output but the longer the operation takes. If the -c# option is not used with either the -J or the -Z option, the default compression value used by both the -J and -Z options is 6.</dl>
<p> -d certdir</p>
<dl>
<dt>
<dd> Specifies your certificate database directory; that is, the directory in which you placed your key3.db and cert7.db files. To specify the current directory, use &quot;-d.&quot; (including the period). The Unix version of signtool assumes ~/.netscape unless told otherwise. The NT version of signtool always requires the use of the -d option to specify where the database files are located.</dl>
<p> -e extension</p>
<dl>
<dt>
<dd> Tells signtool to sign only files with the given extension; for example, use -e&quot;.class&quot; to sign only Java class files. Note that with Netscape Signing Tool version 1.1 and later this option can appear multiple times on one command line, making it possible to specify multiple file types or classes to include.</dl>
<p> -f commandfile</p>
<dl>
<dt>
<dd> Specifies a text file containing Netscape Signing Tool options and arguments in keyword=value format. All options and arguments can be expressed through this file. For more information about the syntax used with this file, see &quot;Tips and Techniques&quot;.</dl>
<p> -G nickname</p>
<dl>
<dt>
<dd> Generates a new private-public key pair and corresponding object-signing certificate with the given nickname. The newly generated keys and certificate are installed into the key and certificate databases in the directory specified by the -d option. With the NT version of Netscape Signing Tool, you must use the -d option with the -G option. With the Unix version of Netscape Signing Tool, omitting the -d option causes the tool to install the keys and certificate in the Communicator key and certificate databases. If you are installing the keys and certificate in the Communicator databases, you must exit Communicator before using this option; otherwise, you risk corrupting the databases. In all cases, the certificate is also output to a file named x509.cacert, which has the MIME-type application/x-x509-ca-cert. Unlike certificates normally used to sign finished code to be distributed over a network, a test certificate created with -G is not signed by a recognized certificate authority. Instead, it is self-signed. In addition, a single test signing certificate functions as both an object-signing certificate and a CA. When you are using it to sign objects, it behaves like an object-signing certificate. When it is imported into browser software such as Communicator, it behaves like an object-signing CA and cannot be used to sign objects. The -G option is available in Netscape Signing Tool 1.0 and later versions only. By default, it produces only RSA certificates with 1024-byte keys in the internal token. However, you can use the -s option specify the required key size and the -t option to specify the token.</dl>
<p> -i scriptname</p>
<dl>
<dt>
<dd> Specifies the name of an installer script for SmartUpdate. This script installs files from the JAR archive in the local system after SmartUpdate has validated the digital signature. For more details, see the description of -m that follows. The -i option provides a straightforward way to provide this information if you don&#8217;t need to specify any metadata other than an installer script.</dl>
<p> -J</p>
<dl>
<dt>
<dd> Signs a directory of HTML files containing JavaScript and creates as many archive files as are specified in the HTML tags. Even if signtool creates more than one archive file, you need to supply the key database password only once. The -J option is available only in Netscape Signing Tool 1.0 and later versions. The -J option cannot be used at the same time as the -Z option. If the -c# option is not used with the -J option, the default compression value is 6. Note that versions 1.1 and later of Netscape Signing Tool correctly recognizes the CODEBASE attribute, allows paths to be expressed for the CLASS and SRC attributes instead of filenames only, processes LINK tags and parses HTML correctly, and offers clearer error messages.</dl>
<p> -j directory</p>
<dl>
<dt>
<dd> Specifies a special JavaScript directory. This option causes the specified directory to be signed and tags its entries as inline JavaScript. This special type of entry does not have to appear in the JAR file itself. Instead, it is located in the HTML page containing the inline scripts. When you use signtool -v, these entries are displayed with the string NOT PRESENT.</dl>
<p> -k key &#8230; directory</p>
<dl>
<dt>
<dd> Specifies the nickname (key) of the certificate you want to sign with and signs the files in the specified directory. The directory to sign is always specified as the last command-line argument. Thus, it is possible to write signtool -k MyCert -d . signdir You may have trouble if the nickname contains a single quotation mark. To avoid problems, escape the quotation mark using the escape conventions for your platform. It&#8217;s also possible to use the -k option without signing any files or specifying a directory. For example, you can use it with the -l option to get detailed information about a particular signing certificate.</dl>
<p> -l</p>
<dl>
<dt>
<dd> Lists signing certificates, including issuing CAs. If any of your certificates are expired or invalid, the list will so specify. This option can be used with the -k option to list detailed information about a particular signing certificate. The -l option is available in Netscape Signing Tool 1.0 and later versions only.</dl>
<p> -L</p>
<dl>
<dt>
<dd> Lists the certificates in your database. An asterisk appears to the left of the nickname for any certificate that can be used to sign objects with signtool.</dl>
<p> &#8211;leavearc</p>
<dl>
<dt>
<dd> Retains the temporary .arc (archive) directories that the -J option creates. These directories are automatically erased by default. Retaining the temporary directories can be an aid to debugging.</dl>
<p> -m metafile</p>
<dl>
<dt>
<dd> Specifies the name of a metadata control file. Metadata is signed information attached either to the JAR archive itself or to files within the archive. This metadata can be any ASCII string, but is used mainly for specifying an installer script. The metadata file contains one entry per line, each with three fields: field #1: file specification, or + if you want to specify global metadata (that is, metadata about the JAR archive itself or all entries in the archive) field #2: the name of the data you are specifying; for example: Install-Script field #3: data corresponding to the name in field #2 For example, the -i option uses the equivalent of this line: + Install-Script: script.js This example associates a MIME type with a file: movie.qt MIME-Type: video/quicktime For information about the way installer script information appears in the manifest file for a JAR archive, see The JAR Format on Netscape DevEdge.</dl>
<p> -M</p>
<dl>
<dt>
<dd> Lists the PKCS #11 modules available to signtool, including smart cards. The -M option is available in Netscape Signing Tool 1.0 and later versions only. For information on using Netscape Signing Tool with smart cards, see &quot;Using Netscape Signing Tool with Smart Cards&quot;. For information on using the -M option to verify FIPS-140-1 validated mode, see &quot;Netscape Signing Tool and FIPS-140-1&quot;.</dl>
<p> &#8211;norecurse</p>
<dl>
<dt>
<dd> Blocks recursion into subdirectories when signing a directory&#8217;s contents or when parsing HTML.</dl>
<p> -o</p>
<dl>
<dt>
<dd> Optimizes the archive for size. Use this only if you are signing very large archives containing hundreds of files. This option makes the manifest files (required by the JAR format) considerably smaller, but they contain slightly less information.</dl>
<p> &#8211;outfile outputfile</p>
<dl>
<dt>
<dd> Specifies a file to receive redirected output from Netscape Signing Tool.</dl>
<p> -p password</p>
<dl>
<dt>
<dd> Specifies a password for the private-key database. Note that the password entered on the command line is displayed as plain text.</dl>
<p> -s keysize</p>
<dl>
<dt>
<dd> Specifies the size of the key for generated certificate. Use the -M option to find out what tokens are available. The -s option can be used with the -G option only.</dl>
<p> -t token</p>
<dl>
<dt>
<dd> Specifies which available token should generate the key and receive the certificate. Use the -M option to find out what tokens are available. The -t option can be used with the -G option only.</dl>
<p> -v archive</p>
<dl>
<dt>
<dd> Displays the contents of an archive and verifies the cryptographic integrity of the digital signatures it contains and the files with which they are associated. This includes checking that the certificate for the issuer of the object-signing certificate is listed in the certificate database, that the CA&#8217;s digital signature on the object-signing certificate is valid, that the relevant certificates have not expired, and so on.</dl>
<p> &#8211;verbosity value</p>
<dl>
<dt>
<dd> Sets the quantity of information Netscape Signing Tool generates in operation. A value of 0 (zero) is the default and gives full information. A value of -1 suppresses most messages, but not error messages.</dl>
<p> -w archive</p>
<dl>
<dt>
<dd> Displays the names of signers of any files in the archive.</dl>
<p> -x directory</p>
<dl>
<dt>
<dd> Excludes the specified directory from signing. Note that with Netscape Signing Tool version 1.1 and later this option can appear multiple times on one command line, making it possible to specify several particular directories to exclude.</dl>
<p> -z</p>
<dl>
<dt>
<dd> Tells signtool not to store the signing time in the digital signature. This option is useful if you want the expiration date of the signature checked against the current date and time rather than the time the files were signed.</dl>
<p> -Z jarfile</p>
<dl>
<dt>
<dd> Creates a JAR file with the specified name. You must specify this option if you want signtool to create the JAR file; it does not do so automatically. If you don&#8217;t specify -Z, you must use an external ZIP tool to create the JAR file. The -Z option cannot be used at the same time as the -J option. If the -c# option is not used with the -Z option, the default compression value is 6.</dl>
<h2>THE COMMAND FILE FORMAT</h2>
<p> Entries in a Netscape Signing Tool command file have this general format: keyword=value Everything before the = sign on a single line is a keyword, and everything from the = sign to the end of line is a value. The value may include = signs; only the first = sign on a line is interpreted. Blank lines are ignored, but white space on a line with keywords and values is assumed to be part of the keyword (if it comes before the equal sign) or part of the value (if it comes after the first equal sign). Keywords are case insensitive, values are generally case sensitive. Since the = sign and newline delimit the value, it should not be quoted. </p>
<p> <code>Subsection</code> </p>
<p> basename</p>
<dl>
<dt>
<dd> Same as -b option.</dl>
<p> compression</p>
<dl>
<dt>
<dd> Same as -c option.</dl>
<p> certdir</p>
<dl>
<dt>
<dd> Same as -d option.</dl>
<p> extension</p>
<dl>
<dt>
<dd> Same as -e option.</dl>
<p> generate</p>
<dl>
<dt>
<dd> Same as -G option.</dl>
<p> installscript</p>
<dl>
<dt>
<dd> Same as -i option.</dl>
<p> javascriptdir</p>
<dl>
<dt>
<dd> Same as -j option.</dl>
<p> htmldir</p>
<dl>
<dt>
<dd> Same as -J option.</dl>
<p> certname</p>
<dl>
<dt>
<dd> Nickname of certificate, as with -k and -l -k options.</dl>
<p> signdir</p>
<dl>
<dt>
<dd> The directory to be signed, as with -k option.</dl>
<p> list</p>
<dl>
<dt>
<dd> Same as -l option. Value is ignored, but = sign must be present.</dl>
<p> listall</p>
<dl>
<dt>
<dd> Same as -L option. Value is ignored, but = sign must be present.</dl>
<p> metafile</p>
<dl>
<dt>
<dd> Same as -m option.</dl>
<p> modules</p>
<dl>
<dt>
<dd> Same as -M option. Value is ignored, but = sign must be present.</dl>
<p> optimize</p>
<dl>
<dt>
<dd> Same as -o option. Value is ignored, but = sign must be present.</dl>
<p> password</p>
<dl>
<dt>
<dd> Same as -p option.</dl>
<p> keysize</p>
<dl>
<dt>
<dd> Same as -s option.</dl>
<p> token</p>
<dl>
<dt>
<dd> Same as -t option.</dl>
<p> verify</p>
<dl>
<dt>
<dd> Same as -v option.</dl>
<p> who</p>
<dl>
<dt>
<dd> Same as -w option.</dl>
<p> exclude</p>
<dl>
<dt>
<dd> Same as -x option.</dl>
<p> notime</p>
<dl>
<dt>
<dd> Same as -z option. value is ignored, but = sign must be present.</dl>
<p> jarfile</p>
<dl>
<dt>
<dd> Same as -Z option.</dl>
<p> outfile</p>
<dl>
<dt>
<dd> Name of a file to which output and error messages will be redirected. This option has no command-line equivalent.</dl>
<h2>EXTENDED EXAMPLES</h2>
<p> The following example will do this and that </p>
<p> <code>Listing Available Signing Certificates</code> </p>
<p> You use the -L option to list the nicknames for all available certificates and check which ones are signing certificates. </p>
<dl>
<dt>
<dd>
<pre><code>
signtool - L using certificate directory : / u / jsmith /.netscape S Certificates - -- -- -- -- -- --BBN Certificate Services CA Root 1 IBM World Registry CA VeriSign Class 1 CA - Individual Subscriber - VeriSign, Inc.GTE CyberTrust Root CA
                                                                                                                                                                                                                              Uptime Group Plc.Class 4 CA
                                                                                                                                                                                                                                  *Verisign Object Signing Cert
                                                                                                                                                                                                                                      Integrion CA
                                                                                                                                                                                                                                          GTE CyberTrust Secure Server CA
                                                                                                                                                                                                                                              AT &amp;T Directory Services
                                                                                                                                                                                                                                                  *test object signing cert
                                                                                                                                                                                                                                                      Uptime Group Plc.Class 1 CA
                                                                                                                                                                                                                                                          VeriSign Class 1 Primary CA -
                                                                                                                                                                                                                          -- -- -- -- -- --Certificates that can be used to sign objects have *'s to their left. 
</code></pre>
</dl>
<p> Two signing certificates are displayed: Verisign Object Signing Cert and test object signing cert. </p>
<p> You use the -l option to get a list of signing certificates only, including the signing CA for each. </p>
<dl>
<dt>
<dd>
signtool &#8211; l using certificate directory : / u / jsmith /.netscape Object signing certificates&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -Verisign Object Signing Cert Issued by : VeriSign, Inc.- Verisign, Inc.Expires : Tue May 19, 1998 test object signing cert Issued by : test object signing cert(Signtool 1.0 Testing Certificate(960187691)) Expires : Sun May 17, 1998 &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;
</dl>
<p> For a list including CAs, use the <code>-L</code> option. </p>
<p> <code>Signing a File</code> </p>
<p> 1. Create an empty directory. </p>
<dl>
<dt>
<dd>
<pre>
mkdir signdir
</pre>
</dl>
<p> 2. Put some file into it. </p>
<dl>
<dt>
<dd>
<pre>
echo boo &gt; signdir/test.f
</pre>
</dl>
<p> 3. Specify the name of your object-signing certificate and sign the directory. </p>
<dl>
<dt>
<dd>
<pre>
signtool -k MySignCert -Z testjar.jar signdir
using key &quot;MySignCert&quot;
using certificate directory: /u/jsmith/.netscape
Generating signdir/META-INF/manifest.mf file..
--&gt; test.f
adding signdir/test.f to testjar.jar
Generating signtool.sf file..
Enter Password or Pin for &quot;Communicator Certificate DB&quot;:
adding signdir/META-INF/manifest.mf to testjar.jar
adding signdir/META-INF/signtool.sf to testjar.jar
adding signdir/META-INF/signtool.rsa to testjar.jar
tree &quot;signdir&quot; signed successfully
</pre>
</dl>
<p> 4. Test the archive you just created. </p>
<dl>
<dt>
<dd>
signtool &#8211; v testjar.jar using certificate directory : / u / jsmith /.netscape archive &#8220;testjar.jar&#8221; has passed crypto verification.status path&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -verified test.f
</dl>
<p> <code>Using Netscape Signing Tool with a ZIP Utility</code> </p>
<p> To use Netscape Signing Tool with a ZIP utility, you must have the utility in your path environment variable. You should use the zip.exe utility rather than pkzip.exe, which cannot handle long filenames. You can use a ZIP utility instead of the -Z option to package a signed archive into a JAR file after you have signed it: </p>
<dl>
<dt>
<dd>
<pre>
cd signdir 
  zip -r ../myjar.jar * 
  adding: META-INF/ (stored 0%) 
  adding: META-INF/manifest.mf (deflated 15%) 
  adding: META-INF/signtool.sf (deflated 28%) 
  adding: META-INF/signtool.rsa (stored 0%) 
  adding: text.txt (stored 0%)
</pre>
</dl>
<p> <code>Generating the Keys and Certificate</code> </p>
<p> The signtool option -G generates a new public-private key pair and certificate. It takes the nickname of the new certificate as an argument. The newly generated keys and certificate are installed into the key and certificate databases in the directory specified by the -d option. With the NT version of Netscape Signing Tool, you must use the -d option with the -G option. With the Unix version of Netscape Signing Tool, omitting the -d option causes the tool to install the keys and certificate in the Communicator key and certificate databases. In all cases, the certificate is also output to a file named x509.cacert, which has the MIME-type application/x-x509-ca-cert. </p>
<p> Certificates contain standard information about the entity they identify, such as the common name and organization name. Netscape Signing Tool prompts you for this information when you run the command with the -G option. However, all of the requested fields are optional for test certificates. If you do not enter a common name, the tool provides a default name. In the following example, the user input is in boldface: </p>
<dl>
<dt>
<dd>
signtool -G MyTestCert<br />
using certificate directory: /u/someuser/.netscape<br />
Enter certificate information. All fields are optional. Acceptable<br />
characters are numbers, letters, spaces, and apostrophes.<br />
certificate common name: Test Object Signing Certificate<br />
organization: Netscape Communications Corp.<br />
organization unit: Server Products Division<br />
state or province: California<br />
country (must be exactly 2 characters): US<br />
username: someuser<br />
email address: someuser [at] netscape.com<br />
Enter Password or Pin for &#8220;Communicator Certificate DB&#8221;: [Password will not echo]<br />
generated public/private key pair<br />
certificate request generated<br />
certificate has been signed<br />
certificate &#8220;MyTestCert&#8221; added to database<br />
Exported certificate to x509.raw and x509.cacert.
</dl>
<p> The certificate information is read from standard input. Therefore, the information can be read from a file using the redirection operator (&lt;) in some operating systems. To create a file for this purpose, enter each of the seven input fields, in order, on a separate line. Make sure there is a newline character at the end of the last line. Then run signtool with standard input redirected from your file as follows: </p>
<dl>
<dt>
<dd>
<pre>
signtool -G MyTestCert inputfile
</pre>
</dl>
<p> The prompts show up on the screen, but the responses will be automatically read from the file. The password will still be read from the console unless you use the -p option to give the password on the command line. </p>
<p> <code>Using the -M Option to List Smart Cards</code> </p>
<p> You can use the -M option to list the PKCS #11 modules, including smart cards, that are available to signtool: </p>
<dl>
<dt>
<dd>
signtool &#8211; d &#8220;c:
etscape
