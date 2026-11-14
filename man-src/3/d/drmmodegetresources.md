---
title: "drmmodegetresources(3)"
name: "drmmodegetresources"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmmodegetresources/"
description: "drmModeGetResources – retrieve current display configuration information"
---

<p>drmModeGetResources &#8211; retrieve current display configuration information </p>
<h2>Synopsis</h2>
<pre>#include &lt;xf86drm.h&gt;</pre>
<pre>#include &lt;xf86drmMode.h&gt;</pre>
<dl COMPACT>
<dt> <code>drmModeResPtr drmModeGetResources(int&nbsp;<wbr></code><i>fd</i><code>);</code></dl>
<h2>Description</h2>
<p><code>drmModeGetResources</code></p>
<dd>allocates, populates, and returns a drmModeRes structure containing information about the current display configuration. The structure contains the following fields: </p>
<dl COMPACT>
<dd>
<pre>typedef struct _drmModeRes {
 int count_fbs;
 uint32_t *fbs;
 int count_crtcs;
 uint32_t *crtcs;
 int count_connectors;
 uint32_t *connectors;
 int count_encoders;
 uint32_t *encoders;
 uint32_t min_width, max_width;
 uint32_t min_height, max_height;
} drmModeRes, *drmModeResPtr;</pre>
</dl>
<p> The <i>count_fbs</i> and <i>fbs</i> fields indicate the number of currently allocated framebuffer objects (i.e., objects that can be attached to a given CRTC or sprite for display). </p>
<p> The <i>count_crtcs</i> and <i>crtcs</i> fields list the available CRTCs in the configuration. A CRTC is simply an object that can scan out a framebuffer to a display sink, and contains mode timing and relative position information. CRTCs drive encoders, which are responsible for converting the pixel stream into a specific display protocol (e.g., MIPI or HDMI). </p>
<p> The <i>count_connectors</i> and <i>connectors</i> fields list the available physical connectors on the system. Note that some of these may not be exposed from the chassis (e.g., LVDS or eDP). Connectors are attached to encoders and contain information about the attached display sink (e.g., width and height in mm, subpixel ordering, and various other properties). </p>
<p> The <i>count_encoders</i> and <i>encoders</i> fields list the available encoders on the device. Each encoder may be associated with a CRTC, and may be used to drive a particular encoder. </p>
<p> The <i>min*</i> and <i>max*</i> fields indicate the maximum size of a framebuffer for this device (i.e., the scanout size limit).</p>
<h2>Return Value</h2>
<p><code>drmModeGetResources</code> returns a drmModeRes structure pointer on success, NULL on failure. The returned structure must be freed with <code><a href="/docs/linux/man/3-drmmodefreeresources/">drmModeFreeResources</a></code>(3).</p>
<h2>Reporting Bugs</h2>
<p>Bugs in this function should be reported to <a rel="nofollow" href="http://bugs.freedesktop.org">http://bugs.freedesktop.org</a> under the &quot;Mesa&quot; product, with &quot;Other&quot; or &quot;libdrm&quot; as the component.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-drm/">drm</a></code>(7), <code><a href="/docs/linux/man/7-drm-kms/">drm-kms</a></code>(7), <code><a href="/docs/linux/man/3-drmmodegetfb/">drmModeGetFB</a></code>(3), <code><a href="/docs/linux/man/3-drmmodeaddfb/">drmModeAddFB</a></code>(3), <code><a href="/docs/linux/man/3-drmmodeaddfb2/">drmModeAddFB2</a></code>(3), <code><a href="/docs/linux/man/3-drmmodermfb/">drmModeRmFB</a></code>(3), <code><a href="/docs/linux/man/3-drmmodedirtyfb/">drmModeDirtyFB</a></code>(3), <code><a href="/docs/linux/man/3-drmmodegetcrtc/">drmModeGetCrtc</a></code>(3), <code><a href="/docs/linux/man/3-drmmodesetcrtc/">drmModeSetCrtc</a></code>(3), <code><a href="/docs/linux/man/3-drmmodegetencoder/">drmModeGetEncoder</a></code>(3), <code><a href="/docs/linux/man/3-drmmodegetconnector/">drmModeGetConnector</a></code>(3)</p>
