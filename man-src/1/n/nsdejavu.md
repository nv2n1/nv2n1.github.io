---
title: "nsdejavu(1)"
name: "nsdejavu"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nsdejavu/"
description: "nsdejavu – DjVu browser plugin"
---

<h2 class="name">NAME</h2>
<p> nsdejavu &#8211; DjVu browser plugin</p>
<h2>SYNOPSIS</h2>
<p> <code>/usr/lib/mozilla/plugins/nsdejavu.so</code> or<br />
 <code>/usr/lib64/mozilla/plugins/nsdejavu.so</code> </p>
<h2>DESCRIPTION</h2>
<p> The shared library <code>nsdejavu.so</code> uses the Netscape browser plugin <font SIZE="-1">API</font> to display DjVu images in in a number of popular web browsers. Different web browsers provide various level of support for Netscape plugins. Please check section &quot;Browser Compatibility&quot; for instructions on how to enable the DjVu browser plugin. </p>
<p> The DjVuLibre browser plugin works by invoking a standalone viewer with the special command line option <code>-netscape</code>. The plugin first searches a program named <code>djview</code>. If this program cannot be found, it searches for <code>djview4</code> and finally <code>djview3.</code> It is always possible to override this search strategy by setting the environment variable <code>NPX_DJVIEW</code> to the full path of the desired executable. </p>
<h2>MIME TYPES AND EXTENSIONS</h2>
<p> Typing the <font SIZE="-1">URL</font> of a recognized DjVu document in your web browser should automatically invoke the DjVu browser plugin. Each browser uses different methods to determine that a particular <font SIZE="-1">URL</font> is in fact a DjVu document. Web server normally provide a <font SIZE="-1">MIME</font> type to web browsers. The official <font SIZE="-1">MIME </font> type for DjVu documents is <code>image/vnd.djvu</code>. For compatibility with ancient versions of the DjVu viewer, it is common to use instead the experimental <font SIZE="-1">MIME </font> type <code>image/x-djvu</code> or <code>image/x.djvu</code>. Web servers should be configured to send the proper <font SIZE="-1">MIME </font> type for DjVu documents. Most web browsers also recognize files ending with <code>.djvu</code> or <code>.djv</code> as DjVu files. </p>
<p> An easy way to check if an http server is giving an appropriate content-type is to invoke the following command with a <font SIZE="-1">URL</font> corresponding to an actual DjVu file on the server.</p>
<dl>
<dt>
<dd> <code>curl -u </code><i>URL</i><code> | grep Content-Type</code></dl>
<p> The result should be one of the following, preferably the first.</p>
<dl>
<dt>
<dd> <code>Content-Type: image/vnd.djvu</code><br />
 <code>Content-Type: image/x.djvu</code><br />
 <code>Content-Type: image/x-djvu</code></dl>
<p> Any other <font SIZE="-1">MIME </font> type indicates a server misconfiguration. </p>
<h2>CGI-STYLE FLAGS</h2>
<p> The behavior of the DjVu browser plugin can be specified by augmenting the <font SIZE="-1">URL</font> using a syntax similar to that used by the <font SIZE="-1">CGI</font> programs. This syntax is described by the following template:</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://.../file.djvu?djvuopts">http://&#8230;/file.djvu?djvuopts</a>&amp;</code><i>keyword=value</i><code>&amp;</code><i>keyword=value</i><code>&amp;</code><i>&#8230;</i></dl>
<p> The DjVu browser plugin only recognizes keywords that appear after the word <code>djvuopts</code>. The keywords recognized by each viewer are listed in the man pages for <code><a href="/docs/linux/man/1-djview3/">djview3</a></code>(1) and <code><a href="/docs/linux/man/1-djview4/">djview4</a></code>(1) Unrecognized keywords are ignored. The most common keywords are:</p>
<dl>
<dt><code>page=</code><i>pagenum_or_pagename</i></p>
<dd> Specify the initial page to be displayed. Page numbers are numbered from 1.</p>
<dt><code>zoom=</code><i>zoomfactor</i></p>
<dd> Specify the initial zoom factor. Legal values for <i>zoomfactor</i> are shown in the below:<br />
 <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><i>number</i></td>
