---
title: "flatpak-build-init(1)"
name: "flatpak-build-init"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-build-init/"
description: "flatpak-build-init – Initialize a build directory"
---

<h2 class="name">NAME</h2>
<p> flatpak-build-init &#8211; Initialize a build directory </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak build-init</code> [OPTION&#8230;] DIRECTORY APPNAME SDK RUNTIME [BRANCH]</dl>
<h2>DESCRIPTION</h2>
<dd>Initializes a directory for building an application. DIRECTORY is the name of the directory. APPNAME is the application id of the app that will be built. SDK and RUNTIME specify the sdk and runtime that the application should be built against and run in. </p>
<p> The result of this command is that a metadata file is created inside the given directory. Additionally, empty files and var subdirectories are created. </p>
<p> It is an error to run build-init on a directory that has already been initialized as a build directory.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;arch=ARCH</code></p>
<dl>
<dt>
<dd> The architecture to use. See <code>flatpak &#8211;supported-arches</code> for architectures supported by the host.</dl>
<p> <code>-v</code>, <code>&#8211;var=RUNTIME</code></p>
<dl>
<dt>
<dd> Initialize var from the named runtime.</dl>
<p> <code>-w</code>, <code>&#8211;writable-sdk</code></p>
<dl>
<dt>
<dd> Initialize /usr with a copy of the sdk, which is writable during flatpak build. This can be used if you need to install build tools in /usr during the build. This is stored in the usr subdirectory of the app dir, but will not be part of the final app.</dl>
<p> <code>&#8211;tag=TAG</code></p>
<dl>
<dt>
<dd> Add a tag to the metadata file. This option can be used multiple times.</dl>
<p> <code>&#8211;sdk-extension=EXTENSION</code></p>
<dl>
<dt>
<dd> When using <code>&#8211;writable-sdk</code>, in addition to the sdk, also install the specified extension. This option can be used multiple times.</dl>
<p> <code>&#8211;extension=NAME=VARIABLE[=VALUE]</code></p>
<dl>
<dt>
<dd> Add extension point info.</dl>
<p> <code>&#8211;sdk-dir</code></p>
<dl>
<dt>
<dd> Specify a custom subdirectory to use instead of usr for <code>&#8211;writable-sdk</code>.</dl>
<p> <code>&#8211;update</code></p>
<dl>
<dt>
<dd> Re-initialize the sdk and var, don&#8217;t fail if already initialized.</dl>
<p> <code>&#8211;base=APP</code></p>
<dl>
<dt>
<dd> Initialize the application with files from another specified application.</dl>
<p> <code>&#8211;base-version=VERSION</code></p>
<dl>
<dt>
<dd> Specify the version to use for <code>&#8211;base</code>. If not specified, will default to &quot;master&quot;.</dl>
<p> <code>&#8211;base-extension=EXTENSION</code></p>
<dl>
<dt>
<dd> When using <code>&#8211;base</code>, also install the specified extension from the app. This option can be used multiple times.</dl>
<p> <code>&#8211;type=TYPE</code></p>
<dl>
<dt>
<dd> This can be used to build different types of things. The default is &quot;app&quot; which is a regular app, but &quot;runtime&quot; creates a runtime based on an existing runtime, and &quot;extension&quot; creates an extension for an app or runtime.</dl>
<p> <code>&#8211;extension-tag=EXTENSION_TAG</code></p>
<dl>
<dt>
<dd> If building an extension, the tag to use when searching for the mount point of the extension.</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak build-init /build/my-app org.gnome.Sdk org.gnome.Platform 3.16</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build/">flatpak-build</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-finish/">flatpak-build-finish</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-build-export/">flatpak-build-export</a></code>(1) </p>
<h2>Index</h2>
