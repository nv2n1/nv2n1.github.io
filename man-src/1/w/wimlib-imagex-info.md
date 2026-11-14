---
title: "wimlib-imagex-info(1)"
name: "wimlib-imagex-info"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wimlib-imagex-info/"
description: "wimlib-imagex-info – Display information about a WIM file, or change information about an image"
---

<h2>NAME</h2>
<p> wimlib-imagex-info &#8211; Display information about a WIM file, or change information about an image</p>
<h2>SYNOPSIS</h2>
<p> <code>wimlib-imagex info</code> <i>WIMFILE</i> [<i>IMAGE</i> [<i>NEW_NAME</i> [<i>NEW_DESC</i>]]] [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>wimlib-imagex info</code> displays information about <i>WIMFILE</i>, and optionally changes which image is bootable, or what the name and description of an image are. This command is also available as simply <code>wiminfo</code> if the appropriate hard link or batch file has been installed. </p>
<p> If neither an image nor any flags other than <code>&#8211;check</code> are specified, some basic information about the WIM archive as well as information about the images contained in it will be printed. If an image is specified by <i>IMAGE</i> (as a 1-based image index or an image name), the printed information is restricted to that concerning the specified image. </p>
<p> Changes to the WIM are made if <i>NEW_NAME</i> and/or <code>&#8211;boot</code> and/or <code>&#8211;image-property</code> are specified. <i>NEW_NAME</i> is taken to be the new name of the image specified by <i>IMAGE</i> while <i>NEW_DESC</i> is taken to be its new description. If <i>NEW_DESC</i> is not specified, the image&#8217;s description is unchanged. </p>
<p> <code>wimlib-imagex info</code> does not support modifying a split WIM, although you may display information about one.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;boot</code></p>
<dd> Indicates that the specified image is to be made the bootable image of the WIM archive.</p>
<dt><code>&#8211;check</code></p>
<dd> When reading <i>WIMFILE</i>, verify its integrity if the integrity table is present; additionally if an action that requires modifying the WIM archive is specified, include an integrity table in the modified WIM. If this option is not specified and <i>WIMFILE</i> is modified, an integrity table will be included in the modified WIM if and only if there was one before.</p>
<dt><code>&#8211;nocheck</code></p>
<dd> If an action that requires modifying the WIM archive is specified, do not include an integrity table in the modified WIM. If this option is not specified and <i>WIMFILE</i> is modified, an integrity table will be included in the modified WIM if and only if there was one before.</p>
<dt><code>&#8211;extract-xml</code>=<i>FILE</i></p>
<dd> Extracts the raw data from the XML resource in the WIM file to <i>FILE</i>. Note: the XML data will be encoded using UTF-16LE, and it will begin with a byte-order mark.</p>
<dt><code>&#8211;header</code></p>
<dd> Shows detailed information from the WIM header.</p>
<dt><code>&#8211;blobs</code></p>
<dd> Prints information about all the blobs (&quot;file data&quot;) in the WIM. A WIM file stores only one copy of each unique blob.</p>
<dt><code>&#8211;xml</code></p>
<dd> Prints the raw XML data from the WIM. Note: the XML data will be encoded using UTF-16LE, and it will begin with a byte-order mark.</p>
<dt><code>&#8211;image-property</code> <i>NAME</i>=<i>VALUE</i></p>
<dd> Set an arbitrary per-image property in the XML document of the WIM file. <i>NAME</i> is an element path such as &quot;WINDOWS/VERSION/MAJOR&quot;, and <i>VALUE</i> is the string to place in the element, such as &quot;10&quot;. See the documentation for this option to <code>wimlib-imagex capture</code> (1) for more details. This option may be specified multiple times.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wimlib-imagex/">wimlib-imagex</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-dir/">wimlib-imagex-dir</a></code>(1) </p>
<h2>Index</h2>
