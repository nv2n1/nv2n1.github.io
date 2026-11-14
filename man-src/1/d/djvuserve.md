---
title: "djvuserve(1)"
name: "djvuserve"
section: "1"
letter: "d"
url: "/docs/linux/man/1-djvuserve/"
description: "djvuserve – Generate indirect DjVu documents on the fly."
---

<h2>NAME</h2>
<p> djvuserve &#8211; Generate indirect DjVu documents on the fly. </p>
<h2>DESCRIPTION</h2>
<p> Program <code>djvuserve </code> is a <font SIZE="-1">CGI</font> program that can be executed by a <font SIZE="-1">HTTP </font> server for serving DjVu documents. This program is able to convert a bundled multi-page document into an indirect document on the fly. </p>
<h2>USING DJVUSERVE</h2>
<p> Program <code>djvuserve</code> must first be installed as a <font SIZE="-1">CGI</font> program for your web server. There are several ways to achieve this. The Apache web server, for instance, often defines a specific directory for <font SIZE="-1">CGI </font> programs using the <code>ScriptAlias</code> directive. Assume that the file <code>httpd.conf</code> contains the following line:</p>
<dl>
<dt>
<dd> <code>ScriptAlias /cgi-bin/ </code><i>&quot;/var/www/cgi-bin&quot;</i></dl>
<p> It is then sufficient to create a small executable shell script <i>/var/www/cgi-bin/</i><code>djvuserve</code> containing the following lines:</p>
<dl>
<dt>
<dd> <code>#!/bin/sh</code><br />
 <code>exec </code><i>/full/path/to/</i><code>djvuserve</code></dl>
<p> Suppose that a large bundled multi-page DjVu document is available at the following <font SIZE="-1">URL.</font></p>
<dl>
<dt>
<dd> <i>http</i><i>://server/dir/doc.djvu</i></dl>
<p> The <font SIZE="-1">CGI </font> program <code>djvuserve</code> lets you access this same document as an indirect multi-page DjVu document using the following <font SIZE="-1">URL.</font></p>
<dl>
<dt>
<dd> <i>http</i><i>://server</i><code>/cgi-bin/djvuserve/</code><i>dir/doc.djvu</i><code>/index.djvu</code></dl>
<p> Serving indirect multi-page DjVu documents provides for efficiently browsing large document without transferring unnecessary pages over the network. See <code><a href="/docs/linux/man/1-djvu/">djvu</a>(1)</code> for more information. </p>
<p> Furthermore <code>djvuserve </code> searches certain keywords among the <font SIZE="-1">CGI </font> arguments of the <font SIZE="-1">URL.</font> The keyword <code>bundled</code> forces serving a bundled document using</p>
<dl>
<dt>
<dd> <i>http</i><i>://server</i><code>/cgi-bin/djvuserve/</code><i>dir/doc.djvu</i><code>?bundled</code></dl>
<p> The keyword <code>download</code> inserts a content disposition <font SIZE="-1">HTTP</font> header that suggests to display a save dialog instead of displaying the document.</p>
<dl>
<dt>
<dd> <i>http</i><i>://server</i><code>/cgi-bin/djvuserve/</code><i>dir/doc.djvu</i><code>?download</code></dl>
<h2>USING DJVUSERVE AS A HANDLER</h2>
<p> The Apache web server provides a way to automatically execute <code>djvuserve</code> for all DjVu documents. This can be achieved using the following directives in either the Apache configuration file or the <code>.htaccess</code> files.</p>
<dl>
<dt>
<dd> <code>Action djvu-server /cgi-bin/djvuserve/</code><br />
 <code>AddHandler djvu-server .djvu</code></dl>
<p> Apache then executes program <code>djvuserve</code> for serving all DjVu files. Providing the <font SIZE="-1">URL</font> of DjVu file serves this DjVu file as usual, except that bundled multipage documents are converted to indirect documents on the fly. This convenience comes at the expense of the computational cost of executing <code>djvuserve</code> whenever a DjVu file is requested. </p>
<h2>TECHNICAL DETAILS</h2>
<p> Program <code>djvuserve</code> provides a mean to directly access any component of a bundled multi-page DjVu document can be accessed using an extended <font SIZE="-1">URL.</font> Suppose that the component file representing page 1 is named <code>p0001.djvu</code>. The following <font SIZE="-1">URL</font> provides a direct access to this page:</p>
<dl>
<dt>
<dd> <i>http</i><i>://server</i><code>/cgi-bin/djvuserve/</code><i>dir/doc.djvu</i><code>/p0001.djvu</code></dl>
<p> It is preferred however to access individual pages using the <code>CGI</code> style arguments described in <code><a href="/docs/linux/man/1-nsdejavu/">nsdejavu</a></code>(1), as in the following <font SIZE="-1">URL.</font></p>
<dl>
<dt>
<dd> <i>http</i><i>://server</i><code>/cgi-bin/djvuserve/</code><i>dir/doc.djvu</i><code>?djvuopts&amp;page=12</code></dl>
<p> The special component file name <code>index.djvu</code> is recognized as a request for the index of the corresponding indirect multi-page document. In fact, when you access a bundled document using <code>djvuserve</code>, the browser gets redirected to the following <font SIZE="-1">URL:</font></p>
<dl>
<dt>
<dd> <i>http</i><i>://server</i><code>/cgi-bin/djvuserve/</code><i>dir/doc.djvu</i><code>/index.djvu</code></dl>
<p> and then behaves as if the bundled file was a directory containing the various component files of an equivalent indirect document. </p>
<h2>ACCESS CONTROL</h2>
<p> Program <code>djvuserve</code>, like many <font SIZE="-1">CGI</font> programs, bypasses a number of access protections established in a web server. Assume for instance that your web site contains DjVu files protected by a password. Program <code>djvuserve</code> knows nothing about this protection and will happily serve any DjVu file associated with a valid <font SIZE="-1">URL.</font> </p>
<p> Access control with <code>djvuserve </code> can be implemented by first remembering that the web server always executes program <code>djvuserve</code> via shell script <i>/var/www/cgi-bin/</i><code>djvuserve.</code> </p>
<p> This script can decide to execute the real program <code>djvuserve</code> on the basis of the target filename available in the environment variable <font SIZE="-1">PATH_TRANSLATED. </font> </p>
<p> There can be several such scripts providing access to various collections of DjVu files. Each of these scripts can be password protected using the usual methods supported by your web server. </p>
<h2>KNOWN BUGS</h2>
<p> Hyperlinks specified using a relative <font SIZE="-1">URL </font> may not work with <code>djvuserve.</code> These <font SIZE="-1">URLs </font> are relative to the <font SIZE="-1">URL </font> of the DjVu document. Yet <code>djvuserve</code> changes the apparent document <font SIZE="-1">URL</font> <i><a rel="nofollow" href="http://server/dir/doc.djvu">http://server/dir/doc.djvu</a></i> into the more complicated <font SIZE="-1">URL</font> <i><a rel="nofollow" href="http://server">http://server</a></i><code>/cgi-bin/djvuserve/</code><i>dir/doc.djvu</i><code>/index.djvu.</code> The extra components change the interpretation of relative <font SIZE="-1">URLs.</font> </p>
<h2>CREDITS</h2>
<p> This program was written by Leon Bottou &lt;leonb [at] users.sourceforge.com&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/1-djvmcvt/">djvmcvt</a></code>(1), <code><a href="/docs/linux/man/1-nsdejavu/">nsdejavu</a></code>(1) </p>
<h2>Index</h2>
