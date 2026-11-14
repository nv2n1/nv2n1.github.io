---
title: "flatpak-remote-modify(1)"
name: "flatpak-remote-modify"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-remote-modify/"
description: "flatpak-remote-modify – Modify a remote repository"
---

<h2 class="name">NAME</h2>
<p> flatpak-remote-modify &#8211; Modify a remote repository </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak remote-modify</code> [OPTION&#8230;] NAME</dl>
<h2>DESCRIPTION</h2>
<dd>Modifies options for an existing remote repository in the flatpak repository configuration. NAME is the name for the remote. </p>
<p> Unless overridden with the <code>&#8211;system</code>, <code>&#8211;user</code>, or <code>&#8211;installation</code> options, this command uses either the default system-wide installation or the per-user one, depending on which has the specified REMOTE.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Modify the per-user configuration.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Modify the default system-wide configuration.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Modify a system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
<p> <code>&#8211;no-gpg-verify</code></p>
<dl>
<dt>
<dd> Disable GPG verification for the added remote.</dl>
<p> <code>&#8211;gpg-verify</code></p>
<dl>
<dt>
<dd> Enable GPG verification for the added remote.</dl>
<p> <code>&#8211;prio=PRIO</code></p>
<dl>
<dt>
<dd> Set the priority for the remote. Default is 1, higher is more prioritized. This is mainly used for graphical installation tools.</dl>
<p> <code>&#8211;no-enumerate</code></p>
<dl>
<dt>
<dd> Mark the remote as not enumerated. This means the remote will not be used to list applications, for instance in graphical installation tools.</dl>
<p> <code>&#8211;no-use-for-deps</code></p>
<dl>
<dt>
<dd> Mark the remote as not to be used for automatic runtime dependency resolution.</dl>
<p> <code>&#8211;disable</code></p>
<dl>
<dt>
<dd> Disable the remote. Disabled remotes will not be automatically updated from.</dl>
<p> <code>&#8211;enable</code></p>
<dl>
<dt>
<dd> Enable the remote.</dl>
<p> <code>&#8211;enumerate</code></p>
<dl>
<dt>
<dd> Mark the remote as enumerated. This means the remote will be used to list applications, for instance in graphical installation tools.</dl>
<p> <code>&#8211;use-for-deps</code></p>
<dl>
<dt>
<dd> Mark the remote as to be used for automatic runtime dependency resolution.</dl>
<p> <code>&#8211;title=TITLE</code></p>
<dl>
<dt>
<dd> A title for the remote, e.g. for display in a UI.</dl>
<p> <code>&#8211;comment=COMMENT</code></p>
<dl>
<dt>
<dd> A single-line comment for the remote, e.g. for display in a UI.</dl>
<p> <code>&#8211;description=DESCRIPTION</code></p>
<dl>
<dt>
<dd> A full-paragraph description for the remote, e.g. for display in a UI.</dl>
<p> <code>&#8211;homepage=URL</code></p>
<dl>
<dt>
<dd> URL for a website for the remote, e.g. for display in a UI.</dl>
<p> <code>&#8211;icon=URL</code></p>
<dl>
<dt>
<dd> URL for an icon for the remote, e.g. for display in a UI.</dl>
<p> <code>&#8211;default-branch=BRANCH</code></p>
<dl>
<dt>
<dd> A default branch for the remote, mainly for use in a UI.</dl>
<p> <code>&#8211;collection-id=COLLECTION-ID</code></p>
<dl>
<dt>
<dd> The globally unique identifier of the remote repository, to allow mirrors to be grouped. This must only be set to the collection ID provided by the remote, and must not be set if the remote does not provide a collection ID.</dl>
<p> <code>&#8211;url=URL</code></p>
<dl>
<dt>
<dd> Set a new URL.</dl>
<p> <code>&#8211;update-metadata</code></p>
<dl>
<dt>
<dd> Update the remote&#8217;s extra metadata from the OSTree repository&#8217;s summary file. Only xa.title and xa.default-branch are supported at the moment.</dl>
<p> <code>&#8211;no-filter</code>, <code>&#8211;filter=FILE</code></p>
<dl>
<dt>
<dd> Modify the path (or unset) for the local filter used for this remote. See <code><a href="/docs/linux/man/1-flatpak-remote-add/">flatpak-remote-add</a></code>(1) for details about the filter file format.</dl>
<p> <code>&#8211;gpg-import=FILE</code></p>
<dl>
<dt>
<dd> Import gpg keys from the specified keyring file as trusted for the new remote. If the file is &#8211; the keyring is read from standard input.</dl>
<p> <code>&#8211;authenticator-name=NAME</code></p>
<dl>
<dt>
<dd> Specify the authenticator to use for the remote.</dl>
<p> <code>&#8211;authenticator-option=KEY=VALUE</code></p>
<dl>
<dt>
<dd> Specify an authenticator option for the remote.</dl>
<p> <code>&#8211;authenticator-install</code></p>
<dl>
<dt>
<dd> Enable auto-installation of authenticator.</dl>
<p> <code>&#8211;no-authenticator-install</code></p>
<dl>
<dt>
<dd> Disable auto-installation of authenticator.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak &#8211;user remote-modify &#8211;no-gpg-verify test-repo</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-remote-add/">flatpak-remote-add</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-remote-delete/">flatpak-remote-delete</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-remotes/">flatpak-remotes</a></code>(1) </p>
<h2>Index</h2>
