---
title: "w3m(1)"
name: "w3m"
section: "1"
letter: "w"
url: "/docs/linux/man/1-w3m/"
description: "w3m – a text based web browser and pager"
---

<h2 class="name">NAME</h2>
<p> w3m &#8211; a text based web browser and pager </p>
<h2>SYNOPSIS</h2>
<p> w3m [OPTION]&#8230; [ <i>file</i> | <i>URL</i> ]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>w3m</i> is a text based browser which can display local or remote web pages as well as other documents. It is able to process HTML tables and frames but it ignores JavaScript and Cascading Style Sheets. <i>w3m</i> can also serve as a pager for text files named as arguments or passed on standard input, and as a general purpose directory browser. </p>
<p> <i>w3m</i> organizes its content in buffers or tabs, allowing easy navigation between them. With the w3m-img extension installed, <i>w3m</i> can display inline graphics in web pages. And whenever <i>w3m</i>&#8216;s HTML rendering capabilities do not meet your needs, the target URL can be handed over to a graphical browser with a single command. </p>
<p> For help with runtime options, press &#8220;H&#8221; while running <i>w3m</i>. </p>
<h2>ARGUMENTS</h2>
<p> When given one or more command line arguments, <i>w3m</i> will handle targets according to content type. For web, <i>w3m</i> gets this information from HTTP headers; for relative or absolute file system paths, it relies on filenames. </p>
<p> With no argument, <i>w3m</i> expects data from standard input and assumes &#8220;text/plain&#8221; unless another MIME type is given by the user. </p>
<p> If provided with no target and no fallback target (see for instance option <code>-v</code> below), <i>w3m</i> will exit with usage information.</p>
<h2>OPTIONS</h2>
<p> Command line options are introduced with a single &#8220;-&#8221; character and may take an argument.</p>
<h3>General options</h3>
<dl>
<dt><code>-B</code></p>
<dd> with no other target defined, use the bookmark page for startup</p>
<dt><code>-M</code></p>
<dd> monochrome display</p>
<dt><code>-no-mouse</code></p>
<dd> deactivate mouse support</p>
<dt><code>-num</code></p>
<dd> display each line&#8217;s number</p>
<dt><code>-N</code></p>
<dd> distribute multiple command line arguments to tabs. By default, a stack of buffers is used</p>
<dt><code>-ppc </code><i>num</i></p>
<dd> width of <i>num</i> pixels per character. Range of 4.0 to 32.0, default 8.0. Larger values will make tables narrower. (Implementation not verified)</p>
<dt><code>-ppl </code><i>num</i></p>
<dd> height of <i>num</i> pixels per line. Range of 4.0 to 64.0. (Implementation not verified)</p>
<dt><code>-title</code>, <code>-title=TERM</code></p>
<dd> use the buffer name as terminal title string. With specified TERM, this sets the title configuration style accordingly</p>
<dt><code>-v</code></p>
<dd> with no other target defined, welcome users with a built-in page</p>
<dt><code>-W</code></p>
<dd> toggle wrapping mode in searches</p>
<dt><code>-X</code></p>
<dd> do not initialize/deinitialize the terminal</p>
<dt><code>+</code><i>num</i></p>
<dd> go to line <i>num</i>; only effective for <i>num</i> larger than the number of lines in the terminal</dl>
<h3>Browser options</h3>
<dl>
<dt><code>-cols </code><i>num</i></p>
<dd> with stdout as destination; HTML is rendered to lines of <i>num</i> characters</p>
<dt><code>-cookie</code>, <code>-no-cookie</code></p>
<dd> use stored cookies and accept new ones, or do neither</p>
<dt><code>-F</code></p>
<dd> render frames</p>
<dt><code>-graph</code>, <code>-no-graph</code></p>
<dd> use or do not use graphic characters for drawing HTML table and frame borders</p>
<dt><code>-header </code><i>string</i></p>
<dd> append <i>string</i> to the HTTP(S) request. Expected to match the header syntax <tt>Variable: Value</tt></p>
<dt><code>-m</code></p>
<dd> Render the body of Usenet messages according to the header &#8220;Content-type&#8221;</p>
<dt><code>-no-proxy</code></p>
<dd> do not use proxy</p>
<dt><code>-post </code><i>file</i></p>
<dd> use POST method to upload data defined in <i>file</i>. The syntax to be used is <tt>var1=value1[&amp;var2=value2]...</tt></p>
<dt><code>-4</code></p>
<dd> IPv4 only. Corresponds to dns_order=4 in configuration files</p>
<dt><code>-6</code></p>
<dd> IPv6 only. Corresponds to dns_order=6 in configuration files</dl>
<h3>Text pager options</h3>
<dl>
<dt><code>-l </code><i>num</i></p>
<dd> number of lines preserved internally when receiving plain text from stdin (default 10,000)</p>
<dt><code>-r</code></p>
<dd> use caret notation to display special escape characters (such as ANSI escapes or nroff-style backspaces for bold and underlined characters) instead of processing them</p>
<dt><code>-s</code></p>
<dd> squeeze multiple blank lines into one</p>
<dt><code>-t</code> <i>num</i></p>
<dd> set tab width to <i>num</i> columns. No effect on stdout</dl>
<h3>Data type/encoding options</h3>
<dl>
<dt><code>-I </code><i>charset</i></p>
<dd> user defined character encoding of input data</p>
<dt><code>-O </code><i>charset</i></p>
<dd> user defined character encoding of output data</p>
<dt><code>-T </code><i>type</i></p>
<dd> explicit characterization of input data by MIME type</dl>
<h3>Options for data output, followed by immediate exit</h3>
<dl>
<dt><code>-dump</code></p>
<dd> dump rendered page into stdout. Set implicitly when output is directed to a file or pipe</p>
<dt><code>-dump_source</code></p>
<dd> dump the page&#8217;s source code into stdout</p>
<dt><code>-dump_head</code></p>
<dd> dump response of a HEAD request for a URL into stdout</p>
<dt><code>-dump_both</code></p>
<dd> dump HEAD, and source code for a URL into stdout</p>
<dt><code>-dump_extra</code></p>
<dd> dump HEAD, source code, and extra information for a URL into stdout</p>
<dt><code>-help</code></p>
<dd> show a summary of compiled-in features and command line options</p>
<dt><code>-show-option</code></p>
<dd> show all available configuration options</p>
<dt><code>-version</code></p>
<dd> show the version of <i>w3m</i></dl>
<h3>Options for overriding default settings and resources</h3>
<dl>
<dt><code>-bookmark </code><i>file</i></p>
<dd> use <i>file</i> instead of the default bookmark.html file</p>
<dt><code>-config </code><i>file</i></p>
<dd> use <i>file</i> instead of the default configuration file</p>
<dt><code>-debug</code></p>
<dd> DO NOT USE</p>
<dt><code>-o </code><i>option=value</i></p>
<dd> modify one configuration item with an explicitly given value; without <i>option=value</i>, equivalent to <code>-show-option</code></p>
<dt><code>-reqlog</code></p>
<dd> log headers of HTTP communication in file <tt>~/.w3m/request.log</tt></dl>
<h2>EXAMPLES</h2>
<h3>Pager-like usage</h3>
<dl>
<dt>Combine snippets of HTML code and preview the page</p>
<dd> $ cat header.html footer.html | w3m -T text/html</p>
<dt>Compare two files using tabs</p>
<dd> $ w3m -N config.old config</dl>
<h3>Browser-like usage</h3>
<dl>
<dt>Display web content in monochrome terminal</p>
<dd> $ w3m -M <a rel="nofollow" href="http://w3m.sourceforge.net">http://w3m.sourceforge.net</a></p>
<dt>Display embedded graphics</p>
<dd> $ w3m -o auto_image=TRUE <a rel="nofollow" href="http://w3m.sourceforge.net">http://w3m.sourceforge.net</a></p>
<dt>Display content from Usenet</p>
<dd> $ w3m -m <a href="nntp://news.aioe.org/comp.os.linux.networking">nntp://news.aioe.org/comp.os.linux.networking</a></p>
<dt>Upload data for a URL using the POST method</p>
<dd> $ w3m -post &#8211; <a rel="nofollow" href="http://example.com/form.php">http://example.com/form.php</a> &lt;&lt;&lt;&#8216;a=0&amp;b=1&#8217;</dl>
<h3>Filter-like usage</h3>
<dl>
<dt>Convert an HTML file to plain text with a defined line length</p>
<dd> $ w3m -cols 40 foo.html &gt; foo.txt</p>
<dt>Output the bookmarks page as text with an appended list of links</p>
<dd> $ w3m -B -o display_link_number=1 &gt; out.txt</p>
<dt>Conversion of file format and character encoding</p>
<dd> $ w3m -T text/html -I EUC-JP -O UTF-8 &lt; foo.html &gt; foo.txt</dl>
<h3>Start with no input</h3>
<dl>
<dt>Welcome users with a built-in page</p>
<dd> $ w3m -v</dl>
<h2>ENVIRONMENT</h2>
<p> <i>w3m</i> recognises the environment variable WWW_HOME as defining a fallback target for use if it is invoked without one.</p>
<h2>FILES</h2>
<dl>
<dt><tt>~/.w3m/bookmark.html</tt></p>
<dd> default bookmark file</p>
<dt><tt>~/.w3m/config</tt></p>
<dd> user defined configuration file; overrides <tt>/etc/w3m/config</tt></p>
<dt><tt>~/.w3m/cookie</tt></p>
<dd> cookie jar; written on exit, read on launch</p>
<dt><tt>~/.w3m/history</tt></p>
<dd> browser history &#8211; visited files and URLs</p>
<dt><tt>~/.w3m/keymap</tt></p>
<dd> user defined key bindings; overrides default key bindings</p>
<dt><tt>~/.w3m/mailcap</tt></p>
<dd> external viewer configuration file</p>
<dt><tt>~/.w3m/menu</tt></p>
<dd> user defined menu; overrides default menu</p>
<dt><tt>~/.w3m/mime.types</tt></p>
<dd> MIME types file</p>
<dt><tt>~/.w3m/mouse</tt></p>
<dd> user defined mouse settings</p>
<dt><tt>~/.w3m/passwd</tt></p>
<dd> password and username file</p>
<dt><tt>~/.w3m/pre_form</tt></p>
<dd> contains predefined values to fill recurrent HTML forms</dl>
<h2>SEE ALSO</h2>
<p> README and example files are to be found in the doc directory of your <i>w3m</i> installation. Recent information about <i>w3m</i> may be found on the project&#8217;s web pages at</p>
<h2>ACKNOWLEDGMENTS</h2>
<p> <i>w3m</i> has incorporated code from several sources. Users have contributed patches and suggestions over time.</p>
<h2>AUTHOR</h2>
<p> Akinori ITO </p>
<h2>Index</h2>
