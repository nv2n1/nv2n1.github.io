---
title: "gpgcompose(1)"
name: "gpgcompose"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpgcompose/"
description: "gpgcompose – Generate a stream of OpenPGP packets"
---

<h2 class="name">NAME</h2>
<p> gpgcompose &#8211; Generate a stream of OpenPGP packets</p>
<h2>SYNOPSIS</h2>
<p> <code>gpgcompose</code> [[<i>OPTION</i> [<i>ARGS</i>]] &#8230; ] </p>
<p> <code>gpgcompose &#8211;help</code> </p>
<p> <code>gpgcompose</code> <i>OPTION</i> <code>&#8211;help</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>gpgcompose</code> generates a stream of OpenPGP packets, including some which can include other nested packets within a layer of encryption. The syntax on the command line isn&#8217;t stable enough to document currently, but additional hints and examples can be found from the command line using <code>&#8211;help</code>. </p>
<h2>EXTERNAL DEPENDENCIES</h2>
<p> <code>gpgcompose</code> is not capable of performing secret key operations on its own. Creation of any OpenPGP object that requires secret key operations (e.g., <code>&#8211;signature</code>) will need to speak to an already-running <code>gpg-agent</code>. </p>
<h2>FILES</h2>
<p> Occasionally, <code>gpgcompose</code> will need to look up existing public keys for reference (e.g., <code>&#8211;public-key</code>). It will do so in <code>~/.gnupg/keyring.kbx,</code> or in <code>$GNUPGHOME/keyring.kbx</code> if that variable is set. </p>
<h2>SEE ALSO</h2>
<p> RFC 4880, <a href="/docs/linux/man/1-gpg/">gpg</a>(1), <a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a>(1), <a href="/docs/linux/man/1-gpg-connect-agent/">gpg-connect-agent</a>(1) </p>
<h2>AUTHOR</h2>
<p> gpgcompose is copyright (C) 2016, g10 Code GmbH. </p>
<p> This manpage was written by Daniel Kahn Gillmor &lt;dkg [at] fifthhorseman.net&gt;. </p>
<h2>Index</h2>
