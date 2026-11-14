---
title: "gdaladdo(1)"
name: "gdaladdo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdaladdo/"
description: "gdaladdo – gdaladdo builds or rebuilds overview images"
---

<h2 class="name">NAME</h2>
<p> gdaladdo &#8211; gdaladdo builds or rebuilds overview images </p>
<h2>SYNOPSIS</h2>
<pre><code>
gdaladdo[-r{nearest, average, gauss, cubic, average_mp, average_magphase, mode}]
        [-b band]
        [-ro][-clean][--help - general] filename levels
</code></pre>
<h2>DESCRIPTION</h2>
<p> The gdaladdo utility can be used to build or rebuild overview images for most supported file formats with one of several downsampling algorithms. </p>
<dl>
<dt><code>-r</code> <i>{nearest (default),average,gauss,cubic,average_mp,average_magphase,mode}</i>:</p>
<dd> Select a resampling algorithm.</p>
<dt><code>-b</code> <i>band</i>:</p>
<dd> (available from GDAL 1.10) Select an input band <i>band</i> for overview generation. Band numbering starts from 1. Multiple <code>-b</code> switches may be used to select a set of input bands to generate overviews.</p>
<dt><code>-ro</code>:</p>
<dd> (available from GDAL 1.6.0) open the dataset in read-only mode, in order to generate external overview (for GeoTIFF especially).</p>
<dt><code>-clean</code>:</p>
<dd> (available from GDAL 1.7.0) remove all overviews.</p>
<dt><i>filename</i>:</p>
<dd> The file to build overviews for (or whose overviews must be removed).</p>
<dt><i>levels</i>:</p>
<dd> A list of integral overview levels to build. Ignored with -clean option.</dl>
<p> <i>Mode</i> (available from GDAL 1.6.0) selects the value which appears most often of all the sampled points. <i>average_mp</i> is unsuitable for use. <i>Average_magphase</i> averages complex data in mag/phase space. <i>Nearest</i> and <i>average</i> are applicable to normal image data. <i>Nearest</i> applies a nearest neighbour (simple sampling) resampler, while <i>average</i> computes the average of all non-NODATA contributing pixels. <i>Cubic</i> resampling (available from GDAL 1.7.0) applies a 4&#215;4 approximate cubic convolution kernel. <i>Gauss</i> resampling (available from GDAL 1.6.0) applies a Gaussian kernel before computing the overview, which can lead to better results than simple averaging in e.g case of sharp edges with high contrast or noisy patterns. The advised level values should be 2, 4, 8, &#8230; so that a 3&#215;3 resampling Gaussian kernel is selected. </p>
<p> gdaladdo will honour properly NODATA_VALUES tuples (special dataset metadata) so that only a given RGB triplet (in case of a RGB image) will be considered as the nodata value and not each value of the triplet independently per band. </p>
<p> Selecting a level value like <i>2</i> causes an overview level that is 1/2 the resolution (in each dimension) of the base layer to be computed. If the file has existing overview levels at a level selected, those levels will be recomputed and rewritten in place. </p>
<p> For internal GeoTIFF overviews (or external overviews in GeoTIFF format), note that -clean does not shrink the file. A later run of gdaladdo with overview levels will cause the file to be expanded, rather than reusing the space of the previously deleted overviews. If you just want to change the resampling method on a file that already has overviews computed, you don&#8217;t need to clean the existing overviews. </p>
<p> Some format drivers do not support overviews at all. Many format drivers store overviews in a secondary file with the extension .ovr that is actually in TIFF format. By default, the GeoTIFF driver stores overviews internally to the file operated on (if it is writeable), unless the -ro flag is specified. </p>
<p> Most drivers also support an alternate overview format using Erdas Imagine format. To trigger this use the USE_RRD=YES configuration option. This will place the overviews in an associated .aux file suitable for direct use with Imagine or ArcGIS as well as GDAL applications. (eg &#8211;config USE_RRD YES)</p>
<h2>External overviews in GeoTIFF format</h2>
<p> External overviews created in TIFF format may be compressed using the COMPRESS_OVERVIEW configuration option. All compression methods, supported by the GeoTIFF driver, are available here. (eg &#8211;config COMPRESS_OVERVIEW DEFLATE). The photometric interpretation can be set with &#8211;config PHOTOMETRIC_OVERVIEW {RGB,YCBCR,&#8230;}, and the interleaving with &#8211;config INTERLEAVE_OVERVIEW {PIXEL|BAND}. </p>
<p> For JPEG compressed external overviews, the JPEG quality can be set with &#8216;&#8211;config JPEG_QUALITY_OVERVIEW value&#8217; (GDAL 1.7.0 or later). </p>
<p> For LZW or DEFLATE compressed external overviews, the predictor value can be set with &#8216;&#8211;config PREDICTOR_OVERVIEW 1|2|3&#8217; (GDAL 1.8.0 or later). </p>
<p> To produce the smallest possible JPEG-In-TIFF overviews, you should use : </p>
<pre>
--config COMPRESS_OVERVIEW JPEG --config PHOTOMETRIC_OVERVIEW YCBCR --config INTERLEAVE_OVERVIEW PIXEL
</pre>
<p> Starting with GDAL 1.7.0, external overviews can be created in the BigTIFF format by using the BIGTIFF_OVERVIEW configuration option : &#8211;config BIGTIFF_OVERVIEW {IF_NEEDED|IF_SAFER|YES|NO}. The default value is IF_NEEDED. The behaviour of this option is exactly the same as the BIGTIFF creation option documented in the GeoTIFF driver documentation. </p>
<dl>
<dt>&bull;</p>
<dd> YES forces BigTIFF.</p>
<dt>&bull;</p>
<dd> NO forces classic TIFF.</p>
<dt>&bull;</p>
<dd> IF_NEEDED will only create a BigTIFF if it is clearly needed (uncompressed, and overviews larger than 4GB).</p>
<dt>&bull;</p>
<dd> IF_SAFER will create BigTIFF if the resulting file <i>might</i> exceed 4GB.</dl>
<p> See the documentation of the GeoTIFF driver for further explanations on all those options.</p>
<h2>EXAMPLE</h2>
<p> Create overviews, embedded in the supplied TIFF file: </p>
<pre>
gdaladdo -r average abc.tif 2 4 8 16
</pre>
<p> Create an external compressed GeoTIFF overview file from the ERDAS .IMG file: </p>
<pre>
gdaladdo -ro --config COMPRESS_OVERVIEW DEFLATE erdas.img 2 4 8 16
</pre>
<p> Create an external JPEG-compressed GeoTIFF overview file from a 3-band RGB dataset (if the dataset is a writeable GeoTIFF, you also need to add the -ro option to force the generation of external overview): </p>
<pre>
gdaladdo --config COMPRESS_OVERVIEW JPEG --config PHOTOMETRIC_OVERVIEW YCBCR
         --config INTERLEAVE_OVERVIEW PIXEL rgb_dataset.ext 2 4 8 16
</pre>
<p> Create an Erdas Imagine format overviews for the indicated JPEG file: </p>
<pre>
gdaladdo --config USE_RRD YES airphoto.jpg 3 9 27 81
</pre>
<h2>AUTHORS</h2>
<p> Frank Warmerdam warmerdam [at] pobox.com, Silke Reimer silke [at] intevation.de </p>
<h2>Index</h2>
