---

title: "blenderplayer(1)"
name: "blenderplayer"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blenderplayer/"
description: "blenderplayer – a utility for previewing .blend files"
---

<h2>NAME</h2>
<p> blenderplayer &#8211; a utility for previewing .blend files</p>
<p> usage: blenderplayer [-w [w h l t]] [-f [fw fh fb ff]] [-g gamengineoptions] [-s stereomode] filename.blend</p>
<dl>
<dt> <code>-h</code>: Prints this command summary</dt>
<dt> <code>-w</code>: display in a window</dt>
<dt> <code>&#8211;Optional</code> parameters&#8211;</dt>
<dd>w = window width h = window height</dd>
<dt>
</dt><dd> l = window left coordinate t = window top coordinate Note: If w or h is defined, both must be defined.</dd>
<dt>
</dt><dd> Also, if l or t is defined, all options must be used.</dd>
<dt> <code>-f</code>: start game in full screen mode</dt>
<dt> <code>&#8211;Optional</code> parameters&#8211;</dt>
<dd>fw = full screen mode pixel width fh = full screen mode pixel height</dd>
<dt>
</dt><dd> fb = full screen mode bits per pixel ff = full screen mode frequency Note: If fw or fh is defined, both must be defined.</dd>
<dt>
</dt><dd> Also, if fb is used, fw and fh must be used. ff requires all options.</dd>
<dt> <code>-s</code>: start player in stereo</dt>
<dt>
</dt><dd>stereomode: hwpageflip</dd>
<dd> (Quad buffered shutter glasses)</dd>
<dt>syncdoubling</dt>
<dd> (Above Below)</dd>
<dt>sidebyside</dt>
<dd> (Left Right)</dd>
<dt>anaglyph</dt>
<dd> (Red-Blue glasses)</dd>
<dt>vinterlace</dt>
<dd> (Vertical interlace for autostereo display)</dd>
<dt>
</dt><dd> depending on the type of stereo you want</dd>
<dt> <code>-D</code>: start player in dome mode</dt>
<dt> <code>&#8211;Optional</code> parameters&#8211;</dt>
<dt>
</dt><dd>angle</dd>
<dd> = field of view in degrees</dd>
<dt>tilt</dt>
<dd> = tilt angle in degrees</dd>
<dt>
</dt><dd> warpdata = a file to use for warping the image (absolute path) mode: fisheye (Fisheye)</dd>
<dt>truncatedfront</dt>
<dd> (Front-Truncated)</dd>
<dt>truncatedrear</dt>
<dd> (Rear-Truncated)</dd>
<dt>cubemap</dt>
<dd> (Cube Map)</dd>
<dt>sphericalpanoramic</dt>
<dd> (Spherical Panoramic)</dd>
<dt>
</dt><dd> depending on the type of dome you are using</dd>
<dt> <code>-i</code>: parent windows ID</dt>
<dt> <code>-d</code>: turn debugging on</dt>
<dt> <code>-g</code>: game engine options:</dt>
<dt>
</dt><dd>Name</dd>
<dd> Default Description</dd>
<dt> <code>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;</code></dt>
<dt>
</dt><dd>fixedtime</dd>
<dd> 0 &quot;Enable all frames&quot;</dd>
<dt>nomipmap</dt>
<dd> 0 Disable mipmaps</dd>
<dt>show_framerate</dt>
<dd> 0 Show the frame rate</dd>
<dt>show_properties</dt>
<dd> 0 Show debug properties</dd>
<dt>show_profile</dt>
<dd> 0 Show profiling information</dd>
<dt>blender_material</dt>
<dd> 0 Enable material settings</dd>
<dt>ignore_deprecation_warnings</dt>
<dd> 1 Ignore deprecation warnings</dd>
<dt>
</dt><dd> &#8211; : all arguments after this are ignored, allowing python to access them from sys.argv</dd></dl>
<p> example: blenderplayer <code>-w</code> 320 200 10 10 <code>-g</code> noaudio//home//user//filename.blend example: blenderplayer <code>-g</code> show_framerate = 0 //home//user//filename.blend </p>
