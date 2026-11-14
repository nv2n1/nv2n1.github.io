---
title: "netpbm(1)"
name: "netpbm"
section: "1"
letter: "n"
url: "/docs/linux/man/1-netpbm/"
description: "netpbm – package of graphics manipulation programs and libraries"
---

<h2 class="name">NAME</h2>
<p> netpbm &#8211; package of graphics manipulation programs and libraries</p>
<h2>DESCRIPTION</h2>
<p> <code>Netpbm</code> is a package of graphics programs and programming libraries. </p>
<p> There are over 220 separate programs in the package, most of which have &quot;pbm&quot;, &quot;pgm&quot;, &quot;ppm&quot;, or &quot;pnm&quot; in their names. For example, <code>pnmscale</code> and <code>giftopnm</code>. </p>
<p> For example, you might use <code>pnmscale</code> to shrink an image by 10%. Or use <code>pnmcomp</code> to overlay one image on top of another. Or use <code>pbmtext</code> to create an image of text. Or reduce the number of colors in an image with <code>pnmquant</code>. </p>
<h2>The Netpbm Formats</h2>
<p> All of the programs work with a set of graphics formats called the &quot;netpbm&quot; formats. Specifically, these formats are <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5), <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), and <code><a href="/docs/linux/man/5-pam/">pam</a></code>(5). The first three of these are sometimes known generically as <code>pnm</code>. Many of the Netpbm programs convert from a Netpbm format to another format or vice versa. This is so you can use the Netpbm programs to work on graphics of any format. It is also common to use a combination of Netpbm programs to convert from one non-Netpbm format to another non-Netpbm format. Netpbm has converters for over 80 graphics formats, and as a package Netpbm lets you do more graphics format conversions than any other computer graphics facility. </p>
<p> The Netpbm formats are all raster formats, i.e. they describe an image as a matrix of rows and columns of pixels. In the PBM format, the pixels are black and white. In the PGM format, pixels are shades of gray. In the PPM format, the pixels are in full color. The PAM format is more sophisticated. A replacement for all three of the other formats, it can represent matrices of general data including but not limited to black and white, grayscale, and color images. </p>
<p> Programs designed to work with PBM images have &quot;pbm&quot; in their names. Programs designed to work with PGM, PPM, and PAM images similarly have &quot;pgm&quot;, &quot;ppm&quot;, and &quot;pam&quot; in their names. </p>
<p> All Netpbm programs designed to read PGM images see PBM images as if they were PGM too. All Netpbm programs designed to read PPM images see PGM and PBM images as if they were PPM. See the section &quot;Implied Format Conversion&quot; below. </p>
<p> Programs that have &quot;pnm&quot; in their names read PBM, PGM, and PPM but unlike &quot;ppm&quot; programs, they distinguish between them and their function depends on the format. For example, <code>pnmtogif</code> creates a black and white GIF output image if its input is PBM or PGM, but a color GIF output image if its input is PPM. And <code>pnmscale</code> produces an output image of the same format as the input. A <code>ppmscale</code> program would read all three PNM input formats, but would see them all as PPM and would always generate PPM output. </p>
<p> If it seems wasteful to you to have three separate PNM formats, be aware that there is a historical reason for it. In the beginning, there were only PBMs. PGMs came later, and then PPMs. Much later came PAM, which realizes the possibility of having just one aggregate format. </p>
<p> The formats are described in the man pages <code><a href="/docs/linux/man/5-pbm/">pbm</a></code>(5), <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), and <code><a href="/docs/linux/man/5-pam/">pam</a></code>(5), </p>
<h2>Implied Format Conversion</h2>
<p> A program that uses the PGM library to read an image can read a PBM image as well as a PGM image. The program sees the PBM image as if it were the equivalent PGM image, with a maxval of 255. </p>
<p> A program that uses the PPM library to read an image can read a PGM image as well as a PPM image and a PBM image as well as a PGM image. The program sees the PBM or PGM image as if it were the equivalent PPM image, with a maxval of 255 in the PBM case and the same maxval as the PGM in the PGM case. </p>
<h2>Netpbm and Transparency</h2>
<p> In many graphics format, there&#8217;s a means of indicating that certain parts of the image are wholly or partially transparent, meaning that if it were displayed &quot;over&quot; another image, the other image would show through there. Netpbm formats deliberately omit that capability, since their purpose is to be extremely simple. </p>
<p> In Netpbm, you handle transparency via a transparency mask in a separate (slightly redefined) PGM image. In this pseudo-PGM, what would normally be a pixel&#8217;s intensity is instead it an opaqueness value. See <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5). <code>pnmcomp</code> is an example of a program that uses a PGM transparency mask. </p>
<h2>The Netpbm Programs</h2>
<p> The Netpbm programs are generally useful run by a person from a command shell, but are also designed to be used by programs. A common characteristic of Netpbm programs is that they are simple, fundamental building blocks. They are most powerful when stacked in pipelines. Netpbm programs do not use graphical user interfaces (in fact, none of them display graphics at all, except for a very simple Linux Svgalib displayer) and do not seek input from a user. </p>
<p> Each of these programs has its own man page. </p>
<h2>Common Options</h2>
<p> There are a few options that are present on all programs that are based on the Netpbm libraries, including virtually all Netpbm programs. These are not mentioned in the individual man pages for the programs. </p>
<dl>
<dt><code>-quiet</code></p>
<dd> Suppress all informational messages that would otherwise be issued to Standard Error. (To be precise, this only works to the extent that the program in question implements the Netpbm convention of issuing all informational messages via the <code>pm_message()</code> service of the Netpbm libraries).</p>
<dt><code>-version</code></p>
<dd> Instead of doing anything else, report the version of the <code>libpbm</code> library linked with the program (it may have been linked statically into the program, or dynamically linked at run time). Normally, the Netpbm programs and the libraries are installed at the same time, so this tells you the version of the program and all the other Netpbm libraries and files it uses as well. </p>
<p> Here is a directory of the Netpbm programs. You can also use <code>man -k</code> to search for a program that does what you want. </p>
</dl>
<h3>Converters</h3>
<dl>
<dt><code>ppmtompeg </code></p>
<dd> convert series of PPM frames to an MPEG movie</p>
<dt><code>jpegtopnm </code></p>
<dd> convert JFIF/JPEG/EXIF file to Netpbm format</p>
<dt><code>pnmtojpeg </code></p>
<dd> convert PPM to JPEG/JFIF/EXIF format</p>
<dt><code>anytopnm </code></p>
<dd> convert any graphics format to Netpbm format</p>
<dt><code>bmptoppm </code></p>
<dd> convert Windows or OS/2 Bitmap file to PPM</p>
<dt><code>ppmtobmp </code></p>
<dd> convert PPM to Windows or OS/2 Bitmap file</p>
<dt><code>winicontoppm</code></p>
<dd> convert Windows icon file to PPM</p>
<dt><code>ppmtowinicon</code></p>
<dd> convert PPM to Windows icon file</p>
<dt><code>giftopnm </code></p>
<dd> convert GIF to portable anymap</p>
<dt><code>ppmtogif </code></p>
<dd> convert PPM to GIF</p>
<dt><code>pnmtopng </code></p>
<dd> convert Netpbm format to Portable Network Graphics</p>
<dt><code>pngtopnm </code></p>
<dd> convert PNG (Portable Network Graphics) to Netpbm formats</p>
<dt><code>palmtopnm </code></p>
<dd> convert Palm pixmap to Netpbm formats</p>
<dt><code>pnmtopalm </code></p>
<dd> convert Netpbm formats to Palm pixmap</p>
<dt><code>jbigtopbm </code></p>
<dd> convert JBIG BIE (compressed bitmap) to PBM</p>
<dt><code>pamtopnm</code></p>
<dd> convert a PAM image to PBM, PGM, or PPM</p>
<dt><code>pbmtojbig </code></p>
<dd> convert PBM to JBIG BIE (compressed bitmap)</p>
<dt><code>pnmtofiasco </code></p>
<dd> convert Netpbm image to Fiasco (wfa) highly compressed format</p>
<dt><code>fiascotopnm </code></p>
<dd> convert Fiasco (wfa) highly compressed format to Netpbm image</p>
<dt><code>hpcdtoppm </code></p>
<dd> convert photo CD to PPM</p>
<dt><code>pbmtonokia</code></p>
<dd> convert PBM to Nokia Smart Messaging Format (SMF)</p>
<dt><code>pbmtowbmp </code></p>
<dd> convert PBM to WAP (Wireless App Protocol) Wireless Bitmap</p>
<dt><code>wbmptopbm </code></p>
<dd> convert WAP (Wireless App Protocol) Wireless Bitmap to PBM</p>
<dt><code>neotoppm</code></p>
<dd> convert Atari Neochrome (.neo) image to PPM</p>
<dt><code>ppmtoneo</code></p>
<dd> convert PPM image to Atari Neochrome (.neo)</p>
<dt><code>pbmtomda </code></p>
<dd> convert from PBM to Microdesign (for Amstrad PCWs)</p>
<dt><code>mdatopbm </code></p>
<dd> convert from Microdesign (for Amstrad PCWs) to PBM</p>
<dt><code>atktopbm </code></p>
<dd> convert Andrew Toolkit raster object to PBM</p>
<dt><code>pbmtoatk </code></p>
<dd> convert PBM to Andrew Toolkit raster object</p>
<dt><code>brushtopbm </code></p>
<dd> convert Xerox doodle brushes to PBM</p>
<dt><code>cmuwmtopbm </code></p>
<dd> convert CMU window manager format to PBM</p>
<dt><code>g3topbm </code></p>
<dd> convert Group 3 FAX to PBM</p>
<dt><code>pbmtog3 </code></p>
<dd> convert PBM to Group 3 FAX</p>
<dt><code>icontopbm </code></p>
<dd> convert Sun icon to PBM</p>
<dt><code>pbmtoicon </code></p>
<dd> convert PBM to Sun icon</p>
<dt><code>gemtopnm </code></p>
<dd> convert GEM .img format to PBM or pixmap</p>
<dt><code>macptopbm </code></p>
<dd> convert MacPaint to PBM</p>
<dt><code>pbmtomacp </code></p>
<dd> convert PBM to MacPaint</p>
<dt><code>mgrtopbm </code></p>
<dd> convert MGR format to PBM</p>
<dt><code>pbmtomgr </code></p>
<dd> convert PBM to MGR format</p>
<dt><code>pi3topbm </code></p>
<dd> convert Atari Degas .pi3 to PBM</p>
<dt><code>pbmtopi3 </code></p>
<dd> convert PBM to Atari Degas .pi3</p>
<dt><code>xbmtopbm </code></p>
<dd> convert X10 or X11 bitmap to PBM</p>
<dt><code>pbmtoxbm </code></p>
<dd> convert PBM to X11 bitmap</p>
<dt><code>pbmtox10bm </code></p>
<dd> convert PBM to X10 bitmap</p>
<dt><code>ybmtopbm </code></p>
<dd> convert Bennet Yee &quot;face&quot; file into PBM</p>
<dt><code>pbmtoybm </code></p>
<dd> convert PBM into Bennet Yee &quot;face&quot; file</p>
<dt><code>pbmto10x </code></p>
<dd> convert PBM to Gemini 10x printer graphics</p>
<dt><code>pbmtoascii </code></p>
<dd> convert PBM to ASCII graphic form</p>
<dt><code>asciitopgm </code></p>
<dd> convert ASCII character graphics to PGM</p>
<dt><code>pbmtobbnbg </code></p>
<dd> convert PBM to BBN BitGraph graphics</p>
<dt><code>pbmtocmuwm </code></p>
<dd> convert PBM to CMU window manager format</p>
<dt><code>pbmtoepson </code></p>
<dd> convert PBM to Epson printer graphics</p>
<dt><code>pbmtogem </code></p>
<dd> convert PBM into GEM .img file</p>
<dt><code>pbmtogo </code></p>
<dd> convert PBM to GraphOn graphics</p>
<dt><code>pbmtolj </code></p>
<dd> convert PBM to HP LaserJet black and white graphics</p>
<dt><code>ppmtolj </code></p>
<dd> convert PPM to HP LaserJet color graphics (PCL)</p>
<dt><code>pjtoppm </code></p>
<dd> convert HP PaintJet file to PPM</p>
<dt><code>ppmtopj </code></p>
<dd> convert PPM to HP PaintJet file</p>
<dt><code>thinkjettopbm</code></p>
<dd> convert HP Thinkjet printer stream to PBM</p>
<dt><code>pbmtoplot </code></p>
<dd> convert PBM into Unix <a href="/docs/linux/man/5-plot/">plot</a>(5) file</p>
<dt><code>pbmtoptx </code></p>
<dd> convert PBM to Printronix graphics</p>
<dt><code>pbmtozinc </code></p>
<dd> convert PBM to Zinc Interface Library icon</p>
<dt><code>fitstopnm </code></p>
<dd> convert FITS format to portable anymap</p>
<dt><code>pnmtofits </code></p>
<dd> convert Netpbm formats to FITS format</p>
<dt><code>fstopgm </code></p>
<dd> convert Usenix FaceSaver(tm) format to PGM</p>
<dt><code>pgmtofs </code></p>
<dd> convert PGM to Usenix FaceSaver(tm) format</p>
<dt><code>hipstopgm </code></p>
<dd> convert HIPS format to PGM</p>
<dt><code>lispmtopgm </code></p>
<dd> convert a Lisp Machine bitmap file into PGM format</p>
<dt><code>pgmtolispm </code></p>
<dd> convert PGM into Lisp Machine format</p>
<dt><code>pnmtops </code></p>
<dd> convert Netpbm formats to Postscript</p>
<dt><code>pstopnm </code></p>
<dd> convert Postscript to Netpbm formats</p>
<dt><code>psidtopgm </code></p>
<dd> convert PostScript &quot;image&quot; data to PGM</p>
<dt><code>pbmtolps </code></p>
<dd> convert PBM image to Postscript using lines</p>
<dt><code>pbmtoepsi </code></p>
<dd> convert a PBM image to encapsulated Postscript preview bitmap</p>
<dt><code>pbmtopsg3</code></p>
<dd> convert PBM images to Postscript using G3 fax compression.</p>
<dt><code>rawtopgm </code></p>
<dd> convert raw grayscale bytes to PGM</p>
<dt><code>pgmtopbm </code></p>
<dd> convert PGM to PBM</p>
<dt><code>gouldtoppm </code></p>
<dd> convert Gould scanner file to PPM</p>
<dt><code>ilbmtoppm </code></p>
<dd> convert IFF ILBM to PPM</p>
<dt><code>ppmtoilbm </code></p>
<dd> convert PPM to IFF ILBM</p>
<dt><code>imgtoppm </code></p>
<dd> convert Img-whatnot to PPM</p>
<dt><code>mtvtoppm </code></p>
<dd> convert MTV ray-tracer output to PPM</p>
<dt><code>pcxtoppm </code></p>
<dd> convert PC Paintbrush format to PPM</p>
<dt><code>pgmtoppm </code></p>
<dd> colorize a portable graymap into a PPM</p>
<dt><code>pi1toppm </code></p>
<dd> convert Atari Degas .pi1 to PPM</p>
<dt><code>ppmtopi1 </code></p>
<dd> convert PPM to Atari Degas .pi1</p>
<dt><code>picttoppm </code></p>
<dd> convert Macintosh PICT to PPM</p>
<dt><code>ppmtopict </code></p>
<dd> convert PPM to Macintosh PICT</p>
<dt><code>qrttoppm </code></p>
<dd> convert QRT ray-tracer output to PPM</p>
<dt><code>rawtoppm </code></p>
<dd> convert raw RGB bytes to PPM</p>
<dt><code>sldtoppm </code></p>
<dd> convert an AutoCAD slide file into a PPM</p>
<dt><code>spctoppm </code></p>
<dd> convert Atari compressed Spectrum to PPM</p>
<dt><code>sputoppm </code></p>
<dd> convert Atari uncompressed Spectrum to PPM</p>
<dt><code>tgatoppm </code></p>
<dd> convert TrueVision Targa file to PPM</p>
<dt><code>ppmtotga </code></p>
<dd> convert PPM to TrueVision Targa file</p>
<dt><code>ximtoppm </code></p>
<dd> convert Xim to PPM</p>
<dt><code>xpmtoppm </code></p>
<dd> convert XPM format to PPM</p>
<dt><code>ppmtoxpm </code></p>
<dd> convert PPM to XPM format</p>
<dt><code>yuvtoppm </code></p>
<dd> convert Abekas YUV format to PPM</p>
<dt><code>eyuvtoppm </code></p>
<dd> convert Encoder/Berkeley YUV format to PPM</p>
<dt><code>ppmtoeyuv </code></p>
<dd> convert PPM to Encoder/Berkeley YUV format</p>
<dt><code>ppmtoyuv </code></p>
<dd> convert PPM to Abekas YUV format</p>
<dt><code>ppmtoyuvsplit</code></p>
<dd> convert PPM to 3 subsampled raw YUV files</p>
<dt><code>yuvsplittoppm </code></p>
<dd> merge 3 subsampled raw YUV files to one PPM</p>
<dt><code>ppmtoacad </code></p>
<dd> convert PPM to AutoCAD database or slide</p>
<dt><code>ppmtoicr </code></p>
<dd> convert PPM to NCSA ICR graphics</p>
<dt><code>ppmtopcx </code></p>
<dd> convert PPM to PC Paintbrush format</p>
<dt><code>ppmtopgm </code></p>
<dd> convert PPM to portable graymap</p>
<dt><code>ppmtopuzz </code></p>
<dd> convert PPM to X11 &quot;puzzle&quot; file</p>
<dt><code>rasttopnm </code></p>
<dd> convert Sun raster file to Netpbm formats</p>
<dt><code>pnmtorast </code></p>
<dd> convert Netpbm formats to Sun raster file</p>
<dt><code>tifftopnm </code></p>
<dd> convert TIFF file to portable anymap</p>
<dt><code>pnmtotiff </code></p>
<dd> convert Netpbm formats to TIFF RGB file</p>
<dt><code>pnmtotiffcmyk</code></p>
<dd> convert Netpbm formats to TIFF CMYK file</p>
<dt><code>xwdtopnm </code></p>
<dd> convert X10 or X11 window dump to Netpbm formats</p>
<dt><code>pnmtoxwd </code></p>
<dd> convert Netpbm formats to X11 window dump</p>
<dt><code>pnmtoplainpnm</code></p>
<dd> convert regular Netpbm format image into plain Netpbm format</p>
<dt><code>pbmtopgm </code></p>
<dd> convert PBM file to PGM by averaging areas</p>
<dt><code>411toppm </code></p>
<dd> convert 411 (Sony Mavica) to PPM</p>
<dt><code>ppmtosixel </code></p>
<dd> convert PPM to DEC sixel format</p>
<dt><code>ppmtouil </code></p>
<dd> convert PPM to Motif UIL icon file</p>
<dt><code>sbigtopgm </code></p>
<dd> convert Santa Barbara Instrument Group CCD file to PGM</p>
<dt><code>vidtoppm </code></p>
<dd> convert Parallax XVideo JPEG to sequence of PPM files</p>
<dt><code>pnmtorle </code></p>
<dd> convert PNM to Utah Raster Toolkit (urt/rle) file</p>
<dt><code>rletopnm </code></p>
<dd> convert Utah Raster Toolkit (urt/rle) file to PNM</p>
<dt><code>ppmtoleaf </code></p>
<dd> convert PPM to Interleaf</p>
<dt><code>leaftoppm </code></p>
<dd> convert Interleaf to PPM</p>
<dt><code>bioradtopgm </code></p>
<dd> convert Biorad confocal image to PGM</p>
<dt><code>pbmtoln03 </code></p>
<dd> convert PGM image to Dec LN03+ Sixel image</p>
<dt><code>pbmtopk </code></p>
<dd> convert PBM image to packed format (PK) font</p>
<dt><code>pktopbm </code></p>
<dd> convert packed format (PK) font to PBM image </p>
</dl>
<h3>Image Generators</h3>
<p> All of these generate Netpbm format output. </p>
<dl>
<dt><code>pbmmake </code></p>
<dd> create a blank PBM image of a specified size</p>
<dt><code>ppmmake </code></p>
<dd> create a PPM image of a specified size and color</p>
<dt><code>pgmramp </code></p>
<dd> generate a grayscale ramp</p>
<dt><code>ppmpat </code></p>
<dd> create a pretty PPM image</p>
<dt><code>ppmrainbow</code></p>
<dd> create a spectrum-like image with colors fading together.</p>
<dt><code>pgmnoise </code></p>
<dd> create a PGM image of white noise</p>
<dt><code>pbmtext </code></p>
<dd> render text into a PBM image</p>
<dt><code>pbmupc </code></p>
<dd> create a Universal Product Code PBM image</p>
<dt><code>ppmcie </code></p>
<dd> generate a CIE color map PPM image</p>
<dt><code>pbmpage </code></p>
<dd> create a printer test pattern page in PBM format</p>
<dt><code>ppmcolors</code></p>
<dd> create a color map (PPM image) containing all possible colors of given maxval </p>
</dl>
<h3>Image Editors</h3>
<p> All of these work on the Netpbm formats </p>
<dl>
<dt><code>ppmlabel </code></p>
<dd> Add text to an image</p>
<dt><code>pnmshadow </code></p>
<dd> add a shadow to an image so it looks like it&#8217;s floating</p>
<dt><code>ppmbrighten </code></p>
<dd> brighten or dim an image &#8212; change saturation and value</p>
<dt><code>ppmdim </code></p>
<dd> dim an image &#8211; different way from ppmbrighten</p>
<dt><code>pbmreduce </code></p>
<dd> reduce a PBM N times, using Floyd-Steinberg</p>
<dt><code>pgmnorm </code></p>
<dd> normalize contrast in a PGM image</p>
<dt><code>ppmnorm </code></p>
<dd> normalize contrast in a PPM image</p>
<dt><code>pbmpscale </code></p>
<dd> enlarge a PBM image with edge smoothing</p>
<dt><code>pnmscale </code></p>
<dd> scale an image with high precision</p>
<dt><code>pnmscalefixed </code></p>
<dd> scale an image quickly with low precision</p>
<dt><code>pnmenlarge </code></p>
<dd> enlarge an image N times</p>
<dt><code>ppmdither </code></p>
<dd> ordered dither for color images</p>
<dt><code>pnmcolormap</code></p>
<dd> Choose the N best colors to represent an image; create a colormap</p>
<dt><code>pnmremap</code></p>
<dd> Replace colors in an image with those from a color map</p>
<dt><code>ppmquant </code></p>
<dd> quantize colors in a color image down to fewer colors</p>
<dt><code>pnmquant </code></p>
<dd> quantize colors/shades in a color or grayscale image down to fewer</p>
<dt><code>ppmquantall </code></p>
<dd> quantize colors on many files</p>
<dt><code>ppmrelief </code></p>
<dd> run a Laplacian Relief filter on a PPM</p>
<dt><code>pnmarith </code></p>
<dd> perform arithmetic on two images</p>
<dt><code>pnmcat </code></p>
<dd> concatenate images</p>
<dt><code>pnmpad </code></p>
<dd> add borders to an image</p>
<dt><code>pnmcomp </code></p>
<dd> create composite (overlay) of images</p>
<dt><code>ppmmix </code></p>
<dd> mix (overlay) two images.</p>
<dt><code>pnmcrop </code></p>
<dd> crop all like-colored borders off an image</p>
<dt><code>pamcut</code></p>
<dd> select a rectangular region from an image</p>
<dt><code>pnmcut </code></p>
<dd> obsolete version of <code>pamcut</code> (kept because it may have fewer bugs)</p>
<dt><code>pamdice</code></p>
<dd> slice an image into many horizontally and/or vertically</p>
<dt><code>pamdeinterlace</code></p>
<dd> remove every other row from an image</p>
<dt><code>pamchannel</code></p>
<dd> extract a single plane (channel, e.g. R, G, or B) from an image</p>
<dt><code>pnmdepth </code></p>
<dd> change the maxval in an image</p>
<dt><code>pnmflip </code></p>
<dd> perform one or more flip operations on an image</p>
<dt><code>pamstretch</code></p>
<dd> scale up an image by inserting interpolated pixels</p>
<dt><code>pamstretch-gen </code></p>
<dd> scale by non-integer values using pamstretch and pnmscale</p>
<dt><code>pnminvert </code></p>
<dd> invert an image</p>
<dt><code>pnmgamma </code></p>
<dd> perform gamma correction on an image</p>
<dt><code>pnmhisteq</code></p>
<dd> histogram equalize image to increase contrast</p>
<dt><code>pnmmargin </code></p>
<dd> add a margin to an image</p>
<dt><code>pnmpaste </code></p>
<dd> paste a rectangle into an image</p>
<dt><code>pnmrotate </code></p>
<dd> rotate an image</p>
<dt><code>pnmshear </code></p>
<dd> shear an image</p>
<dt><code>pnmsmooth </code></p>
<dd> smooth am image</p>
<dt><code>pnmtile </code></p>
<dd> replicate an image into a specified size</p>
<dt><code>pbmclean </code></p>
<dd> remove lone pixels (snow) from a PBM image</p>
<dt><code>pnmalias </code></p>
<dd> antialias an image</p>
<dt><code>ppmchange </code></p>
<dd> change all of one color to another in PPM image</p>
<dt><code>pnmnlfilt</code></p>
<dd> filter an image by replacing each pixel with a function of nearby pixels</p>
<dt><code>ppmshift </code></p>
<dd> shift lines of PPM image left or right a random amount</p>
<dt><code>ppmspread </code></p>
<dd> move pixels of PPM image a random amount</p>
<dt><code>pnmconvol </code></p>
<dd> general MxN convolution on an image</p>
<dt><code>rgb3toppm </code></p>
<dd> combine three portable graymaps into one PPM</p>
<dt><code>ppmtorgb3 </code></p>
<dd> separate a PPM into three portable graymaps</p>
<dt><code>pbmlife </code></p>
<dd> apply Conway&#8217;s rules of Life to a PBM image</p>
<dt><code>ppmdist </code></p>
<dd> map colors to high contrast grayscales arbitrarily</p>
<dt><code>ppmntsc </code></p>
<dd> adjust colors so they are legal for NTSC or PAL television </p>
</dl>
<h3>Image Analyzers</h3>
<p> These all work on the Netpbm formats as input. </p>
<dl>
<dt><code>pnmfile </code></p>
<dd> describe an image&#8217;s vital characteristics</p>
<dt><code>pnmpsnr </code></p>
<dd> measure difference between two images</p>
<dt><code>pgmedge </code></p>
<dd> edge-detect a PGM image</p>
<dt><code>pgmenhance </code></p>
<dd> edge-enhance a PGM image</p>
<dt><code>pgmslice </code></p>
<dd> print grayscale values for a row or column of a PGM image</p>
<dt><code>pgmtexture </code></p>
<dd> calculate textural features on a PGM image</p>
<dt><code>pgmhist </code></p>
<dd> print a histogram of the values in a PGM image</p>
<dt><code>ppmhist </code></p>
<dd> print a histogram of a PPM</p>
<dt><code>pnmhistmap</code></p>
<dd> draw a histogram of a PGM or PPM</p>
<dt><code>ppmtomap </code></p>
<dd> generate a map of all colors in an image</p>
<dt><code>ppm3d</code></p>
<dd> generate a blue/green 3D glasses image from two images </p>
</dl>
<h3>Miscellaneous</h3>
<dl>
<dt><code>ppmsvgalib</code></p>
<dd> display a PPM image on a Linux virtual console using Svgalib</p>
<dt><code>pbmmask </code></p>
<dd> create a mask bitmap from a regular bitmap</p>
<dt><code>ppmcolormask </code></p>
<dd> create mask of areas of a certain color in an image</p>
<dt><code>pnmsplit </code></p>
<dd> split a multi-image Netpbm file into multiple 1-image files</p>
<dt><code>pnmindex </code></p>
<dd> build a visual index of a bunch of Netpbm images</p>
<dt><code>pcdindex </code></p>
<dd> build a visual index of a photo CD from PCD overview file</p>
<dt><code>pnmmontage </code></p>
<dd> build multiple Netpbm images into a single montage image</p>
<dt><code>pgmbentley </code></p>
<dd> Bentleyize a PGM image</p>
<dt><code>pgmcrater </code></p>
<dd> create cratered terrain by fractal forgery</p>
<dt><code>pamoil </code></p>
<dd> turn a PNM or PAM image into an oil painting</p>
<dt><code>ppmforge </code></p>
<dd> fractal forgeries of clouds, planets, and starry skies</p>
<dt><code>pgmkernel </code></p>
<dd> generate a convolution kernel</p>
<dt><code>ppmtv </code></p>
<dd> Make an image lined so it looks like an old TV</p>
<dt><code>pbmto4425 </code></p>
<dd> Display PBM image on AT&amp;T 4425 ASCII terminal with gfx chars<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h3>Uncatalogued As Yet</h3>
<dl>
<dt><code>pnmtoddif</code></p>
<dd>
<dt><code>pnmtosgi</code></p>
<dd>
<dt><code>pnmtosir</code></p>
<dd>
<dt><code>ppmflash</code></p>
<dd>
<dt><code>ppmqvga</code></p>
<dd>
<dt><code>ppmtomitsu</code></p>
<dd>
<dt><code>ppmtopjxl</code></p>
<dd>
<dt><code>sgitopnm</code></p>
<dd>
<dt><code>sirtopnm</code></p>
<dd>
<dt><code>spottopgm</code></p>
<dd>
<dt><code>xvminitoppm</code></p>
<dd>
<dt><code>zeisstopnm</code></p>
<dd>
</dl>
<h2>The Netpbm Libraries</h2>
<p> The Netpbm programming libraries, <code><a href="/docs/linux/man/3-libpbm/">libpbm</a></code>(3), <code><a href="/docs/linux/man/3-libpgm/">libpgm</a></code>(3), <code><a href="/docs/linux/man/3-libppm/">libppm</a></code>(3), and <code><a href="/docs/linux/man/3-libpnm/">libpnm</a></code>(3), make it easy to write programs that manipulate graphic images. Their main function is to read and write files in the Netpbm format, and because the Netpbm package contains converters for all the popular graphics formats, if your program reads and writes the Netpbm formats, you can use it with any formats. </p>
<p> But the libraries also contain some utility functions, such as character drawing and RGB/YCrCb conversion. </p>
<p> The libraries have the conventional C linkage. Virtually all programs in the Netpbm package are based on the Netpbm libraries. </p>
<h3>Application Notes</h3>
<p> As a collection of primitive tools, the power of Netpbm is multiplied by the power of all the other unix tools you can use with them. These notes remind you of some of the more useful ways to do this. Often, when people want to add high level functions to the Netpbm tools, they have overlooked some existing tool that, in combination with Netpbm, already does it. </p>
<p> Often, you need to apply some conversion or edit to a whole bunch of files. </p>
<p> As a rule, Netpbm programs take one input file and produce one output file, usually on Standard Output. This is for flexibility, since you so often have to pipeline many tools together. </p>
<p> Here is an example of a shell command to convert all your of PNG files (named *.png) to JPEG files named *.jpg: </p>
<p> <code>for i in *.png; do pngtopnm $i | ppmtojpeg &gt;`basename $i .png`.jpg; done</code> </p>
<p> Or you might just generate a stream of individual shell commands, one per file, with awk or perl. Here&#8217;s how to brighten 30 YUV images that make up one second of a movie, keeping the images in the same files: </p>
<p> <code>ls *.yuv<br />
 </code> <code>| perl -ne &#8216;chomp; </code><br />
 <code>print yuvtoppm $_ | ppmbrighten -v 100 | ppmtoyuv &gt;tmp$$.yuv;, </code><br />
 <code>mv tmp$$.yuv $_ </code><br />
 <code>&#8216;<br />
 </code> <code>| sh </code> </p>
