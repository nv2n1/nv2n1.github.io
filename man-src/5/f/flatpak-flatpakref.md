---
title: "flatpak-flatpakref(5)"
name: "flatpak-flatpakref"
section: "5"
letter: "f"
url: "/docs/linux/man/5-flatpak-flatpakref/"
description: "flatpak-flatpakref – Reference to a remote for an application or runtime"
---

<p>flatpak-flatpakref &#8211; Reference to a remote for an application or runtime</p>
<h2>Description</h2>
<p>Flatpak uses flatpakref files to share information about a remote for a single application. The flatpakref file contains enough information to add the remote and install the application. Use the <code>flatpak install &#8211;from</code> command to do so. </p>
<p> flatpakref files may also contain additional information that is useful when displaying the application to the user, e.g. in an app store. </p>
<p> The filename extension commonly used for flatpakref files is .flatpakref. </p>
<p> A flatpakref file can also refer to a remote for a runtime.</p>
<h2>File Format</h2>
<p>The flatpakref file is using the same .ini file format that is used for systemd unit files or application .desktop files.</p>
<h3>[Flatpak Ref]</h3>
<p>All the information is contained in the [Flatpak Ref] group. </p>
<p> The following keys can be present in this group: </p>
<p> <code>Version</code> (uint64)</p>
<dl>
<dd>The version of the file format, must be 1 if present.</dl>
<p> <code>Name</code> (string)</p>
<dl>
<dd>The fully qualified name of the runtime or application. This key is mandatory.</dl>
<p> <code>Url</code> (string)</p>
<dl>
<dd>The url for the remote. This key is mandatory.</dl>
<p> <code>Branch</code> (string)</p>
<dl>
<dd>The name of the branch from which to install the application or runtime. If this key is not specified, the &quot;master&quot; branch is used.</dl>
<p> <code>Title</code> (string)</p>
<dl>
<dd>The title of the application or runtime. This should be a user-friendly name that can be displayed e.g. in an app store.</dl>
<p> <code>Comment</code> (string)</p>
<dl>
<dd>A short summary of the application or runtime, for display e.g. in an app store.</dl>
<p> <code>Description</code> (string)</p>
<dl>
<dd>A longer description of the application or runtime, for display e.g. in an app store.</dl>
<p> <code>Icon</code> (string)</p>
<dl>
<dd>The url for an icon that can be used to represent the application or runtime.</dl>
<p> <code>Homepage</code> (string)</p>
<dl>
<dd>The url of a webpage describing the application or runtime.</dl>
<p> <code>DeployCollectionID</code> (string)</p>
<dl>
<dd>The collection ID of the remote, if it has one. This uniquely identifies the collection of apps in the remote, to allow peer to peer redistribution. It is recommended to use this key over CollectionID because only newer clients pay attention to it (and older clients don&#8217;t handle collection IDs properly).</dl>
<p> <code>CollectionID</code> (string)</p>
<dl>
<dd>This is deprecated but still supported for backwards compatibility. Use DeployCollectionID instead.</dl>
<p> <code>IsRuntime</code> (boolean)</p>
<dl>
<dd>Whether this file refers to a runtime. If this key is not specified, the file is assumed to refer to an application.</dl>
<p> <code>GPGKey</code> (string)</p>
<dl>
<dd>The base64-encoded gpg key for the remote.</dl>
<p> <code>RuntimeRepo</code> (string)</p>
<dl>
<dd>The url for a .flatpakrepo file for the remote where the runtime can be found.</dl>
<p> <code>SuggestRemoteName</code> (string)</p>
<dl>
<dd>A suggested name for the remote.</dl>
<h2>Example</h2>
<dl>
<dd>
<pre>[Flatpak Ref]
Title=gedit
Name=org.gnome.gedit
Branch=stable
Url=<a rel="nofollow" href="http://sdk.gnome.org/repo-apps/">http://sdk.gnome.org/repo-apps/</a>
IsRuntime=False
GPGKey=mQENBFUUCGcBCAC/K9WeV4xCaKr3NKRqPXeY5mpaXAJyasLqCtrDx92WUgbu0voWrhohNAKpqizod2dvzc/XTxm3rHyIxmNfdhz1gaGhynU75Qw4aJVcly2eghTIl++gfDtOvrOZo/VuAq30f32dMIgHQdRwEpgCwz7WyjpqZYltPAEcCNL4MTChAfiHJeeiQ5ibystNBW8W6Ymf7sO4m4g5+/aOxI54oCOzD9TwBAe+yXcJJWtc2rAhMCjtyPJzxd0ZVXqIzCe1xRvJ6Rq7YCiMbiM2DQFWXKnmYQbj4TGNMnwNdAajCdrcBWEMSbzq7EzuThIJRd8Ky4BkEe1St6tuqwFaMZz+F9eXABEBAAG0KEdub21lIFNESyAzLjE2IDxnbm9tZS1vcy1saXN0QGdub21lLm9yZz6JATgEEwECACIFAlUUCGcCGwMGCwkIBwMCBhUIAgkKCwQWAgMBAh4BAheAAAoJEArkz6VV0VKBa5cH/0vXa31YgEjNk78gGFXqnQxdD1WYA87OYxDi189l4lA802EFTF4wCBuZyDOqdd5BhS3Ab0cR778DmZXRUP2gwe+1zTJypU2JMnDpkwJ4NK1VP6/tE4SAPrznBtmb76BKaWBqUfZ9Wq1zg3ugvqkZB/Exq+usypIOwQVp1KL58TrjBRda0HvRctzkNhr0qYAtkfLFe0GvksBp4vBm8uGwAx7fw/HbhIjQ9pekTwvB+5GwDPO/tSip/1bQfCS+XJB8Ffa04HYPLGedalnWBrwhYY+G/kn5Zh9L/AC8xeLwTJTHM212rBjPa9CWs9C6a57MSaeGIEHLC1hEyiJJ15w8jmY=
DeployCollectionID=org.gnome.Apps</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-install/">flatpak-install</a></code>(1) <code><a href="/docs/linux/man/5-flatpak-flatpakrepo/">flatpak-flatpakrepo</a></code>(5), </p>
