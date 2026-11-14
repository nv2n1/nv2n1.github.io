---
title: "flatpak-build-update-repo(1)"
name: "flatpak-build-update-repo"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-build-update-repo/"
description: "flatpak-build-update-repo – Create a repository from a build directory"
---

<h2 class="name">NAME</h2>
<p> flatpak-build-update-repo &#8211; Create a repository from a build directory </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak build-update-repo</code> [OPTION&#8230;] LOCATION</dl>
<h2>DESCRIPTION</h2>
<dd>Updates repository metadata for the repository at LOCATION. This command generates an OSTree summary file that lists the contents of the repository. The summary is used by flatpak remote-ls and other commands to display the contents of remote repositories. </p>
<p> After this command, LOCATION can be used as the repository location for flatpak remote-add, either by exporting it over http, or directly with a file: url.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;redirect-url=URL</code></p>
<dl>
<dt>
<dd> Redirect this repo to a new URL.</dl>
<p> <code>&#8211;title=TITLE</code></p>
<dl>
<dt>
<dd> A title for the repository, e.g. for display in a UI. The title is stored in the repository summary.</dl>
<p> <code>&#8211;comment=COMMENT</code></p>
<dl>
<dt>
<dd> A single-line comment for the remote, e.g. for display in a UI. The comment is stored in the repository summary.</dl>
<p> <code>&#8211;description=DESCRIPTION</code></p>
<dl>
<dt>
<dd> A full-paragraph description for the remote, e.g. for display in a UI. The description is stored in the repository summary.</dl>
<p> <code>&#8211;homepage=URL</code></p>
<dl>
<dt>
<dd> URL for a website for the remote, e.g. for display in a UI. The url is stored in the repository summary.</dl>
<p> <code>&#8211;icon=URL</code></p>
<dl>
<dt>
<dd> URL for an icon for the remote, e.g. for display in a UI. The url is stored in the repository summary.</dl>
<p> <code>&#8211;default-branch=BRANCH</code></p>
<dl>
<dt>
<dd> A default branch for the repository, mainly for use in a UI.</dl>
<p> <code>&#8211;gpg-import=FILE</code></p>
<dl>
<dt>
<dd> Import a new default GPG public key from the given file.</dl>
<p> <code>&#8211;collection-id=COLLECTION-ID</code></p>
<dl>
<dt>
<dd> The globally unique identifier of the remote repository, to allow mirrors to be grouped. This must be set to a globally unique reverse DNS string if the repository is to be made publicly available. If a collection ID is already set on an existing repository, this will update it. If not specified, the existing collection ID will be left unchanged.</dl>
<p> <code>&#8211;deploy-collection-id</code></p>
<dl>
<dt>
<dd> Deploy the collection ID (set using <code>&#8211;collection-id</code>) in the static remote configuration for all clients. This is irrevocable once published in a repository. Use it to decide when to roll out a collection ID to users of an existing repository. If constructing a new repository which has a collection ID, you should typically always pass this option.</dl>
<p> <code>&#8211;gpg-sign=KEYID</code></p>
<dl>
<dt>
<dd> Sign the commit with this GPG key. This option can be used multiple times.</dl>
<p> <code>&#8211;gpg-homedir=PATH</code></p>
<dl>
<dt>
<dd> GPG Homedir to use when looking for keyrings</dl>
<p> <code>&#8211;generate-static-deltas</code></p>
<dl>
<dt>
<dd> Generate static deltas for all references. This generates from-empty and delta static files that allow for faster download.</dl>
<p> <code>&#8211;static-delta-jobs=NUM-JOBS</code></p>
<dl>
<dt>
<dd> Limit the number of parallel jobs creating static deltas. The default is the number of cpus.</dl>
<p> <code>&#8211;static-delta-ignore-ref=PATTERN</code></p>
<dl>
<dt>
<dd> Don&#8217;t generate deltas for runtime or application id matching this pattern. For instance, &#8211;static-delta-ignore-ref=*.Sources means there will not be any deltas for source refs.</dl>
<p> <code>&#8211;prune</code></p>
<dl>
<dt>
<dd> Remove unreferenced objects in repo.</dl>
<p> <code>&#8211;prune-depth</code></p>
<dl>
<dt>
<dd> Only keep at most this number of old versions for any particular ref. Default is -1 which means infinite.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ostree/">ostree</a></code>(1), <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-remote-ls/">flatpak-remote-ls</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-export/">flatpak-build-export</a></code>(1) </p>
<h2>Index</h2>
