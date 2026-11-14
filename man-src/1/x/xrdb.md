---
title: "xrdb(1)"
name: "xrdb"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xrdb/"
description: "xrdb – X server resource database utility"
---

<h2 class="name">NAME</h2>
<p> xrdb &#8211; X server resource database utility </p>
<h2>SYNOPSIS</h2>
<p> <code>xrdb</code> [-option &#8230;] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xrdb</i> is used to get or set the contents of the RESOURCE_MANAGER property on the root window of screen 0, or the SCREEN_RESOURCES property on the root window of any or all screens, or everything combined. You would normally run this program from your X startup file. </p>
<p> Most X clients use the RESOURCE_MANAGER and SCREEN_RESOURCES properties to get user preferences about color, fonts, and so on for applications. Having this information in the server (where it is available to all clients) instead of on disk, solves the problem in previous versions of X that required you to maintain <i>defaults</i> files on every machine that you might use. It also allows for dynamic changing of defaults without editing files. </p>
<p> The RESOURCE_MANAGER property is used for resources that apply to all screens of the display. The SCREEN_RESOURCES property on each screen specifies additional (or overriding) resources to be used for that screen. (When there is only one screen, SCREEN_RESOURCES is normally not used, all resources are just placed in the RESOURCE_MANAGER property.) </p>
<p> The file specified by <i>filename</i> (or the contents from standard input if &#8211; or no filename is given) is optionally passed through the C preprocessor with the following symbols defined, based on the capabilities of the server being used:</p>
<dl>
<dt><code>SERVERHOST=</code><i>hostname</i></p>
<dd> the hostname portion of the display to which you are connected.</p>
<dt><code>SRVR_</code><i>name</i></p>
<dd> the SERVERHOST hostname string turned into a legal identifier. For example, &quot;my-dpy.lcs.mit.edu&quot; becomes SRVR_my_dpy_lcs_mit_edu.</p>
<dt><code>HOST=</code><i>hostname</i></p>
<dd> the same as <code>SERVERHOST</code>.</p>
<dt><code>DISPLAY_NUM=</code><i>num</i></p>
<dd> the number of the display on the server host.</p>
<dt><code>CLIENTHOST=</code><i>hostname</i></p>
<dd> the name of the host on which <i>xrdb</i> is running.</p>
<dt><code>CLNT_</code><i>name</i></p>
<dd> the CLIENTHOST hostname string turned into a legal identifier. For example, &quot;expo.lcs.mit.edu&quot; becomes CLNT_expo_lcs_mit_edu.</p>
<dt><code>RELEASE=</code><i>num</i></p>
<dd> the vendor release number for the server. The interpretation of this number will vary depending on VENDOR.</p>
<dt><code>REVISION=</code><i>num</i></p>
<dd> the X protocol minor version supported by this server (currently 0).</p>
<dt><code>VERSION=</code><i>num</i></p>
<dd> the X protocol major version supported by this server (should always be 11).</p>
<dt><code>VENDOR=</code><i>vendor</i></p>
<dd> a string literal specifying the vendor of the server.</p>
<dt><code>VNDR_</code><i>name</i></p>
<dd> the VENDOR name string turned into a legal identifier. For example, &quot;MIT X Consortium&quot; becomes VNDR_MIT_X_Consortium.</p>
<dt><code>EXT_</code><i>name</i></p>
<dd> A symbol is defined for each protocol extension supported by the server. Each extension string name is turned into a legal identifier. For example, &quot;X3D-PEX&quot; becomes EXT_X3D_PEX.</p>
<dt><code>NUM_SCREENS=</code><i>num</i></p>
<dd> the total number of screens.</p>
<dt><code>SCREEN_NUM=</code><i>num</i></p>
<dd> the number of the current screen (from zero).</p>
<dt><code>BITS_PER_RGB=</code><i>num</i></p>
<dd> the number of significant bits in an RGB color specification. This is the log base 2 of the number of distinct shades of each primary that the hardware can generate. Note that it usually is not related to PLANES.</p>
<dt><code>CLASS=</code><i>visualclass</i></p>
<dd> one of StaticGray, GrayScale, StaticColor, PseudoColor, TrueColor, DirectColor. This is the visual class of the root window.</p>
<dt><code>CLASS_</code><i>visualclass</i>=<i>visualid</i></p>
<dd> the visual class of the root window in a form you can <i>#ifdef</i> on. The value is the numeric id of the visual.</p>
<dt><code>COLOR</code></p>
<dd> defined only if CLASS is one of StaticColor, PseudoColor, TrueColor, or DirectColor.</p>
<dt><code>CLASS_</code><i>visualclass</i>_<i>depth</i>=<i>num</i></p>
<dd> A symbol is defined for each visual supported for the screen. The symbol includes the class of the visual and its depth; the value is the numeric id of the visual. (If more than one visual has the same class and depth, the numeric id of the first one reported by the server is used.)</p>
<dt><code>HEIGHT=</code><i>num</i></p>
<dd> the height of the root window in pixels.</p>
<dt><code>WIDTH=</code><i>num</i></p>
<dd> the width of the root window in pixels.</p>
<dt><code>PLANES=</code><i>num</i></p>
<dd> the number of bit planes (the depth) of the root window.</p>
<dt><code>X_RESOLUTION=</code><i>num</i></p>
<dd> the x resolution of the screen in pixels per meter.</p>
<dt><code>Y_RESOLUTION=</code><i>num</i></p>
<dd> the y resolution of the screen in pixels per meter.</dl>
<p> SRVR_<i>name</i>, CLNT_<i>name</i>, VNDR_<i>name</i>, and EXT_<i>name</i> identifiers are formed by changing all characters other than letters and digits into underscores (_). </p>
<p> Lines that begin with an exclamation mark (!) are ignored and may be used as comments. </p>
<p> Note that since <i>xrdb</i> can read from standard input, it can be used to the change the contents of properties directly from a terminal or from a shell script.</p>
<h2>OPTIONS</h2>
<p> <i>xrdb</i> program accepts the following options:</p>
<dl>
<dt><code>-help</code></p>
<dd> This option (or any unsupported option) will cause a brief description of the allowable options and parameters to be printed.</p>
<dt><code>-version</code></p>
<dd> This option will cause the xrdb version to be printed and the program to exit without performing any other operations.</p>
<dt><code>-display </code><i>display</i></p>
<dd> This option specifies the X server to be used; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>. It also specifies the screen to use for the <i>-screen</i> option, and it specifies the screen from which preprocessor symbols are derived for the <i>-global</i> option.</p>
<dt><code>-all</code></p>
<dd> This option indicates that operation should be performed on the screen-independent resource property (RESOURCE_MANAGER), as well as the screen-specific property (SCREEN_RESOURCES) on every screen of the display. For example, when used in conjunction with <i>-query</i>, the contents of all properties are output. For <i>-load</i>, <i>-override</i> and <i>-merge</i>, the input file is processed once for each screen. The resources which occur in common in the output for every screen are collected, and these are applied as the screen-independent resources. The remaining resources are applied for each individual per-screen property. This the default mode of operation.</p>
<dt><code>-global</code></p>
<dd> This option indicates that the operation should only be performed on the screen-independent RESOURCE_MANAGER property.</p>
<dt><code>-screen</code></p>
<dd> This option indicates that the operation should only be performed on the SCREEN_RESOURCES property of the default screen of the display.</p>
<dt><code>-screens</code></p>
<dd> This option indicates that the operation should be performed on the SCREEN_RESOURCES property of each screen of the display. For <i>-load</i>, <i>-override</i> and <i>-merge</i>, the input file is processed for each screen.</p>
<dt><code>-n</code></p>
<dd> This option indicates that changes to the specified properties (when used with <i>-load</i>, <i>-override</i> or <i>-merge</i>) or to the resource file (when used with <i>-edit</i>) should be shown on the standard output, but should not be performed.</p>
<dt><code>-quiet</code></p>
<dd> This option indicates that warning about duplicate entries should not be displayed.</p>
<dt><code>-cpp </code><i>filename</i></p>
<dd> This option specifies the pathname of the C preprocessor program to be used. Although <i>xrdb</i> was designed to use CPP, any program that acts as a filter and accepts the -D, -I, and -U options may be used.</p>
<dt><code>-nocpp</code></p>
<dd> This option indicates that <i>xrdb</i> should not run the input file through a preprocessor before loading it into properties.</p>
<dt><code>-undef</code></p>
<dd> This option is passed to the C preprocessor if used. It prevents it from predefining any system specific macros.</p>
<dt><code>-E</code></p>
<dd> This option indicates that any cpp command run and the output from it should be shown on standard output. If <code>-nocpp</code> was also specified, the input file will be shown as read. The specified changes will also be performed unless the <code>-n</code> option is also specified.</p>
<dt><code>-symbols</code></p>
<dd> This option indicates that the symbols that are defined for the preprocessor should be printed onto the standard output.</p>
<dt><code>-query</code></p>
<dd> This option indicates that the current contents of the specified properties should be printed onto the standard output. Note that since preprocessor commands in the input resource file are part of the input file, not part of the property, they won&#8217;t appear in the output from this option. The <code>-edit</code> option can be used to merge the contents of properties back into the input resource file without damaging preprocessor commands.</p>
<dt><code>-get </code><i>name</i></p>
<dd> This option indicates that the current content of the property matching <i>name</i> should be printed onto the standard output.</p>
<dt><code>-load</code></p>
<dd> This option indicates that the input should be loaded as the new value of the specified properties, replacing whatever was there (i.e. the old contents are removed). This is the default action.</p>
<dt><code>-override</code></p>
<dd> This option indicates that the input should be added to, instead of replacing, the current contents of the specified properties. New entries override previous entries.</p>
<dt><code>-merge</code></p>
<dd> This option indicates that the input should be merged and lexicographically sorted with, instead of replacing, the current contents of the specified properties.</p>
<dt><code>-remove</code></p>
<dd> This option indicates that the specified properties should be removed from the server.</p>
<dt><code>-retain</code></p>
<dd> This option indicates that the server should be instructed not to reset if <i>xrdb</i> is the first client. This should never be necessary under normal conditions, since <i>xdm</i> and <i>xinit</i> always act as the first client.</p>
<dt><code>-edit </code><i>filename</i></p>
<dd> This option indicates that the contents of the specified properties should be edited into the given file, replacing any values already listed there. This allows you to put changes that you have made to your defaults back into your resource file, preserving any comments or preprocessor lines.</p>
<dt><code>-backup </code><i>string</i></p>
<dd> This option specifies a suffix to be appended to the filename used with <code>-edit</code> to generate a backup file.</p>
<dt><code>-D</code><i>name[=value]</i></p>
<dd> This option is passed through to the preprocessor and is used to define symbols for use with conditionals such as <i>#ifdef.</i></p>
<dt><code>-U</code><i>name</i></p>
<dd> This option is passed through to the preprocessor and is used to remove any definitions of this symbol.</p>
<dt><code>-I</code><i>directory</i></p>
<dd> This option is passed through to the preprocessor and is used to specify a directory to search for files that are referenced with <i>#include.</i></dl>
<h2>FILES</h2>
<p> <i>Xrdb</i> does not load any files on its own, but many desktop environments use xrdb to load <i>~/.Xresources</i> files on session startup to initialize the resource database, as a generalized replacement for <i>~/.Xdefaults</i> files.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-appres/">appres</a>(1), <a href="/docs/linux/man/1-listres/">listres</a>(1), Xlib Resource Manager documentation, Xt resource documentation</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to figure out which display to use.</dl>
<h2>BUGS</h2>
<p> The default for no arguments should be to query, not to overwrite, so that it is consistent with other programs.</p>
<h2>AUTHORS</h2>
<p> Bob Scheifler, Phil Karlton, rewritten from the original by Jim Gettys </p>
<h2>Index</h2>
