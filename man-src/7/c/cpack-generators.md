---
title: "cpack-generators(7)"
name: "cpack-generators"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cpack-generators/"
description: "cpack-generators – CPack Generator Reference"
---

<p>cpack-generators &#8211; CPack Generator Reference</p>
<h2>Generators</h2>
<h3>CPack Archive Generator</h3>
<p>CPack generator for packaging files into an archive, which can have any of the following formats:</p>
<dl>
<dt>&bull;</p>
<dd>7Z &#8211; 7zip &#8211; (.7z)</p>
<dt>&bull;</p>
<dd>TBZ2 (.tar.bz2)</p>
<dt>&bull;</p>
<dd>TGZ (.tar.gz)</p>
<dt>&bull;</p>
<dd>TXZ (.tar.xz)</p>
<dt>&bull;</p>
<dd>TZ (.tar.Z)</p>
<dt>&bull;</p>
<dd>TZST (.tar.zst)</p>
<dt>&bull;</p>
<dd>ZIP (.zip) </p>
<p> New in version 3.1: <code>7Z</code> and <code>TXZ</code> formats support. </p>
<p> New in version 3.16: <code>TZST</code> format support. </p>
<p> When this generator is called from <code>CPackSourceConfig.cmake</code> (or through the <code>package_source</code> target), then the generated archive will contain all files in the project directory, except those specified in <code>CPACK_SOURCE_IGNORE_FILES</code>. The following is one example of packaging all source files of a project: </p>
<pre>set(CPACK_SOURCE_GENERATOR &quot;TGZ&quot;)
set(CPACK_SOURCE_IGNORE_FILES
 \.git/
 build/
 &quot;.*~$&quot;
)
set(CPACK_VERBATIM_VARIABLES YES)
include(CPack)</pre>
<p>When this generator is called from <code>CPackConfig.cmake</code> (or through the <code>package</code> target), then the generated archive will contain all files that have been installed via CMake&#8217;s <code>install()</code> command (and the deprecated commands <code>install_files()</code>, <code>install_programs()</code>, and <code>install_targets()</code>).</dl>
<h3>Variables specific to CPack Archive generator</h3>
<dl>
<dt><code>CPACK_ARCHIVE_FILE_NAME</code></p>
<dd>
<dt><code>CPACK_ARCHIVE_&lt;component&gt;_FILE_NAME</code></p>
<dd>Package file name without extension. The extension is determined from the archive format (see list above) and automatically appended to the file name. The default is <code>&lt;CPACK_PACKAGE_FILE_NAME&gt;[-&lt;component&gt;]</code>, with spaces replaced by &#8216;-&#8216;. </p>
<p> New in version 3.9: Per-component <code>CPACK_ARCHIVE_&lt;component&gt;_FILE_NAME</code> variables. </p>
<dt><code>CPACK_ARCHIVE_COMPONENT_INSTALL</code></p>
<dd>Enable component packaging. If enabled (ON), then the archive generator creates multiple packages. The default is OFF, which means that a single package containing files of all components is generated.</dl>
<h3>Variables used by CPack Archive generator</h3>
<p>These variables are used by the Archive generator, but are also available to CPack generators which are essentially archives at their core. These include:</p>
<dl>
<dt>&bull;</p>
<dd><code>CPack Cygwin Generator</code></p>
<dt>&bull;</p>
<dd><code>CPack FreeBSD Generator</code></p>
<dt><code>CPACK_ARCHIVE_THREADS</code></p>
<dd>New in version 3.18. </p>
<p> The number of threads to use when performing the compression. If set to <code>0</code>, the number of available cores on the machine will be used instead. The default is <code>1</code> which limits compression to a single thread. Note that not all compression modes support threading in all environments. Currently, only the XZ compression may support it. </p>
<p> See also the <code>CPACK_THREADS</code> variable. </p>
<p> New in version 3.21: Official CMake binaries available on <code>cmake.org</code> now ship with a <code>liblzma</code> that supports parallel compression. Older versions did not. </p>
</dl>
<h3>CPack Bundle Generator</h3>
<p>CPack Bundle generator (macOS) specific options</p>
<h3>Variables specific to CPack Bundle generator</h3>
<p>Installers built on macOS using the Bundle generator use the aforementioned DragNDrop (<code>CPACK_DMG_xxx</code>) variables, plus the following Bundle-specific parameters (<code>CPACK_BUNDLE_xxx</code>).</p>
<dl>
<dt><code>CPACK_BUNDLE_NAME</code></p>
<dd>The name of the generated bundle. This appears in the macOS Finder as the bundle name. Required.</p>
<dt><code>CPACK_BUNDLE_PLIST</code></p>
<dd>Path to an macOS Property List (<code>.plist</code>) file that will be used for the generated bundle. This assumes that the caller has generated or specified their own <code>Info.plist</code> file. Required.</p>
<dt><code>CPACK_BUNDLE_ICON</code></p>
<dd>Path to an macOS icon file that will be used as the icon for the generated bundle. This is the icon that appears in the macOS Finder for the bundle, and in the macOS dock when the bundle is opened. Required.</p>
<dt><code>CPACK_BUNDLE_STARTUP_COMMAND</code></p>
<dd>Path to a startup script. This is a path to an executable or script that will be run whenever an end-user double-clicks the generated bundle in the macOS Finder. Optional.</p>
<dt><code>CPACK_BUNDLE_APPLE_CERT_APP</code></p>
<dd>New in version 3.2. </p>
<p> The name of your Apple supplied code signing certificate for the application. The name usually takes the form <code>Developer ID Application: [Name]</code> or <code>3rd Party Mac Developer Application: [Name]</code>. If this variable is not set the application will not be signed.</p>
<dt><code>CPACK_BUNDLE_APPLE_ENTITLEMENTS</code></p>
<dd>New in version 3.2. </p>
<p> The name of the Property List (<code>.plist</code>) file that contains your Apple entitlements for sandboxing your application. This file is required for submission to the macOS App Store.</p>
<dt><code>CPACK_BUNDLE_APPLE_CODESIGN_FILES</code></p>
<dd>New in version 3.2. </p>
<p> A list of additional files that you wish to be signed. You do not need to list the main application folder, or the main executable. You should list any frameworks and plugins that are included in your app bundle.</p>
<dt><code>CPACK_BUNDLE_APPLE_CODESIGN_PARAMETER</code></p>
<dd>New in version 3.3. </p>
<p> Additional parameter that will passed to <code>codesign</code>. Default value: <code>&#8211;deep -f</code></p>
<dt><code>CPACK_COMMAND_CODESIGN</code></p>
<dd>New in version 3.2. </p>
<p> Path to the <code><a href="/docs/linux/man/1-codesign/">codesign</a>(1)</code> command used to sign applications with an Apple cert. This variable can be used to override the automatically detected command (or specify its location if the auto-detection fails to find it).</dl>
<h3>CPack Cygwin Generator</h3>
<p>Cygwin CPack generator (Cygwin).</p>
<h3>Variables affecting the CPack Cygwin generator</h3>
<dl>
<dt>&bull;</p>
<dd>New in version 3.18: <code>CPACK_ARCHIVE_THREADS</code> </p>
</dl>
<h3>Variables specific to CPack Cygwin generator</h3>
<p>The following variable is specific to installers build on and/or for Cygwin:</p>
<dl>
<dt><code>CPACK_CYGWIN_PATCH_NUMBER</code></p>
<dd>The Cygwin patch number. FIXME: This documentation is incomplete.</p>
<dt><code>CPACK_CYGWIN_PATCH_FILE</code></p>
<dd>The Cygwin patch file. FIXME: This documentation is incomplete.</p>
<dt><code>CPACK_CYGWIN_BUILD_SCRIPT</code></p>
<dd>The Cygwin build script. FIXME: This documentation is incomplete.</dl>
<h3>CPack DEB Generator</h3>
<p>The built in (binary) CPack DEB generator (Unix only)</p>
<h3>Variables specific to CPack Debian (DEB) generator</h3>
<p>The CPack DEB generator may be used to create DEB package using <code>CPack</code>. The CPack DEB generator is a <code>CPack</code> generator thus it uses the <code>CPACK_XXX</code> variables used by <code>CPack</code>. </p>
<p> The CPack DEB generator should work on any Linux host but it will produce better deb package when Debian specific tools <code>dpkg-xxx</code> are usable on the build system. </p>
<p> The CPack DEB generator has specific features which are controlled by the specifics <code>CPACK_DEBIAN_XXX</code> variables. </p>
<p> <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_XXXX</code> variables may be used in order to have <code>component</code> specific values. Note however that <code>&lt;COMPONENT&gt;</code> refers to the <code>grouping name</code> written in upper case. It may be either a component name or a component GROUP name. </p>
<p> Here are some CPack DEB generator wiki resources that are here for historic reasons and are no longer maintained but may still prove useful:</p>
<dl>
<dt>&bull;</p>
<dd><i><a rel="nofollow" href="https://gitlab.kitware.com/cmake/community/-/wikis/doc/cpack/Configuration">https://gitlab.kitware.com/cmake/community/-/wikis/doc/cpack/Configuration</a></i></p>
<dt>&bull;</p>
<dd><i><a rel="nofollow" href="https://gitlab.kitware.com/cmake/community/-/wikis/doc/cpack/PackageGenerators#deb-unix-only">https://gitlab.kitware.com/cmake/community/-/wikis/doc/cpack/PackageGenerators#deb-unix-only</a></i> </p>
<p> List of CPack DEB generator specific variables:</p>
<dt><code>CPACK_DEB_COMPONENT_INSTALL</code></p>
<dd>Enable component packaging for CPackDEB</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : OFF </p>
<p> If enabled (ON) multiple packages are generated. By default a single package containing files of all components is generated.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_NAME</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_NAME</code></p>
<dd>Set Package control field (variable is automatically transformed to lower case).</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd><code>CPACK_PACKAGE_NAME</code> for non-component based installations</p>
<dt>&bull;</p>
<dd><i>CPACK_DEBIAN_PACKAGE_NAME</i> suffixed with -&lt;COMPONENT&gt; for component-based installations. </p>
<p> New in version 3.5: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_NAME</code> variables. </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Source">https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Source</a></i></p>
<dt><code>CPACK_DEBIAN_FILE_NAME</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_FILE_NAME</code></p>
<dd>New in version 3.6. </p>
<p> Package file name.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>&lt;CPACK_PACKAGE_FILE_NAME&gt;[-&lt;component&gt;].deb</code> </p>
<p> This may be set to <code>DEB-DEFAULT</code> to allow the CPack DEB generator to generate package file name by itself in deb format: </p>
<pre>&lt;PackageName&gt;_&lt;VersionNumber&gt;-&lt;DebianRevisionNumber&gt;_&lt;DebianArchitecture&gt;.deb</pre>
<p>Alternatively provided package file name must end with either <code>.deb</code> or <code>.ipk</code> suffix. </p>
<p> New in version 3.10: <code>.ipk</code> suffix used by OPKG packaging system. </p>
<p> <code>NOTE:</code> Preferred setting of this variable is <code>DEB-DEFAULT</code> but for backward compatibility with the CPack DEB generator in CMake prior to version 3.6 this feature is disabled by default. </p>
<p> <code>NOTE:</code> By using non default filenames duplicate names may occur. Duplicate files get overwritten and it is up to the packager to set the variables in a manner that will prevent such errors.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_EPOCH</code></p>
<dd>New in version 3.10. </p>
<p> The Debian package epoch</p>
<dt>&bull;</p>
<dd>Mandatory : No</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> Optional number that should be incremented when changing versioning schemas or fixing mistakes in the version numbers of older packages.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_VERSION</code></p>
<dd>The Debian package version</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_PACKAGE_VERSION</code> </p>
<p> This variable may contain only alphanumerics (A-Za-z0-9) and the characters . + &#8211; ~ (full stop, plus, hyphen, tilde) and should start with a digit. If <i>CPACK_DEBIAN_PACKAGE_RELEASE</i> is not set then hyphens are not allowed. </p>
<p> <code>NOTE:</code> For backward compatibility with CMake 3.9 and lower a failed test of this variable&#8217;s content is not a hard error when both <i>CPACK_DEBIAN_PACKAGE_RELEASE</i> and <i>CPACK_DEBIAN_PACKAGE_EPOCH</i> variables are not set. An author warning is reported instead.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_RELEASE</code></p>
<dd>New in version 3.6. </p>
<p> The Debian package release &#8211; Debian revision number.</p>
<dt>&bull;</p>
<dd>Mandatory : No</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> This is the numbering of the DEB package itself, i.e. the version of the packaging and not the version of the content (see <i>CPACK_DEBIAN_PACKAGE_VERSION</i>). One may change the default value if the previous packaging was buggy and/or you want to put here a fancy Linux distro specific numbering.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_ARCHITECTURE</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_ARCHITECTURE</code></p>
<dd>The Debian package architecture</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : Output of <code>dpkg &#8211;print-architecture</code> (or <code>i386</code> if <code>dpkg</code> is not found) </p>
<p> New in version 3.6: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_ARCHITECTURE</code> variables. </p>
<dt><code>CPACK_DEBIAN_PACKAGE_DEPENDS</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_DEPENDS</code></p>
<dd>Sets the Debian dependencies of this package.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><i>CPACK_DEBIAN_PACKAGE_DEPENDS</i> for component-based installations. </p>
<p> New in version 3.3: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_DEPENDS</code> variables. </p>
<p> <code>NOTE:</code> If <i>CPACK_DEBIAN_PACKAGE_SHLIBDEPS</i> or more specifically <i>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_SHLIBDEPS</i> is set for this component, the discovered dependencies will be appended to <i>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_DEPENDS</i> instead of <i>CPACK_DEBIAN_PACKAGE_DEPENDS</i>. If <i>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_DEPENDS</i> is an empty string, only the automatically discovered dependencies will be set for this component. </p>
<p> Example: </p>
<pre>set(CPACK_DEBIAN_PACKAGE_DEPENDS &quot;libc6 (&gt;= 2.3.1-6), libc6 (&lt; 2.4)&quot;)</pre>
<dt><code>CPACK_DEBIAN_ENABLE_COMPONENT_DEPENDS</code></p>
<dd>New in version 3.6. </p>
<p> Sets inter-component dependencies if listed with <code>CPACK_COMPONENT_&lt;compName&gt;_DEPENDS</code> variables.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_DEBIAN_PACKAGE_MAINTAINER</code></p>
<dd>The Debian package maintainer</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_PACKAGE_CONTACT</code></p>
<dt><code>CPACK_DEBIAN_PACKAGE_DESCRIPTION</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_DESCRIPTION</code></p>
<dd>The Debian package description</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd><i>CPACK_DEBIAN_&lt;COMPONENT&gt;_DESCRIPTION</i> (component based installers only) if set, or <i>CPACK_DEBIAN_PACKAGE_DESCRIPTION</i> if set, or</p>
<dt>&bull;</p>
<dd><code>CPACK_COMPONENT_&lt;compName&gt;_DESCRIPTION</code> (component based installers only) if set, or <code>CPACK_PACKAGE_DESCRIPTION</code> if set, or</p>
<dt>&bull;</p>
<dd>content of the file specified in <code>CPACK_PACKAGE_DESCRIPTION_FILE</code> if set </p>
<p> If after that description is not set, <code>CPACK_PACKAGE_DESCRIPTION_SUMMARY</code> going to be used if set. Otherwise, <code>CPACK_PACKAGE_DESCRIPTION_SUMMARY</code> will be added as the first line of description as defined in <i>Debian Policy Manual</i>. </p>
<p> New in version 3.3: Per-component <code>CPACK_COMPONENT_&lt;compName&gt;_DESCRIPTION</code> variables. </p>
<p> New in version 3.16: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_DESCRIPTION</code> variables. </p>
<p> New in version 3.16: The <code>CPACK_PACKAGE_DESCRIPTION_FILE</code> variable. </p>
<dt><code>CPACK_DEBIAN_PACKAGE_SECTION</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_SECTION</code></p>
<dd>Set Section control field e.g. admin, devel, doc, &#8230;</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : &quot;devel&quot; </p>
<p> New in version 3.5: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_SECTION</code> variables. </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-archive.html#s-subsections">https://www.debian.org/doc/debian-policy/ch-archive.html#s-subsections</a></i></p>
<dt><code>CPACK_DEBIAN_ARCHIVE_TYPE</code></p>
<dd>New in version 3.7. </p>
<p> Deprecated since version 3.14. </p>
<p> The archive format used for creating the Debian package.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : &quot;gnutar&quot; </p>
<p> Possible value is:</p>
<dt>&bull;</p>
<dd>gnutar </p>
<p> <code>NOTE:</code> This variable previously defaulted to the <code>paxr</code> value, but <code>dpkg</code> has never supported that tar format. For backwards compatibility the <code>paxr</code> value will be mapped to <code>gnutar</code> and a deprecation message will be emitted.</p>
<dt><code>CPACK_DEBIAN_COMPRESSION_TYPE</code></p>
<dd>New in version 3.1. </p>
<p> The compression used for creating the Debian package.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : &quot;gzip&quot; </p>
<p> Possible values are:</p>
<dt><code>lzma</code></p>
<dd>Lempel–Ziv–Markov chain algorithm</p>
<dt><code>xz</code></p>
<dd>XZ Utils compression</p>
<dt><code>bzip2</code></p>
<dd>bzip2 Burrows–Wheeler algorithm</p>
<dt><code>gzip</code></p>
<dd>GNU Gzip compression</p>
<dt><code>zstd</code></p>
<dd>New in version 3.22. </p>
<p> Zstandard compression</p>
<dt><code>CPACK_DEBIAN_PACKAGE_PRIORITY</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_PRIORITY</code></p>
<dd>Set Priority control field e.g. required, important, standard, optional, extra</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : &quot;optional&quot; </p>
<p> New in version 3.5: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_PRIORITY</code> variables. </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-archive.html#s-priorities">https://www.debian.org/doc/debian-policy/ch-archive.html#s-priorities</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_HOMEPAGE</code></p>
<dd>The URL of the web site for this package, preferably (when applicable) the site from which the original source can be obtained and any additional upstream documentation or information may be found.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : <code>CMAKE_PROJECT_HOMEPAGE_URL</code> </p>
<p> New in version 3.12: The <code>CMAKE_PROJECT_HOMEPAGE_URL</code> variable. </p>
<p> <code>NOTE:</code> The content of this field is a simple URL without any surrounding characters such as &lt;&gt;.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_SHLIBDEPS</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_SHLIBDEPS</code></p>
<dd>May be set to ON in order to use <code>dpkg-shlibdeps</code> to generate better package dependency list.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd><i>CPACK_DEBIAN_PACKAGE_SHLIBDEPS</i> if set or</p>
<dt>&bull;</p>
<dd>OFF </p>
<p> <code>NOTE:</code> You may need set <code>CMAKE_INSTALL_RPATH</code> to an appropriate value if you use this feature, because if you don&#8217;t <code>dpkg-shlibdeps</code> may fail to find your own shared libs. See <i><a rel="nofollow" href="https://gitlab.kitware.com/cmake/community/-/wikis/doc/cmake/RPATH-handling">https://gitlab.kitware.com/cmake/community/-/wikis/doc/cmake/RPATH-handling</a></i> </p>
<p> <code>NOTE:</code> You can also set <i>CPACK_DEBIAN_PACKAGE_SHLIBDEPS_PRIVATE_DIRS</i> to an appropriate value if you use this feature, in order to please <code>dpkg-shlibdeps</code>. However, you should only do this for private shared libraries that could not get resolved otherwise. </p>
<p> New in version 3.3: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_SHLIBDEPS</code> variables. </p>
<p> New in version 3.6: Correct handling of <code>$ORIGIN</code> in <code>CMAKE_INSTALL_RPATH</code>. </p>
<dt><code>CPACK_DEBIAN_PACKAGE_SHLIBDEPS_PRIVATE_DIRS</code></p>
<dd>New in version 3.20. </p>
<p> May be set to a list of directories that will be given to <code>dpkg-shlibdeps</code> via its <code>-l</code> option. These will be searched by <code>dpkg-shlibdeps</code> in order to find private shared library dependencies.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : </p>
<p> <code>NOTE:</code> You should prefer to set <code>CMAKE_INSTALL_RPATH</code> to an appropriate value if you use <code>dpkg-shlibdeps</code>. The current option is really only needed for private shared library dependencies.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_DEBUG</code></p>
<dd>May be set when invoking cpack in order to trace debug information during the CPack DEB generator run.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_DEBIAN_PACKAGE_PREDEPENDS</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_PREDEPENDS</code></p>
<dd>Sets the <i>Pre-Depends</i> field of the Debian package. Like <i>Depends</i>, except that it also forces <code>dpkg</code> to complete installation of the packages named before even starting the installation of the package which declares the pre-dependency.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><i>CPACK_DEBIAN_PACKAGE_PREDEPENDS</i> for component-based installations. </p>
<p> New in version 3.4: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_PREDEPENDS</code> variables. </p>
<p> See <i><a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_ENHANCES</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_ENHANCES</code></p>
<dd>Sets the <i>Enhances</i> field of the Debian package. Similar to <i>Suggests</i> but works in the opposite direction: declares that a package can enhance the functionality of another package.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><i>CPACK_DEBIAN_PACKAGE_ENHANCES</i> for component-based installations. </p>
<p> New in version 3.4: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_ENHANCES</code> variables. </p>
<p> See <i><a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_BREAKS</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_BREAKS</code></p>
<dd>Sets the <i>Breaks</i> field of the Debian package. When a binary package (P) declares that it breaks other packages (B), <code>dpkg</code> will not allow the package (P) which declares <i>Breaks</i> be <code>unpacked</code> unless the packages that will be broken (B) are deconfigured first. As long as the package (P) is configured, the previously deconfigured packages (B) cannot be reconfigured again.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><i>CPACK_DEBIAN_PACKAGE_BREAKS</i> for component-based installations. </p>
<p> New in version 3.4: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_BREAKS</code> variables. </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-relationships.html#s-breaks">https://www.debian.org/doc/debian-policy/ch-relationships.html#s-breaks</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_CONFLICTS</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_CONFLICTS</code></p>
<dd>Sets the <i>Conflicts</i> field of the Debian package. When one binary package declares a conflict with another using a <i>Conflicts</i> field, <code>dpkg</code> will not allow them to be unpacked on the system at the same time.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><i>CPACK_DEBIAN_PACKAGE_CONFLICTS</i> for component-based installations. </p>
<p> New in version 3.4: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_CONFLICTS</code> variables. </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-relationships.html#s-conflicts">https://www.debian.org/doc/debian-policy/ch-relationships.html#s-conflicts</a></i> </p>
<p> <code>NOTE:</code> This is a stronger restriction than <i>Breaks</i>, which prevents the broken package from being configured while the breaking package is in the &quot;Unpacked&quot; state but allows both packages to be unpacked at the same time.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_PROVIDES</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_PROVIDES</code></p>
<dd>Sets the <i>Provides</i> field of the Debian package. A virtual package is one which appears in the <i>Provides</i> control field of another package.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><i>CPACK_DEBIAN_PACKAGE_PROVIDES</i> for component-based installations. </p>
<p> New in version 3.4: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_PROVIDES</code> variables. </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-relationships.html#s-virtual">https://www.debian.org/doc/debian-policy/ch-relationships.html#s-virtual</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_REPLACES</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_REPLACES</code></p>
<dd>Sets the <i>Replaces</i> field of the Debian package. Packages can declare in their control file that they should overwrite files in certain other packages, or completely replace other packages.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><i>CPACK_DEBIAN_PACKAGE_REPLACES</i> for component-based installations. </p>
<p> New in version 3.4: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_REPLACES</code> variables. </p>
<p> See <i><a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_RECOMMENDS</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_RECOMMENDS</code></p>
<dd>Sets the <i>Recommends</i> field of the Debian package. Allows packages to declare a strong, but not absolute, dependency on other packages.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><i>CPACK_DEBIAN_PACKAGE_RECOMMENDS</i> for component-based installations. </p>
<p> New in version 3.4: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_RECOMMENDS</code> variables. </p>
<p> See <i><a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_SUGGESTS</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_SUGGESTS</code></p>
<dd>Sets the <i>Suggests</i> field of the Debian package. Allows packages to declare a suggested package install grouping.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><i>CPACK_DEBIAN_PACKAGE_SUGGESTS</i> for component-based installations. </p>
<p> New in version 3.4: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_SUGGESTS</code> variables. </p>
<p> See <i><a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_GENERATE_SHLIBS</code></p>
<dd>New in version 3.6. </p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : OFF </p>
<p> Allows to generate shlibs control file automatically. Compatibility is defined by <i>CPACK_DEBIAN_PACKAGE_GENERATE_SHLIBS_POLICY</i> variable value. </p>
<p> <code>NOTE:</code> Libraries are only considered if they have both library name and version set. This can be done by setting SOVERSION property with <code>set_target_properties()</code> command.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_GENERATE_SHLIBS_POLICY</code></p>
<dd>New in version 3.6. </p>
<p> Compatibility policy for auto-generated shlibs control file.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &quot;=&quot; </p>
<p> Defines compatibility policy for auto-generated shlibs control file. Possible values: &quot;=&quot;, &quot;&gt;=&quot; </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-sharedlibs.html#s-sharedlibs-shlibdeps">https://www.debian.org/doc/debian-policy/ch-sharedlibs.html#s-sharedlibs-shlibdeps</a></i></p>
<dt><code>CPACK_DEBIAN_PACKAGE_CONTROL_EXTRA</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_CONTROL_EXTRA</code></p>
<dd>This variable allow advanced user to add custom script to the control.tar.gz. Typical usage is for conffiles, postinst, postrm, prerm.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> Usage: </p>
<pre>set(CPACK_DEBIAN_PACKAGE_CONTROL_EXTRA
 &quot;${CMAKE_CURRENT_SOURCE_DIR}/prerm;${CMAKE_CURRENT_SOURCE_DIR}/postrm&quot;)</pre>
