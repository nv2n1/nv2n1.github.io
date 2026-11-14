---
title: "drm-gem(7)"
name: "drm-gem"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drm-gem/"
description: "drm-memory, drm-mm, drm-gem, drm-ttm – DRM Memory Management"
---

<p>drm-memory, drm-mm, drm-gem, drm-ttm &#8211; DRM Memory Management</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xf86drm.h&gt;</code></pre>
<h2>Description</h2>
<p>Many modern high-end GPUs come with their own memory managers. They even include several different caches that need to be synchronized during access. Textures, framebuffers, command buffers and more need to be stored in memory that can be accessed quickly by the GPU. Therefore, memory management on GPUs is highly driver- and hardware-dependent. However, there are several frameworks in the kernel that are used by more than one driver. These can be used for trivial mode-setting without requiring driver-dependent code. But for hardware-accelerated rendering you need to read the manual pages for the driver you want to work with.</p>
<h3>Dumb-Buffers</h3>
<p>Almost all in-kernel DRM hardware drivers support an API called <i>Dumb-Buffers</i>. This API allows to create buffers of arbitrary size that can be used for scanout. These buffers can be memory mapped via <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) so you can render into them on the CPU. However, GPU access to these buffers is often not possible. Therefore, they are fine for simple tasks but not suitable for complex compositions and renderings. The <code>DRM_IOCTL_MODE_CREATE_DUMB</code> ioctl can be used to create a dumb buffer. The kernel will return a 32bit handle that can be used to manage the buffer with the DRM API. You can create framebuffers with <code><a href="/docs/linux/man/3-drmmodeaddfb/">drmModeAddFB</a></code>(3) and use it for mode-setting and scanout. To access the buffer, you first need to retrieve the offset of the buffer. The <code>DRM_IOCTL_MODE_MAP_DUMB</code> ioctl requests the DRM subsystem to prepare the buffer for memory-mapping and returns a fake-offset that can be used with <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). The <code>DRM_IOCTL_MODE_CREATE_DUMB</code> ioctl takes as argument a structure of type struct drm_mode_create_dumb: struct drm_gem_open {<br />
    __u32 name;</p>
<p>    __u32 handle;<br />
    __u32 size;<br />
}; The fields <i>height</i>, <i>width</i>, <i>bpp</i> and <i>flags</i> have to be provided by the caller. The other fields are filled by the kernel with the return values. <i>height</i> and <i>width</i> are the dimensions of the rectangular buffer that is created. <i>bpp</i> is the number of bits-per-pixel and must be a multiple of 8. You most commonly want to pass 32 here. The <i>flags</i> field is currently unused and must be zeroed. Different flags to modify the behavior may be added in the future. After calling the ioctl, the <i>handle</i>, <i>pitch</i> and <i>size</i> fields are filled by the kernel. <i>handle</i> is a 32bit gem handle that identifies the buffer. This is used by several other calls that take a gem-handle or memory-buffer as argument. The <i>pitch</i> field is the pitch (or stride) of the new buffer. Most drivers use 32bit or 64bit aligned stride-values. The <i>size</i> field contains the absolute size in bytes of the buffer. This can normally also be computed with <i>(height * pitch + width) * bpp / 4</i>. To prepare the buffer for <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) you need to use the <code>DRM_IOCTL_MODE_MAP_DUMB</code> ioctl. It takes as argument a structure of type struct drm_mode_map_dumb: struct drm_gem_open {<br />
    __u32 name;</p>
<p>    __u32 handle;<br />
    __u32 size;<br />
}; You need to put the gem-handle that was previously retrieved via <code>DRM_IOCTL_MODE_CREATE_DUMB</code> into the <i>handle</i> field. The <i>pad</i> field is unused padding and must be zeroed. After completion, the <i>offset</i> field will contain an offset that can be used with <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) on the DRM file-descriptor. If you don&#8217;t need your dumb-buffer, anymore, you have to destroy it with <code>DRM_IOCTL_MODE_DESTROY_DUMB</code>. If you close the DRM file-descriptor, all open dumb-buffers are automatically destroyed. This ioctl takes as argument a structure of type struct drm_mode_destroy_dumb: struct drm_gem_open {<br />
    __u32 name;</p>
