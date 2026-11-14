---
title: "dcm2pnm(1)"
name: "dcm2pnm"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcm2pnm/"
description: "dcm2pnm – Convert DICOM images to PGM/PPM, PNG, TIFF or BMP"
---

<h2 class="name">NAME</h2>
<p> dcm2pnm &#8211; Convert DICOM images to PGM/PPM, PNG, TIFF or BMP </p>
<h2>SYNOPSIS</h2>
<pre><code>
dcm2pnm[options] dcmfile - in[bitmap - out]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcm2pnm</code> utility reads a DICOM image, converts the pixel data according to the selected image processing options and writes back an image in the well-known PGM/PPM (portable gray map / portable pix map), PNG, TIFF or Windows BMP format. This utility only supports uncompressed and RLE compressed DICOM images. The command line tool <code>dcmj2pnm</code> also supports a number of JPEG compression schemes.</p>
<h2>PARAMETERS</h2>
<pre>
dcmfile-in  DICOM input filename to be converted
bitmap-out  output filename to be written (default: stdout)
</pre>
<h2>OPTIONS</h2>
<h3>general options</h3>
<p>&#8211; h&#8211; help<br />
        print this help text and exit&#8211; version<br />
            print version information and exit&#8211; arguments<br />
                print expanded command line arguments &#8211;<br />
    q&#8211; quiet<br />
        quiet mode,<br />
    print no warnings and errors &#8211; v&#8211; verbose<br />
                                       verbose mode,<br />
    print processing details &#8211; d&#8211; debug<br />
                                   debug mode,<br />
    print debug information &#8211; ll&#8211; log &#8211; level[l] evel:string<br />
                                                       constant(fatal, error, warn, info, debug, trace)<br />
          use level l for the logger<br />
  -lc   &#8211;log-config  [f]ilename: string<br />
          use config file f for the logger</p>
<h3>input options</h3>
<p>input file format : +f&#8211; read &#8211; file<br />
                                    read file format or<br />
    data set(default) + fo&#8211; read &#8211; file &#8211; only read file format only<br />
        &#8211; f&#8211; read &#8211; dataset read data set without file meta information input transfer syntax : -t = &#8211;read &#8211; xfer &#8211; auto use TS recognition(default) &#8211; td&#8211; read &#8211; xfer &#8211; detect ignore TS specified in the file meta header<br />
                                                                                                      &#8211; te&#8211; read &#8211; xfer &#8211; little read with explicit VR little endian TS<br />
                                                                                                      &#8211; tb&#8211; read &#8211; xfer &#8211; big read with explicit VR big endian TS<br />
                                                                                                      &#8211; ti&#8211; read &#8211; xfer &#8211; implicit read with implicit VR little endian TS</p>
<h3>image processing options</h3>
<p>frame selection:<br />
  +F    &#8211;frame  [n]umber: integer<br />
          select specified frame (default: 1)<br />
  +Fr   &#8211;frame-range  [n]umber [c]ount: integer<br />
          select c frames beginning with frame n<br />
  +Fa   &#8211;all-frames<br />
          select all frames<br />
rotation:<br />
  +Rl   &#8211;rotate-left<br />
          rotate image left (-90 degrees)<br />
  +Rr   &#8211;rotate-right<br />
          rotate image right (+90 degrees)<br />
  +Rtd  &#8211;rotate-top-down<br />
          rotate image top-down (180 degrees)<br />
flipping:<br />
  +Lh   &#8211;flip-horizontally<br />
          flip image horizontally<br />
  +Lv   &#8211;flip-vertically<br />
          flip image vertically<br />
  +Lhv  &#8211;flip-both-axes<br />
          flip image horizontally and vertically<br />
scaling:<br />
  +a    &#8211;recognize-aspect<br />
          recognize pixel aspect ratio (default)<br />
  -a    &#8211;ignore-aspect<br />
          ignore pixel aspect ratio when scaling<br />
  +i    &#8211;interpolate  [n]umber of algorithm: integer<br />
          use interpolation when scaling (1..4, default: 1)<br />
  -i    &#8211;no-interpolation<br />
          no interpolation when scaling<br />
  -S    &#8211;no-scaling<br />
          no scaling, ignore pixel aspect ratio (default)<br />
  +Sxf  &#8211;scale-x-factor  [f]actor: float<br />
          scale x axis by factor, auto-compute y axis<br />
  +Syf  &#8211;scale-y-factor  [f]actor: float<br />
          scale y axis by factor, auto-compute x axis<br />
  +Sxv  &#8211;scale-x-size  [n]umber: integer<br />
          scale x axis to n pixels, auto-compute y axis<br />
  +Syv  &#8211;scale-y-size  [n]umber: integer<br />
          scale y axis to n pixels, auto-compute x axis<br />
modality LUT transformation:<br />
  -M    &#8211;no-modality<br />
          ignore stored modality LUT transformation<br />
  +M    &#8211;use-modality<br />
          use modality LUT transformation (default)<br />
