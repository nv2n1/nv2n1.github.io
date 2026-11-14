---
title: "curl-config(1)"
name: "curl-config"
section: "1"
letter: "c"
url: "/docs/linux/man/1-curl-config/"
description: "curl-config – Get information about a libcurl installation"
---

<h2 class="name">NAME</h2>
<p> curl-config &#8211; Get information about a libcurl installation </p>
<h2>SYNOPSIS</h2>
<p> <code>curl-config [options]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>curl-config</code> displays information about the curl and libcurl installation.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;ca</p>
<dd> Displays the built-in path to the CA cert bundle this libcurl uses.</p>
<dt>&#8211;cc</p>
<dd> Displays the compiler used to build libcurl.</p>
<dt>&#8211;cflags</p>
<dd> Set of compiler options (CFLAGS) to use when compiling files that use libcurl. Currently that is only the include path to the curl include files.</p>
<dt>&#8211;checkfor [version]</p>
<dd> Specify the oldest possible libcurl version string you want, and this script will return 0 if the current installation is new enough or it returns 1 and outputs a text saying that the current version is not new enough. (Added in 7.15.4)</p>
<dt>&#8211;configure</p>
<dd> Displays the arguments given to configure when building curl.</p>
<dt>&#8211;feature</p>
<dd> Lists what particular main features the installed libcurl was built with. At the time of writing, this list may include SSL, KRB4 or IPv6. Do not assume any particular order. The keywords will be separated by newlines. There may be none, one, or several keywords in the list.</p>
<dt>&#8211;help</p>
<dd> Displays the available options.</p>
<dt>&#8211;libs</p>
<dd> Shows the complete set of libs and other linker options you will need in order to link your application with libcurl.</p>
<dt>&#8211;prefix</p>
<dd> This is the prefix used when libcurl was installed. Libcurl is then installed in $prefix/lib and its header files are installed in $prefix/include and so on. The prefix is set with &quot;configure &#8211;prefix&quot;.</p>
<dt>&#8211;protocols</p>
<dd> Lists what particular protocols the installed libcurl was built to support. At the time of writing, this list may include HTTP, HTTPS, FTP, FTPS, FILE, TELNET, LDAP, DICT. Do not assume any particular order. The protocols will be listed using uppercase and are separated by newlines. There may be none, one, or several protocols in the list. (Added in 7.13.0)</p>
<dt>&#8211;ssl-backends</p>
<dd> Lists the SSL backends that were enabled when libcurl was built. It might be no, one or several names. If more than one name, they will appear comma-separated. (Added in 7.58.0)</p>
<dt>&#8211;static-libs</p>
<dd> Shows the complete set of libs and other linker options you will need in order to link your application with libcurl statically. (Added in 7.17.1)</p>
<dt>&#8211;version</p>
<dd> Outputs version information about the installed libcurl.</p>
<dt>&#8211;vernum</p>
<dd> Outputs version information about the installed libcurl, in numerical mode. This outputs the version number, in hexadecimal, with 8 bits for each part: major, minor, and patch. So that libcurl 7.7.4 would appear as 070704 and libcurl 12.13.14 would appear as 0c0d0e&#8230; Note that the initial zero might be omitted. (This option was broken in the 7.15.0 release.)</dl>
<h2>EXAMPLES</h2>
<p> What linker options do I need when I link with libcurl? </p>
<p>&nbsp;<wbr>&nbsp;$&nbsp;curl-config &#8211;libs </p>
<p> What compiler options do I need when I compile using libcurl functions? </p>
<p>&nbsp;<wbr>&nbsp;$&nbsp;curl-config &#8211;cflags </p>
<p> How do I know if libcurl was built with SSL support? </p>
<p>&nbsp;<wbr>&nbsp;$&nbsp;curl-config &#8211;feature | grep SSL </p>
<p> What&#8217;s the installed libcurl version? </p>
<p>&nbsp;<wbr>&nbsp;$&nbsp;curl-config &#8211;version </p>
<p> How do I build a single file with a one-line command? </p>
<p>&nbsp;<wbr>&nbsp;$&nbsp;`curl-config &#8211;cc &#8211;cflags`&nbsp;-o example example.c&nbsp;`curl-config &#8211;libs`</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-curl/">curl</a></code>(1) </p>
<h2>Index</h2>
