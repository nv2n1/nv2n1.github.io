---
title: "rpmconf(8)"
name: "rpmconf"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpmconf/"
description: "rpmconf – This tool search for .rpmnew, .rpmsave and .rpmorigfiles and ask you what to do with them: Keep current version, place back old version or watch the diff. -a, –all check configuration fil..."
---

<p>rpmconf &#8211; This tool search for .rpmnew, .rpmsave and .rpmorigfiles and ask you what to do with them: Keep current version, place back old version or watch the diff. -a, &#8211;all check configuration files of all packages -opackage, &#8211;owner=package check only configuration files of given package -ftype, &#8211;frontend=type define which frontend should be used for merging -c, &#8211;clean Find and delete orphaned .rpmnew and .rpmsave files. -d, &#8211;debug Dry run. Just show which file will be deleted. -V, &#8211;version Display rpmconf version. -Z Display SELinux context of old and new file.</p>
<h2>Synopsis</h2>
<pre><code>rpmconf</code> [ <code>options </code><i>...</i> ] 
 [ <code>-a, --all</code> ] 
 [ <code>-o</code><i>package</i><code>, --owner=</code><i>package</i> ] 
 [ <code>-f</code><i>type</i><code> --frontend=</code><i>type</i> ] 
 [ <code>-c, --clean</code> ] 
 [ <code>-d, --debug</code> ] </pre>
<h2>Description</h2>
<p>Rpmconf will search for all config file of given package (or all installed packages) and will check if coresponding .rpmsave, .rpmnew or .rpmorig file exist. In such case you will be asked if you want to keep current version, put back old version or see diff of those two files. Then it delete that unwanted file.</p>
<h2>Options</h2>
<dl>
<dt><code>-a, &#8211;all</code></dt>
<dd>Check configuration files of all packages.</dd>
<dt><code>-opackage, &#8211;owner=package</code></dt>
<dd>Check only configuration files of given package.</dd>
<dt><code>-ftype, &#8211;frontend=type</code></dt>
<dd>Define which frontend should be used for merging. Valid options are: vimdiff, gvimdiff, diffuse, kdiff3, meld.</dd>
<dt><code>-c, &#8211;clean</code></dt>
<dd>Find all .rpmnew and .rpmsave files in /etc and /var directories. List all files, which belongs to installed packages. Then it write all files which are orphaned and ask you if it is safe to delete them.</dd>
<dt><code>-d, &#8211;debug</code></dt>
<dd>Dry run. Instead of executing an action (move/remove of file) it will be echoed to standard output. However executable for merging of configuration files is executed. Beware that this option is position sensitive. And only action specified after &#8211;debug are dry run. E.g. &#8211;all &#8211;debug &#8211;clean, will run in dry run mode only for &#8211;clean, but not for &#8211;all.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd>Display rpmconf version. This option expect that this script is installed as rpm package.</dd>
<dt><code>-Z</code></dt>
<dd>Display SELinux context of old and new file. Note: if you choose to install .rpmsave version. It is copied to original filename, therefore SELinux context is reset to default value specified by SELinux policy.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-rpm/">rpm</a>(8)</p>
<h2>Authors</h2>
<p>Miroslav Suchý &lt;msuchy [at] redhat.com&gt;</p>
