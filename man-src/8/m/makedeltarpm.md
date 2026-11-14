---
title: "makedeltarpm(8)"
name: "makedeltarpm"
section: "8"
letter: "m"
url: "/docs/linux/man/8-makedeltarpm/"
description: "makedeltarpm – create a deltarpm from two rpms"
---

<p>makedeltarpm &#8211; create a deltarpm from two rpms </p>
<h2>Synopsis</h2>
<p><code>makedeltarpm</code> [<code>-v</code>] [<code>-V</code> <i>version</i>] [<code>-z</code> <i>compression</i>] [<code>-m</code> <i>mbytes</i>] [<code>-s</code> <i>seqfile</i>] [<code>-r</code>] [<code>-u</code>] <i>oldrpm</i> <i>newrpm</i> <i>deltarpm</i><br />
 <code>makedeltarpm</code> [<code>-v</code>] [<code>-V</code> <i>version</i>] [<code>-z</code> <i>compression</i>] [<code>-s</code> <i>seqfile</i>] [<code>-u</code>] <code>-p</code> <i>oldrpmprint</i> <i>oldpatchrpm</i> <i>oldrpm</i> <i>newrpm</i> <i>deltarpm</i> </p>
<h2>Description</h2>
<p>makedeltarpm creates a deltarpm from two rpms. The deltarpm can later be used to recreate the new rpm from either filesystem data or the old rpm. Use the <code>-v</code> option to make makedeltarpm more verbose about its work (use it twice to make it even more verbose). If you want to create a smaller and faster to combine &quot;rpm-only&quot; deltarpm which does not work with filesystem data, specify the <code>-r</code> option. makedeltarpm normally produces a V3 format deltarpm, use the <code>-V</code> option to specify a different version if desired. The <code>-z</code> option can be used to specify a different compression method, the default is to use the same compression method as used in the new rpm. The <code>-s</code> option makes makedeltarpm write out the sequence id to the specified file <i>seqfile</i>. If you also use patch rpms you should use the <code>-p</code> option to specify the rpm-print of <i>oldrpm</i> and the created patch rpm. This option tells makedeltarpm to exclude the files that were not included in the patch rpm but are not byteswise identical to the ones in oldrpm. makedeltarpm can also create an &quot;identity&quot; deltarpm by adding the <code>-u</code> switch. In this case only one rpm has to be specified. An identity deltarpm can be useful to just replace the signature header of a rpm or to reconstruct a rpm from the filesystem. </p>
<h2>Memory Considerations</h2>
<p>makedeltarpm normally needs about three to four times the size of the rpm&#8217;s uncompressed payload. You can use the <code>-m</code> option to enable a sliding block algorithm that needs <i>mbytes</i> megabytes of memory. This trades memory usage with the size of the created deltarpm. Furthermore, the uncompressed deltarpm payload is currently also stored in memory when this option is used, but it tends to be small in most cases.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-applydeltarpm/">applydeltarpm</a></code>(8) <code><a href="/docs/linux/man/8-combinedeltarpm/">combinedeltarpm</a></code>(8) </p>
<h2>Author</h2>
<p>Michael Schroeder &lt;mls [at] suse.de&gt;</p>
