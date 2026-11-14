---
title: "gm(1)"
name: "gm"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gm/"
description: "gm – command-line utility to create, edit, compare, convert, or display images"
---

<dt>
<dd></dl>
<h2 class="name">NAME</h2>
<p> gm &#8211; command-line utility to create, edit, compare, convert, or display images</p>
<h2>SYNOPSIS</h2>
<p> <code>gm animate</code> <code>[</code> <i>options &#8230;</i> <code>]</code> <i>file</i> <code>[ [</code> <i>options &#8230;</i> <code>]</code> <i>file &#8230;</i> <code>]</code> </p>
<p> <code>gm batch</code> <code>[</code> <i>options &#8230;</i> <code>]</code> <code>[</code> <i>script</i> <code>]</code> </p>
<p> <code>gm benchmark</code> <code>[</code> <i>options &#8230;</i> <code>]</code> subcommand </p>
<p> <code>gm compare</code> <code>[</code> <i>options</i> <code>&#8230; ]</code> <i>reference-image</i> <code>[</code> <i>options</i> <code>&#8230; ]</code> <i>compare-image</i> <code>[</code> <i>options</i> <code>&#8230; ]</code> </p>
<p> <code>gm composite</code> <code>[</code> <i>options &#8230;</i> <code>]</code> <i>change-image base-image</i> <code>[</code> <i>mask-image</i> <code>]</code> <i>output-image</i> </p>
<p> <code>gm conjure</code> <code>[</code> <i>options</i> <code>]</code> <i>script.msl</i> <code>[ [</code> <i>options</i> <code>]</code> <i>script.msl</i> <code>]</code> </p>
<p> <code>gm convert</code> <code>[ [</code> <i>options &#8230;</i> <code>] [</code> <i>input-file &#8230;</i> <code>] [</code> <i>options &#8230;</i> <code>] ]</code> <i>output-file</i> </p>
<p> <code>gm display</code> <code>[</code> <i>options &#8230;</i> <code>]</code> <i>file &#8230;</i> <code>[ [</code><i>options &#8230;</i> <code>]</code><i>file &#8230;</i> <code>]</code> </p>
<p> <code>gm identify</code> <i>file</i> <code>[</code> <i>file &#8230;</i> <code>]</code> </p>
<p> <code>gm import</code> <code>[</code> <i>options &#8230;</i> <code>]</code> <i>file</i> </p>
<p> <code>gm mogrify</code> <code>[</code> <i>options &#8230;</i> <code>]</code> <i>file &#8230;</i> </p>
<p> <code>gm montage</code> <code>[</code> <i>options &#8230;</i> <code>]</code> <i>file</i> <code>[ [</code> <i>options &#8230;</i> <code>]</code> <i>file &#8230;</i> <code>]</code> <i>output-file</i> </p>
<p> <code>gm time</code> subcommand </p>
<p> <code>gm version</code></p>
<h2>DESCRIPTION</h2>
<p>&nbsp;<wbr>GraphicsMagick&#8217;s&nbsp;<wbr><code>gm</code>&nbsp;<wbr>provides a suite of utilities for creating, comparing, converting, editing, and displaying images. All of the utilities are provided as sub-commands of a single <code>gm</code> executable: </p>
<p> <code>animate</code> displays an animation (e.g. a GIF file) on any workstation display running an <i>X</i> server. </p>
<p> <code>batch</code> executes an arbitary number of the utility commands (e.g. <code>convert</code>) in the form of a simple linear batch script in order to improve execution efficiency, and/or to allow use as a subordinate co-process under the control of an arbitrary script or program. </p>
<p> <code>benchmark</code> executes one of the other utility commands (e.g. <code>convert</code>) for a specified number of iterations, or execution time, and reports execution time and other profiling information such as CPU utilization. <code>Benchmark</code> provides various operating modes including executing the command with a varying number of threads, and alternate reporting formats such as comma-separated value (CSV). </p>
<p> <code>compare</code> compares two images and reports difference statistics according to specified metrics and/or outputs an image with a visual representation of the differences. It may also be used to test if images are similar within a particular range and specified metric, returning a truth value to the executing environment. </p>
<p> <code>composite</code> composites images (blends or merges images together) to create new images. </p>
<p> <code>conjure</code> interprets and executes scripts in the Magick Scripting Language (MSL). </p>
<p> <code>convert</code> converts an input file using one image format to an output file with the same or differing image format while applying an arbitrary number of image transformations. </p>
<p> <code>display</code> is a machine architecture independent image processing and display facility. It can display an image on any workstation display running an <i>X</i> server. </p>
<p> <code>identify</code> describes the format and characteristics of one or more image files. It will also report if an image is incomplete or corrupt. </p>
<p> <code>import</code> reads an image from any visible window on an <i>X</i> server and outputs it as an image file. You can capture a single window, the entire screen, or any rectangular portion of the screen. </p>
<p> <code>mogrify</code> transforms an image or a sequence of images. These transforms include <code>image scaling</code>, <code>image rotation</code>, <code>color reduction</code>, and others. The transmogrified image <code>overwrites</code> the original image. </p>
<p> <code>montage</code> creates a composite by combining several separate images. The images are tiled on the composite image with the name of the image optionally appearing just below the individual tile. </p>
<p> <code>time</code> executes a subcommand and reports the user, system, and total execution time consumed. </p>
<p> <code>version</code> reports the GraphicsMagick release version, maximum sample-depth, copyright notice, supported features, and the options used while building the software. </p>
<p> The <code>GraphicsMagick</code> utilities recognize the following image formats: </p>
<p> <code>Name</code> <code>Mode</code> <code>Description</code><br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>3FR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Hasselblad Photo RAW<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>8BIM&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Photoshop resource format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>8BIMTEXT&nbsp;<wbr>&nbsp;<wbr>rw- Photoshop resource text format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>8BIMWTEXT rw- Photoshop resource wide text format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>APP1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Raw application information<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>APP1JPEG&nbsp;<wbr>&nbsp;<wbr>rw- Raw JPEG binary data<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>ART&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; PF1: 1st Publisher<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>ARW&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Sony Alpha DSLR RAW<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>AVS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>AVS X image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>BIE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Joint Bi-level Image experts Group<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>interchange format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>BMP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Microsoft Windows bitmap image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>BMP2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-w- Microsoft Windows bitmap image v2<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>BMP3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-w- Microsoft Windows bitmap image v3<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>CACHE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; Magick Persistent Cache image format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>CALS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Continuous Acquisition and Life-cycle<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Support Type 1 image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>CAPTION&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Caption&nbsp;<wbr>(requires separate size info)<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>CIN&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Kodak Cineon Format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>CMYK&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Raw cyan, magenta, yellow, and black<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>samples&nbsp;<wbr>(8 or 16 bits, depending on<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the image depth)<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>CMYKA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Raw cyan, magenta, yellow, black, and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>matte samples&nbsp;<wbr>(8 or 16 bits, depending<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>on the image depth)<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>CR2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Canon Photo RAW<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>CRW&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Canon Photo RAW<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>CUR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Microsoft Cursor Icon<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>CUT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; DR Halo<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>DCM&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Digital Imaging and Communications in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Medicine image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>DCR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Kodak Photo RAW<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>DCX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>ZSoft IBM PC multi-page Paintbrush<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>DNG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Adobe Digital Negative<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>DPS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Display PostScript Interpreter<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>DPX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Digital Moving Picture Exchange<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>EPDF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Encapsulated Portable Document Format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>EPI&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Adobe Encapsulated PostScript<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Interchange format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>EPS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Adobe Encapsulated PostScript<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>EPS2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-w- Adobe Level II Encapsulated PostScript<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>EPS3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-w- Adobe Level III Encapsulated PostScript<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>EPSF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Adobe Encapsulated PostScript<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>EPSI&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Adobe Encapsulated PostScript<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Interchange format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>EPT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Adobe Encapsulated PostScript with MS-DOS<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TIFF preview<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>EPT2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Adobe Level II Encapsulated PostScript<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>with MS-DOS TIFF preview<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>EPT3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Adobe Level III Encapsulated PostScript<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>with MS-DOS TIFF preview<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>EXIF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Exif digital camera binary data<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>FAX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Group 3 FAX&nbsp;<wbr>(Not TIFF Group3 FAX!)<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>FITS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Flexible Image Transport System<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>FRACTAL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Plasma fractal image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>FPX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- FlashPix Format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>GIF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>CompuServe graphics interchange format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>GIF87&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- CompuServe graphics interchange format<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(version 87a)<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>GRADIENT&nbsp;<wbr>&nbsp;<wbr>r&#8211; Gradual passing from one shade to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>another<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>GRAY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Raw gray samples&nbsp;<wbr>(8/16/32 bits,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>depending on the image depth)<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>HISTOGRAM -w- Histogram of the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>HRZ&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; HRZ: Slow scan TV<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>HTML&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-w- Hypertext Markup Language and a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>client-side image map<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>ICB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Truevision Targa image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>ICC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- ICC Color Profile<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>ICM&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- ICC Color Profile<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>ICO&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Microsoft icon<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>ICON&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Microsoft icon<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>IDENTITY&nbsp;<wbr>&nbsp;<wbr>r&#8211; Hald CLUT identity image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>IMAGE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; GraphicsMagick Embedded Image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>INFO&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-w+&nbsp;<wbr>Image descriptive information and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>statistics<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>IPTC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- IPTC Newsphoto<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>IPTCTEXT&nbsp;<wbr>&nbsp;<wbr>rw- IPTC Newsphoto text format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>IPTCWTEXT rw- IPTC Newsphoto wide text format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>JBG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Joint Bi-level Image experts Group<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>interchange format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>JBIG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Joint Bi-level Image experts Group<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>interchange format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>JNG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- JPEG Network Graphics<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>JP2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- JPEG-2000 JP2 File Format Syntax<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>JPC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- JPEG-2000 Code Stream Syntax<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>JPEG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Joint Photographic Experts Group<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>JFIF format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>JPG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Joint Photographic Experts Group<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>JFIF format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>K25&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Kodak Photo RAW<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>KDC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Kodak Photo RAW<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>LABEL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Text image format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>M2V&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>MPEG-2 Video Stream<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>MAP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Colormap intensities and indices<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>MAT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; MATLAB image format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>MATTE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-w+&nbsp;<wbr>MATTE format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>MIFF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Magick Image File Format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>MNG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Multiple-image Network Graphics<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>MONO&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Bi-level bitmap in least-significant-<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-byte-first order<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>MPC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Magick Persistent Cache image format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>MPEG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>MPEG-1 Video Stream<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>MPG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>MPEG-1 Video Stream<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>MRW&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Minolta Photo Raw<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>MSL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Magick Scripting Language<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>MTV&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>MTV Raytracing image format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>MVG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Magick Vector Graphics<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>NEF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Nikon Electronic Format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>NULL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Constant image of uniform color<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>OTB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- On-the-air bitmap<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>P7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Xv thumbnail format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PAL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- 16bit/pixel interleaved YUV<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PALM&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Palm Pixmap<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PBM&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Portable bitmap format&nbsp;<wbr>(black and white)<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PCD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Photo CD<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PCDS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Photo CD<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PCL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-w- Page Control Language<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PCT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Apple Macintosh QuickDraw/PICT<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PCX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- ZSoft IBM PC Paintbrush<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PDB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Palm Database ImageViewer Format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PDF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Portable Document Format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PEF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Pentax Electronic File<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PFA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; TrueType font<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PFB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; TrueType font<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PGM&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Portable graymap format&nbsp;<wbr>(gray scale)<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PGX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; JPEG-2000 VM Format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PICON&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Personal Icon<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PICT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Apple Macintosh QuickDraw/PICT<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PIX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Alias/Wavefront RLE image format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PLASMA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Plasma fractal image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PNG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Portable Network Graphics<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PNG24&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Portable Network Graphics, 24 bit RGB<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>opaque only<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PNG32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Portable Network Graphics, 32 bit RGBA<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>semitransparency OK<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PNG8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Portable Network Graphics, 8-bit<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>indexed, binary transparency only<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PNM&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Portable anymap<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PPM&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Portable pixmap format&nbsp;<wbr>(color)<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PREVIEW&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-w- Show a preview an image enhancement,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>effect, or f/x<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Adobe PostScript<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PS2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-w+&nbsp;<wbr>Adobe Level II PostScript<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PS3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-w+&nbsp;<wbr>Adobe Level III PostScript<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PSD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Adobe Photoshop bitmap<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PTIF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Pyramid encoded TIFF<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>PWP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Seattle Film Works<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>RAF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Fuji Photo RAW<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>RAS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>SUN Rasterfile<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>RGB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Raw red, green, and blue samples<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>RGBA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Raw red, green, blue, and matte samples<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>RLA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Alias/Wavefront image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>RLE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Utah Run length encoded image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>SCT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Scitex HandShake<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>SFW&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Seattle Film Works<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>SGI&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Irix RGB image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>SHTML&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-w- Hypertext Markup Language and a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>client-side image map<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>STEGANO&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Steganographic image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>SUN&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>SUN Rasterfile<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>SVG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Scalable Vector Gaphics<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>TEXT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Raw text<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>TGA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Truevision Targa image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>TIFF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Tagged Image File Format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>TILE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Tile image with a texture<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>TIM&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; PSX TIM<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>TOPOL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; TOPOL X Image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>TTF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; TrueType font<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>TXT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Raw text<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>UIL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-w- X-Motif UIL table<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>UYVY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- 16bit/pixel interleaved YUV<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>VDA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Truevision Targa image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>VICAR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- VICAR rasterfile format<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>VID&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Visual Image Directory<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>VIFF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Khoros Visualization image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>VST&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Truevision Targa image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>WBMP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Wireless Bitmap&nbsp;<wbr>(level 0)&nbsp;<wbr>image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>WMF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Windows Metafile<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>WPG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Word Perfect Graphics<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- X Image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>X3F&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Foveon X3&nbsp;<wbr>(Sigma/Polaroid)&nbsp;<wbr>RAW<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>XBM&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- X Windows system bitmap&nbsp;<wbr>(black<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>and white)<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>XC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; Constant image uniform color<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>XCF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&#8211; GIMP image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>XMP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- Adobe XML metadata<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>XPM&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- X Windows system pixmap&nbsp;<wbr>(color)<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>XV&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw+&nbsp;<wbr>Khoros Visualization image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>XWD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- X Windows system window dump&nbsp;<wbr>(color)<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>YUV&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rw- CCIR 601 4:1:1 or 4:2:2&nbsp;<wbr>(8-bit only)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>Modes:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Read<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>w&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Write<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Multi-image </p>
<p> <i>Support for some of these formats require additional programs or libraries. See README in the source package for where to find optional additional software</i>. </p>
<p> Note, a format delineated with + means that if more than one image is specified, frames are combined into a single multi-image file. Use <code>+adjoin</code> if you want a single image produced for each frame. </p>
<p> Your installation might not support all of the formats in the list. To get an accurate listing of the formats supported by your particular configuration, run &quot;gm convert -list format&quot;. </p>
<p> Raw images are expected to have one byte per pixel unless <code>gm</code> is compiled in 16-bit quantum mode or in 32-bit quantum mode. Here, the raw data is expected to be stored two or four bytes per pixel, respectively, in most-significant-byte-first order. For example, you can tell if <code>gm</code> was compiled in 16-bit mode by typing &quot;gm version&quot; without any options, and looking for &quot;Q:16&quot; in the first line of output.</p>
<h2>FILES AND FORMATS</h2>
<p> By default, the image format is determined by its magic number, i.e., the first few bytes of the file. To specify a particular image format, precede the filename with an image format name and a colon (<i>i.e.</i><code>ps:image</code>) or specify the image type as the filename suffix (<i>i.e.</i><code>image.ps</code>). The magic number takes precedence over the filename suffix and the prefix takes precedence over the magic number and the suffix in input files. When a file is read, its magic number is stored in the &quot;image-&gt;magick&quot; string. In output files, the prefix takes precedence over the filename suffix, and the filename suffix takes precedence over the &quot;image-&gt;magick&quot; string. </p>
<p> To read the &quot;built-in&quot; formats (GRANITE, H, LOGO, NETSCAPE, PLASMA, and ROSE) use a prefix (including the colon) without a filename or suffix. To read the XC format, follow the colon with a color specification. To read the CAPTION format, follow the colon with a text string or with a filename prefixed with the at symbol (<code>@</code>). </p>
<p> When you specify <code>X</code> as your image type, the filename has special meaning. It specifies an X window by <code>id, name</code>, or <code>root</code>. If no filename is specified, the window is selected by clicking the mouse in the desired window. </p>
<p> Specify <i>input_file</i> as <code>&#8211;</code> for standard input, <i>output_file</i> as <code>&#8211;</code> for standard output. If <i>input_file</i> has the extension <code>.Z</code> or <code>.gz</code>, the file is uncompressed with <code>uncompress</code> or <code>gunzip</code> respectively. If <i>output_file</i> has the extension <code>.Z</code> or <code>.gz</code>, the file is compressed using with <i>compress</i> or <i>gzip</i> respectively. </p>
<p> Use an optional index enclosed in brackets after an input file name to specify a desired subimage of a multi-resolution image format like Photo CD (e.g. &quot;img0001.pcd[4]&quot;) or a range for MPEG images (e.g. &quot;video.mpg[50-75]&quot;). A subimage specification can be disjoint (e.g. &quot;image.tiff[2,7,4]&quot;). For raw images, specify a subimage with a geometry (e.g. -size 640&#215;512 &quot;image.rgb[320&#215;256+50+50]&quot;). Surround the image name with quotation marks to prevent your shell from interpreting the square brackets. Single images are written with the filename you specify. However, multi-part images (e.g., a multi-page PostScript document with <code>+adjoin</code> specified) may be written with the scene number included as part of the filename. In order to include the scene number in the filename, it is necessary to include a printf-style %d format specification in the file name and use the +adjoin option. For example, </p>
<p>&nbsp;<wbr>image%02d.miff </p>
<p> writes files <i>image00.miff, image01.miff,</i> etc. Only a single specification is allowed within an output filename. If more than one specification is present, it will be ignored. It is best to embed the scene number in the base part of the file name, not in the extension, because the extension will not be a recognizeable image type. </p>
<p> When running a commandline utility, you can prepend an at sign @ to a filename to read a list of image filenames from that file. This is convenient in the event you have too many image filenames to fit on the command line.</p>
<h2>OPTIONS</h2>
<p> Options are processed in command line order. Any option you specify on the command line remains in effect for the set of images that follows, until the set is terminated by the appearance of any option or <code>-noop</code>. Some options only affect the decoding of images and others only the encoding. The latter can appear after the final group of input images. </p>
<p> This is a combined list of the command-line options used by the GraphicsMagick utilities (<i>animate</i>, <i>compare</i>, <i>composite</i>, <i>convert</i>, <i>display</i>, <i>identify</i>, <i>import</i>, <i>mogrify</i> and <i>montage</i>). </p>
<p> In this document, angle brackets (&quot;&lt;&gt;&quot;) enclose variables and curly brackets (&quot;{}&quot;) enclose optional parameters. For example, &quot;<code>-fuzz &lt;distance&gt;{%}</code>&quot; means you can use the option &quot;-fuzz 10&quot; or &quot;-fuzz 2%&quot;. </p>
<dl>
<dt><code>-adjoin</code></p>
<dd> join images into a single multi-image file </p>
<p> By default, all images of an image sequence are stored in the same file. However, some formats (e.g. JPEG) do not support storing more than one image per file and only the first frame in an image sequence will be saved unless the result is saved to separate files. Use <code>+adjoin</code> to force saving multiple frames to multiple numbered files. If <code>+adjoin</code> is used, then the output filename must include a printf style formatting specification for the numeric part of the filename. For example, </p>
<p>&nbsp;<wbr>image%02d.miff </p>
<dt><code>-affine </code><i>&lt;matrix&gt;</i></p>
<dd> drawing transform matrix </p>
<p> This option provides a transform matrix {sx,rx,ry,sy,tx,ty} for use by subsequent <code>-draw</code> or <code>-transform</code> options.</p>
<dt><code>-antialias</code></p>
<dd> remove pixel aliasing </p>
<p> By default antialiasing algorithms are used when drawing objects (e.g. lines) or rendering vector formats (e.g. WMF and Postscript). Use +antialias to disable use of antialiasing algorithms. Reasons to disable antialiasing include avoiding increasing colors in the image, or improving rendering speed.</p>
<dt><code>-append</code></p>
<dd> append a set of images </p>
<p> This option creates a single image where the images in the original set are stacked top-to-bottom. If they are not of the same width, any narrow images will be expanded to fit using the background color. Use <code>+append</code> to stack images left-to-right. The set of images is terminated by the appearance of any option. If the <code>-append</code> option appears after all of the input images, all images are appended.</p>
<dt><i>-asc-cdl &lt;spec&gt;</i></p>
<dd> apply ASC CDL color transform </p>
<p> Applies (&quot;bakes in&quot;) the ASC CDL, which is a format for the exchange of basic primary color grading information between equipment and software from different manufacturers. The format defines the math for three functions: slope, offset and power. Each function uses a number for the red, green, and blue color channels for a total of nine numbers comprising a single color decision. The tenth number (optional) is for chromiance (saturation) as specified by ASC CDL 1.2. </p>
<p> The argument string is comma delimited and is in the following form (but without invervening spaces or line breaks) </p>
<p>&nbsp;<wbr>redslope,redoffset,redpower:<br />
&nbsp;<wbr>greenslope,greenoffset,greenpower:<br />
&nbsp;<wbr>blueslope,blueoffset,bluepower:<br />
&nbsp;<wbr>saturation </p>
<p> with the unity (no change) specification being: </p>
<p>&nbsp;<wbr>&quot;1.0,0.0,1.0:1.0,0.0,1.0:1.0,0.0,1.0:1.0&quot; </p>
<dt><code>-authenticate </code><i>&lt;string&gt;</i></p>
<dd> decrypt image with this password </p>
<p> Use this option to supply a password for decrypting an image or an image sequence, if it is being read from a format such as PDF that supports encryption. Encrypting images being written is not supported.</p>
<dt><code>-auto-orient</code></p>
<dd> orient (rotate) image so it is upright </p>
<p> Adjusts the image orienation so that it is suitable for viewing. Uses the orientation tag obtained from the image file or as supplied by the <code>-orient</code> option.</p>
<dt><code>-average</code></p>
<dd> average a set of images </p>
<p> The set of images is terminated by the appearance of any option. If the <code>-average</code> option appears after all of the input images, all images are averaged.</p>
<dt><code>-backdrop</code></p>
<dd> display the image centered on a backdrop. </p>
<p> This backdrop covers the entire workstation screen and is useful for hiding other X window activity while viewing the image. The color of the backdrop is specified as the foreground color (X11 default is black). Refer to &quot;X Resources&quot;, below, for details.</p>
<dt><code>-background </code><i>&lt;color&gt;</i></p>
<dd> the background color </p>
<p> The color is specified using the format described under the <code>-fill</code> option.</p>
<dt><code>-black-threshold </code><i>red[,green][,blue][,opacity]</i></p>
<dd> pixels below the threshold become black </p>
<p> Use <code>-black-threshold</code> to set pixels with values below the specified threshold to minimum value (black). If only one value is supplied, or the red, green, and blue values are identical, then intensity thresholding is used. If the color threshold values are not identical then channel-based thresholding is used, and color distortion will occur. Specify a negative value (e.g. -1) if you want a channel to be ignored but you do want to threshold a channel later in the list. If a percent (%) symbol is appended, then the values are treated as a percentage of maximum range.</p>
<dt><code>-blue-primary </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> blue chromaticity primary point</p>
<dt><code>-blur </code><i>&lt;radius&gt;{x&lt;sigma&gt;}</i></p>
<dd> blur the image with a Gaussian operator </p>
<p> Blur with the given radius and standard deviation (sigma).</p>
<dt><code>-border </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> surround the image with a border of color </p>
<p> See <code>-geometry</code> for details about the geometry specification.</p>
<dt><code>-bordercolor </code><i>&lt;color&gt;</i></p>
<dd> the border color </p>
<p> The color is specified using the format described under the <code>-fill</code> option.</p>
<dt><code>-borderwidth </code><i>&lt;geometry&gt;</i></p>
<dd> the border width</p>
<dt><code>-box </code><i>&lt;color&gt;</i></p>
<dd> set the color of the annotation bounding box </p>
<p> The color is specified using the format described under the <code>-fill</code> option. </p>
<p> See <code>-draw</code> for further details.</p>
<dt><code>-channel </code><i>&lt;type&gt;</i></p>
<dd> the type of channel </p>
<p> Choose from: <code>Red</code>, <code>Green</code>, <code>Blue</code>, <code>Opacity</code>, <code>Matte</code>, <code>Cyan</code>, <code>Magenta</code>, <code>Yellow</code>, <code>Black</code>, or <code>Gray</code>. </p>
<p> Use this option to extract a particular <i>channel</i> from the image. <code>Opacity</code>, for example, is useful for extracting the opacity values from an image.</p>
<dt><code>-charcoal </code><i>&lt;factor&gt;</i></p>
<dd> simulate a charcoal drawing</p>
<dt><code>-chop </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}</i></p>
<dd> remove pixels from the interior of an image </p>
<p> <i>Width</i> and <i>height</i> give the number of columns and rows to remove, and <i>x</i> and <i>y</i> are offsets that give the location of the leftmost column and topmost row to remove. </p>
<p> The <i>x</i> offset normally specifies the leftmost column to remove. If the <code>-gravity</code> option is present with <i>NorthEast, East,</i> or <i>SouthEast</i> gravity, it gives the distance leftward from the right edge of the image to the rightmost column to remove. Similarly, the <i>y</i> offset normally specifies the topmost row to remove, but if the <code>-gravity</code> option is present with <i>SouthWest, South,</i> or <i>SouthEast</i> gravity, it specifies the distance upward from the bottom edge of the image to the bottom row to remove. </p>
<p> The <code>-chop</code> option removes entire rows and columns, and moves the remaining corner blocks leftward and upward to close the gaps.</p>
<dt><code>-clip</code></p>
<dd> apply the clipping path, if one is present </p>
<p> If a clipping path is present, it will be applied to subsequent operations. </p>
<p> For example, if you type the following command: </p>
<p>&nbsp;<wbr>gm convert -clip -negate cockatoo.tif negated.tif </p>
<p> only the pixels within the clipping path are negated. </p>
<p> The <code>-clip</code> feature requires the XML library. If the XML library is not present, the option is ignored.</p>
<dt><code>-coalesce</code></p>
<dd> merge a sequence of images </p>
<p> Each image N in the sequence after Image 0 is replaced with the image created by flattening images 0 through N. </p>
<p> The set of images is terminated by the appearance of any option. If the <code>-coalesce</code> option appears after all of the input images, all images are coalesced.</p>
<dt><code>-colorize </code><i>&lt;value&gt;</i></p>
<dd> colorize the image with the pen color </p>
<p> Specify the amount of colorization as a percentage. You can apply separate colorization values to the red, green, and blue channels of the image with a colorization value list delimited with slashes (e.g. 0/0/50). </p>
<p> The <code>-colorize</code> option may be used in conjunction with <code>-modulate</code> to produce a nice sepia toned image like: </p>
<p>&nbsp;<wbr>gm convert input.ppm -modulate 115,0,100&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-colorize 7,21,50 output.ppm. </p>
<dt><code>-colormap </code><i>&lt;type&gt;</i></p>
<dd> define the colormap type </p>
<p> Choose between <code>shared</code> or <code>private</code>. </p>
<p> This option only applies when the default X server visual is <i>PseudoColor</i> or <i>GRAYScale</i>. Refer to <code>-visual</code> for more details. By default, a shared colormap is allocated. The image shares colors with other X clients. Some image colors could be approximated, therefore your image may look very different than intended. Choose <code>Private</code> and the image colors appear exactly as they are defined. However, other clients may go <i>technicolor</i> when the image colormap is installed.</p>
<dt><code>-colors </code><i>&lt;value&gt;</i></p>
<dd> preferred number of colors in the image </p>
<p> The actual number of colors in the image may be less than your request, but never more. Note, this is a color reduction option. Images with less unique colors than specified with this option will have any duplicate or unused colors removed. The ordering of an existing color palette may be altered. When converting an image from color to grayscale, convert the image to the gray colorspace before reducing the number of colors since doing so is most efficient. Refer to &lt;a href=&quot;quantize.html&quot;&gt;quantize for more details. </p>
<p> Note, options <code>-dither</code>, <code>-colorspace</code>, and <code>-treedepth</code> affect the color reduction algorithm.</p>
<dt><code>-colorspace </code><i>&lt;value&gt;</i></p>
<dd> the type of colorspace </p>
<p> Choices are: <code>CineonLog</code>, <code>CMYK</code>, <code>GRAY</code>, <code>HSL</code>, <code>HWB</code>, <code>OHTA</code>, <code>RGB</code>, <code>Rec601Luma</code>, <code>Rec709Luma</code>, <code>Rec601YCbCr</code>, <code>Rec709YCbCr</code>, <code>Transparent</code>, <code>XYZ</code>, <code>YCbCr</code>, <code>YIQ</code>, <code>YPbPr</code>, or <code>YUV</code>. </p>
<p> Color reduction, by default, takes place in the RGB color space. Empirical evidence suggests that distances in color spaces such as YUV or YIQ correspond to perceptual color differences more closely than do distances in RGB space. These color spaces may give better results when color reducing an image. Refer to quantize for more details. Two gray colorspaces are supported. The <code>Rec601Luma</code> space is based on the recommendations for legacy NTSC television (ITU-R BT.601-5). The <code>Rec709Luma</code> space is based on the recommendations for HDTV (Rec. ITU-R BT.709-5) and is suitable for use with computer graphics, and for contemporary CRT displays. The <code>GRAY</code> colorspace currently selects the <code>Rec601Luma</code> colorspace by default for backwards compatibly reasons. This default may be re-considered in the future. </p>
<p> Two YCbCr colorspaces are supported. The <code>Rec601YCbCr</code> space is based on the recommendations for legacy NTSC television (ITU-R BT.601-5). The <code>Rec709CbCr</code> space is based on the recommendations for HDTV (Rec. ITU-R BT.709-5) and is suitable for suitable for use with computer graphics, and for contemporary CRT displays. The <code>YCbCr</code> colorspace specification is equivalent to<code>Rec601YCbCr</code>. </p>
<p> The <code>Transparent</code> color space behaves uniquely in that it preserves the matte channel of the image if it exists. </p>
<p> The <code>-colors</code> or <code>-monochrome</code> option, or saving to a file format which requires color reduction, is required for this option to take effect.</p>
<dt><code>-comment </code><i>&lt;string&gt;</i></p>
<dd> annotate an image with a comment </p>
<p> Use this option to assign a specific comment to the image, when writing to an image format that supports comments. You can include the image filename, type, width, height, or other image attribute by embedding special format characters listed under the <code>-format</code> option. The comment is not drawn on the image, but is embedded in the image datastream via a &quot;Comment&quot; tag or similar mechanism. If you want the comment to be visible on the image itself, use the <code>-draw</code> option instead. </p>
<p> For example, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-comment&nbsp;<wbr>&quot;%m:%f&nbsp;<wbr>%wx%h&quot; </p>
<p> produces an image comment of <code>MIFF:bird.miff 512&#215;480</code> for an image titled <code>bird.miff</code> and whose width is 512 and height is 480. </p>
<p> If the first character of <i>string</i> is <i>@</i>, the image comment is read from a file titled by the remaining characters in the string. </p>
<p> If the -comment option appears multiple times, only the last comment is stored. </p>
<p> In PNG images, the comment is stored in a <code>tEXt</code> or <code>zTXt</code> chunk with the keyword &quot;comment&quot;.</p>
<dt><code>-compose </code><i>&lt;operator&gt;</i></p>
<dd> the type of image composition </p>
<p> The description of composition uses abstract terminology in order to allow the the description to be more clear, while avoiding constant values which are specific to a particular build configuration. Each image pixel is represented by red, green, and blue levels (which are equal for a gray pixel). MaxRGB is the maximum integral value which may be stored in the red, green, or blue channels of the image. Each image pixel may also optionally (if the image matte channel is enabled) have an associated level of opacity (ranging from opaque to transparent), which may be used to determine the influence of the pixel color when compositing the pixel with another image pixel. If the image matte channel is disabled, then all pixels in the image are treated as opaque. The color of an <i>opaque</i> pixel is fully visible while the color of a <i>transparent</i> pixel color is entirely absent (pixel color is ignored). </p>
<p> By definition, raster images have a rectangular shape. All image rows are of equal length, and all image columns have the same number of rows. By treating the opacity channel as a visual &quot;mask&quot; the rectangular image may be given a &quot;shape&quot; by treating the opacity channel as a cookie-cutter for the image. Pixels within the shape are opaque, while pixels outside the shape are transparent. Pixels on the boundary of the shape may be between opaque and transparent in order to provide antialiasing (visually smooth edges). The description of the composition operators use this concept of image &quot;shape&quot; in order to make the description of the operators easier to understand. While it is convenient to describe the operators in terms of &quot;shapes&quot; they are by no means limited to mask-style operations since they are based on continuous floating-point mathematics rather than simple boolean operations. </p>
<p> By default, the <i>Over</i> composite operator is used. The following composite operators are available: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Over<br />
&nbsp;<wbr>&nbsp;<wbr>In<br />
&nbsp;<wbr>&nbsp;<wbr>Out<br />
&nbsp;<wbr>&nbsp;<wbr>Atop<br />
&nbsp;<wbr>&nbsp;<wbr>Xor<br />
&nbsp;<wbr>&nbsp;<wbr>Plus<br />
&nbsp;<wbr>&nbsp;<wbr>Minus<br />
&nbsp;<wbr>&nbsp;<wbr>Add<br />
&nbsp;<wbr>&nbsp;<wbr>Subtract<br />
&nbsp;<wbr>&nbsp;<wbr>Difference<br />
&nbsp;<wbr>&nbsp;<wbr>Divide<br />
&nbsp;<wbr>&nbsp;<wbr>Multiply<br />
&nbsp;<wbr>&nbsp;<wbr>Bumpmap<br />
&nbsp;<wbr>&nbsp;<wbr>Copy<br />
&nbsp;<wbr>&nbsp;<wbr>CopyRed<br />
&nbsp;<wbr>&nbsp;<wbr>CopyGreen<br />
&nbsp;<wbr>&nbsp;<wbr>CopyBlue<br />
&nbsp;<wbr>&nbsp;<wbr>CopyOpacity<br />
&nbsp;<wbr>&nbsp;<wbr>CopyCyan<br />
&nbsp;<wbr>&nbsp;<wbr>CopyMagenta<br />
&nbsp;<wbr>&nbsp;<wbr>CopyYellow<br />
&nbsp;<wbr>&nbsp;<wbr>CopyBlack </p>
<p> The behavior of each operator is described below. </p>
<p> <code>Over</code><br />
&nbsp;<wbr> The result will be the union of the two image shapes, with opaque areas of <i>change-image</i> obscuring <i>base-image</i> in the region of overlap. </p>
<p> <code>In</code><br />
&nbsp;<wbr> The result is simply <i>change-image</i> cut by the shape of <i>base-image</i>. None of the image data of <i>base-image</i> will be in the result. </p>
<p> <code>Out</code><br />
&nbsp;<wbr> The resulting image is <i>change-image</i> with the shape of <i>base-image</i> cut out. </p>
<p> <code>Atop</code><br />
&nbsp;<wbr> The result is the same shape as <i>base-image</i>, with <i>change-image</i> obscuring <i>base-image</i> where the image shapes overlap. Note this differs from <code>over</code> because the portion of <i>change-image</i> outside <i>base-image</i>&#8216;s shape does not appear in the result. </p>
<p> <code>Xor</code><br />
&nbsp;<wbr> The result is the image data from both <i>change-image</i> and <i>base-image</i> that is outside the overlap region. The overlap region will be blank. </p>
<p> <code>Plus</code><br />
&nbsp;<wbr> The result is just the sum of the image data. Output values are cropped to MaxRGB (no overflow). This operation is independent of the matte channels. </p>
<p> <code>Minus</code><br />
&nbsp;<wbr> The result of <i>change-image</i> &#8211; <i>base-image</i>, with underflow cropped to zero. The matte channel is ignored (set to opaque, full coverage). </p>
<p> <code>Add</code><br />
&nbsp;<wbr> The result of <i>change-image</i> + <i>base-image</i>, with overflow wrapping around (<i>mod</i> MaxRGB+1). </p>
<p> <code>Subtract</code><br />
&nbsp;<wbr> The result of <i>change-image</i> &#8211; <i>base-image</i>, with underflow wrapping around (<i>mod</i> MaxRGB+1). The <code>add</code> and <code>subtract</code> operators can be used to perform reversible transformations. </p>
<p> <code>Difference</code><br />
&nbsp;<wbr> The result of abs(<i>change-image</i> &#8211; <i>base-image</i>). This is useful for comparing two very similar images. </p>
<p> <code>Divide</code><br />
&nbsp;<wbr> The result of <i>change-image</i> / <i>base-image</i>. This is useful for improving the readability of text on unevenly illuminated photos (by using a gaussian blurred copy of change-image as base-image). </p>
<p> <code>Multiply</code><br />
&nbsp;<wbr> The result of <i>change-image</i> * <i>base-image</i>. This is useful for the creation of drop-shadows. </p>
<p> <code>Bumpmap</code><br />
&nbsp;<wbr> The result <i>base-image</i> shaded by <i>change-image</i>. </p>
<p> <code>Copy</code><br />
&nbsp;<wbr> The resulting image is <i>base-image</i> replaced with <i>change-image</i>. Here the matte information is ignored. </p>
<p> <code>CopyRed</code><br />
&nbsp;<wbr> The resulting image is the red channel in <i>base-image</i> replaced with the red channel in <i>change-image</i>. The other channels are copied untouched. </p>
<p> <code>CopyGreen</code><br />
&nbsp;<wbr> The resulting image is the green channel in <i>base-image</i> replaced with the green channel in <i>change-image</i>. The other channels are copied untouched. </p>
<p> <code>CopyBlue</code><br />
&nbsp;<wbr> The resulting image is the blue channel in <i>base-image</i> replaced with the blue channel in <i>change-image</i>. The other channels are copied untouched. </p>
<p> <code>CopyOpacity</code><br />
&nbsp;<wbr> The resulting image is the opacity channel in <i>base-image</i> replaced with the opacity channel in <i>change-image</i>. The other channels are copied untouched. </p>
<p> <code>CopyCyan</code><br />
&nbsp;<wbr> The resulting image is the cyan channel in <i>base-image</i> replaced with the cyan channel in <i>change-image</i>. The other channels are copied untouched. Use of this operator requires that base-image be in CMYK(A) colorspace. </p>
<p> <code>CopyMagenta</code><br />
&nbsp;<wbr> The resulting image is the magenta channel in <i>base-image</i> replaced with the magenta channel in <i>change-image</i>. The other channels are copied untouched. Use of this operator requires that base-image be in CMYK(A) colorspace. </p>
<p> <code>CopyYellow</code><br />
&nbsp;<wbr> The resulting image is the yellow channel in <i>base-image</i> replaced with the yellow channel in <i>change-image</i>. The other channels are copied untouched. Use of this operator requires that base-image be in CMYK(A) colorspace. </p>
<p> <code>CopyBlack</code><br />
&nbsp;<wbr> The resulting image is the black channel in <i>base-image</i> replaced with the black channel in <i>change-image</i>. The other channels are copied untouched. Use of this operator requires that base-image be in CMYK(A) colorspace. If change-image is not in CMYK space, then the change-image pixel intensities are used. </p>
<dt><code>-compress </code><i>&lt;type&gt;</i></p>
<dd> the type of image compression </p>
<p> Choices are: <i>None</i>, <i>BZip</i>, <i>Fax</i>, <i>Group4</i>, <i>JPEG</i>, <i>Lossless</i>, <i>LZW</i>, <i>RLE</i>, <i>Zip</i>, or <i>LZMA</i>. </p>
<p> Specify <code>+compress</code> to store the binary image in an uncompressed format. The default is the compression type of the specified image file. </p>
<p> <i>&quot;Lossless&quot;</i> refers to lossless JPEG, which is only available if the JPEG library has been patched to support it. Use of lossless JPEG is generally not recommended. </p>
<p> Use the <code>-quality</code> option to set the compression level to be used by JPEG, PNG, MIFF, and MPEG encoders. Use the <code>-sampling-factor</code> option to set the sampling factor to be used by the DPX, JPEG, MPEG, and YUV encoders for downsampling the chroma channels.</p>
<dt><code>-contrast</code></p>
<dd> enhance or reduce the image contrast </p>
<p> This option enhances the intensity differences between the lighter and darker elements of the image. Use <code>-contrast</code> to enhance the image or <code>+contrast</code> to reduce the image contrast. </p>
<p> For a more pronounced effect you can repeat the option: </p>
<p>&nbsp;<wbr>gm convert rose: -contrast -contrast rose_c2.png </p>
<dt><code>-convolve </code><i>&lt;kernel&gt;</i></p>
<dd> convolve image with the specified convolution kernel </p>
<p> The kernel is specified as a comma-separated list of floating point values, ordered left-to right, starting with the top row. The order of the kernel is determined by the square root of the number of entries. Presently only square kernels are supported.</p>
<dt><code>-create-directories</code></p>
<dd> create output directory if required </p>
<p> Use this option with <code>-output-directory</code> if the input paths contain subdirectories and it is desired to create similar subdirectories in the output directory. Without this option, <code>mogrify</code> will fail if the required output directory does not exist.</p>
<dt><code>-crop </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}</i></p>
<dd> preferred size and location of the cropped image </p>
<p> See <code>-geometry</code> for details about the geometry specification. </p>
<p> The width and height give the size of the image that remains after cropping, and <i>x</i> and <i>y</i> are offsets that give the location of the top left corner of the cropped image with respect to the original image. To specify the amount to be removed, use <code>-shave</code> instead. </p>
<p> If the <i>x</i> and <i>y</i> offsets are present, a single image is generated, consisting of the pixels from the cropping region. The offsets specify the location of the upper left corner of the cropping region measured downward and rightward with respect to the upper left corner of the image. If the <code>-gravity</code> option is present with <i>NorthEast, East,</i> or <i>SouthEast</i> gravity, it gives the distance leftward from the right edge of the image to the right edge of the cropping region. Similarly, if the <code>-gravity</code> option is present with <i>SouthWest, South,</i> or <i>SouthEast</i> gravity, the distance is measured upward between the bottom edges. </p>
<p> If the <i>x</i> and <i>y</i> offsets are omitted, a set of tiles of the specified geometry, covering the entire input image, is generated. The rightmost tiles and the bottom tiles are smaller if the specified geometry extends beyond the dimensions of the input image.</p>
<dt><code>-cycle </code><i>&lt;amount&gt;</i></p>
<dd> displace image colormap by amount </p>
<p> <i>Amount</i> defines the number of positions each colormap entry isshifted. </p>
<dt><code>-debug </code><i>&lt;events&gt;</i></p>
<dd> enable debug printout </p>
<p> The events parameter specifies which events are to be logged. It can be either None, All, or a comma-separated list consisting of one or more of the following domains: Annotate, Blob, Cache, Coder, Configure, Deprecate, Error, Exception, Locale, Render,Resource, TemporaryFile, Transform, Warning, X11, or User. For example, to log cache and blob events, use </p>
<p>&nbsp;<wbr>gm convert -debug&nbsp;<wbr>&quot;Cache,Blob&quot;&nbsp;<wbr>rose: rose.png </p>
<p> The &quot;User&quot; domain is normally empty, but developers can log &quot;User&quot; events in their private copy of GraphicsMagick. </p>
<p> Use the <code>-log</code> option to specify the format for debugging output. </p>
<p> Use <code>+debug</code> to turn off all logging. </p>
<p> An alternative to using <code>-debug</code> is to use the <code>MAGICK_DEBUG</code> environment variable. The allowed values for the <code>MAGICK_DEBUG</code> environment variable are the same as for the <code>-debug</code> option.</p>
<dt><code>-deconstruct</code></p>
<dd> break down an image sequence into constituent parts </p>
<p> This option compares each image with the next in a sequence and returns the maximum bounding region of any pixel differences it discovers. This method can undo a coalesced sequence returned by the <code>-coalesce</code> option, and is useful for removing redundant information from a GIF or MNG animation. </p>
<p> The sequence of images is terminated by the appearance of any option. If the <code>-deconstruct</code> option appears after all of the input images, all images are deconstructed.</p>
<dt><code>-define </code><i>&lt;key&gt;{=&lt;value&gt;},&#8230;</i></p>
<dd> add coder/decoder specific options This option creates one or more definitions for coders and decoders to use while reading and writing image data. Definitions may be passed to coders and decoders to control options that are specific to certain image formats. If <i>value</i> is missing for a definition, an empty-valued definition of a flag will be created with that name. This is used to control on/off options. Use +define &lt;key&gt;,&#8230; to remove definitions previously created. Use +define &quot;*&quot; to remove all existing definitions. </p>
<p> The following definitions may be created: </p>
<p> <code>cineon:colorspace={rgb|cineonlog}</code><br />
&nbsp;<wbr> Use the cineon:colorspace option when reading a Cineon file to specify the colorspace the Cineon file uses. This overrides the colorspace type implied by the DPX header (if any). </p>
<p> <code>dpx:bits-per-sample=&lt;value&gt;</code><br />
&nbsp;<wbr> If the dpx:bits-per-sample key is defined, GraphicsMagick will write DPX images with the specified bits per sample, overriding any existing depth value. If this option is not specified, then the value is based on the existing image depth value from the original image file. The DPX standard supports bits per sample values of 1, 8, 10, 12, and 16. Many DPX readers demand a sample size of 10 bits with type A padding (see below). </p>
<p> <code>dpx:colorspace={rgb|cineonlog}</code><br />
&nbsp;<wbr> Use the dpx:colorspace option when reading a DPX file to specify the colorspace the DPX file uses. This overrides the colorspace type implied by the DPX header (if any). </p>
<p> <code>dpx:packing-method={packed|a|b|lsbpad|msbpad}</code><br />
&nbsp;<wbr> DPX samples are output within 32-bit words. They may be tightly packed end-to-end within the words (&quot;packed&quot;), padded with null bits to the right of the sample (&quot;a&quot; or &quot;lsbpad), or padded with null bits to the left of the sample (&quot;b&quot; or &quot;msbpad&quot;). This option only has an effect for sample sizes of 10 or 12 bits. If samples are not packed, the DPX standard recommends type A padding. Many DPX readers demand a sample size of 10 bits with type A padding. </p>
<p> <code>dpx:pixel-endian={lsb|msb}</code><br />
&nbsp;<wbr> Allows the user to specify the endian order of the pixels when reading or writing the DPX files. Sometimes this is useful if the file is (or must be) written incorrectly so that the file header and the pixels use different endianness. </p>
<p> <code>dpx:swap-samples={true|false}</code><br />
&nbsp;<wbr> GraphicsMagick strives to adhere to the DPX standard but certain aspects of the standard can be quite confusing. As a result, some 10-bit DPX files have Red and Blue interchanged, or Cb and Cr interchanged due to an different interpretation of the standard, or getting the wires crossed. The swap-samples option may be supplied when reading or writing in order to read or write using the necessary sample order. </p>
<p> <code>jp2:rate=&lt;value&gt;</code><br />
&nbsp;<wbr> Specify the compression factor to use while writing JPEG-2000 files. The compression factor is the reciprocal of the compression ratio. The valid range is 0.0 to 1.0, with 1.0 indicating lossless compression. If defined, this value overrides the -quality setting. The default quality setting of 75 results in a rate value of 0.06641. </p>
<p> <code>jpeg:block-smoothing={true|false}</code><br />
&nbsp;<wbr> Enables or disables block smoothing when reading a JPEG file (default enabled). </p>
<p> <code>jpeg:dct-method=&lt;value&gt;</code><br />
&nbsp;<wbr> Selects the IJG JPEG library DCT implementation to use. The encoding implementations vary in speed and encoding error. The available choices for <code>value</code> are <code>islow</code>, <code>ifast</code>, <code>float</code>, <code>default</code> and <code>fastest</code>. Note that <code>fastest</code> might not necessarily be fastest on your CPU, depending on the choices made when the JPEG library was built and how your CPU behaves. </p>
<p> <code>jpeg:fancy-upsampling={true|false}</code><br />
&nbsp;<wbr> Enables or disables fancy upsampling when reading a JPEG file (default enabled). </p>
<p> <code>jpeg:optimize-coding={true|false}</code><br />
&nbsp;<wbr> </p>
<p> Selects if huffman encoding should be used. Huffman encoding is enabled by default, but may be disabled for very large images since it encoding requires that the entire image be buffered in memory. Huffman encoding produces smaller JPEG files at the expense of added compression time and memory consumption. </p>
<p> <code>jpeg:preserve-settings</code><br />
&nbsp;<wbr> If the jpeg:preserve-settings flag is defined, the JPEG encoder will use the same &quot;quality&quot; and &quot;sampling-factor&quot; settings that were found in the input file, if the input was in JPEG format. These settings are also preserved if the input is a JPEG file and the output is a JNG file. If the colorspace of the output file differs from that of the input file, the quality setting is preserved but the sampling-factors are not. </p>
<p> <code>pcl:fit-to-page</code><br />
&nbsp;<wbr> If the pcl:fit-to-page flag is defined, then the printer is requested to scale the image to fit the page size (width and/or height). <code>pdf:use-cropbox={true|false}</code><br />
&nbsp;<wbr> If the pdf:use-cropbox flag is set to <code>true</code>, then Ghostscript is requested to apply the PDF crop box. </p>
<p> <code>pdf:stop-on-error={true|false}</code><br />
&nbsp;<wbr> If the pdf:stop-on-error flag is set to <code>true</code>, then Ghostscript is requested to stop processing the PDF when the first error is encountered. Otherwise it will attempt to process all requested pages. </p>
<p> <code>ps:imagemask</code><br />
&nbsp;<wbr> If the ps:imagemask flag is defined, the PS3 and EPS3 coders will create Postscript files that render bilevel images with the Postscript imagemask operator instead of the image operator. </p>
<p> <code>tiff:alpha={unspecified|associated|unassociated}</code><br />
&nbsp;<wbr> Specify the TIFF alpha channel type when reading or writing TIFF files, overriding the normal value. The default alpha channel type for new files is unspecified alpha. Existing alpha settings are preserved when converting from one TIFF file to another. When a TIFF file uses associated alpha, the image pixels are pre-multiplied (i.e. altered) with the alpha channel. Files with &quot;associated&quot; alpha appear as if they were alpha composited on a black background when the matte channel is disabled. If the unassociated alpha type is selected, then the alpha channel is saved without altering the pixels. Photoshop recognizes associated alpha as transparency information, if the file is saved with unassociated alpha, the alpha information is loaded as an independent channel. Note that for many years, ImageMagick and GraphicsMagick marked TIFF files as using associated alpha, without properly pre-multiplying the pixels. </p>
<p> <code>tiff:fill-order={msb2lsb|lsb2msb}</code><br />
&nbsp;<wbr> If the tiff:fill-order key is defined, GraphicsMagick will use it to determine the bit fill order used while writing TIFF files. The normal default is &quot;msb2lsb&quot;, which matches the native bit order of all modern CPUs. The only exception to this is when Group3 or Group4 FAX compression is requested since FAX machines send data in bit-reversed order and therefore RFC 2301 recommends using reverse order. </p>
<p> <code>tiff:group-three-options=&lt;value&gt;</code><br />
&nbsp;<wbr> If the tiff:group-three-options key is defined, GraphicsMagick will use it to set the group3 options tag when writing group3-compressed TIFF. Please see the TIFF specification for the usage of this tag. The default value is 4. </p>
<p> <code>tiff:ignore-tags=&lt;tags&gt;</code><br />
&nbsp;<wbr> If the tiff:ignore-tags key is defined, then it is used as a list of comma-delimited integer TIFF tag values to ignore while reading the TIFF file. This is useful in order to be able to read files which which otherwise fail to read due to problems with TIFF tags. Note that some TIFF tags are required in order to be able to read the image data at all. </p>
<p> <code>tiff:report-warnings={false|true}</code><br />
&nbsp;<wbr> If the tiff:report-warnings key is defined and set to <code>true</code>, then TIFF warnings are reported as a warning exception rather than as a coder log message. Such warnings are reported after the image has been read or written. Most TIFF warnings are benign but sometimes they may help deduce problems with the TIFF file, or help detect that the TIFF file requires a special application to read successfully due to the use of proprietary or specialized extensions. </p>
<p> <code>tiff:sample-format={unsigned|ieeefp}</code><br />
&nbsp;<wbr> If the tiff:sample-format key is defined, GraphicsMagick will use it to determine the sample format used while writing TIFF files. The default is &quot;unsigned&quot;. Specify &quot;ieeefp&quot; in order to write floating-point TIFF files with float (32-bit) or double (64-bit) values. Use the tiff:bits-per-sample define to determine the type of floating-point value to use. </p>
<p> <code>tiff:max-sample-value=&lt;value&gt;</code><br />
&nbsp;<wbr> If the tiff:max-sample-value key is defined, GraphicsMagick will use the assigned value as the maximum floating point value while reading or writing IEEE floating point TIFFs. Otherwise the maximum value is 1.0 or the value obtained from the file&#8217;s SMaxSampleValue tag (if present). The floating point data is currently not scanned in advance to determine a best maximum sample value so if the range is not 1.0, or the SMaxSampleValue tag is not present, it may be necessary to (intelligently) use this parameter to properly read a file. </p>
<p> <code>tiff:min-sample-value=&lt;value&gt;</code><br />
&nbsp;<wbr> If the tiff:min-sample-value key is defined, GraphicsMagick will use the assigned value as the minimum floating point value while reading or writing IEEE floating point TIFFs. Otherwise the minimum value is 0.0 or the value obtained from the file&#8217;s SMinSampleValue tag (if present). </p>
<p> <code>tiff:bits-per-sample=&lt;value&gt;</code><br />
&nbsp;<wbr> If the tiff:bits-per-sample key is defined, GraphicsMagick will write images with the specified bits per sample, overriding any existing depth value. Value may be any in the range of 1 to 32, or 64 when the default &#8216;unsigned&#8217; format is written, or 16/32/24/64 if IEEEFP format is written. Please note that the baseline TIFF 6.0 specification only requires readers to handle certain powers of two, and the values to be handled depend on the nature of the image (e.g. colormapped, grayscale, RGB, CMYK). </p>
<p> <code>tiff:samples-per-pixel=&lt;value&gt;</code><br />
&nbsp;<wbr> If the tiff:samples-per-pixel key is defined to a value, the TIFF coder will write TIFF images with the defined samples per pixel, overriding any value stored in the image. This option should not normally be used. </p>
<p> <code>tiff:rows-per-strip=&lt;value&gt;</code><br />
&nbsp;<wbr> Allows the user to specify the number of rows per TIFF strip. Rounded up to a multiple of 16 when using JPEG compression. Ignored when using tiles. </p>
<p> <code>tiff:strip-per-page=true</code><br />
&nbsp;<wbr> Requests that the image is written in a single TIFF strip. This is normally the default when group3 or group4 compression is requested within reasonable limits. Requesting a single strip for large images may result in failure due to resource consumption in the writer or reader. </p>
<p> <code>tiff:tile</code><br />
&nbsp;<wbr> Enable writing tiled TIFF (rather than stripped) using the default tile size. Tiled TIFF organizes the image as an array of smaller images (tiles) in order to enable random access. </p>
<p> <code>tiff:tile-geometry=&lt;width&gt;x&lt;height&gt;</code><br />
&nbsp;<wbr> Specify the tile size to use while writing tiled TIFF. Width and height should be a multiple of 16. If the value is not a multiple of 16, then it will be rounded down. Enables tiled TIFF if it has not already been enabled. GraphicsMagick does not use tiled storage internally so tiles need to be converted back and forth from the internal scanline-oriented storage to tile-oriented storage. Testing with typical RGB images shows that useful square tile size values range from 128&#215;128 to 1024&#215;1024. Large images which require using a disk-based pixel cache benefit from large tile sizes while images which fit in memory work well with smaller tile sizes. </p>
<p> <code>tiff:tile-width=&lt;width&gt;</code><br />
&nbsp;<wbr> Specify the tile width to use while writing tiled TIFF. The tile height is then defaulted to an appropriate size. Width should be a multiple of 16. If the value is not a multiple of 16, then it will be rounded down. Enables tiled TIFF if it has not already been enabled. </p>
<p> <code>tiff:tile-height=&lt;height&gt;</code><br />
&nbsp;<wbr> Specify the tile height to use while writing tiled TIFF. The tile width is then defaulted to an appropriate size. Height should be a multiple of 16. If the value is not a multiple of 16, then it will be rounded down. Enables tiled TIFF if it has not already been enabled. </p>
<p> <code>webp:lossless={true|false}</code><br />
&nbsp;<wbr> Enable lossless encoding. </p>
<p> <code>webp:method={0-6}</code><br />
&nbsp;<wbr> Quality/speed trade-off. </p>
<p> <code>webp:image-hint={default,graph,photo,picture}</code><br />
&nbsp;<wbr> Hint for image type. </p>
<p> <code>webp:target-size=&lt;integer&gt;</code><br />
&nbsp;<wbr> Target size in bytes. </p>
<p> <code>webp:target-psnr=&lt;float&gt;</code><br />
&nbsp;<wbr> Minimal distortion to try to achieve. </p>
<p> <code>webp:segments={1-4}</code><br />
&nbsp;<wbr> Maximum number of segments to use. </p>
<p> <code>webp:sns-strength={0-100}</code><br />
&nbsp;<wbr> Spatial Noise Shaping. </p>
<p> <code>webp:filter-strength={0-100}</code><br />
&nbsp;<wbr> Filter strength. </p>
<p> <code>webp:filter-sharpness={0-7}</code><br />
&nbsp;<wbr> Filter sharpness. </p>
<p> <code>webp:filter-type={0,1}</code><br />
&nbsp;<wbr> Filtering type. 0 = simple, 1 = strong (only used if filter-strength &gt; 0 or autofilter is enabled). </p>
<p> <code>webp:auto-filter={true|false}</code><br />
&nbsp;<wbr> Auto adjust filter&#8217;s strength. </p>
<p> <code>webp:alpha-compression=&lt;integer&gt;</code><br />
&nbsp;<wbr> Algorithm for encoding the alpha plane (0 = none, 1 = compressed with WebP lossless). Default is 1. </p>
<p> <code>webp:alpha-filtering=&lt;integer&gt;</code><br />
&nbsp;<wbr> Predictive filtering method for alpha plane. 0: none, 1: fast, 2: best. Default is 1. </p>
<p> <code>webp:alpha-quality={0-100}</code><br />
&nbsp;<wbr> Between 0 (smallest size) and 100 (lossless). Default is 100. </p>
<p> <code>webp:pass=[1..10]</code><br />
&nbsp;<wbr> Number of entropy-analysis passes. </p>
<p> <code>webp:show-compressed={true|false}</code><br />
&nbsp;<wbr> Export the compressed picture back. In-loop filtering is not applied. </p>
<p> <code>webp:preprocessing=[0,1,2]</code><br />
&nbsp;<wbr> 0=none, 1=segment-smooth, 2=pseudo-random dithering </p>
<p> <code>webp:partitions=[0-3]</code><br />
&nbsp;<wbr> log2(number of token partitions) in [0..3]. Default is 0 for easier progressive decoding. </p>
<p> <code>webp:partition-limit={0-100}</code><br />
&nbsp;<wbr> Quality degradation allowed to fit the 512k limit on prediction modes coding (0: no degradation, 100: maximum possible degradation). </p>
<p> <code>webp:emulate-jpeg-size={true|false}</code><br />
&nbsp;<wbr> If true, compression parameters will be remapped to better match the expected output size from JPEG compression. Generally, the output size will be similar but the degradation will be lower. </p>
<p> <code>webp:thread-level=&lt;integer&gt;</code><br />
&nbsp;<wbr> If non-zero, try and use multi-threaded encoding. </p>
<p> <code>webp:low-memory={true|false}</code><br />
&nbsp;<wbr> If set, reduce memory usage (but increase CPU use) </p>
<p> For example, to create a postscript file that will render only the black pixels of a bilevel image, use: </p>
<p>&nbsp;<wbr>gm convert bilevel.tif -define ps:imagemask eps3:stencil.ps </p>
<dt><code>-delay </code><i>&lt;1/100ths of a second&gt;</i></p>
<dd> display the next image after pausing </p>
<p> This option is useful for regulating the animation of image sequences <i>Delay/100</i> seconds must expire before the display of the next image. The default is no delay between each showing of the image sequence. The maximum delay is 65535. </p>
<p> You can specify a delay range (e.g. <i>-delay 10-500</i>) which sets the minimum and maximum delay.</p>
<dt><code>-density </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> horizontal and vertical resolution in pixels of the image This option specifies the image resolution to store while encoding a raster image or the canvas resolution while rendering (reading) vector formats such as Postscript, PDF, WMF, and SVG into a raster image. Image resolution provides the unit of measure to apply when rendering to an output device or raster image. The default unit of measure is in dots per inch (DPI). The <code>-units</code> option may be used to select dots per centimeter instead.<br />
&nbsp;<wbr>The default resolution is 72 dots per inch, which is equivalent to one point per pixel (Macintosh and Postscript standard). Computer screens are normally 72 or 96 dots per inch while printers typically support 150, 300, 600, or 1200 dots per inch. To determine the resolution of your display, use a ruler to measure the width of your screen in inches, and divide by the number of horizontal pixels (1024 on a 1024&#215;768 display). If the file format supports it, this option may be used to update the stored image resolution. Note that Photoshop stores and obtains image resolution from a proprietary embedded profile. If this profile is not stripped from the image, then Photoshop will continue to treat the image using its former resolution, ignoring the image resolution specified in the standard file header. The density option is an attribute and does not alter the underlying raster image. It may be used to adjust the rendered size for desktop publishing purposes by adjusting the scale applied to the pixels. To resize the image so that it is the same size at a different resolution, use the <code>-resample</code> option.</p>
<dt><code>-depth </code><i>&lt;value&gt;</i></p>
<dd> depth of the image </p>
<p> This is the number of bits of color to preserve in the image. Any value between 1 and <code>QuantumDepth</code> (build option) may be specified, although 8 or 16 are the most common values. Use this option to specify the depth of raw images whose depth is unknown such as GRAY, RGB, or CMYK, or to change the depth of any image after it has been read. The depth option is applied to the pixels immediately so it may be used as a form of simple compression by discarding the least significant bits. Reducing the depth in advance may speed up color quantization, and help create smaller file sizes when using a compression algorithm like LZW or ZIP.</p>
<dt><code>-descend</code></p>
<dd> obtain image by descending window hierarchy</p>
<dt><code>-despeckle</code></p>
<dd> reduce the speckles within an image</p>
<dt><code>-displace </code><i>&lt;horizontal scale&gt;x&lt;vertical scale&gt;</i></p>
<dd> shift image pixels as defined by a displacement map </p>
<p> With this option, <i>composite image</i> is used as a displacement map. Black, within the displacement map, is a maximum positive displacement. White is a maximum negative displacement and middle gray is neutral. The displacement is scaled to determine the pixel shift. By default, the displacement applies in both the horizontal and vertical directions. However, if you specify <i>mask</i>, <i>composite image</i> is the horizontal X displacement and <i>mask</i> the vertical Y displacement.</p>
<dt><code>-display </code><i>&lt;host:display[.screen]&gt;</i></p>
<dd> specifies the X server to contact </p>
<p> This option is used with convert for obtaining image or font from this X server. See <i><a href="/docs/linux/man/1-x/">X</a>(1)</i>.</p>
<dt><code>-dispose </code><i>&lt;method&gt;</i></p>
<dd> GIF disposal method </p>
<p> The Disposal Method indicates the way in which the graphic is to be treated after being displayed. </p>
<p> Here are the valid methods: </p>
<p>&nbsp;<wbr>Undefined&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>No disposal specified.<br />
&nbsp;<wbr>None&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Do not dispose between frames.<br />
&nbsp;<wbr>Background&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Overwrite the image area with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the background color.<br />
&nbsp;<wbr>Previous&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Overwrite the image area with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>what was there prior to rendering<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the image. </p>
<dt><code>-dissolve </code><i>&lt;percent&gt;</i></p>
<dd> dissolve an image into another by the given percent </p>
<p> The opacity of the composite image is multiplied by the given percent, then it is composited over the main image.</p>
<dt><code>-dither</code></p>
<dd> apply Floyd/Steinberg error diffusion to the image </p>
<p> The basic strategy of dithering is to trade intensity resolution for spatial resolution by averaging the intensities of several neighboring pixels. Images which suffer from severe contouring when reducing colors can be improved with this option. </p>
<p> The <code>-colors</code> or <code>-monochrome</code> option is required for this option to take effect. </p>
<p> Use <code>+dither</code> to turn off dithering and to render PostScript without text or graphic aliasing. Disabling dithering often (but not always) leads to decreased processing time.</p>
<dt><code>-draw </code><i>&lt;string&gt;</i></p>
<dd> annotate an image with one or more graphic primitives </p>
<p> Use this option to annotate an image with one or more graphic primitives. The primitives include shapes, text, transformations, and pixel operations. The shape primitives are </p>
<p>&nbsp;<wbr>&nbsp;<wbr>point&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>x,y<br />
&nbsp;<wbr>&nbsp;<wbr>line&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>x0,y0 x1,y1<br />
&nbsp;<wbr>&nbsp;<wbr>rectangle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>x0,y0 x1,y1<br />
&nbsp;<wbr>&nbsp;<wbr>roundRectangle&nbsp;<wbr>&nbsp;<wbr>x0,y0 x1,y1 wc,hc<br />
&nbsp;<wbr>&nbsp;<wbr>arc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>x0,y0 x1,y1 a0,a1<br />
&nbsp;<wbr>&nbsp;<wbr>ellipse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>x0,y0 rx,ry a0,a1<br />
&nbsp;<wbr>&nbsp;<wbr>circle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>x0,y0 x1,y1<br />
&nbsp;<wbr>&nbsp;<wbr>polyline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>x0,y0&nbsp;<wbr>&nbsp;<wbr>&#8230;&nbsp;<wbr>&nbsp;<wbr>xn,yn<br />
&nbsp;<wbr>&nbsp;<wbr>polygon&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>x0,y0&nbsp;<wbr>&nbsp;<wbr>&#8230;&nbsp;<wbr>&nbsp;<wbr>xn,yn<br />
&nbsp;<wbr>&nbsp;<wbr>Bezier&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>x0,y0&nbsp;<wbr>&nbsp;<wbr>&#8230;&nbsp;<wbr>&nbsp;<wbr>xn,yn<br />
&nbsp;<wbr>&nbsp;<wbr>path&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>path specification<br />
&nbsp;<wbr>&nbsp;<wbr>image&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>operator x0,y0 w,h filename </p>
<p> The text primitive is </p>
<p>&nbsp;<wbr>&nbsp;<wbr>text&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>x0,y0 string </p>
<p> The text gravity primitive is </p>
<p>&nbsp;<wbr>&nbsp;<wbr>gravity&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NorthWest, North, NorthEast, West, Center,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>East, SouthWest, South, or SouthEast </p>
<p> The text gravity primitive only affects the placement of text and does not interact with the other primitives. It is equivalent to using the <code>-gravity</code> commandline option, except that it is limited in scope to the <code>-draw</code> option in which it appears. </p>
<p> The transformation primitives are </p>
<p>&nbsp;<wbr>&nbsp;<wbr>rotate&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>degrees<br />
&nbsp;<wbr>&nbsp;<wbr>translate&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>dx,dy<br />
&nbsp;<wbr>&nbsp;<wbr>scale&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sx,sy<br />
&nbsp;<wbr>&nbsp;<wbr>skewX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>degrees<br />
&nbsp;<wbr>&nbsp;<wbr>skewY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>degrees </p>
<p> The pixel operation primitives are </p>
<p>&nbsp;<wbr>&nbsp;<wbr>color&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>x0,y0 method<br />
&nbsp;<wbr>&nbsp;<wbr>matte&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>x0,y0 method </p>
<p> The shape primitives are drawn in the color specified in the preceding <code>-stroke</code> option. Except for the <code>line</code> and <code>point</code> primitives, they are filled with the color specified in the preceding <code>-fill</code> option. For unfilled shapes, use -fill none. </p>
<p> <code>Point</code> requires a single coordinate. </p>
<p> <code>Line</code> requires a start and end coordinate. </p>
<p> <code>Rectangle</code> expects an upper left and lower right coordinate. </p>
<p> <code>RoundRectangle</code> has the upper left and lower right coordinates and the width and height of the corners. </p>
<p> <code>Circle</code> has a center coordinate and a coordinate for the outer edge. </p>
<p> Use <code>Arc</code> to inscribe an elliptical arc within a rectangle. Arcs require a start and end point as well as the degree of rotation (e.g. 130,30 200,100 45,90). </p>
<p> Use <code>Ellipse</code> to draw a partial ellipse centered at the given point with the x-axis and y-axis radius and start and end of arc in degrees (e.g. 100,100 100,150 0,360). </p>
<p> Finally, <code>polyline</code> and <code>polygon</code> require three or more coordinates to define its boundaries. Coordinates are integers separated by an optional comma. For example, to define a circle centered at 100,100 that extends to 150,150 use: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-draw&nbsp;<wbr>&#8216;circle 100,100 150,150&#8217; </p>
<p> <code>Paths</code> (See Paths) represent an outline of an object which is defined in terms of moveto (set a new current point), lineto (draw a straight line), curveto (draw a curve using a cubic Bezier), arc (elliptical or circular arc) and closepath (close the current shape by drawing a line to the last moveto) elements. Compound paths (i.e., a path with subpaths, each consisting of a single moveto followed by one or more line or curve operations) are possible to allow effects such as &quot;donut holes&quot; in objects. </p>
<p> Use <code>image</code> to composite an image with another image. Follow the image keyword with the composite operator, image location, image size, and filename: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-draw&nbsp;<wbr>&#8216;image Over 100,100 225,225 image.jpg&#8217; </p>
<p> You can use 0,0 for the image size, which means to use the actual dimensions found in the image header. Otherwise, it will be scaled to the given dimensions. See <code>-compose</code> for a description of the composite operators. </p>
<p> Use <code>text</code> to annotate an image with text. Follow the text coordinates with a string. If the string has embedded spaces, enclose it in single or double quotes. Optionally you can include the image filename, type, width, height, or other image attribute by embedding special format character. See <code>-comment</code> for details. </p>
<p> For example, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-draw&nbsp;<wbr>&#8216;text 100,100&nbsp;<wbr>&quot;%m:%f&nbsp;<wbr>%wx%h&quot;&#8217; </p>
<p> annotates the image with MIFF:bird.miff 512&#215;480 for an image titled bird.miff and whose width is 512 and height is 480. </p>
<p> If the first character of <i>string</i> is <i>@</i>, the text is read from a file titled by the remaining characters in the string. </p>
<p> <code>Rotate</code> rotates subsequent shape primitives and text primitives about the origin of the main image. If the <code>-region</code> option precedes the <code>-draw</code> option, the origin for transformations is the upper left corner of the region. </p>
<p> <code>Translate</code> translates them. </p>
<p> <code>Scale</code> scales them. </p>
<p> <code>SkewX</code> and <code>SkewY</code> skew them with respect to the origin of the main image or the region. </p>
<p> The transformations modify the current affine matrix, which is initialized from the initial affine matrix defined by the <code>-affine</code> option. Transformations are cumulative within the <code>-draw</code> option. The initial affine matrix is not affected; that matrix is only changed by the appearance of another <code>-affine</code> option. If another <code>-draw</code> option appears, the current affine matrix is reinitialized from the initial affine matrix. </p>
<p> Use <code>color</code> to change the color of a pixel to the fill color (see <code>-fill</code>). Follow the pixel coordinate with a method: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>point<br />
&nbsp;<wbr>&nbsp;<wbr>replace<br />
&nbsp;<wbr>&nbsp;<wbr>floodfill<br />
&nbsp;<wbr>&nbsp;<wbr>filltoborder<br />
&nbsp;<wbr>&nbsp;<wbr>reset </p>
<p> Consider the target pixel as that specified by your coordinate. The <code>point</code> method recolors the target pixel. The <code>replace</code> method recolors any pixel that matches the color of the target pixel. <code>Floodfill</code> recolors any pixel that matches the color of the target pixel and is a neighbor, whereas <code>filltoborder</code> recolors any neighbor pixel that is not the border color. Finally, <code>reset</code> recolors all pixels. </p>
<p> Use <code>matte</code> to the change the pixel matte value to transparent. Follow the pixel coordinate with a method (see the <code>color</code> primitive for a description of methods). The <code>point</code> method changes the matte value of the target pixel. The <code>replace</code> method changes the matte value of any pixel that matches the color of the target pixel. <code>Floodfill</code> changes the matte value of any pixel that matches the color of the target pixel and is a neighbor, whereas <code>filltoborder</code> changes the matte value of any neighbor pixel that is not the border color (<code>-bordercolor</code>). Finally <code>reset</code> changes the matte value of all pixels. </p>
<p> You can set the primitive color, font, and font bounding box color with <code>-fill</code>, <code>-font</code>, and <code>-box</code> respectively. Options are processed in command line order so be sure to use these options <i>before</i> the <code>-draw</code> option.</p>
<dt><code>-edge </code><i>&lt;radius&gt;</i></p>
<dd> detect edges within an image</p>
<dt><code>-emboss </code><i>&lt;radius&gt;</i></p>
<dd> emboss an image</p>
<dt><code>-encoding </code><i>&lt;type&gt;</i></p>
<dd> specify the text encoding </p>
<p> Choose from <i>AdobeCustom, AdobeExpert, AdobeStandard, AppleRoman, BIG5, GB2312, Latin 2, None, SJIScode, Symbol, Unicode, Wansung.</i></p>
<dt><code>-endian </code><i>&lt;type&gt;</i></p>
<dd> specify endianness (MSB, LSB, or Native) of image </p>
<p> <i>MSB</i> indicates big-endian (e.g. SPARC, Motorola 68K) while <i>LSB</i> indicates little-endian (e.g. Intel &#8216;x86, VAX) byte ordering. <i>Native</i> indicates to use the normal ordering for the current CPU. This option currently only influences the CMYK, DPX, GRAY, RGB, and TIFF, formats. </p>
<p> Use <code>+endian</code> to revert to unspecified endianness.</p>
<dt><code>-enhance</code></p>
<dd> apply a digital filter to enhance a noisy image</p>
<dt><code>-equalize</code></p>
<dd> perform histogram equalization to the image</p>
<dt><code>-extent </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;</i></p>
<dd> composite image on background color canvas image </p>
<p> This option composites the image on a new background color (<code>-background</code>) canvas image of size &lt;width&gt;x&lt;height&gt;. The existing image content is composited at the position specified by geometry x and y offset and/or desired gravity (<code>-gravity</code>) using the current image compose (<code>-compose</code>) method. Image content which falls outside the bounds of the new image dimensions is discarded. </p>
<p> For example, this command creates a thumbnail of an image, and centers it on a red color backdrop image, offsetting the canvas ten pixels to the left and five pixels up, with respect to the thumbnail: </p>
<p>&nbsp;<wbr>gm convert infile.jpg -thumbnail 120&#215;80 -background red -gravity center&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-extent 140&#215;100-10-5 outfile.jpg </p>
<p> This command reduces or expands a JPEG image to fit on an 800&#215;600 display: </p>
<p>&nbsp;<wbr>gm convert -size 800&#215;600 input.jpg&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-resize 800&#215;600 -background black&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-compose Copy -gravity center&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-extent 800&#215;600&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-quality 92 output.jpg </p>
<p> If the aspect ratio of the input image isn&#8217;t exactly 4:3, then the image is centered on an 800&#215;600 black canvas.</p>
<dt><code>-file </code><i>&lt;filename&gt;</i></p>
<dd> write annotated difference image to file </p>
<p> If <code>-file</code> is specified, then an annotated difference image is generated and written to the specified file. Pixels which differ between the <code>reference</code> and <code>compare</code> images are modified from those in the <code>compare</code> image so that the changed pixels become more obvious. Some images may require use of an alternative highlight style (see <code>-highlight-style</code>) or highlight color (see <code>-highlight-color</code>) before the changes are obvious.</p>
<dt><code>-fill </code><i>&lt;color&gt;</i></p>
<dd> color to use when filling a graphic primitive </p>
<p> Colors are represented in GraphicsMagick in the same form used by SVG. Use &quot;gm convert -list color&quot; to list named colors: </p>
<p>&nbsp;<wbr>name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(named color)<br />
&nbsp;<wbr>#RGB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(hex numbers, 4 bits each)<br />
&nbsp;<wbr>#RRGGBB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(8 bits each)<br />
&nbsp;<wbr>#RRRGGGBBB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(12 bits each)<br />
&nbsp;<wbr>#RRRRGGGGBBBB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(16 bits each)<br />
&nbsp;<wbr>#RGBA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(4 bits each)<br />
&nbsp;<wbr>#RRGGBBAA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(8 bits each)<br />
&nbsp;<wbr>#RRRGGGBBBAAA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(12 bits each)<br />
&nbsp;<wbr>#RRRRGGGGBBBBAAAA&nbsp;<wbr>&nbsp;<wbr>(16 bits each)<br />
&nbsp;<wbr>rgb(r,g,b)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(r,g,b are decimal numbers)<br />
&nbsp;<wbr>rgba(r,g,b,a)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(r,g,b,a are decimal numbers) </p>
<p> Enclose the color specification in quotation marks to prevent the &quot;#&quot; or the parentheses from being interpreted by your shell. </p>
<p> For example, </p>
<p>&nbsp;<wbr>gm convert -fill blue &#8230;<br />
&nbsp;<wbr>gm convert -fill&nbsp;<wbr>&quot;#ddddff&quot;&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>gm convert -fill&nbsp;<wbr>&quot;rgb(65000,65000,65535)&quot;&nbsp;<wbr>&#8230; </p>
<p> The shorter forms are scaled up, if necessary by replication. For example, #3af, #33aaff, and #3333aaaaffff are all equivalent. </p>
<p> See <code>-draw</code> for further details.</p>
<dt><code>-filter </code><i>&lt;type&gt;</i></p>
<dd> use this type of filter when resizing an image </p>
<p> Use this option to affect the resizing operation of an image (see <code>-geometry</code>). Choose from these filters (ordered by approximate increasing CPU time): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Point<br />
&nbsp;<wbr>&nbsp;<wbr>Box<br />
&nbsp;<wbr>&nbsp;<wbr>Triangle<br />
&nbsp;<wbr>&nbsp;<wbr>Hermite<br />
&nbsp;<wbr>&nbsp;<wbr>Hanning<br />
&nbsp;<wbr>&nbsp;<wbr>Hamming<br />
&nbsp;<wbr>&nbsp;<wbr>Blackman<br />
&nbsp;<wbr>&nbsp;<wbr>Gaussian<br />
&nbsp;<wbr>&nbsp;<wbr>Quadratic<br />
&nbsp;<wbr>&nbsp;<wbr>Cubic<br />
&nbsp;<wbr>&nbsp;<wbr>Catrom<br />
&nbsp;<wbr>&nbsp;<wbr>Mitchell<br />
&nbsp;<wbr>&nbsp;<wbr>Lanczos<br />
&nbsp;<wbr>&nbsp;<wbr>Bessel<br />
&nbsp;<wbr>&nbsp;<wbr>Sinc </p>
<p> The default filter is automatically selected to provide the best quality while consuming a reasonable amount of time. The <code>Mitchell</code> filter is used if the image supports a palette, supports a matte channel, or is being enlarged, otherwise the <code>Lanczos</code> filter is used.</p>
<dt><code>-flatten</code></p>
<dd> flatten a sequence of images </p>
<p> In some file formats (e.g. Photoshop&#8217;s PSD) complex images may be represented by &quot;layers&quot; (independent images) which must be composited in order to obtain the final rendition. The <code>-flatten</code> option accomplishes this composition. The sequence of images is replaced by a single image created by compositing each image in turn, while respecting composition operators and page offsets. While <code>-flatten</code> is immediately useful for eliminating layers, it is also useful as a general-purpose composition tool. </p>
<p> The sequence of images is terminated by the appearance of any option. If the <code>-flatten</code> option appears after all of the input images, all images are flattened. Also see <code>-mosaic</code> which is similar to <code>-flatten</code> except that it adds a suitably-sized canvas base image. </p>
<p> For example, this composites an image on top of a 640&#215;400 transparent black canvas image: </p>
<p>&nbsp;<wbr>gm convert -size 640&#215;300 xc:transparent&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-compose over -page&nbsp;<wbr>+0-100&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>frame.png -flatten output.png </p>
<p> and this flattens a Photoshop PSD file: </p>
<p>&nbsp;<wbr>gm convert input.psd -flatten output.png </p>
<dt><code>-flip</code></p>
<dd> create a &quot;mirror image&quot; </p>
<p> reflect the scanlines in the vertical direction.</p>
<dt><code>-flop</code></p>
<dd> create a &quot;mirror image&quot; </p>
<p> reflect the scanlines in the horizontal direction.</p>
<dt><code>-font </code><i>&lt;name&gt;</i></p>
<dd> use this font when annotating the image with text </p>
<p> You can tag a font to specify whether it is a PostScript, TrueType, or X11 font. For example, Arial.ttf is a TrueType font, ps:helvetica is PostScript, and x:fixed is X11.</p>
<dt><code>-foreground </code><i>&lt;color&gt;</i></p>
<dd> define the foreground color </p>
<p> The color is specified using the format described under the <code>-fill</code> option.</p>
<dt><code>-format </code><i>&lt;type&gt;</i></p>
<dd> the image format type </p>
<p> When used with the <code>mogrify</code> utility, this option will convert any image to the image format you specify. See <i><a href="/docs/linux/man/1-graphicsmagick/">GraphicsMagick</a>(1)</i> for a list of image format types supported by <code>GraphicsMagick</code>, or see the output of &#8216;gm -list format&#8217;. </p>
<p> By default the file is written to its original name. However, if the filename extension matches a supported format, the extension is replaced with the image format type specified with <code>-format</code>. For example, if you specify <i>tiff</i> as the format type and the input image filename is <i>image.gif</i>, the output image filename becomes <i>image.tiff</i>.</p>
<dt><code>-format </code><i>&lt;string&gt;</i></p>
<dd> output formatted image characteristics </p>
<p> When used with the <code>identify</code> utility, or the <code>convert</code> utility with output written to the &#8216;info:-&#8216; file specification, use this option to print information about the image in a format of your choosing. You can include the image filename, type, width, height, Exif data, or other image attributes by embedding special format characters: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>%b&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>file size<br />
&nbsp;<wbr>&nbsp;<wbr>%c&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>comment<br />
&nbsp;<wbr>&nbsp;<wbr>%d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>directory<br />
&nbsp;<wbr>&nbsp;<wbr>%e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>filename extension<br />
&nbsp;<wbr>&nbsp;<wbr>%f&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>filename<br />
&nbsp;<wbr>&nbsp;<wbr>%g&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>page dimensions and offsets<br />
&nbsp;<wbr>&nbsp;<wbr>%h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>height<br />
&nbsp;<wbr>&nbsp;<wbr>%i&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>input filename<br />
&nbsp;<wbr>&nbsp;<wbr>%k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>number of unique colors<br />
&nbsp;<wbr>&nbsp;<wbr>%l&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>label<br />
&nbsp;<wbr>&nbsp;<wbr>%m&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>magick<br />
&nbsp;<wbr>&nbsp;<wbr>%n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>number of scenes<br />
&nbsp;<wbr>&nbsp;<wbr>%o&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>output filename<br />
&nbsp;<wbr>&nbsp;<wbr>%p&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>page number<br />
&nbsp;<wbr>&nbsp;<wbr>%q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>image bit depth<br />
&nbsp;<wbr>&nbsp;<wbr>%r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>image type description<br />
&nbsp;<wbr>&nbsp;<wbr>%s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>scene number<br />
&nbsp;<wbr>&nbsp;<wbr>%t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>top of filename<br />
&nbsp;<wbr>&nbsp;<wbr>%u&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unique temporary filename<br />
&nbsp;<wbr>&nbsp;<wbr>%w&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>width<br />
&nbsp;<wbr>&nbsp;<wbr>%x&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>horizontal resolution<br />
&nbsp;<wbr>&nbsp;<wbr>%y&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>vertical resolution<br />
&nbsp;<wbr>&nbsp;<wbr>%A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>transparency supported<br />
&nbsp;<wbr>&nbsp;<wbr>%C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>compression type<br />
&nbsp;<wbr>&nbsp;<wbr>%D&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>GIF disposal method<br />
&nbsp;<wbr>&nbsp;<wbr>%G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Original width and height<br />
&nbsp;<wbr>&nbsp;<wbr>%H&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>page height<br />
&nbsp;<wbr>&nbsp;<wbr>%M&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>original filename specification<br />
&nbsp;<wbr>&nbsp;<wbr>%O&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>page offset&nbsp;<wbr>(x,y)<br />
&nbsp;<wbr>&nbsp;<wbr>%P&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>page dimensions&nbsp;<wbr>(width,height)<br />
&nbsp;<wbr>&nbsp;<wbr>%Q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>compression quality<br />
&nbsp;<wbr>&nbsp;<wbr>%T&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>time delay&nbsp;<wbr>(in centi-seconds)<br />
&nbsp;<wbr>&nbsp;<wbr>%U&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>resolution units<br />
&nbsp;<wbr>&nbsp;<wbr>%W&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>page width<br />
&nbsp;<wbr>&nbsp;<wbr>%X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>page horizontal offset&nbsp;<wbr>(x)<br />
&nbsp;<wbr>&nbsp;<wbr>%Y&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>page vertical offset&nbsp;<wbr>(y)<br />
&nbsp;<wbr>&nbsp;<wbr>%@&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>trim bounding box<br />
&nbsp;<wbr>&nbsp;<wbr>%#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>signature<br />
&nbsp;<wbr>&nbsp;<wbr>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>newline<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>carriage return<br />
&nbsp;<wbr>&nbsp;<wbr>%%&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>% </p>
<p> For example, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-format&nbsp;<wbr>&quot;%m:%f&nbsp;<wbr>%wx%h&quot; </p>
<p> displays <code>MIFF:bird.miff 512&#215;480</code> for an image titled <code>bird.miff</code> and whose width is 512 and height is 480. </p>
<p> If the first character of <i>string</i> is <code>@</code>, the format is read from a file titled by the remaining characters in the string. </p>
<p> The values of image type (<code>%p</code>) which may be returned include: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Bilevel<br />
&nbsp;<wbr>&nbsp;<wbr>Grayscale<br />
&nbsp;<wbr>&nbsp;<wbr>GrayscaleMatte<br />
&nbsp;<wbr>&nbsp;<wbr>Palette<br />
&nbsp;<wbr>&nbsp;<wbr>PaletteMatte<br />
&nbsp;<wbr>&nbsp;<wbr>TrueColor<br />
&nbsp;<wbr>&nbsp;<wbr>TrueColorMatte<br />
&nbsp;<wbr>&nbsp;<wbr>ColorSeparation<br />
&nbsp;<wbr>&nbsp;<wbr>ColorSeparationMatte<br />
&nbsp;<wbr>&nbsp;<wbr>Optimize </p>
<p> You can also use the following special formatting syntax to print Exif information contained in the file: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>%[EXIF:&lt;tag&gt;] </p>
<p> Where &quot;&lt;tag&gt;&quot; may be one of the following: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>&nbsp;<wbr>(print all Exif tags, in keyword=data format)<br />
&nbsp;<wbr>&nbsp;<wbr>!&nbsp;<wbr>&nbsp;<wbr>(print all Exif tags, in tag_number format)<br />
&nbsp;<wbr>&nbsp;<wbr>#hhhh&nbsp;<wbr>(print data for Exif tag&nbsp;<wbr>#hhhh)<br />
&nbsp;<wbr>&nbsp;<wbr>ImageWidth<br />
&nbsp;<wbr>&nbsp;<wbr>ImageLength<br />
&nbsp;<wbr>&nbsp;<wbr>BitsPerSample<br />
&nbsp;<wbr>&nbsp;<wbr>Compression<br />
&nbsp;<wbr>&nbsp;<wbr>PhotometricInterpretation<br />
&nbsp;<wbr>&nbsp;<wbr>FillOrder<br />
&nbsp;<wbr>&nbsp;<wbr>DocumentName<br />
&nbsp;<wbr>&nbsp;<wbr>ImageDescription<br />
&nbsp;<wbr>&nbsp;<wbr>Make<br />
&nbsp;<wbr>&nbsp;<wbr>Model<br />
&nbsp;<wbr>&nbsp;<wbr>StripOffsets<br />
&nbsp;<wbr>&nbsp;<wbr>Orientation<br />
&nbsp;<wbr>&nbsp;<wbr>SamplesPerPixel<br />
&nbsp;<wbr>&nbsp;<wbr>RowsPerStrip<br />
&nbsp;<wbr>&nbsp;<wbr>StripByteCounts<br />
&nbsp;<wbr>&nbsp;<wbr>XResolution<br />
&nbsp;<wbr>&nbsp;<wbr>YResolution<br />
&nbsp;<wbr>&nbsp;<wbr>PlanarConfiguration<br />
&nbsp;<wbr>&nbsp;<wbr>ResolutionUnit<br />
&nbsp;<wbr>&nbsp;<wbr>TransferFunction<br />
&nbsp;<wbr>&nbsp;<wbr>Software<br />
&nbsp;<wbr>&nbsp;<wbr>DateTime<br />
&nbsp;<wbr>&nbsp;<wbr>Artist<br />
&nbsp;<wbr>&nbsp;<wbr>WhitePoint<br />
&nbsp;<wbr>&nbsp;<wbr>PrimaryChromaticities<br />
&nbsp;<wbr>&nbsp;<wbr>TransferRange<br />
&nbsp;<wbr>&nbsp;<wbr>JPEGProc<br />
&nbsp;<wbr>&nbsp;<wbr>JPEGInterchangeFormat<br />
&nbsp;<wbr>&nbsp;<wbr>JPEGInterchangeFormatLength<br />
&nbsp;<wbr>&nbsp;<wbr>YCbCrCoefficients<br />
&nbsp;<wbr>&nbsp;<wbr>YCbCrSubSampling<br />
&nbsp;<wbr>&nbsp;<wbr>YCbCrPositioning<br />
&nbsp;<wbr>&nbsp;<wbr>ReferenceBlackWhite<br />
&nbsp;<wbr>&nbsp;<wbr>CFARepeatPatternDim<br />
&nbsp;<wbr>&nbsp;<wbr>CFAPattern<br />
&nbsp;<wbr>&nbsp;<wbr>BatteryLevel<br />
&nbsp;<wbr>&nbsp;<wbr>Copyright<br />
&nbsp;<wbr>&nbsp;<wbr>ExposureTime<br />
&nbsp;<wbr>&nbsp;<wbr>FNumber<br />
&nbsp;<wbr>&nbsp;<wbr>IPTC/NAA<br />
&nbsp;<wbr>&nbsp;<wbr>ExifOffset<br />
&nbsp;<wbr>&nbsp;<wbr>InterColorProfile<br />
&nbsp;<wbr>&nbsp;<wbr>ExposureProgram<br />
&nbsp;<wbr>&nbsp;<wbr>SpectralSensitivity<br />
&nbsp;<wbr>&nbsp;<wbr>GPSInfo<br />
&nbsp;<wbr>&nbsp;<wbr>ISOSpeedRatings<br />
&nbsp;<wbr>&nbsp;<wbr>OECF<br />
&nbsp;<wbr>&nbsp;<wbr>ExifVersion<br />
&nbsp;<wbr>&nbsp;<wbr>DateTimeOriginal<br />
&nbsp;<wbr>&nbsp;<wbr>DateTimeDigitized<br />
&nbsp;<wbr>&nbsp;<wbr>ComponentsConfiguration<br />
&nbsp;<wbr>&nbsp;<wbr>CompressedBitsPerPixel<br />
&nbsp;<wbr>&nbsp;<wbr>ShutterSpeedValue<br />
&nbsp;<wbr>&nbsp;<wbr>ApertureValue<br />
&nbsp;<wbr>&nbsp;<wbr>BrightnessValue<br />
&nbsp;<wbr>&nbsp;<wbr>ExposureBiasValue<br />
&nbsp;<wbr>&nbsp;<wbr>MaxApertureValue<br />
&nbsp;<wbr>&nbsp;<wbr>SubjectDistance<br />
&nbsp;<wbr>&nbsp;<wbr>MeteringMode<br />
&nbsp;<wbr>&nbsp;<wbr>LightSource<br />
&nbsp;<wbr>&nbsp;<wbr>Flash<br />
&nbsp;<wbr>&nbsp;<wbr>FocalLength<br />
&nbsp;<wbr>&nbsp;<wbr>MakerNote<br />
&nbsp;<wbr>&nbsp;<wbr>UserComment<br />
&nbsp;<wbr>&nbsp;<wbr>SubSecTime<br />
&nbsp;<wbr>&nbsp;<wbr>SubSecTimeOriginal<br />
&nbsp;<wbr>&nbsp;<wbr>SubSecTimeDigitized<br />
&nbsp;<wbr>&nbsp;<wbr>FlashPixVersion<br />
&nbsp;<wbr>&nbsp;<wbr>ColorSpace<br />
&nbsp;<wbr>&nbsp;<wbr>ExifImageWidth<br />
&nbsp;<wbr>&nbsp;<wbr>ExifImageLength<br />
&nbsp;<wbr>&nbsp;<wbr>InteroperabilityOffset<br />
&nbsp;<wbr>&nbsp;<wbr>FlashEnergy<br />
&nbsp;<wbr>&nbsp;<wbr>SpatialFrequencyResponse<br />
&nbsp;<wbr>&nbsp;<wbr>FocalPlaneXResolution<br />
&nbsp;<wbr>&nbsp;<wbr>FocalPlaneYResolution<br />
&nbsp;<wbr>&nbsp;<wbr>FocalPlaneResolutionUnit<br />
&nbsp;<wbr>&nbsp;<wbr>SubjectLocation<br />
&nbsp;<wbr>&nbsp;<wbr>ExposureIndex<br />
&nbsp;<wbr>&nbsp;<wbr>SensingMethod<br />
&nbsp;<wbr>&nbsp;<wbr>FileSource<br />
&nbsp;<wbr>&nbsp;<wbr>SceneType </p>
<p> JPEG specific information (from reading a JPEG file) may be obtained like this: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>%[JPEG-&lt;tag&gt;] </p>
<p> Where &quot;&lt;tag&gt;&quot; may be one of the following: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(all JPEG-related tags, in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>keyword=data format)<br />
&nbsp;<wbr>&nbsp;<wbr>Quality&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>IJG JPEG&nbsp;<wbr>&quot;quality&quot;&nbsp;<wbr>estimate<br />
&nbsp;<wbr>&nbsp;<wbr>Colorspace&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>JPEG colorspace numeric ID<br />
&nbsp;<wbr>&nbsp;<wbr>Colorspace-Name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>JPEG colorspace name<br />
&nbsp;<wbr>&nbsp;<wbr>Sampling-factors&nbsp;<wbr>&nbsp;<wbr>JPEG sampling factors </p>
<p> Please note that JPEG has no notion of &quot;quality&quot; and that the quality metric used by, and estimated by the software is based on the quality metric established by IJG JPEG 6b. Other encoders (e.g. that used by Adobe Photoshop) use different encoding metrics. </p>
<p> Surround the format specification with quotation marks to prevent your shell from misinterpreting any spaces and square brackets.</p>
<dt><code>-frame </code><i>&lt;width&gt;x&lt;height&gt;+&lt;outer bevel width&gt;+&lt;inner bevel width&gt;</i></p>
<dd> surround the image with an ornamental border </p>
<p> See <code>-geometry</code> for details about the geometry specification. The <code>-frame</code> option is not affected by the <code>-gravity</code> option. </p>
<p> The color of the border is specified with the <code>-mattecolor</code> command line option.</p>
<dt><code>-frame</code></p>
<dd> include the X window frame in the imported image</p>
<dt><code>-fuzz </code><i>&lt;distance&gt;{%}</i></p>
<dd> colors within this Euclidean distance are considered equal </p>
<p> A number of algorithms search for a target color. By default the color must be exact. Use this option to match colors that are close (in Euclidean distance) to the target color in RGB 3D space. For example, if you want to automatically trim the edges of an image with <code>-trim</code> but the image was scanned and the target background color may differ by a small amount. This option can account for these differences. </p>
<p> The <i>distance</i> can be in absolute intensity units or, by appending <i>&quot;%&quot;</i>, as a percentage of the maximum possible intensity (255, 65535, or 4294967295).</p>
<dt><code>-gamma </code><i>&lt;value&gt;</i></p>
<dd> level of gamma correction </p>
<p> The same color image displayed on two different workstations may look different due to differences in the display monitor. Use gamma correction to adjust for this color difference. Reasonable values extend from <code>0.8</code> to <code>2.3</code>. Gamma less than 1.0 darkens the image and gamma greater than 1.0 lightens it. Large adjustments to image gamma may result in the loss of some image information if the pixel quantum size is only eight bits (quantum range 0 to 255). </p>
<p> You can apply separate gamma values to the red, green, and blue channels of the image with a gamma value list delimited with slashes (e.g., <code>1.7</code>/<code>2.3</code>/<code>1.2</code>). </p>
<p> Use <code>+gamma</code> <i>value</i> to set the image gamma level without actually adjusting the image pixels. This option is useful if the image is of a known gamma but not set as an image attribute (e.g. PNG images).</p>
<dt><code>-gaussian </code><i>&lt;radius&gt;{x&lt;sigma&gt;}</i></p>
<dd> blur the image with a Gaussian operator </p>
<p> Use the given radius and standard deviation (sigma).</p>
<dt><code>-geometry </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}{@}{!}{^}{&lt;}{&gt;}</i></p>
<dd> Specify dimension, offset, and resize options. </p>
<p> The <code>-geometry</code> option is used for a number of different purposes, depending on the utility it is used with. </p>
<p> For the X11 commands (&#8216;animate&#8217;, &#8216;display&#8217;, and &#8216;import&#8217;), it specifies the preferred size and location of the Image window. By default, the window size is the image size and the location is chosen by you (or your window manager) when it is mapped.<br />
&nbsp;<wbr>For the&nbsp;<wbr>&#8216;import&#8217;,&nbsp;<wbr>&#8216;convert&#8217;,&nbsp;<wbr>&#8216;mogrify&#8217;&nbsp;<wbr>utility commands it may be used to specify the desired size when resizing an image. In this case, symbols representing resize options may be appended to the geometry string to influence how the resize request is treated. </p>
<p> See later notes corresponding to usage by particular commands. The following notes apply to when <code>-geometry</code> is used to express a resize request, taking into account the current properties of the image. </p>
<p> By default, the width and height are maximum values. That is, the image is expanded or contracted to fit the width and height value while maintaining the aspect ratio of the image. </p>
<p> Append a ^ to the geometry so that the image aspect ratio is maintained when the image is resized, but the resulting width or height are treated as minimum values rather than maximum values. </p>
<p> Append a ! (exclamation point) to the geometry to force the image size to exactly the size you specify. For example, if you specify 640&#215;480! the image width is set to 640 pixels and height to 480. </p>
<p> If only the width is specified, without the trailing &#8216;x&#8217;, then height is set to width (e.g., -geometry 100 is the same as -geometry 100&#215;100). If only the width is specified but with the trailing &#8216;x&#8217;, then width assumes the value and the height is chosen to maintain the aspect ratio of the image. Similarly, if only the height is specified prefixed by &#8216;x&#8217; (e.g., -geometry x256), the width is chosen to maintain the aspect ratio. </p>
<p> To specify a percentage width or height instead, append %. The image size is multiplied by the width and height percentages to obtain the final image dimensions. To increase the size of an image, use a value greater than 100 (e.g. 125%). To decrease an image&#8217;s size, use a percentage less than 100. </p>
<p> Use @ to specify the maximum area in pixels of an image. </p>
<p> Use &gt; to change the dimensions of the image <i>only</i> if its width or height exceeds the geometry specification. &lt; resizes the image <i>only</i> if both of its dimensions are less than the geometry specification. For example, if you specify &#8216;640&#215;480&gt;&#8217; and the image size is 256&#215;256, the image size does not change. However, if the image is 512&#215;512 or 1024&#215;1024, it is resized to 480&#215;480. Enclose the geometry specification in quotation marks to prevent the &lt; or &gt; from being interpreted by your shell as a file redirection. </p>
<p> When used with <i>animate</i> and <i>display</i>, offsets are handled in the same manner as in <i><a href="/docs/linux/man/1-x/">X</a>(1)</i> and the <code>-gravity</code> option is not used. If the <i>x</i> is negative, the offset is measured leftward from the right edge of the screen to the right edge of the image being displayed. Similarly, negative <i>y</i> is measured between the bottom edges. The offsets are not affected by &quot;%&quot;; they are always measured in pixels. </p>
<p> When used as a <i>composite</i> option, <code>-geometry</code> gives the dimensions of the image and its location with respect to the composite image. If the <code>-gravity</code> option is present with <i>NorthEast, East,</i> or <i>SouthEast</i> gravity, the <i>x</i> represents the distance from the right edge of the image to the right edge of the composite image. Similarly, if the <code>-gravity</code> option is present with <i>SouthWest, South,</i> or <i>SouthEast</i> gravity, <i>y</i> is measured between the bottom edges. Accordingly, a positive offset will never point in the direction outside of the image. The offsets are not affected by &quot;%&quot;; they are always measured in pixels. To specify the dimensions of the composite image, use the <code>-resize</code> option. </p>
<p> When used as a <i>convert</i>, <i>import</i> or <i>mogrify</i> option, <code>-geometry</code> is synonymous with <code>-resize</code> and specifies the size of the output image. The offsets, if present, are ignored. </p>
<p> When used as a <i>montage</i> option, <code>-geometry</code> specifies the image size and border size for each tile; default is 256&#215;256+0+0. Negative offsets (border dimensions) are meaningless. The <code>-gravity</code> option affects the placement of the image within the tile; the default gravity for this purpose is <i>Center</i>. If the &quot;%&quot; sign appears in the geometry specification, the tile size is the specified percentage of the original dimensions of the first tile. To specify the dimensions of the montage, use the <code>-resize</code> option.</p>
<dt><code>-gravity </code><i>&lt;type&gt;</i></p>
<dd> direction primitive gravitates to when annotating the image. </p>
<p> Choices are: NorthWest, North, NorthEast, West, Center, East, SouthWest, South, SouthEast. </p>
<p> The direction you choose specifies where to position the text when annotating the image. For example <i>Center</i> gravity forces the text to be centered within the image. By default, the image gravity is <i>NorthWest</i>. See <code>-draw</code> for more details about graphic primitives. Only the text primitive is affected by the <code>-gravity</code> option. </p>
<p> The <code>-gravity</code> option is also used in concert with the <code>-geometry</code> option and other options that take <code>&lt;geometry&gt;</code> as a parameter, such as the <code>-crop</code> option. See <code>-geometry</code> for details of how the <code>-gravity</code> option interacts with the <code>&lt;x&gt;</code> and <code>&lt;y&gt;</code> parameters of a geometry specification. </p>
<p> When used as an option to <i>composite</i>, <code>-gravity</code> gives the direction that the image gravitates within the composite. </p>
<p> When used as an option to <i>montage</i>, <code>-gravity</code> gives the direction that an image gravitates within a tile. The default gravity is <i>Center</i> for this purpose.</p>
<dt><code>-green-primary </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> green chromaticity primary point</p>
<dt><code>-hald-clut </code><i>&lt;clut&gt;</i></p>
<dd> apply a Hald CLUT to the image </p>
<p> A Hald CLUT (&quot;Color Look-Up Table&quot;) is a special square color image which contains a look-up table for red, green, and blue. The size of the Hald CLUT image is determined by its order. The width (and height) of a Hald CLUT is the cube of the order. For example, a Hald CLUT of order 8 is 512&#215;512 pixels (262,144 colors) and of order 16 is 4096&#215;4096 (16,777,216 colors). A special CLUT is the identity CLUT which which causes no change to the input image. In order to use the Hald CLUT, one takes an identity CLUT and adjusts its colors in some way. The modified CLUT can then be used to transform any number of images in an identical way. </p>
<p> GraphicsMagick contains a built-in identity CLUT generator via the <code>IDENTITY</code> coder. For example reading from the file name IDENTITY:8 returns an identity CLUT of order 8. Typical Hald CLUT identity images have an order of between 8 and 16. The default order for the <code>IDENTITY</code> CLUT generator is 8. Interpolation is used so it is not usually necessary for CLUT images to be very large. The PNG file format is ideal for storing Hald CLUT images because it compresses them very well.</p>
<dt><code>-help</code></p>
<dd> print usage instructions</p>
<dt><code>-highlight-color </code><i>&lt;color&gt;</i></p>
<dd> pixel annotation color </p>
<p> Specifies the color to use when annotating difference pixels.</p>
<dt><code>-highlight-style </code><i>&lt;style&gt;</i></p>
<dd> pixel annotation style </p>
<p> Specifies the pixel difference annotation style used to draw attention to changed pixels. May be one of <code>Assign</code>, <code>Threshold</code>, <code>Tint</code>, or <code>XOR</code>; where <code>Assign</code> replaces the pixel with the highlight color (see <code>-highlight-color</code>), <code>Threshold</code> replaces the pixel with black or white based on the difference in intensity, <code>Tint</code> alpha tints the pixel with the highlight color, and <code>XOR</code> does an XOR between the pixel and the highlight color.</p>
<dt><code>-iconGeometry </code><i>&lt;geometry&gt;</i></p>
<dd> specify the icon geometry </p>
<p> Offsets, if present in the geometry specification, are handled in the same manner as the <code>-geometry</code> option, using X11 style to handle negative offsets.</p>
<dt><code>-iconic</code></p>
<dd> iconic animation</p>
<dt><code>-immutable</code></p>
<dd> make image immutable</p>
<dt><code>-implode </code><i>&lt;factor&gt;</i></p>
<dd> implode image pixels about the center</p>
<dt><code>-intent </code><i>&lt;type&gt;</i></p>
<dd> use this type of rendering intent when managing the image color </p>
<p> Use this option to affect the the color management operation of an image (see <code>-profile</code>). Choose from these intents: <code>Absolute, Perceptual, Relative, Saturation</code>. </p>
<p> The default intent is undefined.</p>
<dt><code>-interlace </code><i>&lt;type&gt;</i></p>
<dd> the type of interlacing scheme </p>
<p> Choices are: <code>None, Line, Plane,</code> or <code>Partition</code>. The default is <code>None</code>. </p>
<p> This option is used to specify the type of interlacing scheme for raw image formats such as <code>RGB</code> or <code>YUV</code>. <code>None</code> means do not interlace (RGBRGBRGBRGBRGBRGB&#8230;), </p>
<p> <code>Line</code> uses scanline interlacing (RRR&#8230;GGG&#8230;BBB&#8230;RRR&#8230;GGG&#8230;BBB&#8230;), and <code>Plane</code> uses plane interlacing (RRRRRR&#8230;GGGGGG&#8230;BBBBBB&#8230;). </p>
<p> <code>Partition</code> is like plane except the different planes are saved to individual files (e.g. image.R, image.G, and image.B). </p>
<p> Use <code>Line</code> to create an <code>interlaced PNG</code> or <code> GIF</code> or <code>progressive JPEG</code> image.</p>
<dt><code>-label </code><i>&lt;name&gt;</i></p>
<dd> assign a label to an image </p>
<p> Use this option to assign a specific label to the image, when writing to an image format that supports labels, such as TIFF, PNG, MIFF, or PostScript. You can include the the image filename, type, width, height, or other image attribute by embedding special format character. A label is not drawn on the image, but is embedded in the image datastream via a &quot;Label&quot; tag or similar mechanism. If you want the label to be visible on the image itself, use the <code>-draw</code> option. See <code>-comment</code> for details. </p>
<p> For example, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-label&nbsp;<wbr>&quot;%m:%f&nbsp;<wbr>%wx%h&quot; </p>
<p> produces an image label of <code>MIFF:bird.miff 512&#215;480</code> for an image titled <code>bird.miff</code> and whose width is 512 and height is 480. </p>
<p> If the first character of <i>string</i> is <i>@</i>, the image label is read from a file titled by the remaining characters in the string. </p>
<p> If the -label option appears multiple times, only the last label is stored. </p>
<p> In PNG images, the label is stored in a <code>tEXt</code> or <code>zTXt</code> chunk with the keyword &quot;label&quot;. </p>
<p> When converting to <i>PostScript</i>, use this option to specify a header string to print above the image. Specify the label font with <code>-font</code>. </p>
<p> When creating a montage, by default the label associated with an image is displayed with the corresponding tile in the montage. Use the <code>+label</code> option to suppress this behavior. </p>
<dt><code>-lat </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;offset&gt;{%}</i></p>
<dd> perform local adaptive thresholding </p>
<p> Perform local adaptive thresholding using the specified width, height, and offset. The offset is a distance in sample space from the mean, as an absolute integer ranging from 0 to the maximum sample value or as a percentage. If the percent option is supplied, then the offset is computed as a percentage of the quantum range. It is strongly recommended to use the percent option so that results are not sensitive to pixel quantum depth. </p>
<p> For example, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-colorspace gray -lat&nbsp;<wbr>&quot;10&#215;10-5%&quot; </p>
<p> will help clarify a scanned grayscale or color document, producing a bi-level equivalent.</p>
<dt><code>-level </code><i>&lt;black_point&gt;{,&lt;gamma&gt;}{,&lt;white_point&gt;}{%}</i></p>
<dd> adjust the level of image contrast </p>
<p> Give one, two or three values delimited with commas: black-point, gamma, white-point (e.g. 10,1.0,250 or 2%,0.5,98%). The black and white points range from 0 to MaxRGB or from 0 to 100%; if the white point is omitted it is set to MaxRGB-black_point. If a &quot;%&quot; sign is present anywhere in the string, the black and white points are percentages of MaxRGB. Gamma is an exponent that ranges from 0.1 to 10.; if it is omitted, the default of 1.0 (no gamma correction) is assumed. This interface works similar to Photoshop&#8217;s &quot;Image-&gt;Adjustments-&gt;Levels&#8230;&quot; &quot;Input Levels&quot; interface.</p>
<dt><code>-limit </code><i>&lt;type&gt; &lt;value&gt;</i></p>
<dd> Disk, File, Map, Memory, Pixels, Width, Height or Threads resource limit </p>
<p> By default, resource limits are estimated based on the available resources of the system. The resource limits are <code>Disk</code>, maximum total disk space consumed; <code>File</code>, maximum number of file descriptors allowed to be open at once; <code>Map</code>, maximum total number of file bytes which may be memory mapped; <code>Memory</code>, maximum total number of bytes of heap memory used for image storage; <code>Pixels</code>, maximum absolute image size (per image); <code>Width</code>, maximum image pixels width; <code>Height</code>, maximum image pixels height; and <code>Threads</code>, the maximum number of worker threads to use per OpenMP thread team. </p>
<p> These resource limits are used to decide if (for a given image) the decoded image (&quot;pixel cache&quot;) should be stored in heap memory (RAM), in a memory-mapped disk file, or in a disk file accessed via read/write I/O. The number of total pixels in one image, and/or the width/height, may also be limited in order to force the reading, or creation of images larger than the limit (in pixels) to intentionally fail. The disk limit establishes an overall limit since using the disk is the means of last resort. When the disk limit has been reached, no more images may be read. </p>
<p> The value argument is an absolute value, but may have standard binary suffix characters applied (&#8216;K&#8217;, &#8216;M&#8217;, &#8216;G&#8217;, &#8216;T&#8217;, &#8216;P&#8217;, &#8216;E&#8217;) to apply a scaling to the value (based on a multiplier of 1024). Any additional characters are ignored. For example, &#8216;-limit Pixels 10MP&#8217; limits the maximum image size to 10 megapixels and &#8216;-limit memory 32MB -limit map 64MB&#8217; limits memory and memory mapped files to 32 megabytes and 64 megabytes respectively. </p>
<p> Resource limits may also be set using environment variables. The environment variables <code>MAGICK_LIMIT_DISK</code>, <code>MAGICK_LIMIT_FILES</code>, <code>MAGICK_LIMIT_MAP</code>, <code>MAGICK_LIMIT_MEMORY</code>, <code>MAGICK_LIMIT_PIXELS</code>, <code>MAGICK_LIMIT_WIDTH</code>, <code>MAGICK_LIMIT_HEIGHT</code>,and <code>OMP_NUM_THREADS</code> may be used to set the limits for disk space, open files, memory mapped size, heap memory, per-image pixels, image width, image height, and threads respectively. </p>
<p> Use the option -list resource list the current limits.</p>
<dt><code>-linewidth</code></p>
<dd> the line width for subsequent draw operations</p>
<dt><code>-list </code><i>&lt;type&gt;</i></p>
<dd> the type of list </p>
<p> Choices are: <code>Color</code>, <code>Delegate</code>, <code>Format</code>, <code>Magic</code>, <code>Module</code>, <code>Resource</code>, or <code>Type</code>. The <code>Module</code> option is only available if GraphicsMagick was built to support loadable modules. </p>
<p> This option lists information about the GraphicsMagick configuration.</p>
<dt><code>-log </code><i>&lt;string&gt;</i></p>
<dd> Specify format for debug log </p>
<p> This option specifies the format for the log printed when the <code>-debug</code> option is active. </p>
<p> You can display the following components by embedding special format characters: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>%d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>domain<br />
&nbsp;<wbr>&nbsp;<wbr>%e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>event<br />
&nbsp;<wbr>&nbsp;<wbr>%f&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>function<br />
&nbsp;<wbr>&nbsp;<wbr>%l&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>line<br />
&nbsp;<wbr>&nbsp;<wbr>%m&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>module<br />
&nbsp;<wbr>&nbsp;<wbr>%p&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>process ID<br />
&nbsp;<wbr>&nbsp;<wbr>%r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>real CPU time<br />
&nbsp;<wbr>&nbsp;<wbr>%t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>wall clock time<br />
&nbsp;<wbr>&nbsp;<wbr>%u&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>user CPU time<br />
&nbsp;<wbr>&nbsp;<wbr>%%&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>percent sign<br />
&nbsp;<wbr>&nbsp;<wbr>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>newline<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>carriage return </p>
<p> For example: </p>
<p>&nbsp;<wbr>gm convert -debug coders -log&nbsp;<wbr>&quot;%u&nbsp;<wbr>%m:%l&nbsp;<wbr>%e&quot;&nbsp;<wbr>in.gif out.png </p>
<p> The default behavior is to print all of the components.</p>
<dt><code>-loop </code><i>&lt;iterations&gt;</i></p>
<dd> add Netscape loop extension to your GIF animation </p>
<p> A value other than zero forces the animation to repeat itself up to <i>iterations</i> times.</p>
<dt><code>-magnify</code></p>
<dd> magnify the image </p>
<p> The image size is doubled using linear interpolation.</p>
<dt><code>-magnify </code><i>&lt;factor&gt;</i></p>
<dd> magnify the image </p>
<p> The displayed image is magnified by <code>factor</code>.</p>
<dt><code>-map </code><i>&lt;filename&gt;</i></p>
<dd> choose a particular set of colors from this image </p>
<p> [<i>convert</i> or <i>mogrify</i>] </p>
<p> By default, color reduction chooses an optimal set of colors that best represent the original image. Alternatively, you can choose a particular set of colors from an image file with this option. </p>
<p> Use <code>+map</code> to reduce all images in the image sequence that follows to a single optimal set of colors that best represent all the images. The sequence of images is terminated by the appearance of any option. If the <code>+map</code> option appears after all of the input images, all images are mapped.</p>
<dt><code>-map </code><i>&lt;type&gt;</i></p>
<dd> display image using this type. </p>
<p> [<i>animate</i> or <i>display</i>] </p>
<p> Choose from these <i>Standard Colormap</i> types: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>best<br />
&nbsp;<wbr>&nbsp;<wbr>default<br />
&nbsp;<wbr>&nbsp;<wbr>gray<br />
&nbsp;<wbr>&nbsp;<wbr>red<br />
&nbsp;<wbr>&nbsp;<wbr>green<br />
&nbsp;<wbr>&nbsp;<wbr>blue </p>
<p> The <i>X server</i> must support the <i>Standard Colormap</i> you choose, otherwise an error occurs. Use <code>list</code> as the type and <code>display</code> searches the list of colormap types in <code>top-to-bottom</code> order until one is located. See <i><a href="/docs/linux/man/1-xstdcmap/">xstdcmap</a>(1)</i> for one way of creating Standard Colormaps.</p>
<dt><code>-mask </code><i>&lt;filename&gt;</i></p>
<dd> Specify a clipping mask </p>
<p> The image read from the file is used as a clipping mask. It must have the same dimensions as the image being masked. </p>
<p> If the mask image contains an opacity channel, the opacity of each pixel is used to define the mask. Otherwise, the intensity (gray level) of each pixel is used. Unmasked (black) pixels are modified while masked pixels (not black) are protected from alteration. </p>
<p> Use <code>+mask</code> to remove the clipping mask. </p>
<p> It is not necessary to use <code>-clip</code> to activate the mask; <code>-clip</code> is implied by <code>-mask</code>.</p>
<dt><code>-matte</code></p>
<dd> store matte channel if the image has one </p>
<p> If the image does not have a matte channel, create an opaque one. </p>
<p> Use <code>+matte</code> to ignore the matte channel and to avoid writing a matte channel in the output file.</p>
<dt><code>-mattecolor </code><i>&lt;color&gt;</i></p>
<dd> specify the color to be used with the <code>-frame</code> option </p>
<p> The color is specified using the format described under the <code>-fill</code> option.</p>
<dt><code>-maximum-error </code><i>&lt;limit&gt;</i></p>
<dd> specifies the maximum amount of total image error </p>
<p> Specifies the maximum amount of total image error (based on comparison using a specified metric) before an error (&quot;image difference exceeds limit&quot;) is reported. The error is reported via a non-zero command execution return status.</p>
<dt><code>-median </code><i>&lt;radius&gt;</i></p>
<dd> apply a median filter to the image</p>
<dt><code>-metric </code><i>&lt;metric&gt;</i></p>
<dd> comparison metric (MAE, MSE, PAE, PSNR, RMSE)</p>
<dt><code>-minify </code><i>&lt;factor&gt;</i></p>
<dd> minify the image </p>
<p> The image size is halved using linear interpolation.</p>
<dt><code>-mode </code><i>&lt;value&gt;</i></p>
<dd> mode of operation </p>
<p> The available montage modes are <code>frame</code> to place the images in a rectangular grid while adding a decorative frame with dropshadow, <code>unframe</code> to place undecorated images in a rectangular grid, and <code>concatenate</code> to pack the images closely together without any well-defined grid or decoration.</p>
<dt><code>-modulate </code><i>brightness[,saturation[,hue]]</i></p>
<dd> vary the brightness, saturation, and hue of an image </p>
<p> Specify the percent change in brightness, color saturation, and hue separated by commas. Default argument values are 100 percent, resulting in no change. For example, to increase the color brightness by 20% and decrease the color saturation by 10% and leave the hue unchanged, use: <code>-modulate 120,90</code>. </p>
<p> Hue is the percentage of absolute rotation from the current position. For example 50 results in a counter-clockwise rotation of 90 degrees, 150 results in a clockwise rotation of 90 degrees, with 0 and 200 both resulting in a rotation of 180 degrees.</p>
<dt><code>-monitor</code></p>
<dd> show progress indication </p>
<p> A simple command-line progress indication is shown while the command is running. The process indication shows the operation currently being performed and the percent completed. Commands using X11 may replace the command line progress indication with a graphical one once an image has been displayed.</p>
<dt><code>-monochrome</code></p>
<dd> transform the image to black and white</p>
<dt><code>-morph </code><i>&lt;frames&gt;</i></p>
<dd> morphs an image sequence </p>
<p> Both the image pixels and size are linearly interpolated to give the appearance of a meta-morphosis from one image to the next. </p>
<p> The sequence of images is terminated by the appearance of any option. If the <code>-morph</code> option appears after all of the input images, all images are morphed.</p>
<dt><code>-mosaic</code></p>
<dd> create a mosaic from an image or an image sequence </p>
<p> The <code>-mosaic</code> option provides a flexible way to composite one or more images onto a solid-color canvas image. It works similar to <code>-flatten</code> except that a base canvas image is automatically created with a suitable size given the image size, page dimensions, and page offsets of images to be composited. The color of the base canvas image may be set via the <code>-background</code> option. The default canvas color is &#8216;white&#8217;, but &#8216;black&#8217; or &#8216;transparent&#8217; may be more suitable depending on the composition algorithm requested. </p>
<p> The <code>-compose</code> option may be used to specify the composition algorithm to use when compositing the subsequent image on the base canvas. </p>
<p> The <code>-page</code> option can be used to establish the dimensions of the mosaic and to position the subsequent image within the mosaic. If the <code>-page</code> argument does not specify width and height, then the canvas dimensions are evaluated based on the image sizes and offsets. </p>
<p> The sequence of images is terminated by the appearance of any option. If the <code>-mosaic</code> option appears after all of the input images, all images are included in the mosaic. </p>
<p> The following is an example of composing an image based on red, green, and blue layers extracted from a sequence of images and pasted on the canvas image at specified offsets: </p>
<p>&nbsp;<wbr>gm convert -background black&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-compose CopyRed&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-page&nbsp;<wbr>+0-100 red.png&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-compose CopyGreen -page&nbsp;<wbr>+0+40&nbsp;<wbr>&nbsp;<wbr>green.png&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-compose CopyBlue&nbsp;<wbr>&nbsp;<wbr>-page&nbsp;<wbr>+0+180 blue.png&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-mosaic output.png </p>
<dt><code>-motion-blur </code><i>&lt;radius&gt;{x&lt;sigma&gt;}{+angle}</i></p>
<dd> Simulate motion blur </p>
<p> Simulate motion blur by convolving the image with a Gaussian operator of the given radius and standard deviation (sigma). For reasonable results, radius should be larger than sigma. If radius is zero, then a suitable radius is automatically selected based on sigma. The angle specifies the angle that the object is coming from (side which is blurred).</p>
<dt><code>-name</code></p>
<dd> name an image</p>
<dt><code>-negate</code></p>
<dd> replace every pixel with its complementary color </p>
<p> The red, green, and blue intensities of an image are negated. White becomes black, yellow becomes blue, etc. Use <code>+negate</code> to only negate the grayscale pixels of the image.</p>
<dt><code>-noise </code><i>&lt;radius|type&gt;</i></p>
<dd> add or reduce noise in an image </p>
<p> The principal function of noise peak elimination filter is to smooth the objects within an image without losing edge information and without creating undesired structures. The central idea of the algorithm is to replace a pixel with its next neighbor in value within a pixel window, if this pixel has been found to be noise. A pixel is defined as noise if and only if this pixel is a maximum or minimum within the pixel window. </p>
<p> Use <code>radius</code> to specify the width of the neighborhood. </p>
<p> Use <code>+noise</code> followed by a noise type to add noise to an image. The noise added modulates the existing image pixels. Choose from these noise types: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Uniform<br />
&nbsp;<wbr>&nbsp;<wbr>Gaussian<br />
&nbsp;<wbr>&nbsp;<wbr>Multiplicative<br />
&nbsp;<wbr>&nbsp;<wbr>Impulse<br />
&nbsp;<wbr>&nbsp;<wbr>Laplacian<br />
&nbsp;<wbr>&nbsp;<wbr>Poisson<br />
&nbsp;<wbr>&nbsp;<wbr>Random&nbsp;<wbr>(uniform distribution) </p>
<dt><code>-noop</code></p>
<dd> NOOP (no option) </p>
<p> The <code>-noop</code> option can be used to terminate a group of images and reset all options to their default values, when no other option is desired.</p>
<dt><code>-normalize</code></p>
<dd> transform image to span the full range of color values </p>
<p> This is a contrast enhancement technique based on the image histogram. </p>
<p> When computing the contrast enhancement values, the histogram edges are truncated so that the majority of the image pixels are considered in the constrast enhancement, and outliers (e.g. random noise or minute details) are ignored. The default is that 0.1 percent of the histogram entries are ignored. The percentage of the histogram to ignore may be specified by using the <code>-set</code> option with the <code>histogram-threshold</code> parameter similar to <code>-set histogram-threshold 0.01</code> to specify 0.01 percent. Use 0 percent to use the entire histogram, with possibly diminished contrast enhancement.</p>
<dt><code>-opaque </code><i>&lt;color&gt;</i></p>
<dd> change this color to the pen color within the image </p>
<p> The color is specified using the format described under the <code>-fill</code> option. The color is replaced if it is identical to the target color, or close enough to the target color in a 3D space as defined by the Euclidean distance specified by <code>-fuzz</code>. </p>
<p> See <code>-fill</code> and <code>-fuzz</code> for more details.</p>
<dt><code>-operator </code><i>channel operator rvalue[%]</i></p>
<dd> apply a mathematical, bitwise, or value operator to an image channel </p>
<p> Apply a low-level mathematical, bitwise, or value operator to a selected image channel or all image channels. Operations which result in negative results are reset to zero, and operations which overflow the available range are reset to the maximum possible value. </p>
<p> Select a channel from: <code>Red</code>, <code>Green</code>, <code>Blue</code>, <code>Opacity</code>, <code>Matte</code>, <code>Cyan</code>, <code>Magenta</code>, <code>Yellow</code>, <code>Black</code>, <code>All</code>, or <code>Gray</code>. <code>All</code> only modifies the color channels and does not modify the <code>Opacity</code> channel. Except for the threshold operators, <code>All</code> operates on each channel independently so that operations are on a per-channel basis. </p>
<p> <code>Gray</code> treats the color channels as a grayscale intensity and performs the requested operation on the equivalent pixel intensity so the result is a gray image. Select an operator from <code>Add</code>, <code>And</code>, <code>Assign</code>, <code>Depth</code>, <code>Divide</code>, <code>Gamma</code>, <code>Negate</code>, <code>LShift</code>, <code>Log</code>, <code>Max</code>, <code>Min</code>, <code>Multiply</code>, <code>Or</code>, <code>Pow</code> <code>RShift</code>, <code>Subtract</code>, <code>Threshold</code>, <code>Threshold-White</code>, <code>Threshold-White-Negate</code>, <code>Threshold-Black</code>, <code>Threshold-Black-Negate</code>, <code>Xor</code>, <code>Noise-Gaussian</code>, <code>Noise-Impulse</code>, <code>Noise-Laplacian</code>, <code>Noise-Multiplicative</code>, <code>Noise-Poisson</code>, <code>Noise-Random</code>, and <code>Noise-Uniform</code>. </p>
<p> Rvalue may be any floating point or integer value. Normally rvalue will be in the range of 0 to MaxRGB, where MaxRGB is the largest quantum value supported by the GraphicsMagick build (255, 65535, or 4294967295) but values outside this range are useful for some arithmetic operations. Arguments to logical or bit-wise operations are rounded to a positive integral value prior to use. If a percent (<code>%</code>) symbol is appended to the argument, then the argument has a range of 0 to 100 percent. </p>
<p> The following is a description of the operators: </p>
<p> <code>Add</code><br />
&nbsp;<wbr> Result is rvalue added to channel value. </p>
<p> <code>And</code><br />
&nbsp;<wbr> Result is the logical AND of rvalue with channel value. </p>
<p> <code>Assign</code><br />
&nbsp;<wbr> Result is rvalue. </p>
<p> <code>Depth</code><br />
&nbsp;<wbr> Result is channel value adjusted so that it may be (approximately) stored in the specified number of bits without additional loss. </p>
<p> <code>Divide</code><br />
&nbsp;<wbr> Result is channel value divided by rvalue. </p>
<p> <code>Gamma</code><br />
&nbsp;<wbr> Result is channel value gamma adjusted by rvalue. </p>
<p> <code>LShift</code><br />
&nbsp;<wbr> Result is channel value bitwise left shifted by rvalue bits. </p>
<p> <code>Log</code><br />
&nbsp;<wbr> Result is computed as log(value*rvalue+1)/log(rvalue+1). </p>
<p> <code>Max</code><br />
&nbsp;<wbr> Result is assigned to rvalue if rvalue is greater than value. </p>
<p> <code>Min</code><br />
&nbsp;<wbr> Result is assigned to rvalue if rvalue is less than value. </p>
<p> <code>Multiply</code><br />
&nbsp;<wbr> Result is channel value multiplied by rvalue. </p>
<p> <code>Negate</code><br />
&nbsp;<wbr> Result is inverse of channel value (like a film negative). An rvalue must be supplied but is currently not used. Inverting the image twice results in the original image. </p>
<p> <code>Or</code><br />
&nbsp;<wbr> Result is the logical OR of rvalue with channel value. </p>
<p> <code>Pow</code><br />
&nbsp;<wbr> Result is computed as pow(value,rvalue). Similar to Gamma except that rvalue is not inverted. </p>
<p> <code>RShift</code><br />
&nbsp;<wbr> Result is channel value bitwise right shifted by rvalue bits. </p>
<p> <code>Subtract</code><br />
&nbsp;<wbr> Result is channel value minus rvalue. </p>
<p> <code>Threshold</code><br />
&nbsp;<wbr> Result is maximum (white) if channel value is greater than rvalue, or minimum (black) if it is less than or equal to rvalue. If <code>all</code> channels are specified, then thresholding is done based on computed pixel intensity. </p>
<p> <code>Threshold-white</code><br />
&nbsp;<wbr> Result is maximum (white) if channel value is greater than rvalue and is unchanged if it is less than or equal to rvalue. This can be used to remove apparent noise from the bright parts of an image. If <code>all</code> channels are specified, then thresholding is done based on computed pixel intensity. </p>
<p> <code>Threshold-White-Negate</code><br />
&nbsp;<wbr> Result is set to black if channel value is greater than rvalue and is unchanged if it is less than or equal to rvalue. If <code>all</code> channels are specified, then thresholding is done based on computed pixel intensity. </p>
<p> <code>Threshold-black</code><br />
&nbsp;<wbr> Result is minimum (black) if channel value is less than than rvalue and is unchanged if it is greater than or equal to rvalue. This can be used to remove apparent noise from the dark parts of an image. If <code>all</code> channels are specified, then thresholding is done based on computed pixel intensity. </p>
<p> <code>Threshold-Black-Negate</code><br />
&nbsp;<wbr> Result is set to white if channel value is less than than rvalue and is unchanged if it is greater than or equal to rvalue. If <code>all</code> channels are specified, then thresholding is done based on computed pixel intensity. </p>
<p> <code>Xor</code><br />
&nbsp;<wbr> Result is the logical XOR of rvalue with channel value. An interesting property of XOR is that performing the same operation twice results in the original value. </p>
<p> <code>Noise-Gaussian</code><br />
&nbsp;<wbr> Result is the current channel value modulated with gaussian noise according to the intensity specified by rvalue. </p>
<p> <code>Noise-Impulse</code><br />
&nbsp;<wbr> Result is the current channel value modulated with impulse noise according to the intensity specified by rvalue. </p>
<p> <code>Noise-Laplacian</code><br />
&nbsp;<wbr> Result is the current channel value modulated with laplacian noise according to the intensity specified by rvalue. </p>
<p> <code>Noise-Multiplicative</code><br />
&nbsp;<wbr> Result is the current channel value modulated with multiplicative gaussian noise according to the intensity specified by rvalue. </p>
<p> <code>Noise-Poisson</code><br />
&nbsp;<wbr> Result is the current channel value modulated with poisson noise according to the intensity specified by rvalue. </p>
<p> <code>Noise-Random</code><br />
&nbsp;<wbr> Result is the current channel value modulated with random (uniform distribution) noise according to the intensity specified by rvalue. The initial noise intensity (rvalue=1.0) is the range of one pixel quantum span. </p>
<p> <code>Noise-Uniform</code><br />
&nbsp;<wbr> Result is the channel value with uniform noise applied according to the intensity specified by rvalue. </p>
<p> As an example, the <code>Assign</code> operator assigns a fixed value to a channel. For example, this command sets the red channel to the mid-range value: </p>
<p>&nbsp;<wbr>gm convert in.bmp -operator red assign&nbsp;<wbr>&quot;50%&quot;&nbsp;<wbr>out.bmp </p>
<p> The following applies 50% thresholding to the image and returns a gray image: </p>
<p>&nbsp;<wbr>gm convert in.bmp -operator gray threshold&nbsp;<wbr>&quot;50%&quot;&nbsp;<wbr>out.bmp </p>
<dt><code>-ordered-dither </code><i>&lt;channeltype&gt; &lt;NxN&gt;</i></p>
<dd> ordered dither the image </p>
<p> The channel or channels specified in the <code>channeltype</code> argument are reduced to binary, using an ordered dither method. The choices for <code>channeltype</code> are <code>All</code>, <code>Intensity</code>, <code>Red</code>, <code>Green</code>, <code>Blue</code>, <code>Cyan</code>, <code>Magenta</code>, <code>Yellow</code>, <code>Black</code>, and <code>Opacity</code> </p>
<p> When <code>channeltype</code> is &quot;All&quot;, the color samples are dithered into a gray level and then that gray level is stored in the three color channels. Separately, the opacity channel is dithered into a bilevel opacity value which is stored in the opacity channel. </p>
<p> When <code>channeltype</code> is &quot;Intensity&quot;, only the color samples are dithered. When <code>channeltype</code> is &quot;opacity&quot; or &quot;matte&quot;, only the opacity channel is dithered. When a color channel is specified, only that channel is dithered. </p>
<p> The choices for N are 2 through 7. The image is divided into NxN pixel tiles. In each tile, some or all pixels are turned to white depending on their intensity. For each N, (N**2)+1 levels of gray can be represented. For N == 2, 3, or 4, the pixels are turned to white in an order that maximizes dispersion (i.e., reduces granularity), while for N == 5, 6, and 7, they are turned to white in an order that creates a roughly circular black blob in the middle of each tile. An attractive &quot;half-tone&quot; looking image can be obtained by first rotating the image 45 degrees, performing a 5&#215;5 ordered-dither operation, then rotating it back to the original orientation and cropping to the original image dimensions. If the original image is gamma-encoded, it is adviseable to convert it to linear intensity first, e.g., with the &quot;-gamma 0.45455&quot; option.</p>
<dt><code>-output-directory </code><i>&lt;directory&gt;</i></p>
<dd> output files to directory </p>
<p> Use -output-directory to specify a directory under which to write the output files. Normally mogrify overwrites the input files but with this option the output files may be written to a different directory so that the input files are preserved. The algorithm used preserves all of the input path specification in the output path so that the user-specified input path (including any directory part) is appended to the output path. The user is responsible for creating the output directory.</p>
<dt><code>-orient </code><i>&lt;orientation&gt;</i></p>
<dd> Set the image orientation attribute </p>
<p> Sets the image orientation attribute. The image orientation attribute is compatible with the TIFF orientation tag (and the EXIF orientation tag). Accepted values are <code>undefined</code>, <code>TopLeft</code>, <code>TopRight</code>, <code>BottomRight</code>, <code>BottomLeft</code>, <code>LeftTop</code>, <code>RightTop</code>, <code>RightBottom</code>, <code>LeftBottom</code>, and hyphenated versions thereof (e.g. <code>left-bottom</code>). Please note that GraphicsMagick does not include an EXIF editor so if an EXIF profile is written to the output image, the value in the EXIF profile might not match the image. It is possible for an image file to indicate its orientation in several different ways simultaneously.</p>
<dt><code>-page </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}{!}{&lt;}{&gt;}</i></p>
<dd> size and location of an image canvas </p>
<p> Use this option to specify the dimensions of the <i>PostScript</i> page in dots per inch or a TEXT page in pixels. The choices for a PostScript page are: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>11&#215;17&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>792&nbsp;<wbr>&nbsp;<wbr>1224<br />
&nbsp;<wbr>&nbsp;<wbr>Ledger&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1224&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>792<br />
&nbsp;<wbr>&nbsp;<wbr>Legal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>612&nbsp;<wbr>&nbsp;<wbr>1008<br />
&nbsp;<wbr>&nbsp;<wbr>Letter&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>612&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>792<br />
&nbsp;<wbr>&nbsp;<wbr>LetterSmall&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>612&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>792<br />
&nbsp;<wbr>&nbsp;<wbr>ArchE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2592&nbsp;<wbr>&nbsp;<wbr>3456<br />
&nbsp;<wbr>&nbsp;<wbr>ArchD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1728&nbsp;<wbr>&nbsp;<wbr>2592<br />
&nbsp;<wbr>&nbsp;<wbr>ArchC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1296&nbsp;<wbr>&nbsp;<wbr>1728<br />
&nbsp;<wbr>&nbsp;<wbr>ArchB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>864&nbsp;<wbr>&nbsp;<wbr>1296<br />
&nbsp;<wbr>&nbsp;<wbr>ArchA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>648&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>864<br />
&nbsp;<wbr>&nbsp;<wbr>A0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2380&nbsp;<wbr>&nbsp;<wbr>3368<br />
&nbsp;<wbr>&nbsp;<wbr>A1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1684&nbsp;<wbr>&nbsp;<wbr>2380<br />
&nbsp;<wbr>&nbsp;<wbr>A2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1190&nbsp;<wbr>&nbsp;<wbr>1684<br />
&nbsp;<wbr>&nbsp;<wbr>A3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>842&nbsp;<wbr>&nbsp;<wbr>1190<br />
&nbsp;<wbr>&nbsp;<wbr>A4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>595&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>842<br />
&nbsp;<wbr>&nbsp;<wbr>A4Small&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>595&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>842<br />
&nbsp;<wbr>&nbsp;<wbr>A5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>421&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>595<br />
&nbsp;<wbr>&nbsp;<wbr>A6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>297&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>421<br />
&nbsp;<wbr>&nbsp;<wbr>A7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>210&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>297<br />
&nbsp;<wbr>&nbsp;<wbr>A8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>148&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>210<br />
&nbsp;<wbr>&nbsp;<wbr>A9&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>105&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>148<br />
&nbsp;<wbr>&nbsp;<wbr>A10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>74&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>105<br />
&nbsp;<wbr>&nbsp;<wbr>B0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2836&nbsp;<wbr>&nbsp;<wbr>4008<br />
&nbsp;<wbr>&nbsp;<wbr>B1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2004&nbsp;<wbr>&nbsp;<wbr>2836<br />
&nbsp;<wbr>&nbsp;<wbr>B2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1418&nbsp;<wbr>&nbsp;<wbr>2004<br />
&nbsp;<wbr>&nbsp;<wbr>B3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1002&nbsp;<wbr>&nbsp;<wbr>1418<br />
&nbsp;<wbr>&nbsp;<wbr>B4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>709&nbsp;<wbr>&nbsp;<wbr>1002<br />
&nbsp;<wbr>&nbsp;<wbr>B5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>501&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>709<br />
&nbsp;<wbr>&nbsp;<wbr>C0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2600&nbsp;<wbr>&nbsp;<wbr>3677<br />
&nbsp;<wbr>&nbsp;<wbr>C1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1837&nbsp;<wbr>&nbsp;<wbr>2600<br />
&nbsp;<wbr>&nbsp;<wbr>C2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1298&nbsp;<wbr>&nbsp;<wbr>1837<br />
&nbsp;<wbr>&nbsp;<wbr>C3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>918&nbsp;<wbr>&nbsp;<wbr>1298<br />
&nbsp;<wbr>&nbsp;<wbr>C4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>649&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>918<br />
&nbsp;<wbr>&nbsp;<wbr>C5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>459&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>649<br />
&nbsp;<wbr>&nbsp;<wbr>C6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>323&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>459<br />
&nbsp;<wbr>&nbsp;<wbr>Flsa&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>612&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>936<br />
&nbsp;<wbr>&nbsp;<wbr>Flse&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>612&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>936<br />
&nbsp;<wbr>&nbsp;<wbr>HalfLetter&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>396&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>612 </p>
<p> For convenience you can specify the page size by media (e.g. A4, Ledger, etc.). Otherwise, <code>-page</code> behaves much like <code>-geometry</code> (e.g. -page letter+43+43&gt;). </p>
<p> This option is also used to place subimages when writing to a multi-image format that supports offsets, such as GIF89 and MNG. When used for this purpose the offsets are always measured from the top left corner of the canvas and are not affected by the <code>-gravity</code> option. To position a GIF or MNG image, use <code>-page</code><i>{+-}&lt;x&gt;{+-}&lt;y&gt;</i> (e.g. -page +100+200). When writing to a MNG file, a <code>-page</code> option appearing ahead of the first image in the sequence with nonzero width and height defines the width and height values that are written in the <code>MHDR</code> chunk. Otherwise, the MNG width and height are computed from the bounding box that contains all images in the sequence. When writing a GIF89 file, only the bounding box method is used to determine its dimensions. </p>
<p> For a PostScript page, the image is sized as in <code>-geometry</code> and positioned relative to the lower left hand corner of the page by {+-}&lt;<code>x</code><i>offset</i>&gt;{+-}&lt;<code>y</code> <i>offset&gt;</i>. Use -page 612&#215;792&gt;, for example, to center the image within the page. If the image size exceeds the PostScript page, it is reduced to fit the page. The default gravity for the <code>-page</code> option is <i>NorthWest</i>, i.e., positive <code>x</code> and <code>y</code> <i>offset</i> are measured rightward and downward from the top left corner of the page, unless the <code>-gravity</code> option is present with a value other than <i>NorthWest</i>. </p>
<p> The default page dimensions for a TEXT image is 612&#215;792. </p>
<p> This option is used in concert with <code>-density</code>. </p>
<p> Use <code>+page</code> to remove the page settings for an image.</p>
<dt><code>-paint </code><i>&lt;radius&gt;</i></p>
<dd> simulate an oil painting </p>
<p> Each pixel is replaced by the most frequent color in a circular neighborhood whose width is specified with <i>radius</i>.</p>
<dt><code>-pause </code><i>&lt;seconds&gt;</i></p>
<dd> pause between animation loops [animate] </p>
<p> Pause for the specified number of seconds before repeating the animation.</p>
<dt><code>-pause </code><i>&lt;seconds&gt;</i></p>
<dd> pause between snapshots [import] </p>
<p> Pause for the specified number of seconds before taking the next snapshot.</p>
<dt><code>-pen </code><i>&lt;color&gt;</i></p>
<dd> (This option has been replaced by the -fill option)</p>
<dt><code>-ping</code></p>
<dd> efficiently determine image characteristics </p>
<p> Use this option to disable reading the image pixels so that image characteristics such as the image dimensions may be obtained very quickly. For identify, use +ping to force reading the image pixels so that the pixel read rate may be included in the displayed information.</p>
<dt><code>-pointsize </code><i>&lt;value&gt;</i></p>
<dd> pointsize of the PostScript, X11, or TrueType font</p>
<dt><code>-preview </code><i>&lt;type&gt;</i></p>
<dd> image preview type </p>
<p> Use this option to affect the preview operation of an image (e.g. convert file.png -preview Gamma Preview:gamma.png). Choose from these previews: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Rotate<br />
&nbsp;<wbr>&nbsp;<wbr>Shear<br />
&nbsp;<wbr>&nbsp;<wbr>Roll<br />
&nbsp;<wbr>&nbsp;<wbr>Hue<br />
&nbsp;<wbr>&nbsp;<wbr>Saturation<br />
&nbsp;<wbr>&nbsp;<wbr>Brightness<br />
&nbsp;<wbr>&nbsp;<wbr>Gamma<br />
&nbsp;<wbr>&nbsp;<wbr>Spiff<br />
&nbsp;<wbr>&nbsp;<wbr>Dull<br />
&nbsp;<wbr>&nbsp;<wbr>Grayscale<br />
&nbsp;<wbr>&nbsp;<wbr>Quantize<br />
&nbsp;<wbr>&nbsp;<wbr>Despeckle<br />
&nbsp;<wbr>&nbsp;<wbr>ReduceNoise<br />
&nbsp;<wbr>&nbsp;<wbr>AddNoise<br />
&nbsp;<wbr>&nbsp;<wbr>Sharpen<br />
&nbsp;<wbr>&nbsp;<wbr>Blur<br />
&nbsp;<wbr>&nbsp;<wbr>Threshold<br />
&nbsp;<wbr>&nbsp;<wbr>EdgeDetect<br />
&nbsp;<wbr>&nbsp;<wbr>Spread<br />
&nbsp;<wbr>&nbsp;<wbr>Shade<br />
&nbsp;<wbr>&nbsp;<wbr>Raise<br />
&nbsp;<wbr>&nbsp;<wbr>Segment<br />
&nbsp;<wbr>&nbsp;<wbr>Solarize<br />
&nbsp;<wbr>&nbsp;<wbr>Swirl<br />
&nbsp;<wbr>&nbsp;<wbr>Implode<br />
&nbsp;<wbr>&nbsp;<wbr>Wave<br />
&nbsp;<wbr>&nbsp;<wbr>OilPaint<br />
&nbsp;<wbr>&nbsp;<wbr>CharcoalDrawing<br />
&nbsp;<wbr>&nbsp;<wbr>JPEG </p>
<p> The default preview is <code>JPEG</code>.</p>
<dt><code>-process </code><i>&lt;command&gt;</i></p>
<dd> process a sequence of images using a process module </p>
<p> The command argument has the form <code>module=arg1,arg2,arg3,&#8230;,argN</code> where <code>module</code> is the name of the module to invoke (e.g. &quot;analyze&quot;) and arg1,arg2,arg3,&#8230;,argN are an arbitrary number of arguments to pass to the process module. The sequence of images is terminated by the appearance of any option. </p>
<p> If the <code>-process</code> option appears after all of the input images, all images are processed.</p>
<dt><code>-profile </code><i>&lt;filename&gt;</i></p>
<dd> add ICM, IPTC, or generic profile to image </p>
<p> -profile filename adds an ICM (ICC color management), IPTC (newswire information), or a generic (including Exif) profile to the image </p>
<p> Use +profile icm, +profile iptc, or +profile profile_name to remove the respective profile. Multiple profiles may be listed, separated by commas. Profiles may be excluded from subsequent listed matches by preceding their name with an exclamation point. For example, +profile &#8216;!icm,*&#8217; strips all profiles except for the ICM profile. Use identify -verbose to find out what profiles are in the image file. Use +profile &quot;*&quot; to remove all profiles. Writing the image to a format that does not support profiles will of course also cause all profiles to be removed. The JPEG and PNG formats will store any profiles that have been read and not removed. In JPEG they are stored in APP1 markers, and in PNG they are stored as hex-coded binary in compressed zTXt chunks, except for the iCC chunk which is stored in the iCCP chunk. </p>
<p> To extract a profile, the <code>-profile</code> option is not used. Instead, simply write the file to an image format such as <i>APP1, 8BIM, ICM,</i> or <i>IPTC</i>. </p>
<p> For example, to extract the Exif data (which is stored in JPEG files in the <i>APP1</i> profile), use </p>
<p>&nbsp;<wbr>gm convert cockatoo.jpg exifdata.app1 </p>
<p> Note that GraphicsMagick does not attempt to update any profile to reflect changes made to the image, e.g., rotation from portrait to landscape orientation, so it is possible that the preserved profile may contain invalid data.</p>
<dt><code>-preserve-timestamp</code></p>
<dd> preserve the original timestamps of the file </p>
<p> Use this option to preserve the original modification and access timestamps of the file, even if it has been modified.</p>
<dt><code>+progress</code></p>
<dd> disable progress monitor and busy cursor </p>
<p> By default, when an image is displayed, a progress monitor bar is shown in the top left corner of an existing image display window, and the current cursor is replaced with an hourglass cursor. Use <code>+progress</code> to disable the progress monitor and busy cursor during display operations. While the progress monitor is disabled for all operations, the busy cursor continues to be enabled for non-display operations such as image processing. This option is useful for non-interactive display operations, or when a &quot;clean&quot; look is desired.</p>
<dt><code>-quality </code><i>&lt;value&gt;</i></p>
<dd> JPEG/MIFF/PNG/TIFF compression level<br />
&nbsp;<wbr>For the JPEG and MPEG image formats, quality is 0&nbsp;<wbr>(lowest image quality and highest compression) to 100 (best quality but least effective compression). The default quality is 75. Use the <code>-sampling-factor</code> option to specify the factors for chroma downsampling. To use the same quality value as that found by the JPEG decoder, use the -define jpeg:preserve-settings flag. </p>
<p> For the MIFF image format, and the TIFF format while using ZIP compression, quality/10 is the zlib compression level, which is 0 (worst but fastest compression) to 9 (best but slowest). It has no effect on the image appearance, since the compression is always lossless. </p>
<p> For the JPEG-2000 image format, quality is mapped using a non-linear equation to the compression ratio required by the Jasper library. This non-linear equation is intended to loosely approximate the quality provided by the JPEG v1 format. The default quality value 75 results in a request for 16:1 compression. The quality value 100 results in a request for non-lossy compression. </p>
<p> For the MNG and PNG image formats, the quality value sets the zlib compression level (quality / 10) and filter-type (quality % 10). Compression levels range from 0 (fastest compression) to 100 (best but slowest). For compression level 0, the Huffman-only strategy is used, which is fastest but not necessarily the worst compression. </p>
<p> If filter-type is 4 or less, the specified filter-type is used for all scanlines: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>0: none<br />
&nbsp;<wbr>&nbsp;<wbr>1: sub<br />
&nbsp;<wbr>&nbsp;<wbr>2: up<br />
&nbsp;<wbr>&nbsp;<wbr>3: average<br />
&nbsp;<wbr>&nbsp;<wbr>4: Paeth </p>
<p> If filter-type is 5, adaptive filtering is used when quality is greater than 50 and the image does not have a color map, otherwise no filtering is used. </p>
<p> If filter-type is 6, adaptive filtering with <i>minimum-sum-of-absolute-values</i> is used. </p>
<p> Only if the output is MNG, if filter-type is 7, the LOCO color transformation and adaptive filtering with <i>minimum-sum-of-absolute-values</i> are used. </p>
<p> The default is quality is 75, which means nearly the best compression with adaptive filtering. The quality setting has no effect on the appearance of PNG and MNG images, since the compression is always lossless. </p>
<p> For further information, see the PNG specification. </p>
<p> When writing a JNG image with transparency, two quality values are required, one for the main image and one for the grayscale image that conveys the opacity channel. These are written as a single integer equal to the main image quality plus 1000 times the opacity quality. For example, if you want to use quality 75 for the main image and quality 90 to compress the opacity data, use -quality 90075. </p>
<p> For the PNM family of formats (PNM, PGM, and PPM) specify a quality factor of zero in order to obtain the ASCII variant of the format. Note that -compress <i>none</i> used to be used to trigger ASCII output but provided the opposite result of what was expected as compared with other formats.</p>
<dt><code>-raise </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> lighten or darken image edges </p>
<p> This will create a 3-D effect. See <code>-geometry</code> for details details about the geometry specification. Offsets are not used. </p>
<p> Use <code>-raise</code> to create a raised effect, otherwise use <code>+raise</code>.</p>
<dt><code>-random-threshold </code><i>&lt;channeltype&gt; &lt;LOWxHIGH&gt;</i></p>
<dd> random threshold the image </p>
<p> The channel or channels specified in the &lt;channeltype&gt; argument are reduced to binary, using an random-threshold method. The choices for <code>channeltype</code> are <code>All</code>, <code>Intensity</code>, <code>Red</code>, <code>Green</code>, <code>Blue</code>, <code>Cyan</code>, <code>Magenta</code>, <code>Yellow</code>, <code>Black</code>, and <code>Opacity</code> </p>
<p> When <code>channeltype</code> is &quot;All&quot;, the color samples are thresholded into a graylevel and then that gray level is stored in the three color channels. Separately, the opacity channel is thresholded into a bilevel opacity value which is stored in the opacity channel. For each pixel, a new random number is used to establish the threshold to be used. The threshold never exceeds the specified maximum (HIGH) and is never less than the specified minimum (LOW). </p>
<p> When <code>channeltype</code> is &quot;intensity&quot;, only the color samples are thresholded. When <code>channeltype</code> is &quot;opacity&quot; or &quot;matte&quot;, only the opacity channel is thresholded. The other named channels only threshold the associated channel.</p>
<dt><code>-recolor </code><i>&lt;matrix&gt;</i></p>
<dd> apply a color translation matrix to image channels </p>
<p> A user supplied color translation matrix (expressed as a text string) is used to translate/blend the image channels based on weightings in a supplied matrix which may be of order 3 (color channels only), 4 (color channels plus opacity), or 5 (color channels plus opacity and offset). Values in the columns of the matrix (red, green, blue, opacity) are used as multipliers with the existing channel values and added together according to the rows of the matrix. Matrix values are floating point and may be negative. The offset column (column 5) is purely additive and is scaled such that 0.0 to 1.0 represents the maximum quantum range (but values are not limited to this range). The math for the color translation matrix is similar to that used by Adobe Flash except that the offset is scaled to 1.0 (divide Flash offset by 255 for use with GraphicsMagick) so that the results are independent of quantum depth. </p>
<p> An <code>identity</code> matrix exists for each matrix order which results in no change to the image. The translation matrix should be based on an alteration of the identity matrix. </p>
<p> Identity matrix of order 3 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>1 0 0<br />
&nbsp;<wbr>&nbsp;<wbr>0 1 0<br />
&nbsp;<wbr>&nbsp;<wbr>0 0 1 </p>
<p> which may be formatted into a convenient matrix argument similar to (comma is treated as white space): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-recolor&nbsp;<wbr>&quot;1 0 0, 0 1 0, 0 0 1&quot; </p>
<p> Identity matrix of order 4 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>1 0 0 0<br />
&nbsp;<wbr>&nbsp;<wbr>0 1 0 0<br />
&nbsp;<wbr>&nbsp;<wbr>0 0 1 0<br />
&nbsp;<wbr>&nbsp;<wbr>0 0 0 1 </p>
<p> Identity matrix of order 5. The last row is required to exist for the purpose of parsing, but is otherwise not used. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>1 0 0 0 0<br />
&nbsp;<wbr>&nbsp;<wbr>0 1 0 0 0<br />
&nbsp;<wbr>&nbsp;<wbr>0 0 1 0 0<br />
&nbsp;<wbr>&nbsp;<wbr>0 0 0 1 0<br />
&nbsp;<wbr>&nbsp;<wbr>0 0 0 0 1 </p>
<p> As an example, an image wrongly in BGR channel order may be converted to RGB using this matrix (blue-&gt;red, red-&gt;blue): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>0 0 1<br />
&nbsp;<wbr>&nbsp;<wbr>0 1 0<br />
&nbsp;<wbr>&nbsp;<wbr>1 0 0 </p>
<p> and an RGB image using standard Rec.709 primaries may be converted to grayscale using this matrix of standard weighting factors: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>0.2126 0.7152 0.0722<br />
&nbsp;<wbr>&nbsp;<wbr>0.2126 0.7152 0.0722<br />
&nbsp;<wbr>&nbsp;<wbr>0.2126 0.7152 0.0722 </p>
<p> and contrast may be reduced by scaling down by 80% and adding a 10% offset: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>0.8 0.0 0.0 0.0 0.1<br />
&nbsp;<wbr>&nbsp;<wbr>0.0 0.8 0.0 0.0 0.1<br />
&nbsp;<wbr>&nbsp;<wbr>0.0 0.0 0.8 0.0 0.1<br />
&nbsp;<wbr>&nbsp;<wbr>0.0 0.0 0.0 0.8 0.1<br />
&nbsp;<wbr>&nbsp;<wbr>0.0 0.0 0.0 0.0 1.0 </p>
<dt><code>-red-primary </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> red chromaticity primary point</p>
<dt><code>-region </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;</i></p>
<dd> apply options to a portion of the image </p>
<p> The <i>x</i> and <i>y</i> offsets are treated in the same manner as in <code>-crop</code>.</p>
<dt><code>-remote</code></p>
<dd> perform a X11 remote operation </p>
<p> The <code>-remote</code> command sends a command to a &quot;gm display&quot; or &quot;gm animate&quot; which is already running. The only command recognized at this time is the name of an image file to load. This capability is very useful to load new images without needing to restart GraphicsMagick (e.g. for a slide-show or to use GraphicsMagick as the display engine for a different GUI). Also see the <code>+progress</code> option for a way to disable progress indication for a clean look while loading new images.</p>
<dt><code>-render</code></p>
<dd> render vector operations </p>
<p> Use <code>+render</code> to turn off rendering vector operations. This is useful when saving the result to vector formats such as MVG or SVG.</p>
<dt><code>-repage </code><i> &lt;width&gt;x&lt;height&gt;+xoff+yoff[!]</i></p>
<dd> Adjust image page offsets </p>
<p> Adjust the current image page canvas and position based on a relative page specification. This option may be used to change the location of a subframe (e.g. part of an animation) prior to composition. If the geometry specification is absolute (includes a &#8216;!&#8217;), then the offset adjustment is absolute and there is no adjustment to page width and height, otherwise the page width and height values are also adjusted based on the current image dimensions. Use <code>+repage</code> to set the image page offsets to default.</p>
<dt><code>-resample </code><i>&lt;horizontal&gt;x&lt;vertical&gt;</i></p>
<dd> Resample image to specified horizontal and vertical resolution </p>
<p> Resize the image so that its rendered size remains the same as the original at the specified target resolution. Either the current image resolution units or the previously set with <code>-units</code> are used to interpret the argument. For example, if a 300 DPI image renders at 3 inches by 2 inches on a 300 DPI device, when the image has been resampled to 72 DPI, it will render at 3 inches by 2 inches on a 72 DPI device. Note that only a small number of image formats (e.g. JPEG, PNG, and TIFF) are capable of storing the image resolution. For formats which do not support an image resolution, the original resolution of the image must be specified via <code>-density</code> on the command line prior to specifying the resample resolution. </p>
<p> Note that Photoshop stores and obtains image resolution from a proprietary embedded profile. If this profile exists in the image, then Photoshop will continue to treat the image using its former resolution, ignoring the image resolution specified in the standard file header. </p>
<p> Some image formats (e.g. PNG) require use of metric or english units so even if the original image used a particular unit system, if it is saved to a different format prior to resampling, then it may be necessary to specify the desired resolution units using <code>-units</code> since the original units may have been lost. In other words, do not assume that the resolution units are restored if the image has been saved to a file.</p>
<dt><code>-resize </code><i>&lt;width&gt;x&lt;height&gt;{%}{@}{!}{&lt;}{&gt;}</i></p>
<dd> resize an image </p>
<p> This is an alias for the <code>-geometry</code> option and it behaves in the same manner. If the <code>-filter</code> option precedes the <code>-resize</code> option, the specified filter is used. </p>
<p> There are some exceptions: </p>
<p> When used as a <i>composite</i> option, <code>-resize</code> conveys the preferred size of the output image, while <code>-geometry</code> conveys the size and placement of the <i>composite image</i> within the main image. </p>
<p> When used as a <i>montage</i> option, <code>-resize</code> conveys the preferred size of the montage, while <code>-geometry</code> conveys information about the tiles.</p>
<dt><code>-roll </code><i>{+-}&lt;x&gt;{+-}&lt;y&gt;</i></p>
<dd> roll an image vertically or horizontally </p>
<p> See <code>-geometry</code> for details the geometry specification. The <i>x</i> and <i>y</i> offsets are not affected by the <code>-gravity</code> option. </p>
<p> A negative <i>x</i> offset rolls the image left-to-right. A negative <i>y</i> offset rolls the image top-to-bottom.</p>
<dt><code>-rotate </code><i>&lt;degrees&gt;{&lt;}{&gt;}</i></p>
<dd> rotate the image </p>
<p> Positive angles rotate the image in a clockwise direction while negative angles rotate counter-clockwise. </p>
<p> Use &gt; to rotate the image only if its width exceeds the height. &lt; rotates the image <i>only</i> if its width is less than the height. For example, if you specify -rotate &quot;-90&gt;&quot; and the image size is 480&#215;640, the image is not rotated. However, if the image is 640&#215;480, it is rotated by -90 degrees. If you use &gt; or &lt;, enclose it in quotation marks to prevent it from being misinterpreted as a file redirection. </p>
<p> Empty triangles left over from rotating the image are filled with the color defined as <code>background</code> (class <code>backgroundColor</code>). The color is specified using the format described under the <code>-fill</code> option.</p>
<dt><code>-sample </code><i>&lt;geometry&gt;</i></p>
<dd> scale image using pixel sampling </p>
<p> See <code>-geometry</code> for details about the geometry specification. <code>-sample</code> ignores the <code>-filter</code> selection if the <code>-filter</code> option is present. Offsets, if present in the geometry string, are ignored, and the <code>-gravity</code> option has no effect.</p>
<dt><code>-sampling-factor </code><i>&lt;horizontal_factor&gt;x&lt;vertical_factor&gt;</i></p>
<dd> chroma subsampling factors </p>
<p> This option specifies the sampling factors to be used by the DPX, JPEG, MPEG, or YUV encoders for chroma downsampling. The sampling factor must be specified while reading the raw YUV format since it is not preserved in the file header. Industry-standard video subsampling notation such as &quot;4:2:2&quot; may also be used to specify the sampling factors. &quot;4:2:2&quot; is equivalent to a specification of &quot;2&#215;1&quot; </p>
<p> The JPEG decoder obtains the original sampling factors (and quality settings) when a JPEG file is read. To re-use the original sampling factors (and quality setting) when JPEG is output, use the -define jpeg:preserve-settings flag.</p>
<dt><code>-scale </code><i>&lt;geometry&gt;</i></p>
<dd> scale the image. </p>
<p> See <code>-geometry</code> for details about the geometry specification. <code>-scale</code> uses a simpler, faster algorithm, and it ignores the <code>-filter</code> selection if the <code>-filter</code> option is present. Offsets, if present in the geometry string, are ignored, and the <code>-gravity</code> option has no effect.</p>
<dt><code>-scene </code><i>&lt;value&gt;</i></p>
<dd> set scene number </p>
<p> This option sets the scene number of an image or the first image in an image sequence.</p>
<dt><code>-scenes </code><i>&lt;value-value&gt;</i></p>
<dd> range of image scene numbers to read </p>
<p> Each image in the range is read with the filename followed by a period (<code>.</code>) and the decimal scene number. You can change this behavior by embedding a <code>%d, %0Nd, %o, %0No, %x, or %0Nx printf</code> format specification in the file name. For example, </p>
<p>&nbsp;<wbr>gm montage -scenes 5-7 image.miff montage.miff </p>
<p> makes a montage of files image.miff.5, image.miff.6, and image.miff.7, and </p>
<p>&nbsp;<wbr>gm animate -scenes 0-12 image%02d.miff </p>
<p> animates files image00.miff, image01.miff, through image12.miff.</p>
<dt><code>-screen</code></p>
<dd> specify the screen to capture </p>
<p> This option indicates that the GetImage request used to obtain the image should be done on the root window, rather than directly on the specified window. In this way, you can obtain pieces of other windows that overlap the specified window, and more importantly, you can capture menus or other popups that are independent windows but appear over the specified window.</p>
<dt><code>-set </code><i>&lt;attribute&gt; &lt;value&gt;</i></p>
<dd> set an image attribute </p>
<p> Set a named image attribute. The attribute is set on the current (previously specified on command line) image.</p>
<dt><code>+set </code><i>&lt;attribute&gt;</i></p>
<dd> unset an image attribute </p>
<p> Unset a named image attribute. The attribute is removed from the current (previously specified on command line) image.</p>
<dt><code>-segment </code><i>&lt;cluster threshold&gt;x&lt;smoothing threshold&gt;</i></p>
<dd> segment an image </p>
<p> Segment an image by analyzing the histograms of the color components and identifying units that are homogeneous with the fuzzy c-means technique. </p>
<p> Segmentation is a very useful fast and and approximate color quantization algorithm for scanned printed pages or scanned cartoons. It may also be used as a special effect. Specify <i>cluster threshold</i> as the minimum percentage of total pixels in a cluster before it is considered valid. For huge images containing small detail, this may need to be a tiny fraction of a percent (e.g. 0.015) so that important detail is not lost. <i>Smoothing threshold</i> eliminates noise in the second derivative of the histogram. As the value is increased, you can expect a smoother second derivative. The default is 1.5. Add the <i>-verbose</i> option to see a dump of cluster statistics given the parameters used. The statistics may be used as a guide to help fine tune the options.</p>
<dt><code>-shade </code><i>&lt;azimuth&gt;x&lt;elevation&gt;</i></p>
<dd> shade the image using a distant light source </p>
<p> Specify <i>azimuth</i> and <i>elevation</i> as the position of the light source. Use <code>+shade</code> to return the shading results as a grayscale image.</p>
<dt><code>-shadow </code><i>&lt;radius&gt;{x&lt;sigma&gt;}</i></p>
<dd> shadow the montage</p>
<dt><code>-shared-memory</code></p>
<dd> use shared memory </p>
<p> This option specifies whether the utility should attempt to use shared memory for pixmaps. GraphicsMagick must be compiled with shared memory support, and the display must support the <i>MIT-SHM</i> extension. Otherwise, this option is ignored. The default is <code>True</code>.</p>
<dt><code>-sharpen </code><i>&lt;radius&gt;{x&lt;sigma&gt;}</i></p>
<dd> sharpen the image </p>
<p> Use a Gaussian operator of the given radius and standard deviation (sigma).</p>
<dt><code>-shave </code><i>&lt;width&gt;x&lt;height&gt;{%}</i></p>
<dd> shave pixels from the image edges </p>
<p> Specify the width of the region to be removed from both sides of the image and the height of the regions to be removed from top and bottom.</p>
<dt><code>-shear </code><i>&lt;x degrees&gt;x&lt;y degrees&gt;</i></p>
<dd> shear the image along the X or Y axis </p>
<p> Use the specified positive or negative shear angle. </p>
<p> Shearing slides one edge of an image along the X or Y axis, creating a parallelogram. An X direction shear slides an edge along the X axis, while a Y direction shear slides an edge along the Y axis. The amount of the shear is controlled by a shear angle. For X direction shears, <i>x degrees</i> is measured relative to the Y axis, and similarly, for Y direction shears <i>y degrees</i> is measured relative to the X axis. </p>
<p> Empty triangles left over from shearing the image are filled with the color defined as <code>background</code> (class <code>backgroundColor</code>). The color is specified using the format described under the <code>-fill</code> option.</p>
<dt><code>-silent</code></p>
<dd> operate silently</p>
<dt><code>-size </code><i>&lt;width&gt;x&lt;height&gt;{+offset}</i></p>
<dd> width and height of the image </p>
<p> Use this option to specify the width and height of raw images whose dimensions are unknown such as <code>GRAY</code>, <code>RGB</code>, or <code>CMYK</code>. In addition to width and height, use <code>-size</code> with an offset to skip any header information in the image or tell the number of colors in a <code>MAP</code> image file, (e.g. -size 640&#215;512+256). </p>
<p> For Photo CD images, choose from these sizes: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>192&#215;128<br />
&nbsp;<wbr>&nbsp;<wbr>384&#215;256<br />
&nbsp;<wbr>&nbsp;<wbr>768&#215;512<br />
&nbsp;<wbr>&nbsp;<wbr>1536&#215;1024<br />
&nbsp;<wbr>&nbsp;<wbr>3072&#215;2048 </p>
<p> Finally, use this option to choose a particular resolution layer of a JBIG or JPEG image (e.g. -size 1024&#215;768).</p>
<dt><code>-snaps </code><i>&lt;value&gt;</i></p>
<dd> number of screen snapshots </p>
<p> Use this option to grab more than one image from the X server screen, to create an animation sequence.</p>
<dt><code>-solarize </code><i>&lt;factor&gt;</i></p>
<dd> negate all pixels above the threshold level </p>
<p> Specify <i>factor</i> as the percent threshold of the intensity (0 &#8211; 99.9%). </p>
<p> This option produces a <i>solarization</i> effect seen when exposing a photographic film to light during the development process.</p>
<dt><code>-spread </code><i>&lt;amount&gt;</i></p>
<dd> displace image pixels by a random amount </p>
<p> <i>Amount</i> defines the size of the neighborhood around each pixel to choose a candidate pixel to swap.</p>
<dt><code>-stegano </code><i>&lt;offset&gt;</i></p>
<dd> hide watermark within an image </p>
<p> Use an offset to start the image hiding some number of pixels from the beginning of the image. Note this offset and the image size. You will need this information to recover the steganographic image (e.g. display -size 320&#215;256+35 stegano:image.png).</p>
<dt><code>-stereo</code></p>
<dd> composite two images to create a stereo anaglyph </p>
<p> The left side of the stereo pair is saved as the red channel of the output image. The right side is saved as the green channel. Red-green stereo glasses are required to properly view the stereo image.</p>
<dt><code>-strip</code></p>
<dd> remove all profiles and text attributes from the image </p>
<p> All embedded profiles and text attributes are stripped from the image. This is useful for images used for the web, or when output files need to be as small as possible </p>
<p> Be careful not to use this option to remove author, copyright, and license information that you are required to retain when redistributing an image.</p>
<dt><code>-stroke </code><i>&lt;color&gt;</i></p>
<dd> color to use when stroking a graphic primitive </p>
<p> The color is specified using the format described under the <code>-fill</code> option. </p>
<p> See <code>-draw</code> for further details.</p>
<dt><code>-strokewidth </code><i>&lt;value&gt;</i></p>
<dd> set the stroke width </p>
<p> See <code>-draw</code> for further details.</p>
<dt><code>-swirl </code><i>&lt;degrees&gt;</i></p>
<dd> swirl image pixels about the center </p>
<p> <i>Degrees</i> defines the tightness of the swirl.</p>
<dt><code>-text-font </code><i>&lt;name&gt;</i></p>
<dd> font for writing fixed-width text </p>
<p> Specifies the name of the preferred font to use in fixed (typewriter style) formatted text. The default is 14 point <i>Courier</i>. </p>
<p> You can tag a font to specify whether it is a PostScript, TrueType, or X11 font. For example, Courier.ttf is a TrueType font and x:fixed is X11.</p>
<dt><code>-texture </code><i>&lt;filename&gt;</i></p>
<dd> name of texture to tile onto the image background</p>
<dt><code>-threshold </code><i>&lt;value&gt;{%}</i></p>
<dd> threshold the image </p>
<p> Modify the image such that any pixel sample with an intensity value greater than the threshold is assigned the maximum intensity (white), or otherwise is assigned the minimum intensity (black). If a percent prefix is applied, then the threshold is a percentage of the available range. </p>
<p> To efficiently create a black and white image from a color image, use </p>
<p>&nbsp;<wbr>gm convert -threshold 50%&nbsp;<wbr>in.png out.png </p>
<p> The optimum threshold value depends on the nature of the image. In order to threshold individual channels, use the <code>-operator</code> subcommand with it&#8217;s <code>Threshold</code>, <code>Threshold-White</code>, or <code>Threshold-Black</code> options.</p>
<dt><code>-thumbnail </code><i>&lt;width&gt;x&lt;height&gt;{%}{@}{!}{&lt;}{&gt;}</i></p>
<dd> resize an image (quickly) </p>
<p> The <code>-thumbnail</code> command resizes the image as quickly as possible, with more concern for speed than resulting image quality. Regardless, resulting image quality should be acceptable for many uses. It is primarily intended to be used to generate smaller versions of the image, but may also be used to enlarge the image. The <code>-thumbnail</code> <code>geometry</code> argument observes the same syntax and rules as it does for <code>-resize</code>.</p>
<dt><code>-tile </code><i>&lt;filename&gt;</i></p>
<dd> tile image when filling a graphic primitive</p>
<dt><code>-tile </code><i>&lt;geometry&gt;</i></p>
<dd> layout of images [<i>montage</i>]</p>
<dt><code>-title </code><i>&lt;string&gt;</i></p>
<dd> assign title to displayed image [<i>animate, display, montage</i>] </p>
<p> Use this option to assign a specific title to the image. This is assigned to the image window and is typically displayed in the window title bar. Optionally you can include the image filename, type, width, height, Exif data, or other image attribute by embedding special format characters described under the <code>-format</code> option. </p>
<p> For example, </p>
<p>&nbsp;<wbr>&nbsp;<wbr>-title&nbsp;<wbr>&quot;%m:%f&nbsp;<wbr>%wx%h&quot; </p>
<p> produces an image title of MIFF:bird.miff 512&#215;480 for an image titled bird.miff and whose width is 512 and height is 480.</p>
<dt><code>-transform</code></p>
<dd> transform the image </p>
<p> This option applies the transformation matrix from a previous <code>-affine</code> option. </p>
<p>&nbsp;<wbr>gm convert -affine 2,2,-2,2,0,0 -transform bird.ppm bird.jpg </p>
<dt><code>-transparent </code><i>&lt;color&gt;</i></p>
<dd> make this color transparent within the image </p>
<p> The color is specified using the format described under the <code>-fill</code> option.</p>
<dt><code>-treedepth </code><i>&lt;value&gt;</i></p>
<dd> tree depth for the color reduction algorithm </p>
<p> Normally, this integer value is zero or one. A value of zero or one causes the use of an optimal tree depth for the color reduction algorithm </p>
<p> An optimal depth generally allows the best representation of the source image with the fastest computational speed and the least amount of memory. However, the default depth is inappropriate for some images. To assure the best representation, try values between 2 and 8 for this parameter. Refer to quantize for more details. </p>
<p> The <code>-colors</code> or <code>-monochrome</code> option, or writing to an image format which requires color reduction, is required for this option to take effect.</p>
<dt><code>-trim</code></p>
<dd> trim an image </p>
<p> This option removes any edges that are exactly the same color as the corner pixels. Use <code>-fuzz</code> to make <code>-trim</code> remove edges that are nearly the same color as the corner pixels.</p>
<dt><code>-type </code><i>&lt;type&gt;</i></p>
<dd> the image type </p>
<p> Choose from: <code>Bilevel</code>, <code>Grayscale</code>, <code>Palette</code>, <code>PaletteMatte</code>, <code>TrueColor</code>, <code>TrueColorMatte</code>, <code>ColorSeparation</code>, <code>ColorSeparationMatte</code>, or <code>Optimize</code>. </p>
<p> Normally, when a format supports different subformats such as bilevel, grayscale, palette, truecolor, and truecolor+alpha, the encoder will try to choose a suitable subformat based on the nature of the image. The <code>-type</code> option may be used to tailor the output subformat. By default the output subformat is based on readily available image information and is usually similar to the input format. </p>
<p> Specify -type Optimize in order to enable inspecting all pixels (if necessary) in order to find the most efficient subformat. Inspecting all of the pixels may be slow for very large images, particularly if they are stored in a disk cache. If an RGB image contains only gray pixels, then every pixel in the image must be inspected in order to decide that the image is actually grayscale! </p>
<p> Sometimes a specific subformat is desired. For example, to force a JPEG image to be written in TrueColor RGB format even though only gray pixels are present, use </p>
<p>&nbsp;<wbr>gm convert bird.pgm -type TrueColor bird.jpg </p>
<p> Similarly, using -type TrueColorMatte will force the encoder to write an alpha channel even though the image is opaque, if the output format supports transparency. </p>
<p> Some pseudo-formats (e.g. the XC format) will respect the requested type if it occurs previously on the command line. For example, to obtain a DirectClass solid color canvas image rather than PsuedoClass, use </p>
<p>&nbsp;<wbr>gm convert -size 640&#215;480 -type TrueColor xc:red red.miff </p>
<p> Likewise, specify <code>-type</code> <code>Bilevel</code>, <code>Grayscale</code>, <code>TrueColor</code>, or <code>TrueColorMatte</code> prior to reading a Postscript (or PDF file) in order to influence the type of image that Ghostcript returns. Reading performance will be dramatically improved for black/white Postscript if <code>Bilevel</code> is specified, and will be considerably faster if <code>Grayscale</code> is specified.</p>
<dt><code>-update </code><i>&lt;seconds&gt;</i></p>
<dd> detect when image file is modified and redisplay. </p>
<p> Suppose that while you are displaying an image the file that is currently displayed is over-written. <code>display</code> will automatically detect that the input file has been changed and update the displayed image accordingly.</p>
<dt><code>-units </code><i>&lt;type&gt;</i></p>
<dd> the units of image resolution </p>
<p> Choose from: <code>Undefined</code>, <code>PixelsPerInch</code>, or <code>PixelsPerCentimeter</code>. This option is normally used in conjunction with the <code>-density</code> option.</p>
<dt><code>-unsharp </code><i>&lt;radius&gt;{x&lt;sigma&gt;}{+&lt;amount&gt;}{+&lt;threshold&gt;}</i></p>
<dd> sharpen the image with an unsharp mask operator </p>
<p> The <code>-unsharp</code> option sharpens an image. The image is convolved with a Gaussian operator of the given radius and standard deviation (sigma). For reasonable results, radius should be larger than sigma. Use a radius of 0 to have the method select a suitable radius. </p>
<p> The parameters are: </p>
<p> <code>radius</code><br />
&nbsp;<wbr> </p>
<p> The radius of the Gaussian, in pixels, not counting the center pixel (default 0). </p>
<p> <code>sigma</code><br />
&nbsp;<wbr> </p>
<p> The standard deviation of the Gaussian, in pixels (default 1.0). </p>
<p> <code>amount</code><br />
&nbsp;<wbr> </p>
<p> The percentage of the difference between the original and the blur image that is added back into the original (default 1.0). </p>
<p> <code>threshold</code><br />
&nbsp;<wbr> </p>
<p> The threshold, as a fraction of MaxRGB, needed to apply the difference amount (default 0.05). </p>
<dt><code>-use-pixmap</code></p>
<dd> use the pixmap</p>
<dt><code>-verbose</code></p>
<dd> print detailed information about the image </p>
<p> This information is printed: image scene number; image name; image size; the image class (<i>DirectClass</i> or <i>PseudoClass</i>); the total number of unique colors; and the number of seconds to read and transform the image. If the image is <i>DirectClass</i>, the total number of unique colors is not displayed unless <code>-verbose</code> is specified twice since it may take quite a long time to compute, particularly for deep images. If the image is <i>PseudoClass</i> then its pixels are defined by indexes into a colormap. If the image is <i>DirectClass</i> then each pixel includes a complete and independent color specification. </p>
<p> If <code>-colors</code> is also specified, the total unique colors in the image and color reduction error values are printed. Refer to quantize for a description of these values.</p>
<dt><code>-version</code></p>
<dd> print GraphicsMagick version string</p>
<dt><code>-view </code><i>&lt;string&gt;</i></p>
<dd> FlashPix viewing parameters</p>
<dt><code>-virtual-pixel </code><i>&lt;method&gt;</i></p>
<dd> specify contents of &quot;virtual pixels&quot; </p>
<p> This option defines &quot;virtual pixels&quot; for use in operations that can access pixels outside the boundaries of an image. </p>
<p> Choose from these methods: </p>
<p> <code>Constant</code><br />
&nbsp;<wbr> </p>
<p> Use the image background color. </p>
<p> <code>Edge</code><br />
&nbsp;<wbr> </p>
<p> Extend the edge pixel toward infinity (default). </p>
<p> <code>Mirror</code><br />
&nbsp;<wbr> </p>
<p> Mirror the image. </p>
<p> <code>Tile</code><br />
&nbsp;<wbr> </p>
<p> Tile the image. </p>
<p> This option affects operations that use virtual pixels such as <code>-blur</code>, <code>-sharpen</code>, <code>-wave</code>, etc.</p>
<dt><code>-visual </code><i>&lt;type&gt;</i></p>
<dd> animate images using this X visual type </p>
<p> Choose from these visual classes: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>StaticGray<br />
&nbsp;<wbr>&nbsp;<wbr>GrayScale<br />
&nbsp;<wbr>&nbsp;<wbr>StaticColor<br />
&nbsp;<wbr>&nbsp;<wbr>PseudoColor<br />
&nbsp;<wbr>&nbsp;<wbr>TrueColor<br />
&nbsp;<wbr>&nbsp;<wbr>DirectColor<br />
&nbsp;<wbr>&nbsp;<wbr>default<br />
&nbsp;<wbr>&nbsp;<wbr>visual id </p>
<p> The X server must support the visual you choose, otherwise an error occurs. If a visual is not specified, the visual class that can display the most simultaneous colors on the default screen is chosen.</p>
<dt><code>-watermark </code><i>&lt;brightness&gt;x&lt;saturation&gt;</i></p>
<dd> percent brightness and saturation of a watermark</p>
<dt><code>-wave </code><i>&lt;amplitude&gt;x&lt;wavelength&gt;</i></p>
<dd> alter an image along a sine wave </p>
<p> Specify <i>amplitude</i> and <i>wavelength</i> of the wave.</p>
<dt><code>-white-point </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> chromaticity white point</p>
<dt><code>-white-threshold </code><i>red[,green][,blue][,opacity]</i></p>
<dd> pixels above the threshold become white </p>
<p> Use <code>-white-threshold</code> to set pixels with values above the specified threshold to maximum value (white). If only one value is supplied, or the red, green, and blue values are identical, then intensity thresholding is used. If the color threshold values are not identical then channel-based thresholding is used, and color distortion will occur. Specify a negative value (e.g. -1) if you want a channel to be ignored but you do want to threshold a channel later in the list. If a percent (%) symbol is appended, then the values are treated as a percentage of maximum range.</p>
<dt><code>-window </code><i>&lt;id&gt;</i></p>
<dd> make image the background of a window </p>
<p> <i>id</i> can be a window id or name. Specify <code>root</code> to select X&#8217;s root window as the target window. </p>
<p> By default the image is tiled onto the background of the target window. If <code>backdrop</code> or <code>-geometry</code> are specified, the image is surrounded by the background color. Refer to <code>X RESOURCES</code> for details. </p>
<p> The image will not display on the root window if the image has more unique colors than the target window colormap allows. Use <code>-colors</code> to reduce the number of colors.</p>
<dt><code>-window-group</code></p>
<dd> specify the window group</p>
<dt><code>-write </code><i>&lt;filename&gt;</i></p>
<dd> write an intermediate image [<i>convert, composite</i>] </p>
<p> The current image is written to the specified filename and then processing continues using that image. The following is an example of how several sizes of an image may be generated in one command (repeat as often as needed): </p>
<p>&nbsp;<wbr>gm convert input.jpg -resize 50%&nbsp;<wbr>-write input50.jpg&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-resize 25%&nbsp;<wbr>input25.jpg </p>
<dt><code>-write </code><i>&lt;filename&gt;</i></p>
<dd> write the image to a file [<i>display</i>] </p>
<p> If <i>filename</i> already exists, you will be prompted as to whether it should be overwritten. </p>
<p> By default, the image is written in the format that it was read in as. To specify a particular image format, prefix <i>filename</i> with the image type and a colon (e.g., ps:image) or specify the image type as the filename suffix (e.g., image.ps). Specify file as &#8211; for standard output. If file has the extension <code>.Z</code> or <code>.gz</code>, the file size is <code>compressed</code> using compress or <code>gzip</code> respectively. Precede the image file name with | to pipe to a system command. </p>
<p> Use <code>-compress</code> to specify the type of image compression. </p>
<p> The equivalent X resource for this option is <code>writeFilename</code> (class <code>WriteFilename</code>). See &quot;X Resources&quot;, below, for details.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>COLUMNS</code></p>
<dd> Output screen width. Used when formatting text for the screen. Many Unix systems keep this shell variable up to date, but it may need to be explicitly exported in order for GraphicsMagick to see it.</p>
<dt><code>DISPLAY</code></p>
<dd> X11 display ID (host, display number, and screen in the form hostname:display.screen).</p>
<dt><code>HOME</code></p>
<dd> Location of user&#8217;s home directory. GraphicsMagick searches for configuration files in $HOME/.magick if the directory exists. See <code>MAGICK_CODER_MODULE_PATH</code>, <code>MAGICK_CONFIGURE_PATH</code>, and <code>MAGICK_FILTER_MODULE_PATH</code> if more flexibility is needed.</p>
<dt><code>MAGICK_ACCESS_MONITOR</code></p>
<dd> When set to <code>TRUE</code>, command line monitor mode (enabled by <code>-monitor</code>) will also show files accessed (including temporary files) and any external commands which are executed. This is useful for debugging, but also illustrates arguments made available to an access handler registered by the <code>MagickSetConfirmAccessHandler()</code> C library function.</p>
<dt><code>MAGICK_CODER_STABILITY</code></p>
<dd> The minimum coder stability level before it will be used. The available levels are <code>PRIMARY</code>, <code>STABLE</code>, <code>UNSTABLE</code>, and <code>BROKEN</code>. The default minimum level is <code>UNSTABLE</code>, which means that all available working coders will be used. The purpose of this option is to reduce the security exposure (or apparent complexity) due to the huge number of formats supported. Coders at the <code>PRIMARY</code> level are commonly used formats with very well maintained implementations. Coders at the <code>STABLE</code> level are reasonably well maintained but represent less used formats. Coders at the <code>UNSTABLE</code> level either have weak implementations, the file format itself is weak, or the probability the coder will be needed is vanishingly small. Coders at the <code>BROKEN</code> level are known to often not work properly or might not be useful in their current state at all.</p>
<dt><code>MAGICK_CODER_MODULE_PATH</code></p>
<dd> Search path to use when searching for image format coder modules. This path allows the user to arbitrarily extend the image formats supported by GraphicsMagick by adding loadable modules to an arbitrary location rather than copying them into the GraphicsMagick installation directory. The formatting of the search path is similar to operating system search paths (i.e. colon delimited for Unix, and semi-colon delimited for Microsoft Windows). This user specified search path is used before trying the default search path.</p>
<dt><code>MAGICK_CONFIGURE_PATH</code></p>
<dd> Search path to use when searching for configuration (.mgk) files. The formatting of the search path is similar to operating system search paths (i.e. colon delimited for Unix, and semi-colon delimited for Microsoft Windows). This user specified search path is used before trying the default search path.</p>
<dt><code>MAGICK_DEBUG</code></p>
<dd> Debug options (see <code>-debug</code> for details). Setting debug options via an environment variable is currently necessary to see the complete initialization process.</p>
<dt><code>MAGICK_FILTER_MODULE_PATH</code></p>
<dd> Search path to use when searching for filter process modules (invoked via <code>-process</code>). This path allows the user to arbitrarily extend GraphicsMagick&#8217;s image processing functionality by adding loadable modules to an arbitrary location rather than copying them into the GraphicsMagick installation directory. The formatting of the search path is similar to operating system search paths (i.e. colon delimited for Unix, and semi-colon delimited for Microsoft Windows). This user specified search path is used before trying the default search path.</p>
<dt><code>MAGICK_GHOSTSCRIPT_PATH</code></p>
<dd> For Microsoft Windows, specify the path to the Ghostscript installation rather than searching for it via the Windows registry. This helps in case Ghostscript is not installed via the Ghostscript Windows installer or the user wants more control over the Ghostscript used.</p>
<dt><code>MAGICK_HOME</code></p>
<dd> Path to top of GraphicsMagick installation directory. Only observed by &quot;uninstalled&quot; builds of GraphicsMagick which do not have their location hard-coded or set by an installer.</p>
<dt><code>MAGICK_MMAP_READ</code></p>
<dd> If <code>MAGICK_MMAP_READ</code> is set to <code>TRUE</code>, GraphicsMagick will attempt to memory-map the input file for reading. This usually substantially improves repeated read performance since the file is already in memory after the first time it has been read. However, testing shows that performance may be reduced for files accessed for the first time since data is accessed via page-faults (upon first access) and many operating systems fail to do sequential read-ahead of memory mapped files, and particularly if those files are accessed over a network. If many large input files are read, then enabling this option may harm performance by overloading the operating system&#8217;s VM system as it then needs to free unmapped pages and map new ones.</p>
<dt><code>MAGICK_IO_FSYNC</code></p>
<dd> If <code>MAGICK_IO_FSYNC</code> is set to <code>TRUE</code>, then GraphicsMagick will request that the output file is fully flushed and synchronized to disk when it is closed. This incurs a performance penalty, but has the benefit that if the power fails or the system crashes, the file should be valid on disk. If image files are referenced from a database, then this option helps assure that the files referenced by the database are valid.</p>
<dt><code>MAGICK_IOBUF_SIZE</code></p>
<dd> The amount of I/O buffering (in bytes) to use when reading and writing encoded files. The default is 16384, which is observed to work well for many cases. The best value for a local filesystem is usually the the native filesystem block size (e.g. 4096, 8192, or even 131,072 for ZFS) in order to minimize the number of physical disk I/O operations. I/O performance to files accessed over a network may benefit significantly by tuning this option. Larger values are not necessarily better (they may be slower!), and there is rarely any benefit from using values larger than 32768. Use convert&#8217;s <code>-verbose</code> option in order to evaluate read and write rates in pixels per second while keeping in mind that the operating system will try to cache files in RAM.</p>
<dt><code>MAGICK_LIMIT_DISK</code></p>
<dd> Maximum amount of disk space allowed for use by the pixel cache.</p>
<dt><code>MAGICK_LIMIT_FILES</code></p>
<dd> Maximum number of open files.</p>
<dt><code>MAGICK_LIMIT_MAP</code></p>
<dd> Maximum size of a memory mapped file allocation. A memory mapped file consumes memory when the file is accessed, although the system may reclaim such memory when needed.</p>
<dt><code>MAGICK_LIMIT_MEMORY</code></p>
<dd> Maximum amount of memory to allocate from the heap.</p>
<dt><code>MAGICK_LIMIT_PIXELS</code></p>
<dd> Maximum number of total pixels (image rows times image colums) to allow for any image which is requested to be created or read. This is useful to place a limit on how large an image may be. If the input image file has image dimensions larger than the pixel limit, then the image memory allocation is denied and an error is returned immediately. This is a per-image limit and does not limit the total number of pixels due to multiple image frames/pages (e.g. multi-page document or an animation).</p>
<dt><code>MAGICK_LIMIT_WIDTH</code></p>
<dd> Maximum pixel width of an image read, or created.</p>
<dt><code>MAGICK_LIMIT_HEIGHT</code></p>
<dd> Maximum pixel height of an image read, or created.</p>
<dt><code>MAGICK_TMPDIR</code></p>
<dd> Path to directory where GraphicsMagick should write temporary files. The default is to use the system default, or the location set by <code>TMPDIR</code>.</p>
<dt><code>TMPDIR</code></p>
<dd> For POSIX-compatible systems (Unix-compatible), the path to the directory where all applications should write temporary files. Overridden by <code>MAGICK_TMPDIR</code> if it is set.</p>
<dt><code>TMP </code><i>or TEMP</i></p>
<dd> For Microsoft Windows, the path to the directory where applications should write temporary files. Overridden by <code>MAGICK_TMPDIR</code> if it is set.</p>
<dt><code>OMP_NUM_THREADS</code></p>
<dd> As per the OpenMP standard, this specifies the number of threads to use in parallel regions. Some compilers default the number of threads to use to the number of processor cores available while others default to just one thread. See the OpenMP specification for other standard adjustments and your compiler&#8217;s manual for vendor-specific settings.</dl>
<h2>CONFIGURATION FILES</h2>
<p> GraphicsMagick uses a number of XML format configuration files:</p>
<dl>
<dt><code>colors.mgk</code></p>
<dd> colors configuration file </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;?xml version=&quot;1.0&quot;?&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;colormap&gt;<br />
&nbsp;<wbr>&lt;color name=&quot;AliceBlue&quot;&nbsp;<wbr>red=&quot;240&quot;&nbsp;<wbr>green=&quot;248&quot;&nbsp;<wbr>blue=&quot;255&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>compliance=&quot;SVG, X11, XPM&quot;&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/colormap&gt; </p>
<dt><code>delegates.mgk</code></p>
<dd> delegates configuration file</p>
<dt><code>log.mgk</code></p>
<dd> logging configuration file </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;?xml version=&quot;1.0&quot;?&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;magicklog&gt;<br />
&nbsp;<wbr>&lt;log events=&quot;None&quot;&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;log output=&quot;stdout&quot;&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;log filename=&quot;Magick-%d.log&quot;&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;log generations=&quot;3&quot;&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;log limit=&quot;2000&quot;&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;log format=&quot;%t&nbsp;<wbr>%r&nbsp;<wbr>%u&nbsp;<wbr>%p&nbsp;<wbr>%m/%f/%l/%d:
&nbsp;<wbr>&nbsp;<wbr>%e&quot;&nbsp;<wbr>&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/magicklog&gt; </p>
<dt><code>modules.mgk</code></p>
<dd> loadable modules configuration file </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;?xml version=&quot;1.0&quot;?&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;modulemap&gt;<br />
&nbsp;<wbr>&lt;module magick=&quot;8BIM&quot;&nbsp;<wbr>name=&quot;META&quot;&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/modulemap&gt; </p>
<dt><code>type.mgk</code></p>
<dd> master type (fonts) configuration file </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;?xml version=&quot;1.0&quot;?&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;typemap&gt;<br />
&nbsp;<wbr>&lt;include file=&quot;type-windows.mgk&quot;&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;type<br />
name=&quot;AvantGarde-Book&quot;<br />
fullname=&quot;AvantGarde Book&quot;<br />
family=&quot;AvantGarde&quot;<br />
foundry=&quot;URW&quot;<br />
weight=&quot;400&quot;<br />
style=&quot;normal&quot;<br />
stretch=&quot;normal&quot;<br />
format=&quot;type1&quot;<br />
metrics=&quot;/usr/local/share/ghostscript/fonts/a010013l.afm&quot;<br />
glyphs=&quot;/usr/local/share/ghostscript/fonts/a010013l.pfb&quot;<br />
&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/typemap&gt; </p>
</dl>
<h2>GM ANIMATE</h2>
<p> <code>Animate</code> displays a sequence of images on any workstation display running an X server. <code>animate</code> first determines the hardware capabilities of the workstation. If the number of unique colors in an image is less than or equal to the number the workstation can support, the image is displayed in an X window. Otherwise the number of colors in the image is first reduced to match the color resolution of the workstation before it is displayed. </p>
<p> This means that a continuous-tone 24 bits-per-pixel image can display on a 8 bit pseudo-color device or monochrome device. In most instances the reduced color image closely resembles the original. Alternatively, a monochrome or pseudo-color image sequence can display on a continuous-tone 24 bits-per-pixel device. </p>
<p> To help prevent color flashing on X server visuals that have colormaps, <code>animate</code> creates a single colormap from the image sequence. This can be rather time consuming. You can speed this operation up by reducing the colors in the image before you &quot;animate&quot; them. Use <code>mogrify</code> to color reduce the images to a single colormap. See <code><a href="/docs/linux/man/1-mogrify/">mogrify</a>(1)</code> for details. Alternatively, you can use a Standard Colormap; or a static, direct, or true color visual. You can define a Standard Colormap with <i>xstdcmap</i>. See <code><a href="/docs/linux/man/1-xstdcmap/">xstdcmap</a>(1)</code> for details. This method is recommended for colormapped X server because it eliminates the need to compute a global colormap.</p>
<h2>EXAMPLES</h2>
<p> To animate a set of images of a cockatoo, use: </p>
<p>&nbsp;<wbr>gm animate cockatoo.* </p>
<p> To animate a cockatoo image sequence while using the Standard Colormap <i>best</i>, use: </p>
<p>&nbsp;<wbr>xstdcmap -best<br />
&nbsp;<wbr>gm animate -map best cockatoo.* </p>
<p> To animate an image of a cockatoo without a border centered on a backdrop, use: </p>
<p>&nbsp;<wbr>gm animate&nbsp;<wbr>+borderwidth -backdrop cockatoo.* </p>
<h2>OPTIONS</h2>
<p> For a more detailed description of each option, see Options, above. </p>
<dl>
<dt><code>-authenticate </code><i>&lt;string&gt;</i></p>
<dd> decrypt image with this password</p>
<dt><code>-backdrop</code></p>
<dd> display the image centered on a backdrop.</p>
<dt><code>-background </code><i>&lt;color&gt;</i></p>
<dd> the background color</p>
<dt><code>-bordercolor </code><i>&lt;color&gt;</i></p>
<dd> the border color</p>
<dt><code>-borderwidth </code><i>&lt;geometry&gt;</i></p>
<dd> the border width</p>
<dt><code>-chop </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}</i></p>
<dd> remove pixels from the interior of an image</p>
<dt><code>-colormap </code><i>&lt;type&gt;</i></p>
<dd> define the colormap type</p>
<dt><code>-colors </code><i>&lt;value&gt;</i></p>
<dd> preferred number of colors in the image</p>
<dt><code>-colorspace </code><i>&lt;value&gt;</i></p>
<dd> the type of colorspace</p>
<dt><code>-crop </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}</i></p>
<dd> preferred size and location of the cropped image</p>
<dt><code>-debug </code><i>&lt;events&gt;</i></p>
<dd> enable debug printout</p>
<dt><code>-define </code><i>&lt;key&gt;{=&lt;value&gt;},&#8230;</i></p>
<dd> add coder/decoder specific options</p>
<dt><code>-delay </code><i>&lt;1/100ths of a second&gt;</i></p>
<dd> display the next image after pausing</p>
<dt><code>-density </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> horizontal and vertical resolution in pixels of the image</p>
<dt><code>-depth </code><i>&lt;value&gt;</i></p>
<dd> depth of the image</p>
<dt><code>-display </code><i>&lt;host:display[.screen]&gt;</i></p>
<dd> specifies the X server to contact</p>
<dt><code>-dispose </code><i>&lt;method&gt;</i></p>
<dd> GIF disposal method</p>
<dt><code>-dither</code></p>
<dd> apply Floyd/Steinberg error diffusion to the image</p>
<dt><code>-font </code><i>&lt;name&gt;</i></p>
<dd> use this font when annotating the image with text</p>
<dt><code>-foreground </code><i>&lt;color&gt;</i></p>
<dd> define the foreground color</p>
<dt><code>-gamma </code><i>&lt;value&gt;</i></p>
<dd> level of gamma correction</p>
<dt><code>-geometry </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}{@}{!}{^}{&lt;}{&gt;}</i></p>
<dd> Specify dimension, offset, and resize options.</p>
<dt><code>-help</code></p>
<dd> print usage instructions</p>
<dt><code>-iconGeometry </code><i>&lt;geometry&gt;</i></p>
<dd> specify the icon geometry</p>
<dt><code>-iconic</code></p>
<dd> iconic animation</p>
<dt><code>-interlace </code><i>&lt;type&gt;</i></p>
<dd> the type of interlacing scheme</p>
<dt><code>-limit </code><i>&lt;type&gt; &lt;value&gt;</i></p>
<dd> Disk, File, Map, Memory, Pixels, Width, Height or Threads resource limit</p>
<dt><code>-log </code><i>&lt;string&gt;</i></p>
<dd> Specify format for debug log</p>
<dt><code>-map </code><i>&lt;type&gt;</i></p>
<dd> display image using this type.</p>
<dt><code>-matte</code></p>
<dd> store matte channel if the image has one</p>
<dt><code>-mattecolor </code><i>&lt;color&gt;</i></p>
<dd> specify the color to be used with the <code>-frame</code> option</p>
<dt><code>-monitor</code></p>
<dd> show progress indication</p>
<dt><code>-monochrome</code></p>
<dd> transform the image to black and white</p>
<dt><code>-name</code></p>
<dd> name an image</p>
<dt><code>-noop</code></p>
<dd> NOOP (no option)</p>
<dt><code>-pause </code><i>&lt;seconds&gt;</i></p>
<dd> pause between animation loops [animate]</p>
<dt><code>-remote</code></p>
<dd> perform a X11 remote operation</p>
<dt><code>-rotate </code><i>&lt;degrees&gt;{&lt;}{&gt;}</i></p>
<dd> rotate the image</p>
<dt><code>-sampling-factor </code><i>&lt;horizontal_factor&gt;x&lt;vertical_factor&gt;</i></p>
<dd> chroma subsampling factors</p>
<dt><code>-scenes </code><i>&lt;value-value&gt;</i></p>
<dd> range of image scene numbers to read</p>
<dt><code>-shared-memory</code></p>
<dd> use shared memory</p>
<dt><code>-size </code><i>&lt;width&gt;x&lt;height&gt;{+offset}</i></p>
<dd> width and height of the image</p>
<dt><code>-text-font </code><i>&lt;name&gt;</i></p>
<dd> font for writing fixed-width text</p>
<dt><code>-title </code><i>&lt;string&gt;</i></p>
<dd> assign title to displayed image [<i>animate, display, montage</i>]</p>
<dt><code>-treedepth </code><i>&lt;value&gt;</i></p>
<dd> tree depth for the color reduction algorithm</p>
<dt><code>-trim</code></p>
<dd> trim an image</p>
<dt><code>-type </code><i>&lt;type&gt;</i></p>
<dd> the image type</p>
<dt><code>-verbose</code></p>
<dd> print detailed information about the image</p>
<dt><code>-version</code></p>
<dd> print GraphicsMagick version string</p>
<dt><code>-visual </code><i>&lt;type&gt;</i></p>
<dd> animate images using this X visual type</p>
<dt><code>-window </code><i>&lt;id&gt;</i></p>
<dd> make image the background of a window </p>
<p> For a more detailed description of each option, see Options, above. </p>
<p> Any option you specify on the command line remains in effect for the group of images following it, until the group is terminated by the appearance of any option or <code>-noop</code>. For example, to animate three images, the first with 32 colors, the second with an unlimited number of colors, and the third with only 16 colors, use: </p>
<p>&nbsp;<wbr>gm animate -colors 32 cockatoo.1 -noop cockatoo.2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-colors 16 cockatoo.3 </p>
<p> <code>Animate</code> options can appear on the command line or in your X resources file. See <i><a href="/docs/linux/man/1-x/">X</a>(1)</i>. Options on the command line supersede values specified in your X resources file. Image filenames may appear in any order on the command line if the image format is <i>MIFF</i> (refer to <code><a href="/docs/linux/man/5-miff/">miff</a>(5)</code> and the <code>scene</code> keyword is specified in the image. Otherwise the images will display in the order they appear on the command line.</dl>
<h2>MOUSE BUTTONS</h2>
<p> Press any button to map or unmap the Command widget. See the next section for more information about the Command widget.</p>
<h2>COMMAND WIDGET</h2>
<p> The Command widget lists a number of sub-menus and commands. They are </p>
<p>&nbsp;<wbr><code>Animate</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Open<br />
&nbsp;<wbr>&nbsp;<wbr>Play<br />
&nbsp;<wbr>&nbsp;<wbr>Step<br />
&nbsp;<wbr>&nbsp;<wbr>Repeat<br />
&nbsp;<wbr>&nbsp;<wbr>Auto Reverse </p>
<p>&nbsp;<wbr><code>Speed</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Faster<br />
&nbsp;<wbr>&nbsp;<wbr>Slower </p>
<p>&nbsp;<wbr><code>Direction</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Forward<br />
&nbsp;<wbr>&nbsp;<wbr>Reverse </p>
<p>&nbsp;<wbr><code>Image Info</code><br />
&nbsp;<wbr><code>Help</code><br />
&nbsp;<wbr><code>Quit</code> </p>
<p> Menu items with a indented triangle have a sub-menu. They are represented above as the indented items. To access a sub-menu item, move the pointer to the appropriate menu and press a button and drag. When you find the desired sub-menu item, release the button and the command is executed. Move the pointer away from the sub-menu if you decide not to execute a particular command.</p>
<h2>KEYBOARD ACCELERATORS</h2>
<p> <code>Ctl+O</code><br />
&nbsp;<wbr> Press to load an image from a file. <code>space</code><br />
&nbsp;<wbr> Press to display the next image in the sequence. <code>&lt;</code><br />
&nbsp;<wbr> Press to speed-up the display of the images. Refer to <code>-delay</code> for more information. <code>&gt;</code><br />
&nbsp;<wbr> Press to slow the display of the images. Refer to <code>-delay</code> for more information. <code>?</code><br />
&nbsp;<wbr> Press to display information about the image. Press any key or button to erase the information. This information is printed: image name; image size; and the total number of unique colors in the image. <code>F1</code><br />
&nbsp;<wbr> Press to display helpful information about <code><a href="/docs/linux/man/1-animate/">animate</a>(1)</code>. <code>Ctl-q</code><br />
&nbsp;<wbr> Press to discard all images and exit program. </p>
<h2>X RESOURCES</h2>
<p> <code>Animate</code> options can appear on the command line or in your X resource file. Options on the command line supersede values specified in your X resource file. See <code><a href="/docs/linux/man/1-x/">X</a>(1)</code> for more information on X resources. </p>
<p> All <code>animate</code> options have a corresponding X resource. In addition, the <code>animate</code> program uses the following X resources: </p>
<p> <code>background</code> <code>(</code><i>class</i> <code>Background)</code><br />
&nbsp;<wbr> </p>
<p> Specifies the preferred color to use for the Image window background. The default is #ccc. <code>borderColor</code> <code>(</code><i>class</i> <code>BorderColor)</code><br />
&nbsp;<wbr> </p>
<p> Specifies the preferred color to use for the Image window border. The default is #ccc. <code>borderWidth</code> <code>(</code><i>class</i> <code>BorderWidth)</code><br />
&nbsp;<wbr> </p>
<p> Specifies the width in pixels of the Image window border. The default is 2. <code>font</code> <code>(</code><i>class</i> <code>Font</code> <code>or</code> <code>FontList)</code><br />
&nbsp;<wbr> </p>
<p> Specifies the name of the preferred font to use in normal formatted text. The default is 14 point <i>Helvetica</i>. <code>foreground</code> <code>(</code><i>class</i> <code>Foreground)</code><br />
&nbsp;<wbr> </p>
<p> Specifies the preferred color to use for text within the Image window. The default is black. <code>geometry</code> <code>(</code><i>class</i> <code>geometry)</code><br />
&nbsp;<wbr> </p>
<p> Specifies the preferred size and position of the image window. It is not necessarily obeyed by all window managers. Offsets, if present, are handled in <i><a href="/docs/linux/man/1-x/">X</a>(1)</i> style. A negative x offset is measured from the right edge of the screen to the right edge of the icon, and a negative y offset is measured from the bottom edge of the screen to the bottom edge of the icon. <code>iconGeometry</code> <code>(</code><i>class</i> <code>IconGeometry)</code><br />
&nbsp;<wbr> </p>
<p> Specifies the preferred size and position of the application when iconified. It is not necessarily obeyed by all window managers. Offsets, if present, are handled in the same manner as in class Geometry. <code>iconic</code> <code>(</code><i>class</i> <code>Iconic)</code><br />
&nbsp;<wbr> </p>
<p> This resource indicates that you would prefer that the application&#8217;s windows initially not be visible as if the windows had be immediately iconified by you. Window managers may choose not to honor the application&#8217;s request. <code>matteColor</code> <code>(</code><i>class</i> <code>MatteColor)</code><br />
&nbsp;<wbr> </p>
<p> Specify the color of windows. It is used for the backgrounds of windows, menus, and notices. A 3D effect is achieved by using highlight and shadow colors derived from this color. Default value: #ddd. <code>name</code> <code>(</code><i>class</i> <code>Name)</code><br />
&nbsp;<wbr> </p>
<p> This resource specifies the name under which resources for the application should be found. This resource is useful in shell aliases to distinguish between invocations of an application, without resorting to creating links to alter the executable file name. The default is the application name. <code>sharedMemory</code> <code>(</code><i>class</i> <code>SharedMemory)</code><br />
&nbsp;<wbr> </p>
<p> This resource specifies whether animate should attempt use shared memory for pixmaps. ImageMagick must be compiled with shared memory support, and the display must support the MIT-SHM extension. Otherwise, this resource is ignored. The default is True. <code>text_font</code> <code>(</code><i>class</i> <code>textFont)</code><br />
&nbsp;<wbr> </p>
<p> Specifies the name of the preferred font to use in fixed (typewriter style) formatted text. The default is 14 point <i>Courier</i>. <code>title</code> <code>(</code><i>class</i> <code>Title)</code><br />
&nbsp;<wbr> </p>
<p> This resource specifies the title to be used for the Image window. This information is sometimes used by a window manager to provide some sort of header identifying the window. The default is the image file name. </p>
<h2>GM BATCH</h2>
<h2>DESCRIPTION</h2>
<p> <code>batch</code> executes an arbitary number of the utility commands (e.g. <code>convert</code>) in the form of a simple linear batch script in order to improve execution efficiency, and/or to allow use as a subordinate co-process under the control of an arbitrary script or program.</p>
<h2>EXAMPLES</h2>
<p>&nbsp;<wbr>To drive&nbsp;<wbr><code>&#8216;gm batch&#8217;</code>&nbsp;<wbr>using a shell script&nbsp;<wbr>(or a program written in any language), have the script/program send commands to &#8216;gm batch&#8217; via its standard input. Specify that standard input should be used by using <code>&#8216;-&#8216;</code> as the file name. The following example converts all files matching &#8216;*.jpg&#8217; to TIFF format while rotating each file by 90 degrees and stripping all embedded profiles. The shell script syntax is standard Unix shell: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>for file in&nbsp;<wbr>*.jpg<br />
&nbsp;<wbr>&nbsp;<wbr>do<br />
&nbsp;<wbr>outfile=`basename&nbsp;<wbr>$file .jpg`.tiff<br />
&nbsp;<wbr>echo convert -verbose&nbsp;<wbr>&quot;&#8217;$file&#8217;&quot;&nbsp;<wbr>-rotate 90&nbsp;<wbr>\<br />
&nbsp;<wbr>+profile&nbsp;<wbr>&quot;&#8217;*&#8217;&quot;&nbsp;<wbr>&quot;&#8217;$outfile&#8217;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>done | gm batch -echo on -feedback on &#8211; </p>
<p> We can accomplish the same as the previous example by putting all the commands in a text file and then specifying the name of the text file as the script to execute: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>for file in&nbsp;<wbr>*.jpg<br />
&nbsp;<wbr>&nbsp;<wbr>do<br />
&nbsp;<wbr>outfile=`basename&nbsp;<wbr>$file .jpg`.tiff<br />
&nbsp;<wbr>echo convert -verbose&nbsp;<wbr>&quot;&#8217;$file&#8217;&quot;&nbsp;<wbr>-rotate 90&nbsp;<wbr>\<br />
&nbsp;<wbr>+profile&nbsp;<wbr>&quot;&#8217;*&#8217;&quot;&nbsp;<wbr>&quot;&#8217;$outfile&#8217;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>done&nbsp;<wbr>&gt;&nbsp;<wbr>script.txt<br />
&nbsp;<wbr>&nbsp;<wbr>gm batch -echo on -feedback on script.txt </p>
<h2>OPTIONS</h2>
<p> Options are processed from left to right and must appear before any filename argument.</p>
<dl>
<dt><code>-echo </code><i>on|off</i></p>
<dd> command echo on or off </p>
<p> Specify <code>on</code> to enable echoing commands to standard output as they are read or <code>off</code> to disable. The default is <code>off</code>.</p>
<dt><code>-escape </code><i>unix|windows</i></p>
<dd> Parse using unix or windows syntax </p>
<p> Commands must be parsed from the input stream and escaping needs to be used to protect spaces or quoting characters in the input. Specify <code>unix</code> to use unix-style command line parsing or <code>windows</code> for Microsoft Windows command shell style parsing. The default depends on if the software is compiled for Microsoft Windows or for a Unix-type system (including Cygwin on Microsoft Windows). It is recommended to use unix syntax because it is more powerful and more portable.</p>
<dt><code>-fail </code><i>text</i></p>
<dd> text to print if a command fails </p>
<p> When feedback is enabled, this specifies the text to print when the command fails. The default text is <code>FAIL</code>.</p>
<dt><code>-feedback </code><i>on|off</i></p>
<dd> enable error feedback </p>
<p> Print text (see -pass and -fail options) feedback after each command to indicate the result, the default is <code>off</code>.</p>
<dt><code>-help</code></p>
<dd>
<p> Prints batch command help.</p>
<dt><code>-pass </code><i>text</i></p>
<dd> text to print if a command passes </p>
<p> When feedback is enabled, this specifies the text to print when the command passes. The default text is <code>PASS</code>.</p>
<dt><code>-prompt </code><i>text</i></p>
<dd> Prompt text to use for command line </p>
<p> If no filename argument was specified, a simple command prompt appears where you may enter GraphicsMagick commands. The default prompt is <code>GM&gt;</code>. Use this option to change the prompt to something else.</p>
<dt><code>-stop-on-error </code><i>on|off</i></p>
<dd> Specify if command processing stops on error </p>
<p> Normally command processing continues if a command encounters an error. Specify <code>-stop-on-error on</code> to cause processing to quit immediately on error.</dl>
<h2>GM BENCHMARK</h2>
<h2>DESCRIPTION</h2>
<p> <code>benchmark</code> executes an arbitrary <code>gm</code> utility command (e.g. <code>convert</code>) for one or more loops, and/or a specified execution time, and reports many execution metrics. For builds using OpenMP, a mode is provided to execute the benchmark with an increasing number of threads and provide a report of speedup and multi-thread execution efficiency. If <code>benchmark</code> is used to execute a command without any additional benchmark options, then the command is run once.</p>
<h2>EXAMPLES</h2>
<p> To obtain benchmark information for a single execution of a command: </p>
<p>&nbsp;<wbr>gm benchmark convert input.ppm -gaussian 0x1 output.ppm </p>
<p> To obtain benchmark information from 100 iterations of the command: </p>
<p>&nbsp;<wbr>gm benchmark -iterations 100 convert input.ppm&nbsp;<wbr>\<br />
-gaussian 0x1 output.ppm </p>
<p> To obtain benchmark information by iterating the command until a specified amount of time (in seconds) has been consumed: </p>
<p>&nbsp;<wbr>gm benchmark -duration 30 convert input.ppm&nbsp;<wbr>\<br />
-gaussian 0x1 output.ppm </p>
<p> To obtain a full performance report with an increasing number of threads (1-32 threads, stepping the number of threads by four each time): </p>
<p>&nbsp;<wbr>gm benchmark -duration 3 -stepthreads 4 convert&nbsp;<wbr>\<br />
input.ppm -gaussian 0x2 output.ppm </p>
<p> Here is the interpretation of the output: </p>
<p>&nbsp;<wbr><code>threads</code>&nbsp;<wbr>&#8211; number of threads used.<br />
&nbsp;<wbr><code>iter</code>&nbsp;<wbr>&#8211; number of command iterations executed.<br />
&nbsp;<wbr><code>user</code>&nbsp;<wbr>&#8211; total user time consumed.<br />
&nbsp;<wbr><code>total</code>&nbsp;<wbr>&#8211; total elapsed time consumed.<br />
&nbsp;<wbr><code>iter/s</code>&nbsp;<wbr>&#8211; number of command iterations per second.<br />
&nbsp;<wbr><code>iter/cpu</code>&nbsp;<wbr>&#8211; amount of CPU time consumed per iteration.<br />
&nbsp;<wbr><code>speedup</code>&nbsp;<wbr>&#8211; speedup compared with one thread.<br />
&nbsp;<wbr><code>karp-flatt</code>&nbsp;<wbr>&#8211; Karp-Flatt measure of speedup efficiency. </p>
<p> <i>Please note that the reported &quot;speedup&quot; is based on the execution time of just one thread. A preliminary warm-up pass is used before timing the first loop in order to ensure that the CPU is brought out of power-saving modes and that system caches are warmed up. Most modern CPUs provide a &quot;turbo&quot; mode where the CPU clock speed is increased (e.g. by a factor of two) when only one or two cores are active. If the CPU grows excessively hot (due to insufficient cooling), then it may dial back its clock rates as a form of thermal management. These factors result in an under-reporting of speedup compared to if &quot;turbo&quot; mode was disabled and the CPU does not need to worry about thermal management. The </i><code>powertop</code> utility available under Linux and Solaris provides a way to observe CPU core clock rates while a benchmark is running.</p>
<h2>OPTIONS</h2>
<p>&nbsp;<wbr>Options are processed from left to right and must appear before any argument.</p>
<dl>
<dt><code>-duration </code><i>duration</i></p>
<dd> duration to run benchmark Specify the number of seconds to run the benchmark. The command is executed repeatedly until the specified amount of time has elapsed.</p>
<dt><code>-help</code></p>
<dd>
<p> Prints benchmark command help.</p>
<dt><code>-iterations </code><i>loops</i></p>
<dd> number of command iterations Specify the number of iterations to run the benchmark. The command is executed repeatedly until the specified number of iterations has been reached.</p>
<dt><code>-rawcsv</code></p>
<dd> Print results in CSV format Print results in a comma-separated value (CSV) format which is easy to parse for plotting or importing into a spreadsheet or database. The values reported are <code>threads</code>, <code>iterations</code>, <code>user_time</code>, and <code>elapsed_time</code>.</p>
<dt><code>-stepthreads </code><i>step</i></p>
<dd> execute a per-thread benchmark ramp<br />
&nbsp;<wbr>Execute a per-thread benchmark ramp, incrementing the number of threads at each step by the specified value. The maximum number of threads is taken from the standard OMP_NUM_THREADS environment variable.</dl>
<h2>GM COMPARE</h2>
<p> <code>compare</code> compares two similar images using a specified statistical method (see <code>-metric</code>) and/or by writing a difference image (<code>-file</code>), with the altered pixels annotated using a specified method (see <code>-highlight-style</code>) and color (see <code>-highlight-color</code>). <i>Reference-image</i> is the original image and <i>compare-image</i> is the (possibly) altered version, which should have the same dimensions as <i>reference-image</i>.</p>
<h2>EXAMPLES</h2>
<p> To compare two images using Mean Square Error (MSE) statistical analysis use: </p>
<p>&nbsp;<wbr>gm compare -metric mse original.miff compare.miff </p>
<p> To create an annotated difference image use: </p>
<p>&nbsp;<wbr>gm compare -highlight-style assign -highlight-color purple&nbsp;<wbr>\<br />
-file diff.miff original.miff compare.miff </p>
<h2>OPTIONS</h2>
<p> Options are processed in command line order. Any option you specify on the command line remains in effect only for the image that follows. All options are reset to their default values after each image is read. </p>
<p> For a more detailed description of each option, see Options, above. </p>
<dl>
<dt><code>-authenticate </code><i>&lt;string&gt;</i></p>
<dd> decrypt image with this password</p>
<dt><code>-colorspace </code><i>&lt;value&gt;</i></p>
<dd> the type of colorspace</p>
<dt><code>-debug </code><i>&lt;events&gt;</i></p>
<dd> enable debug printout</p>
<dt><code>-define </code><i>&lt;key&gt;{=&lt;value&gt;},&#8230;</i></p>
<dd> add coder/decoder specific options</p>
<dt><code>-density </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> horizontal and vertical resolution in pixels of the image</p>
<dt><code>-depth </code><i>&lt;value&gt;</i></p>
<dd> depth of the image</p>
<dt><code>-display </code><i>&lt;host:display[.screen]&gt;</i></p>
<dd> specifies the X server to contact</p>
<dt><code>-endian </code><i>&lt;type&gt;</i></p>
<dd> specify endianness (MSB, LSB, or Native) of image</p>
<dt><code>-file </code><i>&lt;filename&gt;</i></p>
<dd> write annotated difference image to file</p>
<dt><code>-help</code></p>
<dd> print usage instructions</p>
<dt><code>-highlight-color </code><i>&lt;color&gt;</i></p>
<dd> pixel annotation color</p>
<dt><code>-highlight-style </code><i>&lt;style&gt;</i></p>
<dd> pixel annotation style</p>
<dt><code>-interlace </code><i>&lt;type&gt;</i></p>
<dd> the type of interlacing scheme</p>
<dt><code>-limit </code><i>&lt;type&gt; &lt;value&gt;</i></p>
<dd> Disk, File, Map, Memory, Pixels, Width, Height or Threads resource limit</p>
<dt><code>-log </code><i>&lt;string&gt;</i></p>
<dd> Specify format for debug log</p>
<dt><code>-matte</code></p>
<dd> store matte channel if the image has one</p>
<dt><code>-maximum-error </code><i>&lt;limit&gt;</i></p>
<dd> specifies the maximum amount of total image error</p>
<dt><code>-metric </code><i>&lt;metric&gt;</i></p>
<dd> comparison metric (MAE, MSE, PAE, PSNR, RMSE)</p>
<dt><code>-monitor</code></p>
<dd> show progress indication</p>
<dt><code>-sampling-factor </code><i>&lt;horizontal_factor&gt;x&lt;vertical_factor&gt;</i></p>
<dd> chroma subsampling factors</p>
<dt><code>-size </code><i>&lt;width&gt;x&lt;height&gt;{+offset}</i></p>
<dd> width and height of the image</p>
<dt><code>-type </code><i>&lt;type&gt;</i></p>
<dd> the image type</p>
<dt><code>-verbose</code></p>
<dd> print detailed information about the image</p>
<dt><code>-version</code></p>
<dd> print GraphicsMagick version string </p>
<p> For a more detailed description of each option, see Options, above. </p>
</dl>
<h2>GM COMPOSITE</h2>
<p> <code>composite</code> composites (combines) images to create new images. <i>base-image</i> is the base image and <i>change-image</i> contains the changes. <i>ouput-image</i> is the result, and normally has the same dimensions as <i>base-image</i>. </p>
<p> The optional <i>mask-image</i> can be used to provide opacity information for <i>change-image</i> when it has none or if you want a different mask. A mask image is typically grayscale and the same size as <code>base-image</code>. If <i>mask-image</i> is not grayscale, it is converted to grayscale and the resulting intensities are used as opacity information.</p>
<h2>EXAMPLES</h2>
<p> To composite an image of a cockatoo with a perch, use: </p>
<p>&nbsp;<wbr>gm composite cockatoo.miff perch.ras composite.miff </p>
<p> To compute the difference between images in a series, use: </p>
<p>&nbsp;<wbr>gm composite -compose difference series.2 series.1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>difference.miff </p>
<p> To composite an image of a cockatoo with a perch starting at location (100,150), use: </p>
<p>&nbsp;<wbr>gm composite -geometry&nbsp;<wbr>+100+150 cockatoo.miff<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>perch.ras composite.miff </p>
<p> To tile a logo across your image of a cockatoo, use </p>
<p>&nbsp;<wbr>gm convert&nbsp;<wbr>+shade 30&#215;60 cockatoo.miff mask.miff<br />
&nbsp;<wbr>gm composite -compose bumpmap -tile logo.png<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cockatoo.miff mask.miff composite.miff </p>
<p> To composite a red, green, and blue color plane into a single composite image, try </p>
<p>&nbsp;<wbr>gm composite -compose CopyGreen green.png red.png<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>red-green.png<br />
&nbsp;<wbr>gm composite -compose CopyBlue blue.png red-green.png&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gm composite.png </p>
<h2>OPTIONS</h2>
<p> Options are processed in command line order. Any option you specify on the command line remains in effect only for the image that follows. All options are reset to their default values after each image is read. </p>
<p> For a more detailed description of each option, see Options, above. </p>
<dl>
<dt><code>-authenticate </code><i>&lt;string&gt;</i></p>
<dd> decrypt image with this password</p>
<dt><code>-background </code><i>&lt;color&gt;</i></p>
<dd> the background color</p>
<dt><code>-blue-primary </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> blue chromaticity primary point</p>
<dt><code>-colors </code><i>&lt;value&gt;</i></p>
<dd> preferred number of colors in the image</p>
<dt><code>-colorspace </code><i>&lt;value&gt;</i></p>
<dd> the type of colorspace</p>
<dt><code>-comment </code><i>&lt;string&gt;</i></p>
<dd> annotate an image with a comment</p>
<dt><code>-compose </code><i>&lt;operator&gt;</i></p>
<dd> the type of image composition</p>
<dt><code>-compress </code><i>&lt;type&gt;</i></p>
<dd> the type of image compression</p>
<dt><code>-debug </code><i>&lt;events&gt;</i></p>
<dd> enable debug printout</p>
<dt><code>-define </code><i>&lt;key&gt;{=&lt;value&gt;},&#8230;</i></p>
<dd> add coder/decoder specific options</p>
<dt><code>-density </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> horizontal and vertical resolution in pixels of the image</p>
<dt><code>-depth </code><i>&lt;value&gt;</i></p>
<dd> depth of the image</p>
<dt><code>-displace </code><i>&lt;horizontal scale&gt;x&lt;vertical scale&gt;</i></p>
<dd> shift image pixels as defined by a displacement map</p>
<dt><code>-display </code><i>&lt;host:display[.screen]&gt;</i></p>
<dd> specifies the X server to contact</p>
<dt><code>-dispose </code><i>&lt;method&gt;</i></p>
<dd> GIF disposal method</p>
<dt><code>-dissolve </code><i>&lt;percent&gt;</i></p>
<dd> dissolve an image into another by the given percent</p>
<dt><code>-dither</code></p>
<dd> apply Floyd/Steinberg error diffusion to the image</p>
<dt><code>-encoding </code><i>&lt;type&gt;</i></p>
<dd> specify the text encoding</p>
<dt><code>-endian </code><i>&lt;type&gt;</i></p>
<dd> specify endianness (MSB, LSB, or Native) of image</p>
<dt><code>-filter </code><i>&lt;type&gt;</i></p>
<dd> use this type of filter when resizing an image</p>
<dt><code>-font </code><i>&lt;name&gt;</i></p>
<dd> use this font when annotating the image with text</p>
<dt><code>-geometry </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}{@}{!}{^}{&lt;}{&gt;}</i></p>
<dd> Specify dimension, offset, and resize options.</p>
<dt><code>-gravity </code><i>&lt;type&gt;</i></p>
<dd> direction primitive gravitates to when annotating the image.</p>
<dt><code>-green-primary </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> green chromaticity primary point</p>
<dt><code>-help</code></p>
<dd> print usage instructions</p>
<dt><code>-interlace </code><i>&lt;type&gt;</i></p>
<dd> the type of interlacing scheme</p>
<dt><code>-label </code><i>&lt;name&gt;</i></p>
<dd> assign a label to an image</p>
<dt><code>-limit </code><i>&lt;type&gt; &lt;value&gt;</i></p>
<dd> Disk, File, Map, Memory, Pixels, Width, Height or Threads resource limit</p>
<dt><code>-log </code><i>&lt;string&gt;</i></p>
<dd> Specify format for debug log</p>
<dt><code>-matte</code></p>
<dd> store matte channel if the image has one</p>
<dt><code>-monitor</code></p>
<dd> show progress indication</p>
<dt><code>-monochrome</code></p>
<dd> transform the image to black and white</p>
<dt><code>-negate</code></p>
<dd> replace every pixel with its complementary color</p>
<dt><code>-page </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}{!}{&lt;}{&gt;}</i></p>
<dd> size and location of an image canvas</p>
<dt><code>-profile </code><i>&lt;filename&gt;</i></p>
<dd> add ICM, IPTC, or generic profile to image</p>
<dt><code>-quality </code><i>&lt;value&gt;</i></p>
<dd> JPEG/MIFF/PNG/TIFF compression level</p>
<dt><code>-recolor </code><i>&lt;matrix&gt;</i></p>
<dd> apply a color translation matrix to image channels</p>
<dt><code>-red-primary </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> red chromaticity primary point</p>
<dt><code>-render</code></p>
<dd> render vector operations</p>
<dt><code>-repage </code><i> &lt;width&gt;x&lt;height&gt;+xoff+yoff[!]</i></p>
<dd> Adjust image page offsets</p>
<dt><code>-resize </code><i>&lt;width&gt;x&lt;height&gt;{%}{@}{!}{&lt;}{&gt;}</i></p>
<dd> resize an image</p>
<dt><code>-rotate </code><i>&lt;degrees&gt;{&lt;}{&gt;}</i></p>
<dd> rotate the image</p>
<dt><code>-sampling-factor </code><i>&lt;horizontal_factor&gt;x&lt;vertical_factor&gt;</i></p>
<dd> chroma subsampling factors</p>
<dt><code>-scene </code><i>&lt;value&gt;</i></p>
<dd> set scene number</p>
<dt><code>-set </code><i>&lt;attribute&gt; &lt;value&gt;</i></p>
<dd> set an image attribute</p>
<dt><code>+set </code><i>&lt;attribute&gt;</i></p>
<dd> unset an image attribute</p>
<dt><code>-sharpen </code><i>&lt;radius&gt;{x&lt;sigma&gt;}</i></p>
<dd> sharpen the image</p>
<dt><code>-size </code><i>&lt;width&gt;x&lt;height&gt;{+offset}</i></p>
<dd> width and height of the image</p>
<dt><code>-stegano </code><i>&lt;offset&gt;</i></p>
<dd> hide watermark within an image</p>
<dt><code>-stereo</code></p>
<dd> composite two images to create a stereo anaglyph</p>
<dt><code>-strip</code></p>
<dd> remove all profiles and text attributes from the image</p>
<dt><code>-thumbnail </code><i>&lt;width&gt;x&lt;height&gt;{%}{@}{!}{&lt;}{&gt;}</i></p>
<dd> resize an image (quickly)</p>
<dt><code>-treedepth </code><i>&lt;value&gt;</i></p>
<dd> tree depth for the color reduction algorithm</p>
<dt><code>-trim</code></p>
<dd> trim an image</p>
<dt><code>-type </code><i>&lt;type&gt;</i></p>
<dd> the image type</p>
<dt><code>-units </code><i>&lt;type&gt;</i></p>
<dd> the units of image resolution</p>
<dt><code>-unsharp </code><i>&lt;radius&gt;{x&lt;sigma&gt;}{+&lt;amount&gt;}{+&lt;threshold&gt;}</i></p>
<dd> sharpen the image with an unsharp mask operator</p>
<dt><code>-verbose</code></p>
<dd> print detailed information about the image</p>
<dt><code>-version</code></p>
<dd> print GraphicsMagick version string</p>
<dt><code>-watermark </code><i>&lt;brightness&gt;x&lt;saturation&gt;</i></p>
<dd> percent brightness and saturation of a watermark</p>
<dt><code>-white-point </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> chromaticity white point</p>
<dt><code>-write </code><i>&lt;filename&gt;</i></p>
<dd> write an intermediate image [<i>convert, composite</i>] </p>
<p> For a more detailed description of each option, see Options, above. </p>
</dl>
<h2>GM CONJURE</h2>
<p> The Magick scripting language (MSL) will primarily benefit those that want to accomplish custom image processing tasks but do not wish to program, or those that do not have access to a Perl interpreter or a compiler. The interpreter is called conjure and here is an example script: </p>
<p>&nbsp;<wbr>&lt;?xml version=&quot;1.0&quot;&nbsp;<wbr>encoding=&quot;UTF-8&quot;?&gt;<br />
&nbsp;<wbr>&lt;image size=&quot;400&#215;400&quot;&nbsp;<wbr>&gt;<br />
&lt;read filename=&quot;image.gif&quot;&nbsp;<wbr>/&gt;<br />
&lt;get width=&quot;base-width&quot;&nbsp;<wbr>height=&quot;base-height&quot;&nbsp;<wbr>/&gt;<br />
&lt;resize geometry=&quot;%[dimensions]&quot;&nbsp;<wbr>/&gt;<br />
&lt;get width=&quot;width&quot;&nbsp;<wbr>height=&quot;height&quot;&nbsp;<wbr>/&gt;<br />
&lt;print output=<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;Image sized from&nbsp;<wbr>%[base-width]x%[base-height]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to&nbsp;<wbr>%[width]x%[height].
&quot;&nbsp;<wbr>/&gt;<br />
&lt;write filename=&quot;image.png&quot;&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;/image&gt; </p>
<p> invoked with </p>
<p>&nbsp;<wbr>gm conjure -dimensions 400&#215;400 incantation.msl </p>
<p> All operations will closely follow the key/value pairs defined in PerlMagick, unless otherwise noted.</p>
<h2>OPTIONS</h2>
<p> Options are processed in command line order. Any option you specify on the command line remains in effect until it is explicitly changed by specifying the option again with a different effect, or if it is changed by a statement in the scripting language. </p>
<p> You can define your own keyword/value pairs on the command line. The script can then use this information when setting values by including %[keyword] in the string. For example, if you included &quot;-dimensions 400&#215;400&quot; on the command line, as illustrated above, then any string containing &quot;%[dimensions]&quot; would have 400&#215;400 substituted. The &quot;%[string]&quot; can be used either an entire string, such as geometry=&quot;%[dimensions]&quot; or as a part of a string such as filename=&quot;%[basename].png&quot;. </p>
<p> The keyword can be any string except for the following reserved strings (in any upper, lower, or mixed case variant): <code>debug</code>, <code>help</code>, and <code>verbose</code>, whose usage is described below. </p>
<p> The value can be any string. If either the keyword or the value contains white space or any symbols that have special meanings to your shell such as &quot;#&quot;, &quot;|&quot;, or &quot;%&quot;, enclose the string in quotation marks or use &quot;\&quot; to escape the white space and special symbols. </p>
<p> Keywords and values are case dependent. &quot;Key&quot;, &quot;key&quot;, and &quot;KEY&quot; would be three different keywords. </p>
<p> For a more detailed description of each option, see Options, above. </p>
<dl>
<dt><code>-debug </code><i>&lt;events&gt;</i></p>
<dd> enable debug printout</p>
<dt><code>-define </code><i>&lt;key&gt;{=&lt;value&gt;},&#8230;</i></p>
<dd> add coder/decoder specific options</p>
<dt><code>-help</code></p>
<dd> print usage instructions</p>
<dt><code>-log </code><i>&lt;string&gt;</i></p>
<dd> Specify format for debug log</p>
<dt><code>-verbose</code></p>
<dd> print detailed information about the image</p>
<dt><code>-version</code></p>
<dd> print GraphicsMagick version string</dl>
<h2>MAGICK SCRIPTING LANGUAGE</h2>
<p> The Magick Scripting Language (MSL) presently defines the following elements and their attributes: </p>
<p> <code>&lt;image&gt;</code><br />
&nbsp;<wbr> background, color, id, size </p>
<p> Define a new image object. <code>&lt;/image&gt;</code> destroys it. Because of this, if you wish to reference multiple &quot;subimages&quot; (aka pages or layers), you can embed one <code>image</code> element inside of another. For example: </p>
<p>&nbsp;<wbr>&lt;image&gt;<br />
&nbsp;<wbr>&lt;read filename=&quot;input.png&quot;&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;get width=&quot;base-width&quot;&nbsp;<wbr>height=&quot;base-height&quot;&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;image height=&quot;base-height&quot;&nbsp;<wbr>width=&quot;base-width&quot;&gt;<br />
&nbsp;<wbr>&lt;image&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;write filename=&quot;output.mng&quot;&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;/image&gt; </p>
<p>&nbsp;<wbr>&lt;image size=&quot;400&#215;400&quot;&nbsp;<wbr>/&gt; </p>
<p> <code>&lt;group&gt;</code><br />
&nbsp;<wbr> </p>
<p> Define a new group of image objects. By default, images are only valid for the life of their <code>&lt;image&gt;</code>element. </p>
<p>&nbsp;<wbr>&lt;image&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; creates the image<br />
&nbsp;<wbr>&#8230;..&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; do stuff with it<br />
&nbsp;<wbr>&lt;/image&gt;&nbsp;<wbr>&nbsp;<wbr>&#8212; dispose of the image </p>
<p> However, in a group, all images in that group will stay around for the life of the group: </p>
<p>&nbsp;<wbr>&lt;group&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; start a group<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;image&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; create an image<br />
&nbsp;<wbr>&nbsp;<wbr>&#8230;.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; do stuff<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/image&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; NOOP<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;image&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; create another image<br />
&nbsp;<wbr>&nbsp;<wbr>&#8230;.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; do more stuff<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/image&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; NOOP<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;write filename=&quot;image.mng&quot;&nbsp;<wbr>/&gt;&nbsp;<wbr>&nbsp;<wbr>&#8212; output<br />
&nbsp;<wbr>&lt;/group&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212; dispose of both images </p>
<p> <code>&lt;read&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>filename </p>
<p> Read a new image from a disk file. </p>
<p>&nbsp;<wbr>&lt;read filename=&quot;image.gif&quot;&nbsp;<wbr>/&gt; </p>
<p> To read two images use </p>
<p>&nbsp;<wbr>&lt;read filename=&quot;image.gif&quot;&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;read filename=&quot;image.png&nbsp;<wbr>/&gt; </p>
<p> <code>&lt;write&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>filename Write the image(s) to disk, either as a single multiple-image file or multiple ones if necessary. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;write filename=image.tiff&quot;&nbsp;<wbr>/&gt; </p>
<p> <code>&lt;get&gt;</code><br />
&nbsp;<wbr> Get any attribute recognized by PerlMagick&#8217;s GetAttribute() and stores it as an image attribute for later use. Currently only <i>width</i> and <i>height</i> are supported. </p>
<p>&nbsp;<wbr>&lt;get width=&quot;base-width&quot;&nbsp;<wbr>height=&quot;base-height&quot;&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&lt;print output=&quot;Image size is&nbsp;<wbr>%[base-width]x%[base-height].
&quot;&nbsp;<wbr>/&gt; </p>
<p> <code>&lt;set&gt;</code><br />
&nbsp;<wbr> background, bordercolor, clip-mask, colorspace, density, magick, mattecolor, opacity. Set an attribute recognized by PerlMagick&#8217;s GetAttribute(). <code>&lt;profile&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>[profilename] </p>
<p> Read one or more IPTC, ICC or generic profiles from file and assign to image </p>
<p>&nbsp;<wbr>&lt;profile iptc=&quot;profile.iptc&quot;&nbsp;<wbr>generic=&quot;generic.dat&quot;&nbsp;<wbr>/&gt; </p>
<p> To remove a specified profile use &quot;!&quot; as the filename eg </p>
<p>&nbsp;<wbr>&lt;profile icm=&quot;!&quot;&nbsp;<wbr>iptc=&quot;profile.iptc&quot;&nbsp;<wbr>/&gt; </p>
<p> <code>&lt;border&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>fill, geometry, height, width <code>&lt;blur&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>radius, sigma <code>&lt;charcoal&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>radius, sigma <code>&lt;chop&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>geometry, height, width, x, y <code>&lt;crop&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>geometry, height, width, x, y <code>&lt;composite&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>compose, geometry, gravity, image, x, y </p>
<p>&nbsp;<wbr>&lt;?xml version=&quot;1.0&quot;&nbsp;<wbr>encoding=&quot;UTF-8&quot;?&gt;<br />
&nbsp;<wbr>&lt;group&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;image id=&quot;image_01&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;read filename=&quot;cloud3.gif&quot;/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;resize geometry=&quot;250&#215;90&quot;/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/image&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;image id=&quot;image_02&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;read filename=&quot;cloud4.gif&quot;/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;resize geometry=&quot;190&#215;100&quot;/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/image&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;image&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;read filename=&quot;background.jpg&quot;/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;composite image=&quot;image_01&quot;&nbsp;<wbr>geometry=&quot;+740+470&quot;/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;composite image=&quot;image_02&quot;&nbsp;<wbr>geometry=&quot;+390+415&quot;/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/image&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;write filename=&quot;result.png&quot;/&gt;<br />
&nbsp;<wbr>&lt;/group&gt; </p>
<p> <code>&lt;despeckle&gt;</code><br />
&nbsp;<wbr> <code>&lt;emboss&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>radius, sigma <code>&lt;enhance&gt;</code><br />
&nbsp;<wbr> <code>&lt;equalize&gt;</code><br />
&nbsp;<wbr> <code>&lt;edge&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>radius <code>&lt;flip&gt;</code><br />
&nbsp;<wbr> <code>&lt;flop&gt;</code><br />
&nbsp;<wbr> <code>&lt;frame&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>fill, geometry, height, width, x, y, inner, outer <code>&lt;flatten&gt;</code><br />
&nbsp;<wbr> <code>&lt;get&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>height, width <code>&lt;gamma&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>red, green, blue <code>&lt;image&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>background, color, id, size <code>&lt;implode&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>amount <code>&lt;magnify&gt;</code><br />
&nbsp;<wbr> <code>&lt;minify&gt;</code><br />
&nbsp;<wbr> <code>&lt;medianfilter&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>radius <code>&lt;normalize&gt;</code><br />
&nbsp;<wbr> <code>&lt;oilpaint&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>radius <code>&lt;print&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>output <code>&lt;profile&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>[profilename] <code>&lt;read&gt;</code><br />
&nbsp;<wbr> <code>&lt;resize&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>blur, filter, geometry, height, width <code>&lt;roll&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>geometry, x, y <code>&lt;rotate&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>degrees <code>&lt;reducenoise&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>radius <code>&lt;sample&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>geometry, height, width <code>&lt;scale&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>geometry, height, width <code>&lt;sharpen&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>radius, sigma <code>&lt;shave&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>geometry, height, width <code>&lt;shear&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>x, y <code>&lt;solarize&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>threshold <code>&lt;spread&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>radius <code>&lt;stegano&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>image <code>&lt;stereo&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>image <code>&lt;swirl&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>degrees <code>&lt;texture&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>image <code>&lt;threshold&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>threshold <code>&lt;transparent&gt;</code><br />
&nbsp;<wbr><br />
&nbsp;<wbr>color <code>&lt;trim&gt;</code><br />
&nbsp;<wbr> </p>
<h2>GM CONVERT</h2>
<p> <code>Convert</code> converts an input file using one image format to an output file with a differing image format. In addition, various types of image processing can be performed on the converted image during the conversion process. <code>Convert</code> recognizes the image formats listed in <i><a href="/docs/linux/man/1-graphicsmagick/">GraphicsMagick</a>(1)</i>. </p>
<h2>EXAMPLES</h2>
<p> To make a thumbnail of a JPEG image, use: </p>
<p>&nbsp;<wbr>gm convert -size 120&#215;120 cockatoo.jpg -resize 120&#215;120<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+profile&nbsp;<wbr>&quot;*&quot;&nbsp;<wbr>thumbnail.jpg </p>
<p> In this example, &#8216;-size 120&#215;120&#8217; gives a hint to the JPEG decoder that the image is going to be downscaled to 120&#215;120, allowing it to run faster by avoiding returning full-resolution images to GraphicsMagick for the subsequent resizing operation. The &#8216;-resize 120&#215;120&#8217; specifies the desired dimensions of the output image. It will be scaled so its largest dimension is 120 pixels. The &#8216;+profile &quot;*&quot;&#8217; removes any ICM, EXIF, IPTC, or other profiles that might be present in the input and aren&#8217;t needed in the thumbnail. </p>
<p> To convert a <i>MIFF</i> image of a cockatoo to a SUN raster image, use: </p>
<p>&nbsp;<wbr>gm convert cockatoo.miff sun:cockatoo.ras </p>
<p> To convert a multi-page <i>PostScript</i> document to individual FAX pages, use: </p>
<p>&nbsp;<wbr>gm convert -monochrome document.ps fax:page </p>
<p> To convert a TIFF image to a <i>PostScript</i> A4 page with the image in the lower left-hand corner, use: </p>
<p>&nbsp;<wbr>gm convert -page A4+0+0 image.tiff document.ps </p>
<p> To convert a raw Gray image with a 128 byte header to a portable graymap, use: </p>
<p>&nbsp;<wbr>gm convert -depth 8 -size 768&#215;512+128 gray:raw<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>image.pgm </p>
<p> In this example, &quot;raw&quot; is the input file. Its format is &quot;gray&quot; and it has the dimensions and number of header bytes specified by the -size option and the sample depth specified by the -depth option. The output file is &quot;image.pgm&quot;. The suffix &quot;.pgm&quot; specifies its format. </p>
<p> To convert a Photo CD image to a TIFF image, use: </p>
<p>&nbsp;<wbr>gm convert -size 1536&#215;1024 img0009.pcd image.tiff<br />
&nbsp;<wbr>gm convert img0009.pcd[4]&nbsp;<wbr>image.tiff </p>
<p> To create a visual image directory of all your JPEG images, use: </p>
<p>&nbsp;<wbr>gm convert&nbsp;<wbr>&#8216;vid:*.jpg&#8217;&nbsp;<wbr>directory.miff </p>
<p> To annotate an image with blue text using font 12&#215;24 at position (100,100), use: </p>
<p>&nbsp;<wbr>gm convert -font helvetica -fill blue<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-draw&nbsp;<wbr>&quot;text 100,100 Cockatoo&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bird.jpg bird.miff </p>
<p> To tile a 640&#215;480 image with a JPEG texture with bumps use: </p>
<p>&nbsp;<wbr>gm convert -size 640&#215;480 tile:bumps.jpg tiled.png </p>
<p> To surround an icon with an ornamental border to use with <a href="/docs/linux/man/1-mosaic/">Mosaic</a>(1), use: </p>
<p>&nbsp;<wbr>gm convert -mattecolor&nbsp;<wbr>&quot;#697B8F&quot;&nbsp;<wbr>-frame 6&#215;6 bird.jpg<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>icon.png </p>
<p> To create a MNG animation from a DNA molecule sequence, use: </p>
<p>&nbsp;<wbr>gm convert -delay 20 dna.*&nbsp;<wbr>dna.mng </p>
<h2>OPTIONS</h2>
<p> Options are processed in command line order. Any option you specify on the command line remains in effect for the set of images that follows, until the set is terminated by the appearance of any option or <code>-noop</code>. Some options only affect the decoding of images and others only the encoding. The latter can appear after the final group of input images. </p>
<p> For a more detailed description of each option, see Options, above. </p>
<dl>
<dt><code>-adjoin</code></p>
<dd> join images into a single multi-image file</p>
<dt><code>-affine </code><i>&lt;matrix&gt;</i></p>
<dd> drawing transform matrix</p>
<dt><code>-antialias</code></p>
<dd> remove pixel aliasing</p>
<dt><code>-append</code></p>
<dd> append a set of images</p>
<dt><i>-asc-cdl &lt;spec&gt;</i></p>
<dd> apply ASC CDL color transform</p>
<dt><code>-authenticate </code><i>&lt;string&gt;</i></p>
<dd> decrypt image with this password</p>
<dt><code>-auto-orient</code></p>
<dd> orient (rotate) image so it is upright</p>
<dt><code>-average</code></p>
<dd> average a set of images</p>
<dt><code>-background </code><i>&lt;color&gt;</i></p>
<dd> the background color</p>
<dt><code>-black-threshold </code><i>red[,green][,blue][,opacity]</i></p>
<dd> pixels below the threshold become black</p>
<dt><code>-blue-primary </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> blue chromaticity primary point</p>
<dt><code>-blur </code><i>&lt;radius&gt;{x&lt;sigma&gt;}</i></p>
<dd> blur the image with a Gaussian operator</p>
<dt><code>-border </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> surround the image with a border of color</p>
<dt><code>-bordercolor </code><i>&lt;color&gt;</i></p>
<dd> the border color</p>
<dt><code>-box </code><i>&lt;color&gt;</i></p>
<dd> set the color of the annotation bounding box</p>
<dt><code>-channel </code><i>&lt;type&gt;</i></p>
<dd> the type of channel</p>
<dt><code>-charcoal </code><i>&lt;factor&gt;</i></p>
<dd> simulate a charcoal drawing</p>
<dt><code>-chop </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}</i></p>
<dd> remove pixels from the interior of an image</p>
<dt><code>-clip</code></p>
<dd> apply the clipping path, if one is present</p>
<dt><code>-coalesce</code></p>
<dd> merge a sequence of images</p>
<dt><code>-colorize </code><i>&lt;value&gt;</i></p>
<dd> colorize the image with the pen color</p>
<dt><code>-colors </code><i>&lt;value&gt;</i></p>
<dd> preferred number of colors in the image</p>
<dt><code>-colorspace </code><i>&lt;value&gt;</i></p>
<dd> the type of colorspace</p>
<dt><code>-comment </code><i>&lt;string&gt;</i></p>
<dd> annotate an image with a comment</p>
<dt><code>-compose </code><i>&lt;operator&gt;</i></p>
<dd> the type of image composition</p>
<dt><code>-compress </code><i>&lt;type&gt;</i></p>
<dd> the type of image compression</p>
<dt><code>-contrast</code></p>
<dd> enhance or reduce the image contrast</p>
<dt><code>-convolve </code><i>&lt;kernel&gt;</i></p>
<dd> convolve image with the specified convolution kernel</p>
<dt><code>-crop </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}</i></p>
<dd> preferred size and location of the cropped image</p>
<dt><code>-cycle </code><i>&lt;amount&gt;</i></p>
<dd> displace image colormap by amount</p>
<dt><code>-debug </code><i>&lt;events&gt;</i></p>
<dd> enable debug printout</p>
<dt><code>-deconstruct</code></p>
<dd> break down an image sequence into constituent parts</p>
<dt><code>-define </code><i>&lt;key&gt;{=&lt;value&gt;},&#8230;</i></p>
<dd> add coder/decoder specific options</p>
<dt><code>-delay </code><i>&lt;1/100ths of a second&gt;</i></p>
<dd> display the next image after pausing</p>
<dt><code>-density </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> horizontal and vertical resolution in pixels of the image</p>
<dt><code>-depth </code><i>&lt;value&gt;</i></p>
<dd> depth of the image</p>
<dt><code>-despeckle</code></p>
<dd> reduce the speckles within an image</p>
<dt><code>-display </code><i>&lt;host:display[.screen]&gt;</i></p>
<dd> specifies the X server to contact</p>
<dt><code>-dispose </code><i>&lt;method&gt;</i></p>
<dd> GIF disposal method</p>
<dt><code>-dither</code></p>
<dd> apply Floyd/Steinberg error diffusion to the image</p>
<dt><code>-draw </code><i>&lt;string&gt;</i></p>
<dd> annotate an image with one or more graphic primitives</p>
<dt><code>-edge </code><i>&lt;radius&gt;</i></p>
<dd> detect edges within an image</p>
<dt><code>-emboss </code><i>&lt;radius&gt;</i></p>
<dd> emboss an image</p>
<dt><code>-encoding </code><i>&lt;type&gt;</i></p>
<dd> specify the text encoding</p>
<dt><code>-endian </code><i>&lt;type&gt;</i></p>
<dd> specify endianness (MSB, LSB, or Native) of image</p>
<dt><code>-enhance</code></p>
<dd> apply a digital filter to enhance a noisy image</p>
<dt><code>-equalize</code></p>
<dd> perform histogram equalization to the image</p>
<dt><code>-extent </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;</i></p>
<dd> composite image on background color canvas image</p>
<dt><code>-fill </code><i>&lt;color&gt;</i></p>
<dd> color to use when filling a graphic primitive</p>
<dt><code>-filter </code><i>&lt;type&gt;</i></p>
<dd> use this type of filter when resizing an image</p>
<dt><code>-flatten</code></p>
<dd> flatten a sequence of images</p>
<dt><code>-flip</code></p>
<dd> create a &quot;mirror image&quot;</p>
<dt><code>-flop</code></p>
<dd> create a &quot;mirror image&quot;</p>
<dt><code>-font </code><i>&lt;name&gt;</i></p>
<dd> use this font when annotating the image with text</p>
<dt><code>-format </code><i>&lt;string&gt;</i></p>
<dd> output formatted image characteristics</p>
<dt><code>-frame </code><i>&lt;width&gt;x&lt;height&gt;+&lt;outer bevel width&gt;+&lt;inner bevel width&gt;</i></p>
<dd> surround the image with an ornamental border</p>
<dt><code>-fuzz </code><i>&lt;distance&gt;{%}</i></p>
<dd> colors within this Euclidean distance are considered equal</p>
<dt><code>-gamma </code><i>&lt;value&gt;</i></p>
<dd> level of gamma correction</p>
<dt><code>-gaussian </code><i>&lt;radius&gt;{x&lt;sigma&gt;}</i></p>
<dd> blur the image with a Gaussian operator</p>
<dt><code>-geometry </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}{@}{!}{^}{&lt;}{&gt;}</i></p>
<dd> Specify dimension, offset, and resize options.</p>
<dt><code>-gravity </code><i>&lt;type&gt;</i></p>
<dd> direction primitive gravitates to when annotating the image.</p>
<dt><code>-green-primary </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> green chromaticity primary point</p>
<dt><code>-hald-clut </code><i>&lt;clut&gt;</i></p>
<dd> apply a Hald CLUT to the image</p>
<dt><code>-help</code></p>
<dd> print usage instructions</p>
<dt><code>-implode </code><i>&lt;factor&gt;</i></p>
<dd> implode image pixels about the center</p>
<dt><code>-intent </code><i>&lt;type&gt;</i></p>
<dd> use this type of rendering intent when managing the image color</p>
<dt><code>-interlace </code><i>&lt;type&gt;</i></p>
<dd> the type of interlacing scheme</p>
<dt><code>-label </code><i>&lt;name&gt;</i></p>
<dd> assign a label to an image</p>
<dt><code>-lat </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;offset&gt;{%}</i></p>
<dd> perform local adaptive thresholding</p>
<dt><code>-level </code><i>&lt;black_point&gt;{,&lt;gamma&gt;}{,&lt;white_point&gt;}{%}</i></p>
<dd> adjust the level of image contrast</p>
<dt><code>-limit </code><i>&lt;type&gt; &lt;value&gt;</i></p>
<dd> Disk, File, Map, Memory, Pixels, Width, Height or Threads resource limit</p>
<dt><code>-list </code><i>&lt;type&gt;</i></p>
<dd> the type of list</p>
<dt><code>-log </code><i>&lt;string&gt;</i></p>
<dd> Specify format for debug log</p>
<dt><code>-loop </code><i>&lt;iterations&gt;</i></p>
<dd> add Netscape loop extension to your GIF animation</p>
<dt><code>-magnify</code></p>
<dd> magnify the image</p>
<dt><code>-map </code><i>&lt;filename&gt;</i></p>
<dd> choose a particular set of colors from this image</p>
<dt><code>-mask </code><i>&lt;filename&gt;</i></p>
<dd> Specify a clipping mask</p>
<dt><code>-matte</code></p>
<dd> store matte channel if the image has one</p>
<dt><code>-mattecolor </code><i>&lt;color&gt;</i></p>
<dd> specify the color to be used with the <code>-frame</code> option</p>
<dt><code>-median </code><i>&lt;radius&gt;</i></p>
<dd> apply a median filter to the image</p>
<dt><code>-minify </code><i>&lt;factor&gt;</i></p>
<dd> minify the image</p>
<dt><code>-modulate </code><i>brightness[,saturation[,hue]]</i></p>
<dd> vary the brightness, saturation, and hue of an image</p>
<dt><code>-monitor</code></p>
<dd> show progress indication</p>
<dt><code>-monochrome</code></p>
<dd> transform the image to black and white</p>
<dt><code>-morph </code><i>&lt;frames&gt;</i></p>
<dd> morphs an image sequence</p>
<dt><code>-mosaic</code></p>
<dd> create a mosaic from an image or an image sequence</p>
<dt><code>-motion-blur </code><i>&lt;radius&gt;{x&lt;sigma&gt;}{+angle}</i></p>
<dd> Simulate motion blur</p>
<dt><code>-negate</code></p>
<dd> replace every pixel with its complementary color</p>
<dt><code>-noise </code><i>&lt;radius|type&gt;</i></p>
<dd> add or reduce noise in an image</p>
<dt><code>-noop</code></p>
<dd> NOOP (no option)</p>
<dt><code>-normalize</code></p>
<dd> transform image to span the full range of color values</p>
<dt><code>-opaque </code><i>&lt;color&gt;</i></p>
<dd> change this color to the pen color within the image</p>
<dt><code>-operator </code><i>channel operator rvalue[%]</i></p>
<dd> apply a mathematical, bitwise, or value operator to an image channel</p>
<dt><code>-ordered-dither </code><i>&lt;channeltype&gt; &lt;NxN&gt;</i></p>
<dd> ordered dither the image</p>
<dt><code>-orient </code><i>&lt;orientation&gt;</i></p>
<dd> Set the image orientation attribute</p>
<dt><code>-page </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}{!}{&lt;}{&gt;}</i></p>
<dd> size and location of an image canvas</p>
<dt><code>-paint </code><i>&lt;radius&gt;</i></p>
<dd> simulate an oil painting</p>
<dt><code>-pen </code><i>&lt;color&gt;</i></p>
<dd> (This option has been replaced by the -fill option)</p>
<dt><code>-ping</code></p>
<dd> efficiently determine image characteristics</p>
<dt><code>-pointsize </code><i>&lt;value&gt;</i></p>
<dd> pointsize of the PostScript, X11, or TrueType font</p>
<dt><code>-preview </code><i>&lt;type&gt;</i></p>
<dd> image preview type</p>
<dt><code>-process </code><i>&lt;command&gt;</i></p>
<dd> process a sequence of images using a process module</p>
<dt><code>-profile </code><i>&lt;filename&gt;</i></p>
<dd> add ICM, IPTC, or generic profile to image</p>
<dt><code>-quality </code><i>&lt;value&gt;</i></p>
<dd> JPEG/MIFF/PNG/TIFF compression level</p>
<dt><code>-raise </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> lighten or darken image edges</p>
<dt><code>-random-threshold </code><i>&lt;channeltype&gt; &lt;LOWxHIGH&gt;</i></p>
<dd> random threshold the image</p>
<dt><code>-recolor </code><i>&lt;matrix&gt;</i></p>
<dd> apply a color translation matrix to image channels</p>
<dt><code>-red-primary </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> red chromaticity primary point</p>
<dt><code>-region </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;</i></p>
<dd> apply options to a portion of the image</p>
<dt><code>-render</code></p>
<dd> render vector operations</p>
<dt><code>-repage </code><i> &lt;width&gt;x&lt;height&gt;+xoff+yoff[!]</i></p>
<dd> Adjust image page offsets</p>
<dt><code>-resample </code><i>&lt;horizontal&gt;x&lt;vertical&gt;</i></p>
<dd> Resample image to specified horizontal and vertical resolution</p>
<dt><code>-resize </code><i>&lt;width&gt;x&lt;height&gt;{%}{@}{!}{&lt;}{&gt;}</i></p>
<dd> resize an image</p>
<dt><code>-roll </code><i>{+-}&lt;x&gt;{+-}&lt;y&gt;</i></p>
<dd> roll an image vertically or horizontally</p>
<dt><code>-rotate </code><i>&lt;degrees&gt;{&lt;}{&gt;}</i></p>
<dd> rotate the image</p>
<dt><code>-sample </code><i>&lt;geometry&gt;</i></p>
<dd> scale image using pixel sampling</p>
<dt><code>-sampling-factor </code><i>&lt;horizontal_factor&gt;x&lt;vertical_factor&gt;</i></p>
<dd> chroma subsampling factors</p>
<dt><code>-scale </code><i>&lt;geometry&gt;</i></p>
<dd> scale the image.</p>
<dt><code>-scene </code><i>&lt;value&gt;</i></p>
<dd> set scene number</p>
<dt><code>-set </code><i>&lt;attribute&gt; &lt;value&gt;</i></p>
<dd> set an image attribute</p>
<dt><code>+set </code><i>&lt;attribute&gt;</i></p>
<dd> unset an image attribute</p>
<dt><code>-segment </code><i>&lt;cluster threshold&gt;x&lt;smoothing threshold&gt;</i></p>
<dd> segment an image</p>
<dt><code>-shade </code><i>&lt;azimuth&gt;x&lt;elevation&gt;</i></p>
<dd> shade the image using a distant light source</p>
<dt><code>-sharpen </code><i>&lt;radius&gt;{x&lt;sigma&gt;}</i></p>
<dd> sharpen the image</p>
<dt><code>-shave </code><i>&lt;width&gt;x&lt;height&gt;{%}</i></p>
<dd> shave pixels from the image edges</p>
<dt><code>-shear </code><i>&lt;x degrees&gt;x&lt;y degrees&gt;</i></p>
<dd> shear the image along the X or Y axis</p>
<dt><code>-size </code><i>&lt;width&gt;x&lt;height&gt;{+offset}</i></p>
<dd> width and height of the image</p>
<dt><code>-solarize </code><i>&lt;factor&gt;</i></p>
<dd> negate all pixels above the threshold level</p>
<dt><code>-spread </code><i>&lt;amount&gt;</i></p>
<dd> displace image pixels by a random amount</p>
<dt><code>-strip</code></p>
<dd> remove all profiles and text attributes from the image</p>
<dt><code>-stroke </code><i>&lt;color&gt;</i></p>
<dd> color to use when stroking a graphic primitive</p>
<dt><code>-strokewidth </code><i>&lt;value&gt;</i></p>
<dd> set the stroke width</p>
<dt><code>-swirl </code><i>&lt;degrees&gt;</i></p>
<dd> swirl image pixels about the center</p>
<dt><code>-texture </code><i>&lt;filename&gt;</i></p>
<dd> name of texture to tile onto the image background</p>
<dt><code>-threshold </code><i>&lt;value&gt;{%}</i></p>
<dd> threshold the image</p>
<dt><code>-thumbnail </code><i>&lt;width&gt;x&lt;height&gt;{%}{@}{!}{&lt;}{&gt;}</i></p>
<dd> resize an image (quickly)</p>
<dt><code>-tile </code><i>&lt;filename&gt;</i></p>
<dd> tile image when filling a graphic primitive</p>
<dt><code>-transform</code></p>
<dd> transform the image</p>
<dt><code>-transparent </code><i>&lt;color&gt;</i></p>
<dd> make this color transparent within the image</p>
<dt><code>-treedepth </code><i>&lt;value&gt;</i></p>
<dd> tree depth for the color reduction algorithm</p>
<dt><code>-trim</code></p>
<dd> trim an image</p>
<dt><code>-type </code><i>&lt;type&gt;</i></p>
<dd> the image type</p>
<dt><code>-units </code><i>&lt;type&gt;</i></p>
<dd> the units of image resolution</p>
<dt><code>-unsharp </code><i>&lt;radius&gt;{x&lt;sigma&gt;}{+&lt;amount&gt;}{+&lt;threshold&gt;}</i></p>
<dd> sharpen the image with an unsharp mask operator</p>
<dt><code>-use-pixmap</code></p>
<dd> use the pixmap</p>
<dt><code>-verbose</code></p>
<dd> print detailed information about the image</p>
<dt><code>-version</code></p>
<dd> print GraphicsMagick version string</p>
<dt><code>-view </code><i>&lt;string&gt;</i></p>
<dd> FlashPix viewing parameters</p>
<dt><code>-virtual-pixel </code><i>&lt;method&gt;</i></p>
<dd> specify contents of &quot;virtual pixels&quot;</p>
<dt><code>-wave </code><i>&lt;amplitude&gt;x&lt;wavelength&gt;</i></p>
<dd> alter an image along a sine wave</p>
<dt><code>-white-point </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> chromaticity white point</p>
<dt><code>-white-threshold </code><i>red[,green][,blue][,opacity]</i></p>
<dd> pixels above the threshold become white</p>
<dt><code>-write </code><i>&lt;filename&gt;</i></p>
<dd> write an intermediate image [<i>convert, composite</i>] </p>
<p> For a more detailed description of each option, see Options, above.</dl>
<h2>GM DISPLAY</h2>
<p> Display is a machine architecture independent image processing and display program. It can display an image on any workstation screen running an X server. <code>Display</code> can read and write <code>many</code> of the more popular image formats (e.g. <code>JPEG</code>, <code>TIFF</code>, <code>PNM</code>, <code>Photo CD</code>, etc.). </p>
<p> With <code>display</code>, you can perform these functions on an image: </p>
<p>&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>load an image from a file<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>display the next image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>display the former image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>display a sequence of images as a slide show<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>write the image to a file<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>print the image to a&nbsp;<wbr><i>PostScript</i>&nbsp;<wbr>printer<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>delete the image file<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>create a Visual Image Directory<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>select the image to display by its thumbnail rather than name<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>undo last image transformation<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>copy a region of the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>paste a region to the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>restore the image to its original size<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>refresh the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>half the image size<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>double the image size<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>resize the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>crop the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>cut the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>flop image in the horizontal direction<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>flip image in the vertical direction<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>rotate the image 90 degrees clockwise<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>rotate the image 90 degrees counter-clockwise<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>rotate the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>shear the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>roll the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>trim the image edges<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>invert the colors of the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>vary the color brightness<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>vary the color saturation<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>vary the image hue<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>gamma correct the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>sharpen the image contrast<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>dull the image contrast<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>perform histogram equalization on the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>perform histogram normalization on the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>negate the image colors<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>convert the image to grayscale<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>set the maximum number of unique colors in the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>reduce the speckles within an image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>eliminate peak noise from an image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>detect edges within the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>emboss an image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>segment the image by color<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>simulate an oil painting<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>simulate a charcoal drawing<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>annotate the image with text<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>draw on the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>edit an image pixel color<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>edit the image matte information<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>composite an image with another<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>add a border to the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>surround image with an ornamental border<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>apply image processing techniques to a region of interest<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>display information about the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>zoom a portion of the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>show a histogram of the image<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>display image to background of a window<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>set user preferences<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>display information about this program<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>discard all images and exit program<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>change the level of magnification<br />
&nbsp;<wbr>o&nbsp;<wbr>&nbsp;<wbr>display images specified by a World Wide Web&nbsp;<wbr>(WWW)&nbsp;<wbr>uniform resource locator&nbsp;<wbr>(URL) </p>
<h2>EXAMPLES</h2>
<p> To scale an image of a cockatoo to exactly 640 pixels in width and 480 pixels in height and position the window at location (200,200), use: </p>
<p>&nbsp;<wbr>gm display -geometry 640&#215;480+200+200!&nbsp;<wbr>cockatoo.miff </p>
<p> To display an image of a cockatoo without a border centered on a backdrop, use: </p>
<p>&nbsp;<wbr>gm display&nbsp;<wbr>+borderwidth -backdrop cockatoo.miff </p>
<p> To tile a slate texture onto the root window, use: </p>
<p>&nbsp;<wbr>gm display -size 1280&#215;1024 -window root slate.png </p>
<p> To display a visual image directory of all your JPEG images, use: </p>
<p>&nbsp;<wbr>gm display&nbsp;<wbr>&#8216;vid:*.jpg&#8217; </p>
<p> To display a MAP image that is 640 pixels in width and 480 pixels in height with 256 colors, use: </p>
<p>&nbsp;<wbr>gm display -size 640&#215;480+256 cockatoo.map </p>
<p> To display an image of a cockatoo specified with a <code>World Wide Web (WWW)</code> uniform resource locator <code>(URL)</code>, use: </p>
<p>&nbsp;<wbr>gm display&nbsp;<wbr><a href="ftp://wizards.dupont.com/images/cockatoo.jpg">ftp://wizards.dupont.com/images/cockatoo.jpg</a> </p>
<p> To display histogram of an image, use: </p>
<p>&nbsp;<wbr>gm gm convert file.jpg HISTOGRAM:- | gm display &#8211; </p>
<h2>OPTIONS</h2>
<p> Options are processed in command line order. Any option you specify on the command line remains in effect until it is explicitly changed by specifying the option again with a different effect. For example to display three images, the first with 32 colors, the second with an unlimited number of colors, and the third with only 16 colors, use: </p>
<p>&nbsp;<wbr>gm display -colors 32 cockatoo.miff -noop duck.miff<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-colors 16 macaw.miff </p>
<p> <code>Display</code> options can appear on the command line or in your X resources file. See <i><a href="/docs/linux/man/1-x/">X</a>(1)</i>. Options on the command line supersede values specified in your X resources file. </p>
<p> For a more detailed description of each option, see Options, above. </p>
<dl>
<dt><code>-authenticate </code><i>&lt;string&gt;</i></p>
<dd> decrypt image with this password</p>
<dt><code>-backdrop</code></p>
<dd> display the image centered on a backdrop.</p>
<dt><code>-background </code><i>&lt;color&gt;</i></p>
<dd> the background color</p>
<dt><code>-border </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> surround the image with a border of color</p>
<dt><code>-bordercolor </code><i>&lt;color&gt;</i></p>
<dd> the border color</p>
<dt><code>-borderwidth </code><i>&lt;geometry&gt;</i></p>
<dd> the border width</p>
<dt><code>-colormap </code><i>&lt;type&gt;</i></p>
<dd> define the colormap type</p>
<dt><code>-colors </code><i>&lt;value&gt;</i></p>
<dd> preferred number of colors in the image</p>
<dt><code>-colorspace </code><i>&lt;value&gt;</i></p>
<dd> the type of colorspace</p>
<dt><code>-comment </code><i>&lt;string&gt;</i></p>
<dd> annotate an image with a comment</p>
<dt><code>-compress </code><i>&lt;type&gt;</i></p>
<dd> the type of image compression</p>
<dt><code>-contrast</code></p>
<dd> enhance or reduce the image contrast</p>
<dt><code>-crop </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}</i></p>
<dd> preferred size and location of the cropped image</p>
<dt><code>-debug </code><i>&lt;events&gt;</i></p>
<dd> enable debug printout</p>
<dt><code>-define </code><i>&lt;key&gt;{=&lt;value&gt;},&#8230;</i></p>
<dd> add coder/decoder specific options</p>
<dt><code>-delay </code><i>&lt;1/100ths of a second&gt;</i></p>
<dd> display the next image after pausing</p>
<dt><code>-density </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> horizontal and vertical resolution in pixels of the image</p>
<dt><code>-depth </code><i>&lt;value&gt;</i></p>
<dd> depth of the image</p>
<dt><code>-despeckle</code></p>
<dd> reduce the speckles within an image</p>
<dt><code>-display </code><i>&lt;host:display[.screen]&gt;</i></p>
<dd> specifies the X server to contact</p>
<dt><code>-dispose </code><i>&lt;method&gt;</i></p>
<dd> GIF disposal method</p>
<dt><code>-dither</code></p>
<dd> apply Floyd/Steinberg error diffusion to the image</p>
<dt><code>-edge </code><i>&lt;radius&gt;</i></p>
<dd> detect edges within an image</p>
<dt><code>-endian </code><i>&lt;type&gt;</i></p>
<dd> specify endianness (MSB, LSB, or Native) of image</p>
<dt><code>-enhance</code></p>
<dd> apply a digital filter to enhance a noisy image</p>
<dt><code>-filter </code><i>&lt;type&gt;</i></p>
<dd> use this type of filter when resizing an image</p>
<dt><code>-flip</code></p>
<dd> create a &quot;mirror image&quot;</p>
<dt><code>-flop</code></p>
<dd> create a &quot;mirror image&quot;</p>
<dt><code>-font </code><i>&lt;name&gt;</i></p>
<dd> use this font when annotating the image with text</p>
<dt><code>-foreground </code><i>&lt;color&gt;</i></p>
<dd> define the foreground color</p>
<dt><code>-frame </code><i>&lt;width&gt;x&lt;height&gt;+&lt;outer bevel width&gt;+&lt;inner bevel width&gt;</i></p>
<dd> surround the image with an ornamental border</p>
<dt><code>-gamma </code><i>&lt;value&gt;</i></p>
<dd> level of gamma correction</p>
<dt><code>-geometry </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}{@}{!}{^}{&lt;}{&gt;}</i></p>
<dd> Specify dimension, offset, and resize options.</p>
<dt><code>-help</code></p>
<dd> print usage instructions</p>
<dt><code>-iconGeometry </code><i>&lt;geometry&gt;</i></p>
<dd> specify the icon geometry</p>
<dt><code>-iconic</code></p>
<dd> iconic animation</p>
<dt><code>-immutable</code></p>
<dd> make image immutable</p>
<dt><code>-interlace </code><i>&lt;type&gt;</i></p>
<dd> the type of interlacing scheme</p>
<dt><code>-label </code><i>&lt;name&gt;</i></p>
<dd> assign a label to an image</p>
<dt><code>-limit </code><i>&lt;type&gt; &lt;value&gt;</i></p>
<dd> Disk, File, Map, Memory, Pixels, Width, Height or Threads resource limit</p>
<dt><code>-log </code><i>&lt;string&gt;</i></p>
<dd> Specify format for debug log</p>
<dt><code>-magnify </code><i>&lt;factor&gt;</i></p>
<dd> magnify the image</p>
<dt><code>-map </code><i>&lt;type&gt;</i></p>
<dd> display image using this type.</p>
<dt><code>-matte</code></p>
<dd> store matte channel if the image has one</p>
<dt><code>-mattecolor </code><i>&lt;color&gt;</i></p>
<dd> specify the color to be used with the <code>-frame</code> option</p>
<dt><code>-monitor</code></p>
<dd> show progress indication</p>
<dt><code>-monochrome</code></p>
<dd> transform the image to black and white</p>
<dt><code>-name</code></p>
<dd> name an image</p>
<dt><code>-negate</code></p>
<dd> replace every pixel with its complementary color</p>
<dt><code>-noop</code></p>
<dd> NOOP (no option)</p>
<dt><code>-page </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}{!}{&lt;}{&gt;}</i></p>
<dd> size and location of an image canvas</p>
<dt><code>+progress</code></p>
<dd> disable progress monitor and busy cursor</p>
<dt><code>-quality </code><i>&lt;value&gt;</i></p>
<dd> JPEG/MIFF/PNG/TIFF compression level</p>
<dt><code>-raise </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> lighten or darken image edges</p>
<dt><code>-remote</code></p>
<dd> perform a X11 remote operation</p>
<dt><code>-roll </code><i>{+-}&lt;x&gt;{+-}&lt;y&gt;</i></p>
<dd> roll an image vertically or horizontally</p>
<dt><code>-rotate </code><i>&lt;degrees&gt;{&lt;}{&gt;}</i></p>
<dd> rotate the image</p>
<dt><code>-sample </code><i>&lt;geometry&gt;</i></p>
<dd> scale image using pixel sampling</p>
<dt><code>-sampling-factor </code><i>&lt;horizontal_factor&gt;x&lt;vertical_factor&gt;</i></p>
<dd> chroma subsampling factors</p>
<dt><code>-scenes </code><i>&lt;value-value&gt;</i></p>
<dd> range of image scene numbers to read</p>
<dt><code>-set </code><i>&lt;attribute&gt; &lt;value&gt;</i></p>
<dd> set an image attribute</p>
<dt><code>+set </code><i>&lt;attribute&gt;</i></p>
<dd> unset an image attribute</p>
<dt><code>-segment </code><i>&lt;cluster threshold&gt;x&lt;smoothing threshold&gt;</i></p>
<dd> segment an image</p>
<dt><code>-shared-memory</code></p>
<dd> use shared memory</p>
<dt><code>-sharpen </code><i>&lt;radius&gt;{x&lt;sigma&gt;}</i></p>
<dd> sharpen the image</p>
<dt><code>-size </code><i>&lt;width&gt;x&lt;height&gt;{+offset}</i></p>
<dd> width and height of the image</p>
<dt><code>-text-font </code><i>&lt;name&gt;</i></p>
<dd> font for writing fixed-width text</p>
<dt><code>-texture </code><i>&lt;filename&gt;</i></p>
<dd> name of texture to tile onto the image background</p>
<dt><code>-title </code><i>&lt;string&gt;</i></p>
<dd> assign title to displayed image [<i>animate, display, montage</i>]</p>
<dt><code>-treedepth </code><i>&lt;value&gt;</i></p>
<dd> tree depth for the color reduction algorithm</p>
<dt><code>-trim</code></p>
<dd> trim an image</p>
<dt><code>-type </code><i>&lt;type&gt;</i></p>
<dd> the image type</p>
<dt><code>-update </code><i>&lt;seconds&gt;</i></p>
<dd> detect when image file is modified and redisplay.</p>
<dt><code>-use-pixmap</code></p>
<dd> use the pixmap</p>
<dt><code>-verbose</code></p>
<dd> print detailed information about the image</p>
<dt><code>-version</code></p>
<dd> print GraphicsMagick version string</p>
<dt><code>-visual </code><i>&lt;type&gt;</i></p>
<dd> animate images using this X visual type</p>
<dt><code>-window </code><i>&lt;id&gt;</i></p>
<dd> make image the background of a window</p>
<dt><code>-window-group</code></p>
<dd> specify the window group</p>
<dt><code>-write </code><i>&lt;filename&gt;</i></p>
<dd> write the image to a file [<i>display</i>] </p>
<p> For a more detailed description of each option, see Options, above. </p>
</dl>
<h2>MOUSE BUTTONS</h2>
<p> The effects of each button press is described below. Three buttons are required. If you have a two button mouse, button 1 and 3 are returned. Press <code>ALT</code> and button 3 to simulate button 2.</p>
<dl>
<dt><code>1</code></p>
<dd> Press this button to map or unmap the Command widget . See the next section for more information about the Command widget.</p>
<dt><code>2</code></p>
<dd> Press and drag to define a region of the image to magnify.</p>
<dt><code>3</code></p>
<dd> Press and drag to choose from a select set of <code><a href="/docs/linux/man/1-display/">display</a>(1)</code> commands. This button behaves differently if the image being displayed is a visual image directory. Choose a particular tile of the directory and press this button and drag to select a command from a pop-up menu. Choose from these menu items: </p>
<p>&nbsp;<wbr>Open<br />
&nbsp;<wbr>Next<br />
&nbsp;<wbr>Former<br />
&nbsp;<wbr>Delete<br />
&nbsp;<wbr>Update </p>
<p> If you choose <code>Open</code>, the image represented by the tile is displayed. To return to the visual image directory, choose <code>Next</code> from the Command widget (refer to Command Widget). <code>Next</code> and <code>Former</code> moves to the next or former image respectively. Choose <code>Delete</code> to delete a particular image tile. Finally, choose <code>Update</code> to synchronize all the image tiles with their respective images. See montage and miff for more details.</dl>
<h2>COMMAND WIDGET</h2>
<p> The Command widget lists a number of sub-menus and commands. They are </p>
<p>&nbsp;<wbr><code>File</code> </p>
<p>&nbsp;<wbr>Open&#8230;<br />
&nbsp;<wbr>Next<br />
&nbsp;<wbr>Former<br />
&nbsp;<wbr>Select&#8230;<br />
&nbsp;<wbr>Save&#8230;<br />
&nbsp;<wbr>Print&#8230;<br />
&nbsp;<wbr>Delete&#8230;<br />
&nbsp;<wbr>Canvas&#8230;<br />
&nbsp;<wbr>Visual Directory&#8230;<br />
&nbsp;<wbr>Quit </p>
<p>&nbsp;<wbr><code>Edit</code> </p>
<p>&nbsp;<wbr>Undo<br />
&nbsp;<wbr>Redo<br />
&nbsp;<wbr>Cut<br />
&nbsp;<wbr>Copy<br />
&nbsp;<wbr>Paste </p>
<p>&nbsp;<wbr><code>View</code> </p>
<p>&nbsp;<wbr>Half Size<br />
&nbsp;<wbr>Original Size<br />
&nbsp;<wbr>Double Size<br />
&nbsp;<wbr>Resize&#8230;<br />
&nbsp;<wbr>Apply<br />
&nbsp;<wbr>Refresh<br />
&nbsp;<wbr>Restore </p>
<p>&nbsp;<wbr><code>Transform</code> </p>
<p>&nbsp;<wbr>Crop<br />
&nbsp;<wbr>Chop<br />
&nbsp;<wbr>Flop<br />
&nbsp;<wbr>Flip<br />
&nbsp;<wbr>Rotate Right<br />
&nbsp;<wbr>Rotate Left<br />
&nbsp;<wbr>Rotate&#8230;<br />
&nbsp;<wbr>Shear&#8230;<br />
&nbsp;<wbr>Roll&#8230;<br />
&nbsp;<wbr>Trim Edges </p>
<p>&nbsp;<wbr><code>Enhance</code> </p>
<p>&nbsp;<wbr>Hue&#8230;<br />
&nbsp;<wbr>Saturation&#8230;<br />
&nbsp;<wbr>Brightness&#8230;<br />
&nbsp;<wbr>Gamma&#8230;<br />
&nbsp;<wbr>Spiff&#8230;<br />
&nbsp;<wbr>Dull<br />
&nbsp;<wbr>Equalize<br />
&nbsp;<wbr>Normalize<br />
&nbsp;<wbr>Negate<br />
&nbsp;<wbr>GRAYscale<br />
&nbsp;<wbr>Quantize&#8230; </p>
<p>&nbsp;<wbr><code>Effects</code> </p>
<p>&nbsp;<wbr>Despeckle<br />
&nbsp;<wbr>Emboss<br />
&nbsp;<wbr>Reduce Noise<br />
&nbsp;<wbr>Add Noise<br />
&nbsp;<wbr>Sharpen&#8230;<br />
&nbsp;<wbr>Blur&#8230;<br />
&nbsp;<wbr>Threshold&#8230;<br />
&nbsp;<wbr>Edge Detect&#8230;<br />
&nbsp;<wbr>Spread&#8230;<br />
&nbsp;<wbr>Shade&#8230;<br />
&nbsp;<wbr>Raise&#8230;<br />
&nbsp;<wbr>Segment&#8230; </p>
<p>&nbsp;<wbr><code>F/X</code> </p>
<p>&nbsp;<wbr>Solarize&#8230;<br />
&nbsp;<wbr>Swirl&#8230;<br />
&nbsp;<wbr>Implode&#8230;<br />
&nbsp;<wbr>Wave&#8230;<br />
&nbsp;<wbr>Oil Paint&#8230;<br />
&nbsp;<wbr>Charcoal Draw&#8230; </p>
<p>&nbsp;<wbr><code>Image Edit</code> </p>
<p>&nbsp;<wbr>Annotate&#8230;<br />
&nbsp;<wbr>Draw&#8230;<br />
&nbsp;<wbr>Color&#8230;<br />
&nbsp;<wbr>Matte&#8230;<br />
&nbsp;<wbr>Composite&#8230;<br />
&nbsp;<wbr>Add Border&#8230;<br />
&nbsp;<wbr>Add Frame&#8230;<br />
&nbsp;<wbr>Comment&#8230;<br />
&nbsp;<wbr>Launch&#8230;<br />
&nbsp;<wbr>Region of Interest&#8230; </p>
<p>&nbsp;<wbr><code>Miscellany</code> </p>
<p>&nbsp;<wbr>Image Info<br />
&nbsp;<wbr>Zoom Image<br />
&nbsp;<wbr>Show Preview&#8230;<br />
&nbsp;<wbr>Show Histogram<br />
&nbsp;<wbr>Show Matte<br />
&nbsp;<wbr>Background&#8230;<br />
&nbsp;<wbr>Slide Show<br />
&nbsp;<wbr>Preferences&#8230; </p>
<p>&nbsp;<wbr><code>Help</code> </p>
<p>&nbsp;<wbr>Overview<br />
&nbsp;<wbr>Browse Documentation<br />
&nbsp;<wbr>About Display </p>
<p> Menu items with a indented triangle have a sub-menu. They are represented above as the indented items. To access a sub-menu item, move the pointer to the appropriate menu and press button 1 and drag. When you find the desired sub-menu item, release the button and the command is executed. Move the pointer away from the sub-menu if you decide not to execute a particular command.</p>
<h2>KEYBOARD ACCELERATORS</h2>
<p> Accelerators are one or two key presses that effect a particular command. The keyboard accelerators that <code>display</code> understands is: </p>
<p>&nbsp;<wbr>Ctl+O&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to load an image from a file.<br />
&nbsp;<wbr>space&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to display the next image. </p>
<p> If the image is a multi-paged document such as a <i>PostScript</i> document, you can skip ahead several pages by preceding this command with a number. For example to display the fourth page beyond the current page, press 4space. </p>
<p>&nbsp;<wbr>backspace Press to display the former image. </p>
<p> If the image is a multi-paged document such as a <i>PostScript</i> document, you can skip behind several pages by preceding this command with a number. For example to display the fourth page preceding the current page, press 4n. </p>
<p>&nbsp;<wbr>Ctl-S&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to save the image to a file.<br />
&nbsp;<wbr>Ctl-P&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to print the image to a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>PostScript</i>&nbsp;<wbr>printer.<br />
&nbsp;<wbr>Ctl-D&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to delete an image file.<br />
&nbsp;<wbr>Ctl-N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to create a blank canvas.<br />
&nbsp;<wbr>Ctl-Q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to discard all images and exit program.<br />
&nbsp;<wbr>Ctl+Z&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to undo last image transformation.<br />
&nbsp;<wbr>Ctl+R&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to redo last image transformation.<br />
&nbsp;<wbr>Ctl-X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to cut a region of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the image.<br />
&nbsp;<wbr>Ctl-C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to copy a region of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the image.<br />
&nbsp;<wbr>Ctl-V&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to paste a region to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the image.<br />
&nbsp;<wbr>&lt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to halve the image size.<br />
&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to return to the original image size.<br />
&nbsp;<wbr>&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to double the image size.<br />
&nbsp;<wbr>%&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to resize the image to a width and height<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>you specify.<br />
&nbsp;<wbr>Cmd-A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to make any image transformations<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>permanent.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>By default, any image size transformations are<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>applied to the original image to create the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>image displayed on the X server.&nbsp;<wbr>&nbsp;<wbr>However, the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>transformations are not permanent&nbsp;<wbr>(i.e. the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>original image does not change size only the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>X image does). For example, if you press&nbsp;<wbr>&quot;&gt;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the X image will appear to double in size, but<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the original image will in fact remain the same<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>size.&nbsp;<wbr>&nbsp;<wbr>To force the original image to double in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>size, press&nbsp;<wbr>&quot;&gt;&quot;&nbsp;<wbr>followed by&nbsp;<wbr>&quot;Cmd-A&quot;.<br />
&nbsp;<wbr>@&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to refresh the image window.<br />
&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to crop the image.<br />
&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to chop the image.<br />
&nbsp;<wbr>H&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to flop image in the horizontal direction.<br />
&nbsp;<wbr>V&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to flip image in the vertical direction.<br />
&nbsp;<wbr>/&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to rotate the image 90 degrees clockwise.<br />
&nbsp;<wbr>\&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to rotate the image 90 degrees<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>counter-clockwise.<br />
&nbsp;<wbr>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to rotate the image<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the number of degrees you specify.<br />
&nbsp;<wbr>S&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to shear the image the number of degrees<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>you specify.<br />
&nbsp;<wbr>R&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to roll the image.<br />
&nbsp;<wbr>T&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to trim the image edges.<br />
&nbsp;<wbr>Shft-H&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to vary the color hue.<br />
&nbsp;<wbr>Shft-S&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to vary the color saturation.<br />
&nbsp;<wbr>Shft-L&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to vary the image brightness.<br />
&nbsp;<wbr>Shft-G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to gamma correct the image.<br />
&nbsp;<wbr>Shft-C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to spiff up the image contrast.<br />
&nbsp;<wbr>Shft-Z&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to dull the image contrast.<br />
&nbsp;<wbr>=&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to perform histogram equalization on<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the image.<br />
&nbsp;<wbr>Shft-N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to perform histogram normalization on<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the image.<br />
&nbsp;<wbr>Shft-~&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to negate the colors of the image.<br />
&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to convert the image colors to gray.<br />
&nbsp;<wbr>Shft-#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to set the maximum number of unique<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>colors in the image.<br />
&nbsp;<wbr>F2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to reduce the speckles in an image.<br />
&nbsp;<wbr>F2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to emboss an image.<br />
&nbsp;<wbr>F4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to eliminate peak noise from an image.<br />
&nbsp;<wbr>F5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to add noise to an image.<br />
&nbsp;<wbr>F6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to sharpen an image.<br />
&nbsp;<wbr>F7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to blur image an image.<br />
&nbsp;<wbr>F8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to threshold the image.<br />
&nbsp;<wbr>F9&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to detect edges within an image.<br />
&nbsp;<wbr>F10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to displace pixels by a random amount.<br />
&nbsp;<wbr>F11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to shade the image using a distant light<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>source.<br />
&nbsp;<wbr>F12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to lighten or darken image edges to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>create a 3-D effect.<br />
&nbsp;<wbr>F13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to segment the image by color.<br />
&nbsp;<wbr>Meta-S&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to swirl image pixels about the center.<br />
&nbsp;<wbr>Meta-I&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to implode image pixels about the center.<br />
&nbsp;<wbr>Meta-W&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to alter an image along a sine wave.<br />
&nbsp;<wbr>Meta-P&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to simulate an oil painting.<br />
&nbsp;<wbr>Meta-C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to simulate a charcoal drawing.<br />
&nbsp;<wbr>Alt-X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to composite the image<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>with another.<br />
&nbsp;<wbr>Alt-A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to annotate the image with text.<br />
&nbsp;<wbr>Alt-D&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to draw a line on the image.<br />
&nbsp;<wbr>Alt-P&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to edit an image pixel color.<br />
&nbsp;<wbr>Alt-M&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to edit the image matte information.<br />
&nbsp;<wbr>Alt-X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to composite the image with another.<br />
&nbsp;<wbr>Alt-A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to add a border to the image.<br />
&nbsp;<wbr>Alt-F&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to add a ornamental frame to the image.<br />
&nbsp;<wbr>Alt-Shft-!&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to add an image comment.<br />
&nbsp;<wbr>Ctl-A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to apply image processing techniques to a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>region of interest.<br />
&nbsp;<wbr>Shft-?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to display information about the image.<br />
&nbsp;<wbr>Shft-+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to map the zoom image window.<br />
&nbsp;<wbr>Shft-P&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to preview an image enhancement, effect,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or f/x.<br />
&nbsp;<wbr>F1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to display helpful information about<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the&nbsp;<wbr>&quot;display&quot;&nbsp;<wbr>utility.<br />
&nbsp;<wbr>Find&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to browse documentation about<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>GraphicsMagick.<br />
&nbsp;<wbr>1-9&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Press to change the level of magnification. </p>
<p> Use the arrow keys to move the image one pixel up, down, left, or right within the magnify window. Be sure to first map the magnify window by pressing button 2. </p>
<p> Press ALT and one of the arrow keys to trim off one pixel from any side of the image.</p>
<h2>X RESOURCES</h2>
<p> <code>Display</code> options can appear on the command line or in your X resource file. Options on the command line supersede values specified in your X resource file. See <i><a href="/docs/linux/man/1-x/">X</a>(1)</i> for more information on X resources. </p>
<p> Most <code>display</code> options have a corresponding X resource. In addition, <code>display</code> uses the following X resources:</p>
<dl>
<dt><code>background </code><i>(class Background)</i></p>
<dd> Specifies the preferred color to use for the Image window background. The default is #ccc.</p>
<dt><code>borderColor </code><i>(class BorderColor)</i></p>
<dd> Specifies the preferred color to use for the Image window border. The default is #ccc.</p>
<dt><code>borderWidth </code><i>(class BorderWidth)</i></p>
<dd> Specifies the width in pixels of the image window border. The default is 2.</p>
<dt><code>browseCommand </code><i>(class browseCommand)</i></p>
<dd> Specifies the name of the preferred browser when displaying GraphicsMagick documentation. The default is netscape %s.</p>
<dt><code>confirmExit </code><i>(class ConfirmExit)</i></p>
<dd> <code>Display</code> pops up a dialog box to confirm exiting the program when exiting the program. Set this resource to False to exit without a confirmation.</p>
<dt><code>displayGamma </code><i>(class DisplayGamma)</i></p>
<dd> Specifies the gamma of the X server. You can apply separate gamma values to the red, green, and blue channels of the image with a gamma value list delineated with slashes (i.e. 1.7/2.3/1.2). The default is 2.2.</p>
<dt><code>displayWarnings </code><i>(class DisplayWarnings)</i></p>
<dd> <code>Display</code> pops up a dialog box whenever a warning message occurs. Set this resource to False to ignore warning messages.</p>
<dt><code>font </code><i>(class FontList)</i></p>
<dd> Specifies the name of the preferred font to use in normal formatted text. The default is 14 point Helvetica.</p>
<dt><code>font[1-9] </code><i>(class Font[1-9])</i></p>
<dd> Specifies the name of the preferred font to use when annotating the image window with text. The default fonts are fixed, variable, 5&#215;8, 6&#215;10, 7x13bold, 8x13bold, 9x15bold, 10&#215;20, and 12&#215;24.</p>
<dt><code>foreground </code><i>(class Foreground)</i></p>
<dd> Specifies the preferred color to use for text within the image window. The default is black.</p>
<dt><code>gammaCorrect </code><i>(class gammaCorrect)</i></p>
<dd> This resource, if true, will lighten or darken an image of known gamma to match the gamma of the display (see resource <code>displayGamma</code>). The default is True.</p>
<dt><code>geometry </code><i>(class Geometry)</i></p>
<dd> Specifies the preferred size and position of the image window. It is not necessarily obeyed by all window managers. </p>
<p> Offsets, if present, are handled in <i><a href="/docs/linux/man/1-x/">X</a>(1)</i> style. A negative x offset is measured from the right edge of the screen to the right edge of the icon, and a negative y offset is measured from the bottom edge of the screen to the bottom edge of the icon.</p>
<dt><code>iconGeometry </code><i>(class IconGeometry)</i></p>
<dd> Specifies the preferred size and position of the application when iconified. It is not necessarily obeyed by all window managers. </p>
<p> Offsets, if present, are handled in the same manner as in class Geometry.</p>
<dt><code>iconic </code><i>(class Iconic)</i></p>
<dd> This resource indicates that you would prefer that the application&#8217;s windows initially not be visible as if the windows had be immediately iconified by you. Window managers may choose not to honor the application&#8217;s request.</p>
<dt><code>magnify </code><i>(class Magnify)</i></p>
<dd> specifies an integral factor by which the image should be enlarged. The default is 3. This value only affects the magnification window which is invoked with button number 3 after the image is displayed.</p>
<dt><code>matteColor </code><i>(class MatteColor)</i></p>
<dd> Specify the color of windows. It is used for the backgrounds of windows, menus, and notices. A 3D effect is achieved by using highlight and shadow colors derived from this color. Default value: #697B8F.</p>
<dt><code>name </code><i>(class Name)</i></p>
<dd> This resource specifies the name under which resources for the application should be found. This resource is useful in shell aliases to distinguish between invocations of an application, without resorting to creating links to alter the executable file name. The default is the application name.</p>
<dt><code>pen[1-9] </code><i>(class Pen[1-9])</i></p>
<dd> Specifies the color of the preferred font to use when annotating the image window with text. The default colors are black, blue, green, cyan, gray, red, magenta, yellow, and white.</p>
<dt><code>printCommand </code><i>(class PrintCommand)</i></p>
<dd> This command is executed whenever Print is issued. In general, it is the command to print <i>PostScript</i> to your printer. Default value: lp -c -s %i.</p>
<dt><code>sharedMemory </code><i>(class SharedMemory)</i></p>
<dd> This resource specifies whether display should attempt use shared memory for pixmaps. GraphicsMagick must be compiled with shared memory support, and the display must support the MIT-SHM extension. Otherwise, this resource is ignored. The default is True.</p>
<dt><code>textFont </code><i>(class textFont)</i></p>
<dd> Specifies the name of the preferred font to use in fixed (typewriter style) formatted text. The default is 14 point Courier.</p>
<dt><code>title </code><i>(class Title)</i></p>
<dd> This resource specifies the title to be used for the image window. This information is sometimes used by a window manager to provide a header identifying the window. The default is the image file name.</p>
<dt><code>undoCache </code><i>(class UndoCache)</i></p>
<dd> Specifies, in mega-bytes, the amount of memory in the undo edit cache. Each time you modify the image it is saved in the undo edit cache as long as memory is available. You can subsequently <i>undo</i> one or more of these transformations. The default is 16 Megabytes.</p>
<dt><code>usePixmap </code><i>(class UsePixmap)</i></p>
<dd> Images are maintained as a XImage by default. Set this resource to True to utilize a server Pixmap instead. This option is useful if your image exceeds the dimensions of your server screen and you intend to pan the image. Panning is much faster with Pixmaps than with a XImage. Pixmaps are considered a precious resource, use them with discretion. </p>
<p> To set the geometry of the Magnify or Pan or window, use the geometry resource. For example, to set the Pan window geometry to 256&#215;256, use: </p>
<p>&nbsp;<wbr>gm display.pan.geometry: 256&#215;256 </p>
</dl>
<h2>IMAGE LOADING</h2>
<p> To select an image to display, choose <code>Open</code> of the <code>File</code> sub-menu from the Command widget. A file browser is displayed. To choose a particular image file, move the pointer to the filename and press any button. The filename is copied to the text window. Next, press <code>Open</code> or press the <code>RETURN</code> key. Alternatively, you can type the image file name directly into the text window. To descend directories, choose a directory name and press the button twice quickly. A scrollbar allows a large list of filenames to be moved through the viewing area if it exceeds the size of the list area. </p>
<p> You can trim the list of file names by using shell globbing characters. For example, type *.jpg to list only files that end with .jpg. </p>
<p> To select your image from the X server screen instead of from a file, Choose <code>Grab</code> of the <code>Open</code> widget.</p>
<h2>VISUAL IMAGE DIRECTORY</h2>
<p> To create a Visual Image Directory, choose Visual Directory of the <code>File</code> sub-menu from the Command widget . A file browser is displayed. To create a Visual Image Directory from all the images in the current directory, press <code>Directory</code> or press the <code>RETURN key</code>. Alternatively, you can select a set of image names by using shell globbing characters. For example, type *.jpg to include only files that end with .jpg. To descend directories, choose a directory name and press the button twice quickly. A scrollbar allows a large list of filenames to be moved through the viewing area if it exceeds the size of the list area. </p>
<p> After you select a set of files, they are turned into thumbnails and tiled onto a single image. Now move the pointer to a particular thumbnail and press <code>button 3</code> and drag. Finally, select Open. The image represented by the thumbnail is displayed at its full size. Choose <code>Next</code> from the <code>File</code> sub-menu of the Command widget to return to the Visual Image Directory.</p>
<h2>IMAGE CUTTING</h2>
<p> Note that cut information for image window is not retained for colormapped X server visuals (e.g. <i>StaticColor</i>, <i>StaticColor</i>, <i>GRAYScale</i>, <i>PseudoColor</i>). Correct cutting behavior may require a <i>TrueColor</i> or <i>DirectColor</i> visual or a <i>Standard Colormap</i>. </p>
<p> To begin, press choose <code>Cut</code> of the <code>Edit</code> sub-menu from the Command widget. Alternatively, press <code>F3</code> in the image window. </p>
<p> A small window appears showing the location of the cursor in the image window. You are now in cut mode. In cut mode, the Command widget has these options: </p>
<p>&nbsp;<wbr><code>Help</code><br />
&nbsp;<wbr><code>Dismiss</code> </p>
<p> To define a cut region, press button 1 and drag. The cut region is defined by a highlighted rectangle that expands or contracts as it follows the pointer. Once you are satisfied with the cut region, release the button. You are now in rectify mode. In rectify mode, the Command widget has these options: </p>
<p>&nbsp;<wbr><code>Cut</code><br />
&nbsp;<wbr><code>Help</code><br />
&nbsp;<wbr><code>Dismiss</code> </p>
<p> You can make adjustments by moving the pointer to one of the cut rectangle corners, pressing a button, and dragging. Finally, press Cut to commit your copy region. To exit without cutting the image, press Dismiss.</p>
<h2>IMAGE COPYING</h2>
<p> To begin, press choose <code>Copy</code> of the <code>Edit</code> sub-menu from the Command widget. Alternatively, press <code>F4</code> in the image window. </p>
<p> A small window appears showing the location of the cursor in the image window. You are now in copy mode. In copy mode, the Command widget has these options: </p>
<p>&nbsp;<wbr>Help<br />
&nbsp;<wbr>Dismiss </p>
<p> To define a copy region, press button 1 and drag. The copy region is defined by a highlighted rectangle that expands or contracts as it follows the pointer. Once you are satisfied with the copy region, release the button. You are now in rectify mode. In rectify mode, the Command widget has these options: </p>
<p>&nbsp;<wbr>Copy<br />
&nbsp;<wbr>Help<br />
&nbsp;<wbr>Dismiss </p>
<p> You can make adjustments by moving the pointer to one of the copy rectangle corners, pressing a button, and dragging. Finally, press Copy to commit your copy region. To exit without copying the image, press Dismiss.</p>
<h2>IMAGE PASTING</h2>
<p> To begin, press choose <code>Paste</code> of the <code>Edit</code> sub-menu from the Command widget. Alternatively, press <code>F5</code> in the image window. </p>
<p> A small window appears showing the location of the cursor in the image window. You are now in Paste mode. To exit immediately, press Dismiss. In Paste mode, the Command widget has these options: </p>
<p>&nbsp;<wbr><code>Operators</code> </p>
<p>&nbsp;<wbr>over<br />
&nbsp;<wbr>in<br />
&nbsp;<wbr>out<br />
&nbsp;<wbr>atop<br />
&nbsp;<wbr>xor<br />
&nbsp;<wbr>plus<br />
&nbsp;<wbr>minus<br />
&nbsp;<wbr>add<br />
&nbsp;<wbr>subtract<br />
&nbsp;<wbr>difference<br />
&nbsp;<wbr>multiply<br />
&nbsp;<wbr>bumpmap<br />
&nbsp;<wbr>replace </p>
<p>&nbsp;<wbr><code>Help</code><br />
&nbsp;<wbr><code>Dismiss</code> </p>
<p> Choose a composite operation from the <code>Operators</code> sub-menu of the Command widget. How each operator behaves is described below. <i>image window</i> is the image currently displayed on your X server and <i>image</i> is the image obtained with the File Browser widget.</p>
<dl>
<dt><code>over</code></p>
<dd> The result is the union of the two image shapes, with <i>image</i> obscuring <i>image window</i> in the region of overlap.</p>
<dt><code>in</code></p>
<dd> The result is simply <i>image</i> cut by the shape of <i>image window</i>. None of the image data of image window is in the result.</p>
<dt><code>out</code></p>
<dd> The resulting image is <i>image</i> with the shape of <i>image window</i> cut out.</p>
<dt><code>atop</code></p>
<dd> The result is the same shape as <i>image window</i>, with <i>image</i> obscuring <i>image window</i> where the image shapes overlap. Note this differs from over because the portion of image outside <i>image window</i>&#8216;s shape does not appear in the result.</p>
<dt><code>xor</code></p>
<dd> The result is the image data from both <i>image</i> and <i>image window</i> that is outside the overlap region. The overlap region is blank.</p>
<dt><code>plus</code></p>
<dd> The result is just the sum of the image data. Output values are cropped to the maximum value (no overflow). This operation is independent of the matte channels.</p>
<dt><code>minus</code></p>
<dd> The result of <i>image</i> &#8211; <i>image window</i>, with underflow cropped to zero. The matte channel is ignored (set to opaque, full coverage).</p>
<dt><code>add</code></p>
<dd> The result of <i>image</i> + <i>image window</i>, with overflow wrapping around (mod MaxRGB+1).</p>
<dt><code>subtract</code></p>
<dd> The result of <i>image</i> &#8211; <i>image window</i>, with underflow wrapping around (mod MaxRGB+1). The add and subtract operators can be used to perform reversible transformations.</p>
<dt><code>difference</code></p>
<dd> The result of abs(<i>image</i> &#8211; <i>image window</i>). This is useful for comparing two very similar images.</p>
<dt><code>multiply</code></p>
<dd> The result of <i>image</i> * <i>image window</i>. This is useful for the creation of drop-shadows.</p>
<dt><code>bumpmap</code></p>
<dd> The result of <i>image window</i> shaded by <i>window</i>.</p>
<dt><code>replace</code></p>
<dd> The resulting image is <i>image window</i> replaced with <i>image</i>. Here the matte information is ignored. </p>
<p> The image compositor requires a matte, or alpha channel in the image for some operations. This extra channel usually defines a mask which represents a sort of a cookie-cutter for the image. This is the case when matte is 255 (full coverage) for pixels inside the shape, zero outside, and between zero and 255 on the boundary. If image does not have a matte channel, it is initialized with 0 for any pixel matching in color to pixel location (0,0), otherwise 255. See Matte Editing for a method of defining a matte channel. </p>
<p> Note that matte information for image window is not retained for colormapped X server visuals (e.g. <i>StaticColor, StaticColor, GrayScale, PseudoColor</i>). Correct compositing behavior may require a <i>TrueColor</i> or <i>DirectColor</i> visual or a <i>Standard Colormap</i>. </p>
<p> Choosing a composite operator is optional. The default operator is replace. However, you must choose a location to composite your image and press button 1. Press and hold the button before releasing and an outline of the image will appear to help you identify your location. </p>
<p> The actual colors of the pasted image is saved. However, the color that appears in image window may be different. For example, on a monochrome screen image window will appear black or white even though your pasted image may have many colors. If the image is saved to a file it is written with the correct colors. To assure the correct colors are saved in the final image, any <i>PseudoClass</i> image is promoted to <i>DirectClass</i>. To force a <i>PseudoClass</i> image to remain <i>PseudoClass</i>, use <code>-colors</code>.</dl>
<h2>IMAGE CROPPING</h2>
<p> To begin, press choose <code>Crop</code> of the <code>Transform</code> submenu from the Command widget. Alternatively, press C in the image window. </p>
<p> A small window appears showing the location of the cursor in the image window. You are now in crop mode. In crop mode, the Command widget has these options: </p>
<p>&nbsp;<wbr><code>Help</code><br />
&nbsp;<wbr><code>Dismiss</code> </p>
<p> To define a cropping region, press button 1 and drag. The cropping region is defined by a highlighted rectangle that expands or contracts as it follows the pointer. Once you are satisfied with the cropping region, release the button. You are now in rectify mode. In rectify mode, the Command widget has these options: </p>
<p>&nbsp;<wbr><code>Crop</code><br />
&nbsp;<wbr><code>Help</code><br />
&nbsp;<wbr><code>Dismiss</code> </p>
<p> You can make adjustments by moving the pointer to one of the cropping rectangle corners, pressing a button, and dragging. Finally, press Crop to commit your cropping region. To exit without cropping the image, press Dismiss.</p>
<h2>IMAGE CHOPPING</h2>
<p> An image is chopped interactively. There is no command line argument to chop an image. To begin, choose <code>Chop</code> of the <code>Transform</code> sub-menu from the Command widget. Alternatively, press [ in the Image window. </p>
<p> You are now in <code>Chop</code> mode. To exit immediately, press <code>Dismiss</code>. In Chop mode, the Command widget has these options: </p>
<p>&nbsp;<wbr><code>Direction</code> </p>
<p>&nbsp;<wbr>horizontal<br />
&nbsp;<wbr>vertical </p>
<p>&nbsp;<wbr><code>Help</code><br />
&nbsp;<wbr><code>Dismiss</code> </p>
<p> If the you choose the horizontal direction (this is the default), the area of the image between the two horizontal endpoints of the chop line is removed. Otherwise, the area of the image between the two vertical endpoints of the chop line is removed. </p>
<p> Select a location within the image window to begin your chop, press and hold any button. Next, move the pointer to another location in the image. As you move a line will connect the initial location and the pointer. When you release the button, the area within the image to chop is determined by which direction you choose from the Command widget. </p>
<p> To cancel the image chopping, move the pointer back to the starting point of the line and release the button.</p>
<h2>IMAGE ROTATION</h2>
<p> Press the / key to rotate the image 90 degrees or \ to rotate -90 degrees. To interactively choose the degree of rotation, choose <code>Rotate&#8230;</code> of the <code>Transform</code> submenu from the Command Widget. Alternatively, press * in the image window. </p>
<p> A small horizontal line is drawn next to the pointer. You are now in rotate mode. To exit immediately, press Dismiss. In rotate mode, the Command widget has these options: </p>
<p>&nbsp;<wbr><code>Pixel Color</code> </p>
<p>&nbsp;<wbr>black<br />
&nbsp;<wbr>blue<br />
&nbsp;<wbr>cyan<br />
&nbsp;<wbr>green<br />
&nbsp;<wbr>gray<br />
&nbsp;<wbr>red<br />
&nbsp;<wbr>magenta<br />
&nbsp;<wbr>yellow<br />
&nbsp;<wbr>white<br />
&nbsp;<wbr>Browser&#8230; </p>
<p>&nbsp;<wbr><code>Direction</code> </p>
<p>&nbsp;<wbr>horizontal<br />
&nbsp;<wbr>vertical </p>
<p>&nbsp;<wbr><code>Help</code><br />
&nbsp;<wbr><code>Dismiss</code> </p>
<p> Choose a background color from the Pixel Color sub-menu. Additional background colors can be specified with the color browser. You can change the menu colors by setting the X resources pen1 through pen9. </p>
<p> If you choose the color browser and press <code>Grab</code>, you can select the background color by moving the pointer to the desired color on the screen and press any button. </p>
<p> Choose a point in the image window and press this button and hold. Next, move the pointer to another location in the image. As you move a line connects the initial location and the pointer. When you release the button, the degree of image rotation is determined by the slope of the line you just drew. The slope is relative to the direction you choose from the Direction sub-menu of the Command widget. </p>
<p> To cancel the image rotation, move the pointer back to the starting point of the line and release the button.</p>
<h2>IMAGE ANNOTATION</h2>
<p> An image is annotated interactively. There is no command line argument to annotate an image. To begin, choose <code>Annotate</code> of the <code>Image Edit</code> sub-menu from the Command widget. Alternatively, press a in the image window. </p>
<p> A small window appears showing the location of the cursor in the image window. You are now in annotate mode. To exit immediately, press Dismiss. In annotate mode, the Command widget has these options: </p>
<p>&nbsp;<wbr> <code>Font Name</code> </p>
<p>&nbsp;<wbr> fixed<br />
&nbsp;<wbr> variable<br />
&nbsp;<wbr> 5&#215;8<br />
&nbsp;<wbr> 6&#215;10<br />
&nbsp;<wbr> 7x13bold<br />
&nbsp;<wbr> 8x13bold<br />
&nbsp;<wbr> 9x15bold<br />
&nbsp;<wbr> 10&#215;20<br />
&nbsp;<wbr> 12&#215;24<br />
&nbsp;<wbr> Browser&#8230; </p>
<p>&nbsp;<wbr> <code>Font Color</code> </p>
<p>&nbsp;<wbr> black<br />
&nbsp;<wbr> blue<br />
&nbsp;<wbr> cyan<br />
&nbsp;<wbr> green<br />
&nbsp;<wbr> gray<br />
&nbsp;<wbr> red<br />
&nbsp;<wbr> magenta<br />
&nbsp;<wbr> yellow<br />
&nbsp;<wbr> white<br />
&nbsp;<wbr> transparent<br />
&nbsp;<wbr> Browser&#8230; </p>
<p>&nbsp;<wbr> <code>Box Color</code> </p>
<p>&nbsp;<wbr> black<br />
&nbsp;<wbr> blue<br />
&nbsp;<wbr> cyan<br />
&nbsp;<wbr> green<br />
&nbsp;<wbr> gray<br />
&nbsp;<wbr> red<br />
&nbsp;<wbr> magenta<br />
&nbsp;<wbr> yellow<br />
&nbsp;<wbr> white<br />
&nbsp;<wbr> transparent<br />
&nbsp;<wbr> Browser&#8230; </p>
<p>&nbsp;<wbr> <code>Rotate Text</code> </p>
<p>&nbsp;<wbr> -90<br />
&nbsp;<wbr> -45<br />
&nbsp;<wbr> -30<br />
&nbsp;<wbr> 0<br />
&nbsp;<wbr> 30<br />
&nbsp;<wbr> 45<br />
&nbsp;<wbr> 90<br />
&nbsp;<wbr> 180<br />
&nbsp;<wbr> Dialog&#8230; </p>
<p>&nbsp;<wbr> <code>Help</code><br />
&nbsp;<wbr> <code>Dismiss</code> </p>
<p> Choose a font name from the <code>Font Name</code> sub-menu. Additional font names can be specified with the font browser. You can change the menu names by setting the X resources font1 through font9. </p>
<p> Choose a font color from the <code>Font Color</code> sub-menu. Additional font colors can be specified with the color browser. You can change the menu colors by setting the X resources pen1 through pen9. </p>
<p> If you select the color browser and press <code>Grab</code>, you can choose the font color by moving the pointer to the desired color on the screen and press any button. </p>
<p> If you choose to rotate the text, choose <code>Rotate Text</code> from the menu and select an angle. Typically you will only want to rotate one line of text at a time. Depending on the angle you choose, subsequent lines may end up overwriting each other. </p>
<p> Choosing a font and its color is optional. The default font is fixed and the default color is black. However, you must choose a location to begin entering text and press a button. An underscore character will appear at the location of the pointer. The cursor changes to a pencil to indicate you are in text mode. To exit immediately, press Dismiss. </p>
<p> In text mode, any key presses will display the character at the location of the underscore and advance the underscore cursor. Enter your text and once completed press Apply to finish your image annotation. To correct errors press <code>BACK SPACE</code>. To delete an entire line of text, press <code>DELETE</code>. Any text that exceeds the boundaries of the image window is automatically continued onto the next line. </p>
<p> The actual color you request for the font is saved in the image. However, the color that appears in your Image window may be different. For example, on a monochrome screen the text will appear black or white even if you choose the color red as the font color. However, the image saved to a file with <code>-write</code> is written with red lettering. To assure the correct color text in the final image, any <i>PseudoClass</i> image is promoted to <i>DirectClass</i> (see <a href="/docs/linux/man/5-miff/">miff</a>(5)). To force a <i>PseudoClass</i> image to remain <i>PseudoClass</i>, use <code>-colors</code>.</p>
<h2>IMAGE COMPOSITING</h2>
<p> An image composite is created interactively. <code>There is no command line argument to composite an image</code>. To begin, choose <code>Composite</code> of the <code>Image Edit</code> from the Command widget. Alternatively, press x in the Image window. </p>
<p> First a popup window is displayed requesting you to enter an image name. Press <code>Composite</code>, <code>Grab</code> or type a file name. Press <code>Cancel</code> if you choose not to create a composite image. When you choose <code>Grab</code>, move the pointer to the desired window and press any button. </p>
<p> If the <code>Composite</code> image does not have any matte information, you are informed and the file browser is displayed again. Enter the name of a mask image. The image is typically grayscale and the same size as the composite image. If the image is not grayscale, it is converted to grayscale and the resulting intensities are used as matte information. </p>
<p> A small window appears showing the location of the cursor in the image window. You are now in composite mode. To exit immediately, press Dismiss. In composite mode, the Command widget has these options: </p>
<p>&nbsp;<wbr> <code>Operators</code> </p>
<p>&nbsp;<wbr> over<br />
&nbsp;<wbr> in<br />
&nbsp;<wbr> out<br />
&nbsp;<wbr> atop<br />
&nbsp;<wbr> xor<br />
&nbsp;<wbr> plus<br />
&nbsp;<wbr> minus<br />
&nbsp;<wbr> add<br />
&nbsp;<wbr> subtract<br />
&nbsp;<wbr> difference<br />
&nbsp;<wbr> bumpmap<br />
&nbsp;<wbr> replace </p>
<p>&nbsp;<wbr> <code>Blend</code><br />
&nbsp;<wbr> <code>Displace</code><br />
&nbsp;<wbr> <code>Help</code><br />
&nbsp;<wbr> <code>Dismiss</code> </p>
<p> Choose a composite operation from the Operators sub-menu of the Command widget. How each operator behaves is described below. image window is the image currently displayed on your X server and image is the image obtained</p>
<dl>
<dt><code>over</code></p>
<dd> The result is the union of the two image shapes, with <i>image</i> obscuring <i>image window</i> in the region of overlap.</p>
<dt><code>in</code></p>
<dd> The result is simply <i>image</i> cut by the shape of <i>image window</i>. None of the image data of image window is in the result.</p>
<dt><code>out</code></p>
<dd> The resulting image is <i>image</i> with the shape of <i>image window</i> cut out.</p>
<dt><code>atop</code></p>
<dd> The result is the same shape as <i>image window</i>, with <i>image</i> obscuring <i>image window</i> where the image shapes overlap. Note this differs from over because the portion of image outside <i>image window</i>&#8216;s shape does not appear in the result.</p>
<dt><code>xor</code></p>
<dd> The result is the image data from both <i>image</i> and <i>image window</i> that is outside the overlap region. The overlap region is blank.</p>
<dt><code>plus</code></p>
<dd> The result is just the sum of the image data. Output values are cropped to 255 (no overflow). This operation is independent of the matte channels.</p>
<dt><code>minus</code></p>
<dd> The result of <i>image</i> &#8211; <i>image window</i>, with underflow cropped to zero. The matte channel is ignored (set to 255, full coverage).</p>
<dt><code>add</code></p>
<dd> The result of <i>image</i> + <i>image window</i>, with overflow wrapping around (mod 256).</p>
<dt><code>subtract</code></p>
<dd> The result of <i>image</i> &#8211; <i>image window</i>, with underflow wrapping around (mod 256). The add and subtract operators can be used to perform reversible transformations.</p>
<dt><code>difference</code></p>
<dd> The result of abs(<i>image</i> &#8211; <i>image window</i>). This is useful for comparing two very similar images.</p>
<dt><code>bumpmap</code></p>
<dd> The result of <i>image window</i> shaded by <i>window</i>.</p>
<dt><code>replace</code></p>
<dd> The resulting image is <i>image window</i> replaced with <i>image</i>. Here the matte information is ignored. </p>
<p> The image compositor requires a matte, or alpha channel in the image for some operations. This extra channel usually defines a mask which represents a sort of a cookie-cutter for the image. This is the case when matte is 255 (full coverage) for pixels inside the shape, zero outside, and between zero and 255 on the boundary. If image does not have a matte channel, it is initialized with 0 for any pixel matching in color to pixel location (0,0), otherwise 255. See Matte Editing for a method of defining a matte channel. </p>
<p> If you choose <code>blend</code>, the composite operator becomes <code>over</code>. The image matte channel percent transparency is initialized to factor. The image window is initialized to (100-factor). Where factor is the value you specify in the Dialog widget. </p>
<p> <code>Displace</code> shifts the image pixels as defined by a displacement map. With this option, <i>image</i> is used as a displacement map. Black, within the displacement map, is a maximum positive displacement. White is a maximum negative displacement and middle gray is neutral. The displacement is scaled to determine the pixel shift. By default, the displacement applies in both the horizontal and vertical directions. However, if you specify <i>mask</i>, <i>image</i> is the horizontal X displacement and <i>mask</i> the vertical Y displacement. </p>
<p> Note that matte information for image window is not retained for colormapped X server visuals (e.g. <i>StaticColor, StaticColor, GrayScale, PseudoColor</i>). Correct compositing behavior may require a <i>TrueColor</i> or <i>DirectColor</i> visual or a <i>Standard Colormap</i>. </p>
<p> Choosing a composite operator is optional. The default operator is replace. However, you must choose a location to composite your image and press button 1. Press and hold the button before releasing and an outline of the image will appear to help you identify your location. </p>
<p> The actual colors of the composite image is saved. However, the color that appears in image window may be different. For example, on a monochrome screen Image window will appear black or white even though your composited image may have many colors. If the image is saved to a file it is written with the correct colors. To assure the correct colors are saved in the final image, any PseudoClass image is promoted to <i>DirectClass</i> (see miff). To force a <i>PseudoClass</i> image to remain <i>PseudoClass</i>, use <code>-colors</code>.</dl>
<h2>COLOR EDITING</h2>
<p> Changing the the color of a set of pixels is performed interactively. There is no command line argument to edit a pixel. To begin, choose <code>Color</code> from the <code>Image Edit</code> submenu of the Command widget. Alternatively, press c in the image window. </p>
<p> A small window appears showing the location of the cursor in the image window. You are now in color edit mode. To exit immediately, press <code>Dismiss</code>. In color edit mode, the <code>Command widget</code> has these options: </p>
<p>&nbsp;<wbr> <code>Method</code> </p>
<p>&nbsp;<wbr> point<br />
&nbsp;<wbr> replace<br />
&nbsp;<wbr> floodfill<br />
&nbsp;<wbr> reset </p>
<p>&nbsp;<wbr> <code>Pixel Color</code> </p>
<p>&nbsp;<wbr> black<br />
&nbsp;<wbr> blue<br />
&nbsp;<wbr> cyan<br />
&nbsp;<wbr> green<br />
&nbsp;<wbr> gray<br />
&nbsp;<wbr> red<br />
&nbsp;<wbr> magenta<br />
&nbsp;<wbr> yellow<br />
&nbsp;<wbr> white<br />
&nbsp;<wbr> Browser&#8230; </p>
<p>&nbsp;<wbr> <code>Border Color</code> </p>
<p>&nbsp;<wbr> black<br />
&nbsp;<wbr> blue<br />
&nbsp;<wbr> cyan<br />
&nbsp;<wbr> green<br />
&nbsp;<wbr> gray<br />
&nbsp;<wbr> red<br />
&nbsp;<wbr> magenta<br />
&nbsp;<wbr> yellow<br />
&nbsp;<wbr> white<br />
&nbsp;<wbr> Browser&#8230; </p>
<p>&nbsp;<wbr> <code>Fuzz</code> </p>
<p>&nbsp;<wbr> 0<br />
&nbsp;<wbr> 2<br />
&nbsp;<wbr> 4<br />
&nbsp;<wbr> 8<br />
&nbsp;<wbr> 16<br />
&nbsp;<wbr>Dialog&#8230; </p>
<p>&nbsp;<wbr> <code>Undo</code><br />
&nbsp;<wbr> <code>Help</code><br />
&nbsp;<wbr> <code>Dismiss</code> </p>
<p> Choose a color editing method from the <code>Method</code> sub-menu of the Command widget. The <code>point method</code> recolors any pixel selected with the pointer unless the button is released. The <code>replace method</code> recolors any pixel that matches the color of the pixel you select with a button press. <code>Floodfill</code> recolors any pixel that matches the color of the pixel you select with a button press and is a neighbor. Whereas <code>filltoborder</code> changes the matte value of any neighbor pixel that is not the border color. Finally <code>reset</code> changes the entire image to the designated color. </p>
<p> Next, choose a pixel color from the <code>Pixel Color</code> sub-menu. Additional pixel colors can be specified with the color browser. You can change the menu colors by setting the X resources pen1 through pen9. </p>
<p> Now press button 1 to select a pixel within the Image window to change its color. Additional pixels may be recolored as prescribed by the method you choose. additional pixels by increasing the Delta value. </p>
<p> If the <code>Magnify widget</code> is mapped, it can be helpful in positioning your pointer within the image (refer to button 2). Alternatively you can select a pixel to recolor from within the <code>Magnify widget</code>. Move the pointer to the <code>Magnify widget</code> and position the pixel with the cursor control keys. Finally, press a button to recolor the selected pixel (or pixels). </p>
<p> The actual color you request for the pixels is saved in the image. However, the color that appears in your Image window may be different. For example, on a monochrome screen the pixel will appear black or white even if you choose the color red as the pixel color. However, the image saved to a file with -write is written with red pixels. To assure the correct color text in the final image, any <i>PseudoClass</i> image is promoted to <i>DirectClass</i> To force a <i>PseudoClass</i> image to remain <i>PseudoClass</i>, use <code>-colors</code>.</p>
<h2>MATTE EDITING</h2>
<p> Matte information within an image is useful for some operations such as image compositing. This extra channel usually defines a mask which represents a sort of a cookie-cutter for the image. This is the case when matte is 255 (full coverage) for pixels inside the shape, zero outside, and between zero and 255 on the boundary. </p>
<p> Setting the matte information in an image is done interactively. There is no command line argument to edit a pixel. To begin, and choose <code>Matte</code> of the <code>Image Edit</code> sub-menu from the Command widget. </p>
<p> Alternatively, press m in the image window. </p>
<p> A small window appears showing the location of the cursor in the image window. You are now in matte edit mode. To exit immediately, press Dismiss. In matte edit mode, the Command widget has these options: </p>
<p>&nbsp;<wbr> <code>Method</code> </p>
<p>&nbsp;<wbr> point<br />
&nbsp;<wbr> replace<br />
&nbsp;<wbr> floodfill<br />
&nbsp;<wbr> reset </p>
<p>&nbsp;<wbr> <code>Border Color</code> </p>
<p>&nbsp;<wbr> black<br />
&nbsp;<wbr> blue<br />
&nbsp;<wbr> cyan<br />
&nbsp;<wbr> green<br />
&nbsp;<wbr> gray<br />
&nbsp;<wbr> red<br />
&nbsp;<wbr> magenta<br />
&nbsp;<wbr> yellow<br />
&nbsp;<wbr> white<br />
&nbsp;<wbr> Browser&#8230; </p>
<p>&nbsp;<wbr> <code>Fuzz</code> </p>
<p>&nbsp;<wbr> 0<br />
&nbsp;<wbr> 2<br />
&nbsp;<wbr> 4<br />
&nbsp;<wbr> 8<br />
&nbsp;<wbr> 16<br />
&nbsp;<wbr>Dialog&#8230; </p>
<p>&nbsp;<wbr> <code>Matte</code><br />
&nbsp;<wbr> <code>Undo</code><br />
&nbsp;<wbr> <code>Help</code><br />
&nbsp;<wbr> <code>Dismiss</code> </p>
<p> Choose a matte editing method from the <code>Method</code> sub-menu of the Command widget. The <code>point method</code> changes the matte value of the any pixel selected with the pointer until the button is released. The <code>replace method</code> changes the matte value of any pixel that matches the color of the pixel you select with a button press. <code>Floodfill</code> changes the matte value of any pixel that matches the color of the pixel you select with a button press and is a neighbor. Whereas <code>filltoborder</code> recolors any neighbor pixel that is not the border color. Finally <code>reset</code> changes the entire image to the designated matte value. Choose <code>Matte Value</code> and a dialog appears requesting a matte value. Enter a value between <code>0 and 255</code>. This value is assigned as the matte value of the selected pixel or pixels. Now, press any button to select a pixel within the Image window to change its matte value. You can change the matte value of additional pixels by increasing the Delta value. The Delta value is first added then subtracted from the red, green, and blue of the target color. Any pixels within the range also have their matte value updated. If the <code>Magnify widget</code> is mapped, it can be helpful in positioning your pointer within the image (refer to button 2). Alternatively you can select a pixel to change the matte value from within the <code>Magnify widget</code>. Move the pointer to the <code>Magnify widget</code> and position the pixel with the cursor control keys. Finally, press a button to change the matte value of the selected pixel (or pixels). Matte information is only valid in a <i>DirectClass image</i>. Therefore, any <i>PseudoClass</i> image is promoted to <i>DirectClass</i>. Note that matte information for <i>PseudoClass</i> is not retained for colormapped X server visuals (e.g. <i>StaticColor, StaticColor, GrayScale, PseudoColor</i>) unless you immediately save your image to a file (refer to Write). Correct matte editing behavior may require a <i>TrueColor</i> or <i>DirectColor</i> visual or a <i>Standard Colormap</i>.</p>
<h2>IMAGE DRAWING</h2>
<p> An image is drawn upon interactively. <code>There is no command line argument to draw on an image</code>. To begin, choose <code>Draw</code> of the Image <code>Edit</code> sub-menu from the Command widget. Alternatively, press d in the image window. </p>
<p> The cursor changes to a crosshair to indicate you are in draw mode. To exit immediately, press Dismiss. In draw mode, the Command widget has these options: </p>
<p>&nbsp;<wbr> <code>Primitive</code> </p>
<p>&nbsp;<wbr> point<br />
&nbsp;<wbr> line<br />
&nbsp;<wbr> rectangle<br />
&nbsp;<wbr> fill rectangle<br />
&nbsp;<wbr> circle<br />
&nbsp;<wbr> fill circle<br />
&nbsp;<wbr> ellipse<br />
&nbsp;<wbr> fill ellipse<br />
&nbsp;<wbr> polygon<br />
&nbsp;<wbr> fill polygon </p>
<p>&nbsp;<wbr> <code>Color</code> </p>
<p>&nbsp;<wbr> black<br />
&nbsp;<wbr> blue<br />
&nbsp;<wbr> cyan<br />
&nbsp;<wbr> green<br />
&nbsp;<wbr> gray<br />
&nbsp;<wbr> red<br />
&nbsp;<wbr> magenta<br />
&nbsp;<wbr> yellow<br />
&nbsp;<wbr> white<br />
&nbsp;<wbr> transparent<br />
&nbsp;<wbr> Browser&#8230; </p>
<p>&nbsp;<wbr> <code>Stipple</code> </p>
<p>&nbsp;<wbr> Brick<br />
&nbsp;<wbr> Diagonal<br />
&nbsp;<wbr> Scales<br />
&nbsp;<wbr> Vertical<br />
&nbsp;<wbr> Wavy<br />
&nbsp;<wbr> Translucent<br />
&nbsp;<wbr> Opaque<br />
&nbsp;<wbr> Open&#8230; </p>
<p>&nbsp;<wbr> <code>Width</code> </p>
<p>&nbsp;<wbr> 1<br />
&nbsp;<wbr> 2<br />
&nbsp;<wbr> 4<br />
&nbsp;<wbr> 8<br />
&nbsp;<wbr> 16<br />
&nbsp;<wbr>Dialog&#8230; </p>
<p>&nbsp;<wbr> <code>Undo</code><br />
&nbsp;<wbr> <code>Help</code><br />
&nbsp;<wbr> <code>Dismiss</code> </p>
<p> Choose a drawing primitive from the <code>Primitive</code> sub-menu. </p>
<p> Next, choose a color from the <code>Color</code> sub-menu. Additional colors can be specified with the color browser. You can change the menu colors by setting the X resources pen1 through pen9. The transparent color updates the image matte channel and is useful for image compositing. </p>
<p> If you choose the color browser and press <code>Grab</code>, you can select the primitive color by moving the pointer to the desired color on the screen and press any button. The transparent color updates the image matte channel and is useful for image compositing. </p>
<p> Choose a stipple, if appropriate, from the <code>Stipple</code> sub-menu. Additional stipples can be specified with the file browser. Stipples obtained from the file browser must be on disk in the X11 bitmap format. </p>
<p> Choose a line width, if appropriate, from the <code>Width</code> sub-menu. To choose a specific width select the <code>Dialog</code> widget. </p>
<p> Choose a point in the image window and press button 1 and hold. Next, move the pointer to another location in the image. As you move, a line connects the initial location and the pointer. When you release the button, the image is updated with the primitive you just drew. For polygons, the image is updated when you press and release the button without moving the pointer. </p>
<p> To cancel image drawing, move the pointer back to the starting point of the line and release the button.</p>
<h2>REGION OF INTEREST</h2>
<p> To begin, press choose Region of Interest of the Pixel Transform sub-menu from the Command widget. Alternatively, press R in the image window. </p>
<p> A small window appears showing the location of the cursor in the image window. You are now in region of interest mode. In region of interest mode, the Command widget has these options: </p>
<p>&nbsp;<wbr> <code>Help</code><br />
&nbsp;<wbr> <code>Dismiss</code> </p>
<p> To define a region of interest, press button 1 and drag. The region of interest is defined by a highlighted rectangle that expands or contracts as it follows the pointer. Once you are satisfied with the region of interest, release the button. You are now in apply mode. In apply mode the Command widget has these options: </p>
<p>&nbsp;<wbr> <code>File</code> </p>
<p>&nbsp;<wbr> Save&#8230;<br />
&nbsp;<wbr> Print&#8230; </p>
<p>&nbsp;<wbr> <code>Edit</code> </p>
<p>&nbsp;<wbr> Undo<br />
&nbsp;<wbr> Redo </p>
<p>&nbsp;<wbr> <code>Transform</code> </p>
<p>&nbsp;<wbr> Flip<br />
&nbsp;<wbr> Flop<br />
&nbsp;<wbr> Rotate Right<br />
&nbsp;<wbr> Rotate Left </p>
<p>&nbsp;<wbr> <code>Enhance</code> </p>
<p>&nbsp;<wbr> Hue&#8230;<br />
&nbsp;<wbr> Saturation&#8230;<br />
&nbsp;<wbr> Brightness&#8230;<br />
&nbsp;<wbr> Gamma&#8230;<br />
&nbsp;<wbr> Spiff<br />
&nbsp;<wbr> Dull<br />
&nbsp;<wbr> Equalize<br />
&nbsp;<wbr> Normalize<br />
&nbsp;<wbr> Negate<br />
&nbsp;<wbr> GRAYscale<br />
&nbsp;<wbr> Quantize&#8230; </p>
<p>&nbsp;<wbr> <code>Effects</code> </p>
<p>&nbsp;<wbr> Despeckle<br />
&nbsp;<wbr> Emboss<br />
&nbsp;<wbr> Reduce Noise<br />
&nbsp;<wbr> Add Noise<br />
&nbsp;<wbr> Sharpen&#8230;<br />
&nbsp;<wbr> Blur&#8230;<br />
&nbsp;<wbr> Threshold&#8230;<br />
&nbsp;<wbr> Edge Detect&#8230;<br />
&nbsp;<wbr> Spread&#8230;<br />
&nbsp;<wbr> Shade&#8230;<br />
&nbsp;<wbr> Raise&#8230;<br />
&nbsp;<wbr> Segment&#8230; </p>
<p>&nbsp;<wbr> <code>F/X</code> </p>
<p>&nbsp;<wbr> Solarize&#8230;<br />
&nbsp;<wbr> Swirl&#8230;<br />
&nbsp;<wbr> Implode&#8230;<br />
&nbsp;<wbr> Wave&#8230;<br />
&nbsp;<wbr> Oil Paint<br />
&nbsp;<wbr> Charcoal Draw&#8230; </p>
<p>&nbsp;<wbr> <code>Miscellany</code> </p>
<p>&nbsp;<wbr> Image Info<br />
&nbsp;<wbr> Zoom Image<br />
&nbsp;<wbr> Show Preview&#8230;<br />
&nbsp;<wbr> Show Histogram<br />
&nbsp;<wbr> Show Matte </p>
<p>&nbsp;<wbr> <code>Help</code><br />
&nbsp;<wbr> <code>Dismiss</code> </p>
<p> You can make adjustments to the region of interest by moving the pointer to one of the rectangle corners, pressing a button, and dragging. Finally, choose an image processing technique from the Command widget. You can choose more than one image processing technique to apply to an area. Alternatively, you can move the region of interest before applying another image processing technique. To exit, press Dismiss.</p>
<h2>IMAGE PANNING</h2>
<p> When an image exceeds the width or height of the X server screen, display maps a small panning icon. The rectangle within the panning icon shows the area that is currently displayed in the the image window. To pan about the image, press any button and drag the pointer within the panning icon. The pan rectangle moves with the pointer and the image window is updated to reflect the location of the rectangle within the panning icon. When you have selected the area of the image you wish to view, release the button. </p>
<p> Use the arrow keys to pan the image one pixel up, down, left, or right within the image window. </p>
<p> The panning icon is withdrawn if the image becomes smaller than the dimensions of the X server screen.</p>
<h2>USER PREFERENCES</h2>
<p> Preferences affect the default behavior of <code><a href="/docs/linux/man/1-display/">display</a>(1)</code>. The preferences are either true or false and are stored in your home directory as .displayrc: </p>
<p> <code>display image centered on a backdrop</code>&quot;<br />
&nbsp;<wbr> </p>
<p> This backdrop covers the entire workstation screen and is useful for hiding other X window activity while viewing the image. The color of the backdrop is specified as the background color. Refer to X Resources for details. <code>confirm on program exit</code>&quot;<br />
&nbsp;<wbr> </p>
<p> Ask for a confirmation before exiting the <code><a href="/docs/linux/man/1-display/">display</a>(1)</code> program. <code>correct image for display gamma</code>&quot;<br />
&nbsp;<wbr> </p>
<p> If the image has a known gamma, the gamma is corrected to match that of the X server (see the X Resource<code> displayGamma</code>). <code>display warning messages</code>&quot;<br />
&nbsp;<wbr> </p>
<p> Display any warning messages. <code>apply Floyd/Steinberg error diffusion to image</code>&quot;<br />
&nbsp;<wbr> </p>
<p> The basic strategy of dithering is to trade intensity resolution for spatial resolution by averaging the intensities of several neighboring pixels. Images which suffer from severe contouring when reducing colors can be improved with this preference. <code>use a shared colormap for colormapped X visuals</code>&quot;<br />
&nbsp;<wbr> </p>
<p> This option only applies when the default X server visual is <i>PseudoColor</i> or <i>GRAYScale</i>. Refer to <code>-visual</code> for more details. By default, a shared colormap is allocated. The image shares colors with other X clients. Some image colors could be approximated, therefore your image may look very different than intended. Otherwise the image colors appear exactly as they are defined. However, other clients may go technicolor when the image colormap is installed. <code>display images as an X server pixmap</code>&quot;<br />
&nbsp;<wbr> </p>
<p> Images are maintained as a XImage by default. Set this resource to True to utilize a server Pixmap instead. This option is useful if your image exceeds the dimensions of your server screen and you intend to pan the image. Panning is much faster with Pixmaps than with a XImage. Pixmaps are considered a precious resource, use them with discretion. </p>
<dl>
<dt>
<dd></dl>
<h2>GM IDENTIFY</h2>
<p> <code>Identify</code> describes the format and characteristics of one or more image files as internally supported by the software. It will also report if an image is incomplete or corrupt. The information displayed includes the scene number, the file name, the width and height of the image, whether the image is colormapped or not, the number of colors in the image, the number of bytes in the image, the format of the image (JPEG, PNM, etc.), and finally the number of seconds in both user time and elapsed time it took to read and process the image. If -verbose or +ping are provided as an option, the pixel read rate is also displayed. An example line output from <code>identify</code> follows: </p>
<p>&nbsp;<wbr>images/aquarium.miff 640&#215;480 PseudoClass 256c<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>308135b MIFF 0.000u 0:01 </p>
<p> If -verbose is set, expect additional output including any image comment: </p>
<p>&nbsp;<wbr>Image: images/aquarium.miff<br />
&nbsp;<wbr>class: PseudoClass<br />
&nbsp;<wbr>colors: 256<br />
&nbsp;<wbr>signature: eb5dca81dd93ae7e6ffae99a527eb5dca8&#8230;<br />
&nbsp;<wbr>matte: False<br />
&nbsp;<wbr>geometry: 640&#215;480<br />
&nbsp;<wbr>depth: 8<br />
&nbsp;<wbr>bytes: 308135<br />
&nbsp;<wbr>format: MIFF<br />
&nbsp;<wbr>comments:<br />
&nbsp;<wbr>Imported from MTV raster image: aquarium.mtv </p>
<p> For some formats, additional format-specific information about the file will be written if the -debug coder or -debug all option is used.</p>
<h2>IDENTIFY OPTIONS</h2>
<p> Options are processed in command line order. Any option you specify on the command line remains in effect for the set of images immediately following, until the set is terminated by the appearance of any option or <code>-noop</code>. </p>
<p> For a more detailed description of each option, see Options, above. </p>
<dl>
<dt><code>-authenticate </code><i>&lt;string&gt;</i></p>
<dd> decrypt image with this password</p>
<dt><code>-debug </code><i>&lt;events&gt;</i></p>
<dd> enable debug printout</p>
<dt><code>-define </code><i>&lt;key&gt;{=&lt;value&gt;},&#8230;</i></p>
<dd> add coder/decoder specific options</p>
<dt><code>-density </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> horizontal and vertical resolution in pixels of the image</p>
<dt><code>-depth </code><i>&lt;value&gt;</i></p>
<dd> depth of the image</p>
<dt><code>-format </code><i>&lt;string&gt;</i></p>
<dd> output formatted image characteristics</p>
<dt><code>-help</code></p>
<dd> print usage instructions</p>
<dt><code>-interlace </code><i>&lt;type&gt;</i></p>
<dd> the type of interlacing scheme</p>
<dt><code>-limit </code><i>&lt;type&gt; &lt;value&gt;</i></p>
<dd> Disk, File, Map, Memory, Pixels, Width, Height or Threads resource limit</p>
<dt><code>-log </code><i>&lt;string&gt;</i></p>
<dd> Specify format for debug log</p>
<dt><code>-ping</code></p>
<dd> efficiently determine image characteristics</p>
<dt><code>-sampling-factor </code><i>&lt;horizontal_factor&gt;x&lt;vertical_factor&gt;</i></p>
<dd> chroma subsampling factors</p>
<dt><code>-size </code><i>&lt;width&gt;x&lt;height&gt;{+offset}</i></p>
<dd> width and height of the image</p>
<dt><code>-verbose</code></p>
<dd> print detailed information about the image</p>
<dt><code>-version</code></p>
<dd> print GraphicsMagick version string </p>
<p> For a more detailed description of each option, see Options, above. </p>
</dl>
<h2>GM IMPORT</h2>
<p> <code>Import</code> reads an image from any visible window on an X server and outputs it as an image file. You can capture a single window, the entire screen, or any rectangular portion of the screen. Use <i>display</i> for redisplay, printing, editing, formatting, archiving, image processing, etc. of the captured image. </p>
<p> The target window can be specified by id, name, or may be selected by clicking the mouse in the desired window. If you press a button and then drag, a rectangle will form which expands and contracts as the mouse moves. To save the portion of the screen defined by the rectangle, just release the button. The keyboard bell is rung once at the beginning of the screen capture and twice when it completes.</p>
<h2>EXAMPLES</h2>
<p> To select an X window or an area of the screen with the mouse and save it in the MIFF image format to a file entitled window.miff, use: </p>
<p>&nbsp;<wbr>gm import window.miff </p>
<p> To select an X window or an area of the screen with the mouse and save it in the Encapsulated PostScript format to include in another document, use: </p>
<p>&nbsp;<wbr>gm import figure.eps </p>
<p> To capture the entire X server screen in the JPEG image format in a file entitled root.jpeg, without using the mouse, use: </p>
<p>&nbsp;<wbr>gm import -window root root.jpeg </p>
<p> To capture the 512&#215;256 area at the upper right corner of the X server screen in the PNG image format in a well-compressed file entitled corner.png, without using the mouse, use: </p>
<p>&nbsp;<wbr>gm import -window root -crop 512&#215;256-0+0 -quality 90<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>corner.png </p>
<h2>OPTIONS</h2>
<p> Options are processed in command line order. Any option you specify on the command line remains in effect until it is explicitly changed by specifying the option again with a different effect. </p>
<p> <code>Import</code> options can appear on the command line or in your X resources file. See <i><a href="/docs/linux/man/1-x/">X</a>(1)</i>. Options on the command line supersede values specified in your X resources file. </p>
<p> For a more detailed description of each option, see Options, above. </p>
<dl>
<dt><code>-bordercolor </code><i>&lt;color&gt;</i></p>
<dd> the border color</p>
<dt><code>-colors </code><i>&lt;value&gt;</i></p>
<dd> preferred number of colors in the image</p>
<dt><code>-colorspace </code><i>&lt;value&gt;</i></p>
<dd> the type of colorspace</p>
<dt><code>-comment </code><i>&lt;string&gt;</i></p>
<dd> annotate an image with a comment</p>
<dt><code>-crop </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}</i></p>
<dd> preferred size and location of the cropped image</p>
<dt><code>-debug </code><i>&lt;events&gt;</i></p>
<dd> enable debug printout</p>
<dt><code>-define </code><i>&lt;key&gt;{=&lt;value&gt;},&#8230;</i></p>
<dd> add coder/decoder specific options</p>
<dt><code>-delay </code><i>&lt;1/100ths of a second&gt;</i></p>
<dd> display the next image after pausing</p>
<dt><code>-density </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> horizontal and vertical resolution in pixels of the image</p>
<dt><code>-depth </code><i>&lt;value&gt;</i></p>
<dd> depth of the image</p>
<dt><code>-descend</code></p>
<dd> obtain image by descending window hierarchy</p>
<dt><code>-display </code><i>&lt;host:display[.screen]&gt;</i></p>
<dd> specifies the X server to contact</p>
<dt><code>-dispose </code><i>&lt;method&gt;</i></p>
<dd> GIF disposal method</p>
<dt><code>-dither</code></p>
<dd> apply Floyd/Steinberg error diffusion to the image</p>
<dt><code>-encoding </code><i>&lt;type&gt;</i></p>
<dd> specify the text encoding</p>
<dt><code>-endian </code><i>&lt;type&gt;</i></p>
<dd> specify endianness (MSB, LSB, or Native) of image</p>
<dt><code>-frame</code></p>
<dd> include the X window frame in the imported image</p>
<dt><code>-geometry </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}{@}{!}{^}{&lt;}{&gt;}</i></p>
<dd> Specify dimension, offset, and resize options.</p>
<dt><code>-help</code></p>
<dd> print usage instructions</p>
<dt><code>-interlace </code><i>&lt;type&gt;</i></p>
<dd> the type of interlacing scheme</p>
<dt><code>-label </code><i>&lt;name&gt;</i></p>
<dd> assign a label to an image</p>
<dt><code>-limit </code><i>&lt;type&gt; &lt;value&gt;</i></p>
<dd> Disk, File, Map, Memory, Pixels, Width, Height or Threads resource limit</p>
<dt><code>-log </code><i>&lt;string&gt;</i></p>
<dd> Specify format for debug log</p>
<dt><code>-monitor</code></p>
<dd> show progress indication</p>
<dt><code>-monochrome</code></p>
<dd> transform the image to black and white</p>
<dt><code>-negate</code></p>
<dd> replace every pixel with its complementary color</p>
<dt><code>-page </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}{!}{&lt;}{&gt;}</i></p>
<dd> size and location of an image canvas</p>
<dt><code>-pause </code><i>&lt;seconds&gt;</i></p>
<dd> pause between snapshots [import]</p>
<dt><code>-ping</code></p>
<dd> efficiently determine image characteristics</p>
<dt><code>-pointsize </code><i>&lt;value&gt;</i></p>
<dd> pointsize of the PostScript, X11, or TrueType font</p>
<dt><code>-quality </code><i>&lt;value&gt;</i></p>
<dd> JPEG/MIFF/PNG/TIFF compression level</p>
<dt><code>-resize </code><i>&lt;width&gt;x&lt;height&gt;{%}{@}{!}{&lt;}{&gt;}</i></p>
<dd> resize an image</p>
<dt><code>-rotate </code><i>&lt;degrees&gt;{&lt;}{&gt;}</i></p>
<dd> rotate the image</p>
<dt><code>-sampling-factor </code><i>&lt;horizontal_factor&gt;x&lt;vertical_factor&gt;</i></p>
<dd> chroma subsampling factors</p>
<dt><code>-scene </code><i>&lt;value&gt;</i></p>
<dd> set scene number</p>
<dt><code>-screen</code></p>
<dd> specify the screen to capture</p>
<dt><code>-set </code><i>&lt;attribute&gt; &lt;value&gt;</i></p>
<dd> set an image attribute</p>
<dt><code>+set </code><i>&lt;attribute&gt;</i></p>
<dd> unset an image attribute</p>
<dt><code>-silent</code></p>
<dd> operate silently</p>
<dt><code>-snaps </code><i>&lt;value&gt;</i></p>
<dd> number of screen snapshots</p>
<dt><code>-thumbnail </code><i>&lt;width&gt;x&lt;height&gt;{%}{@}{!}{&lt;}{&gt;}</i></p>
<dd> resize an image (quickly)</p>
<dt><code>-transparent </code><i>&lt;color&gt;</i></p>
<dd> make this color transparent within the image</p>
<dt><code>-trim</code></p>
<dd> trim an image</p>
<dt><code>-verbose</code></p>
<dd> print detailed information about the image</p>
<dt><code>-version</code></p>
<dd> print GraphicsMagick version string </p>
<p> For a more detailed description of each option, see Options, above. </p>
</dl>
<h2>GM MOGRIFY</h2>
<p> <code>Mogrify</code> transforms an image or a sequence of images. These transforms include image scaling, image rotation, color reduction, and others. Each transmogrified image overwrites the corresponding original image, unless an option such as <code>-format</code> causes the output filename to be different from the input filename. </p>
<p> The graphics formats supported by <code>mogrify</code> are listed in <i><a href="/docs/linux/man/1-graphicsmagick/">GraphicsMagick</a>(1)</i>.</p>
<h2>EXAMPLES</h2>
<p> To convert all the TIFF files in a particular directory to JPEG, use: </p>
<p>&nbsp;<wbr>gm mogrify -format jpeg&nbsp;<wbr>*.tiff </p>
<p> To convert a directory full of JPEG images to thumbnails, use: </p>
<p>&nbsp;<wbr>gm mogrify -size 120&#215;120&nbsp;<wbr>*.jpg -resize 120&#215;120&nbsp;<wbr>+profile&nbsp;<wbr>&quot;*&quot; </p>
<p> In this example, &#8216;-size 120&#215;120&#8217; gives a hint to the JPEG decoder that the images are going to be downscaled to 120&#215;120, allowing it to run faster by avoiding returning full-resolution images to GraphicsMagick for the subsequent resizing operation. The &#8216;-resize 120&#215;120&#8217; specifies the desired dimensions of the output images. It will be scaled so its largest dimension is 120 pixels. The &#8216;+profile &quot;*&quot;&#8217; removes any ICM, EXIF, IPTC, or other profiles that might be present in the input and aren&#8217;t needed in the thumbnails. </p>
<p> To scale an image of a cockatoo to exactly 640 pixels in width and 480 pixels in height, use: </p>
<p>&nbsp;<wbr>gm mogrify -resize 640&#215;480!&nbsp;<wbr>cockatoo.miff </p>
<h2>OPTIONS</h2>
<p> Options are processed in command line order. Any option you specify on the command line remains in effect for the set of images that follows, until the set is terminated by the appearance of any option or <code>-noop</code>. </p>
<p> For a more detailed description of each option, see Options, above. </p>
<dl>
<dt><code>-affine </code><i>&lt;matrix&gt;</i></p>
<dd> drawing transform matrix</p>
<dt><code>-antialias</code></p>
<dd> remove pixel aliasing</p>
<dt><i>-asc-cdl &lt;spec&gt;</i></p>
<dd> apply ASC CDL color transform</p>
<dt><code>-authenticate </code><i>&lt;string&gt;</i></p>
<dd> decrypt image with this password</p>
<dt><code>-auto-orient</code></p>
<dd> orient (rotate) image so it is upright</p>
<dt><code>-background </code><i>&lt;color&gt;</i></p>
<dd> the background color</p>
<dt><code>-black-threshold </code><i>red[,green][,blue][,opacity]</i></p>
<dd> pixels below the threshold become black</p>
<dt><code>-blue-primary </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> blue chromaticity primary point</p>
<dt><code>-blur </code><i>&lt;radius&gt;{x&lt;sigma&gt;}</i></p>
<dd> blur the image with a Gaussian operator</p>
<dt><code>-border </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> surround the image with a border of color</p>
<dt><code>-bordercolor </code><i>&lt;color&gt;</i></p>
<dd> the border color</p>
<dt><code>-channel </code><i>&lt;type&gt;</i></p>
<dd> the type of channel</p>
<dt><code>-charcoal </code><i>&lt;factor&gt;</i></p>
<dd> simulate a charcoal drawing</p>
<dt><code>-colorize </code><i>&lt;value&gt;</i></p>
<dd> colorize the image with the pen color</p>
<dt><code>-colors </code><i>&lt;value&gt;</i></p>
<dd> preferred number of colors in the image</p>
<dt><code>-colorspace </code><i>&lt;value&gt;</i></p>
<dd> the type of colorspace</p>
<dt><code>-comment </code><i>&lt;string&gt;</i></p>
<dd> annotate an image with a comment</p>
<dt><code>-compose </code><i>&lt;operator&gt;</i></p>
<dd> the type of image composition</p>
<dt><code>-compress </code><i>&lt;type&gt;</i></p>
<dd> the type of image compression</p>
<dt><code>-contrast</code></p>
<dd> enhance or reduce the image contrast</p>
<dt><code>-convolve </code><i>&lt;kernel&gt;</i></p>
<dd> convolve image with the specified convolution kernel</p>
<dt><code>-create-directories</code></p>
<dd> create output directory if required</p>
<dt><code>-crop </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}</i></p>
<dd> preferred size and location of the cropped image</p>
<dt><code>-cycle </code><i>&lt;amount&gt;</i></p>
<dd> displace image colormap by amount</p>
<dt><code>-debug </code><i>&lt;events&gt;</i></p>
<dd> enable debug printout</p>
<dt><code>-define </code><i>&lt;key&gt;{=&lt;value&gt;},&#8230;</i></p>
<dd> add coder/decoder specific options</p>
<dt><code>-delay </code><i>&lt;1/100ths of a second&gt;</i></p>
<dd> display the next image after pausing</p>
<dt><code>-density </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> horizontal and vertical resolution in pixels of the image</p>
<dt><code>-depth </code><i>&lt;value&gt;</i></p>
<dd> depth of the image</p>
<dt><code>-despeckle</code></p>
<dd> reduce the speckles within an image</p>
<dt><code>-display </code><i>&lt;host:display[.screen]&gt;</i></p>
<dd> specifies the X server to contact</p>
<dt><code>-dispose </code><i>&lt;method&gt;</i></p>
<dd> GIF disposal method</p>
<dt><code>-dither</code></p>
<dd> apply Floyd/Steinberg error diffusion to the image</p>
<dt><code>-draw </code><i>&lt;string&gt;</i></p>
<dd> annotate an image with one or more graphic primitives</p>
<dt><code>-edge </code><i>&lt;radius&gt;</i></p>
<dd> detect edges within an image</p>
<dt><code>-emboss </code><i>&lt;radius&gt;</i></p>
<dd> emboss an image</p>
<dt><code>-encoding </code><i>&lt;type&gt;</i></p>
<dd> specify the text encoding</p>
<dt><code>-endian </code><i>&lt;type&gt;</i></p>
<dd> specify endianness (MSB, LSB, or Native) of image</p>
<dt><code>-enhance</code></p>
<dd> apply a digital filter to enhance a noisy image</p>
<dt><code>-equalize</code></p>
<dd> perform histogram equalization to the image</p>
<dt><code>-extent </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;</i></p>
<dd> composite image on background color canvas image</p>
<dt><code>-fill </code><i>&lt;color&gt;</i></p>
<dd> color to use when filling a graphic primitive</p>
<dt><code>-filter </code><i>&lt;type&gt;</i></p>
<dd> use this type of filter when resizing an image</p>
<dt><code>-flip</code></p>
<dd> create a &quot;mirror image&quot;</p>
<dt><code>-flop</code></p>
<dd> create a &quot;mirror image&quot;</p>
<dt><code>-font </code><i>&lt;name&gt;</i></p>
<dd> use this font when annotating the image with text</p>
<dt><code>-format </code><i>&lt;type&gt;</i></p>
<dd> the image format type</p>
<dt><code>-frame </code><i>&lt;width&gt;x&lt;height&gt;+&lt;outer bevel width&gt;+&lt;inner bevel width&gt;</i></p>
<dd> surround the image with an ornamental border</p>
<dt><code>-fuzz </code><i>&lt;distance&gt;{%}</i></p>
<dd> colors within this Euclidean distance are considered equal</p>
<dt><code>-gamma </code><i>&lt;value&gt;</i></p>
<dd> level of gamma correction</p>
<dt><code>-gaussian </code><i>&lt;radius&gt;{x&lt;sigma&gt;}</i></p>
<dd> blur the image with a Gaussian operator</p>
<dt><code>-geometry </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}{@}{!}{^}{&lt;}{&gt;}</i></p>
<dd> Specify dimension, offset, and resize options.</p>
<dt><code>-gravity </code><i>&lt;type&gt;</i></p>
<dd> direction primitive gravitates to when annotating the image.</p>
<dt><code>-green-primary </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> green chromaticity primary point</p>
<dt><code>-hald-clut </code><i>&lt;clut&gt;</i></p>
<dd> apply a Hald CLUT to the image</p>
<dt><code>-help</code></p>
<dd> print usage instructions</p>
<dt><code>-implode </code><i>&lt;factor&gt;</i></p>
<dd> implode image pixels about the center</p>
<dt><code>-interlace </code><i>&lt;type&gt;</i></p>
<dd> the type of interlacing scheme</p>
<dt><code>-label </code><i>&lt;name&gt;</i></p>
<dd> assign a label to an image</p>
<dt><code>-lat </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;offset&gt;{%}</i></p>
<dd> perform local adaptive thresholding</p>
<dt><code>-level </code><i>&lt;black_point&gt;{,&lt;gamma&gt;}{,&lt;white_point&gt;}{%}</i></p>
<dd> adjust the level of image contrast</p>
<dt><code>-limit </code><i>&lt;type&gt; &lt;value&gt;</i></p>
<dd> Disk, File, Map, Memory, Pixels, Width, Height or Threads resource limit</p>
<dt><code>-linewidth</code></p>
<dd> the line width for subsequent draw operations</p>
<dt><code>-list </code><i>&lt;type&gt;</i></p>
<dd> the type of list</p>
<dt><code>-log </code><i>&lt;string&gt;</i></p>
<dd> Specify format for debug log</p>
<dt><code>-loop </code><i>&lt;iterations&gt;</i></p>
<dd> add Netscape loop extension to your GIF animation</p>
<dt><code>-magnify</code></p>
<dd> magnify the image</p>
<dt><code>-map </code><i>&lt;filename&gt;</i></p>
<dd> choose a particular set of colors from this image</p>
<dt><code>-mask </code><i>&lt;filename&gt;</i></p>
<dd> Specify a clipping mask</p>
<dt><code>-matte</code></p>
<dd> store matte channel if the image has one</p>
<dt><code>-mattecolor </code><i>&lt;color&gt;</i></p>
<dd> specify the color to be used with the <code>-frame</code> option</p>
<dt><code>-median </code><i>&lt;radius&gt;</i></p>
<dd> apply a median filter to the image</p>
<dt><code>-minify </code><i>&lt;factor&gt;</i></p>
<dd> minify the image</p>
<dt><code>-modulate </code><i>brightness[,saturation[,hue]]</i></p>
<dd> vary the brightness, saturation, and hue of an image</p>
<dt><code>-monitor</code></p>
<dd> show progress indication</p>
<dt><code>-monochrome</code></p>
<dd> transform the image to black and white</p>
<dt><code>-motion-blur </code><i>&lt;radius&gt;{x&lt;sigma&gt;}{+angle}</i></p>
<dd> Simulate motion blur</p>
<dt><code>-negate</code></p>
<dd> replace every pixel with its complementary color</p>
<dt><code>-noise </code><i>&lt;radius|type&gt;</i></p>
<dd> add or reduce noise in an image</p>
<dt><code>-noop</code></p>
<dd> NOOP (no option)</p>
<dt><code>-normalize</code></p>
<dd> transform image to span the full range of color values</p>
<dt><code>-opaque </code><i>&lt;color&gt;</i></p>
<dd> change this color to the pen color within the image</p>
<dt><code>-operator </code><i>channel operator rvalue[%]</i></p>
<dd> apply a mathematical, bitwise, or value operator to an image channel</p>
<dt><code>-ordered-dither </code><i>&lt;channeltype&gt; &lt;NxN&gt;</i></p>
<dd> ordered dither the image</p>
<dt><code>-output-directory </code><i>&lt;directory&gt;</i></p>
<dd> output files to directory</p>
<dt><code>-orient </code><i>&lt;orientation&gt;</i></p>
<dd> Set the image orientation attribute</p>
<dt><code>-page </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}{!}{&lt;}{&gt;}</i></p>
<dd> size and location of an image canvas</p>
<dt><code>-paint </code><i>&lt;radius&gt;</i></p>
<dd> simulate an oil painting</p>
<dt><code>-pen </code><i>&lt;color&gt;</i></p>
<dd> (This option has been replaced by the -fill option)</p>
<dt><code>-pointsize </code><i>&lt;value&gt;</i></p>
<dd> pointsize of the PostScript, X11, or TrueType font</p>
<dt><code>-profile </code><i>&lt;filename&gt;</i></p>
<dd> add ICM, IPTC, or generic profile to image</p>
<dt><code>-preserve-timestamp</code></p>
<dd> preserve the original timestamps of the file</p>
<dt><code>-quality </code><i>&lt;value&gt;</i></p>
<dd> JPEG/MIFF/PNG/TIFF compression level</p>
<dt><code>-raise </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> lighten or darken image edges</p>
<dt><code>-random-threshold </code><i>&lt;channeltype&gt; &lt;LOWxHIGH&gt;</i></p>
<dd> random threshold the image</p>
<dt><code>-recolor </code><i>&lt;matrix&gt;</i></p>
<dd> apply a color translation matrix to image channels</p>
<dt><code>-red-primary </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> red chromaticity primary point</p>
<dt><code>-region </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;</i></p>
<dd> apply options to a portion of the image</p>
<dt><code>-render</code></p>
<dd> render vector operations</p>
<dt><code>-repage </code><i> &lt;width&gt;x&lt;height&gt;+xoff+yoff[!]</i></p>
<dd> Adjust image page offsets</p>
<dt><code>-resample </code><i>&lt;horizontal&gt;x&lt;vertical&gt;</i></p>
<dd> Resample image to specified horizontal and vertical resolution</p>
<dt><code>-resize </code><i>&lt;width&gt;x&lt;height&gt;{%}{@}{!}{&lt;}{&gt;}</i></p>
<dd> resize an image</p>
<dt><code>-roll </code><i>{+-}&lt;x&gt;{+-}&lt;y&gt;</i></p>
<dd> roll an image vertically or horizontally</p>
<dt><code>-rotate </code><i>&lt;degrees&gt;{&lt;}{&gt;}</i></p>
<dd> rotate the image</p>
<dt><code>-sample </code><i>&lt;geometry&gt;</i></p>
<dd> scale image using pixel sampling</p>
<dt><code>-sampling-factor </code><i>&lt;horizontal_factor&gt;x&lt;vertical_factor&gt;</i></p>
<dd> chroma subsampling factors</p>
<dt><code>-scale </code><i>&lt;geometry&gt;</i></p>
<dd> scale the image.</p>
<dt><code>-scene </code><i>&lt;value&gt;</i></p>
<dd> set scene number</p>
<dt><code>-set </code><i>&lt;attribute&gt; &lt;value&gt;</i></p>
<dd> set an image attribute</p>
<dt><code>+set </code><i>&lt;attribute&gt;</i></p>
<dd> unset an image attribute</p>
<dt><code>-segment </code><i>&lt;cluster threshold&gt;x&lt;smoothing threshold&gt;</i></p>
<dd> segment an image</p>
<dt><code>-shade </code><i>&lt;azimuth&gt;x&lt;elevation&gt;</i></p>
<dd> shade the image using a distant light source</p>
<dt><code>-sharpen </code><i>&lt;radius&gt;{x&lt;sigma&gt;}</i></p>
<dd> sharpen the image</p>
<dt><code>-shave </code><i>&lt;width&gt;x&lt;height&gt;{%}</i></p>
<dd> shave pixels from the image edges</p>
<dt><code>-shear </code><i>&lt;x degrees&gt;x&lt;y degrees&gt;</i></p>
<dd> shear the image along the X or Y axis</p>
<dt><code>-size </code><i>&lt;width&gt;x&lt;height&gt;{+offset}</i></p>
<dd> width and height of the image</p>
<dt><code>-solarize </code><i>&lt;factor&gt;</i></p>
<dd> negate all pixels above the threshold level</p>
<dt><code>-spread </code><i>&lt;amount&gt;</i></p>
<dd> displace image pixels by a random amount</p>
<dt><code>-strip</code></p>
<dd> remove all profiles and text attributes from the image</p>
<dt><code>-stroke </code><i>&lt;color&gt;</i></p>
<dd> color to use when stroking a graphic primitive</p>
<dt><code>-strokewidth </code><i>&lt;value&gt;</i></p>
<dd> set the stroke width</p>
<dt><code>-swirl </code><i>&lt;degrees&gt;</i></p>
<dd> swirl image pixels about the center</p>
<dt><code>-texture </code><i>&lt;filename&gt;</i></p>
<dd> name of texture to tile onto the image background</p>
<dt><code>-threshold </code><i>&lt;value&gt;{%}</i></p>
<dd> threshold the image</p>
<dt><code>-thumbnail </code><i>&lt;width&gt;x&lt;height&gt;{%}{@}{!}{&lt;}{&gt;}</i></p>
<dd> resize an image (quickly)</p>
<dt><code>-tile </code><i>&lt;filename&gt;</i></p>
<dd> tile image when filling a graphic primitive</p>
<dt><code>-transform</code></p>
<dd> transform the image</p>
<dt><code>-transparent </code><i>&lt;color&gt;</i></p>
<dd> make this color transparent within the image</p>
<dt><code>-treedepth </code><i>&lt;value&gt;</i></p>
<dd> tree depth for the color reduction algorithm</p>
<dt><code>-trim</code></p>
<dd> trim an image</p>
<dt><code>-type </code><i>&lt;type&gt;</i></p>
<dd> the image type</p>
<dt><code>-units </code><i>&lt;type&gt;</i></p>
<dd> the units of image resolution</p>
<dt><code>-unsharp </code><i>&lt;radius&gt;{x&lt;sigma&gt;}{+&lt;amount&gt;}{+&lt;threshold&gt;}</i></p>
<dd> sharpen the image with an unsharp mask operator</p>
<dt><code>-verbose</code></p>
<dd> print detailed information about the image</p>
<dt><code>-version</code></p>
<dd> print GraphicsMagick version string</p>
<dt><code>-view </code><i>&lt;string&gt;</i></p>
<dd> FlashPix viewing parameters</p>
<dt><code>-virtual-pixel </code><i>&lt;method&gt;</i></p>
<dd> specify contents of &quot;virtual pixels&quot;</p>
<dt><code>-wave </code><i>&lt;amplitude&gt;x&lt;wavelength&gt;</i></p>
<dd> alter an image along a sine wave</p>
<dt><code>-white-point </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> chromaticity white point</p>
<dt><code>-white-threshold </code><i>red[,green][,blue][,opacity]</i></p>
<dd> pixels above the threshold become white </p>
<p> For a more detailed description of each option, see Options, above. </p>
</dl>
<h2>GM MONTAGE</h2>
<p> <code>montage</code> creates a composite image by combining several separate images. The images are tiled on the composite image with the name of the image optionally appearing just below the individual tile. </p>
<p> The composite image is constructed in the following manner. First, each image specified on the command line, except for the last, is scaled to fit the maximum tile size. The maximum tile size by default is 120&#215;120. It can be modified with the <code>-geometry</code> command line argument or X resource. See <code>Options</code> for more information on command line arguments. See <code><a href="/docs/linux/man/1-x/">X</a>(1)</code> for more information on X resources. Note that the maximum tile size need not be a square. </p>
<p> Next the composite image is initialized with the color specified by the <code>-background</code> command line argument or X resource. The width and height of the composite image is determined by the title specified, the maximum tile size, the number of tiles per row, the tile border width and height, the image border width, and the label height. The number of tiles per row specifies how many images are to appear in each row of the composite image. The default is to have 5 tiles in each row and 4 tiles in each column of the composite. A specific value is specified with <code>-tile</code>. The tile border width and height, and the image border width defaults to the value of the X resource <code>-borderwidth</code>. It can be changed with the <code>-borderwidth</code> or <code>-geometry</code> command line argument or X resource. The label height is determined by the font you specify with the <code>-font</code> command line argument or X resource. If you do not specify a font, a font is chosen that allows the name of the image to fit the maximum width of a tiled area. The label colors is determined by the <code>-background</code> and <code>-fill</code> command line argument or X resource. Note, that if the background and pen colors are the same, labels will not appear. </p>
<p> Initially, the composite image title is placed at the top if one is specified (refer to <code>-fill</code>). Next, each image is set onto the composite image, surrounded by its border color, with its name centered just below it. The individual images are left-justified within the width of the tiled area. The order of the images is the same as they appear on the command line unless the images have a scene keyword. If a scene number is specified in each image, then the images are tiled onto the composite in the order of their scene number. Finally, the last argument on the command line is the name assigned to the composite image. By default, the image is written in the <code>MIFF</code> format and can be viewed or printed with <i><a href="/docs/linux/man/1-display/">display</a>(1)</i>. </p>
<p> Note, that if the number of tiles exceeds the default number of 20 (5 per row, 4 per column), more than one composite image is created. To ensure a single image is produced, use <code>-tile</code> to increase the number of tiles to meet or exceed the number of input images. </p>
<p> Finally, to create one or more empty spaces in the sequence of tiles, use the <code>&quot;NULL:&quot;</code> image format. </p>
<p> Note, a composite MIFF image displayed to an X server with <code>display</code> behaves differently than other images. You can think of the composite as a visual image directory. Choose a particular tile of the composite and press a button to display it. See <code><a href="/docs/linux/man/1-display/">display</a>(1)</code> and <code><a href="/docs/linux/man/5-miff/">miff</a>(5)</code></p>
<h2>EXAMPLES</h2>
<p> To create a montage of a cockatoo, a parrot, and a hummingbird and write it to a file called birds, use: </p>
<p>&nbsp;<wbr>gm montage cockatoo.miff parrot.miff hummingbird.miff<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>birds.miff </p>
<p> To tile several bird images so that they are at most 256 pixels in width and 192 pixels in height, surrounded by a red border, and separated by 10 pixels of background color, use: </p>
<p>&nbsp;<wbr>gm montage -geometry 256&#215;192+10+10 -bordercolor red<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>birds.*&nbsp;<wbr>montage.miff </p>
<p> To create an unlabeled parrot image, 640 by 480 pixels, and surrounded by a border of black, use: </p>
<p>&nbsp;<wbr>gm montage -geometry 640&#215;480 -bordercolor black<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-label&nbsp;<wbr>&quot;&quot;&nbsp;<wbr>parrot.miff bird.miff </p>
<p> To create an image of an eagle with a textured background, use: </p>
<p>&nbsp;<wbr>gm montage -texture bumps.jpg eagle.jpg eagle.png </p>
<p> To join several GIF images together without any extraneous graphics (e.g. no label, no shadowing, no surrounding tile frame), use: </p>
<p>&nbsp;<wbr>gm montage&nbsp;<wbr>+frame&nbsp;<wbr>+shadow&nbsp;<wbr>+label -tile 5&#215;1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-geometry 50&#215;50+0+0&nbsp;<wbr>*.png joined.png </p>
<h2>OPTIONS</h2>
<p> Any option you specify on the command line remains in effect for the group of images following it, until the group is terminated by the appearance of any option or <code>-noop</code>. For example, to make a montage of three images, the first with 32 colors, the second with an unlimited number of colors, and the third with only 16 colors, use: </p>
<p>&nbsp;<wbr>gm montage -colors 32 cockatoo.1 -noop cockatoo.2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-colors 16 cockatoo.3 cockatoos.miff </p>
<p> For a more detailed description of each option, see Options, above. </p>
<dl>
<dt><code>-adjoin</code></p>
<dd> join images into a single multi-image file</p>
<dt><code>-affine </code><i>&lt;matrix&gt;</i></p>
<dd> drawing transform matrix</p>
<dt><code>-authenticate </code><i>&lt;string&gt;</i></p>
<dd> decrypt image with this password</p>
<dt><code>-background </code><i>&lt;color&gt;</i></p>
<dd> the background color</p>
<dt><code>-blue-primary </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> blue chromaticity primary point</p>
<dt><code>-blur </code><i>&lt;radius&gt;{x&lt;sigma&gt;}</i></p>
<dd> blur the image with a Gaussian operator</p>
<dt><code>-bordercolor </code><i>&lt;color&gt;</i></p>
<dd> the border color</p>
<dt><code>-borderwidth </code><i>&lt;geometry&gt;</i></p>
<dd> the border width</p>
<dt><code>-chop </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}</i></p>
<dd> remove pixels from the interior of an image</p>
<dt><code>-colors </code><i>&lt;value&gt;</i></p>
<dd> preferred number of colors in the image</p>
<dt><code>-colorspace </code><i>&lt;value&gt;</i></p>
<dd> the type of colorspace</p>
<dt><code>-comment </code><i>&lt;string&gt;</i></p>
<dd> annotate an image with a comment</p>
<dt><code>-compose </code><i>&lt;operator&gt;</i></p>
<dd> the type of image composition</p>
<dt><code>-compress </code><i>&lt;type&gt;</i></p>
<dd> the type of image compression</p>
<dt><code>-crop </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}</i></p>
<dd> preferred size and location of the cropped image</p>
<dt><code>-debug </code><i>&lt;events&gt;</i></p>
<dd> enable debug printout</p>
<dt><code>-define </code><i>&lt;key&gt;{=&lt;value&gt;},&#8230;</i></p>
<dd> add coder/decoder specific options</p>
<dt><code>-density </code><i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd> horizontal and vertical resolution in pixels of the image</p>
<dt><code>-depth </code><i>&lt;value&gt;</i></p>
<dd> depth of the image</p>
<dt><code>-display </code><i>&lt;host:display[.screen]&gt;</i></p>
<dd> specifies the X server to contact</p>
<dt><code>-dispose </code><i>&lt;method&gt;</i></p>
<dd> GIF disposal method</p>
<dt><code>-dither</code></p>
<dd> apply Floyd/Steinberg error diffusion to the image</p>
<dt><code>-draw </code><i>&lt;string&gt;</i></p>
<dd> annotate an image with one or more graphic primitives</p>
<dt><code>-encoding </code><i>&lt;type&gt;</i></p>
<dd> specify the text encoding</p>
<dt><code>-endian </code><i>&lt;type&gt;</i></p>
<dd> specify endianness (MSB, LSB, or Native) of image</p>
<dt><code>-fill </code><i>&lt;color&gt;</i></p>
<dd> color to use when filling a graphic primitive</p>
<dt><code>-filter </code><i>&lt;type&gt;</i></p>
<dd> use this type of filter when resizing an image</p>
<dt><code>-font </code><i>&lt;name&gt;</i></p>
<dd> use this font when annotating the image with text</p>
<dt><code>-frame </code><i>&lt;width&gt;x&lt;height&gt;+&lt;outer bevel width&gt;+&lt;inner bevel width&gt;</i></p>
<dd> surround the image with an ornamental border</p>
<dt><code>-gamma </code><i>&lt;value&gt;</i></p>
<dd> level of gamma correction</p>
<dt><code>-geometry </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}{@}{!}{^}{&lt;}{&gt;}</i></p>
<dd> Specify dimension, offset, and resize options.</p>
<dt><code>-gravity </code><i>&lt;type&gt;</i></p>
<dd> direction primitive gravitates to when annotating the image.</p>
<dt><code>-green-primary </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> green chromaticity primary point</p>
<dt><code>-help</code></p>
<dd> print usage instructions</p>
<dt><code>-interlace </code><i>&lt;type&gt;</i></p>
<dd> the type of interlacing scheme</p>
<dt><code>-label </code><i>&lt;name&gt;</i></p>
<dd> assign a label to an image</p>
<dt><code>-limit </code><i>&lt;type&gt; &lt;value&gt;</i></p>
<dd> Disk, File, Map, Memory, Pixels, Width, Height or Threads resource limit</p>
<dt><code>-log </code><i>&lt;string&gt;</i></p>
<dd> Specify format for debug log</p>
<dt><code>-matte</code></p>
<dd> store matte channel if the image has one</p>
<dt><code>-mattecolor </code><i>&lt;color&gt;</i></p>
<dd> specify the color to be used with the <code>-frame</code> option</p>
<dt><code>-mode </code><i>&lt;value&gt;</i></p>
<dd> mode of operation</p>
<dt><code>-monitor</code></p>
<dd> show progress indication</p>
<dt><code>-monochrome</code></p>
<dd> transform the image to black and white</p>
<dt><code>-noop</code></p>
<dd> NOOP (no option)</p>
<dt><code>-page </code><i>&lt;width&gt;x&lt;height&gt;{+-}&lt;x&gt;{+-}&lt;y&gt;{%}{!}{&lt;}{&gt;}</i></p>
<dd> size and location of an image canvas</p>
<dt><code>-pen </code><i>&lt;color&gt;</i></p>
<dd> (This option has been replaced by the -fill option)</p>
<dt><code>-pointsize </code><i>&lt;value&gt;</i></p>
<dd> pointsize of the PostScript, X11, or TrueType font</p>
<dt><code>-quality </code><i>&lt;value&gt;</i></p>
<dd> JPEG/MIFF/PNG/TIFF compression level</p>
<dt><code>-red-primary </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> red chromaticity primary point</p>
<dt><code>-render</code></p>
<dd> render vector operations</p>
<dt><code>-repage </code><i> &lt;width&gt;x&lt;height&gt;+xoff+yoff[!]</i></p>
<dd> Adjust image page offsets</p>
<dt><code>-resize </code><i>&lt;width&gt;x&lt;height&gt;{%}{@}{!}{&lt;}{&gt;}</i></p>
<dd> resize an image</p>
<dt><code>-rotate </code><i>&lt;degrees&gt;{&lt;}{&gt;}</i></p>
<dd> rotate the image</p>
<dt><code>-sampling-factor </code><i>&lt;horizontal_factor&gt;x&lt;vertical_factor&gt;</i></p>
<dd> chroma subsampling factors</p>
<dt><code>-scenes </code><i>&lt;value-value&gt;</i></p>
<dd> range of image scene numbers to read</p>
<dt><code>-shadow </code><i>&lt;radius&gt;{x&lt;sigma&gt;}</i></p>
<dd> shadow the montage</p>
<dt><code>-sharpen </code><i>&lt;radius&gt;{x&lt;sigma&gt;}</i></p>
<dd> sharpen the image</p>
<dt><code>-size </code><i>&lt;width&gt;x&lt;height&gt;{+offset}</i></p>
<dd> width and height of the image</p>
<dt><code>-strip</code></p>
<dd> remove all profiles and text attributes from the image</p>
<dt><code>-stroke </code><i>&lt;color&gt;</i></p>
<dd> color to use when stroking a graphic primitive</p>
<dt><code>-strokewidth </code><i>&lt;value&gt;</i></p>
<dd> set the stroke width</p>
<dt><code>-texture </code><i>&lt;filename&gt;</i></p>
<dd> name of texture to tile onto the image background</p>
<dt><code>-thumbnail </code><i>&lt;width&gt;x&lt;height&gt;{%}{@}{!}{&lt;}{&gt;}</i></p>
<dd> resize an image (quickly)</p>
<dt><code>-tile </code><i>&lt;geometry&gt;</i></p>
<dd> layout of images [<i>montage</i>]</p>
<dt><code>-title </code><i>&lt;string&gt;</i></p>
<dd> assign title to displayed image [<i>animate, display, montage</i>]</p>
<dt><code>-transform</code></p>
<dd> transform the image</p>
<dt><code>-transparent </code><i>&lt;color&gt;</i></p>
<dd> make this color transparent within the image</p>
<dt><code>-treedepth </code><i>&lt;value&gt;</i></p>
<dd> tree depth for the color reduction algorithm</p>
<dt><code>-trim</code></p>
<dd> trim an image</p>
<dt><code>-type </code><i>&lt;type&gt;</i></p>
<dd> the image type</p>
<dt><code>-verbose</code></p>
<dd> print detailed information about the image</p>
<dt><code>-version</code></p>
<dd> print GraphicsMagick version string</p>
<dt><code>-white-point </code><i>&lt;x&gt;,&lt;y&gt;</i></p>
<dd> chromaticity white point </p>
<p> For a more detailed description of each option, see Options, above. </p>
</dl>
<h2>X RESOURCES</h2>
<p> <code>Montage</code> options can appear on the command line or in your X resource file. Options on the command line supersede values specified in your X resource file. See <code><a href="/docs/linux/man/1-x/">X</a>(1)</code> for more information on X resources. </p>
<p> All <code>montage</code> options have a corresponding X resource. In addition, <code>montage</code> uses the following X resources:</p>
<dl>
<dt><code>background </code><i>(class Background)</i></p>
<dd> background color </p>
<p> Specifies the preferred color to use for the composite image background. The default is #ccc.</p>
<dt><code>borderColor </code><i>(class BorderColor)</i></p>
<dd> border color </p>
<p> Specifies the preferred color to use for the composite image border. The default is #ccc.</p>
<dt><code>borderWidth </code><i>(class BorderWidth)</i></p>
<dd> border width </p>
<p> Specifies the width in pixels of the composite image border. The default is 2.</p>
<dt><code>font </code><i>(class Font)</i></p>
<dd> font to use </p>
<p> Specifies the name of the preferred font to use when displaying text within the composite image. The default is 9&#215;15, fixed, or 5&#215;8 determined by the composite image size.</p>
<dt><code>matteColor </code><i>(class MatteColor)</i></p>
<dd> color of the frame </p>
<p> Specify the color of an image frame. A 3D effect is achieved by using highlight and shadow colors derived from this color. The default value is #697B8F.</p>
<dt><code>pen </code><i>(class Pen)</i></p>
<dd> text color </p>
<p> Specifies the preferred color to use for text within the composite image. The default is black.</p>
<dt><code>title </code><i>(class Title)</i></p>
<dd> composite image title </p>
<p> This resource specifies the title to be placed at the top of the composite image. The default is not to place a title at the top of the composite image.</dl>
<h2>GM TIME</h2>
<h2>DESCRIPTION</h2>
<p> <code>time</code> executes an arbitrary <code>gm</code> utility command (e.g. <code>convert</code>) and reports the user and elapsed time. This provides way to measure command execution times similar to the Unix &#8216;time&#8217; command but in a portable and consistent way.</p>
<h2>EXAMPLES</h2>
<p> To obtain time information for the execution of a command: </p>
<p> % gm time convert input.ppm -gaussian 0x2 output.ppm convert input.ppm -gaussian 0x2 output.ppm 22.60s user 0.00s system 2354% cpu 0.960 total </p>
<p> Here is the interpretation of the above output: </p>
<p>&nbsp;<wbr><code>user</code>&nbsp;<wbr>&#8211; the total user time consumed.<br />
&nbsp;<wbr><code>system</code>&nbsp;<wbr>&#8211; the total system time consumed.<br />
&nbsp;<wbr><code>total</code>&nbsp;<wbr>&#8211; the total elapsed time consumed. </p>
<h2>OPTIONS</h2>
<p> The time command reqires no options other than the gm command to execute.</p>
<h2>GM VERSION</h2>
<h2>DESCRIPTION</h2>
<p> <code>version</code> displays the software release version, build quantum (pixel sample) depth, web site URL, copyright notice, enabled features support, configuration parameters, and final build options used to build the software. The available information depends on how the software was configured and the host system.</p>
<h2>EXAMPLES</h2>
<p> To display the version information: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>%&nbsp;<wbr>gm -version<br />
&nbsp;<wbr>&nbsp;<wbr>GraphicsMagick 1.3.19 2013-12-31 Q16&nbsp;<wbr><a rel="nofollow" href="http://www.GraphicsMagick.org/">http://www.GraphicsMagick.org/</a><br />
&nbsp;<wbr>&nbsp;<wbr>Copyright&nbsp;<wbr>(C)&nbsp;<wbr>2002-2013 GraphicsMagick Group.<br />
&nbsp;<wbr>&nbsp;<wbr>Additional copyrights and licenses apply to this software.<br />
&nbsp;<wbr>&nbsp;<wbr>See&nbsp;<wbr><a rel="nofollow" href="http://www.GraphicsMagick.org/www/Copyright.html">http://www.GraphicsMagick.org/www/Copyright.html</a>&nbsp;<wbr>for details.<br />
&nbsp;<wbr>&nbsp;<wbr>Feature Support:<br />
&nbsp;<wbr>Thread Safe&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>yes<br />
&nbsp;<wbr>Large Files&nbsp;<wbr>(&gt;&nbsp;<wbr>32 bit)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>yes<br />
&nbsp;<wbr>Large Memory&nbsp;<wbr>(&gt;&nbsp;<wbr>32 bit)&nbsp;<wbr>&nbsp;<wbr>no<br />
&nbsp;<wbr>BZIP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>yes<br />
&nbsp;<wbr>DPS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no<br />
&nbsp;<wbr>FlashPix&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no<br />
&nbsp;<wbr>FreeType&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>yes<br />
&nbsp;<wbr>Ghostscript&nbsp;<wbr>(Library)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no<br />
&nbsp;<wbr>JBIG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no<br />
&nbsp;<wbr>JPEG-2000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>yes<br />
&nbsp;<wbr>JPEG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>yes<br />
&nbsp;<wbr>Little CMS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>yes<br />
&nbsp;<wbr>Loadable Modules&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no<br />
&nbsp;<wbr>OpenMP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>yes&nbsp;<wbr>(201107)<br />
&nbsp;<wbr>PNG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>yes<br />
&nbsp;<wbr>TIFF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>yes<br />
&nbsp;<wbr>TRIO&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no<br />
&nbsp;<wbr>UMEM&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>yes<br />
&nbsp;<wbr>WMF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no<br />
&nbsp;<wbr>X11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>yes<br />
&nbsp;<wbr>XML&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>yes<br />
&nbsp;<wbr>ZLIB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>yes<br />
&nbsp;<wbr>&nbsp;<wbr>Host type: i386-pc-solaris2.11<br />
&nbsp;<wbr>&nbsp;<wbr>Configured using the command:<br />
&nbsp;<wbr>./configure&nbsp;<wbr>&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>Final Build Parameters:<br />
&nbsp;<wbr>CC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>CFLAGS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>CPPFLAGS&nbsp;<wbr>=&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>CXX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>CXXFLAGS&nbsp;<wbr>=&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>LDFLAGS&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>LIBS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>&#8230; </p>
<h2>OPTIONS</h2>
<p> The version command does not currently support any options. </p>
<h2>Index</h2>
