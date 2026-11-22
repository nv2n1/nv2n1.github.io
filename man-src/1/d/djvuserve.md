---

title: "djvuserve(1)"
name: "djvuserve"
section: "1"
letter: "d"
url: "/docs/linux/man/1-djvuserve/"
description: "djvuserve – Generate indirect DjVu documents on the fly."
---

<p> djvuserve &#8211; Generate indirect DjVu documents on the fly. </p>
<h2>DESCRIPTION</h2>
<p> Program <code>djvuserve </code> is a CGI program that can be executed by a HTTP  server for serving DjVu documents. This program is able to convert a bundled multi-page document into an indirect document on the fly. </p>
<h2>USING DJVUSERVE</h2>
<p> Program <code>djvuserve</code> must first be installed as a CGI program for your web server. There are several ways to achieve this. The Apache web server, for instance, often defines a specific directory for CGI  programs using the <code>ScriptAlias</code> directive. Assume that the file <code>httpd.conf</code> contains the following line:</p>
<dl>
<dt>
</dt><dd> <code>ScriptAlias /cgi-bin/ </code><i>&quot;/var/www/cgi-bin&quot;</i></dd></dl>
<p> It is then sufficient to create a small executable shell script <i>/var/www/cgi-bin/</i><code>djvuserve</code> containing the following lines:</p>
<dl>
<dt>
</dt><dd> <code>#!/bin/sh</code><br/>
 <code>exec </code><i>/full/path/to/</i><code>djvuserve</code></dd></dl>
<p> Suppose that a large bundled multi-page DjVu document is available at the following URL.</p>
<dl>
<dt>
</dt><dd> <i>http</i><i>://server/dir/doc.djvu</i></dd></dl>
<p> The CGI  program <code>djvuserve</code> lets you access this same document as an indirect multi-page DjVu document using the following URL.</p>
<dl>
<dt>
</dt><dd> <i>http</i><i>://server</i><code>/cgi-bin/djvuserve/</code><i>dir/doc.djvu</i><code>/index.djvu</code></dd></dl>
<p> Serving indirect multi-page DjVu documents provides for efficiently browsing large document without transferring unnecessary pages over the network. See <code><a href="/docs/linux/man/1-djvu/">djvu</a>(1)</code> for more information. </p>
<p> Furthermore <code>djvuserve </code> searches certain keywords among the CGI  arguments of the URL. The keyword <code>bundled</code> forces serving a bundled document using</p>
<dl>
<dt>
</dt><dd> <i>http</i><i>://server</i><code>/cgi-bin/djvuserve/</code><i>dir/doc.djvu</i><code>?bundled</code></dd></dl>
<p> The keyword <code>download</code> inserts a content disposition HTTP header that suggests to display a save dialog instead of displaying the document.</p>
<dl>
<dt>
</dt><dd> <i>http</i><i>://server</i><code>/cgi-bin/djvuserve/</code><i>dir/doc.djvu</i><code>?download</code></dd></dl>
<h2>USING DJVUSERVE AS A HANDLER</h2>
<p> The Apache web server provides a way to automatically execute <code>djvuserve</code> for all DjVu documents. This can be achieved using the following directives in either the Apache configuration file or the <code>.htaccess</code> files.</p>
<dl>
<dt>
</dt><dd> <code>Action djvu-server /cgi-bin/djvuserve/</code><br/>
 <code>AddHandler djvu-server .djvu</code></dd></dl>
<p> Apache then executes program <code>djvuserve</code> for serving all DjVu files. Providing the URL of DjVu file serves this DjVu file as usual, except that bundled multipage documents are converted to indirect documents on the fly. This convenience comes at the expense of the computational cost of executing <code>djvuserve</code> whenever a DjVu file is requested. </p>
<h2>TECHNICAL DETAILS</h2>
<p> Program <code>djvuserve</code> provides a mean to directly access any component of a bundled multi-page DjVu document can be accessed using an extended URL. Suppose that the component file representing page 1 is named <code>p0001.djvu</code>. The following URL provides a direct access to this page:</p>
<dl>
<dt>
</dt><dd> <i>http</i><i>://server</i><code>/cgi-bin/djvuserve/</code><i>dir/doc.djvu</i><code>/p0001.djvu</code></dd></dl>
<p> It is preferred however to access individual pages using the <code>CGI</code> style arguments described in <code><a href="/docs/linux/man/1-nsdejavu/">nsdejavu</a></code>(1), as in the following URL.</p>
<dl>
<dt>
</dt><dd> <i>http</i><i>://server</i><code>/cgi-bin/djvuserve/</code><i>dir/doc.djvu</i><code>?djvuopts&amp;page=12</code></dd></dl>
<p> The special component file name <code>index.djvu</code> is recognized as a request for the index of the corresponding indirect multi-page document. In fact, when you access a bundled document using <code>djvuserve</code>, the browser gets redirected to the following URL:</p>
<dl>
<dt>
</dt><dd> <i>http</i><i>://server</i><code>/cgi-bin/djvuserve/</code><i>dir/doc.djvu</i><code>/index.djvu</code></dd></dl>
<p> and then behaves as if the bundled file was a directory containing the various component files of an equivalent indirect document. </p>
<h2>ACCESS CONTROL</h2>
<p> Program <code>djvuserve</code>, like many CGI programs, bypasses a number of access protections established in a web server. Assume for instance that your web site contains DjVu files protected by a password. Program <code>djvuserve</code> knows nothing about this protection and will happily serve any DjVu file associated with a valid URL. </p>
<p> Access control with <code>djvuserve </code> can be implemented by first remembering that the web server always executes program <code>djvuserve</code> via shell script <i>/var/www/cgi-bin/</i><code>djvuserve.</code> </p>
<p> This script can decide to execute the real program <code>djvuserve</code> on the basis of the target filename available in the environment variable PATH_TRANSLATED.  </p>
<p> There can be several such scripts providing access to various collections of DjVu files. Each of these scripts can be password protected using the usual methods supported by your web server. </p>
<h2>KNOWN BUGS</h2>
<p> Hyperlinks specified using a relative URL  may not work with <code>djvuserve.</code> These URLs  are relative to the URL  of the DjVu document. Yet <code>djvuserve</code> changes the apparent document URL <i><a rel="nofollow" href="http://server/dir/doc.djvu">http://server/dir/doc.djvu</a></i> into the more complicated URL <i><a rel="nofollow" href="http://server">http://server</a></i><code>/cgi-bin/djvuserve/</code><i>dir/doc.djvu</i><code>/index.djvu.</code> The extra components change the interpretation of relative URLs. </p>
<h2>CREDITS</h2>
<p> This program was written by Leon Bottou &lt;leonb [at] users.sourceforge.com&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/1-djvmcvt/">djvmcvt</a></code>(1), <code><a href="/docs/linux/man/1-nsdejavu/">nsdejavu</a></code>(1) </p>
