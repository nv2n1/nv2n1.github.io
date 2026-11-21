---
title: "w3m(1)"
name: "w3m"
section: "1"
letter: "w"
url: "/docs/linux/man/1-w3m/"
description: "w3m – a text based web browser and pager"
---

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
<dt><code>-B</code></dt>
<dd> with no other target defined, use the bookmark page for startup</dd>
<dt><code>-M</code></dt>
<dd> monochrome display</dd>
<dt><code>-no-mouse</code></dt>
<dd> deactivate mouse support</dd>
<dt><code>-num</code></dt>
<dd> display each line&#8217;s number</dd>
<dt><code>-N</code></dt>
<dd> distribute multiple command line arguments to tabs. By default, a stack of buffers is used</dd>
<dt><code>-ppc </code><i>num</i></dt>
<dd> width of <i>num</i> pixels per character. Range of 4.0 to 32.0, default 8.0. Larger values will make tables narrower. (Implementation not verified)</dd>
<dt><code>-ppl </code><i>num</i></dt>
<dd> height of <i>num</i> pixels per line. Range of 4.0 to 64.0. (Implementation not verified)</dd>
<dt><code>-title</code>, <code>-title=TERM</code></dt>
<dd> use the buffer name as terminal title string. With specified TERM, this sets the title configuration style accordingly</dd>
<dt><code>-v</code></dt>
<dd> with no other target defined, welcome users with a built-in page</dd>
<dt><code>-W</code></dt>
<dd> toggle wrapping mode in searches</dd>
<dt><code>-X</code></dt>
<dd> do not initialize/deinitialize the terminal</dd>
<dt><code>+</code><i>num</i></dt>
<dd> go to line <i>num</i>; only effective for <i>num</i> larger than the number of lines in the terminal</dd></dl>
<h3>Browser options</h3>
<dl>
<dt><code>-cols </code><i>num</i></dt>
<dd> with stdout as destination; HTML is rendered to lines of <i>num</i> characters</dd>
<dt><code>-cookie</code>, <code>-no-cookie</code></dt>
<dd> use stored cookies and accept new ones, or do neither</dd>
<dt><code>-F</code></dt>
<dd> render frames</dd>
<dt><code>-graph</code>, <code>-no-graph</code></dt>
<dd> use or do not use graphic characters for drawing HTML table and frame borders</dd>
<dt><code>-header </code><i>string</i></dt>
<dd> append <i>string</i> to the HTTP(S) request. Expected to match the header syntax <tt>Variable: Value</tt></dd>
<dt><code>-m</code></dt>
<dd> Render the body of Usenet messages according to the header &#8220;Content-type&#8221;</dd>
<dt><code>-no-proxy</code></dt>
<dd> do not use proxy</dd>
<dt><code>-post </code><i>file</i></dt>
<dd> use POST method to upload data defined in <i>file</i>. The syntax to be used is <tt>var1=value1[&amp;var2=value2]...</tt></dd>
<dt><code>-4</code></dt>
<dd> IPv4 only. Corresponds to dns_order=4 in configuration files</dd>
<dt><code>-6</code></dt>
<dd> IPv6 only. Corresponds to dns_order=6 in configuration files</dd></dl>
<h3>Text pager options</h3>
<dl>
<dt><code>-l </code><i>num</i></dt>
<dd> number of lines preserved internally when receiving plain text from stdin (default 10,000)</dd>
<dt><code>-r</code></dt>
<dd> use caret notation to display special escape characters (such as ANSI escapes or nroff-style backspaces for bold and underlined characters) instead of processing them</dd>
<dt><code>-s</code></dt>
<dd> squeeze multiple blank lines into one</dd>
<dt><code>-t</code> <i>num</i></dt>
<dd> set tab width to <i>num</i> columns. No effect on stdout</dd></dl>
<h3>Data type/encoding options</h3>
<dl>
<dt><code>-I </code><i>charset</i></dt>
<dd> user defined character encoding of input data</dd>
<dt><code>-O </code><i>charset</i></dt>
<dd> user defined character encoding of output data</dd>
<dt><code>-T </code><i>type</i></dt>
<dd> explicit characterization of input data by MIME type</dd></dl>
<h3>Options for data output, followed by immediate exit</h3>
<dl>
<dt><code>-dump</code></dt>
<dd> dump rendered page into stdout. Set implicitly when output is directed to a file or pipe</dd>
<dt><code>-dump_source</code></dt>
<dd> dump the page&#8217;s source code into stdout</dd>
<dt><code>-dump_head</code></dt>
<dd> dump response of a HEAD request for a URL into stdout</dd>
<dt><code>-dump_both</code></dt>
<dd> dump HEAD, and source code for a URL into stdout</dd>
<dt><code>-dump_extra</code></dt>
<dd> dump HEAD, source code, and extra information for a URL into stdout</dd>
<dt><code>-help</code></dt>
<dd> show a summary of compiled-in features and command line options</dd>
<dt><code>-show-option</code></dt>
<dd> show all available configuration options</dd>
<dt><code>-version</code></dt>
<dd> show the version of <i>w3m</i></dd></dl>
<h3>Options for overriding default settings and resources</h3>
<dl>
<dt><code>-bookmark </code><i>file</i></dt>
<dd> use <i>file</i> instead of the default bookmark.html file</dd>
<dt><code>-config </code><i>file</i></dt>
<dd> use <i>file</i> instead of the default configuration file</dd>
<dt><code>-debug</code></dt>
<dd> DO NOT USE</dd>
<dt><code>-o </code><i>option=value</i></dt>
<dd> modify one configuration item with an explicitly given value; without <i>option=value</i>, equivalent to <code>-show-option</code></dd>
<dt><code>-reqlog</code></dt>
<dd> log headers of HTTP communication in file <tt>~/.w3m/request.log</tt></dd></dl>
<h2>EXAMPLES</h2>
<h3>Pager-like usage</h3>
<dl>
<dt>Combine snippets of HTML code and preview the page</dt>
<dd> $ cat header.html footer.html | w3m -T text/html</dd>
<dt>Compare two files using tabs</dt>
<dd> $ w3m -N config.old config</dd></dl>
<h3>Browser-like usage</h3>
<dl>
<dt>Display web content in monochrome terminal</dt>
<dd> $ w3m -M <a rel="nofollow" href="http://w3m.sourceforge.net">http://w3m.sourceforge.net</a></dd>
<dt>Display embedded graphics</dt>
<dd> $ w3m -o auto_image=TRUE <a rel="nofollow" href="http://w3m.sourceforge.net">http://w3m.sourceforge.net</a></dd>
<dt>Display content from Usenet</dt>
<dd> $ w3m -m <a href="nntp://news.aioe.org/comp.os.linux.networking">nntp://news.aioe.org/comp.os.linux.networking</a></dd>
<dt>Upload data for a URL using the POST method</dt>
<dd> $ w3m -post &#8211; <a rel="nofollow" href="http://example.com/form.php">http://example.com/form.php</a> &lt;&lt;&lt;&#8216;a=0&amp;b=1&#8217;</dd></dl>
<h3>Filter-like usage</h3>
<dl>
<dt>Convert an HTML file to plain text with a defined line length</dt>
<dd> $ w3m -cols 40 foo.html &gt; foo.txt</dd>
<dt>Output the bookmarks page as text with an appended list of links</dt>
<dd> $ w3m -B -o display_link_number=1 &gt; out.txt</dd>
<dt>Conversion of file format and character encoding</dt>
<dd> $ w3m -T text/html -I EUC-JP -O UTF-8 &lt; foo.html &gt; foo.txt</dd></dl>
<h3>Start with no input</h3>
<dl>
<dt>Welcome users with a built-in page</dt>
<dd> $ w3m -v</dd></dl>
<h2>ENVIRONMENT</h2>
<p> <i>w3m</i> recognises the environment variable WWW_HOME as defining a fallback target for use if it is invoked without one.</p>
<h2>FILES</h2>
<dl>
<dt><tt>~/.w3m/bookmark.html</tt></dt>
<dd> default bookmark file</dd>
<dt><tt>~/.w3m/config</tt></dt>
<dd> user defined configuration file; overrides <tt>/etc/w3m/config</tt></dd>
<dt><tt>~/.w3m/cookie</tt></dt>
<dd> cookie jar; written on exit, read on launch</dd>
<dt><tt>~/.w3m/history</tt></dt>
<dd> browser history &#8211; visited files and URLs</dd>
<dt><tt>~/.w3m/keymap</tt></dt>
<dd> user defined key bindings; overrides default key bindings</dd>
<dt><tt>~/.w3m/mailcap</tt></dt>
<dd> external viewer configuration file</dd>
<dt><tt>~/.w3m/menu</tt></dt>
<dd> user defined menu; overrides default menu</dd>
<dt><tt>~/.w3m/mime.types</tt></dt>
<dd> MIME types file</dd>
<dt><tt>~/.w3m/mouse</tt></dt>
<dd> user defined mouse settings</dd>
<dt><tt>~/.w3m/passwd</tt></dt>
<dd> password and username file</dd>
<dt><tt>~/.w3m/pre_form</tt></dt>
<dd> contains predefined values to fill recurrent HTML forms</dd></dl>
<h2>SEE ALSO</h2>
<p> README and example files are to be found in the doc directory of your <i>w3m</i> installation. Recent information about <i>w3m</i> may be found on the project&#8217;s web pages at</p>
<h2>ACKNOWLEDGMENTS</h2>
<p> <i>w3m</i> has incorporated code from several sources. Users have contributed patches and suggestions over time.</p>
<h2>AUTHOR</h2>
<p> Akinori ITO </p>
