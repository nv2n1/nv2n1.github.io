---
title: "puttygen(1)"
name: "puttygen"
section: "1"
letter: "p"
url: "/docs/linux/man/1-puttygen/"
description: "puttygen – public-key generator for the PuTTY tools"
---

<h2>NAME</h2>
<p> <code>puttygen</code> &#8211; public-key generator for the PuTTY tools</p>
<h2>SYNOPSIS</h2>
<pre><code>
puttygen &amp;nbsp;
(&amp;nbsp; keyfile &amp; nbsp; | &amp;nbsp; - t &amp; nbsp; keytype &amp; nbsp;[&amp;nbsp; - b &amp; nbsp; bits &amp; nbsp;] &amp; nbsp;) &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
[&amp;nbsp; - C &amp; nbsp; new - comment &amp;nbsp;] &amp; nbsp;
[&amp;nbsp; - P &amp; nbsp;] &amp; nbsp;
[&amp;nbsp; - q &amp; nbsp;] &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
[&amp;nbsp; - O &amp; nbsp; output - type &amp; nbsp; | &amp;nbsp; - l &amp; nbsp; | &amp;nbsp; - L &amp; nbsp; | &amp;nbsp; - p &amp; nbsp;] &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
[&amp;nbsp; - o &amp; nbsp; output - file &amp; nbsp;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>puttygen</code> is a tool to generate and manipulate SSH public and private key pairs. It is part of the PuTTY suite, although it can also interoperate with the private key formats used by some other SSH clients. </p>
<p> When you run <code>puttygen</code>, it does three things. Firstly, it either loads an existing key file (if you specified <i>keyfile</i>), or generates a new key (if you specified <i>keytype</i>). Then, it optionally makes modifications to the key (changing the comment and/or the passphrase); finally, it outputs the key, or some information about the key, to a file. </p>
<p> All three of these phases are controlled by the options described in the following section.</p>
<h2>OPTIONS</h2>
<p> In the first phase, <code>puttygen</code> either loads or generates a key. Note that generating a key requires random data (from <code>/dev/random</code>), which can cause <code>puttygen</code> to pause, possibly for some time if your system does not have much randomness available. </p>
<p> The options to control this phase are:</p>
<dl>
<dt><i>keyfile</i></p>
<dd> Specify a private key file to be loaded. This private key file can be in the (de facto standard) SSH-1 key format, or in PuTTY&#8217;s SSH-2 key format, or in either of the SSH-2 private key formats used by OpenSSH and ssh.com&#8217;s implementation.</p>
<dt><code>-t</code> <i>keytype</i></p>
<dd> Specify a type of key to generate. The acceptable values here are <code>rsa</code> and <code>dsa</code> (to generate SSH-2 keys), and <code>rsa1</code> (to generate SSH-1 keys).</p>
<dt><code>-b</code> <i>bits</i></p>
<dd> Specify the size of the key to generate, in bits. Default is 1024.</p>
<dt><code>-q</code></p>
<dd> Suppress the progress display when generating a new key.</dl>
<p> In the second phase, <code>puttygen</code> optionally alters properties of the key it has loaded or generated. The options to control this are:</p>
<dl>
<dt><code>-C</code> <i>new-comment</i></p>
<dd> Specify a comment string to describe the key. This comment string will be used by PuTTY to identify the key to you (when asking you to enter the passphrase, for example, so that you know which passphrase to type).</p>
<dt><code>-P</code></p>
<dd> Indicate that you want to change the key&#8217;s passphrase. This is automatic when you are generating a new key, but not when you are modifying an existing key.</dl>
<p> In the third phase, <code>puttygen</code> saves the key or information about it. The options to control this are:</p>
<dl>
<dt><code>-O</code> <i>output-type</i></p>
<dd> Specify the type of output you want <code>puttygen</code> to produce. Acceptable options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>private</code></p>
<dd> Save the private key in a format usable by PuTTY. This will either be the standard SSH-1 key format, or PuTTY&#8217;s own SSH-2 key format.</p>
<dt><code>public</code></p>
<dd> Save the public key only. For SSH-1 keys, the standard public key format will be used (`<code>1024 37 5698745</code>&#8230;&#8217;). For SSH-2 keys, the public key will be output in the format specified by RFC 4716, which is a multi-line text file beginning with the line `<code>&#8212;- BEGIN SSH2 PUBLIC KEY &#8212;-</code>&#8216;.</p>
<dt><code>public-openssh</code></p>
<dd> Save the public key only, in a format usable by OpenSSH. For SSH-1 keys, this output format behaves identically to <code>public</code>. For SSH-2 keys, the public key will be output in the OpenSSH format, which is a single line (`<code>ssh-rsa AAAAB3NzaC1yc2</code>&#8230;&#8217;).</p>
<dt><code>fingerprint</code></p>
<dd> Print the fingerprint of the public key. All fingerprinting algorithms are believed compatible with OpenSSH.</p>
<dt><code>private-openssh</code></p>
<dd> Save an SSH-2 private key in OpenSSH&#8217;s format. This option is not permitted for SSH-1 keys.</p>
<dt><code>private-sshcom</code></p>
<dd> Save an SSH-2 private key in ssh.com&#8217;s format. This option is not permitted for SSH-1 keys.</dl>
<p> If no output type is specified, the default is <code>private</code>.</dl>
<dt><code>-o</code> <i>output-file</i></p>
<dd> Specify the file where <code>puttygen</code> should write its output. If this option is not specified, <code>puttygen</code> will assume you want to overwrite the original file if the input and output file types are the same (changing a comment or passphrase), and will assume you want to output to stdout if you are asking for a public key or fingerprint. Otherwise, the <code>-o</code> option is required.</p>
<dt><code>-l</code></p>
<dd> Synonym for `<code>-O fingerprint</code>&#8216;.</p>
<dt><code>-L</code></p>
<dd> Synonym for `<code>-O public-openssh</code>&#8216;.</p>
<dt><code>-p</code></p>
<dd> Synonym for `<code>-O public</code>&#8216;.</dl>
<p> The following options do not run PuTTYgen as normal, but print informational messages and then quit:</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display a message summarizing the available options.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display the version of PuTTYgen.</p>
<dt><code>&#8211;pgpfp</code></p>
<dd> Display the fingerprints of the PuTTY PGP Master Keys, to aid in verifying new files released by the PuTTY team.</dl>
<h2>EXAMPLES</h2>
<p> To generate an SSH-2 RSA key pair and save it in PuTTY&#8217;s own format (you will be prompted for the passphrase): </p>
<pre>
puttygen -t rsa -C&nbsp;<wbr>&quot;my home key&quot;&nbsp;<wbr>-o mykey.ppk
</pre>
<p> To generate a larger (2048-bit) key: </p>
<pre>
puttygen -t rsa -b 2048 -C&nbsp;<wbr>&quot;my home key&quot;&nbsp;<wbr>-o mykey.ppk
</pre>
<p> To change the passphrase on a key (you will be prompted for the old and new passphrases): </p>
<pre>
puttygen -P mykey.ppk
</pre>
<p> To change the comment on a key: </p>
<pre>
puttygen -C&nbsp;<wbr>&quot;new comment&quot;&nbsp;<wbr>mykey.ppk
</pre>
<p> To convert a key into OpenSSH&#8217;s private key format: </p>
<pre>
puttygen mykey.ppk -O private-openssh -o my-openssh-key
</pre>
<p> To convert a key <i>from</i> another format (<code>puttygen</code> will automatically detect the input key type): </p>
<pre>
puttygen my-ssh.com-key -o mykey.ppk
</pre>
<p> To display the fingerprint of a key (some key types require a passphrase to extract even this much information): </p>
<pre>
puttygen -l mykey.ppk
</pre>
<p> To add the OpenSSH-format public half of a key to your authorised keys file: </p>
<pre>
puttygen -L mykey.ppk&nbsp;<wbr>&gt;&gt;&nbsp;<wbr>$HOME/.ssh/authorized_keys
</pre>
<h2>BUGS</h2>
<p> There&#8217;s currently no way to supply passphrases in batch mode, or even just to specify that you don&#8217;t want a passphrase at all. </p>
<h2>Index</h2>
