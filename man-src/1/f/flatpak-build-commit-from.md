---
title: "flatpak-build-commit-from(1)"
name: "flatpak-build-commit-from"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-build-commit-from/"
description: "flatpak-build-commit-from – Create new commits based on existing one (possibly from another repository)"
---

<h2 class="name">NAME</h2>
<p> flatpak-build-commit-from &#8211; Create new commits based on existing one (possibly from another repository) </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak build-commit-from</code> [OPTION&#8230;] DST-REPO DST-REF&#8230;</dl>
<h2>DESCRIPTION</h2>
<dd>Creates new commits on the DST-REF branch in the DST-REPO, with the contents (and most of the metadata) taken from another branch, either from another repo, or from another branch in the same repository. </p>
<p> The collection ID set on DST-REPO (if set) will be used for the newly created commits. </p>
<p> This command is very useful when you want to maintain a branch with a clean history that has no unsigned or broken commits. For instance, you can import the head from a different repository from an automatic builder when you&#8217;ve verified that it worked. The new commit will have no parents or signatures from the autobuilder, and can be properly signed with the official key. </p>
<p> Any deltas that affect the original commit and that match parent commits in the destination repository are copied and rewritten for the new commit id.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;src-repo=SRC-REPO</code></p>
<dl>
<dt>
<dd> The (local) repository to pull the source branch from. Defaults to the destination repository.</dl>
<p> <code>&#8211;src-ref=SRC-REF</code></p>
<dl>
<dt>
<dd> The branch to use as the source for the new commit. Defaults to the same as the destination ref, which is useful only if a different source repo has been specified.</dl>
<p> <code>&#8211;extra-collection-id=COLLECTION-ID</code></p>
<dl>
<dt>
<dd> Add an extra collection-ref binding for this collection, in addition to whatever would normally be added due to the destination repository collection id. This option can be used multiple times.</dl>
<p> <code>&#8211;untrusted</code></p>
<dl>
<dt>
<dd> The source repostory is not trusted, all objects are copied (not hardlinked) and all checksums are verified.</dl>
<p> <code>-s</code>, <code>&#8211;subject=SUBJECT</code></p>
<dl>
<dt>
<dd> One line subject for the commit message. If not specified, will be taken from the source commit.</dl>
<p> <code>-b</code>, <code>&#8211;body=BODY</code></p>
<dl>
<dt>
<dd> Full description for the commit message. If not specified, will be taken from the source commit.</dl>
<p> <code>&#8211;update-appstream</code></p>
<dl>
<dt>
<dd> Update the appstream branch after the build.</dl>
<p> <code>&#8211;no-update-summary</code></p>
<dl>
<dt>
<dd> Don&#8217;t update the summary file after the new commit is added. This means the repository will not be useful for serving over http until build-update-repo has been run. This is useful is you want to do multiple repo operations before finally updating the summary.</dl>
<p> <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Create new commit even if the content didn&#8217;t change from the existing branch head.</dl>
<p> <code>&#8211;disable-fsync</code></p>
<dl>
<dt>
<dd> Don&#8217;t fsync when writing to the repository. This can result in data loss in exceptional situations, but can improve performance when working with temporary or test repositories.</dl>
<p> <code>&#8211;gpg-sign=KEYID</code></p>
<dl>
<dt>
<dd> Sign the commit with this GPG key. This option can be used multiple times.</dl>
<p> <code>&#8211;gpg-homedir=PATH</code></p>
<dl>
<dt>
<dd> GPG Homedir to use when looking for keyrings</dl>
<p> <code>&#8211;end-of-life=REASON</code></p>
<dl>
<dt>
<dd> Mark build as end-of-life</dl>
<p> <code>&#8211;end-of-life-rebase=OLDID=NEWID</code></p>
<dl>
<dt>
<dd> Mark new refs as end-of-life. Unlike <code>&#8211;end-of-life</code>, this one takes an ID that supersedes the current one. By the user&#8217;s request, the application data may be preserved for the new application. Note, this is actually a prefix match, so if you say org.the.app=org.new.app, then something like org.the.app.Locale will be rebased to org.new.app.Locale.</dl>
<p> <code>&#8211;timestamp=TIMESTAMP</code></p>
<dl>
<dt>
<dd> Override the timestamp of the commit. Use an ISO 8601 formatted date, or NOW for the current time</dl>
<p> <code>&#8211;disable-fsync</code></p>
<dl>
<dt>
<dd> Don&#8217;t fsync when writing to the repository. This can result in data loss in exceptional situations, but can improve performance when working with temporary or test repositories.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> To revert a commit to the commit before: </p>
<p> <code>$ flatpak build-commit-from &#8211;timestamp=NOW &#8211;src-ref=app/org.gnome.gedit/x86_64/master^ repo app/org.gnome.gedit/x86_64/master</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ostree/">ostree</a></code>(1), <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-init/">flatpak-build-init</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build/">flatpak-build</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-finish/">flatpak-build-finish</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-sign/">flatpak-build-sign</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-update-repo/">flatpak-build-update-repo</a></code>(1) </p>
<h2>Index</h2>
