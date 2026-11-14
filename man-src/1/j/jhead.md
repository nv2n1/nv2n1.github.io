---
title: "jhead(1)"
name: "jhead"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jhead/"
description: "jhead – Digicam JPEG Exif header manipulation tool"
---

<h2>NAME</h2>
<p> jhead &#8211; Digicam JPEG Exif header manipulation tool</p>
<h2>SYNOPSIS</h2>
<p> <code>jhead</code> [ <i>options</i> ] [ <i>file&#8230;</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>jhead</code> is used to display and manipulate data contained in the Exif header of JPEG images from digital cameras. By default, jhead displays the more useful camera settings from the file in a user-friendly format. </p>
<p> <code>jhead</code> can also be used to manipulate some aspects of the image relating to JPEG and Exif headers, such as changing the internal timestamps, removing the thumbnail, or transferring Exif headers back into edited images after graphical editors deleted the Exif header. <code>jhead</code> can also be used to launch other programs, similar in style to the UNIX <code>find</code> command, but much simpler. </p>
<h2>GENERAL METADATA OPTIONS</h2>
<dl>
<dt><code>-te</code><i>&nbsp;<wbr>file</i></p>
<dd> Transplant Exif header from a JPEG (with Exif header) in <i>file</i> into the image that is manipulated. This option is useful if you like to edit the photos but still want the Exif header on your photos. As most photo editing programs will wipe out the Exif header, this option can be used to re-copy them back from original copies after editing the photos. </p>
<p> This feature has an interesting &#8216;relative path&#8217; option for specifying the thumbnail name. Whenever the &lt;name&gt; contains the characters &#8216;&amp;i&#8217;, will substitute the original filename for this name. This allows creating a jhead &#8216;relative name&#8217; when doing a whole batch of files. For example, the incantation: </p>
<p> <i>jhead -te originals/&amp;i *.jpg</i> </p>
<p> would transfer the exif header for each .jpg file in the originals directory by the same name, Both Win32 and most Unix shells treat the &#8216;&amp;&#8217; character in a special way, so you have to put quotes around that command line option for the &#8216;&amp;&#8217; to even be passed to the program. </p>
<dt><code>-dc</code></p>
<dd> Delete comment field from the JPEG header. Note that the comment is not part of the Exif header.</p>
<dt><code>-de</code></p>
<dd> Delete the Exif header entirely. Leaves other metadata sections intact.</p>
<dt><code>-di</code></p>
<dd> Delete the IPTC section, if present. Leaves other metadata sections intact.</p>
<dt><code>-dx</code></p>
<dd> Delete the XMP section, if present. Leaves other metadata sections intact.</p>
<dt><code>-du</code></p>
<dd> Delete sections of jpeg that are not Exif, not comment, and otherwise not contributing to the image either &#8211; such as data that photoshop might leave in the image.</p>
<dt><code>-purejpg</code></p>
<dd> Delete all JPEG sections that aren&#8217;t necessary for rendering the image. Strips any metadata that various applications may have left in the image. A combination of the -de -dc and -du options.</p>
<dt><code>-mkexif</code></p>
<dd> Creates minimal exif header. Exif header contains date/time, and empty thumbnail fields only. Date/time set to file time by default. Use with -rgt option if you want the exif header to contain a thumbnail. Note that exif header creation is very limited at this time, and no other fields can be added to the exif header this way.</p>
<dt><code>-ce</code></p>
<dd> Edit the JPEG header comment field (note, this comment field is outside the Exif structure and can be part of Exif and non Exif style JPEG images). </p>
<p> A temporary file containing the comment is created and a text editor is launched to edit the file. The editor is specified in the EDITOR environment variable. If none is specified notepad or vi are used under Windows and Unix respectively. After the editor exits, the data is transferred back into the image, and the temporary file deleted.</p>
<dt><code>-cs</code><i>&nbsp;<wbr>file</i></p>
<dd> Save comment section to a <i>file</i></p>
<dt><code>-ci</code><i>&nbsp;<wbr>file</i></p>
<dd> Replace comment with text from <i>file</i></p>
<dt><code>-cl</code><i>&nbsp;<wbr>string</i></p>
<dd> Replace comment with specified string from command line <i>file</i> </p>
</dl>
<h2>DATE / TIME MANIPULATION OPTIONS</h2>
<dl>
<dt><code>-ft</code></p>
<dd> Sets the file&#8217;s system time stamp to what is stored in the Exif header.</p>
<dt><code>-dsft</code></p>
<dd> Sets the Exif timestamp to the file&#8217;s timestamp. Requires an Exif header to pre-exist. Use -mkexif option to create one if needed.</p>
<dt><code>-n</code><i>[format_string]</i></p>
<dd> This option causes files to be renamed and/ or mmoved using the date information from the Exif header &quot;DateTimeOriginal&quot; field. If the file is not an Exif file, or the DateTimeOriginal does not contain a valid value, the file date is used. Renaming is by default restricted to files whose names consist largely of digits. This effectively restricts renaming to files that have not already been manually renamed, as the default sequential names from digital cameras consist largely of digits. Use the <code>-n</code> option to force renaming of all files. If the new name contains a &#8216;/&#8217;, this will be interpreted as a new path, and the file will be moved accordingly.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> If the <i>format_string</i> is omitted, the file will be renamed to MMDD-HHMMSS. Note that this scheme doesn&#8217;t include the year (I never have photos from different years together anyway). </p>
<p> If a <i>format_string</i> is provided, it will be passed to the strftime function as the format string. In addition, if the format string contains &#8216;%f&#8217;, this will substitute the original name of the file (minus extension). &#8216;%i&#8217; will substitute a sequence number. Leading zeros can be specified like with printf &#8211; i.e. &#8216;%04i&#8217; pads the number to 4 digits using leading zeros. </p>
<p> If the name includes &#8216;/&#8217;, this is interpreted as a new path for the file. If the new path does not exist, the path will be created. </p>
<p> If the target name already exists, the name will be appended with &quot;a&quot;, &quot;b&quot;, &quot;c&quot;, etc, unless the name ends with a letter, in which case it will be appended with &quot;0&quot;, &quot;1&quot;, &quot;2&quot;, etc. </p>
<p> This feature is especially useful if more than one digital camera was used to take pictures of an event. By renaming them to a scheme according to date, they will automatically appear in order of taking in most directory listings and image browsers. Alternatively, if your image browser supports listing by file time, you can use the -ft option to set the file time to the time the photo was taken. </p>
<p> Some of the more useful arguments for strftime are: </p>
<p> <code>%H</code>&nbsp;<wbr>Hour in 24-hour format&nbsp;<wbr>(00 &#8211; 23)<br />
 <code>%j</code>&nbsp;<wbr>Day of year as decimal number&nbsp;<wbr>(001 &#8211; 366)<br />
 <code>%m</code>&nbsp;<wbr>Month as decimal number&nbsp;<wbr>(01 &#8211; 12)<br />
 <code>%M</code>&nbsp;<wbr>Minute as decimal number&nbsp;<wbr>(00 &#8211; 59)<br />
 <code>%S</code>&nbsp;<wbr>Second as decimal number&nbsp;<wbr>(00 &#8211; 59)<br />
 <code>%w</code>&nbsp;<wbr>Weekday as decimal number&nbsp;<wbr>(0 &#8211; 6;&nbsp;<wbr>Sunday is 0)<br />
 <code>%y</code>&nbsp;<wbr>Year without century, as decimal number&nbsp;<wbr>(00 &#8211; 99)<br />
 <code>%Y</code>&nbsp;<wbr>Year with century, as decimal number </p>
<p> Example: </p>
<p> <i>jhead -n%Y%m%d-%H%M%S *.jpg</i> </p>
<p> This will rename files matched by *.jpg in the format YYYYMMDD-HHMMSS </p>
<p> For a full listing of strftime arguments, look up the strftime in them man pages. Note that some arguments to the strftime function (not listed here) produce strings with characters such as &#8216;:&#8217; that may not be valid as part of a filename on some systems. </p>
<dt><code>-ta&lt;+|-&gt;&lt;timediff&gt;</code></p>
<dd> Adjust time stored in the Exif header by h:mm forwards or backwards. Useful when having taken pictures with the wrong time set on the camera, such as after travelling across time zones, or when daylight savings time has changed. </p>
<p> Examples: </p>
<p> Add 1 hourand 5 minutes to the time<br />
 jhead -ta+1:05 </p>
<p> Decrease time by one second:<br />
 jhead -ta-0:0:1 </p>
<p> This option changes all Date/time fields in the exif header, including &quot;DateTimeOriginal&quot; (tag 0x9003) and &quot;DateTimeDigitized&quot; (tag 0x9004).</p>
<dt><code>-da&lt;newdate&gt;-&lt;olddate&gt;</code></p>
<dd>
<p> Works like -ta, but for specifying large date offsets, to be used when fixing dates from cameras where the date was set incorrectly, such as having date and time reset by battery removal on some cameras </p>
<p> Because different months and years have different numbers of days in them, a simple offset for months, days, years would lead to unexpected results at times. The time offset is thus specified as a difference between two dates, so that jhead can figure out exactly how many days the timestamp needs to be adjusted by, including leap years and daylight savings time changes. The dates are specified as yyyy:mm:dd. For sub-day adjustments, a time of day can also be included, by specifying yyyy:nn:dd/hh:mm or yyyy:mm:dd/hh:mm:ss </p>
<p> Examples: </p>
<p> Year on camera was set to 2005 instead of 2004 for pictures taken in April<br />
 jhead -da2004:03:01-2005:03:01 </p>
<p> Default camera date is 2002:01:01, and date was reset on 2005:05:29 at 11:21 am<br />
 jhead -da2005:05:29/11:21-2002:01:01</p>
<dt><code>-ts</code></p>
<dd> Sets the time stored in the Exif header to what is specified on the command line. Time must be specified as: <i>yyyy:mm:dd-hh:mm:ss</i></p>
<dt><code>-ds</code></p>
<dd> Sets the date stored in the Exif header to what is specified on the command line. Can be used to set date, just year and month, or just year. Date is specified as: <i>yyyy:mm:dd, yyyy:mm, or yyyy</i> </p>
</dl>
<h2>THUMBNAIL MANIPULATION OPTIONS</h2>
<dl>
<dt><code>-dt</code></p>
<dd> Delete thumbnails from the Exif header, but leave the interesting parts intact. This option truncates the thumbnail from the Exif header, provided that the thumbnail is the last part of the Exif header (which so far as I know is always the case). Exif headers have a built-in thumbnail, which typically occupies around 10k of space. This thumbnail is used by digital cameras. Windows XP may also use this thumbnail if present (but it doesn&#8217;t need it). The thumbnails are too small to use even full screen on the digicam&#8217;s LCD. I have not encountered any adverse side effects of deleting the thumbnails, even from the software provided with my old Olympus digicam. Use with caution. </p>
<dt><code>-st</code><i>&nbsp;<wbr>file</i></p>
<dd> Save the integral thumbnail to <i>file</i> The thumbnail lives inside the Exif header, and is a very low-res JPEG image. Note that making any changes to a photo, except for with some programs, generally wipes out the Exif header and with it the thumbnail. </p>
<p> The thumbnail is too low res to really use for very much. </p>
<p> This feature has an interesting &#8216;relative path&#8217; option for specifying the thumbnail name. Whenever the name for <i>file</i> contains the characters &#8216;&amp;i&#8217;, <code>jhead</code> will substitute the original filename for this name. This allows creating a &#8216;relative name&#8217; when doing a whole batch of files. For example, the incantation: </p>
<p> <i>jhead -st thumbnails/&amp;i *.jpg</i> </p>
<p> would create a thumbnail for each .jpg file in the thumbnails directory by the same name, (provided that the thumbnails directory exists, of course). Both Win32 and UNIX shells treat the &#8216;&amp;&#8217;character in a special way, so you have to put quotes around that command line option for the &#8216;&amp;&#8217; to even be passed to the program. </p>
<p> If a &#8216;-&#8216; is specified for the output file, the thumbnail is sent to stdout. (UNIX build only) </p>
<dt><code>-rt</code></p>
<dd> Replace thumbnails from the Exif header. This only works if the exif header already contains a thumbnail, and the thumbnail is at the end of the header (both always the case if the photo came from a digital camera)</p>
<dt><code>-rgt</code><i>&nbsp;<wbr>size</i></p>
<dd> Regenerate exif thumbnail. &#8216;size&#8217; specifies maximum height or width of thumbnail. Relies on &#8216;mogrify&#8217; program (from ImageMagick) to regenerate the thumbnail. This only works if the image already contains a thumbnail. </p>
</dl>
<h2>ROTATION OPTIONS</h2>
<dl>
<dt><code>-autorot</code></p>
<dd> Using the &#8216;Orientation&#8217; tag of the Exif header, rotate the image so that it is upright. The program <code>jpegtran</code> is used to perform the rotation. This program is present in most Linux distributions. For windows, you need to get a copy of it. After rotation, the orientation tag of the Exif header is set to &#8216;1&#8217; (normal orientation). The thumbnail is also rotated. Other fields of the Exif header, including dimensions are untouched, but the JPEG height/width are adjusted. This feature is especially useful with newer Canon cameras, that set the orientation tag automatically using a gravity sensor.</p>
<dt><code>-norot</code></p>
<dd> Clears the rotation field in the Exif header without altering the image. Useful if the images were previously rotated without clearing the Exif rotation tag, as some image browsers will auto rotate images when the rotation tag is set. Sometimes, thumbnails and rotation tags can get very out of sync from manipulation with various tools. To reset it all use -norot with -rgt to clear this out. </p>
</dl>
<h2>OUTPUT VERBOSITY CONTROL</h2>
<dl>
<dt><code>-h</code></p>
<dd> Displays summary of command line options.</p>
<dt><code>-v</code></p>
<dd> Makes the program even more verbose than it already is. Like DOS programs, and unlike UNIX programs, Jhead gives feedback as to what it is doing, even when nothing goes wrong. Windows user that I am, when something doesn&#8217;t give me feedback for 20 seconds, I assume its crashed.</p>
<dt><code>-q</code></p>
<dd> No output on success, more like Unix programs.</p>
<dt><code>-V</code></p>
<dd> Print version info and compilation date. <code>-exifmap</code> Show a map of the bytes in the exif header. Useful when analyzing strange exif headers, not of much use to non software developers.</p>
<dt><code>-se</code></p>
<dd> Suppress error messages relating to corrupt Exif header structure.</p>
<dt><code>-c</code></p>
<dd> Concise output. This causes picture info to be summarized on one line instead of several. Useful for grep-ing through images, as well as importing into spread sheets (data is space delimited with quotes as text qualifier). </p>
</dl>
<h2>FILE MATCHING OPTIONS</h2>
<dl>
<dt><code>-model</code></p>
<dd> Restricts processing of files to those whose camera model, as indicated by the Exif image information, contains the substring specified in the argument after &#8216;-model&#8217;. For example, the following command will list only images that are from an S100 camera: </p>
<p> <i>jhead -model S100 *.jpg</i> </p>
<p> I use this option to restrict my JPEG recompensing to those images that came from my Canon S100 digicam, (see the -cmd option).</p>
<dt><code>-exonly</code></p>
<dd> Skip all files that don&#8217;t have an Exif header. Photos straight from a digital camera have an Exif header, whereas many photo manipulation tools discard the Exif header.</p>
<dt><code>-cmd</code></p>
<dd> Executes the specified command on each JPEG file to be processed. </p>
<p> The Exif section of each file is read before running the command, and reinserted after the command finishes. </p>
<p> The specified command invoked separately for each JPEG that is processed, even if multiple files are specified (explicitly or by wild card). </p>
<p> Example use: </p>
<p> Having a whole directory of photos from my S100, I run the following commands: </p>
<p> <i>jhead -cmd mogrify -quality 80 &amp;i -model S100 *.jpg</i><br />
 <i>jhead -cmd jpegtran -progressive &amp;i &gt; &amp;o *.jpg</i> </p>
<p> The first command mogrifies all JPEGs in the tree that indicate that they are from a Canon S100 in their Exif header to 80% quality at the same resolution. This is a &#8216;lossy&#8217; process, so I only run it on files that are from the Canon, and only run it once. The next command then takes a JPEGs and converts them to progressive JPEGs. The result is the same images, with no discernible differences, stored in half the space. This produces substantial savings on some cameras. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></code>(1), <code><a href="/docs/linux/man/1-mogrify/">mogrify</a></code>(1), <code><a href="/docs/linux/man/1-rdjpgcom/">rdjpgcom</a></code>(1), <code><a href="/docs/linux/man/1-wrjpgcom/">wrjpgcom</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Matthias Wandel</p>
<h2>BUGS</h2>
<p> After jhead runs a program to rotate or resize an image, the image dimensions and thumbnail in the Exif header are not adjusted. </p>
<p> Modifying of Exif header data is very limited, as Jhead internally only has a read only implementation of the file system contained in the Exif header. For example, there is no way to replace the thumbnail or edit the Exif comment in the Exif header. There is also no way to create minimal exif headers. </p>
<p> Some Canon digital SLR cameras fail to adjust the effective sensor resolution when shooting at less than full resolution, causing jhead to incorrectly miscalculate the sensor width and 35mm equivalent focal length. The same can result from resizing photos with Photoshop, which will manipulate parts of the exif header. This is often reported as a bug in Jhead, but Jhead can&#8217;t do much about incorrect data. </p>
<p> Send bug reports to mwandel at sentex dot net. </p>
<h2>COPYING PERMISSIONS</h2>
<p> Jhead is &#8216;public domain&#8217;. You may freely copy jhead, and reuse part or all of its code in free or proprietary programs. I do however request that you do not post my e-mail address in ways that spam robots can harvest it. </p>
<h2>Index</h2>
