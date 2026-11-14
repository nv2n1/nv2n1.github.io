---
title: "pamundice(1)"
name: "pamundice"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamundice/"
description: "pamundice – combine grid of images (tiles) into one"
---

<h2 class="name">NAME</h2>
<p> pamundice &#8211; combine grid of images (tiles) into one</p>
<h2>EXAMPLE</h2>
<pre>
<tt>
    $ pamdice myimage.ppm -outstem=myimage_part -width=10 -height=8
    $ pamundice myimage_part_%1d_%1a.ppm -across=10 -down=8 &gt;myimage.ppm
    $ pamundice myimage.ppm myimage_part_%2a -across=13 -hoverlap=9
</tt>
</pre>
<h2>SYNOPSIS</h2>
<p> <code>pamundice</code> </p>
<p> [<code>-across=</code><i>n</i>] </p>
<p> [<code>-down=</code><i>n</i>] </p>
<p> [<code>-hoverlap=</code><i>pixels</i>] </p>
<p> [<code>-voverlap=</code><i>pixels</i>] </p>
<p> [<code>-verbose</code>] </p>
<p> <i>input_filename_pattern</i> </p>
<p> You can use the minimum unique abbreviation of the options. You can use two hyphens instead of one. You can separate an option name from its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamundice</code> reads a bunch of Netpbm images as input and combines them as a grid of tiles into a single output image of the same kind on Standard Output. </p>
<p> You can optionally make the pieces overlap. </p>
<p> See the <i>input_filename_pattern</i> argument for information on naming of the input files. </p>
<p> The input images must all have the same format (PAM, PPM, etc.) and maxval and for PAM must have the same depth and tuple type. All the images in a rank (horizontal row of tiles) must have the same height. All the images in a file (vertical column of tiles) must have the same width. But it is not required that every rank have the same height or every file have the same width. </p>
<p> <code>pamdice</code> is the inverse of <code>pamundice</code>. You can use <code>pamundice</code> to reassemble an image sliced up by <code>pamdice</code>. You can use <code>pamdice</code> to recreate the tiles of an image created by <code>pamundice</code>, but to do this the original ranks must all have been the same height except for the bottom one and the original files must all have been the same width except the right one. </p>
<p> One use for this is to make pieces that take less computer resources than the whole image to process. For example, you might have an image so large that an image editor can&#8217;t read it all into memory or processes it very slowly. You can split it into smaller pieces with <code>pamdice</code>, edit one at a time, and then reassemble them with <code>pamundice</code>. </p>
<p> An alternative to join images in a single direction (i.e. a single rank or a single file) is <code>pnmcat</code>. <code>pnmcat</code> gives you more flexibility than <code>pamundice</code> in identifying the input images: you can supply them on Standard Input or as a list of arbitrarily named files. </p>
<p> To join piecewise photographs, use <code>pnmstitch</code> instead of <code>pamundice</code>, because it figures out where the pieces overlap, even if they don&#8217;t overlap exactly vertically or horizontally. </p>
<p> To create an image of the same tile repeated in a grid, that&#8217;s <code>pnmtile</code>. </p>
<p> <code>pnmindex</code> does a similar thing to <code>pamundice</code>: it combines a bunch of small images in a grid into a big one. But its purpose is to produce a an index image of the input images. So it leaves space between them and has labels for them, for example. </p>
<h2>ARGUMENTS</h2>
<p> There is one non-option argument, and it is mandatory: <i>input_filename_pattern</i>. This tells <code>pamundice</code> what files contain the input tiles. </p>
<p> <code>pamundice</code> reads the input images from files which are named with a pattern that indicates their positions in the combined image. For example, <code>tile_00_05.ppm</code> could be the 6th tile over in the 1st rank, while <code>tile_04_01</code> is the 2nd tile over in the 5th rank. </p>
<p> You cannot supply any of the data on Standard Input, and the files must be the kind that <code>pamundice</code> can close and reopen and read the same image a second time (e.g. a regular file is fine; a named pipe is probably not). </p>
<p> <i>input_filename_pattern</i> is a printf-style pattern. (See the standard C library <code>printf</code> subroutine). For the example above, it would be <code>tile_%2d_%2a.ppm</code>. The only possible conversion specifiers are: </p>
<dl>
<dt><code>d</code></p>
<dd> &#8216;down&#8217;: The rank (row) number, starting with 0. </p>
<dt><code>a</code></p>
<dd> &#8216;across&#8217;: The file (column) number, starting with 0. </p>
<dt><code>%</code></p>
<dd> The per cent character (%). </p>
</dl>
<p> The number between the % and the conversion specifier is the precision and is required. It says how many characters of the file name are described by that conversion. The rank or file number is filled with leading zeroes as necessary. </p>
<p> So the example <code>tile_%2d_%2a.ppm</code> means to get the name of the file that contains the tile at Rank 0, File 5, you: </p>
<dl>
<dt>&bull;</p>
<dd> replace the &#8216;%2d&#8217; with the rank number, as a 2 digit decimal number: &#8217;00&#8217; </p>
<dt>&bull;</p>
<dd> Replace the &#8216;%2a&#8217; with the file number, as a 2 digit decimal number: &#8217;05&#8217; </p>
</dl>
<p> Note that this pattern describes file names that <code>pamdice</code> produces, except that the precision may be more or less. (<code>pamdice</code> uses however many digits are required for the highest numbered image). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-across=</code><i>N</i></p>
<dd> This is the number of tiles across in the grid, i.e. the number of tiles in each rank, or the number of files. </p>
<p> Default is 1. </p>
<dt><code>-down=</code><i>N</i></p>
<dd> This is the number of tiles up and down in the grid, i.e. the number of tiles in each file, or the number of ranks. </p>
<p> Default is 1. </p>
<dt><code>-hoverlap=</code><i>pixels</i></p>
<dd> This is the amount in pixels to overlap the tiles horizontally. <code>pamundice</code> clips this much off the right edge of every tile before joining it to the adjacent image to the right. The tiles along the right edge remain whole. </p>
<p> There must not be any input image narrower than this. </p>
<p> Note that this undoes the effect of the same <code>-hoverlap</code> option of <code>pamdice</code>. </p>
<p> Default is zero &#8212; no overlap. </p>
<dt><code>-voverlap=</code><i>pixels</i></p>
<dd> This is analogous to <code>-hoverlap</code>, but <code>pamundice</code> clips the bottom edge of each image before joining it to the one below. </p>
<dt><code>-verbose</code></p>
<dd> Print information about the processing to Standard Error. </p>
</dl>
<h2>HISTORY</h2>
<p> <code>pamundice</code> was new in Netpbm 10.39 (June 2007). Before that, <code>pnmcat</code> is the best substitute. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamundice/">pamundice</a></code>(1) , <code><a href="/docs/linux/man/1-pnmcat/">pnmcat</a></code>(1) , <code><a href="/docs/linux/man/1-pnmindex/">pnmindex</a></code>(1) , <code><a href="/docs/linux/man/1-pnmtile/">pnmtile</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<h2>Index</h2>
