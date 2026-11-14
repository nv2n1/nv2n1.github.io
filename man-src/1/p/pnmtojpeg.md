---
title: "pnmtojpeg(1)"
name: "pnmtojpeg"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmtojpeg/"
description: "pnmtojpeg – convert PNM image to a JFIF (\"JPEG\") image"
---

<h2 class="name">NAME</h2>
<p> pnmtojpeg &#8211; convert PNM image to a JFIF (&quot;JPEG&quot;) image</p>
<h2>SYNOPSIS</h2>
<p> <code>pnmtojpeg</code> [ <i>options</i> ] [ <i>filename</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>pnmtojpeg</code> converts the named PBM, PGM, or PPM image file, or the standard input if no file is named, to a JFIF file on the standard output. </p>
<p> <code>pnmtojpeg</code> uses the Independent JPEG Group&#8217;s JPEG library to create the output file. See <code><a rel="nofollow" href="http://www.ijg.org">http://www.ijg.org</a> </code> for information on the library. </p>
<p> &quot;JFIF&quot; is the correct name for the image format commonly known as &quot;JPEG.&quot; Strictly speaking, JPEG is a method of compression. The image format using JPEG compression that is by far the most common is JFIF. There is also a subformat of TIFF that uses JPEG compression. </p>
<p> EXIF is an image format that is a subformat of JFIF (to wit, a JFIF file that contains an EXIF header as an APP1 marker). <code>pnmtojpeg</code> creates an EXIF image when you specify the <code>-exif</code> option. </p>
<h2>OPTIONS</h2>
<p> The basic options are:</p>
<dl>
<dt><code>&#8211;exif=</code><i>filespec</i></p>
<dd> This option specifies that the output image is to be EXIF (a subformat of JFIF), i.e. it will have an EXIF header as a JFIF APP1 marker. The contents of that marker are the contents of the specified file. The special value <code>&#8211;</code> means to read the EXIF header contents from standard input. It is invalid to specify standard input for both the EXIF header and the input image. </p>
<p> The EXIF file starts with a two byte field which is the length of the file, including the length field, in pure binary, most significant byte first. The special value of zero for the length field means there is to be no EXIF header, i.e. the same as no <code>-exif</code> option. This is useful for when you convert a file from JFIF to PNM using <code>jpegtopnm</code>, then transform it, then convert it back to JFIF with <code>pnmtojpeg</code>, and you don&#8217;t know whether or not it includes an EXIF header. <code>jpegtopnm</code> creates an EXIF file containing nothing but two bytes of zero when the input JFIF file has no EXIF header. Thus, you can transfer any EXIF header from the input JFIF to the output JFIF without worrying about whether an EXIF header actually exists. </p>
<p> The contents of the EXIF file after the length field are the exact byte for byte contents of the APP1 marker, not counting the length field, that constitutes the EXIF header. </p>
<dt><code>&#8211;quality=</code><i>n</i></p>
<dd> Scale quantization tables to adjust image quality. <i>n</i> is 0 (worst) to 100 (best); default is 75. (See below for more info.)</p>
<dt><code>&#8211;grayscale</code></p>
<dd>
<dt><code>&#8211;greyscale</code></p>
<dd> Create gray scale JFIF file. With this option, <code>pnmtojpeg</code> converts color input to gray scale. If you don&#8217;t specify this option, The output file is in color format if the input is PPM, and grayscale format if the input is PBM or PGM. </p>
<p> In the PPM input case, even if all the colors in the image are gray, the output is in color format. Of course, the colors in it are still gray. The difference is that color format takes up a lot more space and takes longer to create and process.</p>
<dt><code>&#8211;optimize</code></p>
<dd> Perform optimization of entropy encoding parameters. Without this, <code>pnmtojpeg</code> uses default encoding parameters. <code>&#8211;optimize</code> usually makes the JFIF file a little smaller, but <code>pnmtojpeg</code> runs somewhat slower and needs much more memory. Image quality and speed of decompression are unaffected by <code>&#8211;optimize</code>.</p>
<dt><code>&#8211;progressive</code></p>
<dd> Create a progressive JPEG file (see below).</p>
<dt><code>&#8211;comment=</code><i>text</i></p>
<dd> Include a comment marker in the JFIF output, with comment text <i>text</i>. Without this option, there are no comment markers in the output. </p>
</dl>
<p> The <code>&#8211;quality</code> option lets you trade off compressed file size against quality of the reconstructed image: the higher the quality setting, the larger the JFIF file, and the closer the output image will be to the original input. Normally you want to use the lowest quality setting (smallest file) that decompresses into something visually indistinguishable from the original image. For this purpose the quality setting should be between 50 and 95; the default of 75 is often about right. If you see defects at <code>&#8211;quality=75</code>, then go up 5 or 10 counts at a time until you are happy with the output image. (The optimal setting will vary from one image to another.) </p>
<p> <code>&#8211;quality=100</code> generates a quantization table of all 1&#8217;s, minimizing loss in the quantization step (but there is still information loss in subsampling, as well as roundoff error). This setting is mainly of interest for experimental purposes. Quality values above about 95 are <i>not</i> recommended for normal use; the compressed file size goes up dramatically for hardly any gain in output image quality. </p>
<p> In the other direction, quality values below 50 will produce very small files of low image quality. Settings around 5 to 10 might be useful in preparing an index of a large image library, for example. Try <code>&#8211;quality=2</code> (or so) for some amusing Cubist effects. (Note: quality values below about 25 generate 2-byte quantization tables, which are considered optional in the JFIF standard. <code>pnmtojpeg</code> emits a warning message when you give such a quality value, because some other JFIF programs may be unable to decode the resulting file. Use <code>&#8211;baseline</code> if you need to ensure compatibility at low quality values.) </p>
<p> The <code>&#8211;progressive</code> option creates a &quot;progressive JPEG&quot; file. In this type of JFIF file, the data is stored in multiple scans of increasing quality. If the file is being transmitted over a slow communications link, the decoder can use the first scan to display a low-quality image very quickly, and can then improve the display with each subsequent scan. The final image is exactly equivalent to a standard JFIF file of the same quality setting, and the total file size is about the same &#8212; often a little smaller. <code>Caution:</code> progressive JPEG is not yet widely implemented, so many decoders will be unable to view a progressive JPEG file at all. </p>
<p> Options for advanced users:</p>
<dl>
<dt><code>&#8211;dct=int</code></p>
<dd> Use integer DCT method (default).</p>
<dt><code>&#8211;dct=fast</code></p>
<dd> Use fast integer DCT (less accurate).</p>
<dt><code>&#8211;dct=float</code></p>
<dd> Use floating-point DCT method. The float method is very slightly more accurate than the int method, but is much slower unless your machine has very fast floating-point hardware. Also note that results of the floating-point method may vary slightly across machines, while the integer methods should give the same results everywhere. The fast integer method is much less accurate than the other two.</p>
<dt><code>&#8211;restart=</code><i>n</i></p>
<dd> Emit a JPEG restart marker every <i>n </i> MCU rows, or every <i>n </i> MCU blocks if you append <code>B </code> to the number. <code>&#8211;restart 0</code> (the default) means no restart markers.</p>
<dt><code>&#8211;smooth=</code><i>n</i></p>
<dd> Smooth the input image to eliminate dithering noise. <i>n</i>, ranging from 1 to 100, indicates the strength of smoothing. 0 (the default) means no smoothing.</p>
<dt><code>&#8211;maxmemory=</code><i>n</i></p>
<dd> Set a limit for amount of memory to use in processing large images. Value is in thousands of bytes, or millions of bytes if you append <code>M </code> to the number. For example, <code>&#8211;max=4m</code> selects 4,000,000 bytes. If <code>pnmtojpeg</code> needs more space, it will use temporary files.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Print to the Standard Error file messages about the conversion process. This can be helpful in debugging problems.</dl>
<p> The <code>&#8211;restart</code> option tells <code>pnmtojpeg </code> to insert extra markers that allow a JPEG decoder to resynchronize after a transmission error. Without restart markers, any damage to a compressed file will usually ruin the image from the point of the error to the end of the image; with restart markers, the damage is usually confined to the portion of the image up to the next restart marker. Of course, the restart markers occupy extra space. We recommend <code>&#8211;restart=1</code> for images that will be transmitted across unreliable networks such as Usenet. </p>
<p> The <code>&#8211;smooth</code> option filters the input to eliminate fine-scale noise. This is often useful when converting dithered images to JFIF: a moderate smoothing factor of 10 to 50 gets rid of dithering patterns in the input file, resulting in a smaller JFIF file and a better-looking image. Too large a smoothing factor will visibly blur the image, however. </p>
<p> Options for wizards:</p>
<dl>
<dt><code>&#8211;baseline</code></p>
<dd> Force baseline-compatible quantization tables to be generated. This clamps quantization values to 8 bits even at low quality settings. (This switch is poorly named, since it does not ensure that the output is actually baseline JPEG. For example, you can use <code>&#8211;baseline</code> and <code>&#8211;progressive</code> together.)</p>
<dt><code>&#8211;qtables=</code><i>filespec</i></p>
<dd> Use the quantization tables given in the specified text file.</p>
<dt><code>&#8211;qslots=n[,&#8230;]</code></p>
<dd> Select which quantization table to use for each color component.</p>
<dt><code>&#8211;sample=</code><i>HxV[,&#8230;]</i></p>
<dd> Set JPEG sampling factors for each color component.</p>
<dt><code>&#8211;scans=</code><i>filespec</i></p>
<dd> Use the scan script given in the specified text file. See below for information on scan scripts.</dl>
<p> The &quot;wizard&quot; options are intended for experimentation with JPEG. If you don&#8217;t know what you are doing, <code>don&#8217;t use them</code>. These switches are documented further in the file wizard.doc that comes with the Independent JPEG Group&#8217;s JPEG library.</p>
<h2>EXAMPLES</h2>
<p> This example compresses the PPM file foo.ppm with a quality factor of 60 and saves the output as foo.jpg:</p>
<dl>
<dt>
<dd> <code>pnmtojpeg &#8211;quality=60 foo.ppm &gt; foo.jpg</code></p>
<dt>
<dd> <code>cat foo.bmp | bmptoppm | pnmtojpeg &gt; foo.jpg</code> </p>
</dl>
<h2>HINTS</h2>
<p> JFIF is not ideal for cartoons, line drawings, and other images that have only a few distinct colors. For those, try instead <code>pnmtopng</code> or <code>ppmtobmp</code>. If you need to convert such an image to JFIF, though, you should experiment with <code>pnmtojpeg</code>&#8216;s <code>&#8211;quality</code> and <code>&#8211;smooth</code> options to get a satisfactory conversion. <code>&#8211;smooth 10</code> or so is often helpful. </p>
<p> JPEG compression is notable for being a &quot;lossy.&quot; This means that, unlike with most graphics conversions, you lose information, which means image quality, when you convert to JFIF. If you convert from PPM to JFIF and back repeatedly, image quality loss will accumulate. After ten or so cycles the image may be noticeably worse than it was after one cycle. </p>
<p> Because of this, you should do all the manipulation you have to do on the image in some other format and convert to JFIF as the last step. And if you can keep a copy in the original format, so much the better. PNG is a good choice for a format that is lossless, yet fairly compact. GIF is another way to go, but chances are you can&#8217;t create a GIF image without owing a lot of money to Unisys and IBM, holders of patents on the LZW compression used in the GIF format. </p>
<p> The <code>&#8211;optimize</code> option to <code>pnmtojpeg</code> is worth using when you are making a &quot;final&quot; version for posting or archiving. It&#8217;s also a win when you are using low quality settings to make very small JFIF files; the percentage improvement is often a lot more than it is on larger files. (At present, <code>&#8211;optimize</code> mode is automatically in effect when you generate a progressive JPEG file). </p>
<p> Another program, <code>cjpeg</code>, is similar. <code>cjpeg</code> is maintained by the Independent JPEG Group and packaged with the JPEG library which <code>pnmtojpeg</code> uses for all its JPEG work. Because of that, you may expect it to exploit more current JPEG features. Also, since you have to have the library to run <code>pnmtojpeg</code>, but not vice versa, <code>cjpeg</code> may be more commonly available. </p>
<p> On the other hand, <code>cjpeg</code> does not use the NetPBM libraries to process its input, as all the NetPBM tools such as <code>pnmtojpeg</code> do. This means it is less likely to be consistent with all the other programs that deal with the NetPBM formats. Also, the command syntax of <code>pnmtojpeg</code> is consistent with that of the other Netpbm tools, unlike <code>cjpeg</code>. </p>
<h2>SCAN SCRIPTS</h2>
<p> Use the <code>-scan</code> option to specify a scan script. Or use the <code>-progressive</code> option to specify a particular built-in scan script. </p>
<p> Just what a scan script is, and the basic format of the scan script file, is covered in the <code>wizard.doc </code> file that comes with the Independent JPEG Group&#8217;s JPEG library. Scan scripts are same for <code>pnmtojpeg</code> as the are for <code>cjpeg</code>. </p>
<p> This section contains additional information that isn&#8217;t, but probably should be, in that document. </p>
<p> First, there are many restrictions on what is a valid scan script. The JPEG library, and thus <code>pnmtojpeg</code>, checks thoroughly for any lack of compliance with these restrictions, but does little to tell you how the script fails to comply. The messages are very general and sometimes untrue. </p>
<p> To start with, the entries for the DC coefficient must come before any entries for the AC coefficients. The DC coefficient is Coefficient 0; all the other coefficients are AC coefficients. So in an entry for the DC coefficient, the two numbers after the colon must be 0 and 0. In an entry for AC coefficients, the first number after the colon must not be 0. </p>
<p> In a DC entry, the color components must be in increasing order. E.g. &quot;0,2,1&quot; before the colon is wrong. So is &quot;0,0,0&quot;. </p>
<p> In an entry for an AC coeffient, you must specify only one color component. I.e. there can be only one number before the colon. </p>
<p> In the first entry for a particular coefficient for a particular color component, the &quot;Ah&quot; value must be zero, but the Al value can be any valid bit number. In subsequent entries, Ah must be the Al value from the previous entry (for that coefficient for that color component), and the Al value must be one less than the Ah value. </p>
<p> The script must ultimately specify at least some of the DC coefficent for every color component. Otherwise, you get the error message &quot;Script does not transmit all the data.&quot; You need not specify all of the bits of the DC coefficient, or any of the AC coefficients. </p>
<p> There is a standard option in building the JPEG library to omit scan script capability. If for some reason your library was built with this option, you get the message &quot;Requested feature was omitted at compile time.&quot; </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>JPEGMEM</code></p>
<dd> If this environment variable is set, its value is the default memory limit. The value is specified as described for the <code>&#8211;maxmemory</code> option. An explicit <code>&#8211;maxmemory </code> option overrides any <code>JPEGMEM</code>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cjpeg/">cjpeg</a></code>(1), <code><a href="/docs/linux/man/1-djpeg/">djpeg</a></code>(1), <code><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></code>(1), <code><a href="/docs/linux/man/1-rdjpgcom/">rdjpgcom</a></code>(1), <code><a href="/docs/linux/man/1-wrjpgcom/">wrjpgcom</a></code>(1)<br />
 <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), <code><a href="/docs/linux/man/5-pgm/">pgm</a></code>(5), <code><a href="/docs/linux/man/1-jpegtopnm/">jpegtopnm</a></code>(1)<br />
 Wallace, Gregory K. &quot;The JPEG Still Picture Compression Standard&quot;, Communications of the ACM, April 1991 (vol. 34, no. 4), pp. 30-44.</p>
<h2>LIMITATIONS</h2>
<p> Arithmetic coding is not supported for legal reasons. </p>
<p> The program could be much faster. </p>
<h2>AUTHOR</h2>
<p> <code>pnmtojpeg</code> and this man page were derived in large part from <code>cjpeg</code>, by the Independent JPEG Group. The program is otherwise by Bryan Henderson on March 07, 2000. </p>
<h2>Index</h2>
