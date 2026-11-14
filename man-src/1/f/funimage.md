---
title: "funimage(1)"
name: "funimage"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funimage/"
description: "funimage – create a FITS image from a Funtools data file"
---

<h2>NAME</h2>
<p> <code>funimage &#8211; create a FITS image from a Funtools data file</code></p>
<h2>SYNOPSIS</h2>
<p> funimage [-a] &lt;iname&gt; &lt;oname&gt; [bitpix=n] funimage [-l] &lt;iname&gt; &lt;oname&gt; &lt;xcol:xdims&gt; &lt;ycol:ydims&gt; &lt;vcol&gt; [bitpix=n] funimage [-p x|y] &lt;iname&gt; &lt;oname&gt; [bitpix=n]</p>
<h2>OPTIONS</h2>
<pre>
  -a       # append to existing output file as an image extension
  -l       # input is a list file containing xcol, ycol, value
  -p [x|y] # project along x or y axis to create a 1D image
</pre>
<h2>DESCRIPTION</h2>
<p> <code>funimage</code> creates a primary <font SIZE="-1">FITS</font> image from the specified <font SIZE="-1">FITS</font> Extension and/or Image Section of a <font SIZE="-1">FITS</font> file, or from an Image Section of a non-FITS array, or from a raw event file. </p>
<p> The first argument to the program specifies the <font SIZE="-1">FITS</font> input image, array, or raw event file to process. If &#8220;stdin&#8221; is specified, data are read from the standard input. Use Funtools Bracket Notation to specify <font SIZE="-1">FITS</font> extensions, image sections, and filters. The second argument is the output <font SIZE="-1">FITS</font> file. If &#8220;stdout&#8221; is specified, the <font SIZE="-1">FITS</font> image is written to the standard output. By default, the output pixel values are of the same data type as those of the input file (or type &#8220;int&#8221; when binning a table), but this can be overridden using an optional third argument of the form: </p>
<pre>
  bitpix=n
</pre>
<p> where n is 8,16,32,-32,-64, for unsigned char, short, int, float and double, respectively. </p>
<p> If the input data are of type image, the appropriate section is extracted and blocked (based on how the Image Section is specified), and the result is written to the <font SIZE="-1">FITS</font> primary image. When an integer image containing the <font SIZE="-1">BSCALE</font> and <font SIZE="-1">BZERO</font> keywords is converted to float, the pixel values are scaled and the scaling keywords are deleted from the output header. When converting integer scaled data to integer (possibly of a different size), the pixels are not scaled and the scaling keywords are retained. </p>
<p> If the input data is a binary table or raw event file, these are binned into an image, from which a section is extracted and blocked, and written to a primary <font SIZE="-1">FITS</font> image. In this case, it is necessary to specify the two columns that will be used in the 2D binning. This can be done on the command line using the <code>bincols=(x,y)</code> keyword: </p>
<pre>
  funcnts &quot;foo.ev[EVENTS,bincols=(detx,dety)]&quot;
</pre>
<p> The full form of the <code>bincols=</code> specifier is: </p>
<pre><code>
bincols = ([xname[:tlmin[:tlmax:[binsiz]]]], [yname[:tlmin[:tlmax[:binsiz]]]])
</code></pre>
<p> where the tlmin, tlmax, and binsiz specifiers determine the image binning dimensions: </p>
<pre>
  dim = (tlmax - tlmin)/binsiz     (floating point data)
  dim = (tlmax - tlmin)/binsiz + 1 (integer data)
</pre>
<p> Using this syntax, it is possible to bin any two columns of a binary table at any bin size. Note that the tlmin, tlmax, and binsiz specifiers can be omitted if <font SIZE="-1">TLMIN</font>, <font SIZE="-1">TLMAX</font>, and <font SIZE="-1">TDBIN</font> header parameters (respectively) are present in the <font SIZE="-1">FITS</font> binary table header for the column in question. Note also that if only one parameter is specified, it is assumed to be tlmax, and tlmin defaults to 1. If two parameters are specified, they are assumed to be tlmin and tlmax. See Binning <font SIZE="-1">FITS</font> Binary Tables and Non-FITS Event Files for more information about binning parameters. </p>
<p> By default, a new 2D <font SIZE="-1">FITS</font> image file is created and the image is written to the primary <font SIZE="-1">HDU</font>. If the <code>-a</code> (append) switch is specified, the image is appended to an existing <font SIZE="-1">FITS</font> file as an <font SIZE="-1">IMAGE</font> extension. (If the output file does not exist, the switch is effectively ignored and the image is written to the primary <font SIZE="-1">HDU</font>.) This can be useful in a shell programming environment when processing multiple <font SIZE="-1">FITS</font> images that you want to combine into a single final <font SIZE="-1">FITS</font> file. </p>
<p> <code>funimage</code> also can take input from a table containing columns of x, y, and value (e.g., the output from <code>fundisp -l</code> which displays each image x and y and the number of counts at that position.) When the <code>-l</code> (list) switch is used, the input file is taken to be a <font SIZE="-1">FITS</font> or <font SIZE="-1">ASCII</font> table containing (at least) three columns that specify the x and y image coordinates and the value of that image pixel. In this case, <code>funimage</code> requires four extra arguments: xcolumn:xdims, ycolumn:ydims, vcolumn and bitpix=n. The x and y col:dim information takes the form: </p>
<pre>
  name:dim               # values range from 1 to dim
  name:min:max           # values range from min to max
  name:min:max:binsiz    # dimensions scaled by binsize
</pre>
<p> In particular, the min value should be used whenever the minimum coordinate value is something other than one. For example: </p>
<pre>
  funimage -l foo.lst foo.fits xcol:0:512 ycol:0:512 value bitpix=-32
