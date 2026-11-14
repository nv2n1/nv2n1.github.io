---
title: "ufraw(1)"
name: "ufraw"
section: "1"
letter: "u"
url: "/docs/linux/man/1-ufraw/"
---

<h2 class="name">NAME</h2>
 

 UFRaw - Convert camera RAW images to standard image files. 

<h2>SYNOPSIS</h2>

<dl>
<dt>ufraw [<font SIZE="-1">OPTIONS</font>] &lt;rawfile(s)&gt;
<dd>
<dt>ufraw-batch [<font SIZE="-1">OPTIONS</font>] &lt;rawfile(s)&gt;
<dd></dl>

<h2>DESCRIPTION</h2>

 The Unidentified Flying Raw (UFRaw) is a utility to read and manipulate raw images from digital cameras. It reads raw images using Dave Coffin's raw conversion utility - DCRaw. UFRaw supports basic color management using Little <font SIZE="-1">CMS,</font> allowing the user to apply color profiles. For Nikon users UFRaw has the advantage that it can read the camera's tone curves. Even if you don't own a Nikon, you can still apply a Nikon curve to your images. 

 By default 'ufraw' displays a preview window for each raw image allowing the user to tweak the image parameters before saving. If no raw images are given at the command line, UFRaw will display a file chooser dialog. To process the images with no questions asked (and no preview) use the command 'ufraw-batch'. 

 The input files can be either raw images or UFRaw ID-files. ID-files contain a raw image filename and the parameters for handling the image. 

 UFRaw can also work as a <font SIZE="-1">GIMP</font> plug-in. To activate it simply open a raw image or a UFRaw ID-file in the <font SIZE="-1">GIMP.</font>

<h2>OPTIONS</h2>

 The options supplied on the command-line decide the starting-values for the <font SIZE="-1">GUI.</font> The <font SIZE="-1">GUI</font> will then allow you to tweak these values before saving the final image.

<h3>General Options</h3>

<dl>
<dt>--version
<dd> Display the version of UFRaw and exit.
<dt>--help
<dd> Display a brief description of how to use UFRaw and exit.
<dt>--silent
<dd> Do not display any messages during conversion. This option is only valid with 'ufraw-batch'.
<dt>--conf=&lt;ID-filename&gt;
<dd> Load all parameters from an ID-file. This feature can be used to tweak the parameters for one file using the <font SIZE="-1">GUI</font> and using those parameters as the starting point for other images as well.</dl>

<h3>Image Manipulation Options</h3>

 These command-line options override settings from the default configuration of UFRaw and from any loaded ID-file. The best way to learn about how these parameters work is to experiment with the <font SIZE="-1">GUI.</font> All parameters correspond exactly to a setting available in the <font SIZE="-1">GUI.</font> Not all parameters in the <font SIZE="-1">GUI</font> have corresponding command-line options.
<dl>
<dt>--wb=camera|auto
<dd> White balance setting. ``camera'' means that UFRaw tries to read the color-temperature and green color component that the camera recorded in the meta-information in the raw-file. This does not work for all cameras. If UFRaw fails to read the white-balance information from the meta-information, it falls back to ``auto''. 

 ``auto'' means that UFRaw calculates the color-temperature and green color component automatically from the image data. 

 The white-balance can also be set manually with the --temperature and --green options.
