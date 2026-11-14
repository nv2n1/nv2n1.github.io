---
title: "dmx(3)"
name: "dmx"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmx/"
description: "DMX – X Window System DMX (Distributed Multihead X) extension"
---

<p>DMX &#8211; X Window System DMX (Distributed Multihead X) extension</p>
<h2>Description</h2>
<p>The DMX extension provides support for communication with and control of <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) server. Attributes of the <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) server and of the back-end screens attached to the server can be queried and modified via this protocol.</p>
<h2>Summary Of Library Functions</h2>
<p>The following is a summary of DMX library functions: </p>
<p> <a href="/docs/linux/man/3-dmxqueryextension/">DMXQueryExtension</a>(3) &#8211; determine if DMX is available </p>
<p> <a href="/docs/linux/man/3-dmxqueryversion/">DMXQueryVersion</a>(3) &#8211; determine DMX extension version </p>
<p> <a href="/docs/linux/man/3-dmxsync/">DMXSync</a>(3) &#8211; flush protocol requests between <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) and back-end X servers </p>
<p> <a href="/docs/linux/man/3-dmxforcewindowcreation/">DMXForceWindowCreation</a>(3) &#8211; force immediate back-end window creation </p>
<p> <a href="/docs/linux/man/3-dmxgetscreencount/">DMXGetScreenCount</a>(3) &#8211; determine number of back-end screens </p>
<p> <a href="/docs/linux/man/3-dmxgetscreenattributes/">DMXGetScreenAttributes</a>(3) &#8211; determine back-end screen attributes </p>
<p> <a href="/docs/linux/man/3-dmxchangescreensattributes/">DMXChangeScreensAttributes</a>(3) &#8211; change back-end screen attributes </p>
<p> <a href="/docs/linux/man/3-dmxaddscreen/">DMXAddScreen</a>(3) &#8211; attach a new back-end screen </p>
<p> <a href="/docs/linux/man/3-dmxremovescreen/">DMXRemoveScreen</a>(3) &#8211; detach a back-end screen </p>
<p> <a href="/docs/linux/man/3-dmxgetwindowattributes/">DMXGetWindowAttributes</a>(3) &#8211; determine back-end window attributes </p>
<p> <a href="/docs/linux/man/3-dmxgetdesktopattributes/">DMXGetDesktopAttributes</a>(3) &#8211; determine global bounding box </p>
<p> <a href="/docs/linux/man/3-dmxchangedesktopattributes/">DMXChangeDesktopAttributes</a>(3) &#8211; change global bounding box </p>
<p> <a href="/docs/linux/man/3-dmxgetinputcount/">DMXGetInputCount</a>(3) &#8211; determine number of input devices </p>
<p> <a href="/docs/linux/man/3-dmxgetinputattributes/">DMXGetInputAttributes</a>(3) &#8211; determine input device attributes </p>
<p> <a href="/docs/linux/man/3-dmxaddinput/">DMXAddInput</a>(3) &#8211; attach a new backend or console input </p>
<p> <a href="/docs/linux/man/3-dmxremoveinput/">DMXRemoveInput</a>(3) &#8211; detach an input </p>
<p> <a href="/docs/linux/man/3-dmxaddbackendinput/">DMXAddBackendInput</a>(3) &#8211; attach a new back-end input </p>
<p> <a href="/docs/linux/man/3-dmxaddconsoleinput/">DMXAddConsoleInput</a>(3) &#8211; attach a new console input </p>
<p> Each of these functions is described in its own man page.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1), <code><a href="/docs/linux/man/1-xdmxconfig/">xdmxconfig</a></code>(1), <code><a href="/docs/linux/man/1-vdltodmx/">vdltodmx</a></code>(1)</p>
