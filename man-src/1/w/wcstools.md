---
title: "wcstools(1)"
name: "wcstools"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wcstools/"
---

<h2>Name</h2>

 wcstools - Programs to access image world coordinate systems and catalogs

<h2>Setting an Image World Coordinate System</h2>

<dl>
<dt>imwcs
<dd> Automatically find stars in a FITS or IRAF image, match them to HST Guide USNO A, B, UCAC or UJ Stars, or others, compute the relation between sky coordinates and image coordinates, and write in in the image header. [after U of Iowa SETWCS]
<dt>delwcs
<dd> Delete the WCS keywords from an image. If both EPOCH and EQUINOX are present, EQUINOX is also deleted.</dl>

<h2>Using an Image World Coordinate System</h2>

<dl>
<dt>imcat
<dd> List catalog sources which should be found in the area of the sky covered by a specific image.
<dt>imsize
<dd> Print center and size of image using WCS keywords in header
<dt>imstar
<dd> Find and list the n brightest stars in an IRAF or FITS image, with their sky coordinates if there is WCS information in the image header.
<dt>sky2xy
<dd> Print image pixel coordinates for given sky coordinates on the command line or in a list file.
<dt>xy2sky
<dd> Print sky coordinates for given image pixel coordinates on the command line or in a list file.</dl>

<h2>Catalog Utility Programs</h2>

<dl>
<dt>scat
<dd> Search the HST GSC, USNO-A2.0, or other catalog given a region on the sky.
<dt>
<dt>skycoor
<dd>
<dd> Convert between J2000, B1950, and Galactic coordinates from the command line or a file.</dl>

<h2>Image Utility Programs</h2>

<dl>
<dt>addpix
<dd> Add a constant value(s) to specified pixel(s)
<dt>edhead
<dd> Edit the header of a FITS file or the user parameters of an IRAF image file using a the text editor specified by the EDITOR environment variable.
<dt>gethead
<dd> Return values for keyword(s) specified after filename.
<dt>getpix
<dd> Return value(s) of specified pixel(s)
<dt>i2f
<dd> Read two-dimensional IRAF image file and write FITS image file
<dt>imhead
<dd> Print FITS or IRAF header
<dt>imrot
<dd> Rotate and/or reflect FITS or IRAF image files
<dt>setpix
<dd> Set specified pixel(s) to specified value(s)
<dt>sethead
<dd> Set header parameters in FITS or IRAF images.
<dt>subpix
<dd> Subtract a constant value(s) from specified pixel(s) 

</dl>

<h2>Author</h2>

 Jessica Mink, SAO (jmink [at] cfa.harvard.edu) 

<h2>Index</h2>


