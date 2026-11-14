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
<dt><code>help, -help</code></p>
<dd> Prints a help message.</p>
<dt><code>-echo</code></p>
<dd> Shows all the shell commands executed.</p>
<dt><code>-force</code></p>
<dd> Performs the requested action without offerring any prompt requesting confirmation.</p>
<dt><code>-prefix=dir</code></p>
<dd> Specifies a new directory in which to find the HDF5 subdirectories lib/ and include/. (Default: current working directory)</p>
<dt><code>-tool=tool</code></p>
<dd> Specifies the tool to update. tool must be in the current directory and must be writable. (Default: h5cc)</p>
<dt><code>-show</code></p>
<dd> Shows all of the shell commands to be executed without actually executing them. </p>
</dl>
<h2>Index</h2>
