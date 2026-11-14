---
title: "gdcm2vtk(1)"
name: "gdcm2vtk"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdcm2vtk/"
description: "gdcm2vtk – .TH \"gdcm2vtk\" 1 \"Fri Oct 29 2010\" \"Version 2.0.16\" \"GDCM\""
---

<h2 class="name">NAME</h2>
<p> gdcm2vtk &#8211; .TH &quot;gdcm2vtk&quot; 1 &quot;Fri Oct 29 2010&quot; &quot;Version 2.0.16&quot; &quot;GDCM&quot; </p>
<h2 class="name">NAME</h2>
<p> gdcm2vtk &#8211; .SH &quot;SYNOPSIS&quot; </p>
<pre>
gdcm2vtk [options] file-in file-out
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>gdcm2vtk</code> takes as input any file supported by VTK (including DICOM file) and will generate as output a DICOM file.</p>
<h2>PARAMETERS</h2>
<pre>
file-in   input filename (DICOM or VTK supported)
file-out  DICOM output filename
</pre>
<h2>OPTIONS</h2>
<h3>OPTIONS</h3>
<pre><code>
--force - rescale force rescale.--force - spacing force spacing.--palette - color when supported generate a PALETTE COLOR file.--argb when supported generate a ARGB file.--compress when supported generate a compressed file.--use - vtkdicom Use vtkDICOMImageReader(instead of GDCM).--modality set Modality.- T-- study - uid Study UID.- S-- series - uid Series UID.--root - uid Root UID.
</code></pre>
<h3>compression options</h3>
<p>&#8211; J&#8211; jpeg Compress image in jpeg.- K&#8211; j2k Compress image in j2k.- L&#8211; jpegls Compress image in jpeg &#8211; ls.- R&#8211; rle Compress image in rle(lossless only).</p>
<h3>general options</h3>
<pre><code>
- h-- help
        print this help text and exit -
    v-- version
        print version information and exit -
    V-- verbose
        verbose
        mode(warning + error)
            .-
    W-- warning
    warning mode,
    print warning information
        - E-- error
        error mode,
    print error information
        - D-- debug
        debug mode,
    print debug information
</code></pre>
<h3>environment variable</h3>
<pre>
  GDCM_ROOT_UID Root UID
</pre>
<h2>DESCRIPTION</h2>
<p> Convert a file supported by VTK into DICOM. </p>
<p> Typical usage is: </p>
<pre>
$ gdcm2vtk inputfile output.dcm
</pre>
<p> It uses the internal factory mechanism of VTK to recognize a file (CanRead function). See VTK supported file here: </p>
<p> What image file formats can VTK read and write? <a rel="nofollow" href="http://www.vtk.org/Wiki/VTK_FAQ#What_image_file_formats_can_VTK_read_and_write.3F">http://www.vtk.org/Wiki/VTK_FAQ#What_image_file_formats_can_VTK_read_and_write.3F</a> </p>
<p> If your input file has 4 components, the 4th comp (alpha) will be removed from the output file as DICOM does not support alpha component anymore (see &#8211;argb option). </p>
<p> Special care was taken for the following file format: </p>
<pre>
   1. DICOM: Direction Cosines and vtkMedicalImageInformation are passed to the output
   2. BMP: The file can be saved with a Lookup Table (see --palette-color)
   3. GE Signa: vtkMedicalImageProperties is passed to the output
   4. MINC: Direction Cosines is passed to the output
   5. TIFF: vtkTIFFReader is currently in bad shape in VTK (different behavior in VTK 5.2 and CVS). Only use it, if you know what you are doing.
</pre>
<h3>CONVERT MetaImage (mhd, mha)</h3>
<pre>
$ gdcm2vtk inputfile output.mha
</pre>
<p> This command will convert the input DICOM file: inputfile into a MetaImage .mha file. Same goes for .mhd file.</p>
<h3>CONVERT MHA/MHD</h3>
<pre>
$ gdcm2vtk inputfile output.mha
</pre>
<p>&nbsp;<wbr>or&nbsp;<wbr> </p>
<pre>
$ gdcm2vtk inputfile output.mhd
</pre>
<p> This command will convert the input DICOM file: inputfile into a MetaImageData .mha/.mhd file.</p>
<h3>CONVERT VTI</h3>
<pre>
$ gdcm2vtk inputfile output.vti
</pre>
<p> This command will convert the input DICOM file: inputfile into a XML VTK ImageData .vti file.</p>
<h3>CONVERT VTK</h3>
<pre>
$ gdcm2vtk inputfile output.vtk
</pre>
<p> This command will convert the input DICOM file: inputfile into an old VTK Structured PointSets .vtk file.</p>
<h2>CONVERT DICOM</h2>
<pre>
$ gdcm2vtk input.dcm output.dcm
</pre>
<p> <code>vtkGDCMImageReader</code> will be used to read in a DICOM file, not the default vtkDICOMImageReader. </p>
<p> IMPORTANT NOTE: The internal VTK structured will be filled from the input DICOM, and then pass to the output DICOM writer. Some information might be lost during the conversion DICOM to VTK to DICOM. This option is mostly used to test the vtkGDCMImageReader/vtkGDCMImageWriter combination. </p>
<p> IMPORTANT NOTE: When converting from a lossy format such as JPEG, the information of lossiness is important. The output DICOM will contains the required Lossy Image Compression attribute that indicates that image was lossy-compressed somewhere along the pipeline. See also gdcmimg (better handling of JPEG in general). </p>
<p> IMPORTANT NOTE: When using &#8211;use-vtkdicom the output DICOM file will always be written as MR Image Storage as this information is not available from the reader itself. This allow setting the Image Orientation (Patient) properly.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdcmdump/">gdcmdump</a></code>(1), <code><a href="/docs/linux/man/1-gdcmviewer/">gdcmviewer</a></code>(1), <code><a href="/docs/linux/man/1-gdcmimg/">gdcmimg</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2006-2010 Mathieu Malaterre </p>
<h2>Index</h2>
