---
title: "cclive(1)"
name: "cclive"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cclive/"
description: "cclive – command line video download tool"
---

<h2 class="name">NAME</h2>
<p> cclive &#8211; command line video download tool </p>
<h2>SYNOPSIS</h2>
<p> cclive [options] [url&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> cclive is a command line video download tool for Youtube and similar websites. It is a rewrite of the clive software in C<font SIZE="-2">++</font>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print help and exit.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Print version and exit.</p>
<dt><code>&#8211;hosts</code></p>
<dd> Print supported hosts and exit.</p>
<dt><code>&#8211;background</code></p>
<dd> Go to background immediately after startup. Output will be written to <i>cclive.log</i> unless <code>&#8211;logfile</code> is used.</dl>
<p> <code>Output</code></p>
<dl>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Turn off all output.</p>
<dt><code>&#8211;debug</code></p>
<dd> Turn on libcurl verbose mode.</p>
<dt><code>&#8211;emit-csv</code></p>
<dd> Print video details in <font SIZE="-1">CSV</font> format and exit. Prepends &#8220;csv:&#8221; for each video. Ignores <tt>&quot;--quiet&quot;</tt> for <font SIZE="-1">CSV</font>.</p>
<dt><code>&#8211;print-fname</code></p>
<dd> Print filename on a separate line before each download starts. Prepends &#8220;file:&#8221; for each video.</p>
<dt><code>-o, &#8211;logfile</code>=<i>file</i></p>
<dd> Write output to <i>file</i> while in the background. Defaults to <i>cclive.log</i>.</p>
<dt><code>-i, &#8211;logfile-interval</code>=<i>seconds</i></p>
<dd> Update logfile every <i>seconds</i> while in the background. Defines how frequently the download progress information is written to the log. Defaults to <i>10</i>.</dl>
<p> <font SIZE="-1"><code>HTTP</code></font></p>
<dl>
<dt><code>&#8211;agent</code>=<i>agentstring</i></p>
<dd> Identify cclive as <i>agentstring</i> to the <font SIZE="-1">HTTP</font> servers.</p>
<dt><code>&#8211;proxy</code>=<i>proxyhost[:port]</i></p>
<dd> Use the specified <font SIZE="-1">HTTP</font> proxy. Overrides http_proxy definition.</p>
<dt><code>&#8211;no-proxy</code></p>
<dd> Do not use <font SIZE="-1">HTTP</font> proxy, even if http_proxy environment variable is defined.</p>
<dt><code>&#8211;connect-timeout</code>=<i>seconds</i></p>
<dd> Maximum time in <i>seconds</i> allowed for connection to take. Defaults to 30.</p>
<dt><code>&#8211;connect-timeout-socks</code>=<i>seconds</i></p>
<dd> Otherwise identical to the above option but works around the known &#8220;<font SIZE="-1">SOCKS</font> proxy connect timeout&#8221; bug in libcurl. Defaults to 30.</p>
<dt><code>-t, &#8211;retry</code>=<i>number</i></p>
<dd> <i>number</i> of retries. Specify 0 for infinite. Default is 5 times, with the exception of errors such as &#8220;forbidden&#8221; (403) or &#8220;not found&#8221; (404).</p>
<dt><code>&#8211;retry-wait</code>=<i>seconds</i></p>
<dd> Wait 1..seconds between the retries. Default is 1.</dl>
<p> <code>Download</code></p>
<dl>
<dt><code>-O, &#8211;output-video</code>=<i>file</i></p>
<dd> Write the video to <i>file</i>. Overrides <tt>&quot;--filename-format&quot;</tt>.</p>
<dt><code>-c, &#8211;continue</code></p>
<dd> Resume a partially downloaded video file. Affects the file transfers prior to this invocation of cclive. You do not need to specify this option if you want the current invocation of cclive to retry downloading should the connection be lost midway through. This is the default behaviour.</p>
<dt><code>-W, &#8211;overwrite</code></p>
<dd> Overwrite the existing file. Negates <tt>&quot;--continue&quot;</tt>.</p>
<dt><code>-n, &#8211;no-extract</code></p>
<dd> Do not actually extract any videos, simulate only. cclive parses, verifies the video link and exits without downloading it.</p>
<dt><code>l, &#8211;limit-rate</code>=<i>amount</i></p>
<dd> Limit download speed to <i>amount</i> (KB/s). Ignored for video page fetches.</p>
<dt><code>-f, &#8211;format</code>=<i>formatid</i></p>
<dd> Download <i>formatid</i> of the video. If set to <tt>&quot;best&quot;</tt>, cclive attempts to download the best quality of the video. See also &#8220;<font SIZE="-1">FORMATS</font>&#8221;.</p>
<dt><code>-M, &#8211;format-map</code>=<i>hostid:formatid|hostid:formatid&#8230;</i></p>
<dd> Like <tt>&quot;--format&quot;</tt> but allows specifying the format for multiple hosts. Note that <tt>&quot;--format&quot;</tt> setting overrides this setting. See also &#8220;<font SIZE="-1">EXAMPLES</font>&#8221;.</dl>
<p> <code>Filename formatting</code></p>
<dl>
<dt><code>-N, &#8211;number-videos</code></p>
<dd> Prepend a numeric prefix (e.g. &#8220;001_&#8221;) to the output filenames.</p>
<dt><code>-r, &#8211;regexp</code>=<i>regexp</i></p>
<dd> Regular expression used to clean up video titles before they are used for output filenames. Supports (and mimics) Perl&#8217;s /g (global, find all) and /i (case-insensitive). See also &#8220;<font SIZE="-1">EXAMPLES</font>&#8221;.</p>
<dt><code>-S, &#8211;substitute</code>=<i>regexps</i></p>
<dd> Mimics Perl&#8217;s s/old/new/(gi) substitution. This option can be used to replace occurences in output filenames. Supports /g (global, find all occurences) and /i (case-insensitive). </p>
<p> Use of multiple regular expressions is also supported. You can separate each with with a whitespace. The number of regular expressions is currently unlimited. </p>
<p> See also &#8220;<font SIZE="-1">EXAMPLES</font>&#8221;.</p>
<dt><code>-F, &#8211;filename-format</code>=<i>formatstring</i></p>
<dd> Use the specified <i>formatstring</i> to format the output filenames. cclive defaults to &#8220;%h_%i.%s&#8221;. Any of the following specifiers appearing in the format string will be replaced accordingly: </p>
<pre>
  %t = video title
  %i = video id
  %h = website id
  %s = file suffix
</pre>
<p> See also &#8220;<font SIZE="-1">EXAMPLES</font>&#8221;.</dl>
<p> <code>Subsequent</code></p>
<dl>
<dt><code>&#8211;exec</code>=<i>expression</i><code>;</code></p>
<dd> Execute <i>expression</i> after each file transfer. Optional arguments may be passed to the command. The expression must be terminated by a semicolon (&#8220;;&#8221;). </p>
<p> If the specifier &#8220;%i&#8221; appears anywhere in <i>expression</i> it will be replaced with the pathname of the extracted video file.</p>
<dt><code>&#8211;exec</code>=<i>expression</i><code>+</code></p>
<dd> Same as <tt>&quot;--exec&quot;</tt>, except that &#8220;%i&#8221; will be replaced with as many pathnames as possible for the invocation of <i>expression</i>.</p>
<dt><code>-e, &#8211;exec-run</code></p>
<dd> Invokes the expression specified with <tt>&quot;--exec&quot;</tt> when download finishes.</dl>
<p> <code>Streaming</code></p>
<dl>
<dt><code>&#8211;stream-exec</code>=<i>expression</i></p>
<dd> Expression to be invoked with <tt>&quot;--stream&quot;</tt> and <tt>&quot;--stream-pass&quot;</tt>. </p>
<p> If a &#8220;%i&#8221; specifier is used in the <i>expression</i>, it will be replaced with either the video pathname (<tt>&quot;--stream&quot;</tt>) or the parsed video link (<tt>&quot;--stream-pass&quot;</tt>).</p>
<dt><code>-s, &#8211;stream-pass</code></p>
<dd> In addition to the &#8220;%i&#8221; specifier, if the specifier &#8220;%f&#8221; appears anywhere in <tt>&quot;--stream-exec&quot;</tt> <i>expression</i> it will be replaced with the pathname of the extracted video file. </p>
<p> See also &#8220;<font SIZE="-1">EXAMPLES</font>&#8221;. This feature is based on clive wrapper script contributed by Bill Squire.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>cclive <font SIZE="-1">URL</font></p>
<dd> Download video from <font SIZE="-1">URL</font>.</p>
<dt>cclive -f best Youtube_URL</p>
<dd> Download best available format from Youtube_URL.</p>
<dt>cclive -F %t.%s <font SIZE="-1">URL</font></p>
<dd> Use video titles in filenames. cclive uses &#8220;%i_%h.%s&#8221; by default. Note that cclive will apply &#8211;regexp pattern, if any, to the title before using it. For the supported specifiers, see the <tt>&quot;--filename-format&quot;</tt> description.</p>
<dt>cclive -F %t.%s -r /(\w+)/ <font SIZE="-1">URL</font></p>
<dd> Match a string of &#8220;word&#8221; character from the video title and use it in the filename replacing the &#8220;%t&#8221; specifier. cclive replaces the &#8220;%s&#8221; specifier with appropriate file suffix string (e.g. &#8220;flv&#8221;).</p>
<dt>cclive -F %t.%s -r /(\w|\s)/g <font SIZE="-1">URL</font></p>
<dd> Match all &#8220;word&#8221; and &#8220;whitespace&#8221; characters, and use them in the filename replacing the &#8220;%t&#8221;. Note the use of &#8220;/g&#8221; (global, find all).</p>
<dt>cclive -S s/old/new/i <font SIZE="-1">URL</font></p>
<dd> Replace all occurences of &#8220;old&#8221; with &#8220;new&#8221; in the output filename. Note the use of &#8220;i&#8221; (case-insensitive).</p>
<dt>cclive -S s/old/new/i s/:/_/g <font SIZE="-1">URL</font></p>
<dd> Same but replaces also &#8216;:&#8217; with &#8216;_&#8217;. Note the use of &#8220;g&#8221; (global, find all) and the use of a whitespace to separate the used regular expressions.</p>
<dt>cclive &#8211;exec=mplayer -really-quiet %i; -e <font SIZE="-1">URL</font></p>
<dd> Play the downloaded video with <tt><a href="/docs/linux/man/1-mplayer/">mplayer</a>(1)</tt> when download finishes.</p>
<dt>cclive &#8211;exec=ffmpeg -i %i -acodec libvorbis %i.ogg; -e <font SIZE="-1">URL</font></p>
<dd> Similar but re-encode audio from the downloaded video to a vorbis audio file, using <tt><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a>(1)</tt>.</p>
<dt>echo &#8216;stream-exec = mplayer -really-quiet %i&#8217; &gt;&gt; ~/.ccliverc</p>
<dd> Adds <tt>&quot;--stream-exec&quot;</tt> to the config file for permanent use. Saves typing as shown below:</p>
<dt>cclive -s <font SIZE="-1">URL</font></p>
<dd> Stream and play the video from the <font SIZE="-1">URL</font> using <tt><a href="/docs/linux/man/1-mplayer/">mplayer</a>(1)</tt>, as defined with <tt>&quot;--stream-exec&quot;</tt> above. </p>
<p> Note that cclive itself does not stream or play the media, it only parses and passes the video link to <tt><a href="/docs/linux/man/1-mplayer/">mplayer</a>(1)</tt>. </p>
<p> You can use the above as an alternative to the Adobe flash player if you cannot view the streamed videos otherwise, or if you want to play them in an external player while streaming. </p>
<p> The above should work with other player software, like <tt><a href="/docs/linux/man/1-vlc/">vlc</a>(1)</tt> and <tt><a href="/docs/linux/man/1-totem/">totem</a>(1)</tt>.</p>
<dt>cclive -s <font SIZE="-1">URL</font> &#8211;stream-exec=wget %i -O %f</p>
<dd> Use <tt><a href="/docs/linux/man/1-wget/">wget</a>(1)</tt> to download the video. Note the use of the &#8220;%f&#8221; specifier which is unique to <tt>&quot;--pass-stream, -s&quot;</tt>.</p>
<dt>cat &gt; url.lst</p>
<dd>
<pre>
  <a rel="nofollow" href="http://en.sevenload.com/videos/IUL3gda-Funny-Football-Clips">http://en.sevenload.com/videos/IUL3gda-Funny-Football-Clips</a>
  <a rel="nofollow" href="http://youtube.com/watch?v=3HD220e0bx4">http://youtube.com/watch?v=3HD220e0bx4</a>
  <a rel="nofollow" href="http://break.com/index/beach-tackle-whip-lash.html">http://break.com/index/beach-tackle-whip-lash.html</a>
  <a rel="nofollow" href="http://www.liveleak.com/view?i=704_1228511265">http://www.liveleak.com/view?i=704_1228511265</a>
</pre>
<p> Create a file that will contain multiple URLs, each separated with a newline. We can use the created file with cclive as shown below:</p>
<dt>cclive &lt; url.lst</p>
<dd> Or:</p>
<dt>cat url.lst | cclive</p>
<dd> This may save you some typing, as you would normally have to type each <font SIZE="-1">URL</font> to the command line as an argument.</p>
<dt>echo &#8216;format-map = youtube:best|dailymotion:hq&#8217; &gt;&gt; ~/.ccliverc</p>
<dd> Save <tt>&quot;--format-map&quot;</tt> to config file for permanent use.</p>
<dt>cclive Youtube_URL Dailymotion_URL</p>
<dd> Would set &#8211;format=best for Youtube_URL and &#8211;format=hq for Dailymotion_URL. Note that the use of <tt>&quot;--format&quot;</tt> overrides &#8211;format-map setting.</dl>
<h2>FORMATS</h2>
<p> cclive uses libquvi &lt;<a rel="nofollow" href="http://quvi.googlecode.com">http://quvi.googlecode.com</a>&gt; to parse the video download links. You can get a complete list of the supported formats with the <tt>&quot;--hosts&quot;</tt> option. </p>
<p> If you have any additional info regarding the formats, report them to the quvi project (see above link) as this is strictly quvi territory.</p>
<h2>FILES</h2>
<dl>
<dt><code>$HOME/.ccliverc</code></p>
<dd> Most of the program options can be specified in the <tt>$HOME</tt>/.ccliverc config file. For example: </p>
<pre><code>
agent = JBond / 1.0 #--agent
                    proxy = http : // foo:1234 # --proxy
                                   limit -
                                   rate = 50 #--limit - rate no - extract #--no - extract
</code></pre>
<p> You can also use <tt>$CCLIVE_HOME</tt> instead of <tt>$HOME</tt>.</dl>
<h2>UNICODE</h2>
<p> If you are seeing mangled characters in output filenames (titles), this may be because of an invalid locale setting or a sign of terminal incapable of displaying unicode characters. On a typical Unix-like system, try running &#8220;locale -a&#8221; to get a list of the available locale names. </p>
<p> For example, in bash and urxvt terms: </p>
<pre>
  % LANG=en_US.UTF8 urxvt&amp;
  % cclive ... # in new terminal
</pre>
<p> cclive (libquvi) converts the characters to unicode if the video <font SIZE="-1">HTML</font> specifies the charset meta tag. Otherwise the characters are copied as they are. </p>
<p> If you are missing the unicode characters when using <tt>&quot;--regexp&quot;</tt> and <tt>&quot;--filename-format&quot;</tt>, make sure the regular expression includes &#8220;\pL&#8221;. For example: </p>
<pre>
  % cclive -F &quot;%t.%s&quot; -r &quot;/(\w|\s|\pL)/g&quot; URL
</pre>
<p> &#8220;In <font SIZE="-1">UTF-8</font> mode, characters with values greater than 128 never match \d, \s, or \w, and always match \D, \S, and \W. This is true even when Uni- code character property support is available. These sequences retain their original meanings from before <font SIZE="-1">UTF-8</font> support was available, mainly for efficiency reasons. Note that this also affects , because it is defined in terms of \w and \W.&#8221; &#8212; man pcrepattern</p>
<h2>BUGS</h2>
<p> Report them at &lt;<a rel="nofollow" href="http://cclive.googlecode.com/">http://cclive.googlecode.com/</a>&gt;. Please see if the issue has already been reported (or closed) before you submit another. You can use the issue tracker&#8217;s search feature for this, just be sure to search &#8220;All issues&#8221;. </p>
<p> If your bug report contains an error message starting with &#8220;error: libquvi:&#8221;, report the bug to the quvi tracker instead (&lt;<a rel="nofollow" href="http://quvi.googlecode.com/">http://quvi.googlecode.com/</a>&gt;). </p>
<p> You can use the issue trackers for submitting your patches.</p>
<h2>DEBUGGING</h2>
<p> The following lists some of the cclive options that may be useful while debugging. Other tools, like <tt><a href="/docs/linux/man/1-strace/">strace</a>(1)</tt>, <tt><a href="/docs/linux/man/1-gdb/">gdb</a>(1)</tt> and <tt><a href="/docs/linux/man/1-valgrind/">valgrind</a>(1)</tt> may also prove helpful.</p>
<dl>
<dt>cclive &#8211;debug <font SIZE="-1">URL</font></p>
<dd> Enable libcurl verbose mode.</p>
<dt>cclive -n <font SIZE="-1">URL</font></p>
<dd> Simulate only. Fetch, parse but skip get.</p>
<dt>$prefix/share/quvi/lua/README</p>
<dd>
<dt>$prefix/share/quvi/lua/website/README</p>
<dd> cclive relies on libquvi for parsing the video download links. If the parsing ever breaks, the above two files cover some of the essential details. </p>
<p> The latter directory also contains the website specific Lua scripts that libquvi calls to parse the video links.</p>
<dt>$prefix/share/doc/quvi</p>
<dd> The above directory contains quvi related HOWTOs which may also prove helpful reading for those interested in cclive. The guidelines that the HOWTOs list are also followed in this project.</dl>
<h2>EXIT STATUS</h2>
<p> cclive exits 0 on success, and &gt;0 if an error occurs. </p>
<pre>
  CCLIVE_OK           = 0
  CCLIVE_OPT          = 1  // cmdline option parsing error
  CCLIVE_OPTARG       = 2  // cmdline option arg error
  CCLIVE_CURLINIT     = 3  // curl init error (unused since 0.6.0+)
  CCLIVE_NOTHINGTODO  = 4  // file already retrieved
  CCLIVE_SYSTEM       = 5  // system call failed
  CCLIVE_NOSUPPORT    = 6  // host not supported
  CCLIVE_NET          = 7  // network error
  CCLIVE_FETCH        = 8  // fetch error
  CCLIVE_PARSE        = 9  // parse error
  CCLIVE_INTERNAL     = 10 // internal error (see return code)
</pre>
<h2>OTHER</h2>
<dl>
<dt>Project page:</p>
<dd> &lt;<a rel="nofollow" href="http://cclive.googlecode.com/">http://cclive.googlecode.com/</a>&gt;</dl>
<h2>AUTHOR</h2>
<p> Toni Gundogdu &lt;legatvs [at] gmail.com&gt;. </p>
<h2>Index</h2>
