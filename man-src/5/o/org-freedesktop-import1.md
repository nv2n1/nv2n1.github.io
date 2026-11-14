---
title: "org-freedesktop-import1(5)"
name: "org-freedesktop-import1"
section: "5"
letter: "o"
url: "/docs/linux/man/5-org-freedesktop-import1/"
description: "org.freedesktop.import1 – The D-Bus interface of systemd-importd"
---

<p>org.freedesktop.import1 &#8211; The D-Bus interface of systemd-importd</p>
<h2>Introduction</h2>
<p><code><a href="/docs/linux/man/8-systemd-importd-service/">systemd-importd.service</a></code>(8) is a system service which may be used to import, export and download additional system images. These images can be used by tools such as <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1) to run local containers. The service is used as the backend for <code>machinectl pull-raw</code>, <code>machinectl pull-tar</code> and related commands. This page describes the D-Bus interface. </p>
<p> Note that <code><a href="/docs/linux/man/8-systemd-importd-service/">systemd-importd.service</a></code>(8) is mostly a small companion service for <code><a href="/docs/linux/man/8-systemd-machined-service/">systemd-machined.service</a></code>(8). Many operations to manipulate local container and VM images are hence available via the <code>systemd-machined</code> D-Bus API, c.f. <code><a href="/docs/linux/man/5-org-freedesktop-machine1/">org.freedesktop.machine1</a></code>(5).</p>
<h2>The Manager Object</h2>
<p>The service exposes the following interfaces on the Manager object on the bus: </p>
<dl>
<dd>
<pre>node /org/freedesktop/import1 {
 interface org.freedesktop.import1.Manager {
 methods:
 ImportTar(in h fd,
 in s local_name,
 in b force,
 in b read_only,
 out u transfer_id,
 out o transfer_path);
 ImportRaw(in h fd,
 in s local_name,
 in b force,
 in b read_only,
 out u transfer_id,
 out o transfer_path);
 ImportFileSystem(in h fd,
 in s local_name,
 in b force,
 in b read_only,
 out u transfer_id,
 out o transfer_path);
 ExportTar(in s local_name,
 in h fd,
 in s format,
 out u transfer_id,
 out o transfer_path);
 ExportRaw(in s local_name,
 in h fd,
 in s format,
 out u transfer_id,
 out o transfer_path);
 PullTar(in s url,
 in s local_name,
 in s verify_mode,
 in b force,
 out u transfer_id,
 out o transfer_path);
 PullRaw(in s url,
 in s local_name,
 in s verify_mode,
 in b force,
 out u transfer_id,
 out o transfer_path);
 ListTransfers(out a(usssdo) transfers);
 CancelTransfer(in u transfer_id);
 signals:
 TransferNew(u transfer_id,
 o transfer_path);
 TransferRemoved(u transfer_id,
 o transfer_path,
 s result);
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
};</pre>
</dl>
<h3>Methods</h3>
<p><code>ImportTar()</code> and <code>ImportRaw()</code> import a system image and place it into /var/lib/machines/. The first argument should be a file descriptor (opened for reading) referring to the tar or raw file to import. It should reference a file on disk, a pipe or a socket. When <code>ImportTar()</code> is used the file descriptor should refer to a tar file, optionally compressed with <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), or <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1). <code>systemd-importd</code> will detect the used compression scheme (if any) automatically. When <code>ImportRaw()</code> is used the file descriptor should refer to a raw or qcow2 disk image containing an MBR or GPT disk label, also optionally compressed with gzip, bzip2 or xz. In either case, if the file is specified as a file descriptor on disk, progress information is generated for the import operation (as in that case we know the total size on disk). If a socket or pipe is specified, progress information is not available. The file descriptor argument is followed by a local name for the image. This should be a name suitable as a hostname and will be used to name the imported image below /var/lib/machines/. A tar import is placed as a directory tree or a <code><a href="/docs/linux/man/8-btrfs/">btrfs</a></code>(8) subvolume below /var/lib/machines/ under the specified name with no suffix appended. A raw import is placed as a file in /var/lib/machines/ with the .raw suffix appended. If the <code>force</code> argument is true, any pre-existing image with the same name is removed before starting the operation. Otherwise, the operation fails if an image with the same name already exists. Finally, the <code>read_only</code> argument controls whether to create a writable or read-only image. Both methods return immediately after starting the import, with the import transfer ongoing. They return a pair of transfer identifier and object path, which may be used to retrieve progress information about the transfer or to cancel it. The transfer identifier is a simple numeric identifier, the object path references an org.freedesktop.import1.Transfer object, see below. Listen for a <code>TransferRemoved</code> signal for the transfer ID in order to detect when a transfer is complete. The returned transfer object is useful to determine the current progress or log output of the ongoing import operation. </p>
<p> <code>ExportTar()</code> and <code>ExportRaw()</code> implement the reverse operation, and may be used to export a system image in order to place it in a tar or raw image. They take the machine name to export as their first parameter, followed by a file descriptor (opened for writing) where the tar or raw file will be written. It may either reference a file on disk or a pipe/socket. The third argument specifies in which compression format to write the image. It takes one of &quot;uncompressed&quot;, &quot;xz&quot;, &quot;bzip2&quot; or &quot;gzip&quot;, depending on which compression scheme is required. The image written to the specified file descriptor will be a tar file in case of <code>ExportTar()</code> or a raw disk image in case of <code>ExportRaw()</code>. Note that currently raw disk images may not be exported as tar files, and vice versa. This restriction might be lifted eventually. The method returns a transfer identifier and object path for cancelling or tracking the export operation, similar to <code>ImportTar()</code> or <code>ImportRaw()</code> as described above. </p>
<p> <code>PullTar()</code> and <code>PullRaw()</code> may be used to download, verify and import a system image from a URL. They take an URL argument which should point to a tar or raw file on the &quot;http://&quot; or &quot;https://&quot; protocols, possibly compressed with xz, bzip2 or gzip. The second argument is a local name for the image. It should be suitable as a hostname, similar to the matching argument of the <code>ImportTar()</code> and <code>ImportRaw()</code> methods above. The third argument indicates the verification mode for the image. It may be one of &quot;no&quot;, &quot;checksum&quot;, &quot;signature&quot;. &quot;no&quot; turns off any kind of verification of the image; &quot;checksum&quot; looks for a SHA256SUM file next to the downloaded image and verifies any SHA256 hash value in that file against the image; &quot;signature&quot; does the same but also tries to authenticate the SHA256SUM file via <code><a href="/docs/linux/man/8-gpg/">gpg</a></code>(8) first. The last argument indicates whether to replace a possibly pre-existing image with the same local name (if &quot;true&quot;), or whether to fail (if &quot;false&quot;). Like the import and export calls above, these calls return a pair of transfer identifier and object path for the ongoing download. </p>
<p> <code>ListTransfers()</code> returns a list of ongoing import, export or download operations as created with the six calls described above. It returns an array of structures which consist of the numeric transfer identifier, a string indicating the operation (one of &quot;import-tar&quot;, &quot;import-raw&quot;, &quot;export-tar&quot;, &quot;export-raw&quot;, &quot;pull-tar&quot; or &quot;pull-raw&quot;), a string describing the remote file (in case of download operations this is the source URL, in case of import/export operations this is a short string describing the file descriptor passed in), a string with the local machine image name, a progress value between 0.0 (for 0%) and 1.0 (for 100%), as well as the transfer object path. </p>
<p> <code>CancelTransfer()</code> may be used to cancel an ongoing import, export or download operation. Simply specify the transfer identifier to cancel the ongoing operation.</p>
<h3>Signals</h3>
<p>The <code>TransferNew</code> signal is generated each time a new transfer is started with the import, export or download calls described above. It carries the transfer ID and object path that have just been created. </p>
<p> The <code>TransferRemoved</code> signal is sent each time a transfer finishes, is canceled or fails. It also carries the transfer ID and object path, followed by a string indicating the result of the operation, which is one of &quot;done&quot; (on success), &quot;canceled&quot; or &quot;failed&quot;.</p>
<h2>The Transfer Object</h2>
<dl>
<dd>
<pre>node /org/freedesktop/import1/transfer/_1 {
 interface org.freedesktop.import1.Transfer {
 methods:
 Cancel();
 signals:
 LogMessage(u priority,
 s line);
 properties:
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly u Id = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Local = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Remote = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Type = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;const&quot;)
 readonly s Verify = '...';
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly d Progress = ...;
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
};</pre>
</dl>
<h3>Methods</h3>
<p>The <code>Cancel()</code> method may be used to cancel the transfer. It takes no parameters. This method is pretty much equivalent to the <code>CancelTransfer()</code> method on the Manager interface (see above), but is exposed on the Transfer object itself instead of taking a transfer ID.</p>
<h3>Properties</h3>
<p>The <i>Id</i> property exposes the numeric transfer ID of the transfer object. </p>
<p> The <i>Local</i>, <i>Remote</i> and <i>Type</i> properties expose the local container name of this transfer, the remote source (in case of download: the URL, in case of import/export: a string describing the file descriptor passed in), and the type of operation (see the Manager&#8217;s <code>ListTransfer()</code> method above for an explanation of the possible values). </p>
<p> The <i>Verify</i> property exposes the selected verification setting and is only defined for download operations (see above). </p>
<p> The <i>Progress</i> property exposes the current progress of the transfer as a value between 0.0 and 1.0. To show a progress bar on screen we recommend to query this value in regular intervals, for example every 500 ms or so.</p>
<h2>Examples</h2>
<p><code>Example 1. Introspect org.freedesktop.import1.Manager on the bus</code> </p>
<dl>
<dd>
<pre>$ gdbus introspect --system \
 --dest org.freedesktop.import1 \
 --object-path /org/freedesktop/import1</pre>
</dl>
<p> <code>Example 2. Introspect org.freedesktop.import1.Transfer on the bus</code> </p>
<dl>
<dd>
<pre>$ gdbus introspect --system \
 --dest org.freedesktop.import1 \
 --object-path /org/freedesktop/import1/transfer/_1</pre>
</dl>
<h2>Versioning</h2>
<p>These D-Bus interfaces follow m[blue]<code>the usual interface versioning guidelines</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>the usual interface versioning guidelines</p>
<dl>
<dd><a rel="nofollow" href="http://0pointer.de/blog/projects/versioning-dbus.html">http://0pointer.de/blog/projects/versioning-dbus.html</a></dl>
