---
title: "org-freedesktop-portable1(5)"
name: "org-freedesktop-portable1"
section: "5"
letter: "o"
url: "/docs/linux/man/5-org-freedesktop-portable1/"
description: "org.freedesktop.portable1 – The D-Bus interface of systemd-portabled"
---

<p>org.freedesktop.portable1 &#8211; The D-Bus interface of systemd-portabled</p>
<h2>Introduction</h2>
<p><code><a href="/docs/linux/man/8-systemd-portabled-service/">systemd-portabled.service</a></code>(8) is a system service that may be used to attach, detach and inspect portable services. This page describes the D-Bus interface.</p>
<h2>The Manager Object</h2>
<p>The service exposes the following interfaces on the Manager object on the bus: </p>
<dl>
<dd>
<pre>node /org/freedesktop/portable1 {
 interface org.freedesktop.portable1.Manager {
 methods:
 GetImage(in s image,
 out o object);
 ListImages(out a(ssbtttso) images);
 GetImageOSRelease(in s image,
 out a{ss} os_release);
 GetImageMetadata(in s image,
 in as matches,
 out s image,
 out ay os_release,
 out a{say} units);
 GetImageMetadataWithExtensions(in s image,
 in as extensions,
 in as matches,
 in t flags,
 out s image,
 out ay os_release,
 out a{say} extensions,
 out a{say} units);
 GetImageState(in s image,
 out s state);
 AttachImage(in s image,
 in as matches,
 in s profile,
 in b runtime,
 in s copy_mode,
 out a(sss) changes);
 AttachImageWithExtensions(in s image,
 in as extensions,
 in as matches,
 in s profile,
 in s copy_mode,
 in t flags,
 out a(sss) changes);
 DetachImage(in s image,
 in b runtime,
 out a(sss) changes);
 DetachImageWithExtensions(in s image,
 in as extensions,
 in t flags,
 out a(sss) changes);
 ReattachImage(in s image,
 in as matches,
 in s profile,
 in b runtime,
 in s copy_mode,
 out a(sss) changes_removed,
 out a(sss) changes_updated);
 ReattachImageWithExtensions(in s image,
 in as extensions,
 in as matches,
 in s profile,
 in s copy_mode,
 in t flags,
 out a(sss) changes_removed,
 out a(sss) changes_updated);
 RemoveImage(in s image);
 MarkImageReadOnly(in s image,
 in b read_only);
 SetImageLimit(in s image,
 in t limit);
 SetPoolLimit(in t limit);
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s PoolPath = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t PoolUsage = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t PoolLimit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly as Profiles = ['...', ...];
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
};</pre>
</dl>
<h3>Methods</h3>
<p><code>GetImage()</code> may be used to get the image object path of the image with the specified name. </p>
<p> <code>ListImages()</code> returns an array of all currently known images. The structures in the array consist of the following fields: image name, type, read-only flag, creation time, modification time, current disk space, usage and image object path. </p>
<p> <code>GetImageOSRelease()</code> retrieves the OS release information of an image. This method returns an array of key value pairs read from the <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) file in the image and is useful to identify the operating system used in a portable service. </p>
<p> <code>GetImageMetadata()</code> retrieves metadata associated with an image. This method returns the image name, the image&#8217;s <code><a href="/docs/linux/man/5-os-release/">os-release</a></code>(5) content in the form of a (streamable) array of bytes, and a list of portable units contained in the image, in the form of a string (unit name) and an array of bytes with the content. </p>
<p> <code>GetImageMetadataWithExtensions()</code> retrieves metadata associated with an image. This method is a superset of <code>GetImageMetadata()</code> with the addition of a list of extensions as input parameter, which were overlaid on top of the main image via <code>AttachImageWithExtensions()</code>. The path of each extension and an array of bytes with the content of the respective extension-release file are returned, one such structure for each extension named in the input arguments. </p>
<p> <code>GetImageState()</code> retrieves the image state as one of the following strings: </p>
<dl>
<dd>&bull; detached</dl>
<dl>
<dd>&bull; attached</dl>
<dl>
<dd>&bull; attached-runtime</dl>
<dl>
<dd>&bull; enabled</dl>
<dl>
<dd>&bull; enabled-runtime</dl>
<dl>
<dd>&bull; running</dl>
<dl>
<dd>&bull; running-runtime</dl>
<p> <code>AttachImage()</code> attaches a portable image to the system. This method takes an image path or name, a list of strings that will be used to search for unit files inside the image (partial or complete matches), a string indicating which portable profile to use for the image (see <i>Profiles</i> property for a list of available profiles), a boolean indicating whether to attach the image only for the current boot session, and a string representing the preferred copy mode (whether to copy the image or to just symlink it) with the following possible values: </p>
<dl>
<dd>&bull; (null)</dl>
<dl>
<dd>&bull; copy</dl>
<dl>
<dd>&bull; symlink</dl>
<p> This method returns the list of changes applied to the system (for example, which unit was added and is now available as a system service). Each change is represented as a triplet of strings: the type of change applied, the path on which it was applied, and the source (if any). The type of change applied will be one of the following possible values: </p>
<dl>
<dd>&bull; copy</dl>
<dl>
<dd>&bull; symlink</dl>
<dl>
<dd>&bull; write</dl>
<dl>
<dd>&bull; mkdir</dl>
<p> Note that an image cannot be attached if a unit that it contains is already present on the system. </p>
<p> <code>AttachImageWithExtensions()</code> attaches a portable image to the system. This method is a superset of <code>AttachImage()</code> with the addition of a list of extensions as input parameter, which will be overlaid on top of the main image. When this method is used, detaching must be done by passing the same arguments via the <code>DetachImageWithExtensions()</code> method. For more details on this functionality, see the <i>MountImages=</i> entry on <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) and <code><a href="/docs/linux/man/8-systemd-sysext/">systemd-sysext</a></code>(8). The <i>flag</i> parameter is currently unused and reserved for future purposes. </p>
<p> <code>DetachImage()</code> detaches a portable image from the system. This method takes an image path or name, and a boolean indicating whether the image to detach was attached only for the current boot session or persistently. This method returns the list of changes applied to the system (for example, which unit was removed and is no longer available as a system service). Each change is represented as a triplet of strings: the type of change applied, the path on which it was applied, and the source (if any). The type of change applied will be one of the following possible values: </p>
<dl>
<dd>&bull; unlink</dl>
<p> Note that an image cannot be detached if a unit that it contains is running. </p>
<p> <code>DetachImageWithExtensions()</code> detaches a portable image from the system. This method is a superset of <code>DetachImage()</code> with the addition of a list of extensions as input parameter, which were overlaid on top of the main image via <code>AttachImageWithExtensions()</code>. The <i>flag</i> parameter is currently unused and reserved for future purposes. </p>
<p> <code>ReattachImage()</code> combines the effects of the <code>AttachImage()</code> method and the <code>DetachImage()</code> method. The difference is that it is allowed to reattach an image while one or more of its units are running. The reattach operation will fail if no matching image is attached. The input parameters match the <code>AttachImage()</code> method, and the return parameters are the combination of the return parameters of the <code>DetachImage()</code> method (first array, units that were removed) and the <code>AttachImage()</code> method (second array, units that were updated or added). </p>
<p> <code>ReattachImageWithExtensions()</code> reattaches a portable image to the system. This method is a superset of <code>ReattachImage()</code> with the addition of a list of extensions as input parameter, which will be overlaid on top of the main image. For more details on this functionality, see the <i>MountImages=</i> entry on <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) and <code><a href="/docs/linux/man/8-systemd-sysext/">systemd-sysext</a></code>(8). The <i>flag</i> parameter is currently unused and reserved for future purposes </p>
<p> <code>RemoveImage()</code> removes the image with the specified name. </p>
<p> <code>MarkImageReadOnly()</code> toggles the read-only flag of an image. </p>
<p> <code>SetPoolLimit()</code> sets an overall quota limit on the pool of images. </p>
<p> <code>SetImageLimit()</code> sets a per-image quota limit. </p>
<p> The <code>AttachImageWithExtensions()</code>, <code>DetachImageWithExtensions()</code> and <code>ReattachImageWithExtensions()</code> methods take in options as flags instead of booleans to allow for extendability, defined as follows: </p>
<dl>
<dd>
<pre>#define SD_SYSTEMD_PORTABLE_RUNTIME (<a href="//www.systutorials.com/docs/linux/man/1-UINT64_C/">UINT64_C</a>(1) &lt;&lt; 0)</pre>
</dl>
<h3>Properties</h3>
<p><i>PoolPath</i> specifies the file system path where images are written to. </p>
<p> <i>PoolUsage</i> specifies the current usage size of the image pool in bytes. </p>
<p> <i>PoolLimit</i> specifies the size limit of the image pool in bytes. </p>
<p> <i>Profiles</i> specifies the available runtime profiles for portable services.</p>
<h2>The Image Object</h2>
<p>The service exposes the following interfaces on the Image object on the bus: </p>
<dl>
<dd>
<pre>node /org/freedesktop/portable1 {
 interface org.freedesktop.portable1.Image {
 methods:
 GetOSRelease(out a{ss} os_release);
 GetMetadata(in as matches,
 out s image,
 out ay os_release,
 out a{say} units);
 GetMetadataWithExtensions(in as extensions,
 in as matches,
 in t flags,
 out s image,
 out ay os_release,
 out a{say} extensions,
 out a{say} units);
 GetState(out s state);
 Attach(in as matches,
 in s profile,
 in b runtime,
 in s copy_mode,
 out a(sss) changes);
 AttachWithExtensions(in as extensions,
 in as matches,
 in s profile,
 in s copy_mode,
 in t flags,
 out a(sss) changes);
 Detach(in b runtime,
 out a(sss) changes);
 DetachWithExtensions(in as extensions,
 in t flags,
 out a(sss) changes);
 Reattach(in as matches,
 in s profile,
 in b runtime,
 in s copy_mode,
 out a(sss) changes_removed,
 out a(sss) changes_updated);
 ReattacheWithExtensions(in as extensions,
 in as matches,
 in s profile,
 in s copy_mode,
 in t flags,
 out a(sss) changes_removed,
 out a(sss) changes_updated);
 Remove();
 MarkReadOnly(in b read_only);
 SetLimit(in t limit);
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s Name = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s Path = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly s Type = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b ReadOnly = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t CreationTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t ModificationTimestamp = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t Usage = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t Limit = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t UsageExclusive = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t LimitExclusive = ...;
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
};</pre>
</dl>
<h3>Methods</h3>
<p>The following methods implement the same operation as the respective methods on the Manager object (see above). However, these methods operate on the image object and hence does not take an image name parameter. Invoking the methods directly on the Manager object has the advantage of not requiring a <code>GetImage()</code> call to get the image object for a specific image name. Calling the methods on the Manager object is hence a round trip optimization. List of methods: </p>
<dl>
<dd>&bull; GetOSRelease()</dl>
<dl>
<dd>&bull; GetMetadata()</dl>
<dl>
<dd>&bull; GetMetadataWithExtensions()</dl>
<dl>
<dd>&bull; GetState()</dl>
<dl>
<dd>&bull; Attach()</dl>
<dl>
<dd>&bull; AttachWithExtensions()</dl>
<dl>
<dd>&bull; Detach()</dl>
<dl>
<dd>&bull; DetachWithExtensions()</dl>
<dl>
<dd>&bull; Reattach()</dl>
<dl>
<dd>&bull; ReattacheWithExtensions()</dl>
<dl>
<dd>&bull; Remove()</dl>
<dl>
<dd>&bull; MarkReadOnly()</dl>
<dl>
<dd>&bull; SetLimit()</dl>
<h3>Properties</h3>
<p><i>Name</i> specifies the image name. </p>
<p> <i>Path</i> specifies the file system path where image is stored. </p>
<p> <i>Type</i> specifies the image type. </p>
<p> <i>ReadOnly</i> specifies whether the image is read-only. </p>
<p> <i>CreationTimestamp</i> specifies the image creation timestamp. </p>
<p> <i>ModificationTimestamp</i> specifies the image modification timestamp. </p>
<p> <i>Usage</i> specifies the image disk usage. </p>
<p> <i>Limit</i> specifies the image disk usage limit. </p>
<p> <i>UsageExclusive</i> specifies the image disk usage (exclusive). </p>
<p> <i>LimitExclusive</i> specifies the image disk usage limit (exclusive).</p>
<h2>Versioning</h2>
<p>These D-Bus interfaces follow m[blue]<code>the usual interface versioning guidelines</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>the usual interface versioning guidelines</p>
<dl>
<dd><a rel="nofollow" href="http://0pointer.de/blog/projects/versioning-dbus.html">http://0pointer.de/blog/projects/versioning-dbus.html</a></dl>
