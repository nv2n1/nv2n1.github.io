---
title: "installcheck(1)"
name: "installcheck"
section: "1"
letter: "i"
url: "/docs/linux/man/1-installcheck/"
description: "installcheck – find out which packages cannot be installed"
---

<h2 class="name">NAME</h2>
<p> installcheck &#8211; find out which packages cannot be installed </p>
<h2>SYNOPSIS</h2>
<p> <code>installcheck</code> <i>ARCH</i> <i>REPO1</i> <i>REPO2</i>&#8230; <code>&#8211;nocheck</code> <i>NREPO1</i> <i>NREPO2</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The installcheck tool checks if all packages in <i>REPO1</i>&#8230;<i>REPON</i> are installable. A package is installable if there is a set of packages from the repositories that satisfies its dependencies. The repositories after the <code>&#8211;nocheck</code> option are only used for dependency resolving, but the tool does not check if the packages in them are installable. </p>
<p> A Repository can be a solv file, a rpmmd <code>primary.xml.gz</code> file, a SUSE <code>packages</code> or <code>packages.gz</code> file, or a Debian <code>Packages</code> or <code>Packages.gz</code> file.</p>
<h2>AUTHOR</h2>
<p> Michael Schroeder &lt;mls [at] suse.de&gt; </p>
<h2>Index</h2>
