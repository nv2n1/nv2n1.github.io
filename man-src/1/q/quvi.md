---
title: "quvi(1)"
name: "quvi"
section: "1"
letter: "q"
url: "/docs/linux/man/1-quvi/"
description: "quvi – query video tool"
---

<h2 class="name">NAME</h2>
<p> quvi &#8211; query video tool </p>
<h2>SYNOPSIS</h2>
<p> quvi [options] [url&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> quvi is a command line tool for parsing video download links. It supports Youtube and other similar video websites.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print help and exit.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Print program version and exit.</p>
<dt><code>&#8211;hosts</code></p>
<dd> Print supported hosts and exit.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Turn off all output.</p>
<dt><code>&#8211;debug</code></p>
<dd> Turn on libcurl verbose mode.</p>
<dt><code>-n, &#8211;no-verify</code></p>
<dd> Do not verify video link. Note that quvi will not report video file length, content-type or file suffix if this option is used.</p>
<dt><code>&#8211;page-title</code>=<i>string</i></p>
<dd> Match parsed video page title to <i>string</i>.</p>
<dt><code>&#8211;video-id</code>=<i>string</i></p>
<dd> Match parsed video <font SIZE="-1">ID</font> to <i>string</i>.</p>
<dt><code>&#8211;file-length</code>=<i>length</i></p>
<dd> Match parsed video file length to <i>length</i>.</p>
<dt><code>&#8211;file-suffix</code>=<i>string</i></p>
<dd> Match parsed video file suffix to <i>string</i>.</p>
<dt><code>-a, &#8211;test-all</code></p>
<dd> Run all built-in tests. quvi will test all built-in video page links.</p>
<dt><code>-t, &#8211;test</code>=<i>pattern</i></p>
<dd> Match <i>pattern</i> to a built-in test page link and test it.</p>
<dt><code>-d, &#8211;dump</code></p>
<dd> Dump video details when running tests. To be used with <code>&#8211;test-all</code>.</p>
<dt><code>&#8211;agent</code>=<i>string</i></p>
<dd> Identify quvi as <i>string</i> to servers. Default is &#8220;Mozilla/5.0&#8221;.</p>
<dt><code>&#8211;proxy</code>=<i>host[:port]</i></p>
<dd> Use the specified <font SIZE="-1">HTTP</font> proxy. Note that quvi will use http_proxy environment setting if it is set.</p>
<dt><code>&#8211;connect-timeout</code>=<i>seconds</i></p>
<dd> Maximum seconds allowed connection to server take. Default is 30.</p>
<dt><code>-f, &#8211;format</code>[=]<i>format_id</i></p>
<dd> Query video format, <i>format_id</i> depends on the host, see <code>&#8211;hosts</code> output.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>quvi <font SIZE="-1">URL</font></p>
<dd> Test <font SIZE="-1">URL</font>.</p>
<dt>quvi -a</p>
<dd> Run all built-in host tests.</p>
<dt>quvi -t youtube</p>
<dd> Match &#8216;youtube&#8217; string to built-in video page links and test it.</p>
<dt>quvi <font SIZE="-1">URL</font> -f best</p>
<dd> Query &#8216;best&#8217; of the video from the <font SIZE="-1">URL</font>.</dl>
<h2>BUGS</h2>
<p> Sure to be some. Please report them. </p>
<pre>
  &lt;<a rel="nofollow" href="http://quvi.googlecode.com/">http://quvi.googlecode.com/</a>&gt;
</pre>
<h2>DEBUGGING</h2>
<dl>
<dt>quvi &#8211;debug <font SIZE="-1">URL</font></p>
<dd> Spew out libcurl verbose mode messages.</p>
<dt>$prefix/share/quvi/lua/README</p>
<dd>
<dt>$prefix/share/quvi/lua/website/README</p>
<dd> Contain details about working with the quvi Lua scripts (e.g. website rules). If video link parsing breaks, have a look at these files.</p>
<dt>$prefix/share/doc/quvi</p>
<dd> Various HOWTOs can be found in this directory.</dl>
<h2>FILES</h2>
<dl>
<dt><code>$HOME/.quvirc</code></p>
<dd> You can define most of the command line options in the config file. For example: </p>
<pre><code>
agent = some_agent / 1.0 #--agent
                         proxy = http : // foo:1234    # --proxy
                                        no -
                                        verify #--no - verify debug #--debug
</code></pre>
<p> Note that you can also define <font SIZE="-1">QUVI_HOME</font> and use it instead.</dl>
<h2>EXIT STATUS</h2>
<p> quvi exits with 0 on success and &gt;0 if an error occurred. </p>
<pre>
  QUVI_OK               = 0x00
  QUVI_MEM              = 0x01, Memory allocation failed
  QUVI_BADHANDLE        = 0x02, Bad session handle
  QUVI_INVARG           = 0x03, Invalid function argument
  QUVI_CURLINIT         = 0x04, libcurl initialization failed
  QUVI_LAST             = 0x05, Indicates end of list iteration
  QUVI_ABORTEDBYCALLBACK= 0x06, Aborted by callback function
  QUVI_LUAINIT          = 0x07, Lua initialization failure
  QUVI_NOLUAWEBSITE     = 0x08, Failed to find lua website scripts
  --
  QUVI_PCRE             = 0x40, libpcre error occurred
  QUVI_NOSUPPORT        = 0x41, libquvi does not support the video host
  QUVI_CURL             = 0x42, libcurl error occurred
  QUVI_ICONV            = 0x43, libiconv error occurred
  QUVI_LUA              = 0x44, lua error occurred
</pre>
<h2>OTHER</h2>
<dl>
<dt>Project page:</p>
<dd> &lt;<a rel="nofollow" href="http://quvi.googlecode.com/">http://quvi.googlecode.com/</a>&gt;</p>
<dt><font SIZE="-1">FAQ:</font></p>
<dd> &lt;<a rel="nofollow" href="http://code.google.com/p/quvi/wiki/FAQ">http://code.google.com/p/quvi/wiki/FAQ</a>&gt;</p>
<dt>Development code:</p>
<dd> % git clone <a href="git://repo.or.cz/quvi.git">git://repo.or.cz/quvi.git</a></dl>
<h2>AUTHOR</h2>
<p> Toni Gundogdu. </p>
<h2>Index</h2>
