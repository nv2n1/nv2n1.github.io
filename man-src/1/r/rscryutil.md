---
title: "rscryutil(1)"
name: "rscryutil"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rscryutil/"
description: "rscryutil – Manage Encrypted Log Files"
---

<h2>NAME</h2>
<p> rscryutil &#8211; Manage Encrypted Log Files</p>
<h2>SYNOPSIS</h2>
<pre><code>
rscryutil[OPTIONS][FILE]...
</code></pre>
<h2>DESCRIPTION</h2>
<p> This tool performs various operations on encrypted log files. Most importantly, it provides the ability to decrypt them.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>,<code> &#8211;decrypt</code></p>
<dd> Select decryption mode. This is the default mode.</p>
<dt><code>-W</code>,<i>&#8211;write-keyfile</i><code>&nbsp;<wbr>&lt;file&gt;</code></p>
<dd> Utility function to write a key to a keyfile. The key can be obtained via any method.</p>
<dt><code>-v</code>,<code> &#8211;verbose</code></p>
<dd> Select verbose mode.</p>
<dt><code>-f</code>,<code> &#8211;force</code></p>
<dd> Forces operations that otherwise would fail.</p>
<dt><code>-k</code>,<i>&#8211;keyfile</i><code>&nbsp;<wbr>&lt;file&gt;</code></p>
<dd> Reads the key from &lt;file&gt;. File _must_ contain the key, only, no headers or other meta information. Keyfiles can be generated via the <i>&#8211;write-keyfile</i> option.</p>
<dt><code>-p</code>,<i>&#8211;key-program</i><code>&nbsp;<wbr>&lt;path-to-program&gt;</code></p>
<dd> In this mode, the key is provided by a so-called &quot;key program&quot;. This program is executed and must return the key to (as well as some meta information) via stdout. The core idea of key programs is that using this interface the user can implement as complex (and secure) method to obtain keys as desired, all without the need to make modifications to rsyslog.</p>
<dt><code>-K</code>,<i>&#8211;key</i><code>&nbsp;<wbr>&lt;KEY&gt;</code></p>
<dd> TESTING AID, NOT FOR PRODUCTION USE. This uses the KEY specified on the command line. This is the actual key, and as such this mode is highly insecure. However, it can be useful for intial testing steps. This option may be removed in the future.</p>
<dt><code>-a</code>,<i>&#8211;algo</i><code>&nbsp;<wbr>&lt;algo&gt;</code></p>
<dd> Sets the encryption algorightm (cipher) to be used. See below for supported algorithms. The default is &quot;AES128&quot;.</p>
<dt><code>-m</code>,<i>&#8211;mode</i><code>&nbsp;<wbr>&lt;mode&gt;</code></p>
<dd> Sets the ciphermode to be used. See below for supported modes. The default is &quot;CBC&quot;.</p>
<dt><code>-r</code>,<i>&#8211;generate-random-key</i><code>&nbsp;<wbr>&lt;bytes&gt;</code></p>
<dd> Generates a random key of length &lt;bytes&gt;. This option is meant to be used together with <i>&#8211;write-keyfile</i> (and it is hard to envision any other valid use for it).</dl>
<h2>OPERATION MODES</h2>
<p> The operation mode specifies what exactly the tool does with the provided files. The default operation mode is &quot;dump&quot;, but this may change in the future. Thus, it is recommended to always set the operations mode explicitely. If multiple operations mode are set on the command line, results are unpredictable.</p>
<h3>decrypt</h3>
<p> The provided log files are decrypted. Note that the <i>.encinfo</i> side files must exist and be accessible in order for decryption to to work.</p>
<h3>write-keyfile</h3>
<p> In this mode no log files are processed; thus it is an error to specify any on the command line. The specified keyfile is written. The key itself is obtained via the usual key commands. If <i>&#8211;keyfile</i> is used, that file is effectively copied. </p>
<p> For security reasons, existing key files are _not_ overwritten. To permit this, specify the <i>&#8211;force</i> option. When doing so, keep in mind that lost keys cannot be recovered and data encrypted with them may also be considered lost. </p>
<p> Keyfiles are always created with 0400 permission, that is read access for only the user. An exception is when an existing file is overwritten via the <i>&#8211;force</i> option, in which case the former permissions still apply.</p>
<h2>EXIT CODES</h2>
<p> The command returns an exit code of 0 if everything went fine, and some other code in case of failures.</p>
<h2>SUPPORTED ALGORITHMS</h2>
<p> We basically support what libgcrypt supports. This is: 3DES CAST5 BLOWFISH AES128 AES192 AES256 TWOFISH TWOFISH128 ARCFOUR DES SERPENT128 SERPENT192 SERPENT256 RFC2268_40 SEED CAMELLIA128 CAMELLIA192 CAMELLIA256</p>
<h2>SUPPORTED CIPHER MODES</h2>
<p> We basically support what libgcrypt supports. This is: ECB CFB CBC STREAM OFB CTR AESWRAP</p>
<h2>EXAMPLES</h2>
<p> <code>rscryutil logfile</code> </p>
<p> Decrypts &quot;logfile&quot; and sends data to stdout. </p>
<p> <code>rscryutil &#8211;generate-random-key 16 &#8211;keyfile /some/secured/path/keyfile</code> </p>
<p> Generates random key and stores it in the specified keyfile.</p>
<h2>LOG SIGNATURES</h2>
<p> Encrypted log files can be used together with signing. To verify such a file, it must be decrypted first, and the verification tool <code><a href="/docs/linux/man/1-rsgtutil/">rsgtutil</a>(1)</code> must be run on the decrypted file.</p>
<h2>SECURITY CONSIDERATIONS</h2>
<p> Specifying keys directly on the command line (<i>&#8211;key</i> option) is very insecure and should not be done, except for testing purposes with test keys. Even then it is recommended to use keyfiles, which are also easy to handle during testing. Keep in mind that command history is usally be kept by bash and can also easily be monitored. </p>
<p> Local keyfiles are also a security risk. At a minimum, they should be used with very restrictive file permissions. For this reason, the <i>rscryutil</i> tool creates them with read permissions for the user, only, no matter what umask is set to. </p>
<p> When selecting cipher algorithms and modes, care needs to be taken. The defaults should be reasonable safe to use, but this tends to change over time. Keep up with the most current crypto recommendations.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rsgtutil/">rsgtutil</a>(1)</code>, <code><a href="/docs/linux/man/8-rsyslogd/">rsyslogd</a>(8)</code></p>
<h2>COPYRIGHT</h2>
<p> This page is part of the <i>rsyslog</i> project, and is available under LGPLv2.</p>
<h2>AUTHOR</h2>
<p> Rainer Gerhards &lt;rgerhards [at] adiscon.com&gt; </p>
<h2>Index</h2>