VOI LUT transformation:<br />
  -W    &#8211;no-windowing<br />
          no VOI windowing (default)<br />
  +Wi   &#8211;use-window  [n]umber: integer<br />
          use the n-th VOI window from image file<br />
  +Wl   &#8211;use-voi-lut  [n]umber: integer<br />
          use the n-th VOI look up table from image file<br />
  +Wm   &#8211;min-max-window<br />
          compute VOI window using min-max algorithm<br />
  +Wn   &#8211;min-max-window-n<br />
          compute VOI window using min-max algorithm,<br />
          ignoring extreme values<br />
  +Wr   &#8211;roi-min-max-window  [l]eft [t]op [w]idth [h]eight: integer<br />
          compute ROI window using min-max algorithm,<br />
          region of interest is specified by l,t,w,h<br />
  +Wh   &#8211;histogram-window  [n]umber: integer<br />
          compute VOI window using Histogram algorithm,<br />
          ignoring n percent<br />
  +Ww   &#8211;set-window  [c]enter [w]idth: float<br />
          compute VOI window using center c and width w<br />
  +Wfl  &#8211;linear-function<br />
          set VOI LUT function to LINEAR<br />
  +Wfs  &#8211;sigmoid-function<br />
          set VOI LUT function to SIGMOID<br />
presentation LUT transformation:<br />
  +Pid  &#8211;identity-shape<br />
          set presentation LUT shape to IDENTITY<br />
  +Piv  &#8211;inverse-shape<br />
          set presentation LUT shape to INVERSE<br />
  +Pod  &#8211;lin-od-shape<br />
          set presentation LUT shape to LIN OD<br />
overlay:<br />
  -O    &#8211;no-overlays<br />
          do not display overlays<br />
  +O    &#8211;display-overlay  [n]umber: integer<br />
          display overlay n (0..16, 0=all, default: +O 0)<br />
  +Omr  &#8211;ovl-replace<br />
          use overlay mode &#8220;Replace&#8221;<br />
          (default for Graphic overlays)<br />
  +Omt  &#8211;ovl-threshold<br />
          use overlay mode &#8220;Threshold Replace&#8221;<br />
  +Omc  &#8211;ovl-complement<br />
          use overlay mode &#8220;Complement&#8221;<br />
  +Omv  &#8211;ovl-invert<br />
          use overlay mode &#8220;Invert Bitmap&#8221;<br />
  +Omi  &#8211;ovl-roi<br />
          use overlay mode &#8220;Region of Interest&#8221;<br />
          (default for ROI overlays)<br />
  +Osf  &#8211;set-foreground  [d]ensity: float<br />
          set overlay foreground density (0..1, default: 1)<br />
  +Ost  &#8211;set-threshold  [d]ensity: float<br />
          set overlay threshold density (0..1, default: 0.5)<br />
display LUT transformation:<br />
  +Dm   &#8211;monitor-file  [f]ilename: string<br />
          calibrate output according to monitor characteristics<br />
          defined in f<br />
  +Dp   &#8211;printer-file  [f]ilename: string<br />
          calibrate output according to printer characteristics<br />
          defined in f<br />
  +Da   &#8211;ambient-light  [a]mbient light: float<br />
          ambient light value (cd/m^2, default: file f)<br />
  +Di   &#8211;illumination  [i]llumination: float<br />
          illumination value (cd/m^2, default: file f)<br />
  +Dn   &#8211;min-density  [m]inimum optical density: float<br />
          Dmin value (default: off, only with +Dp)<br />
  +Dx   &#8211;max-density  [m]aximum optical density: float<br />
          Dmax value (default: off, only with +Dp)<br />
  +Dg   &#8211;gsd-function<br />
          use GSDF for calibration (default for +Dm/+Dp)<br />
  +Dc   &#8211;cielab-function<br />
          use CIELAB function for calibration<br />
compatibility:<br />
  +Ma   &#8211;accept-acr-nema<br />
          accept ACR-NEMA images without photometric<br />
          interpretation<br />
  +Mp   &#8211;accept-palettes<br />
          accept incorrect palette attribute tags<br />
          (0028,111x) and (0028,121x)<br />
  +Mc   &#8211;check-lut-depth<br />
          check 3rd value of the LUT descriptor, compare<br />
          with expected bit depth based on LUT data<br />
  +Mm   &#8211;ignore-mlut-depth<br />
          ignore 3rd value of the modality LUT descriptor,<br />
          determine bits per table entry automatically<br />
  +Mv   &#8211;ignore-vlut-depth<br />
          ignore 3rd value of the VOI LUT descriptor,<br />
          determine bits per table entry automatically<br />
