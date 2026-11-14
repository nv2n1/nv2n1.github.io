---
title: "ecm-find-modules(7)"
name: "ecm-find-modules"
section: "7"
letter: "e"
url: "/docs/linux/man/7-ecm-find-modules/"
description: "ecm-find-modules – ECM Find Modules Reference"
---

<p>ecm-find-modules &#8211; ECM Find Modules Reference</p>
<h2>Introduction</h2>
<p>Find modules are used by the CMake <code>find_package</code> command to search for packages that do not provide their own CMake package config files. CMake provides an extensive set of find modules, and Extra CMake Modules (ECM) adds to that. </p>
<p> To use ECM&#8217;s find modules, you need to tell CMake to find the ECM package, and then add either <code>${ECM_MODULE_PATH}</code> or <code>${ECM_FIND_MODULE_DIR}</code> to the <code>CMAKE_MODULE_PATH</code> variable: </p>
<pre>find_package(ECM REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${ECM_FIND_MODULE_DIR})</pre>
<p>Using <code>${ECM_MODULE_PATH}</code> will also make the modules intended for direct use by CMake scripts available (see <code><a href="/docs/linux/man/7-ecm-modules/">ecm-modules</a>(7)</code> and <code><a href="/docs/linux/man/7-ecm-kde-modules/">ecm-kde-modules</a>(7)</code>). </p>
<p> You can also make local copies of find modules using the <code>ecm_use_find_modules</code> function from <code>ECMUseFindModules</code>, which is automatically included when ECM is found: </p>
<pre>find_package(ECM REQUIRED NO_MODULE)
ecm_use_find_modules(
 DIR &quot;${CMAKE_BINARY_DIR}/cmake&quot;
 MODULES FindEGL.cmake
)
set(CMAKE_MODULE_PATH &quot;${CMAKE_BINARY_DIR}/cmake&quot;)</pre>
<p>This allows selective use of ECM&#8217;s find modules, and the NO_OVERRIDE argument can be used to ensure that if CMake ships its own version of that find module, it will be used instead.</p>
<h2>All Find Modules</h2>
<h3>FindEGL</h3>
<p>Try to find EGL. </p>
<p> This will define the following variables:</p>
<dl>
<dt><code>EGL_FOUND</code></p>
<dd>True if (the requested version of) EGL is available</p>
<dt><code>EGL_VERSION</code></p>
<dd>The version of EGL; note that this is the API version defined in the headers, rather than the version of the implementation (eg: Mesa)</p>
<dt><code>EGL_LIBRARIES</code></p>
<dd>This can be passed to target_link_libraries() instead of the <code>EGL::EGL</code> target</p>
<dt><code>EGL_INCLUDE_DIRS</code></p>
<dd>This should be passed to target_include_directories() if the target is not used for linking</p>
<dt><code>EGL_DEFINITIONS</code></p>
<dd>This should be passed to target_compile_options() if the target is not used for linking </p>
<p> If <code>EGL_FOUND</code> is TRUE, it will also define the following imported target:</p>
<dt><code>EGL::EGL</code></p>
<dd>The EGL library </p>
<p> In general we recommend using the imported target, as it is easier to use. Bear in mind, however, that if the target is in the link interface of an exported library, it must be made available by the package config file. </p>
<p> Since pre-1.0.0.</dl>
<h3>FindKF5</h3>
<p>Find KDE Frameworks 5 with a single find_package() call. </p>
<p> This will use the package config files provided by the individual frameworks. For example, if you wish to find KArchive, which presents itself to CMake as KF5Archive (ie: you would do <code>find_package(KF5Archive)</code> to find it directly), you can do </p>
<pre>find_package(KF5 COMPONENTS Archive)</pre>
<p>If all the required components (those given in the COMPONENTS argument, but not those given in the OPTIONAL_COMPONENTS argument) are found, <code>KF5_FOUND</code> will be set to true. Otherwise, it will be set to false. </p>
<p> Since pre-1.0.0.</p>
<h3>FindLibGit2</h3>
<p>Try to find libgit2 on a Unix system. </p>
<p> This will define the following variables:</p>
<dl>
<dt><code>LIBGIT2_FOUND</code></p>
<dd>True if (the requested version of) libgit2 is available</p>
<dt><code>LIBGIT2_VERSION</code></p>
<dd>The version of libgit2</p>
<dt><code>LIBGIT2_LIBRARIES</code></p>
<dd>This can be passed to target_link_libraries() instead of the <code>LibGit2::LibGit2</code> target</p>
<dt><code>LIBGIT2_INCLUDE_DIRS</code></p>
<dd>This should be passed to target_include_directories() if the target is not used for linking</p>
<dt><code>LIBGIT2_DEFINITIONS</code></p>
<dd>This should be passed to target_compile_options() if the target is not used for linking </p>
<p> If <code>LIBGIT2_FOUND</code> is TRUE, it will also define the following imported target:</p>
<dt><code>LibGit2::LibGit2</code></p>
<dd>The libgit2 library </p>
<p> In general we recommend using the imported target, as it is easier to use. Bear in mind, however, that if the target is in the link interface of an exported library, it must be made available by the package config file. </p>
<p> Since 1.3.0.</dl>
<h3>FindOpenEXR</h3>
<p>Try to find the OpenEXR libraries. </p>
<p> This will define the following variables:</p>
<dl>
<dt><code>OpenEXR_FOUND</code></p>
<dd>True if OpenEXR is available</p>
<dt><code>OpenEXR_LIBRARIES</code></p>
<dd>Link to these to use OpenEXR</p>
<dt><code>OpenEXR_INCLUDE_DIRS</code></p>
<dd>Include directory for OpenEXR</p>
<dt><code>OpenEXR_DEFINITIONS</code></p>
<dd>Compiler flags required to link against OpenEXR </p>
<p> and the following imported targets:</p>
<dt><code>OpenEXR::IlmImf</code></p>
<dd>The OpenEXR core library </p>
<p> In general we recommend using the imported target, as it is easier to use. Bear in mind, however, that if the target is in the link interface of an exported library, it must be made available by the package config file. </p>
<p> Since pre-1.0.0.</dl>
<h3>FindPng2Ico</h3>
<p>Try to find png2ico. </p>
<p> If the png2ico executable is not in your PATH, you can provide an alternative name or full path location with the <code>Png2Ico_EXECUTABLE</code> variable. </p>
<p> This will define the following variables:</p>
<dl>
<dt><code>Png2Ico_FOUND</code></p>
<dd>True if png2ico is available.</p>
<dt><code>Png2Ico_EXECUTABLE</code></p>
<dd>The png2ico executable. </p>
<p> If <code>Png2Ico_FOUND</code> is TRUE, it will also define the following imported target:</p>
<dt><code>Png2Ico::Png2Ico</code></p>
<dd>The png2ico executable. </p>
<p> and the following variables:</p>
<dt><code>Png2Ico_HAS_COLORS_ARGUMENT</code></p>
<dd>Whether png2ico accepts a <code>&#8211;colors</code> argument. <i>Matthias Benkmann&#8217;s tool</i> does, while the version of png2ico from the <i>&quot;KDE On Windows&quot; (kdewin)</i> project does not.</p>
<dt><code>Png2Ico_HAS_RCFILE_ARGUMENT</code></p>
<dd>Whether png2ico accepts an <code>&#8211;rcfile</code> argument. The version of png2ico from the <i>&quot;KDE On Windows&quot; (kdewin)</i> project does, while <i>Matthias Benkmann&#8217;s tool</i> does not. </p>
<p> Since 1.7.0.</dl>
<h3>FindPoppler</h3>
<p>Try to find Poppler. </p>
<p> This is a component-based find module, which makes use of the COMPONENTS and OPTIONAL_COMPONENTS arguments to find_module. The following components are available: </p>
<pre>Core Cpp Qt5 Qt4 Glib</pre>
<p>If no components are specified, this module will act as though all components were passed to OPTIONAL_COMPONENTS. </p>
<p> This module will define the following variables, independently of the components searched for or found:</p>
<dl>
<dt><code>Poppler_FOUND</code></p>
<dd>TRUE if (the requested version of) Poppler is available</p>
<dt><code>Poppler_VERSION</code></p>
<dd>Found Poppler version</p>
<dt><code>Poppler_TARGETS</code></p>
<dd>A list of all targets imported by this module (note that there may be more than the components that were requested)</p>
<dt><code>Poppler_LIBRARIES</code></p>
<dd>This can be passed to target_link_libraries() instead of the imported targets</p>
<dt><code>Poppler_INCLUDE_DIRS</code></p>
<dd>This should be passed to target_include_directories() if the targets are not used for linking</p>
<dt><code>Poppler_DEFINITIONS</code></p>
<dd>This should be passed to target_compile_options() if the targets are not used for linking </p>
<p> For each searched-for components, <code>Poppler_&lt;component&gt;_FOUND</code> will be set to TRUE if the corresponding Poppler library was found, and FALSE otherwise. If <code>Poppler_&lt;component&gt;_FOUND</code> is TRUE, the imported target <code>Poppler::&lt;component&gt;</code> will be defined. This module will also attempt to determine <code>Poppler_*_VERSION</code> variables for each imported target, although <code>Poppler_VERSION</code> should normally be sufficient. </p>
<p> In general we recommend using the imported targets, as they are easier to use and provide more control. Bear in mind, however, that if any target is in the link interface of an exported library, it must be made available by the package config file. </p>
<p> Since 5.19</dl>
<h3>FindQtWaylandScanner</h3>
<p>Try to find qtwaylandscanner. </p>
<p> If the qtwaylandscanner executable is not in your PATH, you can provide an alternative name or full path location with the <code>QtWaylandScanner_EXECUTABLE</code> variable. </p>
<p> This will define the following variables:</p>
<dl>
<dt><code>QtWaylandScanner_FOUND</code></p>
<dd>True if qtwaylandscanner is available</p>
<dt><code>QtWaylandScanner_EXECUTABLE</code></p>
<dd>The qtwaylandscanner executable. </p>
<p> If <code>QtWaylandScanner_FOUND</code> is TRUE, it will also define the following imported target:</p>
<dt><code>Wayland::QtScanner</code></p>
<dd>The qtwaylandscanner executable. </p>
<p> This module provides the following functions to generate C++ protocol implementations:</p>
<dt>&bull;</p>
<dd><code>ecm_add_qtwayland_client_protocol</code></p>
<dt>&bull;</p>
<dd><code>ecm_add_qtwayland_server_protocol</code> </p>
<pre>ecm_add_qtwayland_client_protocol(&lt;source_files_var&gt;
 PROTOCOL &lt;xmlfile&gt;
 BASENAME &lt;basename&gt;
 [PREFIX &lt;prefix&gt;])</pre>
