---
title: "csepdjvu(1)"
name: "csepdjvu"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csepdjvu/"
description: "csepdjvu – DjVu encoder for separated data files."
---

<h2>NAME</h2>
<p> csepdjvu &#8211; DjVu encoder for separated data files. </p>
<h2>SYNOPSIS</h2>
<p> <code>csepdjvu [</code><i>options</i><code>] [</code><i>sepfiles</i><code>]&#8230; </code><i>outputdjvufile</i> </p>
<h2>DESCRIPTION</h2>
<p> This program creates a DjVuDocument file <i>outputdjvufile</i> from separated data files <i>sepfiles</i>. It can read separated data from the standard input when given a single dash instead of the separated data file names. This feature is intended for pre-processing programs that push separated data into <code>csepdjvu</code> via a pipe. </p>
<p> Each separated data file represents one or more page images. When the program arguments specify multiple pages, all the pages are encoded and saved as a bundled multi-page document. When the program arguments specify a single page, the page is encoded and saved as a single page file. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d </code><i>n</i></p>
<dd> Specify the resolution information encoded into the output file expressed in dots per inch. The resolution information encoded in DjVu files determine how the decoder scales the image on a particular display. Meaningful resolutions range from 25 to 6000. The default value is 300 dpi.</p>
<dt><code>-q </code><i>n</i><code>,&#8230;,</code><i>n</i></p>
<dd>
<dt><code>-q </code><i>n</i><code>+&#8230;+</code><i>n</i></p>
<dd> Specify the encoding quality of the IW44 encoded background layer. The option argument contain several integers (one per chunk) separated by either commas or pluses. This option is similar to option <code>-slice</code> of program <code>c44</code>. Please refer to the <code><a href="/docs/linux/man/1-c44/">c44</a></code>(1) man page for additional details. The default quality specification is <code>-q 72,83,93,103</code>. </p>
<p> This option does not apply to uniformly white background that were not specified by the separated data but are called for by the DjVu specification. Such background images always come at the lowest possible resolution and with a standard quality setting that ensures the color uniformity.</p>
<dt><code>-t</code></p>
<dd> Program <code>csepdjvu</code> interprets certain comments in the separated file to construct a hidden text layer in the DjVu file. This layer records the location of each word for hiliting purposes. This option reduces the file size by simply recording the location of each line.</p>
<dt><code>-v</code></p>
<dd> Display a brief message describing each page.</p>
<dt><code>-vv</code></p>
<dd> Display extensive informational messages during encoding. </p>
</dl>
<h2>SEPARATED DATA FILE FORMAT</h2>
<p> Each separated data file contains a concatenation of one or more separated page images. Each page is logically represented by a foreground image with a transparent color and by a background image visible through the transparent pixels. The data for each separated page image is the concatenation of the following data blocks:</p>
<dl>
<dt>*</p>
<dd> A foreground image encoded using either the &quot;Color RLE format&quot; or the &quot;Bitonal RLE format&quot;. These formats are described later in this section.</p>
<dt>*</p>
<dd> An optional background image encoded as a &quot;Portable Pixmap&quot; ( <font SIZE="-1">PPM</font> ). This well known format is summarized later in this section. The absence of a background image simply indicates that a uniformly white background should be assumed.</p>
<dt>*</p>
<dd> An arbitrary number of comment lines starting with character &quot;#&quot; and terminated by a linefeed character. Comment lines whose first word starts with a capital letter have special meanings documented later in this document.</dl>
<p> The dimensions (width and height) of the background image must be obtained by rounding up the quotient of the foreground image dimensions by an integer reduction factor ranging from 1 to 12. Assume, for instance, that the width of the foreground is 2507 and the reduction factor is 3. The width of the background image will be the integer ratio (2507+2)/3. </p>
<h3>Color RLE format</h3>
<p> The Color RLE format is a simple run-length encoding scheme for color images with a limited number of distinct colors. The data always begin with a text header composed of the two characters &quot;R6&quot;, the number of columns, the number of rows, and the number of color palette entries. All numbers are expressed in decimal <font SIZE="-1">ASCII.</font> These four items are separated by blank characters (space, tab, carriage return, or linefeed) or by comment lines introduced by character &quot;#&quot;. The last number is followed by exactly one character which usually is a linefeed character. </p>
<p> The header is followed by the color palette containing three bytes per color entry. The bytes represent the red, green, and blue components of the color. </p>
<p> The palette is followed by a collection of four bytes integers (most significant bit first) representing runs of pixels with an identical color. The twelve upper bits of this integer indicate the index of the run color in the palette entry. The twenty lower bits of the integer indicate the run length. Color indices greater than 0xff0 are reserved. Color index 0xfff is used for transparent runs. Each row is represented by a sequence of runs whose lengths add up to the image width. Rows are encoded starting with the top row and progressing toward the bottom row. </p>
<h3>Bitonal RLE format</h3>
<p> The Bitonal RLE format is a simple run-length encoding scheme for bitonal images. The data always begin with a text header composed of the two characters &quot;R4&quot;, the number of columns, and the number of rows. All numbers are expressed in decimal <font SIZE="-1">ASCII.</font> These three items are separated by blank characters (space, tab, carriage return, or linefeed) or by comment lines introduced by character &quot;#&quot;. The last number is followed by exactly one character which usually is a linefeed character. </p>
<p> The rest of the file encodes a sequence of numbers representing the lengths of alternating runs of transparent and black pixels. Lines are encoded starting with the top line and progressing toward the bottom line. Each line starts with a white run. The decoder knows that a line is finished when the sum of the run lengths for that line is equal to the number of columns in the image. Numbers in range 0 to 191 are represented by a single byte in range 0x00 to 0xbf. Numbers in range 192 to 16383 are represented by a two byte sequence: the first byte, in range 0xc0 to 0xff, encodes the six most significant bits of the number, the second byte encodes the remaining eight bits of the number. This scheme allows for runs of length zero, which are useful when a line starts with a black pixel, and when a very long run (whose length exceeds 16383) must be split into smaller runs. </p>
<h3>Portable Pixmap (PPM) format</h3>
<p> The Portable Pixmap format is a well known format for representing color images. Check the <code><a href="/docs/linux/man/1-ppm/">ppm</a></code>(1) man page for complete information. </p>
<p> The data always begin with a text header composed of the two characters &quot;P6&quot;, the number of columns, the number of rows, and the maximal value of a color component (usually 255). All numbers are expressed in decimal <font SIZE="-1">ASCII.</font> These three items are separated by blank characters (space, tab, carriage return, or linefeed) or by comment lines introduced by character &quot;#&quot;. The last number is followed by exactly one character which usually is a linefeed character. </p>
<p> The rest of the file encodes all the pixels. Each pixel is represented by three bytes representing the red, green and blue component of the pixel. Pixels are ordered in left to right, top to bottom. </p>
<h3>Comments in separated files</h3>
<p> Each page is followed by an arbitrary number of comment lines starting with character &quot;#&quot; and terminated by a linefeed character. Comment lines whose first word starts with a capital letter have special meanings. The following constructs are currently defined:</p>
<dl>
<dt>*</p>
<dd> <code># T </code><i>px</i><code>:</code><i>py</i><i>dx</i><code>:</code><i>dy</i><i>w</i><code>x</code><i>h</i><code>+</code><i>x</i><code>+</code><i>y</i><code> (</code><i>string</i><code>)</code><br />
 This constructs indicates that the piece of text <i>string</i> must be associated with an area of size <i>w</i>x<i>h</i> at position <i>x</i>,<i>y</i> relative to the lower left corner of the page. The string is UTF-8 encoded. Special characters can be escaped as in PostScript using the backslash character. Integers <i>px</i>, and <i>py</i> represent the position of the current point on the text baseline before the text was drawn. The drawing operation then moves the current point by <i>dx</i>, and <i>dy</i> pixels. When such comments are present, <code>csepdjvu</code> produces a hidden text layer for the corresponding pages.</p>
