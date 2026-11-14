---
title: "scap-as-rpm(8)"
name: "scap-as-rpm"
section: "8"
letter: "s"
url: "/docs/linux/man/8-scap-as-rpm/"
description: "scap-as-rpm – manual page for scap-as-rpm"
---

<p>scap-as-rpm &#8211; manual page for scap-as-rpm</p>
<h2>Description</h2>
<p>usage: scap-as-rpm [-h] [&#8211;pkg-name PKG_NAME] [&#8211;pkg-version PKG_VERSION]</p>
<dl>
<dd>[&#8211;pkg-release PKG_RELEASE] [&#8211;pkg-summary PKG_SUMMARY] [&#8211;pkg-license PKG_LICENSE] [&#8211;pkg-scap-location PKG_SCAP_LOCATION] [&#8211;rpm-destination RPM_DESTINATION] [&#8211;srpm-destination SRPM_DESTINATION] FILE [FILE &#8230;]</dl>
<p> Takes given SCAP input(s) and makes an RPM package that contains them. The result RPM can be installed using # yum install ./package-name-1-1.rpm which will put the contents into <i>/usr/share/xml/scap</i>. No dependency on openscap or scapworkbench is enforced in the output package so you can use any SCAP-capable scanner to evaluate the content.</p>
<h3>positional arguments:</h3>
<dl>
<dt>FILE</p>
<dd>List of files that should be put into the result package. These should be SCAP XML files but such requirement is not enforced.</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>show this help message and exit</p>
<dt><code>&#8211;pkg-name</code> PKG_NAME</p>
<dd>Name of the RPM package, if none is provided the basename of the first SCAP input is used. Ex.: xyzsecurity-guide</p>
<dt> <code>&#8211;pkg-version</code> PKG_VERSION</p>
<dt> <code>&#8211;pkg-release</code> PKG_RELEASE</p>
<dt><code>&#8211;pkg-summary</code> PKG_SUMMARY</p>
<dd>
<dd>Optional short description of the package.</p>
<dt><code>&#8211;pkg-license</code> PKG_LICENSE</p>
<dd>Short name of the license that you want to publish the package under. Ex.: GPLv2+, BSD, &#8230;</p>
<dt><code>&#8211;pkg-scap-location</code> PKG_SCAP_LOCATION</p>
<dd>Folder where SCAP files are supposed to be installed. Each package will have its own folder inside this folder. RPM variables can be used and will be expanded as usual. It is recommended to keep the default settings.</p>
<dt><code>&#8211;rpm-destination</code> RPM_DESTINATION</p>
<dd>The folder (absolute or relative to CWD) where the result RPM shall be saved.</p>
<dt><code>&#8211;srpm-destination</code> SRPM_DESTINATION</p>
<dd>The folder (absolute or relative to CWD) where the result SRPM shall be saved. </p>
