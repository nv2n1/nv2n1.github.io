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
</dt><dd> Automatically find stars in a FITS or IRAF image, match them to HST Guide USNO A, B, UCAC or UJ Stars, or others, compute the relation between sky coordinates and image coordinates, and write in in the image header. [after U of Iowa SETWCS]
</dd><dt>delwcs
</dt><dd> Delete the WCS keywords from an image. If both EPOCH and EQUINOX are present, EQUINOX is also deleted.</dd></dl>

<h2>Using an Image World Coordinate System</h2>

<dl>
<dt>imcat
</dt><dd> List catalog sources which should be found in the area of the sky covered by a specific image.
</dd><dt>imsize
</dt><dd> Print center and size of image using WCS keywords in header
</dd><dt>imstar
</dt><dd> Find and list the n brightest stars in an IRAF or FITS image, with their sky coordinates if there is WCS information in the image header.
</dd><dt>sky2xy
</dt><dd> Print image pixel coordinates for given sky coordinates on the command line or in a list file.
</dd><dt>xy2sky
</dt><dd> Print sky coordinates for given image pixel coordinates on the command line or in a list file.</dd></dl>

<h2>Catalog Utility Programs</h2>

<dl>
<dt>scat
</dt><dd> Search the HST GSC, USNO-A2.0, or other catalog given a region on the sky.
</dd><dt>
</dt><dt>skycoor
</dt><dd>
</dd><dd> Convert between J2000, B1950, and Galactic coordinates from the command line or a file.</dd></dl>

<h2>Image Utility Programs</h2>

<dl>
<dt>addpix
</dt><dd> Add a constant value(s) to specified pixel(s)
</dd><dt>edhead
</dt><dd> Edit the header of a FITS file or the user parameters of an IRAF image file using a the text editor specified by the EDITOR environment variable.
</dd><dt>gethead
</dt><dd> Return values for keyword(s) specified after filename.
</dd><dt>getpix
</dt><dd> Return value(s) of specified pixel(s)
</dd><dt>i2f
</dt><dd> Read two-dimensional IRAF image file and write FITS image file
</dd><dt>imhead
</dt><dd> Print FITS or IRAF header
</dd><dt>imrot
</dt><dd> Rotate and/or reflect FITS or IRAF image files
</dd><dt>setpix
</dt><dd> Set specified pixel(s) to specified value(s)
</dd><dt>sethead
</dt><dd> Set header parameters in FITS or IRAF images.
</dd><dt>subpix
</dt><dd> Subtract a constant value(s) from specified pixel(s) 
</dd></dl>

<h2>Author</h2>

 Jessica Mink, SAO (jmink [at] cfa.harvard.edu)