<p>New in version 3.4: Per-component <code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_CONTROL_EXTRA</code> variables. </p>
<dt><code>CPACK_DEBIAN_PACKAGE_CONTROL_STRICT_PERMISSION</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_CONTROL_STRICT_PERMISSION</code></p>
<dd>New in version 3.4. </p>
<p> This variable indicates if the Debian policy on control files should be strictly followed.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : FALSE </p>
<p> Usage: </p>
<pre>set(CPACK_DEBIAN_PACKAGE_CONTROL_STRICT_PERMISSION TRUE)</pre>
<p>This overrides the permissions on the original files, following the rules set by Debian policy <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-files.html#s-permissions-owners">https://www.debian.org/doc/debian-policy/ch-files.html#s-permissions-owners</a></i> </p>
<p> <code>NOTE:</code> The original permissions of the files will be used in the final package unless this variable is set to <code>TRUE</code>. In particular, the scripts should have the proper executable flag prior to the generation of the package.</p>
<dt><code>CPACK_DEBIAN_PACKAGE_SOURCE</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;COMPONENT&gt;_PACKAGE_SOURCE</code></p>
<dd>New in version 3.5. </p>
<p> Sets the <code>Source</code> field of the binary Debian package. When the binary package name is not the same as the source package name (in particular when several components/binaries are generated from one source) the source from which the binary has been generated should be indicated with the field <code>Source</code>.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default :</p>
<dt>&bull;</p>
<dd>An empty string for non-component based installations</p>
<dt>&bull;</p>
<dd><i>CPACK_DEBIAN_PACKAGE_SOURCE</i> for component-based installations. </p>
<p> See <i><a rel="nofollow" href="https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Source">https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Source</a></i> </p>
<p> <code>NOTE:</code> This value is not interpreted. It is possible to pass an optional revision number of the referenced source package as well.</dl>
<h3>Packaging of debug information</h3>
<p>New in version 3.13. </p>
<p> Dbgsym packages contain debug symbols for debugging packaged binaries. </p>
<p> Dbgsym packaging has its own set of variables:</p>
<dl>
<dt><code>CPACK_DEBIAN_DEBUGINFO_PACKAGE</code></p>
<dd>
<dt><code>CPACK_DEBIAN_&lt;component&gt;_DEBUGINFO_PACKAGE</code></p>
<dd>Enable generation of dbgsym .ddeb package(s).</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : OFF </p>
<p> <code>NOTE:</code> Setting this also strips the ELF files in the generated non-dbgsym package, which results in debuginfo only being available in the dbgsym package. </p>
<p> <code>NOTE:</code> Binaries must contain debug symbols before packaging so use either <code>Debug</code> or <code>RelWithDebInfo</code> for <code>CMAKE_BUILD_TYPE</code> variable value. </p>
<p> Additionally, if <code>CPACK_STRIP_FILES</code> is set, the files will be stripped before they get to the DEB generator, so will not contain debug symbols and a dbgsym package will not get built. Do not use with <code>CPACK_STRIP_FILES</code>.</dl>
<h3>Building Debian packages on Windows</h3>
<p>New in version 3.10. </p>
<p> To communicate UNIX file permissions from the install stage to the CPack DEB generator the &quot;cmake_mode_t&quot; NTFS alternate data stream (ADT) is used. </p>
<p> When a filesystem without ADT support is used only owner read/write permissions can be preserved.</p>
<h3>Reproducible packages</h3>
<p>New in version 3.13. </p>
<p> The environment variable <code>SOURCE_DATE_EPOCH</code> may be set to a UNIX timestamp, defined as the number of seconds, excluding leap seconds, since 01 Jan 1970 00:00:00 UTC. If set, the CPack DEB generator will use its value for timestamps in the package.</p>
<h3>CPack DragNDrop Generator</h3>
<p>The DragNDrop CPack generator (macOS) creates a DMG image.</p>
<h3>Variables specific to CPack DragNDrop generator</h3>
<p>The following variables are specific to the DragNDrop installers built on macOS:</p>
<dl>
<dt><code>CPACK_DMG_VOLUME_NAME</code></p>
<dd>The volume name of the generated disk image. Defaults to CPACK_PACKAGE_FILE_NAME.</p>
<dt><code>CPACK_DMG_FORMAT</code></p>
<dd>The disk image format. Common values are <code>UDRO</code> (UDIF read-only), <code>UDZO</code> (UDIF zlib-compressed) or <code>UDBZ</code> (UDIF bzip2-compressed). Refer to <code><a href="/docs/linux/man/1-hdiutil/">hdiutil</a>(1)</code> for more information on other available formats. Defaults to <code>UDZO</code>.</p>
<dt><code>CPACK_DMG_DS_STORE</code></p>
<dd>Path to a custom <code>.DS_Store</code> file. This <code>.DS_Store</code> file can be used to specify the Finder window position/geometry and layout (such as hidden toolbars, placement of the icons etc.). This file has to be generated by the Finder (either manually or through AppleScript) using a normal folder from which the <code>.DS_Store</code> file can then be extracted.</p>
<dt><code>CPACK_DMG_DS_STORE_SETUP_SCRIPT</code></p>
<dd>New in version 3.5. </p>
<p> Path to a custom AppleScript file. This AppleScript is used to generate a <code>.DS_Store</code> file which specifies the Finder window position/geometry and layout (such as hidden toolbars, placement of the icons etc.). By specifying a custom AppleScript there is no need to use <code>CPACK_DMG_DS_STORE</code>, as the <code>.DS_Store</code> that is generated by the AppleScript will be packaged.</p>
<dt><code>CPACK_DMG_BACKGROUND_IMAGE</code></p>
<dd>Path to an image file to be used as the background. This file will be copied to <code>.background</code>/<code>background.&lt;ext&gt;</code>, where <code>&lt;ext&gt;</code> is the original image file extension. The background image is installed into the image before <code>CPACK_DMG_DS_STORE_SETUP_SCRIPT</code> is executed or <code>CPACK_DMG_DS_STORE</code> is installed. By default no background image is set.</p>
<dt><code>CPACK_DMG_DISABLE_APPLICATIONS_SYMLINK</code></p>
<dd>New in version 3.6. </p>
<p> Default behavior is to include a symlink to <code>/Applications</code> in the DMG. Set this option to <code>ON</code> to avoid adding the symlink.</p>
<dt><code>CPACK_DMG_SLA_DIR</code></p>
<dd>New in version 3.5. </p>
<p> Directory where license and menu files for different languages are stored. Setting this causes CPack to look for a <code>&lt;language&gt;.menu.txt</code> and <code>&lt;language&gt;.license.txt</code> or <code>&lt;language&gt;.license.rtf</code> file for every language defined in <code>CPACK_DMG_SLA_LANGUAGES</code>. If both this variable and <code>CPACK_RESOURCE_FILE_LICENSE</code> are set, CPack will only look for the menu files and use the same license file for all languages. If both <code>&lt;language&gt;.license.txt</code> and <code>&lt;language&gt;.license.rtf</code> exist, the <code>.txt</code> file will be used. </p>
<p> New in version 3.17: RTF support. </p>
<dt><code>CPACK_DMG_SLA_LANGUAGES</code></p>
<dd>New in version 3.5. </p>
<p> Languages for which a license agreement is provided when mounting the generated DMG. A menu file consists of 9 lines of text. The first line is is the name of the language itself, uppercase, in English (e.g. German). The other lines are translations of the following strings:</p>
<dt>&bull;</p>
<dd>Agree</p>
<dt>&bull;</p>
<dd>Disagree</p>
<dt>&bull;</p>
<dd>Print</p>
<dt>&bull;</p>
<dd>Save&#8230;</p>
<dt>&bull;</p>
<dd>You agree to the terms of the License Agreement when you click the &quot;Agree&quot; button.</p>
<dt>&bull;</p>
<dd>Software License Agreement</p>
<dt>&bull;</p>
<dd>This text cannot be saved. The disk may be full or locked, or the file may be locked.</p>
<dt>&bull;</p>
<dd>Unable to print. Make sure you have selected a printer. </p>
<p> For every language in this list, CPack will try to find files <code>&lt;language&gt;.menu.txt</code> and <code>&lt;language&gt;.license.txt</code> in the directory specified by the <i>CPACK_DMG_SLA_DIR</i> variable.</p>
<dt><code>CPACK_DMG_&lt;component&gt;_FILE_NAME</code></p>
<dd>New in version 3.17. </p>
<p> File name when packaging <code>&lt;component&gt;</code> as its own DMG (<code>CPACK_COMPONENTS_GROUPING</code> set to IGNORE).</p>
<dt>&bull;</p>
<dd>Default: <code>CPACK_PACKAGE_FILE_NAME-&lt;component&gt;</code></p>
<dt><code>CPACK_DMG_FILESYSTEM</code></p>
<dd>New in version 3.21. </p>
<p> The filesystem format. Common values are <code>APFS</code> and <code>HFS+</code>. See <code>man hdiutil</code> for a full list of supported formats. Defaults to <code>HFS+</code>.</p>
<dt><code>CPACK_COMMAND_HDIUTIL</code></p>
<dd>Path to the <code><a href="/docs/linux/man/1-hdiutil/">hdiutil</a>(1)</code> command used to operate on disk image files on macOS. This variable can be used to override the automatically detected command (or specify its location if the auto-detection fails to find it).</p>
<dt><code>CPACK_COMMAND_SETFILE</code></p>
<dd>Path to the <code><a href="/docs/linux/man/1-setfile/">SetFile</a>(1)</code> command used to set extended attributes on files and directories on macOS. This variable can be used to override the automatically detected command (or specify its location if the auto-detection fails to find it).</p>
<dt><code>CPACK_COMMAND_REZ</code></p>
<dd>Path to the <code><a href="/docs/linux/man/1-rez/">Rez</a>(1)</code> command used to compile resources on macOS. This variable can be used to override the automatically detected command (or specify its location if the auto-detection fails to find it).</dl>
<h3>CPack External Generator</h3>
<p>New in version 3.13. </p>
<p> CPack provides many generators to create packages for a variety of platforms and packaging systems. The intention is for CMake/CPack to be a complete end-to-end solution for building and packaging a software project. However, it may not always be possible to use CPack for the entire packaging process, due to either technical limitations or policies that require the use of certain tools. For this reason, CPack provides the &quot;External&quot; generator, which allows external packaging software to take advantage of some of the functionality provided by CPack, such as component installation and the dependency graph.</p>
<h3>Integration with External Packaging Tools</h3>
<p>The CPack External generator generates a <code>.json</code> file containing the CPack internal metadata, which gives external software information on how to package the software. External packaging software may itself invoke CPack, consume the generated metadata, install and package files as required. </p>
<p> Alternatively CPack can invoke an external packaging software through an optional custom CMake script in <i>CPACK_EXTERNAL_PACKAGE_SCRIPT</i> instead. </p>
<p> Staging of installation files may also optionally be taken care of by the generator when enabled through the <i>CPACK_EXTERNAL_ENABLE_STAGING</i> variable.</p>
<h3>JSON Format</h3>
<p>The JSON metadata file contains a list of CPack components and component groups, the various options passed to <code>cpack_add_component()</code> and <code>cpack_add_component_group()</code>, the dependencies between the components and component groups, and various other options passed to CPack. </p>
<p> The JSON&#8217;s root object will always provide two fields: <code>formatVersionMajor</code> and <code>formatVersionMinor</code>, which are always integers that describe the output format of the generator. Backwards-compatible changes to the output format (for example, adding a new field that didn&#8217;t exist before) cause the minor version to be incremented, and backwards-incompatible changes (for example, deleting a field or changing its meaning) cause the major version to be incremented and the minor version reset to 0. The format version is always of the format <code>major.minor</code>. In other words, it always has exactly two parts, separated by a period. </p>
<p> You can request one or more specific versions of the output format as described below with <i>CPACK_EXTERNAL_REQUESTED_VERSIONS</i>. The output format will have a major version that exactly matches the requested major version, and a minor version that is greater than or equal to the requested minor version. If no version is requested with <i>CPACK_EXTERNAL_REQUESTED_VERSIONS</i>, the latest known major version is used by default. Currently, the only supported format is 1.0, which is described below.</p>
<h3>Version 1.0</h3>
<p>In addition to the standard format fields, format version 1.0 provides the following fields in the root:</p>
<dl>
<dt><code>components</code></p>
<dd>The <code>components</code> field is an object with component names as the keys and objects describing the components as the values. The component objects have the following fields:</p>
<dt><code>name</code></p>
<dd>The name of the component. This is always the same as the key in the <code>components</code> object.</p>
<dt><code>displayName</code></p>
<dd>The value of the <code>DISPLAY_NAME</code> field passed to <code>cpack_add_component()</code>.</p>
<dt><code>description</code></p>
<dd>The value of the <code>DESCRIPTION</code> field passed to <code>cpack_add_component()</code>.</p>
<dt><code>isHidden</code></p>
<dd>True if <code>HIDDEN</code> was passed to <code>cpack_add_component()</code>, false if it was not.</p>
<dt><code>isRequired</code></p>
<dd>True if <code>REQUIRED</code> was passed to <code>cpack_add_component()</code>, false if it was not.</p>
<dt><code>isDisabledByDefault</code></p>
<dd>True if <code>DISABLED</code> was passed to <code>cpack_add_component()</code>, false if it was not.</p>
<dt><code>group</code></p>
<dd>Only present if <code>GROUP</code> was passed to <code>cpack_add_component()</code>. If so, this field is a string value containing the component&#8217;s group.</p>
<dt><code>dependencies</code></p>
<dd>An array of components the component depends on. This contains the values in the <code>DEPENDS</code> argument passed to <code>cpack_add_component()</code>. If no <code>DEPENDS</code> argument was passed, this is an empty list.</p>
<dt><code>installationTypes</code></p>
<dd>An array of installation types the component is part of. This contains the values in the <code>INSTALL_TYPES</code> argument passed to <code>cpack_add_component()</code>. If no <code>INSTALL_TYPES</code> argument was passed, this is an empty list.</p>
<dt><code>isDownloaded</code></p>
<dd>True if <code>DOWNLOADED</code> was passed to <code>cpack_add_component()</code>, false if it was not.</p>
<dt><code>archiveFile</code></p>
<dd>The name of the archive file passed with the <code>ARCHIVE_FILE</code> argument to <code>cpack_add_component()</code>. If no <code>ARCHIVE_FILE</code> argument was passed, this is an empty string.</p>
<dt><code>componentGroups</code></p>
<dd>The <code>componentGroups</code> field is an object with component group names as the keys and objects describing the component groups as the values. The component group objects have the following fields:</p>
<dt><code>name</code></p>
<dd>The name of the component group. This is always the same as the key in the <code>componentGroups</code> object.</p>
<dt><code>displayName</code></p>
<dd>The value of the <code>DISPLAY_NAME</code> field passed to <code>cpack_add_component_group()</code>.</p>
<dt><code>description</code></p>
<dd>The value of the <code>DESCRIPTION</code> field passed to <code>cpack_add_component_group()</code>.</p>
<dt><code>parentGroup</code></p>
<dd>Only present if <code>PARENT_GROUP</code> was passed to <code>cpack_add_component_group()</code>. If so, this field is a string value containing the component group&#8217;s parent group.</p>
<dt><code>isExpandedByDefault</code></p>
<dd>True if <code>EXPANDED</code> was passed to <code>cpack_add_component_group()</code>, false if it was not.</p>
<dt><code>isBold</code></p>
<dd>True if <code>BOLD_TITLE</code> was passed to <code>cpack_add_component_group()</code>, false if it was not.</p>
<dt><code>components</code></p>
<dd>An array of names of components that are direct members of the group (components that have this group as their <code>GROUP</code>). Components of subgroups are not included.</p>
<dt><code>subgroups</code></p>
<dd>An array of names of component groups that are subgroups of the group (groups that have this group as their <code>PARENT_GROUP</code>).</p>
<dt><code>installationTypes</code></p>
<dd>The <code>installationTypes</code> field is an object with installation type names as the keys and objects describing the installation types as the values. The installation type objects have the following fields:</p>
<dt><code>name</code></p>
<dd>The name of the installation type. This is always the same as the key in the <code>installationTypes</code> object.</p>
<dt><code>displayName</code></p>
<dd>The value of the <code>DISPLAY_NAME</code> field passed to <code>cpack_add_install_type()</code>.</p>
<dt><code>index</code></p>
<dd>The integer index of the installation type in the list.</p>
<dt><code>projects</code></p>
<dd>The <code>projects</code> field is an array of objects describing CMake projects which comprise the CPack project. The values in this field are derived from <code>CPACK_INSTALL_CMAKE_PROJECTS</code>. In most cases, this will be only a single project. The project objects have the following fields:</p>
<dt><code>projectName</code></p>
<dd>The project name passed to <code>CPACK_INSTALL_CMAKE_PROJECTS</code>.</p>
<dt><code>component</code></p>
<dd>The name of the component or component set which comprises the project.</p>
<dt><code>directory</code></p>
<dd>The build directory of the CMake project. This is the directory which contains the <code>cmake_install.cmake</code> script.</p>
<dt><code>subDirectory</code></p>
<dd>The subdirectory to install the project into inside the CPack package.</p>
<dt><code>packageName</code></p>
<dd>The package name given in <code>CPACK_PACKAGE_NAME</code>. Only present if this option is set.</p>
<dt><code>packageVersion</code></p>
<dd>The package version given in <code>CPACK_PACKAGE_VERSION</code>. Only present if this option is set.</p>
<dt><code>packageDescriptionFile</code></p>
<dd>The package description file given in <code>CPACK_PACKAGE_DESCRIPTION_FILE</code>. Only present if this option is set.</p>
<dt><code>packageDescriptionSummary</code></p>
<dd>The package description summary given in <code>CPACK_PACKAGE_DESCRIPTION_SUMMARY</code>. Only present if this option is set.</p>
<dt><code>buildConfig</code></p>
<dd>The build configuration given to CPack with the <code>-C</code> option. Only present if this option is set.</p>
<dt><code>defaultDirectoryPermissions</code></p>
<dd>The default directory permissions given in <code>CPACK_INSTALL_DEFAULT_DIRECTORY_PERMISSIONS</code>. Only present if this option is set.</p>
<dt><code>setDestdir</code></p>
<dd>True if <code>CPACK_SET_DESTDIR</code> is true, false if it is not.</p>
<dt><code>packagingInstallPrefix</code></p>
<dd>The install prefix given in <code>CPACK_PACKAGING_INSTALL_PREFIX</code>. Only present if <code>CPACK_SET_DESTDIR</code> is true.</p>
<dt><code>stripFiles</code></p>
<dd>True if <code>CPACK_STRIP_FILES</code> is true, false if it is not.</p>
<dt><code>warnOnAbsoluteInstallDestination</code></p>
<dd>True if <code>CPACK_WARN_ON_ABSOLUTE_INSTALL_DESTINATION</code> is true, false if it is not.</p>
<dt><code>errorOnAbsoluteInstallDestination</code></p>
<dd>True if <code>CPACK_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION</code> is true, false if it is not.</dl>
<h3>Variables specific to CPack External generator</h3>
<dl>
<dt><code>CPACK_EXTERNAL_REQUESTED_VERSIONS</code></p>
<dd>This variable is used to request a specific version of the CPack External generator. It is a list of <code>major.minor</code> values, separated by semicolons. </p>
<p> If this variable is set to a non-empty value, the CPack External generator will iterate through each item in the list to search for a version that it knows how to generate. Requested versions should be listed in order of descending preference by the client software, as the first matching version in the list will be generated. </p>
<p> The generator knows how to generate the version if it has a versioned generator whose major version exactly matches the requested major version, and whose minor version is greater than or equal to the requested minor version. For example, if <code>CPACK_EXTERNAL_REQUESTED_VERSIONS</code> contains 1.0, and the CPack External generator knows how to generate 1.1, it will generate 1.1. If the generator doesn&#8217;t know how to generate a version in the list, it skips the version and looks at the next one. If it doesn&#8217;t know how to generate any of the requested versions, an error is thrown. </p>
<p> If this variable is not set, or is empty, the CPack External generator will generate the highest major and minor version that it knows how to generate. </p>
<p> If an invalid version is encountered in <code>CPACK_EXTERNAL_REQUESTED_VERSIONS</code> (one that doesn&#8217;t match <code>major.minor</code>, where <code>major</code> and <code>minor</code> are integers), it is ignored.</p>
<dt><code>CPACK_EXTERNAL_ENABLE_STAGING</code></p>
<dd>This variable can be set to true to enable optional installation into a temporary staging area which can then be picked up and packaged by an external packaging tool. The top level directory used by CPack for the current packaging task is contained in <code>CPACK_TOPLEVEL_DIRECTORY</code>. It is automatically cleaned up on each run before packaging is initiated and can be used for custom temporary files required by the external packaging tool. It also contains the staging area <code>CPACK_TEMPORARY_DIRECTORY</code> into which CPack performs the installation when staging is enabled.</p>
<dt><code>CPACK_EXTERNAL_PACKAGE_SCRIPT</code></p>
<dd>This variable can optionally specify the full path to a CMake script file to be run as part of the CPack invocation. It is invoked after (optional) staging took place and may run an external packaging tool. The script has access to the variables defined by the CPack config file.</p>
<dt><code>CPACK_EXTERNAL_BUILT_PACKAGES</code></p>
<dd>New in version 3.19. </p>
<p> The <code>CPACK_EXTERNAL_PACKAGE_SCRIPT</code> script may set this list variable to the full paths of generated package files. CPack will copy these files from the staging directory back to the top build directory and possibly produce checksum files if the <code>CPACK_PACKAGE_CHECKSUM</code> is set.</dl>
<h3>CPack FreeBSD Generator</h3>
<p>New in version 3.10. </p>
<p> The built in (binary) CPack FreeBSD (pkg) generator (Unix only)</p>
<h3>Variables affecting the CPack FreeBSD (pkg) generator</h3>
<dl>
<dt>&bull;</p>
<dd>New in version 3.18: <code>CPACK_ARCHIVE_THREADS</code> </p>
</dl>
<h3>Variables specific to CPack FreeBSD (pkg) generator</h3>
<p>The CPack FreeBSD generator may be used to create <a href="/docs/linux/man/8-pkg/">pkg</a>(8) packages &#8212; these may be used on FreeBSD, DragonflyBSD, NetBSD, OpenBSD, but also on Linux or OSX, depending on the installed package-management tools &#8212; using <code>CPack</code>. </p>
<p> The CPack FreeBSD generator is a <code>CPack</code> generator and uses the <code>CPACK_XXX</code> variables used by <code>CPack</code>. It tries to re-use packaging information that may already be specified for Debian packages for the <code>CPack DEB Generator</code>. It also tries to re-use RPM packaging information when Debian does not specify. </p>
<p> The CPack FreeBSD generator should work on any host with libpkg installed. The packages it produces are specific to the host architecture and ABI. </p>
<p> The CPack FreeBSD generator sets package-metadata through <code>CPACK_FREEBSD_XXX</code> variables. The CPack FreeBSD generator, unlike the CPack Deb generator, does not specially support componentized packages; a single package is created from all the software artifacts created through CMake. </p>
<p> All of the variables can be set specifically for FreeBSD packaging in the CPackConfig file or in CMakeLists.txt, but most of them have defaults that use general settings (e.g. CMAKE_PROJECT_NAME) or Debian-specific variables when those make sense (e.g. the homepage of an upstream project is usually unchanged by the flavor of packaging). When there is no Debian information to fall back on, but the RPM packaging has it, fall back to the RPM information (e.g. package license).</p>
<dl>
<dt><code>CPACK_FREEBSD_PACKAGE_NAME</code></p>
<dd>Sets the package name (in the package manifest, but also affects the output filename).</p>
<dt>&bull;</p>
<dd>Mandatory: YES</p>
<dt>&bull;</p>
<dd>Default:</p>
<dt>&bull;</p>
<dd><code>CPACK_PACKAGE_NAME</code> (this is always set by CPack itself, based on CMAKE_PROJECT_NAME).</p>
<dt><code>CPACK_FREEBSD_PACKAGE_COMMENT</code></p>
<dd>Sets the package comment. This is the short description displayed by <a href="/docs/linux/man/8-pkg/">pkg</a>(8) in standard &quot;pkg info&quot; output.</p>
<dt>&bull;</p>
<dd>Mandatory: YES</p>
<dt>&bull;</p>
<dd>Default:</p>
<dt>&bull;</p>
<dd><code>CPACK_PACKAGE_DESCRIPTION_SUMMARY</code> (this is always set by CPack itself, if nothing else sets it explicitly).</p>
<dt>&bull;</p>
<dd><code>PROJECT_DESCRIPTION</code> (this can be set with the DESCRIPTION parameter for <code>project()</code>).</p>
<dt><code>CPACK_FREEBSD_PACKAGE_DESCRIPTION</code></p>
<dd>Sets the package description. This is the long description of the package, given by &quot;pkg info&quot; with a specific package as argument.</p>
<dt>&bull;</p>
<dd>Mandatory: YES</p>
<dt>&bull;</p>
<dd>Default:</p>
<dt>&bull;</p>
<dd><code>CPACK_DEBIAN_PACKAGE_DESCRIPTION</code> (this may be set already for Debian packaging, so it is used as a fallback).</p>
<dt><code>CPACK_FREEBSD_PACKAGE_WWW</code></p>
<dd>The URL of the web site for this package, preferably (when applicable) the site from which the original source can be obtained and any additional upstream documentation or information may be found.</p>
<dt>&bull;</p>
<dd>Mandatory: YES</p>
<dt>&bull;</p>
<dd>Default:</p>
<dt>&bull;</p>
<dd><code>CMAKE_PROJECT_HOMEPAGE_URL</code>, or if that is not set, <code>CPACK_DEBIAN_PACKAGE_HOMEPAGE</code> (this may be set already for Debian packaging, so it is used as a fallback). </p>
<p> New in version 3.12: The <code>CMAKE_PROJECT_HOMEPAGE_URL</code> variable. </p>
<dt><code>CPACK_FREEBSD_PACKAGE_LICENSE</code></p>
<dd>The license, or licenses, which apply to this software package. This must be one or more license-identifiers that pkg recognizes as acceptable license identifiers (e.g. &quot;GPLv2&quot;).</p>
<dt>&bull;</p>
<dd>Mandatory: YES</p>
<dt>&bull;</p>
<dd>Default:</p>
<dt>&bull;</p>
<dd><code>CPACK_RPM_PACKAGE_LICENSE</code></p>
<dt><code>CPACK_FREEBSD_PACKAGE_LICENSE_LOGIC</code></p>
<dd>This variable is only of importance if there is more than one license. The default is &quot;single&quot;, which is only applicable to a single license. Other acceptable values are determined by pkg &#8212; those are &quot;dual&quot; or &quot;multi&quot; &#8212; meaning choice (OR) or simultaneous (AND) application of the licenses.</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: single</p>
<dt><code>CPACK_FREEBSD_PACKAGE_MAINTAINER</code></p>
<dd>The FreeBSD maintainer (e.g. <i>kde [at] freebsd.org</i>) of this package.</p>
<dt>&bull;</p>
<dd>Mandatory: YES</p>
<dt>&bull;</p>
<dd>Default: none</p>
<dt><code>CPACK_FREEBSD_PACKAGE_ORIGIN</code></p>
<dd>The origin (ports label) of this package; for packages built by CPack outside of the ports system this is of less importance. The default puts the package somewhere under misc/, as a stopgap.</p>
<dt>&bull;</p>
<dd>Mandatory: YES</p>
<dt>&bull;</p>
<dd>Default: misc/&lt;package name&gt;</p>
<dt><code>CPACK_FREEBSD_PACKAGE_CATEGORIES</code></p>
<dd>The ports categories where this package lives (if it were to be built from ports). If none is set a single category is determined based on the package origin.</p>
<dt>&bull;</p>
<dd>Mandatory: YES</p>
<dt>&bull;</p>
<dd>Default: derived from ORIGIN</p>
<dt><code>CPACK_FREEBSD_PACKAGE_DEPS</code></p>
<dd>A list of package origins that should be added as package dependencies. These are in the form &lt;category&gt;/&lt;packagename&gt;, e.g. x11/libkonq. No version information needs to be provided (this is not included in the manifest).</p>
<dt>&bull;</p>
<dd>Mandatory: NO</p>
<dt>&bull;</p>
<dd>Default: empty</dl>
<h3>CPack IFW Generator</h3>
<p>New in version 3.1. </p>
<p> Configure and run the Qt Installer Framework to generate a Qt installer.</p>
<h3>Overview</h3>
<p>This <code>cpack generator</code> generates configuration and meta information for the <i>Qt Installer Framework</i> (QtIFW), and runs QtIFW tools to generate a Qt installer. </p>
<p> QtIFW provides tools and utilities to create installers for the platforms supported by <i>Qt</i>: Linux, Microsoft Windows, and macOS. </p>
<p> To make use of this generator, QtIFW needs to be installed. The <code>CPackIFW</code> module looks for the location of the QtIFW command-line utilities, and defines several commands to control the behavior of this generator.</p>
<h3>Variables</h3>
<p>You can use the following variables to change behavior of CPack <code>IFW</code> generator.</p>
<h3>Debug</h3>
<dl>
<dt><code>CPACK_IFW_VERBOSE</code></p>
<dd>New in version 3.3. </p>
<p> Set to <code>ON</code> to enable addition debug output. By default is <code>OFF</code>.</dl>
<h3>Package</h3>
<dl>
<dt><code>CPACK_IFW_PACKAGE_TITLE</code></p>
<dd>Name of the installer as displayed on the title bar. By default used <code>CPACK_PACKAGE_DESCRIPTION_SUMMARY</code>.</p>
<dt><code>CPACK_IFW_PACKAGE_PUBLISHER</code></p>
<dd>Publisher of the software (as shown in the Windows Control Panel). By default used <code>CPACK_PACKAGE_VENDOR</code>.</p>
<dt><code>CPACK_IFW_PRODUCT_URL</code></p>
<dd>URL to a page that contains product information on your web site.</p>
<dt><code>CPACK_IFW_PACKAGE_ICON</code></p>
<dd>Filename for a custom installer icon. The actual file is &#8216;.icns&#8217; (macOS), &#8216;.ico&#8217; (Windows). No functionality on Unix.</p>
<dt><code>CPACK_IFW_PACKAGE_WINDOW_ICON</code></p>
<dd>Filename for a custom window icon in PNG format for the Installer application.</p>
<dt><code>CPACK_IFW_PACKAGE_LOGO</code></p>
<dd>Filename for a logo is used as QWizard::LogoPixmap.</p>
<dt><code>CPACK_IFW_PACKAGE_WATERMARK</code></p>
<dd>New in version 3.8. </p>
<p> Filename for a watermark is used as QWizard::WatermarkPixmap.</p>
<dt><code>CPACK_IFW_PACKAGE_BANNER</code></p>
<dd>New in version 3.8. </p>
<p> Filename for a banner is used as QWizard::BannerPixmap.</p>
<dt><code>CPACK_IFW_PACKAGE_BACKGROUND</code></p>
<dd>New in version 3.8. </p>
<p> Filename for an image used as QWizard::BackgroundPixmap (only used by MacStyle).</p>
<dt><code>CPACK_IFW_PACKAGE_WIZARD_STYLE</code></p>
<dd>New in version 3.8. </p>
<p> Wizard style to be used (&quot;Modern&quot;, &quot;Mac&quot;, &quot;Aero&quot; or &quot;Classic&quot;).</p>
<dt><code>CPACK_IFW_PACKAGE_WIZARD_DEFAULT_WIDTH</code></p>
<dd>New in version 3.8. </p>
<p> Default width of the wizard in pixels. Setting a banner image will override this.</p>
<dt><code>CPACK_IFW_PACKAGE_WIZARD_DEFAULT_HEIGHT</code></p>
<dd>New in version 3.8. </p>
<p> Default height of the wizard in pixels. Setting a watermark image will override this.</p>
<dt><code>CPACK_IFW_PACKAGE_WIZARD_SHOW_PAGE_LIST</code></p>
<dd>New in version 3.20. </p>
<p> Set to <code>OFF</code> if the widget listing installer pages on the left side of the wizard should not be shown. </p>
<p> It is <code>ON</code> by default, but will only have an effect if using QtIFW 4.0 or later.</p>
<dt><code>CPACK_IFW_PACKAGE_TITLE_COLOR</code></p>
<dd>New in version 3.8. </p>
<p> Color of the titles and subtitles (takes an HTML color code, such as &quot;#88FF33&quot;).</p>
<dt><code>CPACK_IFW_PACKAGE_STYLE_SHEET</code></p>
<dd>New in version 3.15. </p>
<p> Filename for a stylesheet.</p>
<dt><code>CPACK_IFW_TARGET_DIRECTORY</code></p>
<dd>Default target directory for installation. By default used &quot;@ApplicationsDir@/<code>CPACK_PACKAGE_INSTALL_DIRECTORY</code>&quot; (variables embedded in &#8216;@&#8217; are expanded by the <i>QtIFW scripting engine</i>). </p>
<p> You can use predefined variables.</p>
<dt><code>CPACK_IFW_ADMIN_TARGET_DIRECTORY</code></p>
<dd>Default target directory for installation with administrator rights. </p>
<p> You can use predefined variables.</p>
<dt><code>CPACK_IFW_PACKAGE_REMOVE_TARGET_DIR</code></p>
<dd>New in version 3.11. </p>
<p> Set to <code>OFF</code> if the target directory should not be deleted when uninstalling. </p>
<p> Is <code>ON</code> by default</p>
<dt><code>CPACK_IFW_PACKAGE_GROUP</code></p>
<dd>The group, which will be used to configure the root package</p>
<dt><code>CPACK_IFW_PACKAGE_NAME</code></p>
<dd>The root package name, which will be used if configuration group is not specified</p>
<dt><code>CPACK_IFW_PACKAGE_START_MENU_DIRECTORY</code></p>
<dd>New in version 3.3. </p>
<p> Name of the default program group for the product in the Windows Start menu. </p>
<p> By default used <i>CPACK_IFW_PACKAGE_NAME</i>.</p>
<dt><code>CPACK_IFW_PACKAGE_MAINTENANCE_TOOL_NAME</code></p>
<dd>New in version 3.3. </p>
<p> Filename of the generated maintenance tool. The platform-specific executable file extension is appended. </p>
<p> By default used QtIFW defaults (<code>maintenancetool</code>).</p>
<dt><code>CPACK_IFW_PACKAGE_MAINTENANCE_TOOL_INI_FILE</code></p>
<dd>New in version 3.3. </p>
<p> Filename for the configuration of the generated maintenance tool. </p>
<p> By default used QtIFW defaults (<code>maintenancetool.ini</code>).</p>
<dt><code>CPACK_IFW_PACKAGE_ALLOW_NON_ASCII_CHARACTERS</code></p>
<dd>New in version 3.3. </p>
<p> Set to <code>ON</code> if the installation path can contain non-ASCII characters. </p>
<p> Is <code>ON</code> for QtIFW less 2.0 tools.</p>
<dt><code>CPACK_IFW_PACKAGE_ALLOW_SPACE_IN_PATH</code></p>
<dd>New in version 3.3. </p>
<p> Set to <code>OFF</code> if the installation path cannot contain space characters. </p>
<p> Is <code>ON</code> for QtIFW less 2.0 tools.</p>
<dt><code>CPACK_IFW_PACKAGE_CONTROL_SCRIPT</code></p>
<dd>New in version 3.3. </p>
<p> Filename for a custom installer control script.</p>
<dt><code>CPACK_IFW_PACKAGE_RESOURCES</code></p>
<dd>New in version 3.7. </p>
<p> List of additional resources (&#8216;.qrc&#8217; files) to include in the installer binary. </p>
<p> You can use <code>cpack_ifw_add_package_resources()</code> command to resolve relative paths.</p>
<dt><code>CPACK_IFW_PACKAGE_FILE_EXTENSION</code></p>
<dd>New in version 3.10. </p>
<p> The target binary extension. </p>
<p> On Linux, the name of the target binary is automatically extended with &#8216;.run&#8217;, if you do not specify the extension. </p>
<p> On Windows, the target is created as an application with the extension &#8216;.exe&#8217;, which is automatically added, if not supplied. </p>
<p> On Mac, the target is created as an DMG disk image with the extension &#8216;.dmg&#8217;, which is automatically added, if not supplied.</p>
<dt><code>CPACK_IFW_REPOSITORIES_ALL</code></p>
<dd>The list of remote repositories. </p>
<p> The default value of this variable is computed by CPack and contains all repositories added with command <code>cpack_ifw_add_repository()</code> or updated with command <code>cpack_ifw_update_repository()</code>.</p>
<dt><code>CPACK_IFW_DOWNLOAD_ALL</code></p>
<dd>If this is <code>ON</code> all components will be downloaded. By default is <code>OFF</code> or used value from <code>CPACK_DOWNLOAD_ALL</code> if set</dl>
<h3>Components</h3>
<dl>
<dt><code>CPACK_IFW_RESOLVE_DUPLICATE_NAMES</code></p>
<dd>Resolve duplicate names when installing components with groups.</p>
<dt><code>CPACK_IFW_PACKAGES_DIRECTORIES</code></p>
<dd>Additional prepared packages dirs that will be used to resolve dependent components.</p>
<dt><code>CPACK_IFW_REPOSITORIES_DIRECTORIES</code></p>
<dd>New in version 3.10. </p>
<p> Additional prepared repository dirs that will be used to resolve and repack dependent components. This feature available only since QtIFW 3.1.</dl>
<h3>QtIFW Tools</h3>
<dl>
<dt><code>CPACK_IFW_FRAMEWORK_VERSION</code></p>
<dd>New in version 3.3. </p>
<p> The version of used QtIFW tools. </p>
<p> The following variables provide the locations of the QtIFW command-line tools as discovered by the module <code>CPackIFW</code>. These variables are cached, and may be configured if needed.</p>
<dt><code>CPACK_IFW_ARCHIVEGEN_EXECUTABLE</code></p>
<dd>New in version 3.19. </p>
<p> The path to <code>archivegen</code>.</p>
<dt><code>CPACK_IFW_BINARYCREATOR_EXECUTABLE</code></p>
<dd>The path to <code>binarycreator</code>.</p>
<dt><code>CPACK_IFW_REPOGEN_EXECUTABLE</code></p>
<dd>The path to <code>repogen</code>.</p>
<dt><code>CPACK_IFW_INSTALLERBASE_EXECUTABLE</code></p>
<dd>The path to <code>installerbase</code>.</p>
<dt><code>CPACK_IFW_DEVTOOL_EXECUTABLE</code></p>
<dd>The path to <code>devtool</code>.</dl>
<h3>Hints for Finding QtIFW</h3>
<p>Generally, the CPack <code>IFW</code> generator automatically finds QtIFW tools, but if you don&#8217;t use a default path for installation of the QtIFW tools, the path may be specified in either a CMake or an environment variable:</p>
<dl>
<dt><code>CPACK_IFW_ROOT</code></p>
<dd>New in version 3.9. </p>
<p> An CMake variable which specifies the location of the QtIFW tool suite. </p>
<p> The variable will be cached in the <code>CPackConfig.cmake</code> file and used at CPack runtime.</p>
<dt><code>QTIFWDIR</code></p>
<dd>An environment variable which specifies the location of the QtIFW tool suite. </p>
<p> <code>NOTE:</code> The specified path should not contain &quot;bin&quot; at the end (for example: &quot;D:\DevTools\QtIFW2.0.5&quot;). </p>
<p> The <i>CPACK_IFW_ROOT</i> variable has a higher priority and overrides the value of the <i>QTIFWDIR</i> variable.</dl>
<h3>Other Settings</h3>
<h3>Online installer</h3>
<p>By default, this generator generates an <i>offline installer</i>. This means that that all packaged files are fully contained in the installer executable. </p>
<p> In contrast, an <i>online installer</i> will download some or all components from a remote server. </p>
<p> The <code>DOWNLOADED</code> option in the <code>cpack_add_component()</code> command specifies that a component is to be downloaded. Alternatively, the <code>ALL</code> option in the <code>cpack_configure_downloads()</code> command specifies that <i>all</i> components are to be be downloaded. </p>
<p> The <code>cpack_ifw_add_repository()</code> command and the <i>CPACK_IFW_DOWNLOAD_ALL</i> variable allow for more specific configuration. </p>
<p> When there are online components, CPack will write them to archive files. The help page of the <code>CPackComponent</code> module, especially the section on the <code>cpack_configure_downloads()</code> function, explains how to make these files accessible from a download URL.</p>
<h3>Internationalization</h3>
<p>New in version 3.9. </p>
<p> Some variables and command arguments support internationalization via CMake script. This is an optional feature. </p>
<p> Installers created by QtIFW tools have built-in support for internationalization and many phrases are localized to many languages, but this does not apply to the description of the your components and groups that will be distributed. </p>
<p> Localization of the description of your components and groups is useful for users of your installers. </p>
<p> A localized variable or argument can contain a single default value, and a set of pairs the name of the locale and the localized value. </p>
<p> For example: </p>
<pre>set(LOCALIZABLE_VARIABLE &quot;Default value&quot;
 en &quot;English value&quot;
 en_US &quot;American value&quot;
 en_GB &quot;Great Britain value&quot;
 )</pre>
<h3>See Also</h3>
<p>Qt Installer Framework Manual:</p>
<dl>
<dt>&bull;</p>
<dd>Index page: <i><a rel="nofollow" href="http://doc.qt.io/qtinstallerframework/index.html">http://doc.qt.io/qtinstallerframework/index.html</a></i></p>
<dt>&bull;</p>
<dd>Component Scripting: <i><a rel="nofollow" href="http://doc.qt.io/qtinstallerframework/scripting.html">http://doc.qt.io/qtinstallerframework/scripting.html</a></i></p>
<dt>&bull;</p>
<dd>Predefined Variables: <i><a rel="nofollow" href="http://doc.qt.io/qtinstallerframework/scripting.html#predefined-variables">http://doc.qt.io/qtinstallerframework/scripting.html#predefined-variables</a></i></p>
<dt>&bull;</p>
<dd>Promoting Updates: <i><a rel="nofollow" href="http://doc.qt.io/qtinstallerframework/ifw-updates.html">http://doc.qt.io/qtinstallerframework/ifw-updates.html</a></i></p>
<dt><code>Download Qt Installer Framework for your platform from Qt site:</code></p>
<dd><i><a rel="nofollow" href="http://download.qt.io/official_releases/qt-installer-framework">http://download.qt.io/official_releases/qt-installer-framework</a></i></dl>
<h3>CPack NSIS Generator</h3>
<p>CPack Nullsoft Scriptable Install System (NSIS) generator specific options. </p>
<p> Changed in version 3.22: The NSIS generator requires NSIS 3.03 or newer.</p>
<h3>Variables specific to CPack NSIS generator</h3>
<p>The following variables are specific to the graphical installers built on Windows Nullsoft Scriptable Install System.</p>
<dl>
<dt><code>CPACK_NSIS_INSTALL_ROOT</code></p>
<dd>The default installation directory presented to the end user by the NSIS installer is under this root dir. The full directory presented to the end user is: <code>${CPACK_NSIS_INSTALL_ROOT}/${CPACK_PACKAGE_INSTALL_DIRECTORY}</code></p>
<dt><code>CPACK_NSIS_MUI_ICON</code></p>
<dd>An icon filename. The name of a <code>*.ico</code> file used as the main icon for the generated install program.</p>
<dt><code>CPACK_NSIS_MUI_UNIICON</code></p>
<dd>An icon filename. The name of a <code>*.ico</code> file used as the main icon for the generated uninstall program.</p>
<dt><code>CPACK_NSIS_INSTALLER_MUI_ICON_CODE</code></p>
<dd>undocumented.</p>
<dt><code>CPACK_NSIS_MUI_WELCOMEFINISHPAGE_BITMAP</code></p>
<dd>New in version 3.5. </p>
<p> The filename of a bitmap to use as the NSIS <code>MUI_WELCOMEFINISHPAGE_BITMAP</code>.</p>
<dt><code>CPACK_NSIS_MUI_UNWELCOMEFINISHPAGE_BITMAP</code></p>
<dd>New in version 3.5. </p>
<p> The filename of a bitmap to use as the NSIS <code>MUI_UNWELCOMEFINISHPAGE_BITMAP</code>.</p>
<dt><code>CPACK_NSIS_EXTRA_PREINSTALL_COMMANDS</code></p>
<dd>Extra NSIS commands that will be added to the beginning of the install Section, before your install tree is available on the target system.</p>
<dt><code>CPACK_NSIS_EXTRA_INSTALL_COMMANDS</code></p>
<dd>Extra NSIS commands that will be added to the end of the install Section, after your install tree is available on the target system.</p>
<dt><code>CPACK_NSIS_EXTRA_UNINSTALL_COMMANDS</code></p>
<dd>Extra NSIS commands that will be added to the uninstall Section, before your install tree is removed from the target system.</p>
<dt><code>CPACK_NSIS_COMPRESSOR</code></p>
<dd>The arguments that will be passed to the NSIS <i>SetCompressor</i> command.</p>
<dt><code>CPACK_NSIS_ENABLE_UNINSTALL_BEFORE_INSTALL</code></p>
<dd>Ask about uninstalling previous versions first. If this is set to <code>ON</code>, then an installer will look for previous installed versions and if one is found, ask the user whether to uninstall it before proceeding with the install.</p>
<dt><code>CPACK_NSIS_MODIFY_PATH</code></p>
<dd>Modify <code>PATH</code> toggle. If this is set to <code>ON</code>, then an extra page will appear in the installer that will allow the user to choose whether the program directory should be added to the system <code>PATH</code> variable.</p>
<dt><code>CPACK_NSIS_DISPLAY_NAME</code></p>
<dd>The display name string that appears in the Windows <i>Apps &amp; features</i> in <i>Control Panel</i></p>
<dt><code>CPACK_NSIS_PACKAGE_NAME</code></p>
<dd>The title displayed at the top of the installer.</p>
<dt><code>CPACK_NSIS_INSTALLED_ICON_NAME</code></p>
<dd>A path to the executable that contains the installer icon.</p>
<dt><code>CPACK_NSIS_HELP_LINK</code></p>
<dd>URL to a web site providing assistance in installing your application.</p>
<dt><code>CPACK_NSIS_URL_INFO_ABOUT</code></p>
<dd>URL to a web site providing more information about your application.</p>
<dt><code>CPACK_NSIS_CONTACT</code></p>
<dd>Contact information for questions and comments about the installation process.</p>
<dt><code>CPACK_NSIS_&lt;compName&gt;_INSTALL_DIRECTORY</code></p>
<dd>New in version 3.7. </p>
<p> Custom install directory for the specified component <code>&lt;compName&gt;</code> instead of <code>$INSTDIR</code>.</p>
<dt><code>CPACK_NSIS_CREATE_ICONS_EXTRA</code></p>
<dd>Additional NSIS commands for creating <i>Start Menu</i> shortcuts.</p>
<dt><code>CPACK_NSIS_DELETE_ICONS_EXTRA</code></p>
<dd>Additional NSIS commands to uninstall <i>Start Menu</i> shortcuts.</p>
<dt><code>CPACK_NSIS_EXECUTABLES_DIRECTORY</code></p>
<dd>Creating NSIS <i>Start Menu</i> links assumes that they are in <code>bin</code> unless this variable is set. For example, you would set this to <code>exec</code> if your executables are in an exec directory.</p>
<dt><code>CPACK_NSIS_MUI_FINISHPAGE_RUN</code></p>
<dd>Specify an executable to add an option to run on the finish page of the NSIS installer.</p>
<dt><code>CPACK_NSIS_MENU_LINKS</code></p>
<dd>Specify links in <code>[application]</code> menu. This should contain a list of pair <code>link</code> <code>link name</code>. The link may be a URL or a path relative to installation prefix. Like: </p>
<pre>set(CPACK_NSIS_MENU_LINKS
 &quot;doc/cmake- [at] CMake_VERSION_MAJOR@.@CMake_VERSION_MINOR@/cmake.html&quot;
 &quot;CMake Help&quot; &quot;<a rel="nofollow" href="https://cmake.org">https://cmake.org</a>&quot; &quot;CMake Web Site&quot;)</pre>
<dt><code>CPACK_NSIS_UNINSTALL_NAME</code></p>
<dd>New in version 3.17. </p>
<p> Specify the name of the program to uninstall the version. Default is <code>Uninstall</code>.</p>
<dt><code>CPACK_NSIS_WELCOME_TITLE</code></p>
<dd>New in version 3.17. </p>
<p> The title to display on the top of the page for the welcome page.</p>
<dt><code>CPACK_NSIS_WELCOME_TITLE_3LINES</code></p>
<dd>New in version 3.17. </p>
<p> Display the title in the welcome page on 3 lines instead of 2.</p>
<dt><code>CPACK_NSIS_FINISH_TITLE</code></p>
<dd>New in version 3.17. </p>
<p> The title to display on the top of the page for the finish page.</p>
<dt><code>CPACK_NSIS_FINISH_TITLE_3LINES</code></p>
<dd>New in version 3.17. </p>
<p> Display the title in the finish page on 3 lines instead of 2.</p>
<dt><code>CPACK_NSIS_MUI_HEADERIMAGE</code></p>
<dd>New in version 3.17. </p>
<p> The image to display on the header of installers pages.</p>
<dt><code>CPACK_NSIS_MANIFEST_DPI_AWARE</code></p>
<dd>New in version 3.18. </p>
<p> If set, declares that the installer is DPI-aware.</p>
<dt><code>CPACK_NSIS_BRANDING_TEXT</code></p>
<dd>New in version 3.20. </p>
<p> If set, updates the text at the bottom of the install window. To set the string to blank, use a space (&quot; &quot;).</p>
<dt><code>CPACK_NSIS_BRANDING_TEXT_TRIM_POSITION</code></p>
<dd>New in version 3.20. </p>
<p> If set, trim down the size of the control to the size of the branding text string. Allowed values for this variable are <code>LEFT</code>, <code>CENTER</code> or <code>RIGHT</code>. If not specified, the default behavior is <code>LEFT</code>.</p>
<dt><code>CPACK_NSIS_EXECUTABLE</code></p>
<dd>New in version 3.21. </p>
<p> If set, specify the name of the NSIS executable. Default is <code>makensis</code>.</p>
<dt><code>CPACK_NSIS_IGNORE_LICENSE_PAGE</code></p>
<dd>New in version 3.22. </p>
<p> If set, do not display the page containing the license during installation.</dl>
<h3>CPack NuGet Generator</h3>
<p>New in version 3.12. </p>
<p> When build a NuGet package there is no direct way to control an output filename due a lack of the corresponding CLI option of NuGet, so there is no <code>CPACK_NUGET_PACKAGE_FILE_NAME</code> variable. To form the output filename NuGet uses the package name and the version according to its built-in rules. </p>
<p> Also, be aware that including a top level directory (<code>CPACK_INCLUDE_TOPLEVEL_DIRECTORY</code>) is ignored by this generator.</p>
<h3>Variables specific to CPack NuGet generator</h3>
<p>The CPack NuGet generator may be used to create NuGet packages using <code>CPack</code>. The CPack NuGet generator is a <code>CPack</code> generator thus it uses the <code>CPACK_XXX</code> variables used by <code>CPack</code>. </p>
<p> The CPack NuGet generator has specific features which are controlled by the specifics <code>CPACK_NUGET_XXX</code> variables. In the &quot;one per group&quot; mode (see <code>CPACK_COMPONENTS_GROUPING</code>), <code>&lt;compName&gt;</code> placeholder in the variables below would contain a group name (uppercased and turned into a &quot;C&quot; identifier). </p>
<p> List of CPack NuGet generator specific variables:</p>
<dl>
<dt><code>CPACK_NUGET_COMPONENT_INSTALL</code></p>
<dd>Enable component packaging for CPack NuGet generator</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : OFF</p>
<dt><code>CPACK_NUGET_PACKAGE_NAME</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_NAME</code></p>
<dd>The NUGET package name. <code>CPACK_NUGET_PACKAGE_NAME</code> is used as the package <code>id</code> on <i>nuget.org</i></p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_PACKAGE_NAME</code></p>
<dt><code>CPACK_NUGET_PACKAGE_VERSION</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_VERSION</code></p>
<dd>The NuGet package version.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_PACKAGE_VERSION</code></p>
<dt><code>CPACK_NUGET_PACKAGE_DESCRIPTION</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_DESCRIPTION</code></p>
<dd>A long description of the package for UI display.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>
<dt><code>Default :</code></p>
<dd>
<dt>&bull;</p>
<dd><code>CPACK_COMPONENT_&lt;compName&gt;_DESCRIPTION</code>,</p>
<dt>&bull;</p>
<dd><code>CPACK_COMPONENT_GROUP_&lt;groupName&gt;_DESCRIPTION</code>,</p>
<dt>&bull;</p>
<dd><code>CPACK_PACKAGE_DESCRIPTION</code></p>
<dt><code>CPACK_NUGET_PACKAGE_AUTHORS</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_AUTHORS</code></p>
<dd>A comma-separated list of packages authors, matching the profile names on <i>nuget.org</i>. These are displayed in the NuGet Gallery on <i>nuget.org</i> and are used to cross-reference packages by the same authors.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_PACKAGE_VENDOR</code></p>
<dt><code>CPACK_NUGET_PACKAGE_TITLE</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_TITLE</code></p>
<dd>A human-friendly title of the package, typically used in UI displays as on <i>nuget.org</i> and the Package Manager in Visual Studio. If not specified, the package ID is used.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>
<dt><code>Default :</code></p>
<dd>
<dt>&bull;</p>
<dd><code>CPACK_COMPONENT_&lt;compName&gt;_DISPLAY_NAME</code>,</p>
<dt>&bull;</p>
<dd><code>CPACK_COMPONENT_GROUP_&lt;groupName&gt;_DISPLAY_NAME</code></p>
<dt><code>CPACK_NUGET_PACKAGE_OWNERS</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_OWNERS</code></p>
<dd>A comma-separated list of the package creators using profile names on <i>nuget.org</i>. This is often the same list as in authors, and is ignored when uploading the package to <i>nuget.org</i>.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_NUGET_PACKAGE_HOMEPAGE_URL</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_HOMEPAGE_URL</code></p>
<dd>An URL for the package&#8217;s home page, often shown in UI displays as well as <i>nuget.org</i>.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_PACKAGE_HOMEPAGE_URL</code></p>
<dt><code>CPACK_NUGET_PACKAGE_LICENSEURL</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_LICENSEURL</code></p>
<dd>Deprecated since version 3.20: Use a local license file (<i>CPACK_NUGET_PACKAGE_LICENSE_FILE_NAME</i>) or a <i>(SPDX) license identifier</i> (<i>CPACK_NUGET_PACKAGE_LICENSE_EXPRESSION</i>) instead. </p>
<p> An URL for the package&#8217;s license, often shown in UI displays as well as on <i>nuget.org</i>.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_NUGET_PACKAGE_LICENSE_EXPRESSION</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_LICENSE_EXPRESSION</code></p>
<dd>New in version 3.20. </p>
<p> A Software Package Data Exchange <i>(SPDX) license identifier</i> such as <code>MIT</code>, <code>BSD-3-Clause</code>, or <code>LGPL-3.0-or-later</code>. In the case of a choice of licenses or more complex restrictions, compound license expressions may be formed using boolean operators, for example <code>MIT OR BSD-3-Clause</code>. See the <i>SPDX specification</i> for guidance on forming complex license expressions. </p>
<p> If <code>CPACK_NUGET_PACKAGE_LICENSE_FILE_NAME</code> is specified, <code>CPACK_NUGET_PACKAGE_LICENSE_EXPRESSION</code> is ignored.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_NUGET_PACKAGE_LICENSE_FILE_NAME</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_LICENSE_FILE_NAME</code></p>
<dd>The package&#8217;s license file in <code>.txt</code> or <code>.md</code> format. </p>
<p> If <code>CPACK_NUGET_PACKAGE_LICENSE_FILE_NAME</code> is specified, <code>CPACK_NUGET_PACKAGE_LICENSE_EXPRESSION</code> is ignored. </p>
<p> New in version 3.20. </p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_NUGET_PACKAGE_ICONURL</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_ICONURL</code></p>
<dd>Deprecated since version 3.20: Use a local icon file (<i>CPACK_NUGET_PACKAGE_ICON</i>) instead. </p>
<p> An URL for a 64&#215;64 image with transparency background to use as the icon for the package in UI display.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_NUGET_PACKAGE_ICON</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_ICON</code></p>
<dd>New in version 3.20. </p>
<p> The filename of a 64&#215;64 image with transparency background to use as the icon for the package in UI display.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_NUGET_PACKAGE_DESCRIPTION_SUMMARY</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_DESCRIPTION_SUMMARY</code></p>
<dd>A short description of the package for UI display. If omitted, a truncated version of description is used.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_PACKAGE_DESCRIPTION_SUMMARY</code></p>
<dt><code>CPACK_NUGET_PACKAGE_RELEASE_NOTES</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_RELEASE_NOTES</code></p>
<dd>A description of the changes made in this release of the package, often used in UI like the Updates tab of the Visual Studio Package Manager in place of the package description.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_NUGET_PACKAGE_COPYRIGHT</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_COPYRIGHT</code></p>
<dd>Copyright details for the package.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_NUGET_PACKAGE_LANGUAGE</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_LANGUAGE</code></p>
<dd>New in version 3.20. </p>
<p> Locale specifier for the package, for example <code>en_CA</code>.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_NUGET_PACKAGE_TAGS</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_TAGS</code></p>
<dd>A space-delimited list of tags and keywords that describe the package and aid discoverability of packages through search and filtering.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_NUGET_PACKAGE_DEPENDENCIES</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_DEPENDENCIES</code></p>
<dd>A list of package dependencies.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_NUGET_PACKAGE_DEPENDENCIES_&lt;dependency&gt;_VERSION</code></p>
<dd>
<dt><code>CPACK_NUGET_&lt;compName&gt;_PACKAGE_DEPENDENCIES_&lt;dependency&gt;_VERSION</code></p>
<dd>A <i>version specification</i> for the particular dependency, where <code>&lt;dependency&gt;</code> is an item of the dependency list (see above) transformed with <code>MAKE_C_IDENTIFIER</code> function of <code>string()</code> command.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_NUGET_PACKAGE_DEBUG</code></p>
<dd>Enable debug messages while executing CPack NuGet generator.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : OFF</dl>
<h3>CPack PackageMaker Generator</h3>
<p>PackageMaker CPack generator (macOS). </p>
<p> Deprecated since version 3.17: Xcode no longer distributes the PackageMaker tools. This CPack generator will be removed in a future version of CPack.</p>
<h3>Variables specific to CPack PackageMaker generator</h3>
<p>The following variable is specific to installers built on Mac macOS using PackageMaker:</p>
<dl>
<dt><code>CPACK_OSX_PACKAGE_VERSION</code></p>
<dd>The version of macOS that the resulting PackageMaker archive should be compatible with. Different versions of macOS support different features. For example, CPack can only build component-based installers for macOS 10.4 or newer, and can only build installers that download components on-the-fly for macOS 10.5 or newer. If left blank, this value will be set to the minimum version of macOS that supports the requested features. Set this variable to some value (e.g., 10.4) only if you want to guarantee that your installer will work on that version of macOS, and don&#8217;t mind missing extra features available in the installer shipping with later versions of macOS.</dl>
<h3>Background Image</h3>
<p>New in version 3.17. </p>
<p> This group of variables controls the background image of the generated installer.</p>
<dl>
<dt><code>CPACK_PACKAGEMAKER_BACKGROUND</code></p>
<dd>Adds a background to Distribution XML if specified. The value contains the path to image in <code>Resources</code> directory.</p>
<dt><code>CPACK_PACKAGEMAKER_BACKGROUND_ALIGNMENT</code></p>
<dd>Adds an <code>alignment</code> attribute to the background in Distribution XML. Refer to Apple documentation for valid values.</p>
<dt><code>CPACK_PACKAGEMAKER_BACKGROUND_SCALING</code></p>
<dd>Adds a <code>scaling</code> attribute to the background in Distribution XML. Refer to Apple documentation for valid values.</p>
<dt><code>CPACK_PACKAGEMAKER_BACKGROUND_MIME_TYPE</code></p>
<dd>Adds a <code>mime-type</code> attribute to the background in Distribution XML. The option contains MIME type of an image.</p>
<dt><code>CPACK_PACKAGEMAKER_BACKGROUND_UTI</code></p>
<dd>Adds an <code>uti</code> attribute to the background in Distribution XML. The option contains UTI type of an image.</p>
<dt><code>CPACK_PACKAGEMAKER_BACKGROUND_DARKAQUA</code></p>
<dd>Adds a background for the Dark Aqua theme to Distribution XML if specified. The value contains the path to image in <code>Resources</code> directory.</p>
<dt><code>CPACK_PACKAGEMAKER_BACKGROUND_DARKAQUA_ALIGNMENT</code></p>
<dd>Does the same as <i>CPACK_PACKAGEMAKER_BACKGROUND_ALIGNMENT</i> option, but for the dark theme.</p>
<dt><code>CPACK_PACKAGEMAKER_BACKGROUND_DARKAQUA_SCALING</code></p>
<dd>Does the same as <i>CPACK_PACKAGEMAKER_BACKGROUND_SCALING</i> option, but for the dark theme.</p>
<dt><code>CPACK_PACKAGEMAKER_BACKGROUND_DARKAQUA_MIME_TYPE</code></p>
<dd>Does the same as <i>CPACK_PACKAGEMAKER_BACKGROUND_MIME_TYPE</i> option, but for the dark theme.</p>
<dt><code>CPACK_PACKAGEMAKER_BACKGROUND_DARKAQUA_UTI</code></p>
<dd>Does the same as <i>CPACK_PACKAGEMAKER_BACKGROUND_UTI</i> option, but for the dark theme.</dl>
<h3>CPack productbuild Generator</h3>
<p>New in version 3.7. </p>
<p> productbuild CPack generator (macOS).</p>
<h3>Variables specific to CPack productbuild generator</h3>
<p>The following variable is specific to installers built on Mac macOS using ProductBuild:</p>
<dl>
<dt><code>CPACK_COMMAND_PRODUCTBUILD</code></p>
<dd>Path to the <code><a href="/docs/linux/man/1-productbuild/">productbuild</a>(1)</code> command used to generate a product archive for the macOS Installer or Mac App Store. This variable can be used to override the automatically detected command (or specify its location if the auto-detection fails to find it).</p>
<dt><code>CPACK_PRODUCTBUILD_IDENTITY_NAME</code></p>
<dd>New in version 3.8. </p>
<p> Adds a digital signature to the resulting package.</p>
<dt><code>CPACK_PRODUCTBUILD_KEYCHAIN_PATH</code></p>
<dd>New in version 3.8. </p>
<p> Specify a specific keychain to search for the signing identity.</p>
<dt><code>CPACK_COMMAND_PKGBUILD</code></p>
<dd>Path to the <code><a href="/docs/linux/man/1-pkgbuild/">pkgbuild</a>(1)</code> command used to generate an macOS component package on macOS. This variable can be used to override the automatically detected command (or specify its location if the auto-detection fails to find it).</p>
<dt><code>CPACK_PKGBUILD_IDENTITY_NAME</code></p>
<dd>New in version 3.8. </p>
<p> Adds a digital signature to the resulting package.</p>
<dt><code>CPACK_PKGBUILD_KEYCHAIN_PATH</code></p>
<dd>New in version 3.8. </p>
<p> Specify a specific keychain to search for the signing identity.</p>
<dt><code>CPACK_PREFLIGHT_&lt;COMP&gt;_SCRIPT</code></p>
<dd>Full path to a file that will be used as the <code>preinstall</code> script for the named <code>&lt;COMP&gt;</code> component&#8217;s package, where <code>&lt;COMP&gt;</code> is the uppercased component name. No <code>preinstall</code> script is added if this variable is not defined for a given component.</p>
<dt><code>CPACK_POSTFLIGHT_&lt;COMP&gt;_SCRIPT</code></p>
<dd>Full path to a file that will be used as the <code>postinstall</code> script for the named <code>&lt;COMP&gt;</code> component&#8217;s package, where <code>&lt;COMP&gt;</code> is the uppercased component name. No <code>postinstall</code> script is added if this variable is not defined for a given component.</p>
<dt><code>CPACK_PRODUCTBUILD_RESOURCES_DIR</code></p>
<dd>New in version 3.9. </p>
<p> If specified the productbuild generator copies files from this directory (including subdirectories) to the <code>Resources</code> directory. This is done before the <code>CPACK_RESOURCE_FILE_WELCOME</code>, <code>CPACK_RESOURCE_FILE_README</code>, and <code>CPACK_RESOURCE_FILE_LICENSE</code> files are copied.</dl>
<h3>Background Image</h3>
<p>New in version 3.17. </p>
<p> This group of variables controls the background image of the generated installer.</p>
<dl>
<dt><code>CPACK_PRODUCTBUILD_BACKGROUND</code></p>
<dd>Adds a background to Distribution XML if specified. The value contains the path to image in <code>Resources</code> directory.</p>
<dt><code>CPACK_PRODUCTBUILD_BACKGROUND_ALIGNMENT</code></p>
<dd>Adds an <code>alignment</code> attribute to the background in Distribution XML. Refer to Apple documentation for valid values.</p>
<dt><code>CPACK_PRODUCTBUILD_BACKGROUND_SCALING</code></p>
<dd>Adds a <code>scaling</code> attribute to the background in Distribution XML. Refer to Apple documentation for valid values.</p>
<dt><code>CPACK_PRODUCTBUILD_BACKGROUND_MIME_TYPE</code></p>
<dd>Adds a <code>mime-type</code> attribute to the background in Distribution XML. The option contains MIME type of an image.</p>
<dt><code>CPACK_PRODUCTBUILD_BACKGROUND_UTI</code></p>
<dd>Adds an <code>uti</code> attribute to the background in Distribution XML. The option contains UTI type of an image.</p>
<dt><code>CPACK_PRODUCTBUILD_BACKGROUND_DARKAQUA</code></p>
<dd>Adds a background for the Dark Aqua theme to Distribution XML if specified. The value contains the path to image in <code>Resources</code> directory.</p>
<dt><code>CPACK_PRODUCTBUILD_BACKGROUND_DARKAQUA_ALIGNMENT</code></p>
<dd>Does the same as <i>CPACK_PRODUCTBUILD_BACKGROUND_ALIGNMENT</i> option, but for the dark theme.</p>
<dt><code>CPACK_PRODUCTBUILD_BACKGROUND_DARKAQUA_SCALING</code></p>
<dd>Does the same as <i>CPACK_PRODUCTBUILD_BACKGROUND_SCALING</i> option, but for the dark theme.</p>
<dt><code>CPACK_PRODUCTBUILD_BACKGROUND_DARKAQUA_MIME_TYPE</code></p>
<dd>Does the same as <i>CPACK_PRODUCTBUILD_BACKGROUND_MIME_TYPE</i> option, but for the dark theme.</p>
<dt><code>CPACK_PRODUCTBUILD_BACKGROUND_DARKAQUA_UTI</code></p>
<dd>Does the same as <i>CPACK_PRODUCTBUILD_BACKGROUND_UTI</i> option, but for the dark theme.</dl>
<h3>CPack RPM Generator</h3>
<p>The built in (binary) CPack RPM generator (Unix only)</p>
<h3>Variables specific to CPack RPM generator</h3>
<p>The CPack RPM generator may be used to create RPM packages using <code>CPack</code>. The CPack RPM generator is a <code>CPack</code> generator thus it uses the <code>CPACK_XXX</code> variables used by <code>CPack</code>. </p>
<p> The CPack RPM generator has specific features which are controlled by the specifics <code>CPACK_RPM_XXX</code> variables. </p>
<p> <code>CPACK_RPM_&lt;COMPONENT&gt;_XXXX</code> variables may be used in order to have <code>component</code> specific values. Note however that <code>&lt;COMPONENT&gt;</code> refers to the <code>grouping name</code> written in upper case. It may be either a component name or a component GROUP name. Usually those variables correspond to RPM spec file entities. One may find information about spec files here <i><a rel="nofollow" href="http://www.rpm.org/wiki/Docs">http://www.rpm.org/wiki/Docs</a></i> </p>
<p> Changed in version 3.6: <i>&lt;COMPONENT&gt;</i> part of variables is preferred to be in upper case (e.g. if component is named <code>foo</code> then use <code>CPACK_RPM_FOO_XXXX</code> variable name format) as is with other <code>CPACK_&lt;COMPONENT&gt;_XXXX</code> variables. For the purposes of back compatibility (CMake/CPack version 3.5 and lower) support for same cased component (e.g. <code>fOo</code> would be used as <code>CPACK_RPM_fOo_XXXX</code>) is still supported for variables defined in older versions of CMake/CPack but is not guaranteed for variables that will be added in the future. For the sake of back compatibility same cased component variables also override upper cased versions where both are present. </p>
<p> Here are some CPack RPM generator wiki resources that are here for historic reasons and are no longer maintained but may still prove useful:</p>
<dl>
<dt>&bull;</p>
<dd><i><a rel="nofollow" href="https://gitlab.kitware.com/cmake/community/-/wikis/doc/cpack/Configuration">https://gitlab.kitware.com/cmake/community/-/wikis/doc/cpack/Configuration</a></i></p>
<dt>&bull;</p>
<dd><i><a rel="nofollow" href="https://gitlab.kitware.com/cmake/community/-/wikis/doc/cpack/PackageGenerators#rpm-unix-only">https://gitlab.kitware.com/cmake/community/-/wikis/doc/cpack/PackageGenerators#rpm-unix-only</a></i> </p>
<p> List of CPack RPM generator specific variables:</p>
<dt><code>CPACK_RPM_COMPONENT_INSTALL</code></p>
<dd>Enable component packaging for CPack RPM generator</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : OFF </p>
<p> If enabled (<code>ON</code>) multiple packages are generated. By default a single package containing files of all components is generated.</p>
<dt><code>CPACK_RPM_PACKAGE_SUMMARY</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_SUMMARY</code></p>
<dd>The RPM package summary.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_PACKAGE_DESCRIPTION_SUMMARY</code> </p>
<p> New in version 3.2: Per-component <code>CPACK_RPM_&lt;component&gt;_PACKAGE_SUMMARY</code> variables. </p>
<dt><code>CPACK_RPM_PACKAGE_NAME</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_NAME</code></p>
<dd>The RPM package name.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_PACKAGE_NAME</code> </p>
<p> New in version 3.5: Per-component <code>CPACK_RPM_&lt;component&gt;_PACKAGE_NAME</code> variables. </p>
<dt><code>CPACK_RPM_FILE_NAME</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_FILE_NAME</code></p>
<dd>New in version 3.6. </p>
<p> Package file name.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>
<dt><code>Default</code></p>
<dd><code>&lt;CPACK_PACKAGE_FILE_NAME&gt;[-&lt;component&gt;].rpm</code> with spaces replaced by &#8216;-&#8216; </p>
<p> This may be set to <code>RPM-DEFAULT</code> to allow <code>rpmbuild</code> tool to generate package file name by itself. Alternatively provided package file name must end with <code>.rpm</code> suffix. </p>
<p> <code>NOTE:</code> By using user provided spec file, rpm macro extensions such as for generating <code>debuginfo</code> packages or by simply using multiple components more than one rpm file may be generated, either from a single spec file or from multiple spec files (each component execution produces its own spec file). In such cases duplicate file names may occur as a result of this variable setting or spec file content structure. Duplicate files get overwritten and it is up to the packager to set the variables in a manner that will prevent such errors.</p>
<dt><code>CPACK_RPM_MAIN_COMPONENT</code></p>
<dd>New in version 3.8. </p>
<p> Main component that is packaged without component suffix.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> This variable can be set to any component or group name so that component or group rpm package is generated without component suffix in filename and package name.</p>
<dt><code>CPACK_RPM_PACKAGE_EPOCH</code></p>
<dd>New in version 3.10. </p>
<p> The RPM package epoch</p>
<dt>&bull;</p>
<dd>Mandatory : No</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> Optional number that should be incremented when changing versioning schemas or fixing mistakes in the version numbers of older packages.</p>
<dt><code>CPACK_RPM_PACKAGE_VERSION</code></p>
<dd>The RPM package version.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_PACKAGE_VERSION</code></p>
<dt><code>CPACK_RPM_PACKAGE_ARCHITECTURE</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_ARCHITECTURE</code></p>
<dd>The RPM package architecture.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : Native architecture output by <code>uname -m</code> </p>
<p> This may be set to <code>noarch</code> if you know you are building a <code>noarch</code> package. </p>
<p> New in version 3.3: Per-component <code>CPACK_RPM_&lt;component&gt;_PACKAGE_ARCHITECTURE</code> variables. </p>
<dt><code>CPACK_RPM_PACKAGE_RELEASE</code></p>
<dd>The RPM package release.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : 1 </p>
<p> This is the numbering of the RPM package itself, i.e. the version of the packaging and not the version of the content (see <i>CPACK_RPM_PACKAGE_VERSION</i>). One may change the default value if the previous packaging was buggy and/or you want to put here a fancy Linux distro specific numbering. </p>
<p> <code>NOTE:</code> This is the string that goes into the RPM <code>Release:</code> field. Some distros (e.g. Fedora, CentOS) require <code>1%{?dist}</code> format and not just a number. <code>%{?dist}</code> part can be added by setting <i>CPACK_RPM_PACKAGE_RELEASE_DIST</i>.</p>
<dt><code>CPACK_RPM_PACKAGE_RELEASE_DIST</code></p>
<dd>New in version 3.6. </p>
<p> The dist tag that is added RPM <code>Release:</code> field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : OFF </p>
<p> This is the reported <code>%{dist}</code> tag from the current distribution or empty <code>%{dist}</code> if RPM macro is not set. If this variable is set then RPM <code>Release:</code> field value is set to <code>${CPACK_RPM_PACKAGE_RELEASE}%{?dist}</code>.</p>
<dt><code>CPACK_RPM_PACKAGE_LICENSE</code></p>
<dd>The RPM package license policy.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : &quot;unknown&quot;</p>
<dt><code>CPACK_RPM_PACKAGE_GROUP</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_GROUP</code></p>
<dd>The RPM package group.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : &quot;unknown&quot; </p>
<p> New in version 3.5: Per-component <code>CPACK_RPM_&lt;component&gt;_PACKAGE_GROUP</code> variables. </p>
<dt><code>CPACK_RPM_PACKAGE_VENDOR</code></p>
<dd>The RPM package vendor.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : CPACK_PACKAGE_VENDOR if set or &quot;unknown&quot;</p>
<dt><code>CPACK_RPM_PACKAGE_URL</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_URL</code></p>
<dd>The projects URL.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : <code>CMAKE_PROJECT_HOMEPAGE_URL</code> </p>
<p> New in version 3.12: The <code>CMAKE_PROJECT_HOMEPAGE_URL</code> variable. </p>
<dt><code>CPACK_RPM_PACKAGE_DESCRIPTION</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_DESCRIPTION</code></p>
<dd>RPM package description.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : <code>CPACK_COMPONENT_&lt;compName&gt;_DESCRIPTION</code> (component based installers only) if set, <code>CPACK_PACKAGE_DESCRIPTION_FILE</code> if set or &quot;no package description available&quot; </p>
<p> New in version 3.2: Per-component <code>CPACK_RPM_&lt;component&gt;_PACKAGE_DESCRIPTION</code> variables. </p>
<dt><code>CPACK_RPM_COMPRESSION_TYPE</code></p>
<dd>RPM compression type.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to override RPM compression type to be used to build the RPM. For example some Linux distribution now default to <code>lzma</code> or <code>xz</code> compression whereas older cannot use such RPM. Using this one can enforce compression type to be used. </p>
<p> Possible values are:</p>
<dt>&bull;</p>
<dd>lzma</p>
<dt>&bull;</p>
<dd>xz</p>
<dt>&bull;</p>
<dd>bzip2</p>
<dt>&bull;</p>
<dd>gzip</p>
<dt><code>CPACK_RPM_PACKAGE_AUTOREQ</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_AUTOREQ</code></p>
<dd>RPM spec autoreq field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to enable (<code>1</code>, <code>yes</code>) or disable (<code>0</code>, <code>no</code>) automatic shared libraries dependency detection. Dependencies are added to requires list. </p>
<p> <code>NOTE:</code> By default automatic dependency detection is enabled by rpm generator.</p>
<dt><code>CPACK_RPM_PACKAGE_AUTOPROV</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_AUTOPROV</code></p>
<dd>RPM spec autoprov field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to enable (<code>1</code>, <code>yes</code>) or disable (<code>0</code>, <code>no</code>) automatic listing of shared libraries that are provided by the package. Shared libraries are added to provides list. </p>
<p> <code>NOTE:</code> By default automatic provides detection is enabled by rpm generator.</p>
<dt><code>CPACK_RPM_PACKAGE_AUTOREQPROV</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_AUTOREQPROV</code></p>
<dd>RPM spec autoreqprov field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> Variable enables/disables autoreq and autoprov at the same time. See <i>CPACK_RPM_PACKAGE_AUTOREQ</i> and <i>CPACK_RPM_PACKAGE_AUTOPROV</i> for more details. </p>
<p> <code>NOTE:</code> By default automatic detection feature is enabled by rpm.</p>
<dt><code>CPACK_RPM_PACKAGE_REQUIRES</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_REQUIRES</code></p>
<dd>RPM spec requires field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set RPM dependencies (requires). Note that you must enclose the complete requires string between quotes, for example: </p>
<pre>set(CPACK_RPM_PACKAGE_REQUIRES &quot;python &gt;= 2.5.0, cmake &gt;= 2.8&quot;)</pre>
<p>The required package list of an RPM file could be printed with: </p>
<pre>rpm -qp --requires file.rpm</pre>
<dt><code>CPACK_RPM_PACKAGE_CONFLICTS</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_CONFLICTS</code></p>
<dd>RPM spec conflicts field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set negative RPM dependencies (conflicts). Note that you must enclose the complete requires string between quotes, for example: </p>
<pre>set(CPACK_RPM_PACKAGE_CONFLICTS &quot;libxml2&quot;)</pre>
<p>The conflicting package list of an RPM file could be printed with: </p>
<pre>rpm -qp --conflicts file.rpm</pre>
<dt><code>CPACK_RPM_PACKAGE_REQUIRES_PRE</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_REQUIRES_PRE</code></p>
<dd>New in version 3.2. </p>
<p> RPM spec requires(pre) field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set RPM preinstall dependencies (requires(pre)). Note that you must enclose the complete requires string between quotes, for example: </p>
<pre>set(CPACK_RPM_PACKAGE_REQUIRES_PRE &quot;shadow-utils, initscripts&quot;)</pre>
<dt><code>CPACK_RPM_PACKAGE_REQUIRES_POST</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_REQUIRES_POST</code></p>
<dd>New in version 3.2. </p>
<p> RPM spec requires(post) field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set RPM postinstall dependencies (requires(post)). Note that you must enclose the complete requires string between quotes, for example: </p>
<pre>set(CPACK_RPM_PACKAGE_REQUIRES_POST &quot;shadow-utils, initscripts&quot;)</pre>
<dt><code>CPACK_RPM_PACKAGE_REQUIRES_POSTUN</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_REQUIRES_POSTUN</code></p>
<dd>New in version 3.2. </p>
<p> RPM spec requires(postun) field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set RPM postuninstall dependencies (requires(postun)). Note that you must enclose the complete requires string between quotes, for example: </p>
<pre>set(CPACK_RPM_PACKAGE_REQUIRES_POSTUN &quot;shadow-utils, initscripts&quot;)</pre>
<dt><code>CPACK_RPM_PACKAGE_REQUIRES_PREUN</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_REQUIRES_PREUN</code></p>
<dd>New in version 3.2. </p>
<p> RPM spec requires(preun) field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set RPM preuninstall dependencies (requires(preun)). Note that you must enclose the complete requires string between quotes, for example: </p>
<pre>set(CPACK_RPM_PACKAGE_REQUIRES_PREUN &quot;shadow-utils, initscripts&quot;)</pre>
<dt><code>CPACK_RPM_PACKAGE_SUGGESTS</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_SUGGESTS</code></p>
<dd>RPM spec suggest field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set weak RPM dependencies (suggests). If <code>rpmbuild</code> doesn&#8217;t support the <code>Suggests</code> tag, CPack will emit a warning and ignore this variable. Note that you must enclose the complete requires string between quotes.</p>
<dt><code>CPACK_RPM_PACKAGE_PROVIDES</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_PROVIDES</code></p>
<dd>RPM spec provides field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set RPM dependencies (provides). The provided package list of an RPM file could be printed with: </p>
<pre>rpm -qp --provides file.rpm</pre>
<dt><code>CPACK_RPM_PACKAGE_OBSOLETES</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_PACKAGE_OBSOLETES</code></p>
<dd>RPM spec obsoletes field.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set RPM packages that are obsoleted by this one.</p>
<dt><code>CPACK_RPM_PACKAGE_RELOCATABLE</code></p>
<dd>build a relocatable RPM.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : CPACK_PACKAGE_RELOCATABLE </p>
<p> If this variable is set to TRUE or ON, the CPack RPM generator will try to build a relocatable RPM package. A relocatable RPM may be installed using: </p>
<pre>rpm --prefix or --relocate</pre>
<p>in order to install it at an alternate place see <a href="/docs/linux/man/8-rpm/">rpm</a>(8). Note that currently this may fail if <code>CPACK_SET_DESTDIR</code> is set to <code>ON</code>. If <code>CPACK_SET_DESTDIR</code> is set then you will get a warning message but if there is file installed with absolute path you&#8217;ll get unexpected behavior.</p>
<dt><code>CPACK_RPM_SPEC_INSTALL_POST</code></p>
<dd>Deprecated &#8211; use <i>CPACK_RPM_SPEC_MORE_DEFINE</i> instead.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt>&bull;</p>
<dd>Deprecated: YES </p>
<p> May be used to override the <code>__spec_install_post</code> section within the generated spec file. This affects the install step during package creation, not during package installation. For adding operations to be performed during package installation, use <i>CPACK_RPM_POST_INSTALL_SCRIPT_FILE</i> instead.</p>
<dt><code>CPACK_RPM_SPEC_MORE_DEFINE</code></p>
<dd>RPM extended spec definitions lines.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to add any <code>%define</code> lines to the generated spec file. An example of its use is to prevent stripping of executables (but note that this may also disable other default post install processing): </p>
<pre>set(CPACK_RPM_SPEC_MORE_DEFINE &quot;%define __spec_install_post /bin/true&quot;)</pre>
<dt><code>CPACK_RPM_PACKAGE_DEBUG</code></p>
<dd>Toggle CPack RPM generator debug output.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be set when invoking cpack in order to trace debug information during CPack RPM run. For example you may launch CPack like this: </p>
<pre>cpack -D CPACK_RPM_PACKAGE_DEBUG=1 -G RPM</pre>
<dt><code>CPACK_RPM_USER_BINARY_SPECFILE</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;componentName&gt;_USER_BINARY_SPECFILE</code></p>
<dd>A user provided spec file.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be set by the user in order to specify a USER binary spec file to be used by the CPack RPM generator instead of generating the file. The specified file will be processed by configure_file( @ONLY).</p>
<dt><code>CPACK_RPM_GENERATE_USER_BINARY_SPECFILE_TEMPLATE</code></p>
<dd>Spec file template.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> If set CPack will generate a template for USER specified binary spec file and stop with an error. For example launch CPack like this: </p>
<pre>cpack -D CPACK_RPM_GENERATE_USER_BINARY_SPECFILE_TEMPLATE=1 -G RPM</pre>
<p>The user may then use this file in order to hand-craft is own binary spec file which may be used with <i>CPACK_RPM_USER_BINARY_SPECFILE</i>.</p>
<dt><code>CPACK_RPM_PRE_INSTALL_SCRIPT_FILE</code></p>
<dd>
<dt><code>CPACK_RPM_PRE_UNINSTALL_SCRIPT_FILE</code></p>
<dd>
<dt><code>CPACK_RPM_PRE_TRANS_SCRIPT_FILE</code></p>
<dd>Path to file containing pre install/uninstall/transaction script.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to embed a pre installation/uninstallation/transaction script in the spec file. The referred script file (or both) will be read and directly put after the <code>%pre</code> or <code>%preun</code> section If <i>CPACK_RPM_COMPONENT_INSTALL</i> is set to ON the install/uninstall/transaction script for each component can be overridden with <code>CPACK_RPM_&lt;COMPONENT&gt;_PRE_INSTALL_SCRIPT_FILE</code>, <code>CPACK_RPM_&lt;COMPONENT&gt;_PRE_UNINSTALL_SCRIPT_FILE</code>, and <code>CPACK_RPM_&lt;COMPONENT&gt;_PRE_TRANS_SCRIPT_FILE</code> One may verify which scriptlet has been included with: </p>
<pre>rpm -qp --scripts package.rpm</pre>
<p>New in version 3.18: The <code>CPACK_RPM_PRE_TRANS_SCRIPT_FILE</code> variable. </p>
<dt><code>CPACK_RPM_POST_INSTALL_SCRIPT_FILE</code></p>
<dd>
<dt><code>CPACK_RPM_POST_UNINSTALL_SCRIPT_FILE</code></p>
<dd>
<dt><code>CPACK_RPM_POST_TRANS_SCRIPT_FILE</code></p>
<dd>Path to file containing post install/uninstall/transaction script.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to embed a post installation/uninstallation/transaction script in the spec file. The referred script file (or both) will be read and directly put after the <code>%post</code> or <code>%postun</code> section. If <i>CPACK_RPM_COMPONENT_INSTALL</i> is set to ON the install/uninstall/transaction script for each component can be overridden with <code>CPACK_RPM_&lt;COMPONENT&gt;_POST_INSTALL_SCRIPT_FILE</code>, <code>CPACK_RPM_&lt;COMPONENT&gt;_POST_UNINSTALL_SCRIPT_FILE</code>, and <code>CPACK_RPM_&lt;COMPONENT&gt;_POST_TRANS_SCRIPT_FILE</code> One may verify which scriptlet has been included with: </p>
<pre>rpm -qp --scripts package.rpm</pre>
<p>New in version 3.18: The <code>CPACK_RPM_POST_TRANS_SCRIPT_FILE</code> variable. </p>
<dt><code>CPACK_RPM_USER_FILELIST</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;COMPONENT&gt;_USER_FILELIST</code></p>
<dd>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to explicitly specify <code>%(&lt;directive&gt;)</code> file line in the spec file. Like <code>%config(noreplace)</code> or any other directive that be found in the <code>%files</code> section. Since the CPack RPM generator is generating the list of files (and directories) the user specified files of the <code>CPACK_RPM_&lt;COMPONENT&gt;_USER_FILELIST</code> list will be removed from the generated list. If referring to directories do not add a trailing slash. </p>
<p> New in version 3.8: You can have multiple directives per line, as in <code>%attr(600,root,root) %config(noreplace)</code>. </p>
<dt><code>CPACK_RPM_CHANGELOG_FILE</code></p>
<dd>RPM changelog file.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to embed a changelog in the spec file. The referred file will be read and directly put after the <code>%changelog</code> section.</p>
<dt><code>CPACK_RPM_EXCLUDE_FROM_AUTO_FILELIST</code></p>
<dd>list of path to be excluded.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>
<dt><code>Default</code></p>
<dd>/etc /etc/init.d /usr /usr/bin /usr/include /usr/lib /usr/libx32 /usr/lib64 /usr/share /usr/share/aclocal /usr/share/doc </p>
<p> May be used to exclude path (directories or files) from the auto-generated list of paths discovered by CPack RPM. The default value contains a reasonable set of values if the variable is not defined by the user. If the variable is defined by the user then the CPack RPM generator will NOT any of the default path. If you want to add some path to the default list then you can use <i>CPACK_RPM_EXCLUDE_FROM_AUTO_FILELIST_ADDITION</i> variable. </p>
<p> New in version 3.10: Added <code>/usr/share/aclocal</code> to the default list of excludes. </p>
<dt><code>CPACK_RPM_EXCLUDE_FROM_AUTO_FILELIST_ADDITION</code></p>
<dd>additional list of path to be excluded.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to add more exclude path (directories or files) from the initial default list of excluded paths. See <i>CPACK_RPM_EXCLUDE_FROM_AUTO_FILELIST</i>.</p>
<dt><code>CPACK_RPM_RELOCATION_PATHS</code></p>
<dd>New in version 3.2. </p>
<p> Packages relocation paths list.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to specify more than one relocation path per relocatable RPM. Variable contains a list of relocation paths that if relative are prefixed by the value of <i>CPACK_RPM_&lt;COMPONENT&gt;_PACKAGE_PREFIX</i> or by the value of <code>CPACK_PACKAGING_INSTALL_PREFIX</code> if the component version is not provided. Variable is not component based as its content can be used to set a different path prefix for e.g. binary dir and documentation dir at the same time. Only prefixes that are required by a certain component are added to that component &#8211; component must contain at least one file/directory/symbolic link with <i>CPACK_RPM_RELOCATION_PATHS</i> prefix for a certain relocation path to be added. Package will not contain any relocation paths if there are no files/directories/symbolic links on any of the provided prefix locations. Packages that either do not contain any relocation paths or contain files/directories/symbolic links that are outside relocation paths print out an <code>AUTHOR_WARNING</code> that RPM will be partially relocatable.</p>
<dt><code>CPACK_RPM_&lt;COMPONENT&gt;_PACKAGE_PREFIX</code></p>
<dd>New in version 3.2. </p>
<p> Per component relocation path install prefix.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : CPACK_PACKAGING_INSTALL_PREFIX </p>
<p> May be used to set per component <code>CPACK_PACKAGING_INSTALL_PREFIX</code> for relocatable RPM packages.</p>
<dt><code>CPACK_RPM_NO_INSTALL_PREFIX_RELOCATION</code></p>
<dd>
<dt><code>CPACK_RPM_NO_&lt;COMPONENT&gt;_INSTALL_PREFIX_RELOCATION</code></p>
<dd>New in version 3.3. </p>
<p> Removal of default install prefix from relocation paths list.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>
<dt><code>Default</code></p>
<dd>CPACK_PACKAGING_INSTALL_PREFIX or CPACK_RPM_&lt;COMPONENT&gt;_PACKAGE_PREFIX are treated as one of relocation paths </p>
<p> May be used to remove CPACK_PACKAGING_INSTALL_PREFIX and CPACK_RPM_&lt;COMPONENT&gt;_PACKAGE_PREFIX from relocatable RPM prefix paths.</p>
<dt><code>CPACK_RPM_ADDITIONAL_MAN_DIRS</code></p>
<dd>New in version 3.3. </p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set additional man dirs that could potentially be compressed by brp-compress RPM macro. Variable content must be a list of regular expressions that point to directories containing man files or to man files directly. Note that in order to compress man pages a path must also be present in brp-compress RPM script and that brp-compress script must be added to RPM configuration by the operating system. </p>
<p> Regular expressions that are added by default were taken from brp-compress RPM macro:</p>
<dt>&bull;</p>
<dd>/usr/man/man.*</p>
<dt>&bull;</p>
<dd>/usr/man/.*/man.*</p>
<dt>&bull;</p>
<dd>/usr/info.*</p>
<dt>&bull;</p>
<dd>/usr/share/man/man.*</p>
<dt>&bull;</p>
<dd>/usr/share/man/.*/man.*</p>
<dt>&bull;</p>
<dd>/usr/share/info.*</p>
<dt>&bull;</p>
<dd>/usr/kerberos/man.*</p>
<dt>&bull;</p>
<dd>/usr/X11R6/man/man.*</p>
<dt>&bull;</p>
<dd>/usr/lib/perl5/man/man.*</p>
<dt>&bull;</p>
<dd>/usr/share/doc/.*/man/man.*</p>
<dt>&bull;</p>
<dd>/usr/lib/.*/man/man.*</p>
<dt><code>CPACK_RPM_DEFAULT_USER</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;compName&gt;_DEFAULT_USER</code></p>
<dd>New in version 3.6. </p>
<p> default user ownership of RPM content</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : root </p>
<p> Value should be user name and not UID. Note that &lt;compName&gt; must be in upper-case.</p>
<dt><code>CPACK_RPM_DEFAULT_GROUP</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;compName&gt;_DEFAULT_GROUP</code></p>
<dd>New in version 3.6. </p>
<p> default group ownership of RPM content</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : root </p>
<p> Value should be group name and not GID. Note that &lt;compName&gt; must be in upper-case.</p>
<dt><code>CPACK_RPM_DEFAULT_FILE_PERMISSIONS</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;compName&gt;_DEFAULT_FILE_PERMISSIONS</code></p>
<dd>New in version 3.6. </p>
<p> default permissions used for packaged files</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; (system default) </p>
<p> Accepted values are lists with <code>PERMISSIONS</code>. Valid permissions are:</p>
<dt>&bull;</p>
<dd>OWNER_READ</p>
<dt>&bull;</p>
<dd>OWNER_WRITE</p>
<dt>&bull;</p>
<dd>OWNER_EXECUTE</p>
<dt>&bull;</p>
<dd>GROUP_READ</p>
<dt>&bull;</p>
<dd>GROUP_WRITE</p>
<dt>&bull;</p>
<dd>GROUP_EXECUTE</p>
<dt>&bull;</p>
<dd>WORLD_READ</p>
<dt>&bull;</p>
<dd>WORLD_WRITE</p>
<dt>&bull;</p>
<dd>WORLD_EXECUTE </p>
<p> Note that &lt;compName&gt; must be in upper-case.</p>
<dt><code>CPACK_RPM_DEFAULT_DIR_PERMISSIONS</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;compName&gt;_DEFAULT_DIR_PERMISSIONS</code></p>
<dd>New in version 3.6. </p>
<p> default permissions used for packaged directories</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; (system default) </p>
<p> Accepted values are lists with PERMISSIONS. Valid permissions are the same as for <i>CPACK_RPM_DEFAULT_FILE_PERMISSIONS</i>. Note that &lt;compName&gt; must be in upper-case.</p>
<dt><code>CPACK_RPM_INSTALL_WITH_EXEC</code></p>
<dd>New in version 3.11. </p>
<p> force execute permissions on programs and shared libraries</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; (system default) </p>
<p> Force set owner, group and world execute permissions on programs and shared libraries. This can be used for creating valid rpm packages on systems such as Debian where shared libraries do not have execute permissions set. </p>
<p> <code>NOTE:</code> Programs and shared libraries without execute permissions are ignored during separation of debug symbols from the binary for debuginfo packages.</dl>
<h3>Packaging of Symbolic Links</h3>
<p>New in version 3.3. </p>
<p> The CPack RPM generator supports packaging of symbolic links: </p>
<pre>execute_process(COMMAND ${CMAKE_COMMAND}
 -E create_symlink &lt;relative_path_location&gt; &lt;symlink_name&gt;)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/&lt;symlink_name&gt;
 DESTINATION &lt;symlink_location&gt; COMPONENT libraries)</pre>
<p>Symbolic links will be optimized (paths will be shortened if possible) before being added to the package or if multiple relocation paths are detected, a post install symlink relocation script will be generated. </p>
<p> Symbolic links may point to locations that are not packaged by the same package (either a different component or even not packaged at all) but those locations will be treated as if they were a part of the package while determining if symlink should be either created or present in a post install script &#8211; depending on relocation paths. </p>
<p> Changed in version 3.6: Symbolic links that point to locations outside packaging path produce a warning and are treated as non relocatable permanent symbolic links. Previous versions of CMake produced an error in this case. </p>
<p> Currently there are a few limitations though:</p>
<dl>
<dt>&bull;</p>
<dd>For component based packaging component interdependency is not checked when processing symbolic links. Symbolic links pointing to content of a different component are treated the same way as if pointing to location that will not be packaged.</p>
<dt>&bull;</p>
<dd>Symbolic links pointing to a location through one or more intermediate symbolic links will not be handled differently &#8211; if the intermediate symbolic link(s) is also on a relocatable path, relocating it during package installation may cause initial symbolic link to point to an invalid location.</dl>
<h3>Packaging of debug information</h3>
<p>New in version 3.7. </p>
<p> Debuginfo packages contain debug symbols and sources for debugging packaged binaries. </p>
<p> Debuginfo RPM packaging has its own set of variables:</p>
<dl>
<dt><code>CPACK_RPM_DEBUGINFO_PACKAGE</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_DEBUGINFO_PACKAGE</code></p>
<dd>Enable generation of debuginfo RPM package(s).</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : OFF </p>
<p> <code>NOTE:</code> Binaries must contain debug symbols before packaging so use either <code>Debug</code> or <code>RelWithDebInfo</code> for <code>CMAKE_BUILD_TYPE</code> variable value. </p>
<p> Additionally, if <code>CPACK_STRIP_FILES</code> is set, the files will be stripped before they get to the RPM generator, so will not contain debug symbols and a debuginfo package will not get built. Do not use with <code>CPACK_STRIP_FILES</code>. </p>
<p> <code>NOTE:</code> Packages generated from packages without binary files, with binary files but without execute permissions or without debug symbols will cause packaging termination.</p>
<dt><code>CPACK_BUILD_SOURCE_DIRS</code></p>
<dd>Provides locations of root directories of source files from which binaries were built.</p>
<dt>&bull;</p>
<dd>Mandatory : YES if <i>CPACK_RPM_DEBUGINFO_PACKAGE</i> is set</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> <code>NOTE:</code> For CMake project <i>CPACK_BUILD_SOURCE_DIRS</i> is set by default to point to <code>CMAKE_SOURCE_DIR</code> and <code>CMAKE_BINARY_DIR</code> paths. </p>
<p> <code>NOTE:</code> Sources with path prefixes that do not fall under any location provided with <i>CPACK_BUILD_SOURCE_DIRS</i> will not be present in debuginfo package.</p>
<dt><code>CPACK_RPM_BUILD_SOURCE_DIRS_PREFIX</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_BUILD_SOURCE_DIRS_PREFIX</code></p>
<dd>Prefix of location where sources will be placed during package installation.</p>
<dt>&bull;</p>
<dd>Mandatory : YES if <i>CPACK_RPM_DEBUGINFO_PACKAGE</i> is set</p>
<dt>&bull;</p>
<dd>
<dt><code>Default</code></p>
<dd>&quot;/usr/src/debug/&lt;CPACK_PACKAGE_FILE_NAME&gt;&quot; and for component packaging &quot;/usr/src/debug/&lt;CPACK_PACKAGE_FILE_NAME&gt;-&lt;component&gt;&quot; </p>
<p> <code>NOTE:</code> Each source path prefix is additionally suffixed by <code>src_&lt;index&gt;</code> where index is index of the path used from <i>CPACK_BUILD_SOURCE_DIRS</i> variable. This produces <code>&lt;CPACK_RPM_BUILD_SOURCE_DIRS_PREFIX&gt;/src_&lt;index&gt;</code> replacement path. Limitation is that replaced path part must be shorter or of equal length than the length of its replacement. If that is not the case either <i>CPACK_RPM_BUILD_SOURCE_DIRS_PREFIX</i> variable has to be set to a shorter path or source directories must be placed on a longer path.</p>
<dt><code>CPACK_RPM_DEBUGINFO_EXCLUDE_DIRS</code></p>
<dd>Directories containing sources that should be excluded from debuginfo packages.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &quot;/usr /usr/src /usr/src/debug&quot; </p>
<p> Listed paths are owned by other RPM packages and should therefore not be deleted on debuginfo package uninstallation.</p>
<dt><code>CPACK_RPM_DEBUGINFO_EXCLUDE_DIRS_ADDITION</code></p>
<dd>Paths that should be appended to <i>CPACK_RPM_DEBUGINFO_EXCLUDE_DIRS</i> for exclusion.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_RPM_DEBUGINFO_SINGLE_PACKAGE</code></p>
<dd>New in version 3.8. </p>
<p> Create a single debuginfo package even if components packaging is set.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : OFF </p>
<p> When this variable is enabled it produces a single debuginfo package even if component packaging is enabled. </p>
<p> When using this feature in combination with components packaging and there is more than one component this variable requires <i>CPACK_RPM_MAIN_COMPONENT</i> to be set. </p>
<p> <code>NOTE:</code> If none of the <i>CPACK_RPM_&lt;component&gt;_DEBUGINFO_PACKAGE</i> variables is set then <i>CPACK_RPM_DEBUGINFO_PACKAGE</i> is automatically set to <code>ON</code> when <i>CPACK_RPM_DEBUGINFO_SINGLE_PACKAGE</i> is set.</p>
<dt><code>CPACK_RPM_DEBUGINFO_FILE_NAME</code></p>
<dd>
<dt><code>CPACK_RPM_&lt;component&gt;_DEBUGINFO_FILE_NAME</code></p>
<dd>New in version 3.9. </p>
<p> Debuginfo package file name.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : rpmbuild tool generated package file name </p>
<p> Alternatively provided debuginfo package file name must end with <code>.rpm</code> suffix and should differ from file names of other generated packages. </p>
<p> Variable may contain <code>@cpack_component@</code> placeholder which will be replaced by component name if component packaging is enabled otherwise it deletes the placeholder. </p>
<p> Setting the variable to <code>RPM-DEFAULT</code> may be used to explicitly set filename generation to default. </p>
<p> <code>NOTE:</code> <i>CPACK_RPM_FILE_NAME</i> also supports rpmbuild tool generated package file name &#8211; disabled by default but can be enabled by setting the variable to <code>RPM-DEFAULT</code>.</dl>
<h3>Packaging of sources (SRPM)</h3>
<p>New in version 3.7. </p>
<p> SRPM packaging is enabled by setting <i>CPACK_RPM_PACKAGE_SOURCES</i> variable while usually using <code>CPACK_INSTALLED_DIRECTORIES</code> variable to provide directory containing CMakeLists.txt and source files. </p>
<p> For CMake projects SRPM package would be produced by executing: </p>
<pre>cpack -G RPM --config ./CPackSourceConfig.cmake</pre>
<p><code>NOTE:</code> Produced SRPM package is expected to be built with <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> executable and packaged with <code><a href="/docs/linux/man/1-cpack/">cpack</a>(1)</code> executable so CMakeLists.txt has to be located in root source directory and must be able to generate binary rpm packages by executing <code>cpack -G</code> command. The two executables as well as rpmbuild must also be present when generating binary rpm packages from the produced SRPM package. </p>
<p> Once the SRPM package is generated it can be used to generate binary packages by creating a directory structure for rpm generation and executing rpmbuild tool: </p>
<pre>mkdir -p build_dir/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
rpmbuild --define &quot;_topdir &lt;path_to_build_dir&gt;&quot; --rebuild &lt;SRPM_file_name&gt;</pre>
<p>Generated packages will be located in build_dir/RPMS directory or its sub directories. </p>
<p> <code>NOTE:</code> SRPM package internally uses CPack/RPM generator to generate binary packages so CMakeScripts.txt can decide during the SRPM to binary rpm generation step what content the package(s) should have as well as how they should be packaged (monolithic or components). CMake can decide this for e.g. by reading environment variables set by the package manager before starting the process of generating binary rpm packages. This way a single SRPM package can be used to produce different binary rpm packages on different platforms depending on the platform&#8217;s packaging rules. </p>
<p> Source RPM packaging has its own set of variables:</p>
<dl>
<dt><code>CPACK_RPM_PACKAGE_SOURCES</code></p>
<dd>Should the content be packaged as a source rpm (default is binary rpm).</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : OFF </p>
<p> <code>NOTE:</code> For cmake projects <i>CPACK_RPM_PACKAGE_SOURCES</i> variable is set to <code>OFF</code> in CPackConfig.cmake and <code>ON</code> in CPackSourceConfig.cmake generated files.</p>
<dt><code>CPACK_RPM_SOURCE_PKG_BUILD_PARAMS</code></p>
<dd>Additional command-line parameters provided to <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> executable.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211;</p>
<dt><code>CPACK_RPM_SOURCE_PKG_PACKAGING_INSTALL_PREFIX</code></p>
<dd>Packaging install prefix that would be provided in <code>CPACK_PACKAGING_INSTALL_PREFIX</code> variable for producing binary RPM packages.</p>
<dt>&bull;</p>
<dd>Mandatory : YES</p>
<dt>&bull;</p>
<dd>Default : &quot;/&quot;</p>
<dt><code>CPACK_RPM_BUILDREQUIRES</code></p>
<dd>List of source rpm build dependencies.</p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to set source RPM build dependencies (BuildRequires). Note that you must enclose the complete build requirements string between quotes, for example: </p>
<pre>set(CPACK_RPM_BUILDREQUIRES &quot;python &gt;= 2.5.0, cmake &gt;= 2.8&quot;)</pre>
<dt><code>CPACK_RPM_REQUIRES_EXCLUDE_FROM</code></p>
<dd>New in version 3.22. </p>
<dt>&bull;</p>
<dd>Mandatory : NO</p>
<dt>&bull;</p>
<dd>Default : &#8211; </p>
<p> May be used to keep the dependency generator from scanning specific files or directories for dependencies. Note that you can use a regular expression that matches all of the directories or files, for example: </p>
<pre>set(CPACK_RPM_REQUIRES_EXCLUDE_FROM &quot;bin/libqsqloci.*\.so.*&quot;)</pre>
</dl>
<h3>CPack WIX Generator</h3>
<p>CPack WIX generator specific options </p>
<p> New in version 3.7: Support <code>CPACK_COMPONENT_&lt;compName&gt;_DISABLED</code> variable.</p>
<h3>Variables specific to CPack WIX generator</h3>
<p>The following variables are specific to the installers built on Windows using WiX.</p>
<dl>
<dt><code>CPACK_WIX_UPGRADE_GUID</code></p>
<dd>Upgrade GUID (<code>Product/@UpgradeCode</code>) </p>
<p> Will be automatically generated unless explicitly provided. </p>
<p> It should be explicitly set to a constant generated globally unique identifier (GUID) to allow your installers to replace existing installations that use the same GUID. </p>
<p> You may for example explicitly set this variable in your CMakeLists.txt to the value that has been generated per default. You should not use GUIDs that you did not generate yourself or which may belong to other projects. </p>
<p> A GUID shall have the following fixed length syntax: </p>
<pre>XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX</pre>
<p>(each X represents an uppercase hexadecimal digit)</p>
<dt><code>CPACK_WIX_PRODUCT_GUID</code></p>
<dd>Product GUID (<code>Product/@Id</code>) </p>
<p> Will be automatically generated unless explicitly provided. </p>
<p> If explicitly provided this will set the Product Id of your installer. </p>
<p> The installer will abort if it detects a pre-existing installation that uses the same GUID. </p>
<p> The GUID shall use the syntax described for CPACK_WIX_UPGRADE_GUID.</p>
<dt><code>CPACK_WIX_LICENSE_RTF</code></p>
<dd>RTF License File </p>
<p> If CPACK_RESOURCE_FILE_LICENSE has an .rtf extension it is used as-is. </p>
<p> If CPACK_RESOURCE_FILE_LICENSE has an .txt extension it is implicitly converted to RTF by the WIX Generator. The expected encoding of the .txt file is UTF-8. </p>
<p> With CPACK_WIX_LICENSE_RTF you can override the license file used by the WIX Generator in case CPACK_RESOURCE_FILE_LICENSE is in an unsupported format or the .txt -&gt; .rtf conversion does not work as expected.</p>
<dt><code>CPACK_WIX_PRODUCT_ICON</code></p>
<dd>The Icon shown next to the program name in Add/Remove programs. </p>
<p> If set, this icon is used in place of the default icon.</p>
<dt><code>CPACK_WIX_UI_REF</code></p>
<dd>This variable allows you to override the Id of the <code>&lt;UIRef&gt;</code> element in the WiX template. </p>
<p> The default is <code>WixUI_InstallDir</code> in case no CPack components have been defined and <code>WixUI_FeatureTree</code> otherwise.</p>
<dt><code>CPACK_WIX_UI_BANNER</code></p>
<dd>The bitmap will appear at the top of all installer pages other than the welcome and completion dialogs. </p>
<p> If set, this image will replace the default banner image. </p>
<p> This image must be 493 by 58 pixels.</p>
<dt><code>CPACK_WIX_UI_DIALOG</code></p>
<dd>Background bitmap used on the welcome and completion dialogs. </p>
<p> If this variable is set, the installer will replace the default dialog image. </p>
<p> This image must be 493 by 312 pixels.</p>
<dt><code>CPACK_WIX_PROGRAM_MENU_FOLDER</code></p>
<dd>Start menu folder name for launcher. </p>
<p> If this variable is not set, it will be initialized with CPACK_PACKAGE_NAME </p>
<p> New in version 3.16: If this variable is set to <code>.</code>, then application shortcuts will be created directly in the start menu and the uninstaller shortcut will be omitted. </p>
<dt><code>CPACK_WIX_CULTURES</code></p>
<dd>Language(s) of the installer </p>
<p> Languages are compiled into the WixUI extension library. To use them, simply provide the name of the culture. If you specify more than one culture identifier in a comma or semicolon delimited list, the first one that is found will be used. You can find a list of supported languages at: <i><a rel="nofollow" href="http://wix.sourceforge.net/manual-wix3/WixUI_localization.htm">http://wix.sourceforge.net/manual-wix3/WixUI_localization.htm</a></i></p>
<dt><code>CPACK_WIX_TEMPLATE</code></p>
<dd>Template file for WiX generation </p>
<p> If this variable is set, the specified template will be used to generate the WiX wxs file. This should be used if further customization of the output is required. </p>
<p> If this variable is not set, the default MSI template included with CMake will be used.</p>
<dt><code>CPACK_WIX_PATCH_FILE</code></p>
<dd>Optional list of XML files with fragments to be inserted into generated WiX sources. </p>
<p> New in version 3.5: Support listing multiple patch files. </p>
<p> This optional variable can be used to specify an XML file that the WIX generator will use to inject fragments into its generated source files. </p>
<p> Patch files understood by the CPack WIX generator roughly follow this RELAX NG compact schema: </p>
<pre>start = CPackWiXPatch
CPackWiXPatch = element CPackWiXPatch { CPackWiXFragment* }
CPackWiXFragment = element CPackWiXFragment
{
 attribute Id { string },
 fragmentContent*
}
fragmentContent = element * - CPackWiXFragment
{
 (attribute * { text } | text | fragmentContent)*
}</pre>
<p>Currently fragments can be injected into most Component, File, Directory and Feature elements. </p>
<p> New in version 3.3: The following additional special Ids can be used:</p>
<dt>&bull;</p>
<dd><code>#PRODUCT</code> for the <code>&lt;Product&gt;</code> element.</p>
<dt>&bull;</p>
<dd><code>#PRODUCTFEATURE</code> for the root <code>&lt;Feature&gt;</code> element. </p>
<p> New in version 3.7: Support patching arbitrary <code>&lt;Feature&gt;</code> elements. </p>
<p> New in version 3.9: Allow setting additional attributes. </p>
<p> The following example illustrates how this works. </p>
<p> Given that the WIX generator creates the following XML element: </p>
<pre>&lt;Component Id=&quot;CM_CP_applications.bin.my_libapp.exe&quot; Guid=&quot;*&quot;/&gt;</pre>
<p>The following XML patch file may be used to inject an Environment element into it: </p>
<pre>&lt;CPackWiXPatch&gt;
 &lt;CPackWiXFragment Id=&quot;CM_CP_applications.bin.my_libapp.exe&quot;&gt;
 &lt;Environment Id=&quot;MyEnvironment&quot; Action=&quot;set&quot;
 Name=&quot;MyVariableName&quot; Value=&quot;MyVariableValue&quot;/&gt;
 &lt;/CPackWiXFragment&gt;
&lt;/CPackWiXPatch&gt;</pre>
<dt><code>CPACK_WIX_EXTRA_SOURCES</code></p>
<dd>Extra WiX source files </p>
<p> This variable provides an optional list of extra WiX source files (.wxs) that should be compiled and linked. The full path to source files is required.</p>
<dt><code>CPACK_WIX_EXTRA_OBJECTS</code></p>
<dd>Extra WiX object files or libraries </p>
<p> This variable provides an optional list of extra WiX object (.wixobj) and/or WiX library (.wixlib) files. The full path to objects and libraries is required.</p>
<dt><code>CPACK_WIX_EXTENSIONS</code></p>
<dd>This variable provides a list of additional extensions for the WiX tools light and candle.</p>
<dt><code>CPACK_WIX_&lt;TOOL&gt;_EXTENSIONS</code></p>
<dd>This is the tool specific version of CPACK_WIX_EXTENSIONS. <code>&lt;TOOL&gt;</code> can be either LIGHT or CANDLE.</p>
<dt><code>CPACK_WIX_&lt;TOOL&gt;_EXTRA_FLAGS</code></p>
<dd>This list variable allows you to pass additional flags to the WiX tool <code>&lt;TOOL&gt;</code>. </p>
<p> Use it at your own risk. Future versions of CPack may generate flags which may be in conflict with your own flags. </p>
<p> <code>&lt;TOOL&gt;</code> can be either LIGHT or CANDLE.</p>
<dt><code>CPACK_WIX_CMAKE_PACKAGE_REGISTRY</code></p>
<dd>If this variable is set the generated installer will create an entry in the windows registry key <code>HKEY_LOCAL_MACHINE\Software\Kitware\CMake\Packages\&lt;PackageName&gt;</code> The value for <code>&lt;PackageName&gt;</code> is provided by this variable. </p>
<p> Assuming you also install a CMake configuration file this will allow other CMake projects to find your package with the <code>find_package()</code> command.</p>
<dt><code>CPACK_WIX_PROPERTY_&lt;PROPERTY&gt;</code></p>
<dd>New in version 3.1. </p>
<p> This variable can be used to provide a value for the Windows Installer property <code>&lt;PROPERTY&gt;</code> </p>
<p> The following list contains some example properties that can be used to customize information under &quot;Programs and Features&quot; (also known as &quot;Add or Remove Programs&quot;)</p>
<dt>&bull;</p>
<dd>ARPCOMMENTS &#8211; Comments</p>
<dt>&bull;</p>
<dd>ARPHELPLINK &#8211; Help and support information URL</p>
<dt>&bull;</p>
<dd>ARPURLINFOABOUT &#8211; General information URL</p>
<dt>&bull;</p>
<dd>ARPURLUPDATEINFO &#8211; Update information URL</p>
<dt>&bull;</p>
<dd>ARPHELPTELEPHONE &#8211; Help and support telephone number</p>
<dt>&bull;</p>
<dd>ARPSIZE &#8211; Size (in kilobytes) of the application</p>
<dt><code>CPACK_WIX_ROOT_FEATURE_TITLE</code></p>
<dd>New in version 3.7. </p>
<p> Sets the name of the root install feature in the WIX installer. Same as CPACK_COMPONENT_&lt;compName&gt;_DISPLAY_NAME for components.</p>
<dt><code>CPACK_WIX_ROOT_FEATURE_DESCRIPTION</code></p>
<dd>New in version 3.7. </p>
<p> Sets the description of the root install feature in the WIX installer. Same as CPACK_COMPONENT_&lt;compName&gt;_DESCRIPTION for components.</p>
<dt><code>CPACK_WIX_SKIP_PROGRAM_FOLDER</code></p>
<dd>New in version 3.7. </p>
<p> If this variable is set to true, the default install location of the generated package will be CPACK_PACKAGE_INSTALL_DIRECTORY directly. The install location will not be located relatively below ProgramFiles or ProgramFiles64. </p>
<p> <code>NOTE:</code> Installers created with this feature do not take differences between the system on which the installer is created and the system on which the installer might be used into account. </p>
<p> It is therefore possible that the installer e.g. might try to install onto a drive that is unavailable or unintended or a path that does not follow the localization or convention of the system on which the installation is performed.</p>
<dt><code>CPACK_WIX_ROOT_FOLDER_ID</code></p>
<dd>New in version 3.9. </p>
<p> This variable allows specification of a custom root folder ID. The generator specific <code>&lt;64&gt;</code> token can be used for folder IDs that come in 32-bit and 64-bit variants. In 32-bit builds the token will expand empty while in 64-bit builds it will expand to <code>64</code>. </p>
<p> When unset generated installers will default installing to <code>ProgramFiles&lt;64&gt;Folder</code>.</p>
<dt><code>CPACK_WIX_ROOT</code></p>
<dd>This variable can optionally be set to the root directory of a custom WiX Toolset installation. </p>
<p> When unspecified CPack will try to locate a WiX Toolset installation via the <code>WIX</code> environment variable instead.</p>
<dt><code>CPACK_WIX_CUSTOM_XMLNS</code></p>
<dd>New in version 3.19. </p>
<p> This variable provides a list of custom namespace declarations that are necessary for using WiX extensions. Each declaration should be in the form name=url, where name is the plain namespace without the usual xmlns: prefix and url is an unquoted namespace url. A list of commonly known WiX schemata can be found here: <i><a rel="nofollow" href="https://wixtoolset.org/documentation/manual/v3/xsd/">https://wixtoolset.org/documentation/manual/v3/xsd/</a></i></dl>
<h2>Copyright</h2>
<p>2000-2022 Kitware, Inc. and Contributors</p>
