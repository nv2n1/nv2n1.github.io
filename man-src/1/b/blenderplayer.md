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
<h2>DESCRIPTION</h2>
<p> usage: blenderplayer [-w [w h l t]] [-f [fw fh fb ff]] [-g gamengineoptions] [-s stereomode] filename.blend</p>
<dl>
<dt> <code>-h</code>: Prints this command summary</p>
<dt> <code>-w</code>: display in a window</p>
<dt> <code>&#8211;Optional</code> parameters&#8211;</p>
<dt>
<dd>
<dd>w = window width h = window height</p>
<dt>
<dd> l = window left coordinate t = window top coordinate Note: If w or h is defined, both must be defined.</p>
<dt>
<dd> Also, if l or t is defined, all options must be used.</p>
<dt> <code>-f</code>: start game in full screen mode</p>
<dt> <code>&#8211;Optional</code> parameters&#8211;</p>
<dt>
<dd>
<dd>fw = full screen mode pixel width fh = full screen mode pixel height</p>
<dt>
<dd> fb = full screen mode bits per pixel ff = full screen mode frequency Note: If fw or fh is defined, both must be defined.</p>
<dt>
<dd> Also, if fb is used, fw and fh must be used. ff requires all options.</p>
<dt> <code>-s</code>: start player in stereo</p>
<dt>
<dd>stereomode: hwpageflip</p>
<dd> (Quad buffered shutter glasses)</p>
<dt>syncdoubling</p>
<dd> (Above Below)</p>
<dt>sidebyside</p>
<dd> (Left Right)</p>
<dt>anaglyph</p>
<dd> (Red-Blue glasses)</p>
<dt>vinterlace</p>
<dd> (Vertical interlace for autostereo display)</p>
<dt>
<dd> depending on the type of stereo you want</p>
<dt> <code>-D</code>: start player in dome mode</p>
<dt> <code>&#8211;Optional</code> parameters&#8211;</p>
<dt>
<dd>angle</p>
<dd> = field of view in degrees</p>
<dt>tilt</p>
<dd> = tilt angle in degrees</p>
<dt>
<dd> warpdata = a file to use for warping the image (absolute path) mode: fisheye (Fisheye)</p>
<dt>truncatedfront</p>
<dd> (Front-Truncated)</p>
<dt>truncatedrear</p>
<dd> (Rear-Truncated)</p>
<dt>cubemap</p>
<dd> (Cube Map)</p>
<dt>sphericalpanoramic</p>
<dd> (Spherical Panoramic)</p>
<dt>
<dd> depending on the type of dome you are using</p>
<dt> <code>-i</code>: parent windows ID</p>
<dt> <code>-d</code>: turn debugging on</p>
<dt> <code>-g</code>: game engine options:</p>
<dt>
<dd>Name</p>
<dd> Default Description</p>
<dt> <code>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;</code></p>
<dt>
<dd>fixedtime</p>
<dd> 0 &quot;Enable all frames&quot;</p>
<dt>nomipmap</p>
<dd> 0 Disable mipmaps</p>
<dt>show_framerate</p>
<dd> 0 Show the frame rate</p>
<dt>show_properties</p>
<dd> 0 Show debug properties</p>
<dt>show_profile</p>
<dd> 0 Show profiling information</p>
<dt>blender_material</p>
<dd> 0 Enable material settings</p>
<dt>ignore_deprecation_warnings</p>
<dd> 1 Ignore deprecation warnings</p>
<dt>
<dd> &#8211; : all arguments after this are ignored, allowing python to access them from sys.argv</dl>
<p> example: blenderplayer <code>-w</code> 320 200 10 10 <code>-g</code> noaudio//home//user//filename.blend example: blenderplayer <code>-g</code> show_framerate = 0 //home//user//filename.blend </p>
<h2>Index</h2>
