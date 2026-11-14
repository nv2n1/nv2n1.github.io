---
title: "drm(7)"
name: "drm"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drm/"
description: "drm – Direct Rendering Manager"
---

<p>drm &#8211; Direct Rendering Manager</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xf86drm.h&gt;</code></pre>
<h2>Description</h2>
<p>The <i>Direct Rendering Manager</i> (DRM) is a framework to manage <i>Graphics Processing Units</i> (GPUs). It is designed to support the needs of complex graphics devices, usually containing programmable pipelines well suited to 3D graphics acceleration. Furthermore, it is responsible for memory management, interrupt handling and DMA to provide a uniform interface to applications. </p>
<p> In earlier days, the kernel framework was solely used to provide raw hardware access to priviledged user-space processes which implement all the hardware abstraction layers. But more and more tasks where moved into the kernel. All these interfaces are based on <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) commands on the DRM character device. The <i>libdrm</i> library provides wrappers for these system-calls and many helpers to simplify the API. </p>
<p> When a GPU is detected, the DRM system loads a driver for the detected hardware type. Each connected GPU is then presented to user-space via a character-device that is usually available as /dev/dri/card0 and can be accessed with <code><a href="/docs/linux/man/2-open/">open</a></code>(2) and <code><a href="/docs/linux/man/2-close/">close</a></code>(2). However, it still depends on the grapics driver which interfaces are available on these devices. If an interface is not available, the syscalls will fail with EINVAL.</p>
<h3>Authentication</h3>
<p>All DRM devices provide authentication mechanisms. Only a DRM-Master is allowed to perform mode-setting or modify core state and only one user can be DRM-Master at a time. See <code><a href="/docs/linux/man/3-drmsetmaster/">drmSetMaster</a></code>(3) for information on how to become DRM-Master and what the limitations are. Other DRM users can be authenticated to the DRM-Master via <code><a href="/docs/linux/man/3-drmauthmagic/">drmAuthMagic</a></code>(3) so they can perform buffer allocations and rendering.</p>
<h3>Mode-Setting</h3>
<p>Managing connected monitors and displays and changing the current modes is called <i>Mode-Setting</i>. This is restricted to the current DRM-Master. Historically, this was implemented in user-space, but new DRM drivers implement a kernel interface to perform mode-setting called <i>Kernel Mode Setting</i> (KMS). If your hardware-driver supports it, you can use the KMS API provided by DRM. This includes allocating framebuffers, selecting modes and managing CRTCs and encoders. See <code><a href="/docs/linux/man/7-drm-kms/">drm-kms</a></code>(7) for more.</p>
<h3>Memory Management</h3>
<p>The most sophisticated tasks for GPUs today is managing memory objects. Textures, framebuffers, command-buffers and all other kinds of commands for the GPU have to be stored in memory. The DRM driver takes care of managing all memory objects, flushing caches, synchronizing access and providing CPU access to GPU memory. All memory management is hardware driver dependent. However, two generic frameworks are available that are used by most DRM drivers. These are the <i>Translation Table Manager</i> (TTM) and the <i>Graphics Execution Manager</i> (GEM). They provide generic APIs to create, destroy and access buffers from user-space. However, there are still many differences between the drivers so driver-depedent code is still needed. Many helpers are provided in <i>libgbm</i> (Graphics Buffer Manager) from the <i>mesa-project</i>. For more information on DRM memory-management, see <code><a href="/docs/linux/man/7-drm-memory/">drm-memory</a></code>(7).</p>
<h2>Reporting Bugs</h2>
<p>Bugs in this manual should be reported to <a rel="nofollow" href="http://bugs.freedesktop.org">http://bugs.freedesktop.org</a> under the &quot;Mesa&quot; product, with &quot;Other&quot; or &quot;libdrm&quot; as the component.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-drm-kms/">drm-kms</a></code>(7), <code><a href="/docs/linux/man/7-drm-memory/">drm-memory</a></code>(7), <code><a href="/docs/linux/man/3-drmsetmaster/">drmSetMaster</a></code>(3), <code><a href="/docs/linux/man/3-drmauthmagic/">drmAuthMagic</a></code>(3), <code><a href="/docs/linux/man/3-drmavailable/">drmAvailable</a></code>(3), <code><a href="/docs/linux/man/3-drmopen/">drmOpen</a></code>(3) </p>
