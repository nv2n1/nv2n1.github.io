---
title: "mockchain(1)"
name: "mockchain"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mockchain/"
description: "mockchain – chain package builder."
---

<h2>NAME</h2>
<p> mockchain &#8211; chain package builder.</p>
<h2>SYNOPSIS</h2>
<p> <code>mockchain</code> -r chroot_config [options] [package&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>mockchain</code> builds a series of srpms in mock one at a time. After each successful build of a package it adds the resulting packages to a local repo which are available to the next package to satisfy buildreqs.</p>
<h2>USAGE NOTES</h2>
<p> This does not try to sort the packages by build order b/c that is too much effort and not obviously doable with the buildreq information we have. </p>
<p> The build process when you use -l is idempotent so a package which has already been successfully built will not be built again. </p>
<p> If you want to force the rebuild of a package which has been built successfully simply remove the &#8216;success&#8217; file from the directory for the package in the localrepo path. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code> REPOS, <code>&#8211;addrepo</code>=<i>REPOS</i></p>
<dd> add this repo baseurl to the yumconfig for the chroot. This can be specified multiple times. Let&#8217;s you point to multiple paths beyond the default to pull build deps from. </p>
<dt><code>-c</code>, <code>&#8211;continue</code></p>
<dd> if a pkg fails to build, continue to the next one, default is to stop </p>
<dt><code>-l</code> LOCALREPO, <code>&#8211;localrepo</code>=<i>PATH</i></p>
<dd> set the path to put the results/repo in. This path needs to be somewhere accessible to users other than you for reading as the mock process doesn&#8217;t run as you. Will make a tempdir if not set. </p>
<dt><code>&#8211;log</code>=<i>LOGFILE</i></p>
<dd> log to the file named by this option, defaults to not logging </p>
<dt><code>-m</code> OPTION, <code>&#8211;mock-option</code>=<i>OPTION</i></p>
<dd> pass the OPTION to mock. Can be used several times. For example: </p>
<p> <code>-m &#8211;define=&quot;packager Monkey&quot;</code> </p>
<dt><code>-r</code> CONFIG, <code>&#8211;root</code>=<i>CONFIG</i></p>
<dd> chroot config name to use in the mock build </p>
<dt><code>&#8211;recurse</code></p>
<dd> build all pkgs, record the failures and try to rebuild them again and again until everything gets built (or until the set of pkgs failing to build are the same over) sets &#8211;continue </p>
</dl>
<h2>AUTHORS</h2>
<p> Seth Vidal &lt;skvidal1.3.3&quot;fedoraproject.org&gt; </p>
<h2>Index</h2>
