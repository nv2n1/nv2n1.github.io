---

title: "pnmtojbig(1)"
name: "pnmtojbig"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmtojbig/"
description: "pnmtojbig – PNM to JBIG file converter"
---

<p> <code>pnmtojbig</code> </p>
<p> [<i>options</i>] [<i>input-file</i> [<i>output-file</i>]] </p>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pnmtojbig</code> reads a PBM or PGM image, compresses it, and outputs the image as a JBIG bi-level image entity (BIE) file. </p>
<p> JBIG is a highly effective lossless compression algorithm for bi-level images (one bit per pixel), which is particularly suitable for scanned document pages. </p>
<p> A JBIG encoded image can be stored in several resolutions (progressive mode). These resolution layers can be stored all in one single BIE or they can be stored in several separate BIE files. All resolution layers except the lowest one are stored merely as differences to the next lower resolution layer, because this requires less space than encoding the full image completely every time. Each resolution layer has twice the number of horizontal and vertical pixels than the next lower layer. JBIG files can also store several bits per pixel as separate bitmap planes, and <code>pnmtojbig</code> can read a PGM file and transform it into a multi-bitplane BIE. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q</code></dt>
<dd> Encode the image in one single resolution layer (sequential mode). This is usually the most efficient compression method. By default, the number of resolution layers is chosen automatically such that the lowest layer image is not larger than 640 &#215; 480 pixels. </dd>
<dt><code>-x</code> <i>number</i></dt>
<dd> Specify the maximal horizontal size of the lowest resolution layer. The default is 640 pixels. </dd>
<dt><code>-y</code> <i>number</i></dt>
<dd> Specify the maximal vertical size of the lowest resolution layer. The default is 480 pixels. </dd>
<dt><code>-l</code> <i>number</i></dt>
<dd> Select the lowest resolution layer that will be written to the BIE. It is possible to store the various resolution layers of a JBIG image in progressive mode into different BIEs. Options <code>-l</code> and <code>-h</code> allow you to select the resolution-layer interval that will appear in the created BIE. The lowest resolution layer has number 0 and this is also the default value. By default, <code>pnmtojbig</code> writes all layers. </dd>
<dt><code>-h</code> <i>number</i></dt>
<dd> Select the highest resolution layer that will be written to the BIE. By default, <code>pnmtojbig</code> writes all layers. See also option <code>-l</code>. </dd>
<dt><code>-b</code></dt>
<dd> Use binary values instead of Gray code words in order to encode pixel values in multiple bitplanes. This option has only an effect if the input is a PGM file and if more than one bitplane is produced. Note that the decoder has to make the same selection but cannot determine from the BIE, whether Gray or binary code words were used by the encoder. </dd>
<dt><code>-d</code> <i>number</i></dt>
<dd> Specify the total number of differential resolution layers into which the input image will be split in addition to the lowest layer. Each additional layer reduces the size of layer 0 by 50 %. This option overrides options <code>-x</code> and <code>-y</code>, which are usually a more comfortable way of selecting the number of resolution layers. </dd>
<dt><code>-s</code> <i>number</i></dt>
<dd> The JBIG algorithm splits each image into a number of horizontal stripes. This option specifies that each stripe shall have <i>number</i> lines in layer 0. The default value is selected so that approximately 35 stripes will be used for the whole image. </dd>
<dt><code>-m</code> <i>number</i></dt>
<dd> Select the maximum horizontal offset of the adaptive template pixel. The JBIG encoder uses a number of neighbour pixels in order to get statistical a priori knowledge of the probability, whether the next pixel will be black or white. One single pixel out of this template of context neighbor pixels can be moved around. Especially for dithered images it can be a significant advantage to have one neighbor pixel which has a distance large enough to cover the period of a dither function. By default, the adaptive template pixel can be moved up to 8 pixels away. This encoder supports up to 23 pixels, however as decoders are only required to support at least a distance of 16 pixels by the standard, no higher value than 16 for <i>number</i> is recommended in order to maintain interoperability with other JBIG implementations. The maximal vertical offset of the adaptive template pixel is always zero. </dd>
<dt><code>-t</code> <i>number</i></dt>
<dd> Encode only the specified number of most significant bit planes. This option allows to reduce the depth of an input PGM file if not all bits per pixel are needed in the output. </dd>
<dt><code>-o</code> <i>number</i></dt>
<dd> JBIG separates an image into several horizontal stripes, resolution layers and planes, were each plane contains one bit per pixel. One single stripe in one plane and layer is encoded as a data unit called stripe data entity (SDE) inside the BIE. There are 12 different possible orders in which the SDEs can be stored inside the BIE and <i>number</i> selects which one shall be used. The order of the SDEs is only relevant for applications that want to decode a JBIG file which has not yet completely arrived from e.g. a slow network connection. For instance some applications prefer that the outermost of the three loops (stripes, layers, planes) is over all layers so that all data of the lowest resolution layer is transmitted first. </dd>
<p> The following values for <i>number</i> select these loop arrangements for writing the SDEs (outermost loop first): </p>
<dt>0</dt>
<dd> planes, layers, stripes </dd>
<dt>2</dt>
<dd> layers, planes, stripes </dd>
<dt>3</dt>
<dd> layers, stripes, planes </dd>
<dt>4</dt>
<dd> stripes, planes, layers </dd>
<dt>5</dt>
<dd> planes, stripes, layers </dd>
<dt>6</dt>
<dd> stripes, layers, planes </dd>
<p> All loops count starting with zero, however by adding 8 to the above order code, the layer loop can be reversed so that it counts down to zero and then higher resolution layers will be stored before lower layers. Default order is 3 which writes at first all planes of the first stripe and then completes layer 0 before continuing with the next layer and so on. </p>
<dt><code>-p</code> <i>number</i></dt>
<dd> This option allows you to activate or deactivate various optional algorithms defined in the JBIG standard. Just add the numbers of the following options which you want to activate in order to get the <i>number</i> value: </dd>
<dt>4</dt>
<dd> deterministic prediction (DPON) </dd>
<dt>8</dt>
<dd> typical prediction (TPBON) </dd>
<dt>16</dt>
<dd> diff. layer typical prediction (TPDON) </dd>
<dt>64</dt>
<dd> layer 0 two-line template (LRLTWO) </dd>
<p> Except for special applications (like communication with JBIG subset implementations) and for debugging purposes you will normally not want to change anything here. The default is 28, which provides the best compression result. </p>
<dt><code>-c</code></dt>
<dd> The adaptive template pixel movement is determined as suggested in annex C of the standard. By default the template change takes place directly in the next line which is most effective. However a few conformance test examples in the standard require the adaptive template change to be delayed until the first line of the next stripe. This option selects this special behavior, which is normally not required except in order to pass some conformance test suite. </dd>
<dt><code>-v</code></dt>
<dd> After <code>pnmtojbig</code> creates the BIE, it lists a few technical details of the created file (verbose mode). </dd>
</dl>
<h2>FORMATS</h2>
<p> Most of the format <code>pnmtojbig</code> creates is defined by the JBIG standard. </p>
<p> The standard, however, does not specify which values in the BIE mean white and which mean black. It contains a recommendation that for a single plane image zero mean background and one mean foreground, but the Netpbm formats have no concept of foreground and background. And the standard says nothing about values for multiple plane BIEs. </p>
<p> <code>pnmtojbig</code> follows Markus Kuhn&#8217;s implementation of the standard in the <code>pbmtojbg</code> program that comes with his JBIG library: If the BIE is a single plane BIE, zero means white and one means black. If it is a multiple plane BIE, zero means black and the maximal value is white. </p>
<h2>STANDARDS</h2>
<p> This program implements the JBIG image coding algorithm as specified in ISO/IEC 11544:1993 and ITU-T T.82(1993). </p>
<h2>AUTHOR</h2>
<p> <code>pnmtojbig</code> is based on the JBIG library by Markus Kuhn, part of his <code>JBIG-KIT</code> package. The <code>pbmtojbg</code> program is part of the <i>JBIG-KIT</i> package. The most recent version of that library and tools set is freely available on the Internet from anonymous ftp server <a href="ftp://ftp.informatik.uni-erlangen.de">ftp.informatik.uni-erlangen.de</a> in directory pub/doc/ISO/JBIG/. </p>
<p> <code>pnmtojbig</code> is part of the Netpbm package of graphics tools. </p>
<h2>SEE ALSO</h2>
<p> <code>pnm</code>(1) , <code><a href="/docs/linux/man/1-jbigtopnm/">jbigtopnm</a></code>(1) </p>
<h2>LICENSE</h2>
<p> If you use <code>pnmtojbig</code>, you are using various patents, particularly on its arithmetic encoding method, and in all probability you do not have a license from the patent owners to do so. </p>
