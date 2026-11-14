---
title: "setpix(1)"
name: "setpix"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setpix/"
description: "setpix – Set FITS or IRAF image values"
---

<h2>Name</h2>
<p> setpix &#8211; Set FITS or IRAF image values</p>
<h2>Synopsis</h2>
<p> setpix [-vn] file.fts [x_range y_range value] [@valuefile]</p>
<h2>Description</h2>
<p> Set a specified pixel or range of pixels in a FITS or IRAF image to a specified value. More than one range of pixels and values may be specified on one command line. A file of xrange yrange value triplets may be used to set multiple regions at once. The image may be overwritten or a new image created.</p>
<h2>Options</h2>
<dl>
<dt><code>filename </code></p>
<dd> Name of IRAF image header file or FITS file. This must be present.</p>
<dt><code>@coordfile </code></p>
<dd> Name of file containing lines of the format<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>xrange yrange value where xrange and yrange are of the format n or n-n or n,n,n or n-n,n-n and value my be integer or floating point. value will be converted to the type of the image. If a range is 0, the entire row or column specified by the other non-zero range will be set to the indicated value. If both ranges are zero, the entire image will be set to the specified value. New in version 2.6.4.</p>
<dt><code>xrange yrange value </code></p>
<dd> Image coordinate x and y ranges and the value to which that region will be set. Either one of these triplets or a file of triplets, specified by @filename, must be present. xrange and yrange are of the format n or n-n or n,n,n or n-n,n-n and value my be integer or floating point. value will be converted to the type of the image. If a range is 0, the entire row or column specified by the other non-zero range will be set to the indicated value. If both ranges are zero, the entire image will be set to the specified value. Ranges new in version 2.6.4.</p>
<dt><code>-a &lt;number&gt;</code></p>
<dd> Add constant to pixels</p>
<dt><code>-d &lt;number&gt;</code></p>
<dd> Divide pixels by constant</p>
<dt><code>-i</code></p>
<dd> List each line which is dropped</p>
<dt><code>-m &lt;number&gt;</code></p>
<dd> Multiply pixels by constant</p>
<dt><code>-n </code></p>
<dd> Write the output to a new file which is named by inserting an e before the file extension. The new file is always written to the current working directory.</p>
<dt><code>-s &lt;number&gt;</code></p>
<dd> Subtract constant from pixels</p>
<dt><code>-v </code></p>
<dd> Print more information about the process </p>
</dl>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
