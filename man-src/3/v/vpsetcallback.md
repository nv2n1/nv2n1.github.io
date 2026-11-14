---
title: "vpsetcallback(3)"
name: "vpsetcallback"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetcallback/"
description: "vpSetCallback – define a callback function"
---

<p>vpSetCallback &#8211; define a callback function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetCallback(</code><i>vpc, option, func</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>option;</i></p>
<dd>void <i>(*func)();</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>option</i></p>
<dd>A code specifying which callback function to set.</p>
<dt><i>func</i></p>
<dd>A pointer to the callback function.</dl>
<h2>Description</h2>
<p><code>vpSetCallback</code> is used to set a callback function. The following list gives the possible values for <i>option:</i></p>
<dl>
<dt>VP_GRAY_SHADE_FUNC</p>
<dd>The <i>func</i> argument is a shading callback function that produces a floating point grayscale pixel intensity. The function should be declared:</p>
<dl>
<dd>
<dl>
<dd>void <i>func</i>(void *<i>voxel_ptr,</i> float *<i>i_ptr</i>,<br />
 void *<i>client_data</i>);</dl>
<dl>
<dt><i>voxel_ptr</i></p>
<dd>Pointer to the beginning of a voxel that must be shaded.</p>
<dt><i>i_ptr</i></p>
<dd>Location into which the function should store the grayscale intensity result. It should be a single-precision floating point in the range 0.0 (black) to 1.0 (white).</p>
<dt><i>client_data</i></p>
<dd>Pointer to the application-defined client data (see <a href="/docs/linux/man/3-vpsetclientdata/">vpSetClientData</a>(3)).</dl>
<p> The callback can be used to implement custom shading routines that cannot be implemented with a lookup table. See <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3) for more information.</dl>
<dt>VP_RGB_SHADE_FUNC</p>
<dd>The <i>func</i> argument is a shading callback function that produces a floating point RGB pixel intensity. The function should be declared:</p>
<dl>
<dd>
<dl>
<dd>void <i>func</i>(void *<i>voxel_ptr,</i> float *<i>r_ptr</i>,<br />
 float *<i>r_ptr</i>, float *<i>r_ptr</i>,<br />
 void *<i>client_data</i>);</dl>
<dl>
<dt><i>voxel_ptr</i></p>
<dd>Pointer to the beginning of a voxel that must be shaded.</p>
<dt><i>r_ptr, g_ptr, b_ptr</i></p>
<dd>Location into which the function should store the RGB intensities of the result. Each intensity should be a single-precision floating point in the range 0.0 (no intensity) to 1.0 (full intensity).</p>
<dt><i>client_data</i></p>
<dd>Pointer to the application-defined client data (see <a href="/docs/linux/man/3-vpsetclientdata/">vpSetClientData</a>(3)).</dl>
<p> The callback can be used to implement custom shading routines that cannot be implemented with a lookup table. See <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3) for more information.</dl>
<dt>VP_READ_FUNC</p>
<dd>The <i>func</i> argument is a callback function that takes the same arguments and returns the same result as the <code><a href="/docs/linux/man/2-read/">read</a></code>(2) system call. This function is used to read data from files (see <a href="/docs/linux/man/3-vploadrawvolume/">vpLoadRawVolume</a>(3)). By default, the <code>read</code> system call is used. The callback can be used to implement a custom I/O interface, for example a compression/decompression system.</p>
<dt>VP_WRITE_FUNC</p>
<dd>The <i>func</i> argument is a callback function that takes the same arguments and returns the same result as the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) system call. This function is used to write data to files (see <a href="/docs/linux/man/3-vpstorerawvolume/">vpStoreRawVolume</a>(3)). By default, the <code>write</code> system call is used. The callback can be used to implement a custom I/O interface, for example a compression/decompression system.</p>
<dt>VP_MMAP_FUNC</p>
<dd>The <i>func</i> argument is a callback function that is called to memory map data from a file instead of copying the data into memory (see <a href="/docs/linux/man/3-vploadrawvolume/">vpLoadRawVolume</a>(3)). The function should be declared:</p>
<dl>
<dd>
<dl>
<dd>void *<i>func</i>(int <i>fd,</i> unsigned <i>offset,</i><br />
 void *<i>client_data</i>);</dl>
