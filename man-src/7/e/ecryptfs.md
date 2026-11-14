---
title: "ecryptfs(7)"
name: "ecryptfs"
section: "7"
letter: "e"
url: "/docs/linux/man/7-ecryptfs/"
description: "eCryptfs – an enterprise-class cryptographic filesystem for linux"
---

<p>eCryptfs &#8211; an enterprise-class cryptographic filesystem for linux</p>
<h2>Synopsis</h2>
<p><code>mount -t ecryptfs [SRC DIR] [DST DIR] -o [OPTIONS]</code> </p>
<h2>Description</h2>
<p>eCryptfs is a POSIX-compliant enterprise-class stacked cryptographic filesystem for Linux. It is derived from Erez Zadok&#8217;s Cryptfs, implemented through the FiST framework for generating stacked filesystems. eCryptfs extends Cryptfs to provide advanced key management and policy features. eCryptfs stores cryptographic metadata in the header of each file written, so that encrypted files can be copied between hosts; the file will be decryptable with the proper key, and there is no need to keep track of any additional information aside from what is already in the encrypted file itself. Think of eCryptfs as a sort of &quot;gnupgfs.&quot; </p>
<h2>Options</h2>
<p>KERNEL OPTIONS </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Parameters that apply to the eCryptfs kernel module.</p>
<dl>
<dt><code>ecryptfs_sig=(fekek_sig)</code></p>
<dd>Specify the signature of the mount wide authentication token. The authentication token must be in the kernel keyring before the mount is performed. ecryptfs-manager or the eCryptfs mount helper can be used to construct the authentication token and add it to the keyring prior to mounting.</p>
<dt><code>ecryptfs_fnek_sig=(fnek_sig)</code></p>
<dd>Specify the signature of the mount wide authentication token used for filename crypto. The authentication must be in the kernel keyring before mounting.</p>
<dt><code>ecryptfs_cipher=(cipher)</code></p>
<dd>Specify the symmetric cipher to be used on a per file basis</p>
<dt><code>ecryptfs_key_bytes=(key_bytes)</code></p>
<dd>Specify the keysize to be used with the selected cipher. If the cipher only has one keysize the keysize does not need to be specified.</p>
<dt><code>ecryptfs_passthrough</code></p>
<dd>Allows for non-eCryptfs files to be read and written from within an eCryptfs mount. This option is turned off by default.</p>
<dt><code>no_sig_cache</code></p>
<dd>Do not check the mount key signature against the values in the user&#8217;s ~/.ecryptfs/sig-cache.txt file. This is useful for such things as non-interactive setup scripts, so that the mount helper does not stop and prompt the user in the event that the key sig is not in the cache.</p>
<dt><code>ecryptfs_encrypted_view</code></p>
<dd>This option provides a unified encrypted file format of the eCryptfs files in the lower mount point. Currently, it is only useful if the lower mount point contains files with the metadata stored in the extended attribute. Upon a file read in the upper mount point, the encrypted version of the file will be presented with the metadata in the file header instead of the xattr. Files cannot be opened for writing when this option is enabled.</p>
<dt><code>ecryptfs_xattr</code></p>
<dd>Store the metadata in the extended attribute of the lower files rather than the header region of the lower files.</p>
<dt><code>verbose</code></p>
<dd>Log ecryptfs information to /var/log/messages. Do not run eCryptfs in verbose-mode unless you are doing so for the sole purpose of development, since secret values will be written out to the system log in that case.</p>
<dd>MOUNT HELPER OPTIONS </p>
<p> Parameters that apply to the eCryptfs mount helper. </p>
<dt><code>key=(keytype):[KEY MODULE OPTIONS]</code></p>
<dd>Specify the type of key to be used when mounting eCryptfs.</p>
<dt><code>ecryptfs_enable_filename_crypto=(y/n)</code></p>
<dd>Specify whether filename encryption should be enabled. If not, the mount helper will not prompt the user for the filename encryption key signature (default).</p>
<dt><code>verbosity=0/1</code></p>
<dd>If verbosity=1, the mount helper will ask you for missing values (default). Otherwise, if verbosity=0, it will not ask for missing values and will fail if required values are omitted.</p>
<dd>KEY MODULE OPTIONS </p>
<p> Parameters that apply to individual key modules have the alias for the key module in the prefix of the parameter name. Key modules are pluggable, and which key modules are available on any given system is dependent upon whatever happens to be installed in /usr/lib*/ecryptfs/. </p>
<dt><code>passphrase_passwd=(passphrase)</code></p>
<dd>The actual password is passphrase. Since the password is visible to utilities (like ps under Unix) this form should only be used where security is not important.</p>
<dt><code>passphrase_passwd_file=(filename)</code></p>
<dd>The password should be specified in a file with passphrase_passwd_file=(passphrase). It is highly recommended that the file be stored on a secure medium such as a personal usb key.</p>
<dt><code>passphrase_passwd_fd=(file descriptor)</code></p>
<dd>The password is specified through the specified file descriptor.</p>
<dt><code>passphrase_salt=(hex value)</code></p>
<dd>The salt should be specified as a 16 digit hex value.</p>
<dt><code>openssl_keyfile=(filename)</code></p>
<dd>The filename should be the filename of a file containing an RSA SSL key.</p>
<dt><code>openssl_passwd_file=(filename)</code></p>
<dd>The password should be specified in a file with openssl_passwd=(openssl-password). It is highly recommended that the file be stored on a secure medium such as a personal usb key.</p>
<dt><code>openssl_passwd_fd=(file descriptor)</code></p>
<dd>The password is specified through the specified file descriptor.</p>
<dt><code>openssl_passwd=(password)</code></p>
<dd>The password can be specified on the command line. Since the password is visible in the process list, it is highly recommended to use this option only for testing purposes. </p>
</dl>
<h2>Example</h2>
<p>The following command will layover mount eCryptfs on /secret with a passphrase contained in a file stored on secure media mounted at /mnt/usb/. <code>mount -t ecryptfs -o key=passphrase:passphrase_passwd_file=/mnt/usb/file.txt /secret /secret</code> Where file.txt contains the contents <code>&quot;passphrase_passwd=[passphrase]&quot;</code>. </p>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<dd>
<dt><i>/usr/share/doc/ecryptfs-utils/ecryptfs-faq.html</i></p>
<dd>
<dt><i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i></p>
<dd>
<h2>Notes</h2>
<p>Do not run eCryptfs in verbose-mode unless you are doing so for the sole purpose of development, since secret values will be written out to the system log in that case. Make certain that your eCryptfs mount covers all locations where your applications may write sensitive data. In addition, use dm-crypt to encrypt your swap space with a random key on boot, or see <code><a href="/docs/linux/man/1-ecryptfs-setup-swap/">ecryptfs-setup-swap</a></code>(1). Passphrases have a maximum length of 64 characters. </p>
<h2>Bugs</h2>
<p>Please post bug reports to the eCryptfs bug tracker on Launchpad.net: <a rel="nofollow" href="https://bugs.launchpad.net/ecryptfs/+filebug.">https://bugs.launchpad.net/ecryptfs/+filebug.</a> For kernel bugs, please follow the procedure detailed in Documentation/oops-tracing.txt to help us figure out what is happening. </p>
<h2>Author</h2>
<p>This manpage was (re-)written by Dustin Kirkland &lt;kirkland [at] ubuntu.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
