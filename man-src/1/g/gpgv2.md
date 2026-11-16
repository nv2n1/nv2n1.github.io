---
title: "gpgv2(1)"
name: "gpgv2"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpgv2/"
description: "gpgv2 – Verify OpenPGP signatures"
---

<h2>NAME</h2>
<p> <code>gpgv2</code> &#8211; Verify OpenPGP signatures</p>
<h2>SYNOPSIS</h2>
<p> <code>gpgv2</code> [<i>options</i>] <i>signed_files</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>gpgv2</code> is an OpenPGP signature verification tool. </p>
<p> This program is actually a stripped-down version of <code>gpg</code> which is only able to check signatures. It is somewhat smaller than the fully-blown <code>gpg</code> and uses a different (and simpler) way to check that the public keys used to make the signature are valid. There are no configuration files and only a few options are implemented. </p>
<p> <code>gpgv2</code> assumes that all keys in the keyring are trustworthy. By default it uses a keyring named &#8216;<i>trustedkeys.gpg</i>&#8216; which is assumed to be in the home directory as defined by GnuPG or set by an option or an environment variable. An option may be used to specify another keyring or even multiple keyrings. </p>
<h2>RETURN VALUE</h2>
<p> The program returns 0 if everything is fine, 1 if at least one signature was bad, and other error codes for fatal errors. </p>
<h2>OPTIONS</h2>
<p> <code>gpgv2</code> recognizes these options: </p>
<dl>
<dt><code>&#8211;verbose</code></dt>
<dd>
</dd><dt><code>-v</code></dt>
<dd> Gives more information during processing. If used twice, the input data is listed in detail. </dd>
<dt><code>&#8211;quiet</code></dt>
<dd>
</dd><dt><code>-q</code></dt>
<dd> Try to be as quiet as possible. </dd>
<dt><code>&#8211;keyring </code><i>file</i></dt>
<dd> Add <i>file</i> to the list of keyrings. If <i>file</i> begins with a tilde and a slash, these are replaced by the HOME directory. If the filename does not contain a slash, it is assumed to be in the home-directory (&quot;~/.gnupg&quot; if &#8211;homedir is not used). </dd>
<dt><code>&#8211;status-fd </code><i>n</i></dt>
<dd> Write special status strings to the file descriptor <i>n</i>. See the file DETAILS in the documentation for a listing of them. </dd>
<dt><code>&#8211;logger-fd n</code></dt>
<dd> Write log output to file descriptor <code>n</code> and not to stderr. </dd>
<dt><code>&#8211;ignore-time-conflict</code></dt>
<dd> GnuPG normally checks that the timestamps associated with keys and signatures have plausible values. However, sometimes a signature seems to be older than the key due to clock problems. This option turns these checks into warnings. </dd>
<dt><code>&#8211;homedir </code><i>dir</i></dt>
<dd> Set the name of the home directory to <i>dir</i>. If this option is not used, the home directory defaults to &#8216;<i>~/.gnupg</i>&#8216;. It is only recognized when given on the command line. It also overrides any home directory stated through the environment variable &#8216;<i>GNUPGHOME</i>&#8216; or (on W32 systems) by means of the Registry entry <i>HKCU\Software\GNU\GnuPG:HomeDir</i>. </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>gpgv2 pgpfile</code></dt>
<dd>
</dd><dt><code>gpgv2 sigfile</code> [<code>datafile</code>]</dt>
<dd> Verify the signature of the file. The second form is used for detached signatures, where <code>sigfile</code> is the detached signature (either ASCII-armored or binary) and <code>datafile</code> contains the signed data; if <code>datafile</code> is &quot;-&quot; the signed data is expected on <code>stdin</code>; if <code>datafile</code> is not given the name of the file holding the signed data is constructed by cutting off the extension (&quot;.asc&quot;, &quot;.sig&quot; or &quot;.sign&quot;) from <code>sigfile</code>. </dd>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.gnupg/trustedkeys.gpg</code></dt>
<dd> The default keyring with the allowed keys. </dd>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>HOME</code></dt>
<dd> Used to locate the default home directory. </dd>
<dt><code>GNUPGHOME</code></dt>
<dd> If set directory used instead of &quot;~/.gnupg&quot;. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpg2/">gpg2</a></code>(1) </p>
<p> The full documentation for this tool is maintained as a Texinfo manual. If GnuPG and the info program are properly installed at your site, the command </p>
<dl>
<dt>
</dt><dd>
<pre>
info gnupg
</pre>
</dd></dl>
<p> should give you access to the complete manual including a menu structure and an index. </p>
<h2>Index</h2>
