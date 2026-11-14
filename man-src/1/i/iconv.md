---
title: "iconv(1)"
name: "iconv"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iconv/"
description: "iconv – convert text from one character encoding to another"
---

<h2 class="name">NAME</h2>
<p> iconv &#8211; convert text from one character encoding to another </p>
<h2>SYNOPSIS</h2>
<p> <code>iconv</code> [<i>options</i>] [-f <i>from-encoding</i>] [-t <i>to-encoding</i>] [<i>inputfile</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>iconv</code> program reads in text in one encoding and outputs the text in another encoding. If no input files are given, or if it is given as a dash (-), <code>iconv</code> reads from standard input. If no output file is given, <code>iconv</code> writes to standard output. </p>
<p> If no <i>from-encoding</i> is given, the default is derived from the current locale&#8217;s character encoding. If no <i>to-encoding</i> is given, the default is derived from the current locale&#8217;s character encoding.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i> from-encoding</i>, &#8211;from-code=<i>from-encoding</i></p>
<dd> Use <i>from-encoding</i> for input characters.</p>
<dt><code>-t</code><i> to-encoding</i>, &#8211;to-code=<i>to-encoding</i></p>
<dd> Use <i>to-encoding</i> for output characters.</p>
<dt>
<dd> If the string <code>//IGNORE</code> is appended to <i>to-encoding</i>, characters that cannot be converted are discarded and an error is printed after conversion.</p>
<dt>
<dd> If the string <code>//TRANSLIT</code> is appended to <i>to-encoding</i>, characters being converted are transliterated when needed and possible. This means that when a character cannot be represented in the target character set, it can be approximated through one or several similar looking characters. Characters that are outside of the target character set and cannot be transliterated are replaced with a question mark (?) in the output.</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> List all known character set encodings.</p>
<dt><code>-c</code></p>
<dd> Silently discard characters that cannot be converted instead of terminating when encountering such characters.</p>
<dt><code>-o</code><i> outputfile</i>, &#8211;output=<i>outputfile</i></p>
<dd> Use <i>outputfile</i> for output.</p>
<dt><code>-s</code>, <code>&#8211;silent</code></p>
<dd> This option is ignored; it is provided only for compatibility.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Print progress information on standard error when processing multiple files.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Print a usage summary and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd> Print a short usage summary and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version number, license, and disclaimer of warranty for <code>iconv</code>.</dl>
<h2>EXIT STATUS</h2>
<p> Zero on success, nonzero on errors.</p>
<h2>ENVIRONMENT</h2>
<p> Internally, the <code>iconv</code> program uses the <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3) function which in turn uses <i>gconv</i> modules (dynamically loaded shared libraries) to convert to and from a character set. Before calling <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3), the <code>iconv</code> program must first allocate a conversion descriptor using <code><a href="/docs/linux/man/3-iconv_open/">iconv_open</a></code>(3). The operation of the latter function is influenced by the setting of the <code>GCONV_PATH</code> environment variable:</p>
<dl>
<dt>*</p>
<dd> If <code>GCONV_PATH</code> is not set, <code><a href="/docs/linux/man/3-iconv_open/">iconv_open</a></code>(3) loads the system gconv module configuration cache file created by <code><a href="/docs/linux/man/8-iconvconfig/">iconvconfig</a></code>(8) and then, based on the configuration, loads the gconv modules needed to perform the conversion. If the system gconv module configuration cache file is not available then the system gconv module configuration file is used.</p>
<dt>*</p>
<dd> If <code>GCONV_PATH</code> is defined (as a colon-separated list of pathnames), the system gconv module configuration cache is not used. Instead, <code><a href="/docs/linux/man/3-iconv_open/">iconv_open</a></code>(3) first tries to load the configuration files by searching the directories in <code>GCONV_PATH</code> in order, followed by the system default gconv module configuration file. If a directory does not contain a gconv module configuration file, any gconv modules that it may contain are ignored. If a directory contains a gconv module configuration file and it is determined that a module needed for this conversion is available in the directory, then the needed module is loaded from that directory, the order being such that the first suitable module found in <code>GCONV_PATH</code> is used. This allows users to use custom modules and even replace system-provided modules by providing such modules in <code>GCONV_PATH</code> directories.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/lib/gconv</i></p>
<dd> Usual default gconv module path.</p>
<dt><i>/usr/lib/gconv/gconv-modules</i></p>
<dd> Usual system default gconv module configuration file.</p>
<dt><i>/usr/lib/gconv/gconv-modules.cache</i></p>
<dd> Usual system gconv module configuration cache.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001.</p>
<h2>EXAMPLES</h2>
<p> Convert text from the ISO 8859-15 character encoding to UTF-8: </p>
<p> $ <code>iconv -f ISO-8859-15 -t UTF-8 &lt; input.txt &gt; output.txt</code> </p>
<p> The next example converts from UTF-8 to ASCII, transliterating when possible: </p>
<p> $ <code>echo abc ß α € àḃç | iconv -f UTF-8 -t ASCII//TRANSLIT</code> abc ss ? EUR abc</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/1-uconv/">uconv</a></code>(1), <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3), <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3), <code><a href="/docs/linux/man/7-charsets/">charsets</a></code>(7), <code><a href="/docs/linux/man/8-iconvconfig/">iconvconfig</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
