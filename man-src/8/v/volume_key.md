---
title: "volume_key(8)"
name: "volume_key"
section: "8"
letter: "v"
url: "/docs/linux/man/8-volume_key/"
description: "volume_key – work with volume encryption secrets and escrow packets"
---

<p>volume_key &#8211; work with volume encryption secrets and escrow packets</p>
<h2>Synopis</h2>
<p><code>volume_key</code> [<i>OPTION</i>]&#8230; <i>OPERAND</i>&#8230;</p>
<h2>Description</h2>
<p><code>volume_key</code> extracts &quot;secrets&quot; used for volume encryption (for example keys or passphrases) and stores them into separate encrypted &quot;escrow packets&quot;, uses a previously created escrow packet to restore access to a volume (e.g. if the user forgets a passphrase), or manipulates the information in escrow packets. The mode of operation and operands of <code>volume_key</code> are determined by specifying one of the <code>&#8211;save</code>, <code>&#8211;restore</code>, <code>&#8211;setup-volume</code>, <code>&#8211;reencrypt</code>, <code>&#8211;dump</code> or <code>&#8211;secrets</code> options. See the OPTIONS sections for details. </p>
<h2>Options</h2>
<p>In all options described below, <i>VOLUME</i> is a LUKS device, not the plaintext device containted within:</p>
<dl>
<dd><code>blkid -s TYPE</code> <i>VOLUME</i></dl>
<p> should report <code>TYPE=&quot;crypto_LUKS&quot;</code>. </p>
<p> The following options determine the mode of operation and expected operands of <code>volume_key</code>: </p>
<dl>
<dt><code>&#8211;save</code></p>
<dd>Expects operands <i>VOLUME</i> [<i>PACKET</i>]. Open <i>VOLUME</i>. If <i>PACKET</i> is provided, load the secrets from it. Otherwise, extract secrets from <i>VOLUME</i>, prompting the user if necessary. In any case, store secrets in one or more output packets. </p>
<dt><code>&#8211;restore</code></p>
<dd>Expects operands <i>VOLUME</i> <i>PACKET</i>. Open <i>VOLUME</i> and use the secrets in <i>PACKET</i> to make <i>VOLUME</i> accessible again, prompting the user if necessary (e.g. by letting the user enter a new passphrase). </p>
<dt><code>&#8211;setup-volume</code></p>
<dd>Expects operands <i>VOLUME PACKET</i> <i>NAME</i>. Open <i>VOLUME</i> and use the secrets in <i>PACKET</i> to set up <i>VOLUME</i> for use of the decrypted data as <i>NAME</i>. </p>
<p> Currently <i>NAME</i> is a name of a dm-crypt volume, and this operation makes the decrypted volume available as <code>/dev/mapper/</code><i>NAME</i>. </p>
<p> This operation should not permanently alter <i>VOLUME</i> (e.g. by adding a new passphrase); the user can of course access and modify the decrypted volume, modifying <i>VOLUME</i> in the process. </p>
<dt><code>&#8211;reencrypt</code></p>
<dd>Expects operand <i>PACKET</i>. Open <i>PACKET</i>, decrypting it if necessary, and store the information in one or more new output packets. </p>
<dt><code>&#8211;dump</code></p>
<dd>Expects operand <i>PACKET</i>. Open <i>PACKET</i>, decrypting it if necessary, and output the contents of <i>PACKET</i>. The secrets are not output by default. </p>
<dt><code>&#8211;secrets</code></p>
<dd>Expects operand <i>PACKET</i>. Open <i>PACKET</i>, decrypting it if necessary, and output secrets contained in <i>PACKET</i>. </p>
<dt><code>&#8211;help</code></p>
<dd>Show usage information. </p>
<dt><code>&#8211;version</code></p>
<dd>Show version of <code>volume_key</code>. </p>
</dl>
<p> The following options alter the behavior of the specified operation: </p>
<dl>
<dt><code>-b</code>, <code>&#8211;batch</code></p>
<dd>Run in batch mode. Read passwords and passphrases from standard input, each terminated by a NUL character. If a packet does not match a volume exactly, fail instead of prompting the user. </p>
<dt><code>-d</code>, <code>&#8211;nss-dir</code> <i>DIR</i></p>
<dd>Use private keys in NSS database in <i>DIR</i> to decrypt public key-encrypted packets. </p>
<dt><code>-o</code>, <code>&#8211;output</code> <i>PACKET</i></p>
<dd>Write the default secret to <i>PACKET</i>. </p>
<p> Which secret is the default depends on volume format: it should not be likely to expire, and it should allow restoring access to the volume using <code>&#8211;restore</code>. </p>
<dt><code>&#8211;output-data-encryption-key</code> <i>PACKET</i></p>
<dd>Write the data encryption key (the key directly used to encrypt the actual volume data) to <i>PACKET</i>. </p>
<dt><code>&#8211;output-passphrase</code> <i>PACKET</i></p>
<dd>Write a passphrase that can be used to access the volume to <i>PACKET</i>. </p>
<dt><code>&#8211;create-random-passphrase</code> <i>PACKET</i></p>
<dd>Generate a random alphanumeric passphrase, add it to <i>VOLUME</i> (without affecting other passphrases) and store the random passphrase into <i>PACKET</i>. </p>
<dt><code>-c</code>, <code>&#8211;certificate</code> <i>CERT</i></p>
<dd>Load a certificate from the file specified by <i>CERT</i> and encrypt all output packets using the public key contained in the certificate. If this option is not specified, all output packets are encrypted using a passphrase. </p>
<p> Note that <i>CERT</i> is a certificate file name, not a NSS certificate nickname. </p>
<dt><code>&#8211;output-format</code> <i>FORMAT</i></p>
<dd>Use <i>FORMAT</i> for all output packets. <i>FORMAT</i> can currently be one of <code>asymmetric</code> (use CMS to encrypt the whole packet, requires a certificate), <code>asymmetric_wrap_secret_only</code> (wrap only the secret, requires a certificate), <code>passphrase</code> (use GPG to encrypt the whole packet, requires a passphrase). </p>
<dt><code>&#8211;unencrypted</code></p>
<dd>Only dump the unencrypted parts of the packet, if any, with <code>&#8211;dump</code>. Do not require any passphrase or private key access. </p>
<dt><code>&#8211;with-secrets</code></p>
<dd>Include secrets in the output of <code>&#8211;dump</code> </p>
</dl>
<h2>Exit Status</h2>
<p><code>volume_key</code> returns with exit status 0 on success, 1 on error.</p>
<h2>Notes</h2>
<p>The only currently supported volume format is LUKS. </p>
<h2>Example</h2>
<p>Typical usage of <code>volume_key</code> proceeds as follows. During system installation or soon after, back up the default secret of a volume, and add a system-specific random passphrase. Encrypt both using a certificate:</p>
<dl>
<dd><code>volume_key &#8211;save</code> <i>VOLUME</i> <code>-c</code> <i>CERT</i> <code>-o</code> <i>PACKET_DEFAULT</i> <code>&#8211;create-random-passphrase</code> <i>PACKET_PASSPHRASE</i></dl>
<p> Store <i>PACKET_DEFAULT</i> and <i>PACKET_PASSPHRASE</i> outside of the computer. If the user forgets a passphrase, and you can access the computer, decrypt <i>PACKET_DEFAULT</i> using the certificate private key (which should never leave a secure machine):</p>
<dl>
<dd><code>volume_key &#8211;reencrypt -d</code> <i>NSS_DB</i> <i>PACKET_DEFAULT</i> <code>-o</code> <i>PACKET_DEFAULT_PW</i></dl>
<p> Then boot the computer (e.g. using a &quot;rescue mode&quot;), copy <i>PACKET_DEFAULT_PW</i> to it, and restore access to the volume:</p>
<dl>
<dd><code>volume_key &#8211;restore</code> <i>VOLUME PACKET_DEFAULT_PW</i></dl>
<p> If the user forgets the passphrase, and you cannot access the computer, decrypt the backup passphrase:</p>
<dl>
<dd><code>volume_key &#8211;secrets</code> <i>PACKET_PASSPHRASE</i></dl>
<p> and tell the backup passphrase to the user. (You can later generate a new backup passphrase.) </p>