</pre>
<p> The list feature also can be used to read unnamed columns from standard input: simply replace the column name with a null string. Note that the dimension information is still required: </p>
<pre>
  funimage -l stdin foo.fits &quot;&quot;:0:512 &quot;&quot;:0:512 &quot;&quot; bitpix=-32
  240 250 1
  255 256 2
  ...
  ^D
</pre>
<p> The list feature provides a simple way to generate a blank image. If you pass a Column-based Text File to funimage in which the text header contains the required image information, then funimage will correctly make a blank image. For example, consider the following text file (called foo.txt): </p>
<p>x : I : 1 : 10 y : I : 1 : 10 &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;0 0</p>
<p> This text file defines two columns, x and y, each of data type 32-bit int and image dimension 10. The command: </p>
<pre>
  funimage foo.txt foo.fits bitpix=8
</pre>
<p> will create an empty <font SIZE="-1">FITS</font> image called foo.fits containing a 10&#215;10 image of unsigned char: </p>
<p>fundisp foo.fits 1 2 3 4 5 6 7 8 9 10 &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;10 : 0 0 0 0 0 0 0 0 0 0 9 : 0 0 0 0 0 0 0 0 0 0 8 : 0 0 0 0 0 0 0 0 0 0 7 : 0 0 0 0 0 0 0 0 0 0 6 : 0 0 0 0 0 0 0 0 0 0 5 : 0 0 0 0 0 0 0 0 0 0 4 : 0 0 0 0 0 0 0 0 0 0 3 : 0 0 0 0 0 0 0 0 0 0 2 : 0 0 0 0 0 0 0 0 0 0 1 : 1 0 0 0 0 0 0 0 0 0</p>
<p> Note that the text file must contain at least one row of data. However, in the present example, event position 0,0 is outside the limits of the image and will be ignored. (You can, of course, use real x,y values to seed the image with data.) </p>
<p> Furthermore, you can use the <font SIZE="-1">TEXT</font> filter specification to obviate the need for an input text file altogether. The following command will create the same 10&#215;10 char image without an actual input file: </p>
<p>funimage stdin &#8216;[TEXT(x:I:10,y:I:10)]&#8217; foo.fits bitpix = 8 &lt; / dev / null or<br />
                                                         funimage / dev / null &#8216;[TEXT(x:I:10,y:I:10)]&#8217; foo.fits bitpix = 8</p>
<p> You also can use either of these methods to generate a region mask simply by appending a region inside the filter brackets and specfying <code>mask=all</code> along with the bitpix. For example, the following command will generate a 10&#215;10 char mask using 3 regions: </p>
<pre>
  funimage stdin'[TEXT(x:I:10,y:I:10),cir(5,5,4),point(10,1),-cir(5,5,2)]' \
  foo.fits bitpix=8,mask=all &lt; /dev/null
</pre>
<p> The resulting mask looks like this: </p>
<p>fundisp foo.fits 1 2 3 4 5 6 7 8 9 10 &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;10 : 0 0 0 0 0 0 0 0 0 0 9 : 0 0 0 0 0 0 0 0 0 0 8 : 0 0 1 1 1 1 1 0 0 0 7 : 0 1 1 1 1 1 1 1 0 0 6 : 0 1 1 0 0 0 1 1 0 0 5 : 0 1 1 0 0 0 1 1 0 0 4 : 0 1 1 0 0 0 1 1 0 0 3 : 0 1 1 1 1 1 1 1 0 0 2 : 0 0 1 1 1 1 1 0 0 0 1 : 0 0 0 0 0 0 0 0 0 2</p>
<p> You can use <code>funimage</code> to create 1D image projections along the x or y axis using the <code>-p [x|y]</code> switch. This capability works for both images and tables. For example consider a <font SIZE="-1">FITS</font> table named ev.fits containing the following rows: </p>
<p>X Y&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;1 1 1 2 1 3 1 4 1 5 2 2 2 3 2 4 2 5 3 3 3 4 3 5 4 4 4 5 5 5</p>
<p> A corresponding 5&#215;5 image, called dim2.fits, would therefore contain: </p>
<p>1 2 3 4 5 &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;5 : 1 1 1 1 1 4 : 1 1 1 1 0 3 : 1 1 1 0 0 2 : 1 1 0 0 0 1 : 1 0 0 0 0</p>
<p> A projection along the y axis can be performed on either the table or the image: </p>
<p>funimage &#8211; p y ev.fits stdout | fundisp stdin 1 2 3 4 5 &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;1 : 1 2 3 4 5</p>
<p>funimage &#8211; p y dim2.fits stdout | fundisp stdin 1 2 3 4 5 &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;1 : 1 2 3 4 5</p>
<p> Furthermore, you can create a 1D image projection along any column of a table by using the <code>bincols=[column]</code> filter specification and specifying a single column. For example, the following command projects the same 1D image along the y axis of a table as use of the <code>-p y</code> switch: </p>
<p>funimage ev.fits &#8216;[bincols=y]&#8217; stdout | fundisp stdin 1 2 3 4 5 &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;1 : 1 2 3 4 5</p>
<p> Examples: </p>
<p> Create a <font SIZE="-1">FITS</font> image from a <font SIZE="-1">FITS</font> binary table: </p>
<pre>
  [sh] funimage test.ev test.fits
</pre>
<p> Display the <font SIZE="-1">FITS</font> image generated from a blocked section of <font SIZE="-1">FITS</font> binary table: </p>
<pre><code>
[sh] funimage "test.ev[2:8,3:7,2]" stdout | fundisp stdin 1 2 3 -- -- -- -- - -- -- -- -- - -- -- -- -- -1 : 20 28 36 2 : 28 36 44
</code></pre>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
