---
title: "h5redeploy(1)"
name: "h5redeploy"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h5redeploy/"
description: "h5redeploy – Updates HDF5 compiler tools after an HDF5 software installation in a new location."
---

<h2>NAME</h2>
<p> h5redeploy &#8211; Updates HDF5 compiler tools after an HDF5 software installation in a new location.</p>
<h2>SYNOPSIS</h2>
<p> h5redeploy [help | -help] </p>
<p> h5redeploy [-echo] [-force] [-prefix=dir] [-tool=tool] [-show]</p>
<h2>DESCRIPTION</h2>
<p> h5redeploy updates the HDF5 compiler tools after the HDF5 software has been installed in a new location.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>help, -help</code></dt>
<dd> Prints a help message.</dd>
<dt><code>-echo</code></dt>
<dd> Shows all the shell commands executed.</dd>
<dt><code>-force</code></dt>
<dd> Performs the requested action without offerring any prompt requesting confirmation.</dd>
<dt><code>-prefix=dir</code></dt>
<dd> Specifies a new directory in which to find the HDF5 subdirectories lib/ and include/. (Default: current working directory)</dd>
<dt><code>-tool=tool</code></dt>
<dd> Specifies the tool to update. tool must be in the current directory and must be writable. (Default: h5cc)</dd>
<dt><code>-show</code></dt>
<dd> Shows all of the shell commands to be executed without actually executing them. </dd>
</dl>
