---
title: "pem2openpgp(1)"
name: "pem2openpgp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pem2openpgp/"
description: "pem2openpgp – translate PEM-encoded RSA keys to OpenPGP certificates"
---

<h2>NAME</h2>
<p> pem2openpgp &#8211; translate PEM-encoded RSA keys to OpenPGP certificates</p>
<h2>SYNOPSIS</h2>
<p> <code>pem2openpgp $USERID &lt; mykey.pem | gpg &#8211;import</code> </p>
<p><code>PEM2OPENPGP_EXPIRATION=$((86400 * $DAYS)) PEM2OPENPGP_USAGE_FLAGS=authenticate,certify pem2openpgp $USERID &lt;mykey.pem</code></p>
<h2>DESCRIPTION</h2>
<p> <code>pem2openpgp $USERID < mykey.pem | gpg \-\-import</code> is a low-level utility for transforming raw, PEM-encoded RSA secret keys into OpenPGP-formatted certificates. The generated certificates include the secret key material, so they should be handled carefully. </p>
<p> It works as an element within a pipeline: feed it the raw key on stdin, supply the desired User ID as a command line argument. Note that you may need to quote the string to ensure that it is entirely in a single argument. </p>
<p> Other choices about how to generate the new OpenPGP certificate are governed by environment variables.</p>
<h2>ENVIRONMENT</h2>
<p> The following environment variables influence the behavior of <code>:</code> </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <code>PEM2OPENPGP_TIMESTAMP</code> controls the timestamp (measured in seconds since the UNIX epoch) indicated as the creation time (a.k.a &quot;not valid before&quot;) of the generated certificate (self-signature) and the key itself. By default, <code>pem2openpgp $USERID < mykey.pem | gpg \-\-import</code> uses the current time. </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <code>PEM2OPENPGP_KEY_TIMESTAMP</code> controls the timestamp (measured in seconds since the UNIX epoch) indicated as the creation time of just the key itself (not the self-signature). By default, <code>pem2openpgp $USERID < mykey.pem | gpg \-\-import</code> uses the value from PEM2OPENPGP_TIMESTAMP. </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <code>PEM2OPENPGP_USAGE_FLAGS</code> should contain a comma-separated list of valid OpenPGP usage flags (see section 5.2.3.21 of RFC 4880 for what these mean). The available choices are: certify, sign, encrypt_comms, encrypt_storage, encrypt (this means both encrypt_comms and encrypt_storage), authenticate, split, shared. By default, <code>pem2openpgp $USERID < mykey.pem | gpg \-\-import</code> only sets the certify flag. </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <code>PEM2OPENPGP_EXPIRATION</code> sets an expiration (measured in seconds after the creation time of the key) in each self-signature packet. By default, no expiration subpacket is included. </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <code>PEM2OPENPGP_NEWKEY</code> indicates that <code>pem2openpgp $USERID < mykey.pem | gpg \-\-import</code> should ignore stdin, and instead generate a new key internally and build the certificate based on this new key. Set this variable to the number of bits for the new key (e.g. 2048). By default (when this is unset), <code>pem2openpgp $USERID < mykey.pem | gpg \-\-import</code> will read the key from stdin.</p>
<h2>AUTHOR</h2>
<p> <code>pem2openpgp $USERID < mykey.pem | gpg \-\-import</code> and this man page were written by Daniel Kahn Gillmor &lt;dkg [at] fifthhorseman.net&gt;.</p>
<h2>BUGS</h2>
<p> Only handles RSA keys at the moment. It might be nice to handle DSA keys as well. </p>
<p> Currently only creates certificates with a single User ID. Should be able to create certificates with multiple User IDs. </p>
<p> Currently only accepts unencrypted RSA keys. It should be able to deal with passphrase-locked key material. </p>
<p> Currently outputs OpenPGP certificates with cleartext secret key material. It would be good to be able to lock the output with a passphrase. </p>
<p> If you find other bugs, please report them at <a rel="nofollow" href="https://labs.riseup.net/code/projects/show/monkeysphere">https://labs.riseup.net/code/projects/show/monkeysphere</a></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-openpgp2ssh/">openpgp2ssh</a>(1), <a href="/docs/linux/man/1-monkeysphere/">monkeysphere</a>(1), <a href="/docs/linux/man/7-monkeysphere/">monkeysphere</a>(7), <a href="/docs/linux/man/1-ssh/">ssh</a>(1), monkeysphere-host8, monkeysphere-authentication8 </p>
<h2>Index</h2>
