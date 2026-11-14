---
title: "wimlib-imagex-delete(1)"
name: "wimlib-imagex-delete"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wimlib-imagex-delete/"
description: "wimlib-imagex-delete – Delete an image from a WIM archive"
---

<h2>NAME</h2>
<p> wimlib-imagex-delete &#8211; Delete an image from a WIM archive</p>
<h2>SYNOPSIS</h2>
<p> <code>wimlib-imagex delete</code> <i>WIMFILE</i> <i>IMAGE</i> [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>wimlib-imagex delete</code> deletes the specified image from the Windows Imaging (WIM) file <i>WIMFILE</i>. This command is also available as simply <code>wimdelete</code> if the appropriate hard link or batch file has been installed. </p>
<p> <i>IMAGE</i> specifies the WIM image in <i>WIMFILE</i> to delete. It may be a 1-based index of an image in the WIM, the name of an image in the WIM, or the keyword &quot;all&quot; to indicate that all images are to be deleted. Use the <code>wimlib-imagex info</code> (1) command to show what images a WIM file contains.</p>
<h2>NOTES</h2>
<p> By default, the WIM file is rebuilt with all unnecessary file data removed. This is different from Microsoft&#8217;s ImageX and DISM, which only will delete the directory tree metadata and XML data for this operation. (See the <code>&#8211;soft</code> option for the other kind of delete). </p>
<p> Also wimlib allows you to delete all the images from a WIM and have a WIM with 0 images, although such a file wouldn&#8217;t be very useful. </p>
<p> <code>wimlib-imagex delete</code> does not support split WIMs.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;check</code></p>
<dd> When reading <i>WIMFILE</i>, verify its integrity if the integrity table is present; additionally, when rewriting <i>WIMFILE</i> after the specified image was deleted, always write an integrity table. If this option is not specified, the integrity of <i>WIMFILE</i> will not be checked when it&#8217;s opened, but an integrity table will be written in the updated WIM if and only if one was present before.</p>
<dt><code>&#8211;soft</code></p>
<dd> Perform a &quot;soft delete&quot;. Specifying this flag overrides the default behavior of rebuilding the entire WIM after deleting an image. Instead, only minimal changes to correctly remove the image from the WIM will be taken. In particular, all streams will be left alone, even if they are no longer referenced. This is probably not what you want, because no space will be saved by deleting an image in this way.</p>
<dt>
<dd> You may use <code>wimlib-imagex optimize</code> to delete unreferenced streams from a WIM that has had images soft-deleted from it.</p>
<dt><code>&#8211;unsafe-compact</code></p>
<dd> Compact the WIM archive in-place, eliminating &quot;holes&quot;. In general, this option should <i>not</i> be used because a failed or interrupted compaction will corrupt the WIM archive. For more information, see the documentation for this option in <code>wimlib-imagex-optimize</code> (1).</dl>
<h2>EXAMPLES</h2>
<p> Delete the first image from &#8216;boot.wim&#8217;:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex delete boot.wim 1</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wimlib-imagex/">wimlib-imagex</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-info/">wimlib-imagex-info</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-optimize/">wimlib-imagex-optimize</a></code>(1) </p>
<h2>Index</h2>
