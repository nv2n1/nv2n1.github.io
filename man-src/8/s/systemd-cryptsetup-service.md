---
title: "systemd-cryptsetup-service(8)"
name: "systemd-cryptsetup-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-cryptsetup-service/"
description: "systemd-cryptsetup [at] .service, systemd-cryptsetup – Full disk decryption logic"
---

<p>systemd-cryptsetup [at] .service, systemd-cryptsetup &#8211; Full disk decryption logic</p>
<h2>Synopsis</h2>
<p>systemd-cryptsetup [at] .service </p>
<p> system-systemd-cryptsetup.slice </p>
<p> /lib/systemd/systemd-cryptsetup</p>
<h2>Description</h2>
<p>systemd-cryptsetup [at] .service is a service responsible for setting up encrypted block devices. It is instantiated for each device that requires decryption for access. </p>
<p> systemd-cryptsetup [at] .service instances are part of the system-systemd-cryptsetup.slice slice, which is destroyed only very late in the shutdown procedure. This allows the encrypted devices to remain up until filesystems have been unmounted. </p>
<p> systemd-cryptsetup [at] .service will ask for hard disk passwords via the m[blue]<code>password agent logic</code>m[]<font SIZE="-2">[1]</font>, in order to query the user for the password using the right mechanism at boot and during runtime. </p>
<p> At early boot and when the system manager configuration is reloaded, /etc/crypttab is translated into systemd-cryptsetup [at] .service units by <code><a href="/docs/linux/man/8-systemd-cryptsetup-generator/">systemd-cryptsetup-generator</a></code>(8). </p>
<p> In order to unlock a volume a password or binary key is required. systemd-cryptsetup [at] .service tries to acquire a suitable password or binary key via the following mechanisms, tried in order: </p>
<dl>
<dd>1. If a key file is explicitly configured (via the third column in /etc/crypttab), a key read from it is used. If a PKCS#11 token, FIDO2 token or TPM2 device is configured (using the <i>pkcs11-uri=</i>, <i>fido2-device=</i>, <i>tpm2-device=</i> options) the key is decrypted before use.</dl>
<dl>
<dd>2. If no key file is configured explicitly this way, a key file is automatically loaded from /etc/cryptsetup-keys.d/<i>volume</i>.key and /run/cryptsetup-keys.d/<i>volume</i>.key, if present. Here too, if a PKCS#11/FIDO2/TPM2 token/device is configured, any key found this way is decrypted before use.</dl>
<dl>
<dd>3. If the <i>try-empty-password</i> option is specified it is then attempted to unlock the volume with an empty password.</dl>
<dl>
<dd>4. The kernel keyring is then checked for a suitable cached password from previous attempts.</dl>
<dl>
<dd>5. Finally, the user is queried for a password, possibly multiple times, unless the <i>headless</i> option is set.</dl>
<p> If no suitable key may be acquired via any of the mechanisms describes above, volume activation fails.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-cryptsetup-generator/">systemd-cryptsetup-generator</a></code>(8), <code><a href="/docs/linux/man/5-crypttab/">crypttab</a></code>(5), <code><a href="/docs/linux/man/1-systemd-cryptenroll/">systemd-cryptenroll</a></code>(1), <code><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>password agent logic</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/PASSWORD_AGENTS/">https://systemd.io/PASSWORD_AGENTS/</a></dl>
