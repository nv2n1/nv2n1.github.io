---
title: "flatpak-remote-add(1)"
name: "flatpak-remote-add"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-remote-add/"
description: "flatpak-remote-add – Add a remote repository"
---

<h2 class="name">NAME</h2>
<p> flatpak-remote-add &#8211; Add a remote repository </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak remote-add</code> [OPTION&#8230;] NAME LOCATION</dl>
<h2>DESCRIPTION</h2>
<dd>Adds a remote repository to the flatpak repository configuration. NAME is the name for the new remote, and LOCATION is a url or pathname. The LOCATION is either a flatpak repository, or a .flatpakrepo file which describes a repository. In the former case you may also have to specify extra options, such as the gpg key for the repo. </p>
<p> Unless overridden with the <code>&#8211;user</code> or <code>&#8211;installation</code> options, this command changes the default system-wide installation.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;from</code></p>
<dl>
<dt>
<dd> Assume the URI is a .flatpakrepo file rather than the repository itself. This is enabled by default if the extension is .flatpakrepo, so generally you don&#8217;t need this option.</dl>
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
<p> <code>&#8211;if-not-exists</code></p>
<dl>
<dt>
<dd> Do nothing if the provided remote already exists.</dl>
<p> <code>&#8211;disable</code></p>
<dl>
<dt>
<dd> Disable the added remote.</dl>
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
<p> <code>&#8211;filter=PATH</code></p>
<dl>
<dt>
<dd> Add a local filter to the remote. A filter file is a list of lines, each file starting with &quot;allow&quot; or &quot;deny&quot;, and then a glob for the ref to allow or disallow. The globs specify a partial ref (i.e. you can leave out trailing parts which will then match everything), but otherwise only &quot;*&quot; is special, matching anything in that part of the ref. </p>
<p> By default all refs are allowed, but if a ref matches a deny rule it is disallowed unless it specifically matches an allow rule. This means you can use this to implement both whitelisting and blacklisting. </p>
<p> Here is an example filter file: </p>
<dl>
<dt>
<dd>
<pre>
# This is a whitelist style filter as it denies all first
deny *
allow runtime/org.freedesktop.*
allow org.some.app/arm
allow org.signal.Signal/*/stable
allow org.signal.Signal.*/*/stable
</pre>
</dl>
</dl>
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
<p> <code>$ flatpak remote-add gnome <a rel="nofollow" href="https://sdk.gnome.org/gnome.flatpakrepo">https://sdk.gnome.org/gnome.flatpakrepo</a></code> </p>
<p> <code>$ flatpak &#8211;user remote-add &#8211;no-gpg-verify test-repo <a rel="nofollow" href="https://people.gnome.org/~alexl/gnome-sdk/repo/">https://people.gnome.org/~alexl/gnome-sdk/repo/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-remote-modify/">flatpak-remote-modify</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-remote-delete/">flatpak-remote-delete</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-remotes/">flatpak-remotes</a></code>(1), <code><a href="/docs/linux/man/5-flatpak-flatpakrepo/">flatpak-flatpakrepo</a></code>(5) </p>
<h2>Index</h2>