<p>Generate C++ wrapper to Wayland client protocol files from <code>&lt;xmlfile&gt;</code> XML definition for the <code>&lt;basename&gt;</code> interface and append those files to <code>&lt;source_files_var&gt;</code>. Pass the <code>&lt;prefix&gt;</code> argument if the interface names don&#8217;t start with <code>qt_</code> or <code>wl_</code>. </p>
<p> WaylandScanner is required and will be searched for. </p>
<pre>ecm_add_qtwayland_server_protocol(&lt;source_files_var&gt;
 PROTOCOL &lt;xmlfile&gt;
 BASENAME &lt;basename&gt;
 [PREFIX &lt;prefix&gt;])</pre>
<p>Generate C++ wrapper to Wayland server protocol files from <code>&lt;xmlfile&gt;</code> XML definition for the <code>&lt;basename&gt;</code> interface and append those files to <code>&lt;source_files_var&gt;</code>. Pass the <code>&lt;prefix&gt;</code> argument if the interface names don&#8217;t start with <code>qt_</code> or <code>wl_</code>. </p>
<p> WaylandScanner is required and will be searched for. </p>
<p> Since 1.4.0.</dl>
<h3>FindSharedMimeInfo</h3>
<p>Try to find the shared-mime-info package. </p>
<p> This will define the following variables:</p>
<dl>
<dt><code>SharedMimeInfo_FOUND</code></p>
<dd>True if system has the shared-mime-info package</p>
<dt><code>UPDATE_MIME_DATABASE_EXECUTABLE</code></p>
<dd>The update-mime-database executable </p>
<p> and the following imported targets:</p>
<dt><code>SharedMimeInfo::UpdateMimeDatabase</code></p>
<dd>The update-mime-database executable </p>
<p> The follow macro is available: </p>
<pre>update_xdg_mimetypes(&lt;path&gt;)</pre>
<p>Updates the XDG mime database at install time (unless the <code>$DESTDIR</code> environment variable is set, in which case it is up to package managers to perform this task). </p>
<p> Since pre-1.0.0.</dl>
<h3>FindWayland</h3>
<p>Try to find Wayland. </p>
<p> This is a component-based find module, which makes use of the COMPONENTS and OPTIONAL_COMPONENTS arguments to find_module. The following components are available: </p>
<pre>Client Server Cursor Egl</pre>
<p>If no components are specified, this module will act as though all components were passed to OPTIONAL_COMPONENTS. </p>
<p> This module will define the following variables, independently of the components searched for or found:</p>
<dl>
<dt><code>Wayland_FOUND</code></p>
<dd>TRUE if (the requested version of) Wayland is available</p>
<dt><code>Wayland_VERSION</code></p>
<dd>Found Wayland version</p>
<dt><code>Wayland_TARGETS</code></p>
<dd>A list of all targets imported by this module (note that there may be more than the components that were requested)</p>
<dt><code>Wayland_LIBRARIES</code></p>
<dd>This can be passed to target_link_libraries() instead of the imported targets</p>
<dt><code>Wayland_INCLUDE_DIRS</code></p>
<dd>This should be passed to target_include_directories() if the targets are not used for linking</p>
<dt><code>Wayland_DEFINITIONS</code></p>
<dd>This should be passed to target_compile_options() if the targets are not used for linking </p>
<p> For each searched-for components, <code>Wayland_&lt;component&gt;_FOUND</code> will be set to TRUE if the corresponding Wayland library was found, and FALSE otherwise. If <code>Wayland_&lt;component&gt;_FOUND</code> is TRUE, the imported target <code>Wayland::&lt;component&gt;</code> will be defined. This module will also attempt to determine <code>Wayland_*_VERSION</code> variables for each imported target, although <code>Wayland_VERSION</code> should normally be sufficient. </p>
<p> In general we recommend using the imported targets, as they are easier to use and provide more control. Bear in mind, however, that if any target is in the link interface of an exported library, it must be made available by the package config file. </p>
<p> Since pre-1.0.0.</dl>
<h3>FindWaylandScanner</h3>
<p>Try to find wayland-scanner. </p>
<p> If the wayland-scanner executable is not in your PATH, you can provide an alternative name or full path location with the <code>WaylandScanner_EXECUTABLE</code> variable. </p>
<p> This will define the following variables:</p>
<dl>
<dt><code>WaylandScanner_FOUND</code></p>
<dd>True if wayland-scanner is available.</p>
<dt><code>WaylandScanner_EXECUTABLE</code></p>
<dd>The wayland-scanner executable. </p>
<p> If <code>WaylandScanner_FOUND</code> is TRUE, it will also define the following imported target:</p>
<dt><code>Wayland::Scanner</code></p>
<dd>The wayland-scanner executable. </p>
<p> This module provides the following functions to generate C protocol implementations:</p>
<dt>&bull;</p>
<dd><code>ecm_add_wayland_client_protocol</code></p>
<dt>&bull;</p>
<dd><code>ecm_add_wayland_server_protocol</code> </p>
<pre>ecm_add_wayland_client_protocol(&lt;source_files_var&gt;
 PROTOCOL &lt;xmlfile&gt;
 BASENAME &lt;basename&gt;)</pre>
