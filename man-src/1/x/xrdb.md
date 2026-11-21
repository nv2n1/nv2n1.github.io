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
<dt><code>SERVERHOST=</code><i>hostname</i></dt>
<dd> the hostname portion of the display to which you are connected.</dd>
<dt><code>SRVR_</code><i>name</i></dt>
<dd> the SERVERHOST hostname string turned into a legal identifier. For example, &quot;my-dpy.lcs.mit.edu&quot; becomes SRVR_my_dpy_lcs_mit_edu.</dd>
<dt><code>HOST=</code><i>hostname</i></dt>
<dd> the same as <code>SERVERHOST</code>.</dd>
<dt><code>DISPLAY_NUM=</code><i>num</i></dt>
<dd> the number of the display on the server host.</dd>
<dt><code>CLIENTHOST=</code><i>hostname</i></dt>
<dd> the name of the host on which <i>xrdb</i> is running.</dd>
<dt><code>CLNT_</code><i>name</i></dt>
<dd> the CLIENTHOST hostname string turned into a legal identifier. For example, &quot;expo.lcs.mit.edu&quot; becomes CLNT_expo_lcs_mit_edu.</dd>
<dt><code>RELEASE=</code><i>num</i></dt>
<dd> the vendor release number for the server. The interpretation of this number will vary depending on VENDOR.</dd>
<dt><code>REVISION=</code><i>num</i></dt>
<dd> the X protocol minor version supported by this server (currently 0).</dd>
<dt><code>VERSION=</code><i>num</i></dt>
<dd> the X protocol major version supported by this server (should always be 11).</dd>
<dt><code>VENDOR=</code><i>vendor</i></dt>
<dd> a string literal specifying the vendor of the server.</dd>
<dt><code>VNDR_</code><i>name</i></dt>
<dd> the VENDOR name string turned into a legal identifier. For example, &quot;MIT X Consortium&quot; becomes VNDR_MIT_X_Consortium.</dd>
<dt><code>EXT_</code><i>name</i></dt>
<dd> A symbol is defined for each protocol extension supported by the server. Each extension string name is turned into a legal identifier. For example, &quot;X3D-PEX&quot; becomes EXT_X3D_PEX.</dd>
<dt><code>NUM_SCREENS=</code><i>num</i></dt>
<dd> the total number of screens.</dd>
<dt><code>SCREEN_NUM=</code><i>num</i></dt>
<dd> the number of the current screen (from zero).</dd>
<dt><code>BITS_PER_RGB=</code><i>num</i></dt>
<dd> the number of significant bits in an RGB color specification. This is the log base 2 of the number of distinct shades of each primary that the hardware can generate. Note that it usually is not related to PLANES.</dd>
<dt><code>CLASS=</code><i>visualclass</i></dt>
<dd> one of StaticGray, GrayScale, StaticColor, PseudoColor, TrueColor, DirectColor. This is the visual class of the root window.</dd>
<dt><code>CLASS_</code><i>visualclass</i>=<i>visualid</i></dt>
<dd> the visual class of the root window in a form you can <i>#ifdef</i> on. The value is the numeric id of the visual.</dd>
<dt><code>COLOR</code></dt>
<dd> defined only if CLASS is one of StaticColor, PseudoColor, TrueColor, or DirectColor.</dd>
<dt><code>CLASS_</code><i>visualclass</i>_<i>depth</i>=<i>num</i></dt>
<dd> A symbol is defined for each visual supported for the screen. The symbol includes the class of the visual and its depth; the value is the numeric id of the visual. (If more than one visual has the same class and depth, the numeric id of the first one reported by the server is used.)</dd>
<dt><code>HEIGHT=</code><i>num</i></dt>
<dd> the height of the root window in pixels.</dd>
<dt><code>WIDTH=</code><i>num</i></dt>
<dd> the width of the root window in pixels.</dd>
<dt><code>PLANES=</code><i>num</i></dt>
<dd> the number of bit planes (the depth) of the root window.</dd>
<dt><code>X_RESOLUTION=</code><i>num</i></dt>
<dd> the x resolution of the screen in pixels per meter.</dd>
<dt><code>Y_RESOLUTION=</code><i>num</i></dt>
<dd> the y resolution of the screen in pixels per meter.</dd></dl>
<p> SRVR_<i>name</i>, CLNT_<i>name</i>, VNDR_<i>name</i>, and EXT_<i>name</i> identifiers are formed by changing all characters other than letters and digits into underscores (_). </p>
<p> Lines that begin with an exclamation mark (!) are ignored and may be used as comments. </p>
<p> Note that since <i>xrdb</i> can read from standard input, it can be used to the change the contents of properties directly from a terminal or from a shell script.</p>
<h2>OPTIONS</h2>
<p> <i>xrdb</i> program accepts the following options:</p>
<dl>
<dt><code>-help</code></dt>
<dd> This option (or any unsupported option) will cause a brief description of the allowable options and parameters to be printed.</dd>
<dt><code>-version</code></dt>
<dd> This option will cause the xrdb version to be printed and the program to exit without performing any other operations.</dd>
<dt><code>-display </code><i>display</i></dt>
<dd> This option specifies the X server to be used; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>. It also specifies the screen to use for the <i>-screen</i> option, and it specifies the screen from which preprocessor symbols are derived for the <i>-global</i> option.</dd>
<dt><code>-all</code></dt>
<dd> This option indicates that operation should be performed on the screen-independent resource property (RESOURCE_MANAGER), as well as the screen-specific property (SCREEN_RESOURCES) on every screen of the display. For example, when used in conjunction with <i>-query</i>, the contents of all properties are output. For <i>-load</i>, <i>-override</i> and <i>-merge</i>, the input file is processed once for each screen. The resources which occur in common in the output for every screen are collected, and these are applied as the screen-independent resources. The remaining resources are applied for each individual per-screen property. This the default mode of operation.</dd>
<dt><code>-global</code></dt>
<dd> This option indicates that the operation should only be performed on the screen-independent RESOURCE_MANAGER property.</dd>
<dt><code>-screen</code></dt>
<dd> This option indicates that the operation should only be performed on the SCREEN_RESOURCES property of the default screen of the display.</dd>
<dt><code>-screens</code></dt>
<dd> This option indicates that the operation should be performed on the SCREEN_RESOURCES property of each screen of the display. For <i>-load</i>, <i>-override</i> and <i>-merge</i>, the input file is processed for each screen.</dd>
<dt><code>-n</code></dt>
<dd> This option indicates that changes to the specified properties (when used with <i>-load</i>, <i>-override</i> or <i>-merge</i>) or to the resource file (when used with <i>-edit</i>) should be shown on the standard output, but should not be performed.</dd>
<dt><code>-quiet</code></dt>
<dd> This option indicates that warning about duplicate entries should not be displayed.</dd>
<dt><code>-cpp </code><i>filename</i></dt>
<dd> This option specifies the pathname of the C preprocessor program to be used. Although <i>xrdb</i> was designed to use CPP, any program that acts as a filter and accepts the -D, -I, and -U options may be used.</dd>
<dt><code>-nocpp</code></dt>
<dd> This option indicates that <i>xrdb</i> should not run the input file through a preprocessor before loading it into properties.</dd>
<dt><code>-undef</code></dt>
<dd> This option is passed to the C preprocessor if used. It prevents it from predefining any system specific macros.</dd>
<dt><code>-E</code></dt>
<dd> This option indicates that any cpp command run and the output from it should be shown on standard output. If <code>-nocpp</code> was also specified, the input file will be shown as read. The specified changes will also be performed unless the <code>-n</code> option is also specified.</dd>
<dt><code>-symbols</code></dt>
<dd> This option indicates that the symbols that are defined for the preprocessor should be printed onto the standard output.</dd>
<dt><code>-query</code></dt>
<dd> This option indicates that the current contents of the specified properties should be printed onto the standard output. Note that since preprocessor commands in the input resource file are part of the input file, not part of the property, they won&#8217;t appear in the output from this option. The <code>-edit</code> option can be used to merge the contents of properties back into the input resource file without damaging preprocessor commands.</dd>
<dt><code>-get </code><i>name</i></dt>
<dd> This option indicates that the current content of the property matching <i>name</i> should be printed onto the standard output.</dd>
<dt><code>-load</code></dt>
<dd> This option indicates that the input should be loaded as the new value of the specified properties, replacing whatever was there (i.e. the old contents are removed). This is the default action.</dd>
<dt><code>-override</code></dt>
<dd> This option indicates that the input should be added to, instead of replacing, the current contents of the specified properties. New entries override previous entries.</dd>
<dt><code>-merge</code></dt>
<dd> This option indicates that the input should be merged and lexicographically sorted with, instead of replacing, the current contents of the specified properties.</dd>
<dt><code>-remove</code></dt>
<dd> This option indicates that the specified properties should be removed from the server.</dd>
<dt><code>-retain</code></dt>
<dd> This option indicates that the server should be instructed not to reset if <i>xrdb</i> is the first client. This should never be necessary under normal conditions, since <i>xdm</i> and <i>xinit</i> always act as the first client.</dd>
<dt><code>-edit </code><i>filename</i></dt>
<dd> This option indicates that the contents of the specified properties should be edited into the given file, replacing any values already listed there. This allows you to put changes that you have made to your defaults back into your resource file, preserving any comments or preprocessor lines.</dd>
<dt><code>-backup </code><i>string</i></dt>
<dd> This option specifies a suffix to be appended to the filename used with <code>-edit</code> to generate a backup file.</dd>
<dt><code>-D</code><i>name[=value]</i></dt>
<dd> This option is passed through to the preprocessor and is used to define symbols for use with conditionals such as <i>#ifdef.</i></dd>
<dt><code>-U</code><i>name</i></dt>
<dd> This option is passed through to the preprocessor and is used to remove any definitions of this symbol.</dd>
<dt><code>-I</code><i>directory</i></dt>
<dd> This option is passed through to the preprocessor and is used to specify a directory to search for files that are referenced with <i>#include.</i></dd></dl>
<h2>FILES</h2>
<p> <i>Xrdb</i> does not load any files on its own, but many desktop environments use xrdb to load <i>~/.Xresources</i> files on session startup to initialize the resource database, as a generalized replacement for <i>~/.Xdefaults</i> files.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-appres/">appres</a>(1), <a href="/docs/linux/man/1-listres/">listres</a>(1), Xlib Resource Manager documentation, Xt resource documentation</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></dt>
<dd> to figure out which display to use.</dd></dl>
<h2>BUGS</h2>
<p> The default for no arguments should be to query, not to overwrite, so that it is consistent with other programs.</p>
<h2>AUTHORS</h2>
<p> Bob Scheifler, Phil Karlton, rewritten from the original by Jim Gettys </p>
