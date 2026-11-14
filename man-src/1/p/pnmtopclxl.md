---
title: "pnmtopclxl(1)"
name: "pnmtopclxl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmtopclxl/"
description: "pnmtopclxl – convert a PNM image to an HP LaserJet PCL XL printer stream"
---

<h2>NAME</h2>
<p> pnmtopclxl &#8211; convert a PNM image to an HP LaserJet PCL XL printer stream </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmtopclxl</code> &lt;br&gt;{ [<code>-dpi=</code><i>N</i>] [<code>-xoffs=</code><i>N</i>] [<code>-yoffs=</code><i>N</i>] [<code>-center</code>] [<code>-duplex=</code>{<code>vertical</code>|<code>horizontal</code>}] [<code>-format=</code><i>paperformat</i>] [<code>-feeder=</code><i>N</i>] [<code>-copies=</code><i>N</i>] [<code>-rendergray</code>] [<code>-jobsetup=</code><i>filename</i>] &lt;br&gt;| <code>-embedded</code> &lt;br&gt;} [<code>-colorok</code>] <i>pnmfile1</i> <i>pnmfile2</i> &#8230; </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pnmtopclxl</code> reads one or more PNM input streams, each containing one or more PNM images, and generates a sequence of output pages in the HP PCL-XL (formerly named PCL 6) printer control language. You can send this stream to a PCL-XL printer to print the images. </p>
<p> Alternatively, you can make <code>pnmtopclxl</code> generate just the PCL-XL instructions to print an image, which you can embed in your own PCL-XL stream to place an image on one of your pages. (<code>-embedded</code> option). </p>
<p> If the input is PPM, the output is a color printer stream (the PCL color space is RGB). Otherwise, the output is grayscale (the PCL color space is grayscale). If you want a grayscale output from a color input, run your input through <code><a href="/docs/linux/man/1-ppmtopgm/">ppmtopgm</a></code>(1) <code>-colorok</code> option for more information about choosing between color and grayscale. </p>
<p> The output goes to Standard Output. All of the pages go to one file, concatenated in the same order as the input images. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-dpi=</code><i>N</i></p>
<dd> This option selects the resolution of the image (not the printer!). <i>N</i> is the resolution in dots per inch, from 1 to 65535. The default is 300. </p>
<dt><code>-xoffs=</code><i>N</i></p>
<dd> This option and <code>-yoffs</code> determine the location on the page of the upper left corner of each image. Note that the image may have built in borders too, which would make the main image within more left and down that what you specify here. </p>
<p> <code>-xoffs</code> and <code>-yoffs</code> specify the distance from the left of the page and from the top of the page, respectively, in inches, of the upper left corner of the image. The default for each is zero. </p>
<p> These options are meaningless if you specify <code>-center</code>. </p>
<dt><code>-yoffs</code> <i>N</i></p>
<dd> See <code>-xoffs</code>. </p>
<dt><code>-center</code></p>
<dd> This option tells <code>pnmtopclxl</code> to center each image on the page. If you don&#8217;t specify this option, the position of an image on the page is determined by <code>-xoffs</code> and <code>-yoffs</code> (or their defaults). </p>
<dt><code>-duplex=</code>{<code>vertical</code>|<code>horizontal</code>}</p>
<dd> This option causes <code>pnmtopclxl</code> to create a printer stream that prints pages on both sides of the sheet of paper. <code>vertical</code> means to print them so that the left edge of both pages is on the same edge of the sheet, while <code>horizontal</code> means the more usual duplexing where the top of both pages is on the same edge of the sheet. </p>
<dt><code>-format=</code><i>paperformat</i></p>
<dd> This option selects the media (e.g. paper size) that the printer control stream specifies. <i>paperformat</i> is one of the following self-explanatory keywords: </p>
<dt>&bull;</p>
<dd> letter</p>
<dt>&bull;</p>
<dd> legal</p>
<dt>&bull;</p>
<dd> a3</p>
<dt>&bull;</p>
<dd> a4</p>
<dt>&bull;</p>
<dd> a5</p>
<dt>&bull;</p>
<dd> a6</p>
<dt>&bull;</p>
<dd> jb4</p>
<dt>&bull;</p>
<dd> jb5</p>
<dt>&bull;</p>
<dd> jb6</p>
<dt>&bull;</p>
<dd> exec</p>
<dt>&bull;</p>
<dd> ledger</p>
<dt>&bull;</p>
<dd> b5envelope</p>
<dt>&bull;</p>
<dd> c5envelope</p>
<dt>&bull;</p>
<dd> com10envelope</p>
<dt>&bull;</p>
<dd> monarchenvelope</p>
<dt>&bull;</p>
<dd> dlenvelope</p>
<dt>&bull;</p>
<dd> jpostcard</p>
<dt>&bull;</p>
<dd> jdoublepostcard </p>
<p> The default is <code>letter</code>. </p>
<dt><code>-feeder=</code><i>N</i></p>
<dd> This options selects the media source (e.g. paper tray) that the printer control stream specifies. </p>
<dt><code>-copies=</code><i>N</i></p>
<dd> This option specifies the number of copies that the printer control stream tells the printer to print. </p>
<dt><code>-rendergray</code></p>
<dd> This option causes <code>pnmtopclxl</code> to include in the output stream a command to set the RENDERMODE environment variable to GRAYSCALE, which typically causes the printer to print in grayscale regardless of the colors in the input, and may cause it to run much faster even if the image is grayscale anyway. </p>
<p> This option was new in Netpbm 10.29 (August 2005). </p>
<dt><code>-jobsetup=</code><i>filename</i></p>
<dd> This option causes <code>pnmtopclxl</code> to include arbitrary job setup PJL commands at the beginning of the output stream. It reads them from the named file. </p>
<p> <code>pnmtopclxl</code> does not inspect these commands in any way, but it does expect them to be job setup commands. If you have garbage in your file, you will hear from the printer. </p>
<p> This option was new in Netpbm 10.29 (August 2005). </p>
<dt><code>-colorok</code></p>
<dd> This option simply tells <code>pnmtopclxl</code> not to warn you if you supply a color input and therefore get color output. By default, <code>pnmtopclxl</code> issues a warning any time it produces a color printer stream because it is usually a mistake. It&#8217;s a mistake because PCL XL is mainly used for laser printers, and laser printers are mainly black and white. If you send a color print stream to a black and white printer, it typically refuses to print anything, and even if it manages to convert it to black and white and print it, it takes 3 times as long to transmit a color stream to the printer than to transmit the grayscale image that gives the same result. </p>
<dt><code>-embedded</code></p>
<dd> Without this option, <code>pnmtopclxl</code> generates an entire printer control stream that sets up the printer, ejects pages, and places a lone image on each page. With the option, <code>pnmtopclxl</code> generates only the instructions to generate the image itself. This is not useful all by itself, but you can embed it in a suitable PCL-XL stream in order to add an image to it. </p>
<p> This makes sense only for a single image, so you cannot specify multiple input files and if an input file has multiple images in it, <code>pnmtopclxl</code> ignores any after the first (it won&#8217;t even read them). </p>
<p> All the options that control the printer control stream outside the image itself, such as <code>-xoffs</code> and <code>-feeder</code> are invalid with <code>-embedded</code>. </p>
<p> This option was new in Netpbm 10.54 (March 2011). </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ppmtolj/">ppmtolj</a></code>(1) , <code><a href="/docs/linux/man/1-pbmtolj/">pbmtolj</a></code>(1) , <code><a href="/docs/linux/man/1-ppmtopj/">ppmtopj</a></code>(1) , <code><a href="/docs/linux/man/1-ppmtopjxl/">ppmtopjxl</a></code>(1) , <code><a href="/docs/linux/man/1-thinkjettopbm/">thinkjettopbm</a></code>(1) , <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) </p>
<h2>HISTORY</h2>
<p> <code>pnmtopclxl</code> was added to Netpbm in Release 10.6 (July 2002). It was contributed by <i>Jochen Karrer</i>. </p>
<h2>Index</h2>
