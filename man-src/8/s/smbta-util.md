---
title: "smbta-util(8)"
name: "smbta-util"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbta-util/"
description: "smbta-util – control encryption in VFS smb_traffic_analyzer"
---

<p>smbta-util &#8211; control encryption in VFS smb_traffic_analyzer</p>
<h2>Synopsis</h2>
<dl>
<dd>smbta-util [<i>COMMANDS</i>&#8230;]</dl>
<h2>Description</h2>
<p>This tool is part of the <code><a href="/docs/linux/man/1-samba/">samba</a></code>(1) suite. </p>
<p> smbta-util is a tool to ease the configuration of the vfs_smb_traffic_analyzer module regarding data encryption. </p>
<p> The user can generate a key, install a key (activating encryption), or uninstall a key (deactivating encryption). Any operation that installs a key will create a File containing the key. This file can be used by smbta-tool on other machines to install the same key from the file.</p>
<h2>Commands</h2>
<p><code>-h</code></p>
<dl>
<dd>Show a short help text on the command line.</dl>
<p> <code>-f</code> <i>KEYFILE</i></p>
<dl>
<dd>Open an existing keyfile, read the key from the file, and install the key, activating encryption.</dl>
<p> <code>-g</code> <i>KEYFILE</i></p>
<dl>
<dd>Generate a new random key, install the key, activate encryption, and store the key into the file KEYFILE.</dl>
<p> <code>-u</code></p>
<dl>
<dd>Uninstall the key, deactivating encryption.</dl>
<p> <code>-s</code></p>
<dl>
<dd>Check if a key is installed.</dl>
<p> <code>-c</code> <i>KEYFILE</i></p>
<dl>
<dd>Create a KEYFILE from an installed key.</dl>
<h2>Version</h2>
<p>This man page is correct for version 3.4 of the Samba suite.</p>
<h2>Author</h2>
<p>The original version of smbta-util was created by Holger Hetterich. </p>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
