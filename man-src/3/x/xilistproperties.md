---
title: "xilistproperties(3)"
name: "xilistproperties"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xilistproperties/"
---

XIListProperties - List a device's properties. 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput2.h&gt;</pre><pre>Atom* XListProperties( Display *display,
 int deviceid,
 int *nprops_return);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>deviceid
 The device to list the properties for.</pre><pre>nprops_return
 Specifies the number of Atoms returned.</pre><h2>Description</h2>The XIListProperties function returns a list of the properties associated with the input device specified with deviceid. Each device may have an arbitrary number of properties attached, some of which were created by the driver and/or server, others created by clients at runtime. 

 The client is expected to free the list of properties using XFree. 

 XIListProperties can generate a BadDevice error.
<h2>Diagnostics</h2>BadDevice An invalid device was specified. The device does not exist.
<h2>See Also</h2><a HREF="/docs/linux/man/3-xichangeproperty/">XIChangeProperty</a>(3), <a HREF="/docs/linux/man/3-xigetproperty/">XIGetProperty</a>(3), <a HREF="/docs/linux/man/3-xideleteproperty/">XIDeleteProperty</a>(3)