<dt>--temperature=TEMP
<dd> Manually set the color temperature in Kelvin.
<dt>--green=GREEN
<dd> Green color component. Range 0.20 to 2.50.
<dt>--gamma=GAMMA
<dd> Gamma adjustment of the base curve. Range 0.10 to 1.00. Default 0.45.
<dt>--linearity=LINEARITY
<dd> Linearity of the base curve. Range 0.00 to 1.00. Default 0.10.
<dt>--exposure=auto|EXPOSURE
<dd> Auto exposure or exposure correction in <font SIZE="-1">EV.</font> Range -3.00 to 3.00. Default 0.
<dt>--restore=clip|lch|hsv
<dd> Control how highlights are restored when applying negative <font SIZE="-1">EV. </font>'clip' restores nothing and is therefore safe from any artifacts. 'lch' restores in <font SIZE="-1">LCH</font> space, resulting in restored highlights with soft details (good for clouds). 'hsv' restores in <font SIZE="-1">HSV</font> space, resulting in restored highlights with sharp details. The default is 'lch'.
<dt>--clip=digital|film
<dd> Control how highlights are clipped when applying positive <font SIZE="-1">EV. </font>'digital' corresponds to using a linear response, emulating the harsh behaviour of the digital sensor. 'film' emulate the soft film response. The default is 'digital'.
<dt>--saturation=SAT
<dd> Adjust the color saturation. Range 0.00 to 8.00. Default 1.0, use 0 for black &amp; white output.
<dt>--wavelet-denoising-threshold=THRESHOLD
<dd> Wavelet denoising threshold (default 0.0).
<dt>--base-curve=manual|linear|custom|camera|CURVE
<dd> Type of tone curve to use. The base curve is a combination of the gamma curve corrected by the curve specified here. The base curve is applied to each channel of the raw data after the white balance and color matrix, but before the <font SIZE="-1">ICC</font> transformation. 

 ``manual'' means that a manual tone curve is used. This is probably not very useful as a command-line option, since there is no way to specify what the curve should look like. 

 ``linear'' means that no tone curve corrections is performed. 

 ``custom'' means that UFRaw shall use the curve supplied by the camera in the meta-information in the raw-file. 

 ``camera'' means that UFRaw shall use the ``custom'' curve only if the camera was set to use it (according to the meta-information). Otherwise the ``linear'' curve is used. 

 <font SIZE="-1">CURVE</font> can be the filename (without path) of any curve that was previously loaded in the <font SIZE="-1">GUI.</font> 

 The default is ``camera'' if such a curve exists, linear otherwise.
<dt>--base-curve-file=&lt;curve-file&gt;
<dd> Load the base curve from a file. The curve file format can be either UFRaw's <font SIZE="-1">XML</font> format or Nikon's <font SIZE="-1">NTC/NCV</font> format.
<dt>--curve=manual|linear|CURVE
<dd> Type of luminosity curve to use. This curve is applied in <font SIZE="-1">HSV</font> space and therefore hue and saturation should not be effected by it. 

 ``manual'' means that a manual luminosity curve is used. This is probably not very useful as a command-line option, since there is no way to specify what the curve should look like. 

 ``linear'' means that no luminosity correction is performed. 

 <font SIZE="-1">CURVE</font> can be the filename (without path) of any curve that was previously loaded in the <font SIZE="-1">GUI.</font> 

 The default is ``linear''.
<dt>--curve-file=&lt;curve-file&gt;
<dd> Load the luminosity curve from a file. The curve file format can be either UFRaw's <font SIZE="-1">XML</font> format or Nikon's <font SIZE="-1">NTC/NCV</font> format.
<dt>--black-point=auto|BLACK
<dd> Black-point value. Range 0.0 to 1.0, default 0.0.
<dt>--interpolation=ahd|vng|four-color|ppg|bilinear
<dd> Interpolation algorithm to use when converting from the color filter array to normal <font SIZE="-1">RGB</font> values. <font SIZE="-1">AHD </font>(Adaptive Homogeneity Directed) interpolation is the best, but also the slowest. <font SIZE="-1">VNG </font>(Variable Number Gradients) is second best and a bit faster. Bilinear is the simplest yet fastest interpolation. 

 ``four-color'' is a variation of the <font SIZE="-1">VNG</font> interpolation that should only be used if you see strange square patterns in the <font SIZE="-1">VNG</font> interpolation, See &lt;<a rel="nofollow" HREF="http://www.cybercom.net/~dcoffin/dcraw/">http://www.cybercom.net/~dcoffin/dcraw/</a>&gt;. 

 <font SIZE="-1">AHD</font> is the default interpolation. <font SIZE="-1">AHD</font> interpolation is not supported for cameras with four color filters, such as the Sony-828 <font SIZE="-1">RGBE</font> filter. In such cases, <font SIZE="-1">VNG</font> interpolation will be used instead.
<dt>--color-smoothing
<dd> Apply color smoothing.
<dt>--grayscale=none|lightness|luminance|value|mixer
<dd> Grayscale conversion algorithm to use (default none).
<dt>--darkframe=FILE
<dd> Use <font SIZE="-1">FILE</font> for raw darkframe subtraction.</dl>

<h3>Output Options</h3>

 The options which are related to the final output are:
