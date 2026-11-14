---
title: "gpgv(1)"
name: "gpgv"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpgv/"
description: "gpgv – Verify OpenPGP signatures"
---

<h2 class="name">NAME</h2>
<p> <code>gpgv</code> &#8211; Verify OpenPGP signatures </p>
<h2>SYNOPSIS</h2>
<p> <code>gpgv</code> [<i>options</i>] <i>signed_files</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>gpgv</code> is an OpenPGP signature verification tool. </p>
<p> This program is actually a stripped-down version of <code>gpg</code> which is only able to check signatures. It is somewhat smaller than the fully-blown <code>gpg</code> and uses a different (and simpler) way to check that the public keys used to make the signature are valid. There are no configuration files and only a few options are implemented. </p>
<p> <code>gpgv</code> assumes that all keys in the keyring are trustworthy. That does also mean that it does not check for expired or revoked keys. </p>
<p> If no <code>&#8211;keyring</code> option is given, <code>gpgv</code> looks for a &#8220;default&#8221; keyring named &#8216;<i>trustedkeys.kbx</i>&#8216; (preferred) or &#8216;<i>trustedkeys.gpg</i>&#8216; in the home directory of GnuPG, either the default home directory or the one set by the <code>&#8211;homedir</code> option or the <code>GNUPGHOME</code> environment variable. If any <code>&#8211;keyring</code> option is used, <code>gpgv</code> will not look for the default keyring. The <code>&#8211;keyring</code> option may be used multiple times and all specified keyrings will be used together. </p>
<h2>RETURN VALUE</h2>
<p> The program returns 0 if everything is fine, 1 if at least one signature was bad, and other error codes for fatal errors. </p>
<h2>OPTIONS</h2>
<p> <code>gpgv</code> recognizes these options: </p>
<dl>
<dt><code>&#8211;verbose</code></p>
<dd> <code>-v</code> Gives more information during processing. If used twice, the input data is listed in detail. </p>
<dt><code>&#8211;quiet</code></p>
<dd> <code>-q</code> Try to be as quiet as possible. </p>
<dt><code>&#8211;keyring </code><i>file</i></p>
<dd> Add <i>file</i> to the list of keyrings. If <i>file</i> begins with a tilde and a slash, these are replaced by the HOME directory. If the filename does not contain a slash, it is assumed to be in the home-directory (&quot;~/.gnupg&quot; if &#8211;homedir is not used). </p>
<dt><code>&#8211;output </code><i>file</i></p>
<dd> <code>-o </code><i>file</i> Write output to <i>file</i>; to write to stdout use <code>&#8211;</code>. This option can be used to get the signed text from a cleartext or binary signature; it also works for detached signatures, but in that case this option is in general not useful. Note that an existing file will be overwritten. </p>
<dt><code>&#8211;status-fd </code><i>n</i></p>
<dd> Write special status strings to the file descriptor <i>n</i>. See the file DETAILS in the documentation for a listing of them. </p>
<dt><code>&#8211;logger-fd n</code></p>
<dd> Write log output to file descriptor <code>n</code> and not to stderr. </p>
<dt><code>&#8211;log-file file</code></p>
<dd> Same as <code>&#8211;logger-fd</code>, except the logger data is written to file <code>file</code>. Use &#8216;<i>socket://</i>&#8216; to log to socket. </p>
<dt><code>&#8211;ignore-time-conflict</code></p>
<dd> GnuPG normally checks that the timestamps associated with keys and signatures have plausible values. However, sometimes a signature seems to be older than the key due to clock problems. This option turns these checks into warnings. </p>
<dt><code>&#8211;homedir </code><i>dir</i></p>
<dd> Set the name of the home directory to <i>dir</i>. If this option is not used, the home directory defaults to &#8216;<i>~/.gnupg</i>&#8216;. It is only recognized when given on the command line. It also overrides any home directory stated through the environment variable &#8216;<i>GNUPGHOME</i>&#8216; or (on Windows systems) by means of the Registry entry <i>HKCU\Software\GNU\GnuPG:HomeDir</i>. </p>
<p> On Windows systems it is possible to install GnuPG as a portable application. In this case only this command line option is considered, all other ways to set a home directory are ignored. </p>
<p> To install GnuPG as a portable application under Windows, create an empty file named &#8216;<i>gpgconf.ctl</i>&#8216; in the same directory as the tool &#8216;<i>gpgconf.exe</i>&#8216;. The root of the installation is then that directory; or, if &#8216;<i>gpgconf.exe</i>&#8216; has been installed directly below a directory named &#8216;<i>bin</i>&#8216;, its parent directory. You also need to make sure that the following directories exist and are writable: &#8216;<i>ROOT/home</i>&#8216; for the GnuPG home and &#8216;<i>ROOT/var/cache/gnupg</i>&#8216; for internal cache files. </p>
<dt><code>&#8211;weak-digest name</code></p>
<dd> Treat the specified digest algorithm as weak. Signatures made over weak digests algorithms are normally rejected. This option can be supplied multiple times if multiple algorithms should be considered weak. MD5 is always considered weak, and does not need to be listed explicitly. </p>
<dt><code>&#8211;enable-special-filenames</code></p>
<dd> This option enables a mode in which filenames of the form &#8216;<i>-&amp;n</i>&#8216;, where n is a non-negative decimal number, refer to the file descriptor n and not to a file with that name. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>gpgv pgpfile</code></p>
<dd> <code>gpgv sigfile</code> [<code>datafile</code>] Verify the signature of the file. The second form is used for detached signatures, where <code>sigfile</code> is the detached signature (either ASCII-armored or binary) and <code>datafile</code> contains the signed data; if <code>datafile</code> is &quot;-&quot; the signed data is expected on <code>stdin</code>; if <code>datafile</code> is not given the name of the file holding the signed data is constructed by cutting off the extension (&quot;.asc&quot;, &quot;.sig&quot; or &quot;.sign&quot;) from <code>sigfile</code>. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.gnupg/trustedkeys.gpg</code></p>
<dd> The default keyring with the allowed keys. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>HOME</code></p>
<dd> Used to locate the default home directory. </p>
<dt><code>GNUPGHOME</code></p>
<dd> If set directory used instead of &quot;~/.gnupg&quot;. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1) </p>
<p> The full documentation for this tool is maintained as a Texinfo manual. If GnuPG and the info program are properly installed at your site, the command </p>
<dl>
<dt>
<dd>
<pre>
info gnupg
</pre>
</dl>
<p> should give you access to the complete manual including a menu structure and an index. </p>
<h2>Index</h2>
