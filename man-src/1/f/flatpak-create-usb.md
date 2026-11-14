---
title: "flatpak-create-usb(1)"
name: "flatpak-create-usb"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-create-usb/"
description: "flatpak-create-usb – Copy apps and/or runtimes onto removable media."
---

<h2 class="name">NAME</h2>
<p> flatpak-create-usb &#8211; Copy apps and/or runtimes onto removable media. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak create-usb</code> [OPTION&#8230;] MOUNT-PATH REF&#8230;</dl>
<h2>DESCRIPTION</h2>
<dd>Copies the specified apps and/or runtimes REFs onto the removable media mounted at MOUNT-PATH, along with all the dependencies and metadata needed for installing them. This is one way of transferring flatpaks between computers that doesn&#8217;t require an Internet connection. After using this command, the USB drive can be connected to another computer and <code>flatpak install</code> will prefer to install from it rather than the Internet if (a) each ref comes from a configured remote whose GPG keyring will be used for verification and (b) the refs on the drive are at least as new as what&#8217;s available elsewhere (e.g. the Internet if you&#8217;re online). For this process to work a collection ID must be configured on the relevant remotes on both the source and destination computers, and on the remote server. </p>
<p> On the destination computer one can install from the USB (or any mounted filesystem) the same way you would install from the Internet, e.g. with <code>flatpak install flathub org.gnome.Builder</code> or using a GUI. </p>
<p> Each REF argument is a full or partial identifier in the flatpak ref format, which looks like &quot;(app|runtime)/ID/ARCH/BRANCH&quot;. All elements except ID are optional and can be left out, including the slashes, so most of the time you need only specify ID. Any part left out will be matched against what is installed, and if there are multiple matches an error message will list the alternatives. </p>
<p> By default this looks for both installed apps and runtimes with the given REF, but you can limit this by using the <code>&#8211;app</code> or <code>&#8211;runtime</code> option. </p>
<p> All REFs must be in the same installation (user, system, or other). Otherwise it&#8217;s ambiguous which repository metadata refs to put on the USB drive. </p>
<p> By default <code>flatpak create-usb</code> uses .ostree/repo as the destination directory under MOUNT-PATH but if you specify another location using <code>&#8211;destination-repo</code> a symbolic link will be created for you in .ostree/repos.d. This ensures that either way the repository will be found by flatpak (and other consumers of libostree) for install/update operations. </p>
<p> Unless overridden with the <code>&#8211;system</code>, <code>&#8211;user</code>, or <code>&#8211;installation</code> options, this command searches both the system-wide installation and the per-user one for REF and errors out if it exists in more than one.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Copy refs from the per-user installation.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Copy refs from the default system-wide installation.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Copy refs from a system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
<p> <code>&#8211;app</code></p>
<dl>
<dt>
<dd> Assume that all REFs are apps if not explicitly specified.</dl>
<p> <code>&#8211;runtime</code></p>
<dl>
<dt>
<dd> Assume that all REFs are runtimes if not explicitly specified.</dl>
<p> <code>&#8211;destination-repo</code>=DEST</p>
<dl>
<dt>
<dd> Create the repository in DEST under MOUNT-PATH, rather than the default location.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak create-usb /run/media/mwleeds/1a9b4cb2-a7ef-4d9b-91a5-6eaf8fdd2bf6/ com.endlessm.wiki_art.en</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-install/">flatpak-install</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-list/">flatpak-list</a></code>(1), <code><a href="/docs/linux/man/1-ostree-create-usb/">ostree-create-usb</a></code>(1) </p>
<h2>Index</h2>
