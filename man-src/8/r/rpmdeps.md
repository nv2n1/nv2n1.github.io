---
title: "rpmdeps(8)"
name: "rpmdeps"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpmdeps/"
description: "rpmdeps – Generate RPM Package Dependencies"
---

<p>rpmdeps &#8211; Generate RPM Package Dependencies</p>
<h2>Synopsis</h2>
<p><code>rpmdeps</code> <code>{-P|&#8211;provides}</code> <code>{-R|&#8211;requires}</code> <i>FILE</i><i> &#8230;</i> </p>
<h2>Description</h2>
<p><code>rpmdeps</code> generates package dependencies for the set of <i>FILE</i> arguments. Each <i>FILE</i> argument is searched for Elf32/Elf64, script interpreter, or per-script dependencies, and the dependencies are printed to stdout.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rpm/">rpm</a></code>(8), </p>
<p> <code><a href="/docs/linux/man/8-rpmbuild/">rpmbuild</a></code>(8),</p>
<h2>Authors</h2>
<p>Jeff Johnson &lt;jbj [at] redhat.com&gt;</p>
