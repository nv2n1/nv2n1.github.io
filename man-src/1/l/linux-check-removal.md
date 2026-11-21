---

title: "linux-check-removal(1)"
name: "linux-check-removal"
section: "1"
letter: "l"
url: "/docs/linux/man/1-linux-check-removal/"
description: "linux-check-removal – check whether removal of a kernel is safe"
---

<p> linux-check-removal &#8211; check whether removal of a kernel is safe </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>linux-check-removal</code><i>&nbsp;VERSION</i></dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>linux-check-removal</code> is intended to be called from the prerm</p>
<dd>maintainer scripts of Linux kernel packages. </dd>
<p> The <i>VERSION</i> argument must be the kernel version string as shown by <code>uname -r</code> and used in filenames. </p>
<p> If the currently running kernel matches <i>VERSION</i>, <code>linux-check-removal</code> normally prompts the user to confirm this potentially dangerous action and fails if the user chooses to abort. There are two exceptions to this behaviour:</p>
<dl>
<dt>&bull;</dt>
<dd> If the current environment is a chroot or container, it is assumed that the running kernel is independent of any installed kernel package and the command always quietly succeeds</dd>
<dt>&bull;</dt>
<dd> If debconf prompts are disabled, the command warns if removing the running kernel but always succeeds </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><i>DEBIAN_FRONTEND</i></dt>
<dd> Name of the preferred debconf front-end. If set to <i>noninteractive</i>, debconf prompts are disabled and <code>linux-check-removal</code> always quietly succeeds.</dd>
<dt><i>DPKG_MAINTSCRIPT_PACKAGE</i></dt>
<dd> Name of the package to be removed, automatically set by dpkg. </dd>
</dl>
<h2>AUTHOR</h2>
<p> <code>linux-check-removal</code> and this manual page were written by Ben Hutchings as part of the Debian <code>linux-base</code> package. </p>