TIFF format:<br />
  +Tl   &#8211;compr-lzw<br />
          LZW compression (default)<br />
  +Tr   &#8211;compr-rle<br />
          RLE compression<br />
  +Tn   &#8211;compr-none<br />
          uncompressed<br />
  +Pd   &#8211;predictor-default<br />
          no LZW predictor (default)<br />
  +Pn   &#8211;predictor-none<br />
          LZW predictor 1 (no prediction)<br />
  +Ph   &#8211;predictor-horz<br />
          LZW predictor 2 (horizontal differencing)<br />
  +Rs   &#8211;rows-per-strip  [r]ows: integer (default: 0)<br />
          rows per strip, default 8K per strip<br />
PNG format:<br />
  +il   &#8211;interlace<br />
          create interlaced file (default)<br />
  -il   &#8211;nointerlace<br />
          create non-interlaced file<br />
  +mf   &#8211;meta-file<br />
          create PNG file meta information (default)<br />
  -mf   &#8211;meta-none<br />
          no PNG file meta information<br />
other transformations:<br />
  +G    &#8211;grayscale<br />
          convert to grayscale if necessary<br />
  +P    &#8211;change-polarity<br />
          change polarity (invert pixel output)<br />
  +C    &#8211;clip-region  [l]eft [t]op [w]idth [h]eight: integer<br />
          clip image region (l, t, w, h)</p>
<h3>output options</h3>
<pre><code>
general:
  -im   --image-info
          print image details (requires verbose mode)
  -o    --no-output
          do not create any output (useful with -im)
image format:
  +op   --write-raw-pnm
          write 8-bit binary PGM/PPM (default for files)
  +opb  --write-8-bit-pnm
          write 8-bit ASCII PGM/PPM (default for stdout)
  +opw  --write-16-bit-pnm
          write 16-bit ASCII PGM/PPM
  +opn  --write-n-bit-pnm  [n]umber: integer
          write n-bit ASCII PGM/PPM (1..32)
  +ob   --write-bmp
          write 8-bit (monochrome) or 24-bit (color) BMP
  +obp  --write-8-bit-bmp
          write 8-bit palette BMP (monochrome only)
  +obt  --write-24-bit-bmp
          write 24-bit truecolor BMP
  +obr  --write-32-bit-bmp
          write 32-bit truecolor BMP
  +ot   --write-tiff
          write 8-bit (monochrome) or 24-bit (color) TIFF
  +on   --write-png
          write 8-bit (monochrome) or 24-bit (color) PNG
</code></pre>
<h2>NOTES</h2>
<p> The following preferred interpolation algorithms can be selected using the <i>&#8211;interpolate</i> option: </p>
<dl>
<dt>&bull;</p>
<dd> 1 = free scaling algorithm with interpolation from pbmplus toolkit</p>
<dt>&bull;</p>
<dd> 2 = free scaling algorithm with interpolation from c&#8217;t magazine</p>
<dt>&bull;</p>
<dd> 3 = magnification algorithm with bilinear interpolation from Eduard Stanescu</p>
<dt>&bull;</p>
<dd> 4 = magnification algorithm with bicubic interpolation from Eduard Stanescu</dl>
<p> The <i>&#8211;write-tiff</i> option is only available when DCMTK has been configured and compiled with support for the external <code>libtiff</code> TIFF library. The availability of the TIFF compression options depends on the <code>libtiff</code> configuration. In particular, the patented LZW algorithm may not be available. </p>
<p> The <i>&#8211;write-png</i> option is only available when DCMTK has been configured and compiled with support for the external <code>libpng</code> PNG library. Option <i>&#8211;interlace</i> enables progressive image view while loading the PNG file. Only a few applications take care of the meta info (TEXT) in a PNG file.</p>
<h2>TRANSFER SYNTAXES</h2>
<p> <code>dcm2pnm</code> supports the following transfer syntaxes for input (<i>dcmfile-in</i>): </p>
<pre>
LittleEndianImplicitTransferSyntax             1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax             1.2.840.10008.1.2.1
DeflatedExplicitVRLittleEndianTransferSyntax   1.2.840.10008.1.2.1.99 (*)
BigEndianExplicitTransferSyntax                1.2.840.10008.1.2.2
RLELosslessTransferSyntax                      1.2.840.10008.1.2.5
</pre>
<p> (*) if compiled with zlib support enabled</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcm2pnm</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>FILES</h2>
<p> <i>&lt;datadir&gt;/camera.lut</i> &#8211; sample characteristics file of a camera<br />
 <i>&lt;datadir&gt;/monitor.lut</i> &#8211; sample characteristics file of a monitor<br />
 <i>&lt;datadir&gt;/printer.lut</i> &#8211; sample characteristics file of a printer<br />
 <i>&lt;datadir&gt;/scanner.lut</i> &#8211; sample characteristics file of a scanner</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmj2pnm/">dcmj2pnm</a></code>(1), <code><a href="/docs/linux/man/1-img2dcm/">img2dcm</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1998-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
