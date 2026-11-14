---
title: "iipsrv(8)"
name: "iipsrv"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iipsrv/"
description: "IIPSRV – IIPImage Image Server"
---

<p>IIPSRV &#8211; IIPImage Image Server </p>
<h2>Description</h2>
<p>IIPImage is an advanced high-performance feature-rich multi-protocol image server for web-based streamed viewing and zooming of ultra high-resolution images. It is designed to be fast and bandwidth-efficient with low processor and memory requirements. The system can comfortably handle gigapixel size images as well as advanced image features such as 8, 16 and 32 bit depths, CIELAB colorimetric images and scientific imagery such as multispectral images. Source images can be either TIFF (tiled multi-resolution) or JPEG2000 (if enabled). The image server can also dynamically export images in JPEG format and perform basic image processing, such as contrast adjustment, gamma control, conversion from color to greyscale, color twist, region extraction and arbitrary rescaling. The server can also export spectral point or profile data from multispectral data and apply color maps or perform hillshading rendering. </p>
<h2>Synopsis</h2>
<p>Command line use: <code>iipsrv.fcgi &#8211;bind</code> <i>host</i> : <i>port</i> </p>
<h2>Files</h2>
<p><i>iipsrv.fcgi</i> main executable </p>
<p> <i>iipsrv.log</i> log file: usually in <i>/var/log/</i> or <i>/tmp/</i></p>
<h2>Options</h2>
<p>There are several parameters that can be supplied to <code>iipsrv.fcgi</code> These should be set via the appropriate web server configuration directives if running via Apache or Lighttpd. See <code>EXAMPLES</code> for details of web server configuations. Alternatively these parameters can be set via environment settings if running directly from the command line or from <code>spawn-fcgi.</code> </p>
<dl>
<dt>LOGFILE</p>
<dd>The log file the module will (attempt) to write to. If no value is given, no log will be written. Make sure the server process has write access to this directory. Paths with spaces in them may not work correctly.</p>
<dt>VERBOSITY</p>
<dd>The level of logging. 0 means no logging, 1 is minimal logging, 2 lots of debugging stuff and 3 even more debugging stuff and 4 a very large amount indeed. Logging is only enabled if <code>LOGFILE</code> has also been defined.</p>
<dt>JPEG_QUALITY</p>
<dd>The default JPEG quality factor for compression when the client does not specify one. The value should be between 1 (highest level of compression) and 100 (highest image quality). The default is 75.</p>
<dt>MAX_IMAGE_CACHE_SIZE</p>
<dd>Max image cache size to be held in RAM in MB. This is a cache of the compressed JPEG image tiles requested by the client. The default is 5MB.</p>
<dt>FILESYSTEM_PREFIX</p>
<dd>This is a prefix automatically added by the server to the beginning of each file system path. This can be useful for security reasons to limit access to certain sub-directories. For example, with a prefix of &quot;/home/images/&quot; set on the server, a request by a client for &quot;image.tif&quot; will point to the path &quot;/home/images/image.tif&quot;. Any reverse directory path component such as ../ is also filtered out. No default value.</p>
<dt>MAX_CVT</p>
<dd>The maximum permitted image pixel size returned by the CVT command in conjunction with WID or HEI or RGN. The default is 5000. This prevents huge requests from overloading the server</p>
<dt>MAX_LAYERS</p>
<dd>The maximum number of quality layers to decode for image that support progressive quality encoding, such as JPEG2000. Ignored for other file formats. By default half of the available layers are decoded. If set to -1, all the available layers will be decoded.</p>
<dt>WATERMARK</p>
<dd>TIFF image to use as watermark file. This image should be not be bigger the tile size used for TIFF tiling. If bigger, it will simply be cropped to the tile size. If smaller, the watermark will be positioned randomly within the available space. The image can be either colour or grayscale.</p>
<dt>WATERMARK_PROBABILITY</p>
<dd>The probability that a particilar tile will have a watermark applied to it. 0 means never, 1 means always.</p>
<dt>WATERMARK_OPACITY</p>
<dd>The opacity (between 0 and 1) applied to the watermark image.</p>
<dt>MEMCACHED_SERVERS</p>
<dd>A comma-delimitted list of memcached servers with optional port numbers. For example: localhost,192.168.0.1:8888,192.168.0.2.</p>
<dt>MEMCACHED_TIMEOUT</p>
<dd>Time in seconds that cache remains fresh. Default is 86400 seconds (24 hours).</p>
<dt>FILENAME_PATTERN</p>
<dd>Pattern that follows the name stem for a panoramic image sequence. eg: &quot;_pyr_&quot; for <i>FZ1_pyr_000_090.tif</i>. In this example, just supply FZ1 to the FIF command. The &quot;000&quot; indicates the vertical angle and &quot;090&quot; the horizontal. This is only relevant to 3D image sequences. The default is &quot;_pyr_&quot;.</p>
<dt>CORS</p>
<dd>Cross Origin Resource Sharing setting. Disabled by default. Set to &quot;*&quot; to enable for all domains or specify a single domain. See <a rel="nofollow" href="http://www.w3.org/TR/cors/">http://www.w3.org/TR/cors/</a> for more details on CORS.</p>
<dt>BASE_URL</p>
<dd>Set a base URL for use in certain protocol requests if web server rewriting has taken place and the public URL is not the same as that supplied to <code>iipsrv</code></p>
<dt>CACHE_CONTROL</p>
<dd>Set the HTTP Cache-Control header. See <a rel="nofollow" href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9">http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9</a> for a full list of options. If not set, header defaults to &quot;max-age=86400&quot; (24 hours).<br />
&nbsp;<wbr> </p>
</dl>
<h2>Examples</h2>
<p><code>iipsrv</code> will be automatically started by both Apache and Lighttpd. But not by Nginx or Java Application Servers. See the example configuration in the README or included with your distribution for the appropriate syntax. Note that Apache has two FCGI modules: mod_fastcgi and mod_fcgid which are configured differently. You may also wish to run <code>iipsrv</code> as a standalone program. To do this, use the following syntax to bind to a particular port and listen for FCGI (not HTTP) requests. In the following example, <code>iipsrv</code> will bind to port 9000 on the machine&#8217;s IP address 192.168.0.1: % iipsrv.fcgi &#8211;bind 192.168.0.1:9000 There is additionally a <code>&#8211;backlog</code> parameter that is optional and sets the socket backlog value. The backlog value specifies the number of requests can be queued and, therefore, increases the number of concurrent connections that <code>iipsrv</code> can handle and is set to 2048 by default. For example: % iipsrv.fcgi &#8211;bind 192.168.0.1:9000 &#8211;backlog 1024 Note that the backlog parameter must be specified <code>after the bind parameter and argument.</code> Note also that this value may be limited by the operating system. On Linux kernels &lt; 2.4.25 and Mac OS X, the backlog limit is hard-coded to 128, so any value above this will be limited to 128 by the OS. If you do provide a backlog value, verify whether the setting /proc/sys/net/core/somaxconn should be updated. It is also possible to run <i>iipsrv</i> via the <i>spawn-fcgi</i> program. Set up any parameters via environment variables and run the command as follows to bind, as in the previous example to port 9000 on IP address 192.168.0.1: % spawn-fcgi -f src/iipsrv.fcgi -a 192.168.0.1 -p 9000 For use in stand alone or spawn-fcgi mode, you will then need to configure your webserver on the same machine or another to direct FCGI protocol requests to this IP address and port. For web servers such as Nginx or Java Application Servers such as Tomcat, JBoss or Jetty, which cannot automatically start FCGI processes, <code>iipsrv</code> will need to be started in stand alone mode or via spawn-fcgi. </p>
<h2>Protocols</h2>
<p>The IIPImage server supports the <code>Internet Imaging Protocol (IIP)</code> , the <code>Zoomify</code> protocol, the <code>DeepZoom</code> and the <code>International Image Interoperability Framework (IIIF)</code> protocols. Client applications supporting these protocols should be able to use <code>iipsrv</code> as their back-end server. <code>IIP</code> is the most feature rich of the 4 protocols and allows access to the more advanced imaging server features.</p>
<h2>Image Paths</h2>
<p>The image paths given to the server must be absolute paths on the server machine (eg. via the FIF variable for the IIP protocol: FIF=/images/test.tif) and <i>not </i> paths relative to the web server document root location. If the FILESYSTEM_PREFIX server directive has been set (see OPTIONS above), then this prefix is automatically pre-pended to all requests to generate the absolute image path. Make sure that the server process owner is able to access and read the images. </p>
<p> Note that images do <i>not</i> need to be directly accessible externally by the client via the web server.</p>
<h2>See Also</h2>
<p>IIPImage website: <a rel="nofollow" href="http://iipimage.sourceforge.net">http://iipimage.sourceforge.net</a> </p>
<h2>Authors</h2>
<p>Ruven Pillay &lt;ruven [at] users.sourceforge.net&gt;</p>