<dl>
<dt>--shrink=FACTOR
<dd> Shrink the image by <font SIZE="-1">FACTOR </font>(default 1).
<dt>--size=SIZE
<dd> Downsize max(height,width) to <font SIZE="-1">SIZE.</font>
<dt>--rotate=camera|ANGLE|no
<dd> Rotate image to camera's setting, by <font SIZE="-1">ANGLE</font> degrees clockwise, or do not rotate the image (default camera)
<dt>--crop-(left|right|top|bottom)=PIXELS
<dd> Crop the output to the given pixel range, relative to the raw image after rotation but before any scaling.
<dt>--out-type=ppm|tiff|tif|png|jpeg|jpg|fits
<dd> Output file-format to use. The default output file-format is ppm.
<dt>--out-depth=8|16
<dd> Output bit depth per channel. ppm, tiff, png and fits output formats can uses either 8 bits or 16 bits to encode each of the Red, Green and Blue components of each pixel. The jpeg format only allows for 8 bits for each color component. 

 The raw-files contain more than eight bits of information for each color component. This means that by using an eight bit format, you are actually discarding some of the information supplied by the camera. This is not a problem if you only plan to view the image on screen. For prints you should consider a 16 bits workflow.
<dt>--compression=VALUE
<dd> <font SIZE="-1">JPEG</font> quality factor. Range 0-100 with a higher number giving a higher quality at the cost of a larger file. Default 85. The --compression parameter is only relevant if the output file-format is jpeg.
<dt>--[no]exif
<dd> Embed exif in output. Default embed exif. Exif is currently embedded in <font SIZE="-1">JPEG, PNG</font> and <font SIZE="-1">TIFF</font> output.
<dt>--[no]zip
<dd> Enable [disable] <font SIZE="-1">TIFF</font> zip compression. The zip-compression is loss-less. Default nozip. The --zip parameter is only relevant if the output file-format if tiff8 or tiff16.
<dt>--out-path=PATH
<dd> <font SIZE="-1">PATH</font> for output file. In batch mode by default, output-files are placed in the same directory as the input-files. In interactive mode UFRaw tries to ''guess'' if you have a favorite output directory.
<dt>--output=FILE
<dd> Output file name to use. This is only relevant if a single raw-file is supplied on the command-line. . Use '-' to output to stdout. The default is to name the output-file the same as the input-file but with the extension given by the output file-format.
<dt>--overwrite
<dd> Overwrite existing files without asking. Default is to ask before deleting an existing file.
<dt>--create-id=no|also|only
<dd> Control whether UFRaw <font SIZE="-1">ID</font> files are created for the output image. (Default is no).
<dt>--embedded-image
<dd> Extract the preview image embedded in the raw file instead of converting the raw image. This option is only valid with 'ufraw-batch'.</dl>

<h2>Conversion Setting Priority</h2>

 Conversion settings are applied in the following priority order:
<dl>
<dt>1. Command-line options
<dd>
<dt>2. Settings from the configuration file specified with --conf=&lt;ID-file&gt; (ignoring any filenames in the ID-file).
<dd>
<dt>3. Settings from an ID-file supplied as an input-file.
<dd>
<dt>4. Settings from $HOME/.ufrawrc
<dd>
<dt>5. UFRaw's default settings.
<dd></dl>
 

 This means that an option supplied on the command-line always takes precedence over all other options. 

 The conversion settings can be changed in the <font SIZE="-1">GUI</font> before the resulting image is saved.

<h2>FILES</h2>

 <tt>$HOME</tt>/.ufrawrc - UFRaw resource file containing the user default settings. This is an <font SIZE="-1">XML</font> file that can be modified with any text editor. Still, it is recommended not to edit this file. This file is updated from the <font SIZE="-1">GUI</font> when you save an image, or when you explicitly ask to save this file in the 'Options' menu. 

 <tt>$HOME</tt>/.ufraw-gtkrc - An optional file for setting up a specific <font SIZE="-1">GTK</font> theme for UFRaw.

<h2>ONLINE RESOURCES</h2>

<dl>
<dt>UFRaw homepage: &lt;<a rel="nofollow" HREF="http://ufraw.sourceforge.net">http://ufraw.sourceforge.net</a>&gt;
<dd>
<dt>DCRaw homepage: &lt;<a rel="nofollow" HREF="http://www.cybercom.net/~dcoffin/dcraw">http://www.cybercom.net/~dcoffin/dcraw</a>&gt;
<dd></dl>

<h2>SEE ALSO</h2>

<dl>
<dt>The <font SIZE="-1">GIMP</font> homepage: &lt;<a rel="nofollow" HREF="http://www.gimp.org">http://www.gimp.org</a>&gt;
<dd> 

</dl>

<h2>Index</h2>


