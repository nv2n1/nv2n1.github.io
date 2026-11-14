---
title: "motion(1)"
name: "motion"
section: "1"
letter: "m"
url: "/docs/linux/man/1-motion/"
description: "motion – Detect motion using a video4linux device"
---

<h2>NAME</h2>
<p> motion &#8211; Detect motion using a video4linux device</p>
<h2>SYNOPSIS</h2>
<p> <code>motion</code> [ -hmns ] [ -c config file path ] [ -d log level ] [ -k log type ] [ -p process_id_file ] [ -l logfile ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Motion</i> uses a video4linux device to detect motion. If motion is detected both normal and motion pictures will be taken. Motion can also take actions to notify you if needed. Creation of automated snapshots is also possible.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Full path and filename of config file. E.g. /home/kurt/motion.conf. Default is /usr/local/etc unless specified differently when building Motion. Many RPMs and debian packages will most likely use /etc or /etc/motion as default.</p>
<dt><code>-h</code></p>
<dd> Show help screen.</p>
<dt><code>-m</code></p>
<dd> Disable motion detection at startup.</p>
<dt><code>-n</code></p>
<dd> Run in non-daemon mode.</p>
<dt><code>-s</code></p>
<dd> Run in setup mode. Also forces non-daemon mode</p>
<dt><code>-d log level</code></p>
<dd> Set log level [1..9] (EMR, ALR, CRT, ERR, WRN, NTC, INF, DBG, ALL). (default: 6 / NTC)</p>
<dt><code>-k log type</code></p>
<dd> Set type of log (COR, STR, ENC, NET, DBL, EVT, TRK, VID, ALL). (default: ALL)</p>
<dt><code>-p</code></p>
<dd> Full path and filename for process id file (pid file). E.g /var/run/motion.pid. Default is not defined. Pid file is only created when Motion is started in daemon mode.</p>
<dt><code>-l</code></p>
<dd> Full path and filename of log file. ( use -l syslog to log to stderr and syslog )</p>
<dt></dl>
<h2>CONFIG FILE OPTIONS</h2>
<dd> These are the options that can be used in the config file. <i>They are overridden by the commandline!</i> All number values are integer numbers (no decimals allowed). Boolean options can be on or off (values &quot;1&quot;, &quot;yes&quot; and &quot;on&quot; all means true and any other value means false).</p>
<dl>
<dt><code>area_detect integer</code></p>
<dd> Values: 0 &#8211; 999999999 / Default: Not defined<br />
 Detect motion in predefined areas (1 &#8211; 9). Areas are numbered like that: 1 2 3<br />
 A script (on_area_detected) is started immediately when motion is 4 5 6<br />
 detected in one of the given areas, but only once during an event. 7 8 9<br />
 One or more areas can be specified with this option. Take care: This option does NOT restrict detection to these areas! (Default: not defined)</p>
<dt><code>auto_brightness boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Let motion regulate the brightness of a video device. Only recommended for cameras without auto brightness</p>
<dt><code>brightness integer</code></p>
<dd> Values: 0 &#8211; 255 / Default: 0 (disabled)<br />
 The brightness level for the video device.</p>
<dt><code>contrast boolean</code></p>
<dd> Values: 0 &#8211; 255 / Default: 0 (disabled)<br />
 The contrast level for the video device.</p>
<dt><code>daemon boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Start in daemon (background) mode and release terminal. This option must be placed in motion.conf and not in a thread config file.</p>
<dt><code>database_dbname string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 Name of the database.</p>
<dt><code>database_host string</code></p>
<dd> Values: Max 4095 characters / Default: localhost<br />
 IP address or domain name for the database server. Use &quot;localhost&quot; if motion and database runs on the same server.</p>
<dt><code>database_password string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 The database password.</p>
<dt><code>database_port integer</code></p>
<dd> Values: 0 &#8211; 65535 / Default: Not defined<br />
 The database server port number.</p>
<dt><code>database_type discrete strings</code></p>
<dd> Values: mysql, postgresql / Default: Not defined<br />
 The database type ( mysql , postgresql ).</p>
<dt><code>database_user string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 The database user name.</p>
<dt><code>despeckle_filter string</code></p>
<dd> Values: EedDl / Default: Not defined<br />
 Despeckle motion image using combinations of (E/e)rode or (D/d)ilate. And ending with optional (l)abeling.</p>
<dt><code>emulate_motion boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Picture are saved continuously as if motion was detected all the time.</p>
<dt><code>event_gap integer</code></p>
<dd> Values: 0 &#8211; 2147483647 / Default: 60<br />
 Event Gap is the seconds of no motion detection that triggers the end of an event. An event is defined as a series of motion images taken within a short timeframe.</p>
<dt><code>exif_text string </code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 Text to include in a JPEG EXIF comment , may be any text, including conversion specifiers. The EXIF timestamp is included independent of this text.</p>
<dt><code>extpipe string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 pipe raw video to generally &#8211; &#8216;STDIN&#8217;, allowing to use an external video encoder.<br />
 e.g. using memcoder :<br />
 extpipe mencoder -demuxer rawvideo -rawvideo w=320:h=240:i420 -ovc x264 -x264encopts bframes=4:frameref=1:subq=1:scenecut=-1:nob_adapt: threads=1:keyint=1000:8x8dct:vbv_bufsize=4000:crf=24:partitions=i8x8,i4x4:vbv_maxrate=800:no-chroma-me -vf denoise3d=16:12:48:4,pp=lb -of avi -o %f.avi &#8211; -fps %fps</p>
<dt><code>ffmpeg_bps integer</code></p>
<dd> Values: 0 &#8211; 9999999 / Default: 400000<br />
 Bitrate of movies produced by ffmpeg. Bitrate is bits per second. Default: 400000 (400kbps). Higher value mans better quality and larger files. Option requires that ffmpeg libraries are installed.</p>
<dt><code>ffmpeg_output_debug_movies boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Use ffmpeg libraries to encode motion type movies where you only see the pixels that changes.</p>
<dt><code>ffmpeg_output_movies boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Use ffmpeg libraries to encode movies in realtime.</p>
<dt><code>ffmpeg_deinterlace boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Use ffmpeg to deinterlace video. Necessary if you use an analog camera and see horizontal combing on moving objects in video or pictures.</p>
<dt><code>ffmpeg_timelapse integer</code></p>
<dd> Values: 0 &#8211; 2147483647 / Default: 0 (disabled)<br />
 Create a timelapse movie saving a picture frame at the interval in seconds set by this parameter. Set it to 0 if not used.</p>
<dt><code>ffmpeg_timelapse_mode discrete strings</code></p>
<dd> Values: hourly, daily, weekly-sunday, weekly-monday, monthly, manual / Default: daily<br />
 The file rollover mode of the timelapse video.</p>
<dt><code>ffmpeg_variable_bitrate integer</code></p>
<dd> Values: 0, 2 &#8211; 31 / Default: 0 (disabled)<br />
 Enables and defines variable bitrate for the ffmpeg encoder. ffmpeg_bps is ignored if variable bitrate is enabled. Valid values: 0 (default) = fixed bitrate defined by ffmpeg_bps, or the range 2 &#8211; 31 where 2 means best quality and 31 is worst.</p>
<dt><code>ffmpeg_video_codec discrete strings</code></p>
<dd> Values: mpeg1 (ffmpeg-0.4.8 only), mpeg4, msmpeg4, swf , flv , ffv1, mov, ogg / Default: mpeg4<br />
 Codec to be used by ffmpeg for the video compression. Timelapse movies are always made in mpeg1 format independent from this option.</p>
<dt><code>framerate integer</code></p>
<dd> Values: 2 &#8211; 100 / Default: 100 (no limit)<br />
 Maximum number of frames to be captured from the camera per second.</p>
<dt><code>frequency integer</code></p>
<dd> Values: 0 &#8211; 999999 / Default: 0 (Not set)<br />
 The frequency to set the tuner to (kHz). Valid range: per tuner spec, default: 0 (Don&#8217;t set it)</p>
<dt><code>height integer</code></p>
<dd> Values: Device Dependent / Default: 288<br />
 The height of each frame in pixels.</p>
<dt><code>hue integer</code></p>
<dd> Values: 0 &#8211; 255 / Default: 0 (disabled)<br />
 The hue level for the video device.</p>
<dt><code>input integer</code></p>
<dd> Values: -1 &#8211; 64, -1 = disabled / Default: -1 (disabled)<br />
 Input channel to use expressed as an integer number starting from -1. Should normally be set to 1 for video/TV cards, and -1 for USB cameras.</p>
<dt><code>ipv6_enabled boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Enable or disable IPV6 for http control and stream.</p>
<dt><code>lightswitch integer</code></p>
<dd> Values: 0 &#8211; 100 / Default: 0 (disabled)<br />
 Ignore sudden massive light intensity changes given as a percentage of the picture area that changed intensity.</p>
<dt><code>locate_motion discrete strings</code></p>
<dd> Values: on, off, redbox, center, redcross, preview / Default: off<br />
 Locate and draw a box around the moving object. Value &#8216;preview&#8217; makes Motion only draw a box on a saved preview jpeg image and not on the saved movie.</p>
<dt><code>logfile string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 Use a file to save logs messages, if not defined stderr and syslog is used.</p>
<dt><code>logfile string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 Use a file to save logs messages, if not defined stderr and syslog is used. ( if syslog is set then will log to stderr and syslog )</p>
<dt><code>log_level integer</code></p>
<dd> Values: 1 &#8211; 9 / Default: 6<br />
 Level of log messages [1..9] (EMR, ALR, CRT, ERR, WRN, NTC, ERR, DBG, ALL). (default: 6 / NTC).</p>
<dt><code>log_type discrete strings</code></p>
<dd> Values: STR, ENC, NET, DBL, EVT, TRK, VID, ALL / Default: ALL<br />
 Filter to log messages by type (STR, ENC, NET, DBL, EVT, TRK, VID, ALL).</p>
<dt><code>mask_file string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 PGM file to use as a sensitivity mask. This picture MUST have the same width and height as the frames being captured and be in binary format.</p>
<dt><code>max_movie_time integer</code></p>
<dd> Values: 0 (infinite) &#8211; 2147483647 / Default: 3600<br />
 The maximum length of a movie in seconds. Set this to zero for unlimited length.</p>
<dt><code>minimum_frame_time integer</code></p>
<dd> Values: 0 &#8211; 2147483647 / Default: 0<br />
 Minimum time in seconds between the capturing picture frames from the camera. Default: 0 = disabled &#8211; the capture rate is given by the camera framerate.</p>
<dt><code>minimum_motion_frames integer</code></p>
<dd> Values: 1 &#8211; 1000s / Default: 1<br />
 Picture frames must contain motion at least the specified number of frames in a row before they are detected as true motion. At the default of 1, all motion is detected. Valid range is 1 to thousands, but it is recommended to keep it within 1-5.</p>
<dt><code>motion_video_pipe string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 The video4linux video loopback input device for motion images. If a particular pipe is to be used then use the device filename of this pipe, if a dash &#8216;-&#8216; is given motion will use /proc/video/vloopback/vloopbacks to locate a free pipe. Default: not set</p>
<dt><code>movie_filename string</code></p>
<dd> Values: Max 4095 characters / Default: %v-%Y%m%d%H%M%S<br />
 File path for motion triggered ffmpeg movies relative to target_dir. This was previously called ffmpeg_filename.</p>
<dt><code>netcam_tolerant_check boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Set less strict jpeg checks for network cameras with a poor/buggy firmware.</p>
<dt><code>netcam_keepalive discrete string</code></p>
<dd> Values: off , force, on / Default: off<br />
 The setting for keep-alive of network socket, should improve performance on compatible net cameras.</p>
<dt><code>netcam_proxy string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 URL to use for a netcam proxy server, if required. The syntax is <a rel="nofollow" href="http://myproxy:portnumber">http://myproxy:portnumber</a></p>
<dt><code>netcam_url string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 Specify an url to a downloadable jpeg file or raw mjpeg stream to use as input device. Such as an AXIS 2100 network camera.<br />
 http:// ftp:// mjpg:// or file:/// ( mjpg:// is for network cameras with codec mjpeg ).</p>
<dt><code>netcam_userpass string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 For network cameras protected by username and password, use this option for HTTP 1.1 Basic authentication. The string is specified as username:password. Do not specify this option for no authentication.</p>
<dt><code>noise_level integer</code></p>
<dd> Values: 1 &#8211; 255 / Default: 32<br />
 The noise level is used as a threshold for distinguishing between noise and motion.</p>
<dt><code>noise_tune boolean</code></p>
<dd> Values: on, off / Default: on<br />
 Activates the automatic tuning of noise level.</p>
<dt><code>norm integer</code></p>
<dd> Values: 0 (PAL), 1 (NTSC), 2 (SECAM), 3 (PAL NC no colour) / Default: 0 (PAL)<br />
 Select the norm of the video device. Values: 0 (PAL), 1 (NTSC), 2 (SECAM), 3 (PAL NC no colour). Default: 0 (PAL)</p>
<dt><code>on_area_detected string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 Command to be executed when motion in a predefined area is detected, check option area_detect.</p>
<dt><code>on_camera_lost</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 Command to be executed when a camera can&#8217;t be opened or if it is lost. You can use Conversion Specifiers and spaces as part of the command. Use %f for passing filename (with full path) to the command.</p>
<dt><code>on_event_end string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 Command to be executed when an event ends after a period of no motion. The period of no motion is defined by option event_gap. You can use Conversion Specifiers and spaces as part of the command.</p>
<dt><code>on_event_start string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 Command to be executed when an event starts. An event starts at first motion detected after a period of no motion defined by event_gap. You can use ConversionSpecifiers and spaces as part of the command.</p>
<dt><code>on_motion_detected string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 Command to be executed when a motion frame is detected. You can use Conversion Specifiers and spaces as part of the command.</p>
<dt><code>on_movie_end string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 Command to be executed when an ffmpeg movie is closed at the end of an event. You can use Conversion Specifiers and spaces as part of the command. Use %f for passing filename (with full path) to the command.</p>
<dt><code>on_movie_start string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 Command to be executed when a movie is created. You can use Conversion Specifiers and spaces as part of the command. Use %f for passing filename (with full path) to the command.</p>
<dt><code>on_picture_save string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 Command to be executed when an image is saved. You can use Conversion Specifiers and spaces as part of the command. Use %f for passing filename (with full path) to the command.</p>
<dt><code>output_debug_pictures boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Output pictures with only the moving object. This feature generates the special motion type movies where you only see the pixels that changes as a graytone image. If labelling is enabled you see the largest area in blue. Smartmask is shown in red.</p>
<dt><code>output_pictures discrete strings</code></p>
<dd> Values: on, off, first, best, center / Default: on<br />
 Normal image is an image that is stored when motion is detected. It is the same image that was taken by the camera. I.e. not a motion image like defined by output_motion. Default is that normal images are stored.</p>
<dt><code>picture_filename string</code></p>
<dd> Values: Max 4095 characters / Default: %v-%Y%m%d%H%M%S-%q<br />
 File path for motion triggered images (jpeg or ppm) relative to target_dir. Value &#8216;preview&#8217; makes a jpeg filename with the same name body as the associated saved movie file.</p>
<dt><code>picture_type discrete strings</code></p>
<dd> Values: jpeg , ppm / Default: jpeg<br />
 Type of images motion will trigger when motion is detected.</p>
<dt><code>post_capture integer</code></p>
<dd> Values: 0 &#8211; 2147483647 / Default: 0 (disabled)<br />
 Specifies the number of frames to be captured after motion has been detected.</p>
<dt><code>pre_capture integer</code></p>
<dd> Values: 0 &#8211; 100s / Default: 0 (disabled)<br />
 Specifies the number of previous frames to be outputted at motion detection. Recommended range: 0 to 5, default=0. Do not use large values! Large values will cause Motion to skip video frames and cause unsmooth movies. To smooth movies use larger values of post_capture instead.</p>
<dt><code>process_id_file string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 File to store the process ID, also called pid file. Recommended value when used: /var/run/motion.pid</p>
<dt><code>quality integer</code></p>
<dd> Values: 1 &#8211; 100 / Default: 75<br />
 The quality for the jpeg images in percent.</p>
<dt><code>quiet boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Be quiet, don&#8217;t output beeps when detecting motion.</p>
<dt><code>rotate discrete strings</code></p>
<dd> Values: 0, 90, 180, 270 / Default: 0 (not rotated)<br />
 Rotate image the given number of degrees. The rotation affects all saved images as well as movies.</p>
<dt><code>roundrobin_frames integer</code></p>
<dd> Values: 1 &#8211; 2147483647 / Default: 1<br />
 Specifies the number of frames to capture before switching inputs, this way also slow switching (e.g. every second) is possible.</p>
<dt><code>roundrobin_skip integer</code></p>
<dd> Values: 1 &#8211; 2147483647 / Default: 1<br />
 Specifies the number of frames to skip after a switch. (1 if you are feeling lucky, 2 if you want to be safe).</p>
<dt><code>saturation integer</code></p>
<dd> Values: 0 &#8211; 255 / Default: 0 (disabled)<br />
 The colour saturation level for the video device.</p>
<dt><code>sdl_threadnr</code></p>
<dd> Values: 0 &#8211; 2147483647 / Default: 0 (disabled)<br />
 Number of motion thread to show in SDL Window (default: 0 = disabled)</p>
<dt><code>setup_mode boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Run Motion in setup mode.</p>
<dt><code>smart_mask_speed integer</code></p>
<dd> Values: 0 &#8211; 10 / Default: 0 (disabled)<br />
 Slugginess of the smart mask. Default is 0 = DISABLED. 1 is slow, 10 is fast.</p>
<dt><code>snapshot_filename string</code></p>
<dd> Values: Max 4095 characters / Default: %v-%Y%m%d%H%M%S-snapshot<br />
 File path for snapshots (jpeg or ppm) relative to target_dir.</p>
<dt><code>snapshot_interval integer</code></p>
<dd> Values: 0 &#8211; 2147483647 / Default: 0 (disabled)<br />
 Make automated snapshots every &#8216;snapshot_interval&#8217; seconds.</p>
<dt><code>sql_log_picture boolean</code></p>
<dd> Values: on, off / Default: on<br />
 Log to the database when creating motion triggered image file.</p>
<dt><code>sql_log_movie boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Log to the database when creating motion triggered movie file.</p>
<dt><code>sql_log_snapshot boolean</code></p>
<dd> Values: on, off / Default: on<br />
 Log to the database when creating a snapshot image file.</p>
<dt><code>sql_log_timelapse boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Log to the database when creating timelapse movie file</p>
<dt><code>sql_query string</code></p>
<dd> Values: Max 4095 characters / Default: insert into security(camera, filename, frame, file_type, time_stamp, text_event) values(&#8216;%t&#8217;, &#8216;%f&#8217;, &#8216;%q&#8217;, &#8216;%n&#8217;, &#8216;%Y-%m-%d %T&#8217;, &#8216;%C&#8217;)<br />
 SQL query string that is sent to the database. The values for each field are given by using convertion specifiers</p>
<dt><code>stream_auth_method integer</code></p>
<dd> Values: 0 = disabled , 1 = Basic authentication ,2 = MD5 digest (the safer authentication). / Default: 0 (disabled)<br />
 Set the authentication method for stream.</p>
<dt><code>stream_authentication string</code></p>
<dd> Values: username:password / Default: not defined (disabled)<br />
 Authentication for the stream.</p>
<dt><code>stream_limit integer</code></p>
<dd> Values: 0 &#8211; 2147483647 / Default: 0 (unlimited)<br />
 Limit the number of frames to number frames. After &#8216;stream_limit&#8217; number of frames the connection will be closed by motion. The value 0 means unlimited.</p>
<dt><code>stream_localhost boolean</code></p>
<dd> Values: on, off / Default: on<br />
 Limits the access to the stream to the localhost.</p>
<dt><code>stream_maxrate integer</code></p>
<dd> Values: 1 &#8211; 100 / Default: 1<br />
 Limit the framerate of the stream in frames per second. Default is 1. Set the value to 100 for practically unlimited.</p>
<dt><code>stream_motion boolean</code></p>
<dd> Values: on, off / Default: off<br />
 If set to &#8216;on&#8217; Motion sends slows down the stream to 1 picture per second when no motion is detected. When motion is detected the stream runs as defined by stream_maxrate. When &#8216;off&#8217; the stream always runs as defined by stream_maxrate.</p>
<dt><code>stream_port integer</code></p>
<dd> Values: 0 &#8211; 65535 / Default: 0 (disabled)<br />
 TCP port on which motion will listen for incoming connects with its stream server.</p>
<dt><code>stream_quality integer</code></p>
<dd> Values: 1 &#8211; 100 / Default: 50<br />
 Quality setting in percent for the mjpeg picture frames transferred over the stream connection. Keep it low to restrict needed bandwidth.</p>
<dt><code>switchfilter boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Turns the switch filter on or off. The filter can distinguish between most switching noise and real motion. With this you can even set roundrobin_skip to 1 without generating much false detection.</p>
<dt><code>target_dir string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined = current working directory<br />
 Target directory for picture and movie files.</p>
<dt><code>text_changes boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Turns the text showing changed pixels on/off.</p>
<dt><code>text_double boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Draw characters at twice normal size on images.</p>
<dt><code>text_event string</code></p>
<dd> Values: Max 4095 characters / Default: %Y%m%d%H%M%S<br />
 This option defines the value of the special event conversion specifier %C. You can use any conversion specifier in this option except %C. Date and time values are from the timestamp of the first image in the current event.</p>
<dt><code>text_left string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 User defined text overlayed on each in the lower left corner. Use A-Z, a-z, 0-9, &quot; / ( ) @ ~ # &lt; &gt; | , . : &#8211; + _ and conversion specifiers (codes starting by a %).</p>
<dt><code>text_right string</code></p>
<dd> Values: Max 4095 characters / Default: %Y-%m-%dT<br />
 User defined text overlayed on each in the lower right corner. Use A-Z, a-z, 0-9, &quot; / ( ) @ ~ # &lt; &gt; | , . : &#8211; + _ and conversion specifiers (codes starting by a %). Default: %Y-%m-%dT = date in ISO format and time in 24 hour clock</p>
<dt><code>thread string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 Specifies full path and filename for a thread config file. Each camera needs a thread config file containing the options that are unique to the camera. If you only have one camera you do not need thread config files. If you have two or more cameras you need one thread config file for each camera in addition to motion.conf. This option must be placed in motion.conf and not in a thread config file.</p>
<dt><code>threshold integer</code></p>
<dd> Values: 1 &#8211; 2147483647 / Default: 1500<br />
 Threshold for declaring motion. The threshold is the number of changed pixels counted after noise filtering, masking, despeckle, and labelling.</p>
<dt><code>threshold_tune boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Activates the automatic tuning of threshold level.</p>
<dt><code>timelapse_filename string</code></p>
<dd> Values: Max 4095 characters / Default: %v-%Y%m%d-timelapse<br />
 File path for timelapse movies relative to target_dir (ffmpeg only).</p>
<dt><code>track_auto boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Enable auto tracking</p>
<dt><code>track_iomojo_id integer</code></p>
<dd> Values: 0 &#8211; 65535 / Default: 0<br />
 Use this option if you have an iomojo smilecam connected to the serial port instead of a general stepper motor controller.</p>
<dt><code>track_maxx integer</code></p>
<dd> Values: 0 &#8211; 65535 / Default: 0<br />
 The maximum position for servo x.</p>
<dt><code>track_maxy integer</code></p>
<dd> Values: 0 &#8211; 65535 / Default: 0<br />
 The maximum position for servo y.</p>
<dt><code>track_motorx integer</code></p>
<dd> Values: 0 &#8211; 65535 / Default: 0<br />
 The motor number that is used for controlling the x-axis.</p>
<dt><code>track_motory integer</code></p>
<dd> Values: 0 &#8211; 65535 / Default: 0<br />
 The motor number that is used for controlling the y-axis.</p>
<dt><code>track_move_wait integer</code></p>
<dd> Values: 0 &#8211; 65535 / Default: 10<br />
 Delay during which tracking is disabled after auto tracking has moved the camera. Delay is defined as number of picture frames.</p>
<dt><code>track_port string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 This is the device name of the serial port to which the stepper motor interface is connected.</p>
<dt><code>track_speed integer</code></p>
<dd> Values: 0 &#8211; 255 / Default: 255<br />
 Speed to set the motor to.</p>
<dt><code>track_step_angle_x integer</code></p>
<dd> Values: 0-90 / Default: 10<br />
 Angle in degrees the camera moves per step on the X-axis with auto tracking. Currently only used with pwc type cameras.</p>
<dt><code>track_step_angle_y integer</code></p>
<dd> Values: 0-40 / Default: 10<br />
 Angle in degrees the camera moves per step on the Y-axis with auto tracking. Currently only used with pwc type cameras.</p>
<dt><code>track_stepsize integer</code></p>
<dd> Values: 0 &#8211; 255 / Default: 40<br />
 Number of steps to make.</p>
<dt><code>track_type discrete strings</code></p>
<dd> Values: 0 (none), 1 (stepper), 2 (iomojo), 3 (pwc), 4 (generic), 5 (uvcvideo) / Default: 0 (None)<br />
 Type of tracker.</p>
<dt><code>tunerdevice string</code></p>
<dd> Values: Max 4095 characters / Default: /dev/tuner0<br />
 The tuner device used for controlling the tuner in a tuner card. This option is only used when Motion is compiled for FreeBSD.</p>
<dt><code>use_extpipe boolean</code></p>
<dd> Values: on, off / Default: off<br />
 Enables extpipe to use an external video encoder feeding with YUV420 using a pipe .</p>
<dt><code>v4l2_palette discrete strings</code></p>
<dd> Values: 0 &#8211; 8 / Default: 8<br />
 Allow to choose preferable palette to be use by motion to capture from those supported by your videodevice.</p>
<dt><code>video_pipe string</code></p>
<dd> Values: Max 4095 characters / Default: Not defined<br />
 The video4linux video loopback input device for normal images. If a particular pipe is to be used then use the device filename of this pipe. If a dash &#8216;-&#8216; is given motion will use /proc/video/vloopback/vloopbacks to locate a free pipe.</p>
<dt><code>videodevice string</code></p>
<dd> Values: Max 4095 characters / Default: /dev/video0 (FreeBSD: /dev/bktr0)<br />
 The video device to be used for capturing. Default for Linux is /dev/video0. for FreeBSD the default is /dev/bktr0.</p>
<dt><code>webcontrol_authentication string</code></p>
<dd> Values: Max 4096 characters / Default: Not defined<br />
 To protect HTTP Control by username and password, use this option for HTTP 1.1 Basic authentication. The string is specified as username: password. Do not specify this option for no authentication. This option must be placed in motion.conf and not in a thread config file.</p>
<dt><code>webcontrol_html_output boolean</code></p>
<dd> Values: on, off / Default: on<br />
 Enable HTML in the answer sent back to a browser connecting to the webcontrol_port. This option must be placed in motion.conf and not in a thread config file.</p>
<dt><code>webcontrol_localhost boolean</code></p>
<dd> Values: on, off / Default: on<br />
 Limits the webcontrol to the localhost. This option must be placed in motion.conf and not in a thread config file.</p>
<dt><code>webcontrol_port integer</code></p>
<dd> Values: 0 &#8211; 65535 / Default: 0 (disabled)<br />
 Sets the port number for the http (html using browser) based remote webcontrol. This option must be placed in motion.conf and not in a thread config file. </p>
<dt><code>width integer</code></p>
<dd> Values: Device Dependent / Default: 352<br />
 The width in pixels of each frame. Valid range is camera dependent. </p>
</dl>
<h2>SIGNALS</h2>
<p> Motion responds to the following signals:</p>
<dl>
<dt><code>SIGHUP</code></p>
<dd> The config file will be reread.</p>
<dt><code>SIGTERM</code></p>
<dd> If needed motion will create a movie file of the last event and exit</p>
<dt><code>SIGUSR1</code></p>
<dd> Motion will create a movie file of the current event.</dl>
<h2>NOTES</h2>
<dl>
<dt><code>Snapshot</code></p>
<dd> A snapshot is a picture taken at regular intervals independently of any movement in the picture.</p>
<dt><code>Motion image</code></p>
<dd> A &quot;motion&quot; image/movie shows the pixels that have actually changed during the last frames. These pictures are not very useful for normal presentation to the public but they are quite useful for testing and tuning and making mask files as you can see exactly where motion sees something moving. Motion is shown in greytones. If labelling is enabled the largest area is marked as blue. Smart mask is shown in read.</p>
<dt><code>Normal image</code></p>
<dd> A &quot;normal&quot; image is the real image taken by the camera with text overlayed.</p>
<dt><code>Threads and config files</code></p>
<dd> If Motion was invoked with command line option -c pathname Motion will expect the config file to be as specified. When you specify the config file on the command line with -c you can call it anything.<br />
 If you do not specify -c or the filename you give Motion does not exist, Motion will search for the configuration file called &#8216;motion.conf&#8217; in the following order:<br />
 1. Current directory from where motion was invoked<br />
 2. Then in a directory called &#8216;.motion&#8217; in the current users home directory (shell environment variable $HOME). E.g. /home/goofy/.motion/motion.conf<br />
 3. The directory defined by the &#8211;sysconfdir=DIR when running .configure during installation of Motion (If this option was not defined the default is /usr/local/etc/)<br />
 If you have write access to /usr/local/etc then the editor recommends having only one motion.conf file in the default /usr/local/etc/ directory.<br />
 Motion has a configuration file in the distribution package called motion-dist.conf. When you run &#8216;make install&#8217; this files gets copied to the /usr/local/etc directory.<br />
 The configuration file needs to be renamed from motion-dist.conf to motion.conf. The original file is called motion-dist.conf so that your perfectly working motion.conf file does not accidentally get overwritten when you re-install or upgrade to a newer version of Motion.<br />
 If you have more than one camera you should not try and invoke Motion more times. Motion is made to work with more than one camera in a very elegant way and the way to do it is to create a number of thread config files. Motion will then create an extra tread of itself for each camera. If you only have one camera you only need the motion.conf file. The minute you have two or more cameras you must have one thread config file per camera besides the motion.conf file.<br />
 So if you have for example two cameras you need motion.conf and two thread config files. Total of 3 config files.<br />
 An option that is common to all cameras can be placed in motion.conf. (You can also put all parameters in the thread files but that makes a lot of editing when you change a common thing).<br />
 An option that is unique to a camera must be defined in each thread file.<br />
 The first camera is defined in the first thread file called from motion.conf. The 2nd camera is defined in the 2nd thread file called from motion.conf etc.<br />
 Any option defined in motion.conf will be used for all cameras except for the cameras in which the same option is defined in a thread config file.<br />
 Motion reads its configuration parameters in the following sequence. If the same parameter exists more than one place the last one read wins.<br />
 1. Motion reads the configuration file motion.conf from the beginning of the file going down line by line.<br />
 2. If the option &quot;thread&quot; is defined in motion.conf, the thread configuration file(s) is/(are) read.<br />
 3. Motion continues reading the rest of the motion.conf file. Any options from here will overrule the same option previously defines in a thread config file.<br />
 4. Motion reads the command line option again overruling any previously defined options.<br />
 So always call the thread config files in the end of the motion.conf file. If you define options in motion.conf AFTER the thread file calls, the same options in the thread files will never be used. So always put the thread file call at the end of motion.conf.<br />
 If motion is built without specific features such as ffmpeg, mysql etc it will ignore the options that belongs to these features. You do not have to remove them or comment them out.<br />
 If you run the webcontrol command <a rel="nofollow" href="http://host:port/0/config/writeyes,">http://host:port/0/config/writeyes,</a> motion will overwrite motion.conf and all the thread.conf files by autogenerated config files neatly formatted and only with the features included that Motion was built with. If you later re-build Motion with more features or upgrade to a new version, you can use your old config files, run the motion.conf.write command, and you will have new config files with the new options included all set to their default values. This makes upgrading very easy to do.</p>
<dt><code>Conversion Specifiers for Advanced Filename and Text Features</code></p>
<dd> The table below shows all the supported Conversion Specifiers you can use in the options text_left, text_right, snapshot_filename, picture_filename, movie_filename, timelapse_filename, on_area_detected, on_camera_lost, on_event_start, on_event_end, on_picture_save, on_movie_start, on_movie_end, and on_motion_detected.<br />
 In text_left and text_right you can additionally use &#8216; for new line. </p>
<dt><code>%a</code></p>
<dd> The abbreviated weekday name according to the current locale.</p>
<dt><code>%A</code></p>
<dd> The full weekday name according to the current locale.</p>
<dt><code>%b</code></p>
<dd> The abbreviated month name according to the current locale.</p>
<dt><code>%B</code></p>
<dd> The full month name according to the current locale.</p>
<dt><code>%c</code></p>
<dd> The preferred date and time representation for the current locale.</p>
<dt><code>%C</code></p>
<dd> Text defined by the text_event feature</p>
<dt><code>%d</code></p>
<dd> The day of the month as a decimal number (range 01 to 31).</p>
<dt><code>%D</code></p>
<dd> Number of pixels detected as Motion. If labelling is enabled the number is the number of pixels in the largest labelled motion area.</p>
<dt><code>%E</code></p>
<dd> Modifier: use alternative format, see below.</p>
<dt><code>%f</code></p>
<dd> File name &#8211; used in the on_picture_save, on_movie_start, on_movie_end, and sql_query features.</p>
<dt><code>%F</code></p>
<dd> Equivalent to %Y-%m-%d (the ISO 8601 date format).</p>
<dt><code>%H</code></p>
<dd> The hour as a decimal number using a 24-hour clock (range 00 to 23).</p>
<dt><code>%i</code></p>
<dd> Width of the rectangle containing the motion pixels (the rectangle that is shown on the image when locate_motion is on).</p>
<dt><code>%I</code></p>
<dd> The hour as a decimal number using a 12-hour clock (range 01 to 12).</p>
<dt><code>%j</code></p>
<dd> The day of the year as a decimal number (range 001 to 366).</p>
<dt><code>%J</code></p>
<dd> Height of the rectangle containing the motion pixels (the rectangle that is shown on the image when locate_motion is on).</p>
<dt><code>%k</code></p>
<dd> The hour (24-hour clock) as a decimal number (range 0 to 23); single digits are preceded by a blank. (See also %H.)</p>
<dt><code>%K</code></p>
<dd> X coordinate in pixels of the center point of motion. Origin is upper left corner.</p>
<dt><code>%l</code></p>
<dd> The hour (12-hour clock) as a decimal number (range 1 to 12); single digits are preceded by a blank. (See also %I.)</p>
<dt><code>%L</code></p>
<dd> Y coordinate in pixels of the center point of motion. Origin is upper left corner and number is positive moving downwards (I may change this soon).</p>
<dt><code>%m</code></p>
<dd> The month as a decimal number (range 01 to 12).</p>
<dt><code>%M</code></p>
<dd> The minute as a decimal number (range 00 to 59).</p>
<dt><code>%n</code></p>
<dd> Filetype as used in the on_picture_save, on_movie_start, on_movie_end, and sql_query features.</p>
<dt><code>%N</code></p>
<dd> Noise level.</p>
<dt><code>%o</code></p>
<dd> Threshold. The number of detected pixels required to trigger motion. When threshold_tune is &#8216;on&#8217; this can be used to show the current tuned value of threshold.</p>
<dt><code>%p</code></p>
<dd> Either &#8216;AM&#8217; or &#8216;PM&#8217; according to the given time value, or the corresponding strings for the current locale. Noon is treated as `pm&#8217; and midnight as `am&#8217;.</p>
<dt><code>%P</code></p>
<dd> Like %p but in lowercase: `am&#8217; or `pm&#8217; or a corresponding string for the current locale.</p>
<dt><code>%q</code></p>
<dd> Picture frame number within current second. For jpeg filenames this should always be included in the filename if you save more then 1 picture per second to ensure unique filenames. It is not needed in filenames for movies.</p>
<dt><code>%Q</code></p>
<dd> Number of detected labels found by the despeckle feature</p>
<dt><code>%r</code></p>
<dd> The time in a.m. or p.m. notation.</p>
<dt><code>%R</code></p>
<dd> The time in 24-hour notation (%H:%M).</p>
<dt><code>%s</code></p>
<dd> The number of seconds since the Epoch, i.e., since 1970-01-01 00:00:00 UTC.</p>
<dt><code>%S</code></p>
<dd> The second as a decimal number (range 00 to 61).</p>
<dt><code>%t</code></p>
<dd> Thread number (camera number)</p>
<dt><code>%T</code></p>
<dd> The time in 24-hour notation (%H:%M:%S).</p>
<dt><code>%u</code></p>
<dd> The day of the week as a decimal, range 1 to 7, Monday being 1. See also %w.</p>
<dt><code>%U</code></p>
<dd> The week number of the current year as a decimal number, range 00 to 53, starting with the first Sunday as the first day of week 01. See also %V and %W.</p>
<dt><code>%v</code></p>
<dd> Event number. An event is a series of motion detections happening with less than &#8216;gap&#8217; seconds between them.</p>
<dt><code>%V</code></p>
<dd> The ISO 8601:1988 week number of the current year as a decimal number, range 01 to 53, where week 1 is the first week that has at least 4 days in the current year, and with Monday as the first day of the week. See also %U and %W.</p>
<dt><code>%w</code></p>
<dd> The day of the week as a decimal, range 0 to 6, Sunday being 0. See also %u.</p>
<dt><code>%W</code></p>
<dd> The week number of the current year as a decimal number, range 00 to 53, starting with the first Monday as the first day of week 01.</p>
<dt><code>%x</code></p>
<dd> The preferred date representation for the current locale without the time.</p>
<dt><code>%X</code></p>
<dd> The preferred time representation for the current locale without the date.</p>
<dt><code>%y</code></p>
<dd> The year as a decimal number without a century (range 00 to 99).</p>
<dt><code>%Y</code></p>
<dd> The year as a decimal number including the century.</p>
<dt><code>%z</code></p>
<dd> The time-zone as hour offset from GMT.</p>
<dt><code>%Z</code></p>
<dd> The time zone or name or abbreviation. </p>
<dt><code>More information</code></p>
<dd> Motion homepage: <a rel="nofollow" href="http://motion.sourceforge.net/">http://motion.sourceforge.net/</a> </p>
<p> Motion Guide (user and installation guide):<br />
 <a rel="nofollow" href="http://www.lavrsen.dk/twiki/bin/view/Motion/MotionGuide">http://www.lavrsen.dk/twiki/bin/view/Motion/MotionGuide</a><br />
 <a rel="nofollow" href="http://www.lavrsen.dk/twiki/bin/view/Motion/VideoFourLinuxLoopbackDevice">http://www.lavrsen.dk/twiki/bin/view/Motion/VideoFourLinuxLoopbackDevice</a></dl>
<h2>AUTHORS</h2>
<p> Jeroen Vreeken (pe1rxq [at] amsat.org), Folkert van Heusden, Kenneth Lavrsen (kenneth [at] lavrsen.dk) </p>
<h2>Index</h2>
