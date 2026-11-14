---
title: "jpegexiforient(1)"
name: "jpegexiforient"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jpegexiforient/"
description: "jpegexiforient – reads or writes the Exif Orientation Tag"
---

<h2 class="name">NAME</h2>
<p> jpegexiforient &#8211; reads or writes the Exif Orientation Tag </p>
<h2>SYNOPSIS</h2>
<p> <code>jpegexiforient</code> [<i>switches</i>] <i>jpegfile</i></p>
<h2>DESCRIPTION</h2>
<p> This is a utility program to get and set the Exif Orientation Tag. It can be used together with jpegtran in scripts for automatic orientation correction of digital camera pictures. </p>
<p> The Exif orientation value gives the orientation of the camera relative to the scene when the image was captured. The relation of the &#8216;0th row&#8217; and &#8216;0th column&#8217; to visual position is shown as below.</p>
<dl>
<dt>
<dd>
<pre><code>
Value | 0th Row | 0th Column-- -- --+-- -- -- -- -- -- -+-- -- -- -- -- -1 | top | left side 2 | top | right side 3 | bottom | right side 4 | bottom | left side 5 | left side | top 6 | right side | top 7 | right side | bottom 8 | left side | bottom
</code></pre>
</dl>
<p> For convenience, here is what the letter F would look like if it were tagged correctly and displayed by a program that ignores the orientation tag:</p>
<dl>
<dt>
<dd>
<pre>
  1        2       3      4     
888888  888888      88  88      
88          88      88  88      
8888      8888    8888  8888    
88          88      88  88
88          88  888888  888888
    5            6           7          8
                                               
8888888888  88                  88  8888888888
88  88      88  88          88  88      88  88
88          8888888888  8888888888          88
</pre>
</dl>
<p> jpegexiforient output the Exif Orientation Tag in a JPEG Exif file. With the options -1 .. -8, it can also be used to set the tag.</p>
<h3>OPTIONS</h3>
<dl>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</p>
<dt><code>-n</code></p>
<dd> Do not output the trailing newline</p>
<dt><code>-1</code> .. <code>-8</code></p>
<dd> Set orientation value 1 .. 8</dl>
<h2>AUTHOR</h2>
<p>&nbsp;Guido Vollbeding&nbsp;&lt;guido [at] jpegclub.org&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jpegtran/">jpegtran</a>(1),</code> <code><a href="/docs/linux/man/1-exifautotran/">exifautotran</a>(1)</code> </p>
<h2>Index</h2>