<p>Generate Wayland client protocol files from <code>&lt;xmlfile&gt;</code> XML definition for the <code>&lt;basename&gt;</code> interface and append those files to <code>&lt;source_files_var&gt;</code>. </p>
<pre>ecm_add_wayland_server_protocol(&lt;source_files_var&gt;
 PROTOCOL &lt;xmlfile&gt;
 BASENAME &lt;basename&gt;)</pre>
<p>Generate Wayland server protocol files from <code>&lt;xmlfile&gt;</code> XML definition for the <code>&lt;basename&gt;</code> interface and append those files to <code>&lt;source_files_var&gt;</code>. </p>
<p> Since 1.4.0.</dl>
<h3>FindX11_XCB</h3>
<p>Try to find the X11 XCB compatibility library. </p>
<p> This will define the following variables:</p>
<dl>
<dt><code>X11_XCB_FOUND</code></p>
<dd>True if (the requested version of) libX11-xcb is available</p>
<dt><code>X11_XCB_VERSION</code></p>
<dd>The version of libX11-xcb (this is not guaranteed to be set even when X11_XCB_FOUND is true)</p>
<dt><code>X11_XCB_LIBRARIES</code></p>
<dd>This can be passed to target_link_libraries() instead of the <code>EGL::EGL</code> target</p>
<dt><code>X11_XCB_INCLUDE_DIR</code></p>
<dd>This should be passed to target_include_directories() if the target is not used for linking</p>
<dt><code>X11_XCB_DEFINITIONS</code></p>
<dd>This should be passed to target_compile_options() if the target is not used for linking </p>
<p> If <code>X11_XCB_FOUND</code> is TRUE, it will also define the following imported target:</p>
<dt><code>X11::XCB</code></p>
<dd>The X11 XCB compatibility library </p>
<p> In general we recommend using the imported target, as it is easier to use. Bear in mind, however, that if the target is in the link interface of an exported library, it must be made available by the package config file. </p>
<p> Since pre-1.0.0.</dl>
<h3>FindXCB</h3>
<p>Try to find XCB. </p>
<p> This is a component-based find module, which makes use of the COMPONENTS and OPTIONAL_COMPONENTS arguments to find_module. The following components are available: </p>
<pre>XCB
ATOM AUX COMPOSITE CURSOR DAMAGE
DPMS DRI2 DRI3 EVENT EWMH
GLX ICCCM IMAGE KEYSYMS PRESENT
RANDR RECORD RENDER RENDERUTIL RES
SCREENSAVER SHAPE SHM SYNC UTIL
XEVIE XF86DRI XFIXES XINERAMA XINPUT
XKB XPRINT XTEST XV XVMC</pre>
<p>If no components are specified, this module will act as though all components except XINPUT (which is considered unstable) were passed to OPTIONAL_COMPONENTS. </p>
<p> This module will define the following variables, independently of the components searched for or found:</p>
<dl>
<dt><code>XCB_FOUND</code></p>
<dd>True if (the requestion version of) xcb is available</p>
<dt><code>XCB_VERSION</code></p>
<dd>Found xcb version</p>
<dt><code>XCB_TARGETS</code></p>
<dd>A list of all targets imported by this module (note that there may be more than the components that were requested)</p>
<dt><code>XCB_LIBRARIES</code></p>
<dd>This can be passed to target_link_libraries() instead of the imported targets</p>
<dt><code>XCB_INCLUDE_DIRS</code></p>
<dd>This should be passed to target_include_directories() if the targets are not used for linking</p>
<dt><code>XCB_DEFINITIONS</code></p>
<dd>This should be passed to target_compile_options() if the targets are not used for linking </p>
<p> For each searched-for components, <code>XCB_&lt;component&gt;_FOUND</code> will be set to true if the corresponding xcb library was found, and false otherwise. If <code>XCB_&lt;component&gt;_FOUND</code> is true, the imported target <code>XCB::&lt;component&gt;</code> will be defined. This module will also attempt to determine <code>XCB_*_VERSION</code> variables for each imported target, although <code>XCB_VERSION</code> should normally be sufficient. </p>
<p> In general we recommend using the imported targets, as they are easier to use and provide more control. Bear in mind, however, that if any target is in the link interface of an exported library, it must be made available by the package config file. </p>
<p> Since pre-1.0.0.</dl>
<h2>Copyright</h2>
<p>KDE Developers</p>