<p> The tools <code>find </code> (with the <code>-exec </code> option) and <code>xargs </code> are also useful for simple manipulation of groups of files. </p>
<p> Some shells&#8217; &quot;process substitution&quot; facility can help where a non-Netpbm program expects you to identify a disk file for input and you want it to use the result of a Netpbm manipulation. Say printcmyk takes the filename of a Tiff CMYK file as input and what you have is a PNG file <code>abc.png</code>. Try: </p>
<p> <code>printcmyk &lt;({ pngtopnm abc.png | pnmtotiffcmyk ; })</code> </p>
<p> It works in the other direction too, if you have a program that makes you name its output file and you want the output to go through a Netpbm tool. </p>
<h3>Other Graphics Software</h3>
<p> Netpbm contains primitive building blocks. It certainly is not a complete graphics library. </p>
<p> The first thing you will need to make use of any of these tools is a viewer. For the X inclined, there is <code>xzgv</code>. See <code><a href="ftp://metalab.unc.edu/pub/Linux/apps/graphics/viewers/X">ftp://metalab.unc.edu/pub/Linux/apps/graphics/viewers/X</a></code>. </p>
<p> <code>xloadimage</code> and its extension <code>xli</code> are also common ways to display a graphic image in X. </p>
<p> <code>ImageMagick </code> is like a visual version of Netpbm. Using the X/Window system on Unix, you can do basic editing of images and lots of format conversions. The package does include at least some non-visual tools. Convert, Mogrify, Montage, and Animate are popular programs from the <code>ImageMagick </code> package. <code>ImageMagick </code> runs on Unix, Windows, Windows NT, Macintosh, and VMS. </p>
<p> The Gimp is a visual image editor for Unix and X, in the same category as the more famous, less capable, and much more expensive Adobe Photoshop, etc. for Windows. See <code><a rel="nofollow" href="http://www.gimp.org">http://www.gimp.org</a></code>. </p>
<p> The <code>file </code> program looks at a file and tells you what kind of file it is. It recognizes most of the graphics formats with which Netpbm deals, so it is pretty handy for graphics work. Netpbm&#8217;s <code>anytopnm</code> program depends on <code>file. </code> See <code><a href="ftp://ftp.astron.com/pub/file">ftp://ftp.astron.com/pub/file</a></code>. </p>
<p> The Utah Raster Toolkit serves a lot of the same purpose as Netpbm, but without the emphasis on format conversions. This package is based on the RLE format, which you can convert to and from the Netpbm formats. <code><a rel="nofollow" href="http://www.cs.utah.edu/research/projects/alpha1/urt.html">http://www.cs.utah.edu/research/projects/alpha1/urt.html</a></code> gives some information on the Utah Raster Toolkit, but does not tell where to get it. </p>
<p> There are some Netpbm-like graphics tools distributed by the Army High Performance Computing Research Center at <code><a rel="nofollow" href="http://www.arc.umn.edu/gvl-software/media-tools.html">http://www.arc.umn.edu/gvl-software/media-tools.html</a></code>. These operate directly on non-Netpbm format images, so they aren&#8217;t included in the Netpbm package. However, you can use them with any image format by using the Netpbm format converters. </p>
<p> <code>Ivtools </code> is a suite of free X Windows drawing editors for Postscript, Tex, and web graphics production, as well as an embeddable and extendable vector graphic shell. It uses the Netpbm facilities. See <code><a rel="nofollow" href="http://www.ivtools.org">http://www.ivtools.org</a></code>. </p>
<p> <code>Ilib </code> is a C subroutine library with functions for adding text to an image (as you might do at a higher level with <code>pbmtext</code>, <code>pnmcomp</code>, etc.). It works with Netpbm input and output. Find it at <code><a rel="nofollow" href="http://www.radix.net/~cknudsen/Ilib">http://www.radix.net/~cknudsen/Ilib</a></code>. Netpbm also includes character drawing functions in the <code>libppm</code> library, but they do not have as fancy font capabilities (see <code>ppmlabel</code> for an example of use of the Netpbm character drawing functions). </p>
<p> <code>GD</code> is a library of graphics routines that is part of PHP. It has a subset of Netpbm&#8217;s functions and has been found to resize images more slowly and with less quality. </p>
<p> <code>pnm2ppa </code> converts to HP&#8217;s &quot;Winprinter&quot; format (for HP 710, 720, 820, 1000, etc). It is a superset of Netpbm&#8217;s <code>pbmtoppa </code> and handles, notably, color. However, it is more of a printer driver than a Netpbm-style primitive graphics building block. See <code><a rel="nofollow" href="http://sourceforge.net/project/?group_id=1322">http://sourceforge.net/project/?group_id=1322</a></code>. </p>
<p> The program <code>morph </code> morphs one image into another. It uses Targa format images, but you can use <code>tgatoppm </code> and <code>ppmtotga </code> to deal with that format. You have to use the graphical (X/Tk) Xmorph to create the mesh files that you must feed to <code>morph</code>. <code>morph </code> is part of the Xmorph package. See <code><a rel="nofollow" href="http://www.colorado-research.com/~gourlay/software/Graphics/Xmorph">http://www.colorado-research.com/~gourlay/software/Graphics/Xmorph</a></code>. </p>
<p> To create an animated GIF, or extract a frame from one, use <code>gifsicle</code>. <code>gifsicle </code> converts between animated GIF and still GIF, and you can use <code>ppmtogif </code> and <code>giftopnm </code> to connect up to all the Netpbm utilities. See <code><a rel="nofollow" href="http://www.lcdf.org/gifsicle">http://www.lcdf.org/gifsicle</a></code>. </p>
<p> To convert an image of text to text (optical character recongition &#8211; OCR), use <code>gocr </code> (think of it as an inverse of <code>pbmtext</code>). See <code><a rel="nofollow" href="http://altmark.nat.uni-magdeburg.de/~jschulen/ocr/">http://altmark.nat.uni-magdeburg.de/~jschulen/ocr/</a></code>. </p>
<p> <code><a rel="nofollow" href="http://schaik.com/pngsuite">http://schaik.com/pngsuite</a></code> contains a PNG test suite &#8212; a whole bunch of PNG images exploiting the various features of the PNG format. </p>
<p> Another version of <code>pnmtopng</code>/<code>pngtopnm</code> is at <code><a rel="nofollow" href="http://www.schaik.com/png/pnmtopng.html">http://www.schaik.com/png/pnmtopng.html</a></code>. The version in Netpbm was actually based on that package a long time ago, and you can expect to find better exploitation of the PNG format, especially recent enhancements, in that package. It may be a little less consistent with the Netpbm project and less exploitive of recent Netpbm format enhancements, though. </p>
<p> <code>jpegtran</code> Does some of the same transformations as Netpbm is famous for, but does them specifically on JPEG files and does them without loss of information. By contrast, if you were to use Netpbm, you would first decompress the JPEG image to Netpbm format, then transform the image, then compress it back to JPEG format. In that recompression, you lose a little image information because JPEG is a lossy compression. <code>jpegtran</code> comes with the Independent Jpeg Group&#8217;s (<a rel="nofollow" href="http://www.ijg.org)">http://www.ijg.org)</a> JPEG library. </p>
<p> Some tools to deal with EXIF files (see also Netpbm&#8217;s <code>jpegtopnm </code> and <code>pnmtojpeg</code>): To dump (interpret) an EXIF header: Exifdump ((<a rel="nofollow" href="http://topo.math.u-psud.fr/~bousch/exifdump.py)">http://topo.math.u-psud.fr/~bousch/exifdump.py)</a> or Jhead (<a rel="nofollow" href="http://www.sentex.net/~mwandel/jhead">http://www.sentex.net/~mwandel/jhead</a>). </p>
<p> A Python EXIF library and dumper: <a rel="nofollow" href="http://pyexif.sourceforge.net.">http://pyexif.sourceforge.net.</a> </p>
<p> Latex2html converts Latex document source to HTML document source. Part of that involves graphics, and Latex2html uses Netpbm tools for some of that. But Latex2html through its history has had some rather esoteric codependencies with Netpbm. Older Latex2html doesn&#8217;t work with current Netpbm. Latex2html-99.2beta8 works, though. </p>
<h3>Other Graphics Formats</h3>
<p> People never seem to tire of inventing new graphics formats, often completely redundant with pre-existing ones. Netpbm cannot keep up with them. Here is a list of a few that we know Netpbm does <i>not</i> handle (yet). </p>
<p>&nbsp;<wbr>&nbsp;CAL&nbsp;(originated by US Department Of Defense, favored by architects). <a rel="nofollow" href="http://www.landfield.com/faqs/graphics/fileformats-faq/part3/section-24.html">http://www.landfield.com/faqs/graphics/fileformats-faq/part3/section-24.html</a> </p>
<p>&nbsp;<wbr>&nbsp;array formats dx, general, netcdf, CDF, hdf, cm </p>
<p>&nbsp;<wbr>&nbsp;CGM+ </p>
<p>&nbsp;<wbr>&nbsp;Windows Meta File&nbsp;(.WMF).&nbsp;<wbr>&nbsp;Libwmf converts from WMF to things like&nbsp; Latex, PDF, PNG. Some of these can be input to Netpbm. </p>
<p>&nbsp;<wbr>&nbsp;Microsoft Word, RTF.&nbsp;<wbr>&nbsp;Microsoft keeps a proprietary hold on these formats. Any software you see that can handle them is likely to cost money. </p>
<p>&nbsp;<wbr>&nbsp;DXF&nbsp;(AutoCAD) </p>
<h2>HISTORY</h2>
<p> Netpbm has a long history, starting with Jef Poskanzer&#8217;s <code>Pbmplus</code> package in 1988. The file <i>HISTORY</i> in the Netpbm source code contains a historical overview as well as a detailed history release by release. </p>
<h2>AUTHOR</h2>
<p> <code>Netpbm </code> is based on the <code>Pbmplus</code> package by Jef Poskanzer, first distributed in 1988 and maintained by him until 1991. But the package contains work by countless other authors, added since Jef&#8217;s original work. In fact, the name is derived from the fact that the work was contributed by people all over the world via the Internet, when such collaboration was still novel enough to merit naming the package after it. </p>
<p> Bryan Henderson has been maintaining <code>Netpbm</code> since 1999. In addition to packaging work by others, Bryan has also written a significant amount of new material for the package. </p>
<h2>Index</h2>