<td>Magnification factor in range 10% to 999%.
</td>
</tr>
<tr VALIGN=top>
<td><code>one2one</code></td>
<td>Select the &quot;one-to-one&quot; mode.
</td>
</tr>
<tr VALIGN=top>
<td><code>width</code></td>
<td>Select the &quot;fit width&quot; mode.
</td>
</tr>
<tr VALIGN=top>
<td><code>page</code></td>
<td>Select the &quot;fit page&quot; mode.
</td>
</tr>
<tr VALIGN=top>
<td><code>stretch</code></td>
<td>Stretch the image to the plugin window size.
</td>
</tr>
</table>
</table>
<p></center> </p>
</dl>
<h2>EMBEDDING DJVU IMAGES IN HTML PAGES</h2>
<p> You can integrate DjVu content on an <font SIZE="-1">HTML</font> web page with the <font SIZE="-1">&lt;embed&gt;</font> tag. This method is that it will work even if your web server does not support the DjVu <font SIZE="-1">MIME</font> type. The <font SIZE="-1">CGI</font> style flags can be directly used as attributes of the embedding tag. The following example shows the W3C standard syntax with the <font SIZE="-1">OBJECT </font> tag:</p>
<dl>
<dt>
<dd> <code>&lt;object data=myfile.djvu type=image/x-djvu</code><br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> width=100% height=100% &gt;</code><br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> &lt;param name=page value=iii&gt;</code><br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> &lt;param name=zoom value=stretch&gt;</code><br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> This browser cannot render djvu data.</code><br />
 <code>&lt;/object&gt;</code></dl>
<p> And this is the customary syntax with the <font SIZE="-1">EMBED</font> tag:</p>
<dl>
<dt>
<dd> <code>&lt;embed src=myfile.djvu type=image/x-djvu</code><br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> width=100% height=100%</code><br />
 <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> page=iii zoom=stretch&gt;&lt;/embed&gt;</code></dl>
<h2>BROWSER COMPATIBILITY</h2>
<p> The DjVu browser plugin has been tested with several popular web browsers:</p>
<h3>MOZILLA</h3>
<p> The DjVuLibre plugin works nicely with Mozilla 0.9.5 or better. </p>
<p> Start <code>mozilla</code> and select menu <code>Help-&gt;About Plugins</code> to check whether the DjVuLibre plugin is properly recognized. </p>
<h3>FIREFOX</h3>
<p> The DjVuLibre plugin works nicely with Firefox or better. </p>
<p> Start <code>firefox</code> and enter the address <code>about:plugins</code> to check whether the DjVuLibre plugin is properly recognized. </p>
<h3>GALEON</h3>
<p> Galeon internally uses the Mozilla rendering engine. If the plugin works for Mozilla, it should also work for Galeon. </p>
<h3>NETSCAPE 6</h3>
<p> The DjVuLibre plugin works nicely with Netscape 6.1 or better. It seems that Netscape 6 only recognize plugins installed inside its own plugin directory. This can be done using a symbolic link. Let us assume that Netscape 6 is installed in <i>/usr/local/netscape6</i>. The following commands should do the trick:</p>
<dl>
<dt>
<dd> <code>cd </code><i>/usr/local/netscape6/plugins</i><br />
 <code>ln -s /usr/lib/mozilla/plugins/nsdejavu.so .</code><br />
 ( or <code>ln -s /usr/lib64/mozilla/plugins/nsdejavu.so .</code> )</dl>
<h3>KONQUEROR</h3>
<p> The DjVuLibre plugin works with <font SIZE="-1">KDE-2.2</font> or better. You must first make sure that <code>konqueror</code> recognizes the DjVU plugin. In Konqueror, select <code>Settings-&gt;Configure Konqueror</code>. When the dialog appears, select the icon <code>Netscape Plugins</code>. Make sure that directory <code>/usr/lib/mozilla/plugins</code> (or <code>/usr/lib64/mozilla/plugins</code> ) appears in the list of plugin directories. Then press button <code>Scan for new plugins</code>. Clicking the <code>Plugins</code> tab button should display a list of recognized plugins. Check that <code>nsdejavu.so</code> appears there. </p>
<h3>OPERA</h3>
<p> The DjVuLibre plugin works with Opera-6. As explained in the Opera software support pages, you must have the OpenMotif libraries installed. </p>
<h2>CREDITS</h2>
<p> This program was written by Andrei Erofeev &lt;andrew_erofeev [at] yahoo.com&gt; and was then improved by Bill Riemers &lt;docbill [at] sourceforge.net&gt; and L&#8217;eon Bottou &lt;leonb [at] users.sourceforge.net&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/1-ddjvu/">ddjvu</a></code>(1), <code><a href="/docs/linux/man/1-djview4/">djview4</a></code>(1) <code><a href="/docs/linux/man/1-djview3/">djview3</a></code>(1) </p>
<h2>Index</h2>