<dl>
<dt><i>fd</i></p>
<dd>File descriptor from <code><a href="/docs/linux/man/2-open/">open</a></code>(2) open for reading.</p>
<dt><i>offset</i></p>
<dd>Byte offset in the file to the beginning of the memory to be mapped.</p>
<dt><i>client_data</i></p>
<dd>Pointer to the application-defined client data (see <a href="/docs/linux/man/3-vpsetclientdata/">vpSetClientData</a>(3)).</dl>
<p> The function should map the entire file into memory and return a pointer to the memory location that corresponds to the file offset. By default, memory mapping is disabled.</dl>
<dt>VP_STATUS_FUNC</p>
<dd>The <i>func</i> argument is a callback function that is called periodically during long-running operations such as during preprocessing of a volume. The function should be declared:</p>
<dl>
<dd>
<dl>
<dd>void <i>func</i>(double <i>frac</i>, void *<i>client_data</i>);</dl>
<dl>
<dt><i>frac</i></p>
<dd>An estimate of the fraction of the current operation that is complete.</p>
<dt><i>client_data</i></p>
<dd>Pointer to the client data associated with the context.</dl>
<p> The callback can be used to print a status report or to process time-critical events such as user input. However, the callback should not make any calls to VolPack functions since the internal VolPack state may be inconsistent.</dl>
<dt>VP_LOG_ALLOC_FUNC</p>
<dd>The <i>func</i> argument is a callback function that is called whenever VolPack allocates memory. The function should be declared:</p>
<dl>
<dd>
<dl>
<dd>void <i>func</i>(void *<i>ptr,</i> int <i>size</i>, char *<i>use</i>,<br />
 int <i>line</i>, char *<i>file</i>, void *<i>client_data</i>);</dl>
<dl>
<dt><i>ptr</i></p>
<dd>Address of the allocated memory.</p>
<dt><i>size</i></p>
<dd>Size (in bytes) of the allocated memory.</p>
<dt><i>use</i></p>
<dd>Short description of the use of the allocated memory.</p>
<dt><i>line</i></p>
<dd>Source code line number for the call to the memory allocator.</p>
<dt><i>file</i></p>
<dd>Source code file name for the call to the memory allocator.</p>
<dt><i>client_data</i></p>
<dd>Pointer to the client data associated with the context.</dl>
<p> The callback can be used to track memory allocations (primarily for debugging memory leaks).</dl>
<dt>VP_LOG_FREE_FUNC</p>
<dd>The <i>func</i> argument is a callback function that is called whenever VolPack deallocates memory. The function should be declared:</p>
<dl>
<dd>
<dl>
<dd>void <i>func</i>(void *<i>ptr</i>, void *<i>client_data</i>)</dl>
<dl>
<dt><i>ptr</i></p>
<dd>Address of the deallocated memory.</p>
<dt><i>client_data</i></p>
<dd>Pointer to the client data associated with the context.</dl>
<p> The callback can be used to track memory deallocations (primarily for debugging memory leaks).</dl>
</dl>
<p> If the <i>func</i> argument is NULL then the corresponding callback function is reset to the default behavior or disabled if there is no default behavior.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return value is possible:</p>
<dl>
<dt>VPERROR_BAD_OPTION</p>
<dd>The <i>option</i> argument is invalid.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpsetclientdata/">vpSetClientData</a>(3), <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3), <a href="/docs/linux/man/3-vploadrawvolume/">vpLoadRawVolume</a>(3), <a href="/docs/linux/man/3-vpstorerawvolume/">vpStoreRawVolume</a>(3) </p>
