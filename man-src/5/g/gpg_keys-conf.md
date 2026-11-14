---
title: "gpg_keys-conf(5)"
name: "gpg_keys-conf"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gpg_keys-conf/"
---

gpg_keys.conf - Configuration file for abrt-action-save-package-data.

<h2>Description</h2>

The configuration file consists of items in the format &quot;Option = Value&quot;. Currently, only one item exists: 

 GPGKeysDir = <i>directory</i>
<dl><dd>The path of the directory which contains files with GPG keys of known RPM repositories. These keys are used to verify package signatures. Example: /etc/pki/rpm-gpg</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-abrt-action-save-package-data/">abrt-action-save-package-data</a>(1) <a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5)

<h2>Authors</h2>

<dl><dd>&bull; ABRT team</dl>
