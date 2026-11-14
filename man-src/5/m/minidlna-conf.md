---
title: "minidlna-conf(5)"
name: "minidlna-conf"
section: "5"
letter: "m"
url: "/docs/linux/man/5-minidlna-conf/"
description: "minidlna"
---

<p>minidlna</p>
<h2>Description</h2>
<p><code>minidlna</code> is a light weight but very functional DLNA server. In most cases, the defaults do not need modifications. The global configuration file is /etc/minidlna.conf but local users without system root access can run minidlna with their own configuration file. </p>
<h2>Options</h2>
<p>The following are user configurable options in /etc/minidlna.conf. minidlna runs by default as user nobody, so make sure system permissions are set correctly for read access to media and write access to cache and log dirs. </p>
<dl>
<dt><code>friendly_name</code></p>
<dd>The name you want your media server seen as, EG: friendly_name=Home Media Server </p>
<dt><code>port</code></p>
<dd>
<pre>Port for HTTP (descriptions, SOAP, media transfer) traffic etc, defaults to 8200.
There should be no need to change this.</pre>
<dt><code>network_interface</code></p>
<dd>Network interfaces to serve, comma delimited. Defaults to all. </p>
<dt><code>strict_dlna</code></p>
<dd>
<pre>Set this to strictly adhere to DLNA standards. 
This will allow server-side downscaling of very large JPEG images,
which may hurt JPEG serving performance on (at least) Sony DLNA products.</pre>
<dt><code>notify_interval</code></p>
<dd>Notify interval in seconds. The default is 895 seconds. </p>
<dt><code>minissdpdsocket</code></p>
<dd>
<pre>Specify the path to the MiniSSDPd socket, 
EG: minissdpdsocket=/var/run/minissdpd.sock</pre>
<dt><code>serial</code></p>
<dd>
<pre>Serial number the daemon will report to clients in its XML description. 
Defaults to 12345678</pre>
<dt><code>model</code></p>
<dd>
<pre>Model number the daemon will report to clients in its XML description. 
Defaults to 1</pre>
<dt><code>media_dir</code></p>
<dd>
<pre>Path to the directory containing the media files minidlna should share. 
Use this option multile times if you have more than one directory to share. 
Example:
 media_dir=/opt/multimedia/videos
 media_dir=/opt/multimedia/movies</pre>
</dl>
<p> You can also restrict an entry to a specific media type, you do this by using the following syntax: </p>
<pre> the letter 'A', 'V' or 'P', followed by a comma (',') followed by the path.
 The meaning of the first letter is as follows:
 'A' for audio files
 'V' for video files
 'P' for image files
 For example, if you want to include only video files located
 in /opt/multimedia/videos directory, and only music
 in /opt/multimedia/music, then you would use
 media_dir=V,/opt/multimedia/videos
 media_dir=A,/opt/multimedia/music
 Another example would be
 media_dir=V,/opt/multimedia/videos
 media_dir=V,/opt/multimedia/movies
 media_dir=A,/opt/multimedia/music
 Or, if you did not care what type it finds, then you could use
 media_dir=/opt/multimedia/videos
 media_dir=/opt/multimedia/movies
 media_dir=/opt/multimedia/music
 You can mix it up, find anything in music, but only Videos, in videos and movies
 media_dir=V,/opt/multimedia/videos
 media_dir=V,/opt/multimedia/movies
 media_dir=/opt/multimedia/music</pre>
<dl>
<dt><code>presentation_url</code></p>
<dd>
<pre>Default presentation url is http address on port 80
EG: presentation_url=<a rel="nofollow" href="http://www.mediaserver.lan/index.php">http://www.mediaserver.lan/index.php</a></pre>
<dt><code>db_dir</code></p>
<dd>Where minidlna stores the data files, including Album caceh files, by default this is /var/cache/minidlna </p>
<dt><code>log_dir</code></p>
<dd>Path to the directory where the log file upnp-av.log should be stored, this defaults to /var/log </p>
<dt><code>log_level</code></p>
<dd>Set this to change the verbosity of the information that is logged each section can use a different level: off, fatal, error, warn, info, or debug </p>
<pre>Example
log_level=general,artwork,database,inotify,scanner,metadata,http,ssdp,tivo=warn</pre>
<dt><code>inotify</code></p>
<dd>Set to &#8216;yes&#8217; to enable inotify monitoring of the files under media_dir to automatically discover new files. Set to &#8216;no&#8217; to disable inotify. </p>
<dt><code>album_art_names</code></p>
<dd>This should be a list of file names to check for when searching for album art and names should be delimited with a forward slash (&quot;/&quot;). </p>
<pre>Example
album_art_names=Cover.jpg/cover.jpg/AlbumArtSmall.jpg/albumartsmall.jpg/AlbumArt.jpg
/albumart.jpg/Album.jpg/album.jpg/Folder.jpg/folder.jpg/Thumb.jpg/thumb.jpg</pre>
<dt><code>enable_tivo</code></p>
<dd>Set this to yes to enable support for streaming .jpg and .mp3 files to a TiVo supporting HMO, default is no. </p>
<dt><code>root_container</code></p>
<dd>Use a different container as the root of the tree exposed to clients. </p>
<pre>The possible values are:
 '.' to use the standard container (this is the default)
 'B' to use the &quot;Browse Directory&quot; container;
 'M' to use the &quot;Music&quot; container;
 'V' to use the &quot;Video&quot; container;
 'P' to use the &quot;Pictures&quot; container.
 If you specify 'B' and the client device is audio only, then
 &quot;Music/Folders&quot; will be used as root container and you wont see Videos.</pre>
<dt><code>force_sort_criteria</code></p>
<dd>Always force SortCriteria to this value, regardless of the SortCriteria passed by the client. </p>
<pre>Example
force_sort_criteria=+upnp:class,+upnp:originalTrackNumber,+dc:title</pre>
</dl>
<h2>Version</h2>
<p>This manpage corresponds to minidlna version 1.0.25</p>
<h2>Author</h2>
<pre>minidlna developed by Justin Maggard <a rel="nofollow" href="https://sourceforge.net/projects/minidlna/">https://sourceforge.net/projects/minidlna/</a>
man page written by Noel Butler &lt;noelb [at] ausics.net&gt;</pre>
<h2>License</h2>
<p>GPL</p>
<h2>Files</h2>
<p>/etc/minidlna.conf</p>
<h2>See Also</h2>
<p>&nbsp;<wbr><a href="/docs/linux/man/8-minidlna/">minidlna</a>(8) </p>
