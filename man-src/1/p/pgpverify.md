---
title: "pgpverify(1)"
name: "pgpverify"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgpverify/"
description: "pgpverify – Cryptographically verify Usenet control messages"
---

<h2 class="name">NAME</h2>
<p> pgpverify &#8211; Cryptographically verify Usenet control messages </p>
<h2>SYNOPSIS</h2>
<p> <code>pgpverify</code> [<code>&#8211;findid</code>=<i>string</i>] [<code>&#8211;test</code>] &lt; <i>message</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>pgpverify</code> program reads (on standard input) a Usenet control message that has been cryptographically signed using the <code>signcontrol</code> program (or some other program that produces a compatible format). <code>pgpverify</code> then uses a <font SIZE="-1">PGP</font> implementation to determine who signed the control message. If the control message has a valid signature, <code>pgpverify</code> prints (to stdout) the user <font SIZE="-1">ID</font> of the key that signed the message. Otherwise, it exits with a non-zero exit status. </p>
<p> If <code>pgpverify</code> is installed as part of <font SIZE="-1">INN</font>, it uses <font SIZE="-1">INN</font>&#8216;s configuration to determine what signature verification program to use, how to log errors, what temporary directory to use, and what keyring to use. Otherwise, all of those parameters can be set by editing the beginning of this script. </p>
<p> By default, when running as part of <font SIZE="-1">INN</font>, <code>pgpverify</code> expects the <font SIZE="-1">PGP</font> key ring to be found in <i>pathetc</i>/pgp (as either <i>pubring.pgp</i> or <i>pubring.gpg</i> depending on whether <font SIZE="-1">PGP</font> or GnuPG is used to verify signatures). If that directory doesn&#8217;t exist, it will fall back on using the default key ring, which is in a <i>.pgp</i> or <i>.gnupg</i> subdirectory of the running user&#8217;s home directory. </p>
<p> <font SIZE="-1">INN</font>, when using GnuPG, configures <code>pgpverify</code> to use <code>gpgv</code>, which by default expects keys to be in a keyring named <i>trustedkeys.gpg</i>, since it doesn&#8217;t implement trust checking directly. <code>pgpverify</code> uses that file if present but falls back to <i>pubring.gpg</i> if it&#8217;s not found. This bypasses the trust model for checking keys, but is compatible with the way that <code>pgpverify</code> used to behave. Of course, if a keyring is found in <i>pathetc</i>/pgp or configured at the top of the script, that overrides all of this behavior.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;findid</code>=<i>string</i></p>
<dd> The <code>&#8211;findid</code> flag causes <code>pgpverify</code> to explicitly search for <i>string</i> in the output from <font SIZE="-1">PGP</font>&#8216;s analysis of the message. This option is useful when several UIDs are defined on a single <font SIZE="-1">PGP</font> key, and the caller to <code>pgpverify</code> needs checking whether a given one is defined on this key. In case the signature is valid but does not contain <i>string</i>, <code>pgpverify</code> exits with exit status 4.</p>
<dt><code>&#8211;test</code></p>
<dd> The <code>&#8211;test</code> flag causes <code>pgpverify</code> to print out the input that it is passing to <font SIZE="-1">PGP</font> (which is a reconstructed version of the input that supposedly created the control message) as well as the output from <font SIZE="-1">PGP</font>&#8216;s analysis of the message.</dl>
<h2>EXIT STATUS</h2>
<p> <code>pgpverify</code> may exit with the following statuses:</p>
<dl>
<dt>0</p>
<dd> The control message had a good <font SIZE="-1">PGP</font> signature.</p>
<dt>1</p>
<dd> The control message had no <font SIZE="-1">PGP</font> signature.</p>
<dt>2</p>
<dd> The control message had an unknown <font SIZE="-1">PGP</font> signature.</p>
<dt>3</p>
<dd> The control message had a bad <font SIZE="-1">PGP</font> signature.</p>
<dt>4</p>
<dd> The control message had a good <font SIZE="-1">PGP</font> signature but the argument given to the <code>&#8211;findid</code> flag had non been found in the output from <font SIZE="-1">PGP</font>&#8216;s analysis of the message.</p>
<dt>255</p>
<dd> A problem occurred not directly related to <font SIZE="-1">PGP</font> analysis of signature.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>pgpverify</code> does not modify or otherwise alter the environment before invoking the <code>pgp</code> or <code>gpgv</code> program. It is the responsibility of the person who installs <code>pgpverify</code> to ensure that when <code>pgp</code> or <code>gpgv</code> runs, it has the ability to locate and read a <font SIZE="-1">PGP</font> key file that contains the <font SIZE="-1">PGP</font> public keys for the appropriate Usenet hierarchy administrators. <code>pgpverify</code> can be pointed to an appropriate key ring by editing variables at the beginning of this script.</p>
<h2>NOTES</h2>
<p> Historically, Usenet news server administrators have configured their news servers to automatically honor Usenet control messages based on the originator of the control messages and the hierarchies for which the control messages applied. For example, in the past, David Lawrence always issued control messages for the &#8220;Big 8&#8221; hierarchies (comp, humanities, misc, news, rec, sci, soc, talk). Usenet news administrators would configure their news server software to automatically honor newgroup and rmgroup control messages that originated from David Lawrence and applied to any of the Big 8 hierarchies. </p>
<p> Unfortunately, Usenet news articles (including control messages) are notoriously easy to forge. Soon, malicious users realized they could create or remove (at least temporarily) any Big 8 newsgroup they wanted by simply forging an appropriate control message in David Lawrence&#8217;s name. As Usenet became more widely used, forgeries became more common. </p>
<p> The <code>pgpverify</code> program was designed to allow Usenet news administrators to configure their servers to cryptographically verify control messages before automatically acting on them. Under the <code>pgpverify</code> system, a Usenet hierarchy maintainer creates a <font SIZE="-1">PGP</font> public/private key pair and disseminates the public key. Whenever the hierarchy maintainer issues a control message, he uses the <code>signcontrol</code> program to sign the control message with the <font SIZE="-1">PGP</font> private key. Usenet news administrators configure their news servers to run the <code>pgpverify</code> program on the appropriate control messages, and take action based on the <font SIZE="-1">PGP</font> key User <font SIZE="-1">ID</font> that signed the control message, not the name and address that appear in the control message&#8217;s From: or Sender: headers. </p>
<p> Thus, appropriate use of the <code>signcontrol</code> and <code>pgpverify</code> programs essentially eliminates the possibility of malicious users forging Usenet control messages that sites will act upon, as such users would have to obtain the <font SIZE="-1">PGP</font> private key in order to forge a control message that would pass the cryptographic verification step. If the hierarchy administrators properly protect their <font SIZE="-1">PGP</font> private keys, the only way a malicious user could forge a validly-signed control message would be by breaking the public key encryption algorithm, which (at least at this time) is believed to be prohibitively difficult for <font SIZE="-1">PGP</font> keys of a sufficient bit length.</p>
<h2>HISTORY</h2>
<p> <code>pgpverify</code> was written by David C Lawrence &lt;tale [at] isc.org&gt;. Manual page provided by James Ralston. It is currently maintained by Russ Allbery &lt;eagle [at] eyrie.org&gt;.</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> David Lawrence wrote: &#8220;Our lawyer told me to include the following. The upshot of it is that you can use the software for free as much as you like.&#8221; </p>
<p> Copyright (c) 1996 <font SIZE="-1">UUNET</font> Technologies, Inc. All rights reserved. </p>
<p> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:</p>
<dl>
<dt>1.</p>
<dd> Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.</p>
<dt>2.</p>
<dd> Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.</p>
<dt>3.</p>
<dd> All advertising materials mentioning features or use of this software must display the following acknowledgement: </p>
<pre>
  This product includes software developed by UUNET Technologies, Inc.
</pre>
<dt>4.</p>
<dd> The name of <font SIZE="-1">UUNET</font> Technologies (&#8220;<font SIZE="-1">UUNET</font>&#8221;) may not be used to endorse or promote products derived from this software without specific prior written permission.</dl>
<p> <font SIZE="-1">THIS</font> <font SIZE="-1">SOFTWARE</font> <font SIZE="-1">IS</font> <font SIZE="-1">PROVIDED</font> <font SIZE="-1">BY</font> <font SIZE="-1">UUNET</font> &#8220;<font SIZE="-1">AS</font> <font SIZE="-1">IS</font>&#8221; <font SIZE="-1">AND</font> <font SIZE="-1">ANY</font> <font SIZE="-1">EXPRESS</font> <font SIZE="-1">OR</font> <font SIZE="-1">IMPLIED</font> <font SIZE="-1">WARRANTIES</font>, <font SIZE="-1">INCLUDING</font>, <font SIZE="-1">BUT</font> <font SIZE="-1">NOT</font> <font SIZE="-1">LIMITED</font> <font SIZE="-1">TO</font>, <font SIZE="-1">THE</font> <font SIZE="-1">IMPLIED</font> <font SIZE="-1">WARRANTIES</font> <font SIZE="-1">OF</font> <font SIZE="-1">MERCHANTABILITY</font> <font SIZE="-1">AND</font> <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font> <font SIZE="-1">ARE</font> <font SIZE="-1">DISCLAIMED</font>. <font SIZE="-1">IN</font> <font SIZE="-1">NO</font> <font SIZE="-1">EVENT</font> <font SIZE="-1">SHALL</font> <font SIZE="-1">UUNET</font> <font SIZE="-1">BE</font> <font SIZE="-1">LIABLE</font> <font SIZE="-1">FOR</font> <font SIZE="-1">ANY</font> <font SIZE="-1">DIRECT</font>, <font SIZE="-1">INDIRECT</font>, <font SIZE="-1">INCIDENTAL</font>, <font SIZE="-1">SPECIAL</font>, <font SIZE="-1">EXEMPLARY</font>, <font SIZE="-1">OR</font> <font SIZE="-1">CONSEQUENTIAL</font> <font SIZE="-1">DAMAGES</font> (<font SIZE="-1">INCLUDING</font>, <font SIZE="-1">BUT</font> <font SIZE="-1">NOT</font> <font SIZE="-1">LIMITED</font> <font SIZE="-1">TO</font>, <font SIZE="-1">PROCUREMENT</font> <font SIZE="-1">OF</font> <font SIZE="-1">SUBSTITUTE</font> <font SIZE="-1">GOODS</font> <font SIZE="-1">OR</font> <font SIZE="-1">SERVICES</font>; <font SIZE="-1">LOSS</font> <font SIZE="-1">OF</font> <font SIZE="-1">USE</font>, <font SIZE="-1">DATA</font>, <font SIZE="-1">OR</font> <font SIZE="-1">PROFITS</font>; <font SIZE="-1">OR</font> <font SIZE="-1">BUSINESS</font> <font SIZE="-1">INTERRUPTION</font>) <font SIZE="-1">HOWEVER</font> <font SIZE="-1">CAUSED</font> <font SIZE="-1">AND</font> <font SIZE="-1">ON</font> <font SIZE="-1">ANY</font> <font SIZE="-1">THEORY</font> <font SIZE="-1">OF</font> <font SIZE="-1">LIABILITY</font>, <font SIZE="-1">WHETHER</font> <font SIZE="-1">IN</font> <font SIZE="-1">CONTRACT</font>, <font SIZE="-1">STRICT</font> <font SIZE="-1">LIABILITY</font>, <font SIZE="-1">OR</font> <font SIZE="-1">TORT</font> (<font SIZE="-1">INCLUDING</font> <font SIZE="-1">NEGLIGENCE</font> <font SIZE="-1">OR</font> <font SIZE="-1">OTHERWISE</font>) <font SIZE="-1">ARISING</font> <font SIZE="-1">IN</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WAY</font> <font SIZE="-1">OUT</font> <font SIZE="-1">OF</font> <font SIZE="-1">THE</font> <font SIZE="-1">USE</font> <font SIZE="-1">OF</font> <font SIZE="-1">THIS</font> <font SIZE="-1">SOFTWARE</font>, <font SIZE="-1">EVEN</font> <font SIZE="-1">IF</font> <font SIZE="-1">ADVISED</font> <font SIZE="-1">OF</font> <font SIZE="-1">THE</font> <font SIZE="-1">POSSIBILITY</font> <font SIZE="-1">OF</font> <font SIZE="-1">SUCH</font> <font SIZE="-1">DAMAGE</font>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gpgv/">gpgv</a></i>(1), <i><a href="/docs/linux/man/1-pgp/">pgp</a></i>(1). </p>
<p> &lt;<a href="ftp://ftp.isc.org/pub/pgpcontrol/">ftp://ftp.isc.org/pub/pgpcontrol/</a>&gt; is where the most recent versions of <code>signcontrol</code> and <code>pgpverify</code> live, along with <font SIZE="-1">PGP</font> public keys used for hierarchy administration. </p>
<h2>Index</h2>
