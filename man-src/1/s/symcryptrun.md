---
title: "symcryptrun(1)"
name: "symcryptrun"
section: "1"
letter: "s"
url: "/docs/linux/man/1-symcryptrun/"
description: "symcryptrun – Call a simple symmetric encryption tool"
---

<h2 class="name">NAME</h2>
<p> <code>symcryptrun</code> &#8211; Call a simple symmetric encryption tool </p>
<h2>SYNOPSIS</h2>
<p> <code>symcryptrun</code> <code>&#8211;class</code> <i>class</i> <code>&#8211;program</code> <i>program</i> <code>&#8211;keyfile</code> <i>keyfile</i> [<code>&#8211;decrypt</code>|<code>&#8211;encrypt</code>] [<i>inputfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> Sometimes simple encryption tools are already in use for a long time and there might be a desire to integrate them into the GnuPG framework. The protocols and encryption methods might be non-standard or not even properly documented, so that a full-fledged encryption tool with an interface like <code>gpg</code> is not doable. <code>symcryptrun</code> provides a solution: It operates by calling the external encryption/decryption module and provides a passphrase for a key using the standard <code>pinentry</code> based mechanism through <code>gpg-agent</code>. </p>
<p> Note, that <code>symcryptrun</code> is only available if GnuPG has been configured with &#8216;&#8211;enable-symcryptrun&#8217; at build time. </p>
<p> For encryption, the plain text must be provided on STDIN or as the argument <i>inputfile</i>, and the ciphertext will be output to STDOUT. For decryption vice versa. </p>
<p> <i>CLASS</i> describes the calling conventions of the external tool. Currently it must be given as &#8216;confucius&#8217;. <i>PROGRAM</i> is the full filename of that external tool. </p>
<p> For the class &#8216;confucius&#8217; the option <code>&#8211;keyfile</code> is required; <i>keyfile</i> is the name of a file containing the secret key, which may be protected by a passphrase. For detailed calling conventions, see the source code. </p>
<p> Note, that <code>gpg-agent</code> must be running before starting <code>symcryptrun</code>. </p>
<p> The following additional options may be used: </p>
<dl>
<dt><code>-v</code></p>
<dd> <code>&#8211;verbose</code> Output additional information while running. </p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Try to be as quiet as possible. </p>
<dt><code>&#8211;homedir </code><i>dir</i></p>
<dd> Set the name of the home directory to <i>dir</i>. If this option is not used, the home directory defaults to &#8216;<i>~/.gnupg</i>&#8216;. It is only recognized when given on the command line. It also overrides any home directory stated through the environment variable &#8216;<i>GNUPGHOME</i>&#8216; or (on Windows systems) by means of the Registry entry <i>HKCU\Software\GNU\GnuPG:HomeDir</i>. </p>
<p> On Windows systems it is possible to install GnuPG as a portable application. In this case only this command line option is considered, all other ways to set a home directory are ignored. </p>
<p> To install GnuPG as a portable application under Windows, create an empty file named &#8216;<i>gpgconf.ctl</i>&#8216; in the same directory as the tool &#8216;<i>gpgconf.exe</i>&#8216;. The root of the installation is then that directory; or, if &#8216;<i>gpgconf.exe</i>&#8216; has been installed directly below a directory named &#8216;<i>bin</i>&#8216;, its parent directory. You also need to make sure that the following directories exist and are writable: &#8216;<i>ROOT/home</i>&#8216; for the GnuPG home and &#8216;<i>ROOT/var/cache/gnupg</i>&#8216; for internal cache files. </p>
<dt><code>&#8211;log-file </code><i>file</i></p>
<dd> Append all logging output to <i>file</i>. Use &#8216;<i>socket://</i>&#8216; to log to socket. Default is to write logging information to STDERR. </p>
</dl>
<p> The possible exit status codes of <code>symcryptrun</code> are: </p>
<dl>
<dt><code>0</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Success.</p>
<dt><code>1</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Some error occurred.</p>
<dt><code>2</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;No valid passphrase was provided.</p>
<dt><code>3</code></p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The operation was canceled by the user. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1), <code><a href="/docs/linux/man/1-gpgsm/">gpgsm</a></code>(1), <code><a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a></code>(1), </p>
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
