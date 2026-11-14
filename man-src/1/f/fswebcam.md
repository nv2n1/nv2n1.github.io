---
title: "fswebcam(1)"
name: "fswebcam"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fswebcam/"
description: "fswebcam – Small and simple webcam for *nix."
---

<h2>NAME</h2>
<p> fswebcam &#8211; Small and simple webcam for *nix.</p>
<h2>SYNOPSIS</h2>
<p> <code>fswebcam</code> [<i>&lt;options&gt;</i>] <i>&lt;filename&gt;</i> [[<i>&lt;options&gt;</i>] <i>&lt;filename&gt;</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> fswebcam is a small and simple webcam app for *nix. It can capture images from a number of different sources and perform simple manipulation on the captured image. The image can be saved as one or more PNG or JPEG files. </p>
<p> The PNG or JPEG image can be sent to stdio using the filename &quot;-&quot;. The output filename is formatted by <code>strftime</code>. </p>
<h2>CONFIGURATION</h2>
<h3>Configuration File</h3>
<dl>
<dt>Config files use the long version of options without the &quot;&#8211;&quot; prefix. Comments start with a # symbol at the beginning of the line.</p>
<dd>
</dl>
<h3>General Options</h3>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show a usage summary. </p>
<dt><code>-c</code>, <code>&#8211;config</code></p>
<dd> Load options from a file. You can load more than one config file, and can mix them with command-line arguments. </p>
<p> Note: This option can not be used from within a configuration file. </p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Hides all messages except errors. </p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print extra information during the capture process. </p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number and exit. </p>
<dt><code>-l</code>, <code>&#8211;loop</code> <i>&lt;frequency&gt;</i></p>
<dd> Continually capture images. The time between images is specified in seconds.</p>
<dt>
<dd> Default behaviour is to capture a single image and exit.</p>
<dt>
<dd> <i>Note</i>: The time to capture the next image is calculated relative to the epoch, so an image will not be captured immediately when the program is first started. </p>
<dt><code>&#8211;offset</code> <i>&lt;seconds&gt;</i></p>
<dd> Sets the offset to use when calculating when the next image is due in loop mode. Value can be positive or negative. </p>
<dt><code>-b</code>, <code>&#8211;background</code></p>
<dd> Run in the background. In this mode <i>stdout</i> and console logging are unavailable. </p>
<dt><code>&#8211;pid</code> <i>&lt;filename&gt;</i></p>
<dd> Saves the PID of the background process to the specified file. Ignored when not using background mode. </p>
<dt><code>&#8211;log</code> <i>[file/syslog:]&lt;filename&gt;</i></p>
<dd> Redirect log messages to a file or syslog. For example</p>
<dt>
<dd> &#8211;log output.log<br />
 &#8211;log file:output.log<br />
 &#8211;log syslog </p>
<dt><code>&#8211;gmt</code></p>
<dd> Use GMT instead of the local timezone when formatting text with <code>strftime</code>. </p>
</dl>
<h3>Capture Options</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;device</code> <i>[&lt;prefix&gt;:]&lt;device name&gt;</i></p>
<dd> Set the source or device to use. The source module is selected automatically unless specified in the prefix.</p>
<dt>
<dd> Default is <i>/dev/video0</i>.</p>
<dt>
<dd> Available source modules, in order of preference:</p>
<dt>
<dd> V4L2 &#8211; Capture images from a V4L2 compatible video device.<br />
 V4L1 &#8211; Capture images from a V4L1 compatible video device.<br />
 FILE &#8211; Capture an image from a JPEG or PNG image file.<br />
 RAW &#8211; Reads images straight from a device or file.<br />
 TEST &#8211; Draws colour bars. </p>
<dt><code>-i</code>, <code>&#8211;input</code> <i>&lt;input number or name&gt;</i></p>
<dd> Set the input to use. You may select an input by either it&#8217;s number or name.</p>
<dt>
<dd> Default is &quot;0&quot;. </p>
<dt><code>&#8211;list-inputs</code></p>
<dd> List available inputs for the selected source or device.</p>
<dt>
<dd> fswebcam -d v4l2:/dev/video1 &#8211;list-inputs </p>
<dt><code>-t</code>, <code>&#8211;tuner</code> <i>&lt;tuner number&gt;</i></p>
<dd> Set the tuner to use. </p>
<dt><code>-f</code>, <code>&#8211;frequency</code> <i>&lt;frequency&gt;</i></p>
<dd> Set the frequency of the selected input or tuner. The value may be read as KHz or MHz depending on the input or tuner. </p>
<dt><code>-p</code>, <code>&#8211;palette</code> <i>&lt;name&gt;</i></p>
<dd> Try to use the specified image format when capturing the image.</p>
<dt>
<dd> Default is to select one automatically.</p>
<dt>
<dd> Supported formats:</p>
<dt>
<dd> PNG<br />
 JPEG<br />
 MJPEG<br />
 RGB32<br />
 RGB24<br />
 BGR32<br />
 BGR24<br />
 YUYV<br />
 UYVY<br />
 YUV420P<br />
 BAYER<br />
 SGBRG8<br />
 SGRBG8<br />
 RGB565<br />
 RGB555<br />
 GREY </p>
<dt><code>-r</code>, <code>&#8211;resolution</code> <i>&lt;dimensions&gt;</i></p>
<dd> Set the image resolution of the source or device. The actual resolution used may differ if the source or device cannot capture at the specified resolution.</p>
<dt>
<dd> Default is &quot;384&#215;288&quot;. </p>
<dt><code>&#8211;fps</code> <i>&lt;frames per second&gt;</i></p>
<dd> Sets the frame rate of the capture device. This currently only works with certain V4L2 devices.</p>
<dt>
<dd> Default is &quot;0&quot;, let the device decide. </p>
<dt><code>-F</code>, <code>&#8211;frames</code> <i>&lt;number&gt;</i></p>
<dd> Set the number of frames to capture. More frames mean less noise in the final image, however capture times will be longer and moving objects may appear blurred.</p>
<dt>
<dd> Default is &quot;1&quot;. </p>
<dt><code>-S</code>, <code>&#8211;skip</code> <i>&lt;number&gt;</i></p>
<dd> Set the number of frames to skip. These frames will be captured but won&#8217;t be use. Use this option if your camera sends some bad or corrupt frames when it first starts capturing.</p>
<dt>
<dd> Default is &quot;0&quot;. </p>
<dt><code>-D</code>, <code>&#8211;delay</code> <i>&lt;delay&gt;</i></p>
<dd> Inserts a delay after the source or device has been opened and initialised, and before the capture begins. Some devices need this delay to let the image settle after a setting has changed. The delay time is specified in seconds. </p>
<dt><code>-R</code>, <code>&#8211;read</code></p>
<dd> Use read() to capture images. This can be slower but more stable with some devices.</p>
<dt>
<dd> Default is to use mmap(), falling back on read() if mmap() is unavailable. </p>
<dt><code>-s</code>, <code>&#8211;set</code> <i>&lt;name=value&gt;</p>
<dd> Set a control. These are used by the source modules to control image or device parameters. Numeric values can be expressed as a percentage of there maximum range or a literal value, for example:</p>
<dt>
<dd> &#8211;set brightness=50% &#8211;set framerate=5</p>
<dt>
<dd> Non-numeric controls are also supported:</p>
<dt>
<dd> &#8211;set lights=on</p>
<dt>
<dd> V4L2 features a type of control called a &#8216;button&#8217;. These controls do not take any value, but trigger an action. For example:</p>
<dt>
<dd> &#8211;set &quot;Restore Factory Settings&quot;</p>
<dt>
<dd> Control names and values are not case sensitive.</p>
<dt>
<dd> Note</i>: Available controls will vary depending in the source module and devices used. For more information see the <code>&#8211;list-controls</code> option. </p>
<dt><code>&#8211;list-controls</code></p>
<dd> List available controls and their current values for the selected source module and device. For example:</p>
<dt>
<dd> fswebcam -d v4l2:/dev/video2 &#8211;list-controls </p>
</dl>
<h3>Output Options</h3>
<dl>
<dt>These options are performed in the order they appear on the command line, only effecting images output later on the command line. For example:</p>
<dd>
<dt>
<dd> fswebcam -r 640&#215;480 output1.jpeg &#8211;scale 320&#215;240 output2.jpeg</p>
<dt>
<dd> Will create two images, &quot;output1.jpeg&quot; containing a full resolution copy of the captured image and &quot;output2.jpeg&quot; containing the same captured image but scaled to half the size. </p>
<dt><code>&#8211;no-banner</code></p>
<dd> Disable the banner. </p>
<dt><code>&#8211;top-banner</code></p>
<dd> Position the banner at the top of the image. </p>
<dt><code>&#8211;bottom-banner</code></p>
<dd> Position the banner at the bottom of the image.</p>
<dt>
<dd> This is the default. </p>
<dt><code>&#8211;banner-colour</code> <i>&lt;#AARRGGBB&gt;</i></p>
<dd> Set the colour of the banner. Uses the web-style hexadecimal format (#RRGGBB) to describe the colour, and can support an alpha channel (#AARRGGBB). Examples:</p>
<dt>
<dd> &quot;#FF0000&quot; is pure red.<br />
 &quot;#80000000&quot; is semi-transparent black.<br />
 &quot;#FF000000&quot; is invisible (alpha channel is at maximum).<br />
 Default is &quot;#40263A93&quot;. </p>
<dt><code>&#8211;line-colour</code> <i>&lt;#AARRGGBB&gt;</i></p>
<dd> Set the colour of the divider line. See <code>&#8211;banner-colour</code> for more information.</p>
<dt>
<dd> Default is &quot;#00FF0000&quot;. </p>
<dt><code>&#8211;text-colour</code> <i>&lt;#AARRGGBB&gt;</i></p>
<dd> Set the colour of the text. See <code>&#8211;banner-colour</code> for more information.</p>
<dt>
<dd> Default is &quot;#00FFFFFF&quot;. </p>
<dt><code>&#8211;font</code> <i>&lt;[file or font name]:[font size]&gt;</i></p>
<dd> Set the font used in the banner. If no path is specified the path in the GDFONTPATH environment variable is searched for the font.</p>
<dt>
<dd> If no font size is specified the default of &quot;10&quot; will be used.</p>
<dt>
<dd> Default is &quot;luxisr:10&quot;. </p>
<dt><code>&#8211;no-shadow</code></p>
<dd> Disable the text shadow. </p>
<dt><code>&#8211;shadow</code></p>
<dd> Enable the text shadow.</p>
<dt>
<dd> This is the default behaviour. </p>
<dt><code>&#8211;title</code> <i>&lt;text&gt;</i></p>
<dd> Set the main text, located in the top left of the banner. </p>
<dt><code>&#8211;no-title</code></p>
<dd> Clear the main text. </p>
<dt><code>&#8211;subtitle</code> <i>&lt;text&gt;</i></p>
<dd> Set the sub-title text, located in the bottom left of the banner. </p>
<dt><code>&#8211;no-subtitle</code></p>
<dd> Clear the sub-title text. </p>
<dt><code>&#8211;timestamp</code> <i>&lt;text&gt;</i></p>
<dd> Set the timestamp text, located in the top right of the banner. This string is formatted by <code>strftime</code>.</p>
<dt>
<dd> Default is &quot;%Y-%m-%d %H:%M (%Z)&quot;. </p>
<dt><code>&#8211;no-timestamp</code></p>
<dd> Clear the timestamp text. </p>
<dt><code>&#8211;info</code> <i>&lt;text&gt;</i></p>
<dd> Set the info text, located in the bottom right of the banner. </p>
<dt><code>&#8211;no-info</code></p>
<dd> Clear the info text. </p>
<dt><code>&#8211;underlay</code> <i>&lt;filename&gt;</i></p>
<dd> Load a PNG image and overlay it on the image, below the banner. The image is aligned to the top left.</p>
<dt>
<dd> <i>Note</i>: The underlay is only applied when saving an image and is not modified by any of the image options or effects. </p>
<dt><code>&#8211;no-underlay</code></p>
<dd> Clear the underlay image. </p>
<dt><code>&#8211;overlay</code> <i>&lt;filename&gt;</i></p>
<dd> Load a PNG image and overlay on the image, above the banner. The image is aligned to the top left.</p>
<dt>
<dd> <i>Note</i>: The overlay is only applied when saving an image and is not modified by any of the image options or effects. </p>
<dt><code>&#8211;no-overlay</code></p>
<dd> Remove the overlay image. </p>
<dt><code>&#8211;jpeg</code> <i>&lt;factor&gt;</i></p>
<dd> Set JPEG as the output image format. The compression factor is a value between 0 and 95, or -1 for automatic.</p>
<dt>
<dd> This is the default format, with a factor of &quot;-1&quot;. </p>
<dt><code>&#8211;png</code> <i>&lt;factor&gt;</i></p>
<dd> Set PNG as the output image format. The compression factor can be a value between 0 and 9, or -1 for automatic. </p>
<dt><code>&#8211;save</code> <i>&lt;filename&gt;</i></p>
<dd> Saves the image to the specified filename. </p>
<p> Note: This isn&#8217;t necessary on the command-line where a filename alone is enough to save an image. </p>
<dt><code>&#8211;revert</code></p>
<dd> Revert to the original captured image and resolution. This undoes all previous effects on the image. </p>
<p> Note: This only reverts the image itself, and not options such as font, colours and overlay. </p>
<dt><code>&#8211;flip</code> <i>&lt;direction[,direction]&gt;</p>
<dd> Flips the image. Direction can be (h)orizontal or (v)ertical. Example:</p>
<dt>
<dd> &#8211;flip h Flips the image horizontally.<br />
 &#8211;flip h,v Flips the image both horizontally and vertically. </p>
<dt></i><code>&#8211;crop</code> <i>&lt;dimensions[,offset]&gt;</i></p>
<dd> Crop the image. With no offset the cropped area will be the center of the image. Example:</p>
<dt>
<dd> &#8211;crop 320&#215;240 Crops the center 320&#215;240 area of the image.<br />
 &#8211;crop 10&#215;10,0x0 Crops the 10&#215;10 area at the top left corner of the image. </p>
<dt><code>&#8211;scale</code> &lt;dimensions&gt;</p>
<dd> Scale the image.</p>
<dt>
<dd> Example: &quot;&#8211;scale 640&#215;480&quot; scales the image up or down to 640&#215;480.</p>
<dt>
<dd> <i>Note:</i> The aspect ratio of the image is not maintained. </p>
<dt><code>&#8211;rotate</code> <i>&lt;angle&gt;</i></p>
<dd> Rotate the image in right angles (90, 180 and 270 degrees).</p>
<dt>
<dd> <i>Note:</i> Rotating the image 90 or 270 degrees will swap the dimensions. </p>
<dt><code>&#8211;deinterlace</code></p>
<dd> Apply a simple deinterlacer to the image. </p>
<dt><code>&#8211;invert</code></p>
<dd> Invert all the colours in the image, creating a negative. </p>
<dt><code>&#8211;exec</code> &lt;command&gt;</p>
<dd> Executes the specified command and waits for it to complete before continuing. The command line is formatted by <code>strftime</code>. </p>
</dl>
<h2>SIGNALS</h2>
<dl>
<dt><code>SIGHUP</code></p>
<dd> This causes fswebcam to reload it&#8217;s configuration. </p>
<dt><code>SIGUSR1</code></p>
<dd> Causes fswebcam to capture an image immediately without waiting on the timer in loop mode. </p>
</dl>
<h2>KNOWN BUGS</h2>
<p> The spacing between letters may be incorrect. This is an issue with the GD library. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to &lt;phil [at] sanslogic.co.uk&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code> <a href="/docs/linux/man/1-ncftpput/">ncftpput</a>(1), <a href="/docs/linux/man/3-strftime/">strftime</a>(3) </code> </p>
<h2>AUTHOR</h2>
<p> Written by Philip Heron &lt;phil [at] sanslogic.co.uk&gt;. </p>
<h2>Index</h2>
