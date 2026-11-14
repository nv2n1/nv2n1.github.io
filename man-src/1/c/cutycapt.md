---
title: "cutycapt(1)"
name: "cutycapt"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cutycapt/"
description: "cutycapt – utility to capture WebKit’s rendering of a web page"
---

<h2 class="name">NAME</h2>
<p> cutycapt &#8211; utility to capture WebKit&#8217;s rendering of a web page </p>
<h2>SYNOPSIS</h2>
<p> <code>cutycapt</code> [<i>options</i>] <code>&#8211;url=</code><i><a rel="nofollow" href="http://www.someurl.com">http://www.someurl.com</a></i> <code>&#8211;out=</code><i>output.png</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>cutycapt</code> command. </p>
<p> <code>CutyCapt</code> is a small cross-platform command-line utility to capture WebKit&#8217;s rendering of a web page into a variety of vector and bitmap formats, including SVG, PDF, PS, PNG, JPEG, TIFF, GIF, and BMP.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;url=</code><i>&lt;url&gt;</i></p>
<dd> The URL to capture (http:&#8230;|file:&#8230;|&#8230;)</p>
<dt><code>&#8211;out=</code><i>&lt;path&gt;</i></p>
<dd> The target file (.png|pdf|ps|svg|jpeg|&#8230;)</p>
<dt><code>&#8211;out-format=</code><i>&lt;f&gt;</i></p>
<dd> Like extension in <code>&#8211;out, overrides heuristic</p>
<dt>&#8211;min-width=</code><i>&lt;int&gt;</i></p>
<dd> Minimal width for the image (default: 800)</p>
<dt><code>&#8211;min-height=</code><i>&lt;int&gt;</i></p>
<dd> Minimal height for the image (default: 600)</p>
<dt><code>&#8211;max-wait=</code><i>&lt;ms&gt;</i></p>
<dd> Don&#8217;t wait more than (default: 90000, infinite: 0)</p>
<dt><code>&#8211;delay=</code><i>&lt;ms&gt;</i></p>
<dd> After successful load, wait (default: 0)</p>
<dt><code>&#8211;user-style-path=</code><i>&lt;path&gt;</i></p>
<dd> Location of user style sheet file, if any</p>
<dt><code>&#8211;user-style-string=</code><i>&lt;css&gt;</i></p>
<dd> User style rules specified as text</p>
<dt><code>&#8211;header=</code><i>&lt;name&gt;</i><code>:</code><i>&lt;value&gt;</i></p>
<dd> Request header; repeatable; some can&#8217;t be set</p>
<dt><code>&#8211;method=</code><i>&lt;get|post|put&gt;</i></p>
<dd> Specifies the request method (default: get)</p>
<dt><code>&#8211;body-string=</code><i>&lt;string&gt;</i></p>
<dd> Unencoded request body (default: none)</p>
<dt><code>&#8211;body-base64=</code><i>&lt;base64&gt;</i></p>
<dd> Base64-encoded request body (default: none)</p>
<dt><code>&#8211;app-name=</code><i>&lt;name&gt;</i></p>
<dd> Application name used in User-Agent; default is none</p>
<dt><code>&#8211;app-version=</code><i>&lt;version&gt;</i></p>
<dd> Application version used in User-Agent; default is none</p>
<dt><code>&#8211;user-agent=</code><i>&lt;string&gt;</i></p>
<dd> Override the User-Agent header Qt would set</p>
<dt><code>&#8211;javascript=</code><i>&lt;on|off&gt;</i></p>
<dd> JavaScript execution (default: on)</p>
<dt><code>&#8211;java=</code><i>&lt;on|off&gt;</i></p>
<dd> Java execution (default: unknown)</p>
<dt><code>&#8211;plugins=</code><i>&lt;on|off&gt;</i></p>
<dd> Plugin execution (default: unknown)</p>
<dt><code>&#8211;private-browsing=</code><i>&lt;on|off&gt;</i></p>
<dd> Private browsing (default: unknown)</p>
<dt><code>&#8211;auto-load-images=</code><i>&lt;on|off&gt;</i></p>
<dd> Automatic image loading (default: on)</p>
<dt><code>&#8211;js-can-open-windows=</code><i>&lt;on|off&gt;</i></p>
<dd> Script can open windows? (default: unknown)</p>
<dt><code>&#8211;js-can-access-clipboard=</code><i>&lt;on|off&gt;</i></p>
<dd> Script clipboard privs (default: unknown)</p>
<dt><code>&#8211;print-backgrounds=</code><i>&lt;on|off&gt;</i></p>
<dd> Backgrounds in PDF/PS output (default: off)</p>
<dt><code>&#8211;zoom-factor=</code><i>&lt;float&gt;</i></p>
<dd> Page zoom factor (default: no zooming)</p>
<dt><code>&#8211;zoom-text-only=</code><i>&lt;on|off&gt;</i></p>
<dd> Whether to zoom only the text (default: off)</p>
<dt><code>&#8211;http-proxy=</code><i>&lt;url&gt;</i></p>
<dd> Address for HTTP proxy server (default: none)</dl>
<h2>AUTHOR</h2>
<p> CutyCapt was written by Björn Höhrmann &lt;bjoern [at] hoehrmann.de&gt;. </p>
<p> This manual page was written by David Paleino &lt;dapal [at] debian.org&gt;, for the Debian project (and may be used by others), and is licensed under the GNU General Public License, version 2 or later. </p>
<h2>Index</h2>
