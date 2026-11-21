---

title: "cutycapt(1)"
name: "cutycapt"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cutycapt/"
description: "cutycapt – utility to capture WebKit’s rendering of a web page"
---

<p> cutycapt &#8211; utility to capture WebKit&#8217;s rendering of a web page </p>
<h2>SYNOPSIS</h2>
<p> <code>cutycapt</code> [<i>options</i>] <code>&#8211;url=</code><i><a rel="nofollow" href="http://www.someurl.com">http://www.someurl.com</a></i> <code>&#8211;out=</code><i>output.png</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>cutycapt</code> command. </p>
<p> <code>CutyCapt</code> is a small cross-platform command-line utility to capture WebKit&#8217;s rendering of a web page into a variety of vector and bitmap formats, including SVG, PDF, PS, PNG, JPEG, TIFF, GIF, and BMP.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>&#8211;url=</code><i>&lt;url&gt;</i></dt>
<dd> The URL to capture (http:&#8230;|file:&#8230;|&#8230;)</dd>
<dt><code>&#8211;out=</code><i>&lt;path&gt;</i></dt>
<dd> The target file (.png|pdf|ps|svg|jpeg|&#8230;)</dd>
<dt><code>&#8211;out-format=</code><i>&lt;f&gt;</i></dt>
<dd> Like extension in <code>&#8211;out, overrides heuristic</dd>
<dt>&#8211;min-width=</code><i>&lt;int&gt;</i></dt>
<dd> Minimal width for the image (default: 800)</dd>
<dt><code>&#8211;min-height=</code><i>&lt;int&gt;</i></dt>
<dd> Minimal height for the image (default: 600)</dd>
<dt><code>&#8211;max-wait=</code><i>&lt;ms&gt;</i></dt>
<dd> Don&#8217;t wait more than (default: 90000, infinite: 0)</dd>
<dt><code>&#8211;delay=</code><i>&lt;ms&gt;</i></dt>
<dd> After successful load, wait (default: 0)</dd>
<dt><code>&#8211;user-style-path=</code><i>&lt;path&gt;</i></dt>
<dd> Location of user style sheet file, if any</dd>
<dt><code>&#8211;user-style-string=</code><i>&lt;css&gt;</i></dt>
<dd> User style rules specified as text</dd>
<dt><code>&#8211;header=</code><i>&lt;name&gt;</i><code>:</code><i>&lt;value&gt;</i></dt>
<dd> Request header; repeatable; some can&#8217;t be set</dd>
<dt><code>&#8211;method=</code><i>&lt;get|post|put&gt;</i></dt>
<dd> Specifies the request method (default: get)</dd>
<dt><code>&#8211;body-string=</code><i>&lt;string&gt;</i></dt>
<dd> Unencoded request body (default: none)</dd>
<dt><code>&#8211;body-base64=</code><i>&lt;base64&gt;</i></dt>
<dd> Base64-encoded request body (default: none)</dd>
<dt><code>&#8211;app-name=</code><i>&lt;name&gt;</i></dt>
<dd> Application name used in User-Agent; default is none</dd>
<dt><code>&#8211;app-version=</code><i>&lt;version&gt;</i></dt>
<dd> Application version used in User-Agent; default is none</dd>
<dt><code>&#8211;user-agent=</code><i>&lt;string&gt;</i></dt>
<dd> Override the User-Agent header Qt would set</dd>
<dt><code>&#8211;javascript=</code><i>&lt;on|off&gt;</i></dt>
<dd> JavaScript execution (default: on)</dd>
<dt><code>&#8211;java=</code><i>&lt;on|off&gt;</i></dt>
<dd> Java execution (default: unknown)</dd>
<dt><code>&#8211;plugins=</code><i>&lt;on|off&gt;</i></dt>
<dd> Plugin execution (default: unknown)</dd>
<dt><code>&#8211;private-browsing=</code><i>&lt;on|off&gt;</i></dt>
<dd> Private browsing (default: unknown)</dd>
<dt><code>&#8211;auto-load-images=</code><i>&lt;on|off&gt;</i></dt>
<dd> Automatic image loading (default: on)</dd>
<dt><code>&#8211;js-can-open-windows=</code><i>&lt;on|off&gt;</i></dt>
<dd> Script can open windows? (default: unknown)</dd>
<dt><code>&#8211;js-can-access-clipboard=</code><i>&lt;on|off&gt;</i></dt>
<dd> Script clipboard privs (default: unknown)</dd>
<dt><code>&#8211;print-backgrounds=</code><i>&lt;on|off&gt;</i></dt>
<dd> Backgrounds in PDF/PS output (default: off)</dd>
<dt><code>&#8211;zoom-factor=</code><i>&lt;float&gt;</i></dt>
<dd> Page zoom factor (default: no zooming)</dd>
<dt><code>&#8211;zoom-text-only=</code><i>&lt;on|off&gt;</i></dt>
<dd> Whether to zoom only the text (default: off)</dd>
<dt><code>&#8211;http-proxy=</code><i>&lt;url&gt;</i></dt>
<dd> Address for HTTP proxy server (default: none)</dd></dl>
<h2>AUTHOR</h2>
<p> CutyCapt was written by Björn Höhrmann &lt;bjoern [at] hoehrmann.de&gt;. </p>
<p> This manual page was written by David Paleino &lt;dapal [at] debian.org&gt;, for the Debian project (and may be used by others), and is licensed under the GNU General Public License, version 2 or later. </p>
