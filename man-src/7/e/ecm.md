---
title: "ecm(7)"
name: "ecm"
section: "7"
letter: "e"
url: "/docs/linux/man/7-ecm/"
description: "ecm – Extra CMake Modules"
---

<p>ecm &#8211; Extra CMake Modules</p>
<h2>Introduction</h2>
<p>The Extra CMake Modules package, or ECM, adds to the modules provided by CMake, including ones used by <code>find_package()</code> to find common software, ones that can be used directly in <code>CMakeLists.txt</code> files to perform common tasks and toolchain files that must be specified on the commandline by the user. </p>
<p> In addition, it provides common build settings used in software produced by the KDE community. </p>
<p> While the driving force of this module is to reduce duplication in CMake scripts across KDE software, it is intended to be useful for any software that uses the CMake build system.</p>
<h2>Usage</h2>
<p>To use ECM, add the following to your <code>CMakeLists.txt</code>: </p>
<pre>find_package(ECM REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${ECM_MODULE_PATH})</pre>
<p>(note that you may want to append <code>${ECM_MODULE_PATH}</code> to <code>CMAKE_MODULE_PATH</code> rather than discarding the existing value). You can then just include the modules you require, or use <code>find_package()</code> as needed. For example: </p>
<pre>include(ECMInstallIcons)</pre>
<p>Developers of KDE software will often want to use the KDE standard settings provided by ECM; they can do the following: </p>
<pre>find_package(ECM REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${ECM_MODULE_PATH})
include(KDEInstallDirs)
include(KDECompilerSettings)
include(KDECMakeSettings)</pre>
<p>Note that any combination of the above includes can be used if you only want some of the settings. Some of the functionality of <code>KDECMakeSettings</code> can also be selectively disabled.</p>
<h3>Organization</h3>
<p>ECM provides four different types of modules.</p>
<dl>
<dt>&bull;</p>
<dd>Core modules provide helpful macros for use in project CMake scripts. See <code><a href="/docs/linux/man/7-ecm-modules/">ecm-modules</a>(7)</code> for more information.</p>
<dt>&bull;</p>
<dd>Find modules extend the functionality of CMake&#8217;s <code>find_package()</code> command. See <code><a href="/docs/linux/man/7-ecm-find-modules/">ecm-find-modules</a>(7)</code> for more information.</p>
<dt>&bull;</p>
<dd>KDE modules provide common settings for software produced by KDE; much of this may also be useful to other projects. See <code><a href="/docs/linux/man/7-ecm-kde-modules/">ecm-kde-modules</a>(7)</code> for more information.</p>
<dt>&bull;</p>
<dd>Toolchain files change the build tools and targets used by CMake. See <code><a href="/docs/linux/man/7-ecm-toolchains/">ecm-toolchains</a>(7)</code> for more information. </p>
<p> The <code>${ECM_MODULE_DIR}</code>, <code>${ECM_FIND_MODULE_DIR}</code> and <code>${ECM_KDE_MODULE_DIR}</code> variables may be used instead of <code>${ECM_MODULE_PATH}</code> if you only need some of this functionality.</dl>
<h2>Development</h2>
<p>The <code><a href="/docs/linux/man/7-ecm-developer/">ecm-developer</a>(7)</code> manual contains more information about developing for Extra CMake Modules.</p>
<h2>License</h2>
<p>All code is licensed under the <i>BSD 3-Clause license</i>.</p>
<h2>Links</h2>
<dl>
<dt>&bull;</p>
<dd>Home page: <i><a rel="nofollow" href="https://commits.kde.org/extra-cmake-modules">https://commits.kde.org/extra-cmake-modules</a></i></p>
<dt>&bull;</p>
<dd>Documentation: <i><a rel="nofollow" href="https://api.kde.org/ecm/">https://api.kde.org/ecm/</a></i></p>
<dt>&bull;</p>
<dd>Mailing list: <i><a rel="nofollow" href="https://mail.kde.org/mailman/listinfo/kde-buildsystem">https://mail.kde.org/mailman/listinfo/kde-buildsystem</a></i></p>
<dt>&bull;</p>
<dd>IRC channel: #kde-devel on Freenode</p>
<dt>&bull;</p>
<dd>Git repository: <i><a rel="nofollow" href="https://commits.kde.org/extra-cmake-modules">https://commits.kde.org/extra-cmake-modules</a></i></dl>
<h2>Copyright</h2>
<p>KDE Developers</p>
