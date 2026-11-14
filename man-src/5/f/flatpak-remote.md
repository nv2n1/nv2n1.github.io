---
title: "flatpak-remote(5)"
name: "flatpak-remote"
section: "5"
letter: "f"
url: "/docs/linux/man/5-flatpak-remote/"
description: "flatpak-remote – Configuration for a remote"
---

<p>flatpak-remote &#8211; Configuration for a remote</p>
<h2>Description</h2>
<p>Flatpak stores information about configured remotes for an installation location in $installation/repo/config. For example, the remotes for the default system-wide installation are in $prefix/var/lib/flatpak/repo/config, and the remotes for the per-user installation are in $HOME/.local/share/flatpak/repo/config. </p>
<p> Normally, it is not necessary to edit remote config files directly, the <code>flatpak remote-modify</code> command should be used to change properties of remotes. </p>
<p> System-wide remotes can be statically preconfigured by dropping flatpakref files into /etc/flatpak/remotes.d/.</p>
<h2>File Format</h2>
<p>The remote config file format is using the same .ini file format that is used for systemd unit files or application .desktop files.</p>
<h3>[remote &#8230;]</h3>
<p>All the configuration for the the remote with name NAME is contained in the [remote &quot;NAME&quot;] group. </p>
<p> The following keys are recognized by OSTree, among others: </p>
<p> <code>url</code> (string)</p>
<dl>
<dd>The url for the remote. An URL of the form oci+https:// or oci+http:// is a Flatpak extension that indicates that the remote is not an ostree repository, but is rather an URL to an index of OCI images that are stored within a container image registry.</dl>
<p> <code>gpg-verify</code> (boolean)</p>
<dl>
<dd>Whether to use GPG verification for content from this remote.</dl>
<p> <code>gpg-verify-summary</code> (boolean)</p>
<dl>
<dd>Whether to use GPG verification for the summary of this remote. </p>
<p> This is ignored if <code>collection-id</code> is set, as refs are verified in commit metadata in that case. Enabling <code>gpg-verify-summary</code> would break peer to peer distribution of refs.</dl>
<p> <code>collection-id</code> (string)</p>
<dl>
<dd>The globally unique identifier for the upstream collection repository, to allow mirrors to be grouped.</dl>
<p> All flatpak-specific keys have a xa. prefix: </p>
<p> <code>xa.disable</code> (boolean)</p>
<dl>
<dd>Whether the remote is disabled. Defaults to false.</dl>
<p> <code>xa.prio</code> (integer)</p>
<dl>
<dd>The priority for the remote. This is used when listing remotes. Defaults to 1.</dl>
<p> <code>xa.noenumerate</code> (boolean)</p>
<dl>
<dd>Whether this remote should be used when presenting available contents. Defaults to true.</dl>
<p> <code>xa.nodeps</code> (boolean)</p>
<dl>
<dd>Whether this remote should be used when searching for dependencies. Defaults to true.</dl>
<p> <code>xa.title</code> (string)</p>
<dl>
<dd>An optional title to use when presenting this remote in a UI.</dl>
<p> <code>xa.title-is-set</code> (boolean)</p>
<dl>
<dd>This key is set to true if <code>xa.title</code> has been explicitly set.</dl>
<p> <code>xa.comment</code> (string)</p>
<dl>
<dd>An optional single-line comment to use when presenting this remote in a UI.</dl>
<p> <code>xa.comment-is-set</code> (boolean)</p>
<dl>
<dd>This key is set to true if <code>xa.comment</code> has been explicitly set.</dl>
<p> <code>xa.description</code> (string)</p>
<dl>
<dd>An optional full-paragraph of text to use when presenting this remote in a UI.</dl>
<p> <code>xa.description-is-set</code> (boolean)</p>
<dl>
<dd>This key is set to true if <code>xa.description</code> has been explicitly set.</dl>
<p> <code>xa.homepage</code> (string)</p>
<dl>
<dd>An optional URL that points to a website for this repository to use when presenting this remote in a UI.</dl>
<p> <code>xa.homepage-is-set</code> (boolean)</p>
<dl>
<dd>This key is set to true if <code>xa.homepage</code> has been explicitly set.</dl>
<p> <code>xa.icon</code> (string)</p>
<dl>
<dd>An optional URL that points to an icon for this repository to use when presenting this remote in a UI.</dl>
<p> <code>xa.icon-is-set</code> (boolean)</p>
<dl>
<dd>This key is set to true if <code>xa.icon</code> has been explicitly set.</dl>
<p> <code>xa.default-branch</code> (string)</p>
<dl>
<dd>The default branch to use when installing from this remote.</dl>
<p> <code>xa.default-branch-is-set</code> (boolean)</p>
<dl>
<dd>This key is set to true if <code>xa.default-branch</code> has been explicitly set.</dl>
<p> <code>xa.main-ref</code> (string)</p>
<dl>
<dd>The main reference served by this remote. This is used for origin remotes of applications installed via a flatpakref file.</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre>[remote &quot;gnome-nightly-apps&quot;]
gpg-verify=true
gpg-verify-summary=true
url=<a rel="nofollow" href="https://sdk.gnome.org/nightly/repo-apps/">https://sdk.gnome.org/nightly/repo-apps/</a>
xa.title=GNOME Applications</pre>
</dl>
<dl>
<dd>
<pre>[remote &quot;flathub&quot;]
gpg-verify=true
gpg-verify-summary=false
collection-id=org.flathub.Stable
url=<a rel="nofollow" href="https://dl.flathub.org/repo/">https://dl.flathub.org/repo/</a>
xa.title=Flathub</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-flatpak-remote-modify/">flatpak-remote-modify</a></code>(1) </p>
