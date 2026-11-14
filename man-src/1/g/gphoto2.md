---
title: "gphoto2(1)"
name: "gphoto2"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gphoto2/"
description: "gphoto2 – command-line gphoto2 client"
---

<h2 class="name">NAME</h2>
<p> gphoto2 &#8211; command-line gphoto2 client </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gphoto2</code> [&#8211;debug] [&#8211;debug-logfile&nbsp;<wbr><i>FILENAME</i>] [[-q] | [&#8211;quiet]] [[-v] | [&#8211;verbose]] [[-h] | [&#8211;help]]</p>
<dd> [&#8211;hook-script&nbsp;<wbr><i>FILENAME</i>]</p>
<dd> [&#8211;list-cameras] [&#8211;list-ports] [&#8211;stdout] [&#8211;stdout-size]</p>
<dd> [&#8211;auto-detect] [&#8211;port&nbsp;<wbr><i>PATH</i>] [&#8211;speed&nbsp;<wbr><i>SPEED</i>] [&#8211;camera&nbsp;<wbr><i>MODEL</i>]</p>
<dd> [&#8211;filename&nbsp;<wbr><i>FILENAME</i>]</p>
<dd> [&#8211;usbid&nbsp;<wbr><i>USBIDS</i>]</p>
<dd> [[-a] | [&#8211;abilities]]</p>
<dd> [[&#8211;folder&nbsp;<wbr><i>FOLDER</i>] | [-f&nbsp;<wbr><i>FOLDER</i>]] [[[-R] | [&#8211;recurse]] | [&#8211;no-recurse]]</p>
<dd> [[-l] | [&#8211;list-folders]]</p>
<dd> [[-L] | [&#8211;list-files]] [[-m&nbsp;<wbr><i>NAME</i>] | [&#8211;mkdir&nbsp;<wbr><i>NAME</i>]]</p>
<dd> [[-r&nbsp;<wbr><i>NAME</i>] | [&#8211;rmdir&nbsp;<wbr><i>NAME</i>]] [[-n] | [&#8211;num-files]]</p>
<dd> [[-p&nbsp;<wbr><i>RANGE</i>] | [&#8211;get-file&nbsp;<wbr><i>RANGE</i>]] [[-P] | [&#8211;get-all-files]]</p>
<dd> [[-t&nbsp;<wbr><i>RANGE</i>] | [&#8211;get-thumbnail&nbsp;<wbr><i>RANGE</i>]]</p>
<dd> [[-T] | [&#8211;get-all-thumbnails]]</p>
<dd> [&#8211;get-raw-data&nbsp;<wbr><i>RANGE</i>] [&#8211;get-all-raw-data]</p>
<dd> [&#8211;get-audio-data&nbsp;<wbr><i>RANGE</i>] [&#8211;get-all-audio-data]</p>
<dd> [&#8211;force-overwrite]</p>
<dd> [&#8211;new]</p>
<dd> [[-d&nbsp;<wbr><i>RANGE</i>] | [&#8211;delete-file&nbsp;<wbr><i>RANGE</i>]] [[-D] | [&#8211;delete-all-files]]</p>
<dd> [[-u&nbsp;<wbr><i>FILENAME</i>] | [&#8211;upload-file&nbsp;<wbr><i>FILENAME</i>]] [&#8211;config]</p>
<dd> [&#8211;list-config]</p>
<dd> [&#8211;get-config&nbsp;<wbr><i>CONFIGENTRY</i>] [&#8211;set-config&nbsp;<wbr><i>CONFIGENTRY=CONFIGVALUE</i>] [&#8211;set-config-index&nbsp;<wbr><i>CONFIGENTRY=CONFIGINDEX</i>] [&#8211;set-config-value&nbsp;<wbr><i>CONFIGENTRY=CONFIGVALUE</i>]</p>
<dd> [&#8211;capture-preview]</p>
<dd> [[-F&nbsp;<wbr><i>COUNT</i>] | [&#8211;frames&nbsp;<wbr><i>COUNT</i>]] [[-I&nbsp;<wbr><i>SECONDS</i>] | [&#8211;interval&nbsp;<wbr><i>SECONDS</i>]]</p>
<dd> [&#8211;reset-interval]</p>
<dd> [&#8211;capture-image] [&#8211;capture-movie] [&#8211;capture-sound]</p>
<dd> [&#8211;capture-tethered&nbsp;<wbr><i>SECONDS or COUNT</i>]</p>
<dd> [&#8211;wait-event&nbsp;<wbr><i>SECONDS or COUNT</i>] [&#8211;wait-event-and-download&nbsp;<wbr><i>SECONDS or COUNT</i>]</p>
<dd> [&#8211;show-info&nbsp;<wbr><i>RANGE</i>]</p>
<dd> [&#8211;show-exif&nbsp;<wbr><i>RANGE</i>]</p>
<dd> [&#8211;storage-info] [&#8211;summary] [&#8211;manual] [&#8211;about] [&#8211;shell]</dl>
<h2>DESCRIPTION</h2>
<dd><a href="/docs/linux/man/3-libgphoto2/">libgphoto2</a>(3) is a cross-platform digital camera library, and <a href="/docs/linux/man/1-gphoto2/">gphoto2</a>(1) is a command-line client for it. </p>
<p> Where an option takes a <i>RANGE</i> of files, thumbnails, or other data, they are numbered beginning at 1. A range is a comma-separated list of numbers or spans (lq<i>first</i>&#8211;<i>last</i>rq). Ranges are XOR (exclusive or), so that lq1-5,3,7rq is equivalent to lq1,2,4,5,7rq. </p>
<p> <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> Turn on debugging output. Debugging output is written to stderr by default, or to the filename given to the <code>&#8211;debug-logfile</code> option.</dl>
<p> <code>&#8211;debug-logfile</code> <i>FILENAME</i> (since 2.3.0)</p>
<dl>
<dt>
<dd> The logfile to write the debugging info to, if <code>&#8211;debug</code> is given.</dl>
<p> <code>&#8211;hook-script</code> <i>FILENAME</i> (new after 2.3.0)</p>
<dl>
<dt>
<dd> Execute the hook script <i>FILENAME</i> every time a certain event happens within <code>gphoto2</code>. The hook script reads the environment variable <code>ACTION</code>. It must ignore <code>ACTION</code> values unknown to it. </p>
<p> <code>ACTION</code>=init</p>
<dl>
<dt>
<dd>
<p> <code>gphoto2</code> has just been initialized. If the hook script returns with a non-zero exit code now, <code>gphoto2</code> will abort.</dl>
<p> <code>ACTION</code>=start</p>
<dl>
<dt>
<dd>
<p> <code>gphoto2</code> has just finished parsing the command line and is about to start executing the commands given on the command line.</dl>
<p> <code>ACTION</code>=download</p>
<dl>
<dt>
<dd>
<p> <code>gphoto2</code> has just downloaded a file to the computer, storing it in the file indicated by the environment variable <code>ARGUMENT</code>.</dl>
<p> <code>ACTION</code>=stop</p>
<dl>
<dt>
<dd>
<p> <code>gphoto2</code> is about to finish. Do your final cleanups here.</dl>
<p> All other environment variables are passed to the hook script unchanged. You can make use of that to pass data to the hook script. </p>
<p> Hook script may be specified in the <i>~/.gphoto/settings</i> file as <code>gphoto2=hook-script=</code><i>filename</i>.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Quiet output (default=verbose).</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a short usage message.</dl>
<p> <code>&#8211;list-cameras</code></p>
<dl>
<dt>
<dd> List supported camera models.</dl>
<p> <code>&#8211;list-ports</code></p>
<dl>
<dt>
<dd> List supported port devices.</dl>
<p> <code>&#8211;stdout</code></p>
<dl>
<dt>
<dd> Send file to stdout.</dl>
<p> <code>&#8211;stdout-size</code></p>
<dl>
<dt>
<dd> Print filesize before data.</dl>
<p> <code>&#8211;auto-detect</code></p>
<dl>
<dt>
<dd> List auto-detected cameras and the ports to which they are connected.</dl>
<p> <code>&#8211;port</code> <i>PATH</i></p>
<dl>
<dt>
<dd> Specify port device. The <code>&#8211;list-ports</code> prints a list of valid, usable ports. In case of multiple USB cameras, the <code>&#8211;auto-detect</code> shows you the specific port each camera is connected to.</dl>
<p> <code>&#8211;speed</code> <i>SPEED</i></p>
<dl>
<dt>
<dd> Specify serial transfer speed.</dl>
<p> <code>&#8211;camera</code> <i>MODEL</i></p>
<dl>
<dt>
<dd> Specify camera model. The <code>&#8211;list-cameras</code> option prints a list of all explicitly supported cameras. </p>
<p> Most model names contain spaces: remember to enclose the name in quotes so that the shell knows it is one parameter. For example: <code>&#8211;camera</code><code> &quot;Kodak DC240&quot;</code>. </p>
<p> Note that if you specify <code>&#8211;camera</code>, you must also specify <code>&#8211;port</code>. Otherwise the <code>&#8211;camera</code> option will be silently ignored.</dl>
<p> <code>&#8211;filename</code> <i>FILENAME</i></p>
<dl>
<dt>
<dd> When downloading files from the camera, specify the file name or file name pattern to use when storing the downloaded file on the local disk. When uploading a file to the camera, specify the filename to store the uploaded file as on the camera. </p>
<p> The <code>&#8211;filename</code> option accepts %a, %A, %b, %B, %d, %H, %k, %I, %l, %j, %m, %M, %S, %y, %%, (see <a href="/docs/linux/man/1-date/">date</a>(1)) and, in addition, %n for the number, %C for the filename suffix, %f for the filename without suffix, %: for the complete filename in lowercase. </p>
<p> Note that %: is still in alpha stage, and the actual character or syntax may still be changed. E.g. it might be possible to use %#f and %#C for lower case versions, and %^f and %^C for upper case versions. </p>
<p> %n is the only conversion specifier to accept a padding character and width: %03n will pad with zeros to width 3 (e.g. print the number 7 as lq007rq). Leaving out the padding character (e.g. %3n) will use an implementation specific default padding character which may or may not be suitable for use in file names. </p>
<p> Default value for this option can be specified in the <i>~/.gphoto/settings</i> file as <code>gphoto2=filename=value</code>.</dl>
<p> <code>&#8211;usbid</code> <i>USBIDS</i></p>
<dl>
<dt>
<dd> (Expert only) Override USB IDs. <i> </i><i>USBIDS</i>must be of the form <i> </i><i>DetectedVendorID</i><i>:</i><i>DetectedProductID</i><i>=</i><i>TreatAsVendorID</i><i>:</i><i>TreatAsProductID</i> to treat any USB device detected as <i>DetectedVendorID</i><i>:</i><i>DetectedProductID</i> as <i>TreatAsVendorID</i><i>:</i><i>TreatAsProductID</i> instead. All the VendorIDs and ProductIDs should be hexadecimal numbers beginning in C notation, i.e. beginning with &#8216;0x&#8217;. </p>
<p> Example: <code>&#8211;usbid </code><i>0x4a9:0x306b=0x4a9:0x306c</i></dl>
<p> <code>-a</code>, <code>&#8211;abilities</code></p>
<dl>
<dt>
<dd> Display camera abilities.</dl>
<p> <code>-f</code>, <code>&#8211;folder</code> <i>FOLDER</i></p>
<dl>
<dt>
<dd> Specify camera folder (default=&quot;/&quot;).</dl>
<p> <code>-R</code>, <code>&#8211;recurse</code></p>
<dl>
<dt>
<dd> Recursion (default for download).</dl>
<p> <code>&#8211;no-recurse</code></p>
<dl>
<dt>
<dd> No recursion (default for deletion).</dl>
<p> <code>-l</code>, <code>&#8211;list-folders</code></p>
<dl>
<dt>
<dd> List folders in folder.</dl>
<p> <code>-L</code>, <code>&#8211;list-files</code></p>
<dl>
<dt>
<dd> List files in folder.</dl>
<p> <code>-m</code>, <code>&#8211;mkdir</code> <i>NAME</i></p>
<dl>
<dt>
<dd> Create a directory.</dl>
<p> <code>-r</code>, <code>&#8211;rmdir</code> <i>NAME</i></p>
<dl>
<dt>
<dd> Remove a directory.</dl>
<p> <code>-n</code>, <code>&#8211;num-files</code></p>
<dl>
<dt>
<dd> Display number of files.</dl>
<p> <code>-p</code>, <code>&#8211;get-file</code> <i>RANGE</i></p>
<dl>
<dt>
<dd> Get files given in range.</dl>
<p> <code>-P</code>, <code>&#8211;get-all-files</code></p>
<dl>
<dt>
<dd> Get all files from folder.</dl>
<p> <code>-t</code>, <code>&#8211;get-thumbnail</code> <i>RANGE</i></p>
<dl>
<dt>
<dd> Get thumbnails given in range.</dl>
<p> <code>-T</code>, <code>&#8211;get-all-thumbnails</code></p>
<dl>
<dt>
<dd> Get all thumbnails from folder.</dl>
<p> <code>&#8211;get-raw-data</code> <i>RANGE</i></p>
<dl>
<dt>
<dd> Get raw data given in range.</dl>
<p> <code>&#8211;get-all-raw-data</code></p>
<dl>
<dt>
<dd> Get all raw data from folder.</dl>
<p> <code>&#8211;get-audio-data</code> <i>RANGE</i></p>
<dl>
<dt>
<dd> Get audio data given in range.</dl>
<p> <code>&#8211;get-all-audio-data</code></p>
<dl>
<dt>
<dd> Get all audio data from folder.</dl>
<p> <code>&#8211;force-overwrite</code></p>
<dl>
<dt>
<dd> Overwrite files without asking.</dl>
<p> <code>&#8211;new</code></p>
<dl>
<dt>
<dd> Only get not already downloaded files. This option depends on camera support of flagging already downloaded images and is not available for all drivers.</dl>
<p> <code>-d</code>, <code>&#8211;delete-file</code> <i>RANGE</i></p>
<dl>
<dt>
<dd> Delete files given in range.</dl>
<p> <code>-D</code>, <code>&#8211;delete-all-files</code></p>
<dl>
<dt>
<dd> Delete all files in folder.</dl>
<p> <code>-u</code>, <code>&#8211;upload-file</code> <i>FILENAME</i></p>
<dl>
<dt>
<dd> Upload a file to camera.</dl>
<p> <code>&#8211;capture-preview</code></p>
<dl>
<dt>
<dd> Capture a quick preview.</dl>
<p> <code>-F </code><i>COUNT</i>, <code>&#8211;frames </code><i>COUNT</i></p>
<dl>
<dt>
<dd> Number of frames to capture in one run. Default is infinite number of frames.</dl>
<p> <code>-I </code><i>SECONDS</i>, <code>&#8211;interval </code><i>SECONDS</i></p>
<dl>
<dt>
<dd> Time between capture of multiple frames. </p>
<p> (Since 2.4) If SIGUSR1 signal is received, a picture is taken immediately without waiting for the end of the current interval period (see the section called lqSIGNALSrq). A value of -1 will let gphoto2 wait forever, i.e. until a signal arrives. See also <code>&#8211;reset-interval</code> (since 2.4).</dl>
<p> <code>&#8211;reset-interval</code> (since 2.4)</p>
<dl>
<dt>
<dd> Setting this option will reset the time interval to the value given by the <code>-I|&#8211;interval</code> option when a SIGUSR1 signal is received in time-lapse mode.</dl>
<p> <code>&#8211;capture-image</code></p>
<dl>
<dt>
<dd> Capture an image and keep it on the camera.</dl>
<p> <code>&#8211;capture-image-and-download</code></p>
<dl>
<dt>
<dd> Capture an image and download it immediately to the computer.</dl>
<p> <code>&#8211;capture-movie</code></p>
<dl>
<dt>
<dd> Capture a movie. (No driver supports this at this time.)</dl>
<p> <code>&#8211;capture-sound</code></p>
<dl>
<dt>
<dd> Capture an audio clip.</dl>
<p> <code>&#8211;capture-tethered</code></p>
<dl>
<dt>
<dd> Lets gphoto2 wait for notifications from the camera that an object was added. This is useful for tethered capture, where pressing the shutter on the camera immediately transfer the image to the machine for processing. </p>
<p> Together with the <code>&#8211;hook-script</code> to immediately postprocess or display the images this can help a studio workflow. </p>
<p> This option requires support in the driver and by the camera, currently newer Canon EOS and Nikon DSC are known to work.</dl>
<p> <code>&#8211;wait-event </code><i>SECONDS or COUNT</i>, <code>&#8211;wait-event-and-download </code><i>SECONDS or COUNT</i></p>
<dl>
<dt>
<dd> Lets gphoto2 wait for notifications from the camera for various things. This is useful for seeing what the camera does and waiting for objects to be added. The objects are kept on camera in the lq&#8211;wait-eventrq version, with lq&#8211;wait-event-and-downloadrq they are downloaded. </p>
<p> &#8211;wait-event-and-download is equivalent to &#8211;capture-tethered. </p>
<p> The time to wait can be either specified as full seconds with a &quot;s&quot; suffix, or as a number of events (just a number). If nothing happens, a timeout is generated after 1 second, so a lqwait-event=5rq will take at most 5 seconds. A lq&#8211;wait-event=5srq will take exactly 5 second. </p>
<p> If no argument is given, the wait time is 1 million events (basically forever). </p>
<p> In the download variant this can be used together with the <code>&#8211;hook-script</code> to immediately postprocess or display the images this can help a studio workflow. </p>
<p> This option requires support in the driver and by the camera, currently newer Canon EOS and Nikon DSC are known to work.</dl>
<p> <code>&#8211;show-info</code> <i>RANGE</i></p>
<dl>
<dt>
<dd> Show info.</dl>
<p> <code>&#8211;list-config</code></p>
<dl>
<dt>
<dd> List all configuration entries.</dl>
<p> <code>&#8211;get-config</code> <i>CONFIGENTRY</i></p>
<dl>
<dt>
<dd> Get the specified configuration entry. </p>
<p> This command will list the type, the current value and also the available options of this configuration value.</dl>
<p> <code>&#8211;set-config</code> <i>CONFIGENTRY=CONFIGVALUE</i></p>
<dl>
<dt>
<dd> Set the specified configuration entry. For lists of choices of values this setting first looks up CONFIGVALUE as value and then as index into the choice list. Since this is not fully clear, you can use <code>&#8211;set-config-index</code> or <code>&#8211;set-config-value</code> to be more clear what is searched for. </p>
<p> Look at the output of <code>&#8211;get-config</code> to see what values are possible to set here.</dl>
<p> <code>&#8211;set-config-index</code> <i>CONFIGENTRY=CONFIGINDEX</i></p>
<dl>
<dt>
<dd> Set the specified configuration entry by specifying the index into the list of choices for the configuration value. This of course only works for configuration settings that offer list of choices. </p>
<p> Look at the output of <code>&#8211;get-config</code> to see what indices are possible to set here.</dl>
<p> <code>&#8211;set-config-value</code> <i>CONFIGENTRY=CONFIGVALUE</i></p>
<dl>
<dt>
<dd> Set the specified configuration entry by specifying its new value. For lists of choices the value is looked up and set. </p>
<p> Look at the output of <code>&#8211;get-config</code> to see what indices are possible to set here.</dl>
<p> <code>&#8211;storage-info</code></p>
<dl>
<dt>
<dd> Display information about the camera&#8217;s storage media.</dl>
<p> <code>&#8211;summary</code></p>
<dl>
<dt>
<dd> Summary of camera status.</dl>
<p> <code>&#8211;manual</code></p>
<dl>
<dt>
<dd> Camera driver manual.</dl>
<p> <code>&#8211;about</code></p>
<dl>
<dt>
<dd> About the camera driver.</dl>
<p> <code>&#8211;shell</code></p>
<dl>
<dt>
<dd> Start the gphoto2 shell, an interactive environment. See SHELL MODEfor a detailed description.</dl>
<h2>SHELL MODE</h2>
<p> The following commands are available: </p>
<p> cd</p>
<dl>
<dt>
<dd> Change to a directory on the camera.</dl>
<p> ls</p>
<dl>
<dt>
<dd> List the contents of the current directory on the camera.</dl>
<p> lcd</p>
<dl>
<dt>
<dd> Change to a directory on the local machine.</dl>
<p> get</p>
<dl>
<dt>
<dd> Download the file to the current directory.</dl>
<p> get-thumbnail</p>
<dl>
<dt>
<dd> Download the thumbnail to the current directory.</dl>
<p> get-raw</p>
<dl>
<dt>
<dd> Download raw data to the current directory.</dl>
<p> show-info</p>
<dl>
<dt>
<dd> Show information.</dl>
<p> delete</p>
<dl>
<dt>
<dd> Delete a file or directory.</dl>
<p> mkdir <i>DIRECTORY</i></p>
<dl>
<dt>
<dd> Creates a directory named lqDIRECTORYrq.</dl>
<p> rmdir <i>DIRECTORY</i></p>
<dl>
<dt>
<dd> Removes a directory named lqDIRECTORYrq.</dl>
<p> show-exif</p>
<dl>
<dt>
<dd> Show EXIF information (only if compiled with EXIF support).</dl>
<p> capture-image</p>
<dl>
<dt>
<dd> Captures a single image and keeps it on the camera.</dl>
<p> capture-image-and-download</p>
<dl>
<dt>
<dd> Captures a single image and downloads it from the camera.</dl>
<p> list-config</p>
<dl>
<dt>
<dd> Lists all configuration values.</dl>
<p> get-config <i>NAME</i></p>
<dl>
<dt>
<dd> Gets the configuration specified by lqNAMErq.</dl>
<p> set-config <i>NAME=VALUE</i></p>
<dl>
<dt>
<dd> Sets the configuration specified by lqNAMErq to lqVALUErq.</dl>
<p> set-config-value <i>NAME=VALUE</i></p>
<dl>
<dt>
<dd> Sets the configuration specified by lqNAMErq to lqVALUErq.</dl>
<p> set-config-index <i>NAME=VALUE</i></p>
<dl>
<dt>
<dd> Sets the configuration specified by lqNAMErq to the lqINDEXrq into the list of choices. Works only for Menu or Radio button entries.</dl>
<p> wait-event <i>COUNT or SECONDS</i></p>
<dl>
<dt>
<dd> Waits for events from the camera for the specified time in SECONDS (if suffixed with s) or the COUNT of events from the camera, where every seconds a timeout event happens. Newly added images are kept on the camera. </p>
<p> Default is 1 event.</dl>
<p> wait-event-and-download <i>COUNT or SECONDS</i>, capture-tethered <i>COUNT or SECONDS</i></p>
<dl>
<dt>
<dd> Waits for events from the camera for the specified time in SECONDS (if suffixed with s) or the COUNT of events from the camera, where every seconds a timeout event happens. Newly added images are downloaded from the camera. </p>
<p> Default is 1 event.</dl>
<p> help, ?</p>
<dl>
<dt>
<dd> Displays command usage.</dl>
<p> exit, quit, q</p>
<dl>
<dt>
<dd> Exit the gphoto2 shell.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>CAMLIBS</code></p>
<dl>
<dt>
<dd> If set, defines the directory where the libgphoto2 library looks for its camera drivers (camlibs). You only need to set this on OS/2 systems and broken/test installations.</dl>
<p> <code>IOLIBS</code></p>
<dl>
<dt>
<dd> If set, defines the directory where the libgphoto2_port library looks for its I/O drivers (iolibs). You only need to set this on OS/2 systems and broken/test installations.</dl>
<p> <code>LD_DEBUG</code></p>
<dl>
<dt>
<dd> Set this to <i>all</i> to receive lots of debug information regarding library loading on <code>ld</code> based systems.</dl>
<p> <code>USB_DEBUG</code></p>
<dl>
<dt>
<dd> If set, defines the numeric debug level with which the libusb library will print messages. In order to get some debug output, set it to <i>1</i>.</dl>
<h2>SIGNALS</h2>
<p> SIGUSR1 (since 2.4)</p>
<dl>
<dt>
<dd> In time-lapse capture mode, receiving a SIGUSR1 signal makes gphoto2 take a picture immediately. </p>
<p> If the <code>&#8211;reset-interval</code> option is given, the time counter is reset to the value given by the <code>-I|&#8211;interval</code> option. Note that the camera will need some time (from 50ms to a few seconds) to actually capture the image.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-libgphoto2/">libgphoto2</a>(3), <i>The gPhoto2 Manual</i>[1], </p>
<p> <i>The gphoto.org website</i>[2], <i>Digital Camera Support for UNIX, Linux and BSD</i>[3]</p>
<h2>EXAMPLES</h2>
<p> <code>gphoto2 </code><code>&#8211;list-ports</code></p>
<dl>
<dt>
<dd> Shows what kinds of ports (USB and serial) you have.</dl>
<p> <code>gphoto2 </code><code>&#8211;auto-detect</code></p>
<dl>
<dt>
<dd> Shows what camera(s) you have connected.</dl>
<p> <code>gphoto2 </code><code>&#8211;list-files</code></p>
<dl>
<dt>
<dd> List files on camera.</dl>
<p> <code>gphoto2 </code><code>&#8211;get-file</code><i>7-13</i></p>
<dl>
<dt>
<dd> Get files number 7 through 13 from the list output by <code>gphoto2</code><code>&#8211;list-files</code>.</dl>
<p> <code>gphoto2 </code><code>&#8211;capture-image</code><code>&#8211;interval</code><i>60</i><code>&#8211;hook-script</code><i>/usr/share/doc/gphoto2/test-hook.sh</i></p>
<dl>
<dt>
<dd> Capture one image every 60 seconds from now to eternity. The example hook script will be called after each captured image has been stored on the computer.</dl>
<p> To track down errors, you can add the <code>&#8211;debug</code> parameter to the <code>gphoto2</code> command line and, if dealing with USB problems, setting the environment variable <code>USB_DEBUG</code><i>=1</i>.</p>
<h2>AUTHORS</h2>
<p> <code>Tim Waugh</code> </p>
<dl>
<dt>
<dd> Author.</dl>
<p> <code>Hans Ulrich Niedermann, current maintainer</code> &lt;gp [at] n-dimensional.de&gt; </p>
<dl>
<dt>
<dd> Author.</dl>
<p> <code>Michael J. Rensing</code> </p>
<dl>
<dt>
<dd> Author.</dl>
<p> <code>Miscellanous Contributors.</code> </p>
<p> <code>The gPhoto2 Team</code> </p>
<dl>
<dt>
<dd> Author.</dl>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt; </p>
<dl>
<dt>
<dd> Original man page author.</dl>
<p> <code>Hans Ulrich Niedermann</code> &lt;gp [at] n-dimensional.de&gt; </p>
<dl>
<dt>
<dd> Current man page editor.</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> The gPhoto2 Manual</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.gphoto.org/doc/manual/">http://www.gphoto.org/doc/manual/</a></dl>
<dt> 2.</p>
<dd> The gphoto.org website</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.gphoto.org/">http://www.gphoto.org/</a></dl>
<dt> 3.</p>
<dd> Digital Camera Support for UNIX, Linux and BSD</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.teaser.fr/~hfiguiere/linux/digicam.html">http://www.teaser.fr/~hfiguiere/linux/digicam.html</a></dl>
</dl>
<h2>Index</h2>
