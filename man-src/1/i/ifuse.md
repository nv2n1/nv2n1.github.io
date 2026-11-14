---
title: "ifuse(1)"
name: "ifuse"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ifuse/"
description: "ifuse – Mount directories of an iOS device locally using fuse."
---

<h2>NAME</h2>
<p> ifuse &#8211; Mount directories of an iOS device locally using fuse.</p>
<h2>SYNOPSIS</h2>
<p> <code>ifuse MOUNTPOINT [OPTIONS]</code> </p>
<h2>DESCRIPTION</h2>
<p> Mount directories of an iOS device locally using fuse. By default the media directory is mounted, options allow to also mount the sandbox container of an app, an app&#8217;s documents folder or even the root filesystem on jailbroken devices. </p>
<p> Example: </p>
<p> $ ifuse /media/iPhone &#8211;root </p>
<p> This mounts the root filesystem of the first attached device on this computer in the directory /media/iPhone. </p>
<p> Regular users are able to unmount fuse mounts using &quot;fusermount -u MOUNTPOINT&quot;. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o opt,[opt&#8230;] </code></p>
<dd> mount options.</p>
<dt><code>-u, &#8211;uuid UUID</code></p>
<dd> mount specific device by its 40-digit device UUID.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> prints usage information.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> print version.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> enable libimobiledevice communication debugging.</p>
<dt><code>&#8211;documents APPID</code></p>
<dd> mount &#8216;Documents&#8217; folder of app identified by APPID.</p>
<dt><code>&#8211;container APPID</code></p>
<dd> mount sandbox root of an app identified by APPID.</p>
<dt><code>&#8211;root </code></p>
<dd> mount root file system (jailbroken device required). </p>
</dl>
<h2>AUTHOR</h2>
<p> Julien Lavergne (man page) </p>
<p> Martin Szulecki </p>
<p> Matt Colyer </p>
<p> Nikias Bassen </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fusermount/">fusermount</a>(1) </p>
<h2>Index</h2>
