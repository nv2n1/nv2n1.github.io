---
title: "atomic-mount(1)"
name: "atomic-mount"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-mount/"
description: "atomic-mount – Mount Images/Containers to Filesystem"
---

<h2 class="name">NAME</h2>
<p> atomic-mount &#8211; Mount Images/Containers to Filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic mount</code> [<code>&#8211;live</code> | <code>&#8211;shared</code> | <code>&#8211;storage=[ostree|docker]</code> | [<code>-o</code>|<code>&#8211;options</code> <i>OPTIONS</i>]] [REGISTRY/]REPO[:TAG]|UUID|NAME DIRECTORY </p>
<h2>DESCRIPTION</h2>
<p> <code>atomic mount</code> attempts to mount the underlying filesystem of a container or image into the host filesystem. Accepts one of image UUID, container UUID, container NAME, or image REPO (optionally with registry and tag information). If the given UUID or NAME is a container, and <code>&#8211;live</code> is not set, then <i>atomic mount</i> will create a snapshot of the container by committing it to a temporary image and spawning a temporary container from that image. If UUID or REPO refers to an image, then <i>atomic mount</i> will simply create a temporary container from the given image. If the UID is not zero, i.e. not being run as root, then <i>atomic mount</i> will call ostree checkout with &#8211;user-mode option. It will also ignore the mount system call, since ostree checkout takes care of that. All temporary artifacts are cleaned upon <i>atomic unmount</i>. Atomic mount is <i>only</i> supported on the devicemapper and overlayfs docker storage backends. If an image stored on an OSTree repository is mounted, then a temporary checkout is done, which will be deleted by atomic unmount. </p>
<h2>OPTIONS</h2>
<p> <code>-o|&#8211;options</code> <i>OPTIONS</i> Specify options to be passed to <i>mount</i>. All options accepted by the &#8216;mount&#8217; command are valid. The default mount options for the devicemapper backend (if the <code>&#8211;live</code> flag is unset) are: &#8216;ro,nodev,nosuid&#8217;. If the <code>-o</code> flag is specified, then no default options are assumed. Use of the &#8216;rw&#8217; flag is discouraged, as writes into the atomic temporary containers are never preserved. Use of this option conflicts with <code>&#8211;live</code>, as live containers have predetermined, immutable mount options. The OverlayFS driver has, by default, only the &#8216;ro&#8217; option set, and the &#8216;rw&#8217; option is illegal and will cause the program to terminate. </p>
<p> <code>&#8211;live</code> Mount a running container live, writable, and synchronized. This option allows the user to modify the container&#8217;s contents as the container runs or update the container&#8217;s software without rebuilding the container. If live mode is used, no mount options may be provided. Live mode is <i>not</i> supported on the OverlayFS docker storage driver. </p>
<p> <code>&#8211;shared</code> Mount a container image with a shared SELinux label </p>
<p> [<code>&#8211;storage=[ostree|docker]</code>] Optionally specify the storage of the image. Will prompt user to specify if the same image name exists in both ostree and docker, and the user did not specify. </p>
<h2>HISTORY</h2>
<p> June 2015, Originally compiled by William Temple (wtemple at redhat dot com) </p>
<h2>Index</h2>