<p>    __u32 handle;<br />
    __u32 size;<br />
}; You only need to put your handle into the <i>handle</i> field. After this call, the handle is invalid and may be reused for new buffers by the dumb-API.</p>
<h3>Ttm</h3>
<p><i>TTM</i> stands for <i>Translation Table Manager</i> and is a generic memory-manager provided by the kernel. It does not provide a common user-space API so you need to look at each driver interface if you want to use it. See for instance the radeon manpages for more information on memory-management with radeon and TTM.</p>
<h3>Gem</h3>
<p><i>GEM</i> stands for <i>Graphics Execution Manager</i> and is a generic DRM memory-management framework in the kernel, that is used by many different drivers. Gem is designed to manage graphics memory, control access to the graphics device execution context and handle essentially NUMA environment unique to modern graphics hardware. Gem allows multiple applications to share graphics device resources without the need to constantly reload the entire graphics card. Data may be shared between multiple applications with gem ensuring that the correct memory synchronization occurs. Gem provides simple mechanisms to manage graphics data and control execution flow within the linux DRM subsystem. However, gem is not a complete framework that is fully driver independent. Instead, if provides many functions that are shared between many drivers, but each driver has to implement most of memory-management with driver-dependent ioctls. This manpage tries to describe the semantics (and if it applies, the syntax) that is shared between all drivers that use gem. All GEM APIs are defined as <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) on the DRM file descriptor. An application must be authorized via <code><a href="/docs/linux/man/3-drmauthmagic/">drmAuthMagic</a></code>(3) to the current DRM-Master to access the GEM subsystem. A driver that does not support gem will return <code>ENODEV</code> for all these ioctls. Invalid object handles return <code>EINVAL</code> and invalid object names return <code>ENOENT</code>. Gem provides explicit memory management primitives. System pages are allocated when the object is created, either as the fundamental storage for hardware where system memory is used by the graphics processor directly, or as backing store for graphics-processor resident memory. Objects are referenced from user-space using handles. These are, for all intents and purposes, equivalent to file descriptors but avoid the overhead. Newer kernel drivers also support the <code><a href="/docs/linux/man/7-drm-prime/">drm-prime</a></code>(7) infrastructure which can return real file-descriptor for gem-handles using the linux dma-buf API. Objects may be published with a name so that other applications and processes can access them. The name remains valid as long as the object exists. Gem-objects are reference counted in the kernel. The object is only destroyed when all handles from user-space were closed. Gem-buffers cannot be created with a generic API. Each driver provides its own API to create gem-buffers. See for example <code>DRM_I915_GEM_CREATE</code>, <code>DRM_NOUVEAU_GEM_NEW</code> or <code>DRM_RADEON_GEM_CREATE</code>. Each of these ioctls returns a gem-handle that can be passed to different generic ioctls. The <i>libgbm</i> library from the <i>mesa3D</i> distribution tries to provide a driver-independent API to create gbm buffers and retrieve a gbm-handle to them. It allows to create buffers for different use-cases including scanout, rendering, cursors and CPU-access. See the libgbm library for more information or look at the driver-dependent man-pages (for example <code><a href="/docs/linux/man/7-drm-intel/">drm-intel</a></code>(7) or <code><a href="/docs/linux/man/7-drm-radeon/">drm-radeon</a></code>(7)). Gem-buffers can be closed with the <code>DRM_IOCTL_GEM_CLOSE</code> ioctl. It takes as argument a structure of type struct drm_gem_close: struct drm_gem_open {<br />
    __u32 name;</p>
<p>    __u32 handle;<br />
    __u32 size;<br />
}; The <i>handle</i> field is the gem-handle to be closed. The <i>pad</i> field is unused padding. It must be zeroed. After this call the gem handle cannot be used by this process anymore and may be reused for new gem objects by the gem API. If you want to share gem-objects between different processes, you can create a name for them and pass this name to other processes which can then open this gem-object. Names are currently 32bit integer IDs and have no special protection. That is, if you put a name on your gem-object, every other client that has access to the DRM device and is authenticated via <code><a href="/docs/linux/man/3-drmauthmagic/">drmAuthMagic</a></code>(3) to the current DRM-Master, can <i>guess</i> the name and open or access the gem-object. If you want more fine-grained access control, you can use the new <code><a href="/docs/linux/man/7-drm-prime/">drm-prime</a></code>(7) API to retrieve file-descriptors for gem-handles. To create a name for a gem-handle, you use the <code>DRM_IOCTL_GEM_FLINK</code> ioctl. It takes as argument a structure of type struct drm_gem_flink: struct drm_gem_open {<br />
    __u32 name;</p>
<p>    __u32 handle;<br />
    __u32 size;<br />
}; You have to put your handle into the <i>handle</i> field. After completion, the kernel has put the new unique name into the <i>name</i> field. You can now pass this name to other processes which can then import the name with the <code>DRM_IOCTL_GEM_OPEN</code> ioctl. It takes as argument a structure of type struct drm_gem_open: struct drm_gem_open {<br />
    __u32 name;</p>
<p>    __u32 handle;<br />
    __u32 size;<br />
}; You have to fill in the <i>name</i> field with the name of the gem-object that you want to open. The kernel will fill in the <i>handle</i> and <i>size</i> fields with the new handle and size of the gem-object. You can now access the gem-object via the handle as if you created it with the gem API. Besides generic buffer management, the GEM API does not provide any generic access. Each driver implements its own functionality on top of this API. This includes execution-buffers, GTT management, context creation, CPU access, GPU I/O and more. The next higher-level API is <i>OpenGL</i>. So if you want to use more GPU features, you should use the <i>mesa3D</i> library to create OpenGL contexts on DRM devices. This does <i>not</i> require any windowing-system like X11, but can also be done on raw DRM devices. However, this is beyond the scope of this man-page. You may have a look at other mesa3D manpages, including libgbm and libEGL. 2D software-rendering (rendering with the CPU) can be achieved with the dumb-buffer-API in a driver-independent fashion, however, for hardware-accelerated 2D or 3D rendering you must use OpenGL. Any other API that tries to abstract the driver-internals to access GEM-execution-buffers and other GPU internals, would simply reinvent OpenGL so it is not provided. But if you need more detailed information for a specific driver, you may have a look into the driver-manpages, including <code><a href="/docs/linux/man/7-drm-intel/">drm-intel</a></code>(7), <code><a href="/docs/linux/man/7-drm-radeon/">drm-radeon</a></code>(7) and <code><a href="/docs/linux/man/7-drm-nouveau/">drm-nouveau</a></code>(7). However, the <code><a href="/docs/linux/man/7-drm-prime/">drm-prime</a></code>(7) infrastructure and the generic gem API as described here allow display-managers to handle graphics-buffers and render-clients without any deeper knowledge of the GPU that is used. Moreover, it allows to move objects between GPUs and implement complex display-servers that don&#8217;t do any rendering on their own. See its man-page for more information.</p>
<h2>Examples</h2>
<p>This section includes examples for basic memory-management tasks.</p>
<h3>Dumb-Buffers</h3>
<p>This examples shows how to create a dumb-buffer via the generic DRM API. This is driver-independent (as long as the driver supports dumb-buffers) and provides memory-mapped buffers that can be used for scanout. This example creates a full-HD 1920&#215;1080 buffer with 32 bits-per-pixel and a color-depth of 24 bits. The buffer is then bound to a framebuffer which can be used for scanout with the KMS API (see <code><a href="/docs/linux/man/7-drm-kms/">drm-kms</a></code>(7)). </p>
<pre><code>struct drm_mode_create_dumb creq;
struct drm_mode_destroy_dumb dreq;
struct drm_mode_map_dumb mreq;
uint32_t fb;
int ret;
void *map;

