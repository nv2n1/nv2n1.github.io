---
title: "systemd-cryptenroll(1)"
name: "systemd-cryptenroll"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-cryptenroll/"
description: "systemd-cryptenroll – Enroll PKCS#11, FIDO2, TPM2 token/devices to LUKS2 encrypted volumes"
---

<h2 class="name">NAME</h2>
<p> systemd-cryptenroll &#8211; Enroll PKCS#11, FIDO2, TPM2 token/devices to LUKS2 encrypted volumes </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-cryptenroll </code><code>[OPTIONS&#8230;]</code><code>[DEVICE]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-cryptenroll</code></p>
<dd>is a tool for enrolling hardware security tokens and devices into a LUKS2 encrypted volume, which may then be used to unlock the volume during boot. Specifically, it supports tokens and credentials of the following kind to be enrolled: </p>
<dl>
<dt>
<dd> 1. PKCS#11 security tokens and smartcards that may carry an RSA key pair (e.g. various YubiKeys)</dl>
<dl>
<dt>
<dd> 2. FIDO2 security tokens that implement the &quot;hmac-secret&quot; extension (most FIDO2 keys, including YubiKeys)</dl>
<dl>
<dt>
<dd> 3. TPM2 security devices</dl>
<dl>
<dt>
<dd> 4. Recovery keys. These are similar to regular passphrases, however are randomly generated on the computer and thus generally have higher entropy than user chosen passphrases. Their character set has been designed to ensure they are easy to type in, while having high entropy. They may also be scanned off screen using QR codes. Recovery keys may be used for unlocking LUKS2 volumes wherever passphrases are accepted. They are intended to be used in combination with an enrolled hardware security token, as a recovery option when the token is lost.</dl>
<dl>
<dt>
<dd> 5. Regular passphrases</dl>
<p> In addition, the tool may be used to enumerate currently enrolled security tokens and wipe a subset of them. The latter may be combined with the enrollment operation of a new security token, in order to update or replace enrollments. </p>
<p> The tool supports only LUKS2 volumes, as it stores token meta-information in the LUKS2 JSON token area, which is not available in other encryption formats.</p>
<h2>LIMITATIONS</h2>
<p> Note that currently when enrolling a new key of one of the five supported types listed above, it is required to first provide a passphrase or recovery key (i.e. one of the latter two key types). For example, it&#8217;s currently not possible to unlock a device with a FIDO2 key in order to enroll a new FIDO2 key. Instead, in order to enroll a new FIDO2 key, it is necessary to provide an already enrolled regular passphrase or recovery key. Thus, if in future key roll-over is desired it&#8217;s generally recommended to combine TPM2, FIDO2, PKCS#11 key enrollment with enrolling a regular passphrase or recovery key. </p>
<p> Also note that support for enrolling multiple FIDO2 tokens is currently not too useful, as while unlocking <code>systemd-cryptsetup</code> cannot identify which token is currently plugged in and thus does not know which authentication request to send to the device. This limitation does not apply to tokens enrolled via PKCS#11 &#8212; because tokens of this type may be identified immediately, before authentication.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;password</code></p>
<dl>
<dt>
<dd> Enroll a regular password/passphrase. This command is mostly equivalent to <code>cryptsetup luksAddKey</code>, however may be combined with <code>&#8211;wipe-slot=</code> in one call, see below.</dl>
<p> <code>&#8211;recovery-key</code></p>
<dl>
<dt>
<dd> Enroll a recovery key. Recovery keys are most identical to passphrases, but are computer generated instead of human chosen, and thus have a guaranteed high entropy. The key uses a character set that is easy to type in, and may be scanned off screen via a QR code.</dl>
<p> <code>&#8211;pkcs11-token-uri=</code><i>URI</i></p>
<dl>
<dt>
<dd> Enroll a PKCS#11 security token or smartcard (e.g. a YubiKey). Expects a PKCS#11 smartcard URI referring to the token. Alternatively the special value &quot;auto&quot; may be specified, in order to automatically determine the URI of a currently plugged in security token (of which there must be exactly one). The special value &quot;list&quot; may be used to enumerate all suitable PKCS#11 tokens currently plugged in. The security token must contain an RSA key pair which is used to encrypt the randomly generated key that is used to unlock the LUKS2 volume. The encrypted key is then stored in the LUKS2 JSON token header area. </p>
<p> In order to unlock a LUKS2 volume with an enrolled PKCS#11 security token, specify the <code>pkcs11-uri=</code> option in the respective /etc/crypttab line: </p>
<dl>
<dt>
<dd>
<pre>
myvolume /dev/sda1 - pkcs11-uri=auto
</pre>
</dl>
<p> See <code><a href="/docs/linux/man/5-crypttab/">crypttab</a></code>(5) for a more comprehensive example of a <code>systemd-cryptenroll</code> invocation and its matching /etc/crypttab line.</dl>
<p> <code>&#8211;fido2-device=</code><i>PATH</i></p>
<dl>
<dt>
<dd> Enroll a FIDO2 security token that implements the &quot;hmac-secret&quot; extension (e.g. a YubiKey). Expects a hidraw device referring to the FIDO2 device (e.g. /dev/hidraw1). Alternatively the special value &quot;auto&quot; may be specified, in order to automatically determine the device node of a currently plugged in security token (of which there must be exactly one). The special value &quot;list&quot; may be used to enumerate all suitable FIDO2 tokens currently plugged in. Note that many hardware security tokens that implement FIDO2 also implement the older PKCS#11 standard. Typically FIDO2 is preferable, given it&#8217;s simpler to use and more modern. </p>
<p> In order to unlock a LUKS2 volume with an enrolled FIDO2 security token, specify the <code>fido2-device=</code> option in the respective /etc/crypttab line: </p>
<dl>
<dt>
<dd>
<pre>
myvolume /dev/sda1 - fido2-device=auto
</pre>
</dl>
<p> See <code><a href="/docs/linux/man/5-crypttab/">crypttab</a></code>(5) for a more comprehensive example of a <code>systemd-cryptenroll</code> invocation and its matching /etc/crypttab line.</dl>
<p> <code>&#8211;fido2-with-client-pin=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> When enrolling a FIDO2 security token, controls whether to require the user to enter a PIN when unlocking the volume (the FIDO2 &quot;clientPin&quot; feature). Defaults to &quot;yes&quot;. (Note: this setting is without effect if the security token does not support the &quot;clientPin&quot; feature at all, or does not allow enabling or disabling it.)</dl>
<p> <code>&#8211;fido2-with-user-presence=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> When enrolling a FIDO2 security token, controls whether to require the user to verify presence (tap the token, the FIDO2 &quot;up&quot; feature) when unlocking the volume. Defaults to &quot;yes&quot;. (Note: this setting is without effect if the security token does not support the &quot;up&quot; feature at all, or does not allow enabling or disabling it.)</dl>
<p> <code>&#8211;fido2-with-user-verification=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> When enrolling a FIDO2 security token, controls whether to require user verification when unlocking the volume (the FIDO2 &quot;uv&quot; feature). Defaults to &quot;no&quot;. (Note: this setting is without effect if the security token does not support the &quot;uv&quot; feature at all, or does not allow enabling or disabling it.)</dl>
<p> <code>&#8211;tpm2-device=</code><i>PATH</i></p>
<dl>
<dt>
<dd> Enroll a TPM2 security chip. Expects a device node path referring to the TPM2 chip (e.g. /dev/tpmrm0). Alternatively the special value &quot;auto&quot; may be specified, in order to automatically determine the device node of a currently discovered TPM2 device (of which there must be exactly one). The special value &quot;list&quot; may be used to enumerate all suitable TPM2 devices currently discovered. </p>
<p> In order to unlock a LUKS2 volume with an enrolled TPM2 security chip, specify the <code>tpm2-device=</code> option in the respective /etc/crypttab line: </p>
<dl>
<dt>
<dd>
<pre>
myvolume /dev/sda1 - tpm2-device=auto
</pre>
</dl>
<p> See <code><a href="/docs/linux/man/5-crypttab/">crypttab</a></code>(5) for a more comprehensive example of a <code>systemd-cryptenroll</code> invocation and its matching /etc/crypttab line. </p>
<p> Use <code>&#8211;tpm2-pcrs=</code> (see below) to configure which TPM2 PCR indexes to bind the enrollment to.</dl>
<p> <code>&#8211;tpm2-pcrs=</code> [PCR&#8230;]</p>
<dl>
<dt>
<dd> Configures the TPM2 PCRs (Platform Configuration Registers) to bind the enrollment requested via <code>&#8211;tpm2-device=</code> to. Takes a &quot;+&quot; separated list of numeric PCR indexes in the range 0&#8230;23. If not used, defaults to PCR 7 only. If an empty string is specified, binds the enrollment to no PCRs at all. PCRs allow binding the enrollment to specific software versions and system state, so that the enrolled unlocking key is only accessible (may be &quot;unsealed&quot;) if specific trusted software and/or configuration is used. </p>
<p> <code>Table 1. Well-known PCR Definitions</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> PCR </code></td>
<td><code> Explanation </code>
</td>
</tr>
<tr VALIGN=top>
<td> 0 </td>
<td> Core system firmware executable code; changes on firmware updates
</td>
</tr>
<tr VALIGN=top>
<td> 1 </td>
<td> Core system firmware data/host platform configuration; typically contains serial and model numbers, changes on basic hardware/CPU/RAM replacements
</td>
</tr>
<tr VALIGN=top>
<td> 2 </td>
<td> Extended or pluggable executable code; includes option ROMs on pluggable hardware
</td>
</tr>
<tr VALIGN=top>
<td> 3 </td>
<td> Extended or pluggable firmware data; includes information about pluggable hardware
</td>
</tr>
<tr VALIGN=top>
<td> 4 </td>
<td> Boot loader; changes on boot loader updates
</td>
</tr>
<tr VALIGN=top>
<td> 5 </td>
<td> GPT/Partition table; changes when the partitions are added, modified or removed
</td>
</tr>
<tr VALIGN=top>
<td> 6 </td>
<td> Power state events; changes on system suspend/sleep
</td>
</tr>
<tr VALIGN=top>
<td> 7 </td>
<td> Secure boot state; changes when UEFI SecureBoot mode is enabled/disabled
</td>
</tr>
<tr VALIGN=top>
<td> 8 </td>
<td> <code><a href="/docs/linux/man/7-sd-boot/">sd-boot</a></code>(7) measures the kernel command line in this PCR.
</td>
</tr>
</table>
</dl>
<p> <code>&#8211;wipe-slot=</code> [SLOT&#8230;]</p>
<dl>
<dt>
<dd> Wipes one or more LUKS2 key slots. Takes a comma separated list of numeric slot indexes, or the special strings &quot;all&quot; (for wiping all key slots), &quot;empty&quot; (for wiping all key slots that are unlocked by an empty passphrase), &quot;password&quot; (for wiping all key slots that are unlocked by a traditional passphrase), &quot;recovery&quot; (for wiping all key slots that are unlocked by a recovery key), &quot;pkcs11&quot; (for wiping all key slots that are unlocked by a PKCS#11 token), &quot;fido2&quot; (for wiping all key slots that are unlocked by a FIDO2 token), &quot;tpm2&quot; (for wiping all key slots that are unlocked by a TPM2 chip), or any combination of these strings or numeric indexes, in which case all slots matching either are wiped. As safety precaution an operation that wipes all slots without exception (so that the volume cannot be unlocked at all anymore, unless the volume key is known) is refused. </p>
<p> This switch may be used alone, in which case only the requested wipe operation is executed. It may also be used in combination with any of the enrollment options listed above, in which case the enrollment is completed first, and only when successful the wipe operation executed &#8212; and the newly added slot is always excluded from the wiping. Combining enrollment and slot wiping may thus be used to update existing enrollments: </p>
<dl>
<dt>
<dd>
<pre>
systemd-cryptenroll /dev/sda1 --wipe-slot=tpm2 --tpm2-device=auto
</pre>
</dl>
<p> The above command will enroll the TPM2 chip, and then wipe all previously created TPM2 enrollments on the LUKS2 volume, leaving only the newly created one. Combining wiping and enrollment may also be used to replace enrollments of different types, for example for changing from a PKCS#11 enrollment to a FIDO2 one: </p>
<dl>
<dt>
<dd>
<pre>
systemd-cryptenroll /dev/sda1 --wipe-slot=pkcs11 --fido2-device=auto
</pre>
</dl>
<p> Or for replacing an enrolled empty password by TPM2: </p>
<dl>
<dt>
<dd>
<pre>
systemd-cryptenroll /dev/sda1 --wipe-slot=empty --tpm2-device=auto
</pre>
</dl>
</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code>systemd-cryptsetup [at] .service</code>(8), <code><a href="/docs/linux/man/5-crypttab/">crypttab</a></code>(5), <code><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a></code>(8) </p>
<h2>Index</h2>
