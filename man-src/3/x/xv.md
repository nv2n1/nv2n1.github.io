---
title: "xv(3)"
name: "xv"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xv/"
description: "Xv – X Window System video extension"
---

<p>Xv &#8211; X Window System video extension </p>
<h2>Description</h2>
<p>The X Video Extension (Xv) extension provides support for video adaptors attached to an X display. It takes the approach that a display may have one or more video adaptors, each of which has one or more ports through which independent video streams pass. </p>
<p> An adaptor may be able to display video in a drawable, capture video from a drawable, or both. It translates between video encoding (NTSC, PAL, SECAM, etc&#8230;) and drawable format (depth and visual-id pair). An adaptor may support multiple video encodings and/or multiple drawable formats. </p>
<p> Clients use <code><a href="/docs/linux/man/3-xv/">Xv</a></code>(3) to gain access and manage sharing of a display&#8217;s video resources. Typically, a client will use <code><a href="/docs/linux/man/3-xvqueryextension/">XvQueryExtension</a></code>(3) to determine the status of the extension, <code><a href="/docs/linux/man/3-xvqueryadaptors/">XvQueryAdaptors</a></code>(3) to get a description of what video adaptors exist, and <code><a href="/docs/linux/man/3-xvqueryencodings/">XvQueryEncodings</a></code>(3) to get a description of what video encodings an adaptor supports. </p>
<p> Once a client has determined what video resources are available, it is free to put video into a drawable or get video from a drawable, according the capabilities supported. Clients can select to receive events when video activity changes in a drawable and when port attributes have changed. </p>
<p> The Xv protocol version 2.2 and later is extended to support client images in alternate colorspaces (XvImages). Xv adaptors which are capable of displaying XvImages will have the XvImageMask field set in the type field of the XvAdaptorInfo. XvImage formats supported by the port may be queried with <code><a href="/docs/linux/man/3-xvlistimageformats/">XvListImageFormats</a></code>(3). XvImages may be created with the help of <code><a href="/docs/linux/man/3-xvcreateimage/">XvCreateImage</a></code>(3) or <code><a href="/docs/linux/man/3-xvshmcreateimage/">XvShmCreateImage</a></code>(3); XvImages may be displayed with <code><a href="/docs/linux/man/3-xvputimage/">XvPutImage</a></code>(3) or <code><a href="/docs/linux/man/3-xvshmputimage/">XvShmPutImage</a></code>(3). The Port attributes of the port specified in the Xv(Shm)PutImage command will be valid for the image operation when applicable. There will be a port encoding with the name &quot;XV_IMAGE&quot;. The width and height of that encoding will indicate the maximum source image size.</p>
<h2>Summary Of Library Functions</h2>
<p>The following is a summary of Xv library functions and events: </p>
<p> <code><a href="/docs/linux/man/3-xvcreateimage/">XvCreateImage</a></code>(3) &#8211; create an XvImage </p>
<p> <code><a href="/docs/linux/man/3-xvgetportattribute/">XvGetPortAttribute</a></code>(3) &#8211; return current port attribute value </p>
<p> <code><a href="/docs/linux/man/3-xvgetstill/">XvGetStill</a></code>(3) &#8211; capture a single frame of video from a drawable </p>
<p> <code><a href="/docs/linux/man/3-xvgetvideo/">XvGetVideo</a></code>(3) &#8211; capture video from a drawable </p>
<p> <code><a href="/docs/linux/man/3-xvgrabport/">XvGrabPort</a></code>(3) &#8211; lock port for exclusive use by client </p>
<p> <code><a href="/docs/linux/man/3-xvlistimageformats/">XvListImageFormats</a></code>(3) &#8211; return list of image formats for a port </p>
<p> <code><a href="/docs/linux/man/3-xvportnotify/">XvPortNotify</a></code>(3) &#8211; event generated when port attributes change </p>
<p> <code><a href="/docs/linux/man/3-xvputimage/">XvPutImage</a></code>(3) &#8211; write a XvImage to a drawable </p>
<p> <code><a href="/docs/linux/man/3-xvputstill/">XvPutStill</a></code>(3) &#8211; write a single frame of video to a drawable </p>
<p> <code><a href="/docs/linux/man/3-xvputvideo/">XvPutVideo</a></code>(3) &#8211; write video into a drawable </p>
<p> <code><a href="/docs/linux/man/3-xvqueryadaptors/">XvQueryAdaptors</a></code>(3) &#8211; return adaptor information for a screen </p>
<p> <code><a href="/docs/linux/man/3-xvquerybestsize/">XvQueryBestSize</a></code>(3) &#8211; determine the optimum drawable region size </p>
<p> <code><a href="/docs/linux/man/3-xvqueryencodings/">XvQueryEncodings</a></code>(3) &#8211; return list of encodings for an adaptor </p>
<p> <code><a href="/docs/linux/man/3-xvqueryextension/">XvQueryExtension</a></code>(3) &#8211; return version and revision of extension </p>
<p> <code><a href="/docs/linux/man/3-xvqueryportattributes/">XvQueryPortAttributes</a></code>(3) &#8211; return list of attributes of a port </p>
<p> <code><a href="/docs/linux/man/3-xvselectportnotify/">XvSelectPortNotify</a></code>(3) &#8211; enable or disable XvPortNotify events </p>
<p> <code><a href="/docs/linux/man/3-xvselectvideonotify/">XvSelectVideoNotify</a></code>(3) &#8211; enable or disable XvVideoNotify events </p>
<p> <code><a href="/docs/linux/man/3-xvsetportattribute/">XvSetPortAttribute</a></code>(3) &#8211; set an attribute for a port </p>
<p> <code><a href="/docs/linux/man/3-xvshmcreateimage/">XvShmCreateImage</a></code>(3) &#8211; create an XvImage in shared memory </p>
<p> <code><a href="/docs/linux/man/3-xvshmputimage/">XvShmPutImage</a></code>(3) &#8211; write a XvImage in shared memory to a drawable </p>
<p> <code><a href="/docs/linux/man/3-xvstopvideo/">XvStopVideo</a></code>(3) &#8211; stop active video </p>
<p> <code><a href="/docs/linux/man/3-xvungrabport/">XvUngrabPort</a></code>(3) &#8211; release a grabbed port </p>
<p> <code><a href="/docs/linux/man/3-xvvideonotify/">XvVideoNotify</a></code>(3) &#8211; event generated for video processing </p>
<p> Each of these functions and events is described in its own Xv man page.</p>
