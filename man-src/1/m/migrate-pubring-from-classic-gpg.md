---
title: "migrate-pubring-from-classic-gpg(1)"
name: "migrate-pubring-from-classic-gpg"
section: "1"
letter: "m"
url: "/docs/linux/man/1-migrate-pubring-from-classic-gpg/"
description: "migrate-pubring-from-classic-gpg – Migrate a public keyring from \"classic\" to \"modern\" GnuPG"
---

<h2 class="name">NAME</h2>
<p> migrate-pubring-from-classic-gpg &#8211; Migrate a public keyring from &quot;classic&quot; to &quot;modern&quot; GnuPG</p>
<h2>SYNOPSIS</h2>
<p> <code>migrate-pubring-from-classic-gpg</code> [ <code>GPGHOMEDIR</code> | <i>&#8211;default</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>migrate-pubring-from-classic-gpg</code> migrates the public keyring in GnuPG home directory GPGHOMEDIR from the &quot;classic&quot; keyring format (pubring.gpg) to the &quot;modern&quot; keybox format using GnuPG versions 2.1 or 2.2 (pubring.kbx). </p>
<p> Specifying <code>&#8211;default</code> selects the standard GnuPG home directory (looking at $GNUPGHOME first, and falling back to ~/.gnupg if unset. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code>, <code>&#8211;usage</code> Output a short usage information. </p>
<h2>DIAGNOSTICS</h2>
<p> The program sends quite a bit of text (perhaps too much) to stderr. </p>
<p> During a migration, the tool backs up several pieces of data in a timestamped subdirectory of the GPGHOMEDIR. </p>
<h2>LIMITATIONS</h2>
<p> The keybox format rejects a number of OpenPGP certificates that the &quot;classic&quot; keyring format used to accept. These filters are defensive, since the certificates rejected are unsafe &#8212; either cryptographically unsound, or dangerously non-performant. This means that some migrations may produce warning messages about the migration being incomplete. This is generally a good thing! </p>
<p> Known limitations: </p>
<p> <code>Flooded certificates</code></p>
<dl>
<dt>
<dd> Some OpenPGP certificates have been flooded with bogus certifications as part of an attack on the SKS keyserver network (see <a rel="nofollow" href="https://tools.ietf.org/html/draft-dkg-openpgp-abuse-resistant-keystore-03#section-2.1">https://tools.ietf.org/html/draft-dkg-openpgp-abuse-resistant-keystore-03#section-2.1</a>). </p>
<p> The keybox format rejects import of any OpenPGP certificate larger than 5MiB. As of GnuPG 2.2.17, if gpg encounters such a flooded certificate will retry the import while stripping all third-party certifications (see &quot;self-sigs-only&quot; in <a href="/docs/linux/man/1-gpg/">gpg</a>(1)). </p>
<p> The typical error message when migrating a keyring with a flooded certificate will be something like: </p>
</dl>
<dl>
<dt>
<dd> error writing keyring &#8216;pubring.kbx&#8217;: Provided object is too large</dl>
<p> <code>OpenPGPv3 public keys (a.k.a. PGP-2 keys)</code></p>
<dl>
<dt>
<dd> Modern OpenPGP implementations use so-called &quot;OpenPGP v4&quot; public keys. Older versions of the public key format have serious known problems. See <a rel="nofollow" href="https://tools.ietf.org/html/rfc4880#section-5.5.2">https://tools.ietf.org/html/rfc4880#section-5.5.2</a> for more details about and reasons for v3 key deprecation. </p>
<p> The keybox format skips v3 keys entirely during migration, and GnuPG will produce a message like: </p>
</dl>
<dl>
<dt>
<dd> skipped PGP-2 keys: 1</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>GNUPGHOME</code> Selects the GnuPG home directory when set and &#8211;default is given. </p>
<p> <code>GPG</code> The name of the <code>gpg</code> executable (defaults to <code>gpg</code> ). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2016 Daniel Kahn Gillmor for the Debian project. Please report bugs via the Debian BTS. </p>
<h2>Index</h2>