<dt>*</p>
<dd> <code># L </code><i>w</i><code>x</code><i>h</i><code>+</code><i>x</i><code>+</code><i>y</i><code> (</code><i>url</i><code>)</code><br />
 This construct indicates that an hyperlink to url <i>url</i> should be associated with area of size <i>w</i>x<i>h</i> at position <i>x</i>,<i>y</i>. When such comments are present, <code>csepdjvu</code> produces pages with an annotation chunk containing the specified hyperlinks.</p>
<dt>*</p>
<dd> <code># B </code><i>count</i><code> (</code><i>string</i><code>) (#</code><i>pageno</i><code>)</code><br />
 This constructs provides outline information for the document. An outline entry entitled <i>string</i> is associated with page <i>pageno</i>. Integer <i>count </i> indicates how many of the following outline entries must be attached to the current entry as subentries. When such comments are present in the first page <code>csepdjvu</code> produces an navigation chunk with the specified outline. </p>
</dl>
<h2>CREDITS</h2>
<p> This program was initially written by L&eacute;on Bottou &lt;leonb [at] users.sourceforge.net&gt; and was improved by Bill Riemers &lt;docbill [at] sourceforge.net&gt; and many others. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5), <code><a href="/docs/linux/man/1-c44/">c44</a></code>(1) </p>
<h2>Index</h2>
