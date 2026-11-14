---
title: "libopencl(7)"
name: "libopencl"
section: "7"
letter: "l"
url: "/docs/linux/man/7-libopencl/"
description: "libOpenCL, libOpenCL.so – OCL-ICD implementation of OpenCL ICD loader"
---

<p>libOpenCL, libOpenCL.so &#8211; OCL-ICD implementation of OpenCL ICD loader</p>
<h2>Description</h2>
<p>libOpenCL.so is the library linked by OpenCL programs. It does not contains any OpenCL implementation itself, but merely act as a dispatcher to real OpenCL implementations provided as OpenCL Installable Client Driver (ICD). An ICD loader should be able to load ICDs provided by any vendors. </p>
<p> According to OpenCL specifications from Khronos (see [Khronos]), the ICD Loader looks for files into <i>/etc/OpenCL/vendors</i> directory and, for each file whose name ends with <i>.icd</i>, the ICD Loader loads with <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3) the shared library whose name is on the first line of the <i>.icd</i> file. </p>
<p> Each shared library name in &quot;.icd&quot; files can have its path, or it can be a plain filename. In the latter case, the ICD shared library will be looked for into the standard dynamic library loader paths.</p>
<h2>Environment</h2>
<p>Some environment variables can be used modify the default behavior of libOpenCL. </p>
<p> <code>OPENCL_VENDOR_PATH</code></p>
<dl>
<dd>This variable allows one to modify the default <i>/etc/OpenCL/vendors</i> path. It is compatible with some other ICD loaders (but not all of them, as the variable is not part of the standard). Note that <code>$OCL_ICD_VENDORS</code> (see below) is used in priority if defined and not empty.</dl>
<p> <code>OCL_ICD_VENDORS</code></p>
<dl>
<dd>This variable allows one to change the way ICD are searched on the system. Several cases are considered: </p>
<dl>
<dd>1. if <code>$OCL_ICD_VENDORS</code> is a directory path, then this path replaces the &quot;/etc/OpenCL/vendors&quot; path in the standard behavior: the loader will use the <i>.icd</i> files in this directory;</dl>
<dl>
<dd>2. else, if <code>$OCL_ICD_VENDORS</code> ends with <i>.icd</i>, libOpenCL.so will only load the ICD whose shared library name is wrote into the specified &quot;.icd&quot; file; </p>
<p> If there is no slashes into <code>$OCL_ICD_VENDORS</code>, libOpenCL.so will first try to use <i>/etc/OpenCL/vendors/</i><code>$OCL_ICD_VENDORS</code> (or <code>$OPENCL_VENDOR_PATH</code><i>/</i><code>$OCL_ICD_VENDORS</code> if <code>OPENCL_VENDOR_PATH</code> is defined). If this fail or if there are shashes, it uses <code>$OCL_ICD_VENDORS</code> (as a relative or absolute file name path).</dl>
<dl>
<dd>3. else libOpenCL.so will try to load <code>$OCL_ICD_VENDORS</code> as the ICD shared library itself (i.e. to load it directly with <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3)).</dl>
</dl>
<p> <code>OCL_ICD_LAYERS</code></p>
<dl>
<dd>This variable allows one to specify a colon separated list of layers to load, specifying their path. This support is experimental.</dl>
<p> <code>OCL_ICD_ASSUME_ICD_EXTENSION</code></p>
<dl>
<dd>If set to an non-empty value, contrary the Khronos specification, the loader will not check that the loaded ICDs declare the cl_khr_icd extension. It will also use the clGetPlatformInfo from the dispatch table if no such function is globally available. You may need to define this environment variable if you are using not (fully) compliant ICD, or if you are using the Intel ICD together with <code><a href="/docs/linux/man/1-optirun/">optirun</a></code>(1). In the latter case, a bug into the Intel ICD will make the application crash.</dl>
<p> If set to the <i>debug</i> value, some additional messages will be printed in debug mode (see <code>OCL_ICD_DEBUG</code> below). </p>
<p> <code>OCL_ICD_PLATFORM_SORT</code></p>
<dl>
<dd>Allows one to choose the way platforms are sorted when presented to programs through <code><a href="/docs/linux/man/3-clgetplatformids/">clGetPlatformIDs</a></code>(3). Current provided algorithms are: </p>
<dl>
<dd>&bull; <code>devices</code>: first, list platforms that support most GPU, then most CPU then most accelerators. If <code>OCL_ICD_PLATFORM_SORT</code> is not set or set to an unknown value, this algorithm is used.</dl>
<dl>
<dd>&bull; <code>none</code>: no sort is done and the order can change at each run.</dl>
</dl>
<p> <code>OCL_ICD_DEFAULT_PLATFORM</code></p>
<dl>
<dd>Number of the platform to choose as default platform. Note that using this environment variable without ensuring the use of a sort algorithm for platforms is not really useful.</dl>
<p> <code>OCL_ICD_DEBUG</code></p>
<dl>
<dd>If ocl-icd has been compiled with debug support, you can set this environment variable to a value where each bit display some kind of informations. Defined values are: </p>
<dl>
<dd>&bull; <code>1</code>: warnings (enabled by default if debug support is present and <code>OCL_ICD_DEBUG</code> is not set)</dl>
<dl>
<dd>&bull; <code>2</code>: informative messages</dl>
<dl>
<dd>&bull; <code>4</code>: entering/exiting for some OpenCL functions</dl>
<dl>
<dd>&bull; <code>8</code>: dump of the internal structure of loaded ICDs</dl>
<p> <code>OCL_ICD_DEBUG</code> is mainly useful for ocl-icd development itself and/or for ICD development.</dl>
<h2>See Also</h2>
<p>Khronos OpenCL registry website</p>
<h2>Author</h2>
<p><code>Vincent Danjean</code> &lt;Vincent.Danjean [at] ens-lyon.org&gt;</p>
<dl>
<dd>Author.</dl>
