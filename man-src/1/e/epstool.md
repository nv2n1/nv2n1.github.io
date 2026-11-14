---
title: "epstool(1)"
name: "epstool"
section: "1"
letter: "e"
url: "/docs/linux/man/1-epstool/"
description: "epstool – Edit preview images and fix bounding boxes in EPS files."
---

<h2>NAME</h2>
<p> epstool &#8211; Edit preview images and fix bounding boxes in EPS files. </p>
<h2>SYNOPSIS</h2>
<p> <code>epstool</code> <i>command</i> [ <i>options</i> ] <i>inputfile outputfile</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>epstool</code> is a utility to create or extract preview images in EPS files. It can also calculate optimal bounding boxes. </p>
<h3>EPS (Encapsulated PostScript Format)</h3>
<p> EPS is a specialised form of a PostScript file that complies with the Document Structuring Conventions (DSC) and is intended to be embedded inside another PostScript file. An EPS file must contain a special first line that identifies it as an EPS file (e.g. <code>%!PS-Adobe-3.0 EPSF-3.0</code>) and it must contain a <code>%%BoundingBox:</code> line. The EPS file only draws within the rectangle defined by the bounding box. The PostScript code must avoid using PostScript operators that would interfere with the embedding. These include operators with global effects such as changing the page size and changing the half tone screen. </p>
<h3>PREVIEWS</h3>
<p> EPS files may contain a preview to be used by programs that can&#8217;t interpret the PostScript code. There are three ways to add a preview to an EPS file. </p>
<dl>
<dt>Interchange</p>
<dd> This preview is included within PostScript comments in a section marked %%BeginPreview: / %%EndPreview. The actual image data is stored in hexadecimal format. This format is most commonly used on Unix. </p>
<dt>DOS EPS</p>
<dd> The preview is a TIFF or Windows Metafile. A DOS EPS file has a 30 byte binary header which gives offsets and lengths for the PostScript, TIFF and Windows Metafile sections. You can&#8217;t send a DOS EPS file directly to a printer &#8211; you have to remove the binary header and preview first. This format is most commonly used on MS-Windows. </p>
<dt>PICT</p>
<dd> The preview is in PICT format stored in the resource fork of the file. This format is most commonly used on the Macinstosh. Epstool provides limited support for this format. </p>
</dl>
<h2>COMMANDS (one only):</h2>
<dl>
<dt><code>-t4, &#8211;add-tiff4-preview</code></p>
<dd> Add a TIFF 4 preview. The preview is monochrome and is intended for use with old programs that won&#8217;t read TIFF6, such as Word Perfect 5.1 for DOS. </p>
<dt><code>-t6u, &#8211;add-tiff6u-preview</code></p>
<dd> Add a TIFF 6 uncompressed preview. See <code>&#8211;add-tiff6p-preview</code> for how to add a greyscale or monochrome preview. </p>
<dt><code>-t6p, &#8211;add-tiff6p-preview</code></p>
<dd> Add a TIFF 6 preview compressed with packbits (simple run length encoding). The preview will normally be full colour, but you can make it greyscale by adding the option <code>&#8211;device bmpgray</code> or <code>&#8211;device pgmraw,</code> or monochrome using <code>&#8211;device bmpmono</code> or <code>&#8211;device pbmraw</code>. </p>
<dt><code>-tg, &#8211;add-tiff-preview</code></p>
<dd> Add a TIFF preview using ghostscript to generate the TIFF file. You must specify a suitable TIFF device using <code>&#8211;device</code>. If you want a compressed monochrome image, you might use <code>&#8211;device tiffg3</code>. </p>
<dt><code>-i, &#8211;add-interchange-preview</code></p>
<dd> Add a monochrome interchange preview. </p>
<dt><code>-w, &#8211;add-metafile-preview</code></p>
<dd> Add a Windows Metafile (WMF) preview. The metafile will contain a bitmap, not vector information. The preview will normally be full colour. See <code>&#8211;add-tiff6p-preview</code> for how to add a greyscale or monochrome preview. </p>
<dt><code>&#8211;add-pict-preview</code></p>
<dd> Add a Mac PICT preview. EPSF files with PICT previews can generally be used only on Mac computers. The preview will be full colour. The AppleSingle and MacBinary formats will contain the EPSF and the preview. The AppleDouble or Resource format will contain the preview only and needs to accompany the original EPSF file. To specify the file format use <code>&#8211;mac-single</code>, <code>&#8211;mac-double</code>, <code>&#8211;mac-binary</code> or <code>&#8211;mac-rsrc</code>. </p>
<dt><code>&#8211;add-user-preview </code><i> filename</i></p>
<dd> Add a user supplied image as a preview. The image can be a Windows bitmap, a PBMPLUS file, a TIFF image or a Windows Metafile. Window bitmaps and PBMPLUS files will be converted to TIFF6 compressed with packbits. TIFF and Windows Metafile images will be added unchanged. </p>
<dt><code>&#8211;bitmap</code></p>
<dd> Create a bitmap of the area within the EPS bounding box. The bitmap type must be specified with <code>&#8211;device</code>. If processing a DCS 2.0 file, the separation can be specified with <code>&#8211;page-number</code>. </p>
<dt><code>&#8211;copy</code></p>
<dd> Copy the EPS file. This is generally used with the <code>&#8211;bbox</code> option to update the bounding box. </p>
<dt><code>&#8211;dcs2-multi</code></p>
<dd> Convert DCS 2.0 separations to multiple files. See DCS 2.0. If the output name is out.eps, then the separations would be named out.eps.Cyan etc. </p>
<dt><code>&#8211;dcs2-single</code></p>
<dd> Convert DCS 2.0 separations to a single file. See DCS 2.0. </p>
<dt><code>&#8211;dcs2-report</code></p>
<dd> Write the separation names, lengths and CMYK values to standard output. This can be used to identify if a DCS 2.0 file is missing the composite page or preview. </p>
<dt><code>&#8211;dump</code></p>
<dd> Display some information about the file type and DSC comments. </p>
<dt><code>-p, &#8211;extract-postscript</code></p>
<dd> Extract the PostScript section from a DOS EPS file. </p>
<dt><code>-v, &#8211;extract-preview</code></p>
<dd> Extract the preview section from a DOS EPS file. </p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a summary of the epstool commands and options. </p>
<dt><code>&#8211;test-eps</code></p>
<dd> Partially test if a file complies with the EPSF specification. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b, &#8211;bbox</code></p>
<dd> Calculate the bounding box using the ghostscript bbox device and update in the EPS file. </p>
<dt><code>&#8211;combine-separations </code><i> filename</i></p>
<dd> Combine the separations of the input DCS 2.0 file with those of this file. It is an error if the bounding boxes do not match or they contain separations with the same name. This option must be used with <code>&#8211;dcs2-multi</code> or <code>&#8211;dcs2-single</code>. The composite page may later need to be updated with <code>&#8211;replace-composite</code>. </p>
<dt><code>&#8211;combine-tolerance </code><i> pts</i></p>
<dd> When using <code>&#8211;combine-separations</code>, allow the bounding boxes to vary by up to <i>pts</i> points. The default is 0 so the bounding boxes must match exactly. </p>
<dt><code>&#8211;custom-colours </code><i> filename</i></p>
<dd> When using <code>&#8211;replace-composite</code> on a DCS 2.0 file, use the colours specified in this file in preference to those specified in the composite page. </p>
<dt><code>-d, &#8211;debug</code></p>
<dd> Be more verbose about progress. Do not remove temporary files. </p>
<dt><code>&#8211;device</code><i> name</i></p>
<dd> Specify a ghostscript device to be used when creating the preview or bitmap. For <code>&#8211;add-tiff-preview</code> this must be one of the ghostscript tiff devices (e.g. tiffg3, tiff24nc). For any other preview, it must be one of the bmp or pbmplus devices (e.g. bmpgray, bmp16m, pgmraw, ppmraw). For bitmap output (<code>&#8211;bitmap</code>) it can be any ghostscript bitmap device. </p>
<dt><code>&#8211;doseps-reverse</code></p>
<dd> When writing a DOS EPS file (TIFF or WMF preview), the default is to write the PostScript before the preview. Using <code>&#8211;doseps-reverse</code> puts the preview before the PostScript section, which is required by some buggy programs. Either order is correct. </p>
<dt><code>&#8211;dpi</code><i> resolution</i></p>
<dd> Set the resolution of the preview or bitmap. The default is 72 dpi. </p>
<dt><code>&#8211;dpi-render</code><i> resolution</i></p>
<dd> Render at a higher resolution set by <code>&#8211;dpi-render</code> , then downsample to the resolution set by <code>&#8211;dpi</code>. This works when adding a preview image or using <code>&#8211;replace-composite</code> , but not when using <code>&#8211;bitmap.</code> This improves the preview quality when the original contains a pre-rendered image and <code>&#8211;dpi-render</code> is set to match the original target printer. </p>
<dt><code>&#8211;ignore-information</code></p>
<dd> Ignore information messages from the DSC parser. Use at your own risk. These messages usually indicate that something is wrong with an EPS file, but that most EPS handlers probably won&#8217;t care. An example is a line with more than 255 characters. </p>
<dt><code>&#8211;ignore-warnings</code></p>
<dd> Ignore warnings from the DSC parser. Use at your own risk. These messages are usually about faults in the DSC comments that are recoverable by <code>epstool</code>, but may confuse other EPS handlers. An example is a bounding box that incorrectly uses floating point numbers instead of integer. </p>
<dt><code>&#8211;ignore-errors</code></p>
<dd> Ignore warnings from the DSC parser. Use at your own risk. You really should fix the EPS file first. </p>
<dt><code>&#8211;gs command</code></p>
<dd> Specify the name the ghostscript program. On Unix the default is gs. On Windows, <code>epstool</code> will check the registry for installed versions of ghostscript and use the latest, otherwise it will use gswin32c.exe. </p>
<dt><code>&#8211;gs-args</code><i> arguments</i></p>
<dd> Specify additional Ghostscript arguments. This might be used to select anti-aliasing with &quot;-dTextAlphaBits=4 -dGraphicsAlphaBits=4&quot; </p>
<dt><code>&#8211;output</code><i> filename</i></p>
<dd> Specify the output file (instead of using the second file parameter). Using the filename <code>&#8211;</code> causes epstool to write to standard output, which requires the use of <code>&#8211;quiet</code>. </p>
<dt><code>&#8211;mac-binary</code></p>
<dd> When adding a PICT preview, use the MacBinary I format. for the Mac </p>
<dt><code>&#8211;mac-double</code></p>
<dd> When adding a PICT preview, use the AppleDouble format for the Mac. </p>
<dt><code>&#8211;mac-rsrc</code></p>
<dd> When adding a PICT preview, use the Resource format for the Mac. </p>
<dt><code>&#8211;mac-single</code></p>
<dd> When adding a PICT preview, use the AppleSingle format for the Mac. </p>
<dt><code>&#8211;missing-separations</code></p>
<dd> When writing a DCS 2.0 file, epstool will normally fail if a separation is missing. When this option is used, it will remove references to missing separations when writing the file. </p>
<dt><code>&#8211;page-number</code><i> page</i></p>
<dd> When creating a bitmap with <code>&#8211;device</code> from a DCS 2.0 file, <i>page</i> specifies the separation to be used. Page 1 is the composite and page 2 is the first separation. Use <code>&#8211;dcs2-report</code> to get the list of separations. </p>
<dt><code>&#8211;quiet</code></p>
<dd> Try to run without writing to standard output. </p>
<dt><code>&#8211;rename-separation</code><i> oldname newname</i></p>
<dd> When copying a DCS 2.0 file with <code>&#8211;dcs2-multi</code> or <code>&#8211;dcs2-single</code>, rename separation with <i>oldname</i> to <i>newname</i>. This option implies <code>&#8211;missing-separations</code>. It is assumed that the new name is just an alias for the same colour and that the CMYK or RGB values for the separation are not changed. This option may be used multiple times. This must be used if the input file incorrectly has two separations of the same name. </p>
<dt><code>&#8211;replace-composite</code></p>
<dd> Some DCS 2.0 files do not have an image in the composite page. This option replaces the composite page with a CMYK image derived from the separations. This option must be used with <code>&#8211;dcs2-multi</code> or <code>&#8211;dcs2-single</code>. See also the options <code>&#8211;dpi</code> and <code>&#8211;custom-colours</code>. </p>
</dl>
<h2>MACINTOSH</h2>
<p> The Macintosh does not use a flat file system. Each file can have a data fork and a resource fork. EPSF files have the PostScript in the data fork, and optionally have a preview in the resource fork as a PICT image. In addition, file type is obtained from the finder info rather than a file extension. File types use a four character code such as &quot;EPSF&quot; or &quot;PICT&quot;. When Macintosh files are copied to a foreign file system, the resource fork may be left behind. Alternatives to retain the resource fork are to package the finder data, data fork and resource fork in a single MacBinary or AppleSingle file, or to put the data fork in a flat file and the finder info and resource fork in an AppleDouble file. The Mac OSX finder will handle AppleDouble files automatically when copying files to and from a foreign file system. When copying <i>test.eps</i> to a foreign file system, the data fork would be written as <i>test.eps</i> and the finder info and resource fork to the AppleDouble file <i>._test.eps</i> or <i>.AppleDouble/test.eps</i>. </p>
<p> Epstool can read MacBinary and AppleSingle files. It can write MacBinary I, AppleSingle, AppleDouble or Resource files. Files written by epstool will have type <i>EPSF</i> and creator <i>MSWD</i>. When adding a preview to <i>test.eps</i>, it is suggested that you create the MacBinary file <i>test.eps.bin</i>. On a Macintosh computer you then need to extract it with StuffIt Expander. Another alternative is to write the AppleDouble file to <i>._test.eps</i> then copy <code>both files</code> to a file system accessible to a Mac computer. </p>
<p> If the output file name starts with <i>.</i> then AppleDouble will be assumed, otherwise if it ends with <i>.as</i> then AppleSingle will be assumed, otherwise if it ends with <i>.rsrc</i> or <i>/rsrc</i> then Resource will be assumed, otherwise MacBinary will be assumed. When writing a MacBinary file, it is recommended that you end the filename in <i>.bin</i>. To force the file type, use <code>&#8211;mac-single</code>, <code>&#8211;mac-double</code>, <code>&#8211;mac-binary</code> or <code>&#8211;mac-rsrc</code>. </p>
<p> On Mac OS X you can access a file&#8217;s resource fork from command line tools by appending <i>/rsrc</i> to the original file name. The easiest way to add a preview to the file <i>test.eps</i> on Mac OS X is to let epstool write in <code>&#8211;mac-rsrc</code> format to <i>test.eps/rsrc</i> (see <code>Examples</code>). </p>
<h2>DESKTOP COLOR SEPARATIONS (DCS 2.0)</h2>
<p> The Desktop Color Separation (DCS) image file format contains a low resolution preview, a main file with the full resolution composite image, and colour separations with full resolution separated plates. The separations will typically contain Cyan, Magenta, Yellow, Black and possibly spot colours. There are two versions of DCS 2.0. </p>
<dl>
<dt>Multiple File</p>
<dd> The main file contains <i>%%PlateFile: (name) EPS Local filename</i> comments which give the filenames of the separation plates. The main file may contain a low resolution DOS EPS preview. The separation files do not contain previews. </p>
<dt>Single File</p>
<dd> This is an abuse of the EPS specification. The single file contains the main file and the separations concatenated together, which makes the DSC comments incorrect. The main file specifies the byte offsets to the separations using <i>%%PlateFile: (name) EPS #offset size</i>. The single file may then be placed inside a DOS EPS file with a low resolution preview. By default, epstool writes single file DCS 2.0. </p>
</dl>
<p> Epstool can add previews to single and multiple file DCS 2.0. It can split single file DCS 2.0 into multiple files and vice versa. This allows a single file DCS 2.0 to be split, the composite image replaced, a new preview created, and then be recombined into a single file. </p>
<p> Some DCS 2.0 files do not have an image in the composite page. To determine if the composite page does not contain an image, use <code>&#8211;dcs2-report</code> and look to see if the composite section is very short. Using <code>&#8211;dcs2-single &#8211;replace-composite</code> replaces the composite page with the headers of the original composite page and a body containing a CMYK image derived from the separations. Set the resolution of the CMYK image using <code>&#8211;dpi</code>. </p>
<p> When replacing the composite page with a CMYK image using <code>&#8211;replace-composite</code>, the <code>&#8211;custom-colours</code> option is useful for dealing with DCS 2.0 files that have incorrect CMYK colours, for example specifying that the varnish layer is grey. Each line of the CMYK colours file is formatted like a DSC <i>%%CMYKCustomColor:</i> or <i>%%RGBCustomColor:</i> line, as shown in the example below. </p>
<p> %%CMYKCustomColor: 0.00 0.00 0.00 0.00 Varnish </p>
<p> %%CMYKCustomColor: 1.00 0.68 0.00 0.12 (Dark Blue) </p>
<p> %%RGBCustomColor: 0.5 0.0 0.0 (Dark Red) </p>
<p> DCS2 files should not have two separations with the same name. Epstool will not allow a DCS2 output file to have duplicate separation names. Use <code>&#8211;rename-separation</code> to resolve this. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>Add colour preview (24bit/pixel) to EPS file</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>epstool -t6p tiger.eps output.eps </p>
<dt>Add TIFF (G3 Fax) preview to tiger.eps.</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>epstool &#8211;add-tiff-preview &#8211;device tiffg3 tiger.eps output.eps</dl>
<p> Any GS TIFF device can be used, e.g. tiffg4, tiffpack </p>
<dl>
<dt>Extract TIFF preview from tiger.eps</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>epstool -v tiger.eps tiger.tif </p>
<dt>Fix incorrect %%BoundingBox then add TIFF4 preview.</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>epstool &#8211;bbox -t4 golfer.eps output.eps </p>
<dt>Adjust the BoundingBox of an existing EPS file, but don&#8217;t add a preview:</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>epstool &#8211;copy &#8211;bbox input.eps output.eps </p>
<dt>Add user supplied Windows Metafile to EPS file.</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>epstool &#8211;add-user-preview logo.wmf logo.eps output.eps</dl>
<p> Typically used when an application can export EPS and WMF separately but can&#8217;t export EPS with WMF preview. </p>
<dl>
<dt>Add a PICT preview and write an AppleDouble file.</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>epstool &#8211;add-pict-preview &#8211;mac-double tiger.eps ._tiger.eps</dl>
<p> To be used by a Mac, both <i>tiger.eps</i> and <i>._tiger.eps</i> need to be on a foreign file system accessible to the Mac. </p>
<dl>
<dt>Add a PICT preview, overwriting the existing resources.</p>
<dd>
&nbsp;<wbr>epstool &#8211;add-pict-preview &#8211;mac-rsrc tiger.eps tiger.eps/rsrc</dl>
<p> On Mac OS X you can access a file&#8217;s resource fork from command line tools by appending &quot;/rsrc&quot; to the file&#8217;s original name. </p>
<h2>NOTES</h2>
<p> When adding a WMF preview to an EPS file using <code>-add-user-preview filename</code>, the placeable metafile header is removed from the metafile as it is put into the EPS file. When extracting a WMF preview from an EPS file, a placeable metafile header is created from the EPS BoundingBox information. This placeable metafile header assumes that the WMF has its origin at (0,0), which might not be correct. </p>
<p> When epstool is creating a TIFF or WMF preview, it will convert palette colour images into 24-bit/pixel. </p>
<p> The environment variable TEMP should point to a writeable directory for temporary files. If not defined, /tmp will be used for Unix and the current directory will be used for other platforms. </p>
<h2>AUTHOR</h2>
<p> <code>epstool</code> was written by Russell Lang &lt;gsview [at] ghostgum.com.au&gt; </p>
<p> This man page was contributed by Martin Pitt &lt;martin [at] piware.de&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
