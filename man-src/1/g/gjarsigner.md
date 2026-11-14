---
title: "gjarsigner(1)"
name: "gjarsigner"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gjarsigner/"
description: "gjarsigner – Java ARchive (JAR) file signing and verification tool"
---

<h2 class="name">NAME</h2>
<p> gjarsigner &#8211; Java ARchive (JAR) file signing and verification tool </p>
<h2>SYNOPSIS</h2>
<p> jarsigner [<i></i><font SIZE="-1"><i>OPTION</i></font><i></i>]&#8230; <i></i><font SIZE="-1"><i>FILE</i></font><i></i> <i></i><font SIZE="-1"><i>ALIAS</i></font><i></i> </p>
<p> jarsigner <code>-verify</code> [<i></i><font SIZE="-1"><i>OPTION</i></font><i></i>]&#8230; <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<h2>DESCRIPTION</h2>
<p> When the first form is used, the tool signs the designated <font SIZE="-1">JAR</font> file. The second form, on the other hand, is used to verify a previously signed <font SIZE="-1">JAR</font> file. </p>
<p> <i></i><font SIZE="-1"><i>FILE</i></font><i></i> is the .JAR file to process; i.e., to sign if the first syntax form is used, or to verify if the second syntax form is used instead. </p>
<p> <i></i><font SIZE="-1"><i>ALIAS</i></font><i></i> must be a known <i>Alias</i> of a <i>Key Entry</i> in the designated <i>Key Store</i>. The private key material associated with this <i>Alias</i> is then used for signing the designated .JAR file.</p>
<h2>OPTIONS</h2>
<p> <i>Common options</i> </p>
<p> The following options may be used when the tool is used for either signing, or verifying, a .JAR file.</p>
<dl>
<dt><code>-verbose</code></p>
<dd> Use this option to force the tool to generate more verbose messages, during its processing.</p>
<dt><code>-internalsf</code></p>
<dd> When present, the tool will include &#8211;which otherwise it does not&#8212; the <tt>&quot;.SF&quot;</tt> file in the <tt>&quot;.DSA&quot;</tt> generated file.</p>
<dt><code>-sectionsonly</code></p>
<dd> When present, the tool will include in the <tt>&quot;.SF&quot;</tt> generated file &#8211;which otherwise it does not&#8212; a header containing a hash of the whole manifest file. When that header is included, the tool can quickly check, during verification, if the hash (in the header) matches or not the manifest file.</p>
<dt><code>-provider </code><font SIZE="-1"><code>PROVIDER_CLASS_NAME</code></font></p>
<dd> A fully qualified class name of a <i>Security Provider</i> to add to the current list of <i>Security Providers</i> already installed in the <font SIZE="-1">JVM</font> in-use. If a provider class is specified with this option, and was successfully added to the runtime &#8211;i.e. it was not already installed&#8212; then the tool will attempt to remove this <i>Security Provider</i> before exiting.</p>
<dt><code>-help</code></p>
<dd> Prints a help text similar to this one.</dl>
<p> <i>Signing options</i> </p>
<p> The following options may be specified when using the tool for signing purposes.</p>
<dl>
<dt><code>-keystore</code> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd> Use this option to specify the location of the key store to use. The default value is a file <font SIZE="-1">URL</font> referencing the file named <i>.keystore</i> located in the path returned by the call to <tt>&quot;java.lang.System#getProperty(String)&quot;</tt> using <tt>&quot;user.home&quot;</tt> as argument. </p>
<p> If a <font SIZE="-1">URL</font> was specified, but was found to be malformed &#8211;e.g. missing protocol element&#8212; the tool will attempt to use the <font SIZE="-1">URL</font> value as a file-name (with absolute or relative path-name) of a key store &#8211;as if the protocol was <tt>&quot;file:&quot;</tt>.</p>
<dt><code>-storetype</code> <i></i><font SIZE="-1"><i>STORE_TYPE</i></font><i></i></p>
<dd> Use this option to specify the type of the key store to use. The default value, if this option is omitted, is that of the property <tt>&quot;keystore.type&quot;</tt> in the security properties file, which is obtained by invoking the static method call <tt>&quot;getDefaultType()&quot;</tt> in <tt>&quot;java.security.KeyStore&quot;</tt>.</p>
<dt><code>-storepass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> Use this option to specify the password which will be used to unlock the key store. If this option is missing, the User will be prompted to provide a password.</p>
<dt><code>-keypass</code> <i></i><font SIZE="-1"><i>PASSWORD</i></font><i></i></p>
<dd> Use this option to specify the password which the tool will use to unlock the <i>Key Entry</i> associated with the designated <i>Alias</i>. </p>
<p> If this option is omitted, the tool will first attempt to unlock the <i>Key Entry</i> using the same password protecting the key store. If this fails, you will then be prompted to provide a password.</p>
<dt><code>-sigfile</code> <i></i><font SIZE="-1"><i>NAME</i></font><i></i></p>
<dd> Use this option to designate a literal that will be used to construct file names for both the <tt>&quot;.SF&quot;</tt> and <tt>&quot;.DSA&quot;</tt> signature files. These files will be generated, by the tool, and placed in the <i>META-INF</i> directory of the signed <font SIZE="-1">JAR</font>. Permissible characters for <i></i><font SIZE="-1"><i>NAME</i></font><i></i> must be in the range &#8220;a-zA-Z0-9_-&#8221;. All characters will be converted to upper-case ones. </p>
<p> If this option is missing, the first eight characters of the <i></i><font SIZE="-1"><i>ALIAS</i></font><i></i> argument will be used. When this is the case, any character in <i></i><font SIZE="-1"><i>ALIAS</i></font><i></i> that is outside the permissible range of characters will be replaced by an underscore.</p>
<dt><code>-signedjar</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Use this option to specify the file name of the signed <font SIZE="-1">JAR</font>. If this option is omitted, then the signed <font SIZE="-1">JAR</font> will be named the same as <i></i><font SIZE="-1"><i>FILE</i></font><i></i>; i.e., the input <font SIZE="-1">JAR</font> file will be replaced with the signed copy.</dl>
<p> <i>Verification options</i> </p>
<p> The following options may be specified when using the tool for verification purposes.</p>
<dl>
<dt><code>-verify</code></p>
<dd> Use this option to indicate that the tool is to be used for verification purposes.</p>
<dt><code>-certs</code></p>
<dd> This option is used in conjunction with the <code>-verbose</code> option. When present, along with the <code>-verbose</code> option, the tool will print more detailed information about the certificates of the signer(s) being processed.</dl>
<h2>BUGS</h2>
<h2>SEE ALSO</h2>
<h2>AUTHOR</h2>
<h2>Index</h2>
