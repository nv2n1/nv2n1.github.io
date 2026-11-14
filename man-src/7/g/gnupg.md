---
title: "gnupg(7)"
name: "gnupg"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gnupg/"
description: "GnuPG – The GNU Privacy Guard suite of programs"
---

<p><code>GnuPG</code> &#8211; The GNU Privacy Guard suite of programs</p>
<h2>Description</h2>
<p>GnuPG is a set of programs for public key encryption and digital signatures. The program most users will want to use is the OpenPGP command line tool, named <code>gpg2</code>. <code>gpgv</code>is a stripped down version of <code>gpg2</code> with no encryption functionality, used only to verify signatures against a trusted keyring. <code>gpgsm</code> is the X.509/CMS (for S/MIME) counterpart of <code>gpg2</code>. <code>gpg-agent</code> is a passphrase and private key daemon which may also emulate the <code>ssh-agent</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1), <code><a href="/docs/linux/man/1-gpg2/">gpg2</a></code>(1), <code><a href="/docs/linux/man/1-gpgv/">gpgv</a></code>(1), <code><a href="/docs/linux/man/1-gpgsm/">gpgsm</a></code>(1), <code><a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a></code>(1), <code><a href="/docs/linux/man/8-dirmngr/">dirmngr</a></code>(8), <code><a href="/docs/linux/man/1-scdaemon/">scdaemon</a></code>(1) The full documentation for this tool is maintained as a Texinfo manual. If GnuPG and the info program are properly installed at your site, the command</p>
<dl>
<dd>
<pre>info gnupg</pre>
</dl>
<p> should give you access to the complete manual including a menu structure and an index. </p>
