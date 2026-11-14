---
title: "llvm-stress-14(1)"
name: "llvm-stress-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-stress-14/"
description: "llvm-stress – generate random .ll files"
---

<h2 class="name">NAME</h2>
<p> llvm-stress &#8211; generate random .ll files </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-stress</code> [-size=filesize] [-seed=initialseed] [-o=outfile]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-stress</code> tool is used to generate random <code>.ll</code> files that can be used to test different components of LLVM.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o filename</code></p>
<dd> Specify the output filename.</p>
<dt><code>-size size</code></p>
<dd> Specify the size of the generated <code>.ll</code> file.</p>
<dt><code>-seed seed</code></p>
<dd> Specify the seed to be used for the randomly generated instructions.</dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-stress</code> returns 0.</p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
