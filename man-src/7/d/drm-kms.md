---
title: "drm-kms(7)"
name: "drm-kms"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drm-kms/"
description: "drm-kms – Kernel Mode-Setting"
---

<p>drm-kms &#8211; Kernel Mode-Setting</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xf86drm.h&gt;
#include &lt;xf86drmMode.h&gt;</code></pre>
<h2>Description</h2>
<p>Each DRM device provides access to manage which monitors and displays are currently used and what frames to be displayed. This task is called <i>Kernel Mode-Setting</i> (KMS). Historically, this was done in user-space and called <i>User-space Mode-Setting</i> (UMS). Almost all open-source drivers now provide the KMS kernel API to do this in the kernel, however, many non-open-source binary drivers from different vendors still do not support this. You can use <code><a href="/docs/linux/man/3-drmmodesettingsupported/">drmModeSettingSupported</a></code>(3) to check whether your driver supports this. To understand how KMS works, we need to introduce 5 objects: <i>CRTCs</i>, <i>Planes</i>, <i>Encoders</i>, <i>Connectors</i> and <i>Framebuffers</i>. </p>
<p> CRTCs</p>
<dl>
<dd>A <i>CRTC</i> short for <i>CRT Controller</i> is an abstraction representing a part of the chip that contains a pointer to a scanout buffer. Therefore, the number of CRTCs available determines how many independent scanout buffers can be active at any given time. The CRTC structure contains several fields to support this: a pointer to some video memory (abstracted as a frame-buffer object), a list of driven connectors, a display mode and an (x, y) offset into the video memory to support panning or configurations where one piece of video memory spans multiple CRTCs. A CRTC is the central point where configuration of displays happens. You select which objects to use, which modes and which parameters and then configure each CRTC via <code><a href="/docs/linux/man/3-drmmodecrtcset/">drmModeCrtcSet</a></code>(3) to drive the display devices.</dl>
<p> Planes</p>
<dl>
<dd>A <i>plane</i> respresents an image source that can be blended with or overlayed on top of a CRTC during the scanout process. Planes are associated with a frame-buffer to crop a portion of the image memory (source) and optionally scale it to a destination size. The result is then blended with or overlayed on top of a CRTC. Planes are not provided by all hardware and the number of available planes is limited. If planes are not available or if not enough planes are available, the user should fall back to normal software blending (via GPU or CPU).</dl>
<p> Encoders</p>
<dl>
<dd>An <i>encoder</i> takes pixel data from a CRTC and converts it to a format suitable for any attached connectors. On some devices, it may be possible to have a CRTC send data to more than one encoder. In that case, both encoders would receive data from the same scanout buffer, resulting in a <i>cloned</i> display configuration across the connectors attached to each encoder.</dl>
<p> Connectors</p>
<dl>
<dd>A <i>connector</i> is the final destination of pixel-data on a device, and usually connects directly to an external display device like a monitor or laptop panel. A connector can only be attached to one encoder at a time. The connector is also the structure where information about the attached display is kept, so it contains fields for display data, <i>EDID</i> data, <i>DPMS</i> and <i>connection status</i>, and information about modes supported on the attached displays.</dl>
<p> Framebuffers</p>
<dl>
<dd><i>Framebuffers</i> are abstract memory objects that provide a source of pixel data to scanout to a CRTC. Applications explicitly request the creation of framebuffers and can control their behavior. Framebuffers rely on the underneath memory manager for low-level memory operations. When creating a framebuffer, applications pass a memory handle through the API which is used as backing storage. The framebuffer itself is only an abstract object with no data. It just refers to memory buffers that must be created with the <code><a href="/docs/linux/man/7-drm-memory/">drm-memory</a></code>(7) API.</dl>
<h3>Mode-Setting</h3>
<p>Before mode-setting can be performed, an application needs to call <code><a href="/docs/linux/man/3-drmsetmaster/">drmSetMaster</a></code>(3) to become <i>DRM-Master</i>. It then has exclusive access to the KMS API. A call to <code><a href="/docs/linux/man/3-drmmodegetresources/">drmModeGetResources</a></code>(3) returns a list of <i>CRTCs</i>, <i>Connectors</i>, <i>Encoders</i> and <i>Planes</i>. </p>
<p> Normal procedure now includes: First, you select which connectors you want to use. Users are mostly interested in which monitor or display-panel is active so you need to make sure to arrange them in the correct logical order and select the correct ones to use. For each connector, you need to find a CRTC to drive this connector. If you want to clone output to two or more connectors, you may use a single CRTC for all cloned connectors (if the hardware supports this). To find a suitable CRTC, you need to iterate over the list of encoders that are available for each connector. Each encoder contains a list of CRTCs that it can work with and you simply select one of these CRTCs. If you later program the CRTC to control a connector, it automatically selects the best encoder. However, this procedure is needed so your CRTC has at least one working encoder for the selected connector. See the <i>Examples</i> section below for more information. </p>
<p> All valid modes for a connector can be retrieved with a call to <code><a href="/docs/linux/man/3-drmmodegetconnector/">drmModeGetConnector</a></code>(3) You need to select the mode you want to use and save it. The first mode in the list is the default mode with the highest resolution possible and often a suitable choice. </p>
<p> After you have a working connector+CRTC+mode combination, you need to create a framebuffer that is used for scanout. Memory buffer allocation is driver-depedent and described in <code><a href="/docs/linux/man/7-drm-memory/">drm-memory</a></code>(7). You need to create a buffer big enough for your selected mode. Now you can create a framebuffer object that uses your memory-buffer as scanout buffer. You can do this with <code><a href="/docs/linux/man/3-drmmodeaddfb/">drmModeAddFB</a></code>(3) and <code><a href="/docs/linux/man/3-drmmodeaddfb2/">drmModeAddFB2</a></code>(3). </p>
<p> As a last step, you want to program your CRTC to drive your selected connector. You can do this with a call to <code><a href="/docs/linux/man/3-drmmodesetcrtc/">drmModeSetCrtc</a></code>(3).</p>
<h3>Page-Flipping</h3>
<p>A call to <code><a href="/docs/linux/man/3-drmmodesetcrtc/">drmModeSetCrtc</a></code>(3) is executed immediately and forces the CRTC to use the new scanout buffer. If you want smooth-transitions without tearing, you probably use double-buffering. You need to create one framebuffer object for each buffer you use. You can then call <code><a href="/docs/linux/man/3-drmmodesetcrtc/">drmModeSetCrtc</a></code>(3) on the next buffer to flip. If you want to synchronize your flips with <i>vertical-blanks</i>, you can use <code><a href="/docs/linux/man/3-drmmodepageflip/">drmModePageFlip</a></code>(3) which schedules your page-flip for the next <i>vblank</i>.</p>
<h3>Planes</h3>
<p>Planes are controlled independently from CRTCs. That is, a call to <code><a href="/docs/linux/man/3-drmmodesetcrtc/">drmModeSetCrtc</a></code>(3) does not affect planes. Instead, you need to call <code><a href="/docs/linux/man/3-drmmodesetplane/">drmModeSetPlane</a></code>(3) to configure a plane. This requires the plane ID, a CRTC, a framebuffer and offsets into the plane-framebuffer and the CRTC-framebuffer. The CRTC then blends the content from the plane over the CRTC framebuffer buffer during scanout. As this does not involve any software-blending, it is way faster than traditional blending. However, plane resources are limited. See <code><a href="/docs/linux/man/3-drmmodegetplaneresources/">drmModeGetPlaneResources</a></code>(3) for more information.</p>
<h3>Cursors</h3>
<p>Similar to planes, many hardware also supports cursors. A cursor is a very small buffer with an image that is blended over the CRTC framebuffer. You can set a different cursor for each CRTC with <code><a href="/docs/linux/man/3-drmmodesetcursor/">drmModeSetCursor</a></code>(3) and move it on the screen with <code><a href="/docs/linux/man/3-drmmodemovecursor/">drmModeMoveCursor</a></code>(3). This allows to move the cursor on the screen without rerendering. If no hardware cursors are supported, you need to rerender for each frame the cursor is moved.</p>
<h2>Examples</h2>
<p>Some examples of how basic mode-setting can be done. See the man-page of each DRM function for more information.</p>
<h3>CRTC/Encoder Selection</h3>
<p>If you retrieved all display configuration information via <code><a href="/docs/linux/man/3-drmmodegetresources/">drmModeGetResources</a></code>(3) as drmModeRes *<i>res</i>, selected a connector from the list in <i>res</i>-&gt;<i>connectors</i> and retrieved the connector-information as drmModeConnector *<i>conn</i> via <code><a href="/docs/linux/man/3-drmmodegetconnector/">drmModeGetConnector</a></code>(3) then this example shows, how you can find a suitable CRTC id to drive this connector. This function takes a file-descriptor to the DRM device (see <code><a href="/docs/linux/man/3-drmopen/">drmOpen</a></code>(3)) as <i>fd</i>, a pointer to the retrieved resources as <i>res</i> and a pointer to the selected connector as <i>conn</i>. It returns an integer smaller than 0 on failure, otherwise, a valid CRTC id is returned. </p>
<pre><code>static int modeset_find_crtc(int fd, drmModeRes *res, drmModeConnector *conn)
{
    drmModeEncoder *enc;
    unsigned int i, j;

    /* iterate all encoders of this connector */
    for (i = 0; i &lt; conn-&gt;count_encoders; ++i) {
        enc = drmModeGetEncoder(fd, conn-&gt;encoders[i]);
        if (!enc) {
            /* cannot retrieve encoder, ignoring... */
            continue;
        }

        /* iterate all global CRTCs */
        for (j = 0; j &lt; res-&gt;count_crtcs; ++j) {
            /* check whether this CRTC works with the encoder */
            if (!(enc-&gt;possible_crtcs &amp; (1 &lt;&lt; j)))
                continue;

            /* Here you need to check that no other connector
             * currently uses the CRTC with id &quot;crtc&quot;. If you intend
             * to drive one connector only, then you can skip this
             * step. Otherwise, simply scan your list of configured
             * connectors and CRTCs whether this CRTC is already
             * used. If it is, then simply continue the search here. */
            if (res-&gt;crtcs[j] &quot;is unused&quot;) {
                drmModeFreeEncoder(enc);
                return res-&gt;crtcs[j];
            }
        }

        drmModeFreeEncoder(enc);
    }

    /* cannot find a suitable CRTC */
    return -ENOENT;
}</code></pre>
<h2>Reporting Bugs</h2>
<p>Bugs in this manual should be reported to <a rel="nofollow" href="http://bugs.freedesktop.org">http://bugs.freedesktop.org</a> under the &quot;Mesa&quot; product, with &quot;Other&quot; or &quot;libdrm&quot; as the component.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-drm/">drm</a></code>(7), <code><a href="/docs/linux/man/7-drm-memory/">drm-memory</a></code>(7), <code><a href="/docs/linux/man/3-drmmodegetresources/">drmModeGetResources</a></code>(3), <code><a href="/docs/linux/man/3-drmmodegetconnector/">drmModeGetConnector</a></code>(3), <code><a href="/docs/linux/man/3-drmmodegetencoder/">drmModeGetEncoder</a></code>(3), <code><a href="/docs/linux/man/3-drmmodegetcrtc/">drmModeGetCrtc</a></code>(3), <code><a href="/docs/linux/man/3-drmmodesetcrtc/">drmModeSetCrtc</a></code>(3), <code><a href="/docs/linux/man/3-drmmodegetfb/">drmModeGetFB</a></code>(3), <code><a href="/docs/linux/man/3-drmmodeaddfb/">drmModeAddFB</a></code>(3), <code><a href="/docs/linux/man/3-drmmodeaddfb2/">drmModeAddFB2</a></code>(3), <code><a href="/docs/linux/man/3-drmmodermfb/">drmModeRmFB</a></code>(3), <code><a href="/docs/linux/man/3-drmmodepageflip/">drmModePageFlip</a></code>(3), <code><a href="/docs/linux/man/3-drmmodegetplaneresources/">drmModeGetPlaneResources</a></code>(3), <code><a href="/docs/linux/man/3-drmmodegetplane/">drmModeGetPlane</a></code>(3), <code><a href="/docs/linux/man/3-drmmodesetplane/">drmModeSetPlane</a></code>(3), <code><a href="/docs/linux/man/3-drmmodesetcursor/">drmModeSetCursor</a></code>(3), <code><a href="/docs/linux/man/3-drmmodemovecursor/">drmModeMoveCursor</a></code>(3), <code><a href="/docs/linux/man/3-drmsetmaster/">drmSetMaster</a></code>(3), <code><a href="/docs/linux/man/3-drmavailable/">drmAvailable</a></code>(3), <code><a href="/docs/linux/man/3-drmcheckmodesettingsupported/">drmCheckModesettingSupported</a></code>(3), <code><a href="/docs/linux/man/3-drmopen/">drmOpen</a></code>(3) </p>
