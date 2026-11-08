---
title: "TPM 2.0: Understanding Platform Configuration Registers"
date: 2024-12-14 09:09:40 +0000
author: "Eric Ma"
layout: post
categories: [systems-architecture]
canonical: /understanding-tpm-2-0-and-platform-configuration-registers-pcrs/
---

The Trusted Platform Module (TPM) 2.0 is a cryptographic coprocessor—either as discrete hardware or firmware—that provides hardware-rooted security. It’s the foundation for features like Windows Hello, BitLocker, macOS FileVault, and Linux dm-crypt integration with hardware key binding. On modern systems, TPM 2.0 is nearly universal: integrated into recent Intel (PTT), AMD (fTPM), and ARM processors, or available as discrete chips on enterprise hardware.

Unlike TPM 1.2, TPM 2.0 uses stronger cryptography (SHA-256 and later), supports more complex policies, and is genuinely recoverable if locked out—critical for production systems.

## Platform Configuration Registers (PCRs)

Platform Configuration Registers are protected memory banks inside the TPM that store cryptographic digests of system components. Each PCR is a hash value (typically SHA-256), and once written, it can only be extended—new values are hashed with the existing PCR value, making modification impossible without reboot.

The standard PCR assignments are:

- **PCR 0**: UEFI firmware code and settings
- **PCR 1**: UEFI firmware configuration
- **PCR 2**: UEFI GPT partition table
- **PCR 3**: UEFI boot variables
- **PCR 4**: Bootloader and GRUB configuration (UEFI/Secure Boot path)
- **PCR 5**: GPT partition table alterations, Secure Boot state transitions
- **PCR 7**: Secure Boot state, firmware and OS-specific security policies
- **PCR 8 and 9**: Linux kernel and initramfs (when using systemd-boot or GRUB with TPM measurement)
- **PCR 10**: IMa (Integrity Measurement Architecture) for user-space binaries on Linux

Note that UEFI firmware is responsible for measuring PCR 0–7 at boot time. On Linux systems with IMA enabled, the kernel measures user-space files into PCR 10 at runtime.

## How Measured Boot Works

Measured boot is a chain of trust: each component measures and extends the next, creating an auditable record of what executed.

1.  **Pre-boot**: Firmware verifies its own signature, measures itself into PCR 0, then measures the bootloader.
2.  **Bootloader**: The bootloader (e.g., GRUB, systemd-boot) measures kernel and initramfs, extending PCR 4 and PCR 8–9.
3.  **Kernel**: The Linux kernel extends PCR 10 with IMA measurements of loaded binaries.
4.  **Attestation**: The TPM can prove—via a signed quote—that each PCR matches an expected value, proving the system booted cleanly.

If malware modifies the bootloader or kernel, the PCR hash changes. Systems configured with PCR policies will then refuse to unseal encryption keys, preventing both boot and decryption.

## Checking PCR Values on Linux

To view current PCR values:

``` bash
tpm2_pcrread
```

Output example:

      0  : 0xB123456789ABCDEF...
      4  : 0xA987654321FEDCBA...
      7  : 0xC111111111111111...
     10  : 0xD222222222222222...

To read a specific PCR:

``` bash
tpm2_pcrread 0
```

To retrieve the event log (which PCR banks were extended and why):

``` bash
cat /sys/kernel/security/tpm0/binary_bios_measurements | hexdump -C
```

On systems with IMA enabled:

``` bash
cat /sys/kernel/security/ima/ascii_runtime_measurements
```

## Sealing Data to PCR Values

You can encrypt a secret (like a LUKS passphrase) so it’s only accessible if specific PCR values match. This is done via **unsealing**:

``` bash
# Create a sealed secret
echo "my-secret" | tpm2_seal -L "pcr:sha256:0,4,7" -o secret.sealed

# Later, unseal (only works if PCR 0, 4, 7 match original values)
tpm2_unseal -i secret.sealed
```

If PCR values differ, `tpm2_unseal` fails, leaving the secret inaccessible. This powers automated encrypted-root-filesystem unlocking: if firmware or bootloader is tampered with, the root password stays locked.

## TPM 2.0 in Production and Security Use Cases

**WebAuthn and Passkeys**: TPM 2.0 generates, stores, and never exports ECDSA or RSA private keys for passwordless login. Even if the OS is compromised, the key remains in the TPM. Windows Hello on Windows 11 and modern Linux systems (via libfido2 and systemd-homed) use TPM for key storage.

**Encrypted Root Filesystems**: systemd-cryptenroll can bind LUKS encryption to TPM and PCR policy, automatically unlocking the root filesystem only on clean boot. Example:

``` bash
systemd-cryptenroll /dev/sda1 --tpm2-device=auto --tpm2-pcrs=0,4,7
```

**Remote Attestation**: Cloud platforms (AWS, Azure, GCP) and Kubernetes clusters verify TPM attestation before admitting nodes. A node proves—via a signed PCR quote—that it’s running approved firmware and kernel versions.

``` bash
tpm2_quote -c 0x81000001 -l sha256:0,4,7,10 -m attest.out -s sig.out
```

**Hardware Wallets**: Dedicated TPM-based devices or secure enclaves use TPM principles to store cryptocurrency keys, preventing key extraction even under physical attack.

## Common Pitfalls

- **Changing firmware or kernel without re-measuring**: PCRs become stale. Re-sealing is required after OS updates.
- **Not enabling Secure Boot**: PCR 7 won’t reflect security state changes. Measured boot is weaker without it.
- **Ignoring IMA/EVM on production systems**: Userspace binaries can be modified post-boot. Enable IMA with `ima=on` kernel parameter for complete coverage.
- **Losing PCR values across OS upgrades**: Document expected PCR values before upgrading. Use `tpm2_eventlog` to correlate changes.

Modern Linux distributions (RHEL 9+, Ubuntu 22.04+, Fedora 37+) ship with TPM support enabled by default. For maximum security, pair TPM 2.0 with Secure Boot, UEFI Capsule updates, and measured boot attestation in your infrastructure tooling.
