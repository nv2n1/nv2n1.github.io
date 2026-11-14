---
title: "grid-ca-package(1)"
name: "grid-ca-package"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grid-ca-package/"
description: "grid-ca-package – Prepare a CA certificate, configuration, and policy for distribution"
---

<h2 class="name">NAME</h2>
<p> grid-ca-package &#8211; Prepare a CA certificate, configuration, and policy for distribution </p>
<h2>SYNOPSIS</h2>
<p> <code>grid-ca-sign</code> [-ca <i>HASH</i>] [-g] [-b] [-r] [-d] </p>
<p> <code>grid-ca-sign</code> [ -help| -h| -usage| -version| -versions ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>grid-ca-sign</code> utility creates a tarball containing an RPM spec file and the files needed to use a CA with grid tools. It optionally will also create a GPT package for distributing a CA. </p>
<p> By default, the <code>grid-ca-sign</code> utility displays a list of installed grid CA and prompts for which CA to package. It then creates a tarball containing the CA certificate, signing policy, CA configuration files, and an spec script to generate a binary RPM package containing the CA. If the CA hash is known prior to running <code>grid-ca-sign</code>, it may provided as an argument to the <i>-ca</i> parameter to avoid prompting. </p>
<p> In addition to generating a spec script and tarball, <code>grid-ca-sign</code> creates a GPT package if either the <i>-g</i> or <i>-b</i> options are used on the command-line. These packages may be used to distribute a CA and configuration to systems which do not support RPM packages. </p>
<p> The <code>grid-ca-sign</code> utility writes the package tarballs to the current working directory.</p>
<h2>OPTIONS</h2>
<p> The full set of command-line options to <code>grid-ca-sign</code> follows: </p>
<p> <code>-help, -h, -usage</code></p>
<dl>
<dt>
<dd> Display the command-line options to <code>grid-ca-sign</code> and exit.</dl>
<p> <code>-version, -versions</code></p>
<dl>
<dt>
<dd> Display the version number of the <code>grid-ca-sign</code> command. The second form includes more details.</dl>
<p> <code>-ca </code><i>CA</i></p>
<dl>
<dt>
<dd> Use the CA whose name matches the hash string <i>CA</i>. When invoked with this option, <code>grid-ca-sign</code> runs non-interactively.</dl>
<p> <code>-g</code></p>
<dl>
<dt>
<dd> Create a GPT binary package in addition to the RPM script tarball. This package may be installed on other systems using the <code>gpt-install</code> program.</dl>
<p> <code>-b</code></p>
<dl>
<dt>
<dd> Create a GPT binary package with GPT metadata located in the path expected by GPT 3.2 (used in Globus 2.0.0-5.0.x) instead of overrides the <i>-g</i> command-line option.</dl>
<p> <code>-r</code></p>
<dl>
<dt>
<dd> Create a binary RPM package for the CA. This option currently only works on RPM-based distributions.</dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Create a binary Debian package for the CA. This option currently only works on Debian-based distributions.</dl>
<h2>EXAMPLES</h2>
<p> Package a Simple CA with hash 0146c503. </p>
<dl>
<dt>
<dd>
<pre>
% grid-ca-sign -ca 0146c503
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Creating RPM source tarball... done
globus_simple_ca_0146c503.tar.gz
</pre>
</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affect the execution of <code>grid-ca-sign</code>: </p>
<p> GLOBUS_LOCATION</p>
<dl>
<dt>
<dd> Non-standard installation path of the Globus Toolkit.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-grid-cert-request/">grid-cert-request</a>(1), <a href="/docs/linux/man/1-grid-ca-sign/">grid-ca-sign</a>(1), <a href="/docs/linux/man/1-grid-default-ca/">grid-default-ca</a>(1), <a href="/docs/linux/man/1-grid-ca-create/">grid-ca-create</a>(1)</p>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2014 University of Chicago </p>
<h2>Index</h2>