/* create dumb buffer */
memset(&amp;creq, 0, sizeof(creq));
creq.width = 1920;
creq.height = 1080;
creq.bpp = 32;
ret = drmIoctl(fd, DRM_IOCTL_MODE_CREATE_DUMB, &amp;creq);
if (ret &lt; 0) {
    /* buffer creation failed; see &quot;errno&quot; for more error codes */
    ...
}
/* creq.pitch, creq.handle and creq.size are filled by this ioctl with
 * the requested values and can be used now. */

/* create framebuffer object for the dumb-buffer */
ret = drmModeAddFB(fd, 1920, 1080, 24, 32, creq.pitch, creq.handle, &amp;fb);
if (ret) {
    /* frame buffer creation failed; see &quot;errno&quot; */
    ...
}
/* the framebuffer &quot;fb&quot; can now used for scanout with KMS */

/* prepare buffer for memory mapping */
memset(&amp;mreq, 0, sizeof(mreq));
mreq.handle = creq.handle;
ret = drmIoctl(fd, DRM_IOCTL_MODE_MAP_DUMB, &amp;mreq);
if (ret) {
    /* DRM buffer preparation failed; see &quot;errno&quot; */
    ...
}
/* mreq.offset now contains the new offset that can be used with mmap() */

/* perform actual memory mapping */
map = mmap(0, creq.size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, mreq.offset);
if (map == MAP_FAILED) {
    /* memory-mapping failed; see &quot;errno&quot; */
    ...
}

/* clear the framebuffer to 0 */
memset(map, 0, creq.size);</code></pre>
<h2>Reporting Bugs</h2>
<p>Bugs in this manual should be reported to <a rel="nofollow" href="http://bugs.freedesktop.org">http://bugs.freedesktop.org</a> under the &quot;Mesa&quot; product, with &quot;Other&quot; or &quot;libdrm&quot; as the component.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-drm/">drm</a></code>(7), <code><a href="/docs/linux/man/7-drm-kms/">drm-kms</a></code>(7), <code><a href="/docs/linux/man/7-drm-prime/">drm-prime</a></code>(7), <code><a href="/docs/linux/man/3-drmavailable/">drmAvailable</a></code>(3), <code><a href="/docs/linux/man/3-drmopen/">drmOpen</a></code>(3), <code><a href="/docs/linux/man/7-drm-intel/">drm-intel</a></code>(7), <code><a href="/docs/linux/man/7-drm-radeon/">drm-radeon</a></code>(7), <code><a href="/docs/linux/man/7-drm-nouveau/">drm-nouveau</a></code>(7) </p>
