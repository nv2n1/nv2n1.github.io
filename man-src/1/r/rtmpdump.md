---
title: "rtmpdump(1)"
name: "rtmpdump"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rtmpdump/"
description: "rtmpdump – RTMP streaming media client"
---

<h2 class="name">NAME</h2>
<p> rtmpdump &#8211; RTMP streaming media client </p>
<h2>SYNOPSIS</h2>
<p> <code>rtmpdump</code> <code>-r</code><i>&nbsp;url</i> [<code>-n</code><i>&nbsp;hostname</i>] [<code>-c</code><i>&nbsp;port</i>] [<code>-l</code><i>&nbsp;protocol</i>] [<code>-S</code><i>&nbsp;host:port</i>] [<code>-a</code><i>&nbsp;app</i>] [<code>-t</code><i>&nbsp;tcUrl</i>] [<code>-p</code><i>&nbsp;pageUrl</i>] [<code>-s</code><i>&nbsp;swfUrl</i>] [<code>-f</code><i>&nbsp;flashVer</i>] [<code>-u</code><i>&nbsp;auth</i>] [<code>-C</code><i>&nbsp;conndata</i>] [<code>-y</code><i>&nbsp;playpath</i>] [<code>-Y</code>] [<code>-v</code>] [<code>-d</code><i>&nbsp;subscription</i>] [<code>-e</code>] [<code>-k</code><i>&nbsp;skip</i>] [<code>-A</code><i>&nbsp;start</i>] [<code>-B</code><i>&nbsp;stop</i>] [<code>-b</code><i>&nbsp;buffer</i>] [<code>-m</code><i>&nbsp;timeout</i>] [<code>-T</code><i>&nbsp;key</i>] [<code>-j</code><i>&nbsp;JSON</i>] [<code>-w</code><i>&nbsp;swfHash</i>] [<code>-x</code><i>&nbsp;swfSize</i>] [<code>-W</code><i>&nbsp;swfUrl</i>] [<code>-X</code><i>&nbsp;swfAge</i>] [<code>-o</code><i>&nbsp;output</i>] [<code>-#</code>] [<code>-q</code>] [<code>-V</code>] [<code>-z</code>]<br />
 <code>rtmpdump -h</code></p>
<h2>DESCRIPTION</h2>
<p> <code>rtmpdump</code> is a tool for dumping media content streamed over RTMP. </p>
<p> <code>rtmpdump</code> makes a connection to the specified RTMP server and plays the media specified by the given <i>url</i>. The url should be of the form </p>
<pre><code>
rtmp[t][e]: // hostname[:port][/app[/playpath]]
</code></pre>
<p> Plain rtmp, as well as tunneled and encrypted sessions are supported.</p>
<h2>OPTIONS</h2>
<h3>Network Parameters</h3>
<p> These options define how to connect to the media server.</p>
<dl>
<dt><code>&#8211;rtmp<tt>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-r</code>&nbsp;<i>url</i></p>
<dd> URL of the server and media content.</p>
<dt><code>&#8211;host<tt>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-n</code>&nbsp;<i>hostname</i></p>
<dd> Overrides the hostname in the RTMP URL.</p>
<dt><code>&#8211;port<tt>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-c</code>&nbsp;<i>port</i></p>
<dd> Overrides the port number in the RTMP URL.</p>
<dt><code>&#8211;protocol<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-l</code>&nbsp;<i>number</i></p>
<dd> Overrides the protocol in the RTMP URL.</p>
<pre>
  0 = rtmp
  1 = rtmpt
  2 = rtmpe
  3 = rtmpte
  4 = rtmps
  5 = rtmpts
</pre>
<dt><code>&#8211;socks<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-S</code>&nbsp;<i>host:port</i></p>
<dd> Use the specified SOCKS4 proxy.
</dl>
<h3>Connection Parameters</h3>
<p> These options define the content of the RTMP Connect request packet. If correct values are not provided, the media server will reject the connection attempt.</p>
<dl>
<dt><code>&#8211;app<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-a</code>&nbsp;<i>app</i></p>
<dd> Name of application to connect to on the RTMP server. Overrides<br />
 the app in the RTMP URL. Sometimes the rtmpdump URL parser cannot determine the app name automatically, so it must be given explicitly using this option.</p>
<dt><code>&#8211;tcUrl<tt>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-t</code>&nbsp;<i>url</i></p>
<dd> URL of the target stream. Defaults to rtmp[e]://host[:port]/app/playpath.</p>
<dt><code>&#8211;pageUrl<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-p</code>&nbsp;<i>url</i></p>
<dd> URL of the web page in which the media was embedded. By default no<br />
 value will be sent.</p>
<dt><code>&#8211;swfUrl<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-s</code>&nbsp;<i>url</i></p>
<dd> URL of the SWF player for the media. By default no value will be sent.</p>
<dt><code>&#8211;flashVer<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-f</code>&nbsp;<i>version</i></p>
<dd> Version of the Flash plugin used to run the SWF player. The<br />
 default is &quot;LNX 10,0,32,18&quot;.</p>
<dt><code>&#8211;auth<tt>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-u</code>&nbsp;<i>string</i></p>
<dd> An authentication string to be appended to the Connect message. Using<br />
 this option will append a Boolean TRUE and then the specified string. This option is only used by some particular servers and is deprecated. The more general <code>&#8211;conn</code> option should be used instead.</p>
<dt><code>&#8211;conn<tt>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-C</code>&nbsp;<i>type:data</i></p>
<dd> Append arbitrary AMF data to the Connect message. The type<br />
 must be B for Boolean, N for number, S for string, O for object, or Z for null. For Booleans the data must be either 0 or 1 for FALSE or TRUE, respectively. Likewise for Objects the data must be 0 or 1 to end or begin an object, respectively. Data items in subobjects may be named, by prefixing the type with &#8216;N&#8217; and specifying the name before the value, e.g. NB:myFlag:1. This option may be used multiple times to construct arbitrary AMF sequences. E.g. </p>
<pre>
  -C B:1 -C S:authMe -C O:1 -C NN:code:1.23 -C NS:flag:ok -C O:0
</pre>
</dl>
<h3>Session Parameters</h3>
<p> These options take effect after the Connect request has succeeded.</p>
<dl>
<dt><code>&#8211;playpath<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-y</code>&nbsp;<i>path</i></p>
<dd> Overrides the playpath parsed from the RTMP URL. Sometimes the<br />
 rtmpdump URL parser cannot determine the correct playpath automatically, so it must be given explicitly using this option.</p>
<dt><code>&#8211;playlist<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-Y</code></p>
<dd> Issue a set_playlist command before sending the play command. The<br />
 playlist will just contain the current playpath.</p>
<dt><code>&#8211;live<tt>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-v</code></p>
<dd> Specify that the media is a live stream. No resuming or seeking in<br />
 live streams is possible.</p>
<dt><code>&#8211;subscribe<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-d</code>&nbsp;<i>stream</i></p>
<dd> Name of live stream to subscribe to. Defaults to<br />
 <i>playpath</i>.</p>
<dt><code>&#8211;realtime<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-R</code></p>
<dd> Download approximately in realtime, without attempting to speed up via<br />
 Pause/Unpause commands (&quot;the BUFX hack&quot;). Useful for servers that jump backwards in time at the Unpause command. Resuming and seeking in realtime streams is still possible.</p>
<dt><code>&#8211;resume<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-e</code></p>
<dd> Resume an incomplete RTMP download.</p>
<dt><code>&#8211;skip<tt>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-k</code>&nbsp;<i>num</i></p>
<dd> Skip<br />
 <i>num</i> keyframes when looking for the last keyframe from which to resume. This may be useful if a regular attempt to resume fails. The default is 0.</p>
<dt><code>&#8211;start<tt>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-A</code>&nbsp;<i>num</i></p>
<dd> Start at<br />
 <i>num</i> seconds into the stream. Not valid for live streams.</p>
<dt><code>&#8211;stop<tt>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-B</code>&nbsp;<i>num</i></p>
<dd> Stop at<br />
 <i>num</i> seconds into the stream.</p>
<dt><code>&#8211;buffer<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-b</code>&nbsp;<i>num</i></p>
<dd> Set buffer time to<br />
 <i>num</i> milliseconds. The default is 36000000.</p>
<dt><code>&#8211;timeout<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-m</code>&nbsp;<i>num</i></p>
<dd> Timeout the session after<br />
 <i>num</i> seconds without receiving any data from the server. The default is 120.</dl>
<h3>Security Parameters</h3>
<p> These options handle additional authentication requests from the server.</p>
<dl>
<dt><code>&#8211;token<tt>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-T</code>&nbsp;<i>key</i></p>
<dd> Key for SecureToken response, used if the server requires SecureToken<br />
 authentication.</p>
<dt><code>&#8211;jtv<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-j</code>&nbsp;<i>JSON</i></p>
<dd> JSON token used by legacy Justin.tv servers. Invokes NetStream.Authenticate.UsherToken</p>
<dt><code>&#8211;swfhash<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-w</code>&nbsp;<i>hexstring</i></p>
<dd> SHA256 hash of the decompressed SWF file. This option may be needed if<br />
 the server uses SWF Verification, but see the <code>&#8211;swfVfy</code> option below. The hash is 32 bytes, and must be given in hexadecimal. The <code>&#8211;swfsize</code> option must always be used with this option.</p>
<dt><code>&#8211;swfsize<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-x</code>&nbsp;<i>num</i></p>
<dd> Size of the decompressed SWF file. This option may be needed if the<br />
 server uses SWF Verification, but see the <code>&#8211;swfVfy</code> option below. The <code>&#8211;swfhash</code> option must always be used with this option.</p>
<dt><code>&#8211;swfVfy<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-W</code>&nbsp;<i>url</i></p>
<dd> URL of the SWF player for this media. This option replaces all three<br />
 of the <code>&#8211;swfUrl</code>, <code>&#8211;swfhash</code>, and <code>&#8211;swfsize</code> options. When this option is used, the SWF player is retrieved from the specified URL and the hash and size are computed automatically. Also the information is cached in a <i>.swfinfo</i> file in the user&#8217;s home directory, so that it doesn&#8217;t need to be retrieved and recalculated every time rtmpdump is run. The .swfinfo file records the URL, the time it was fetched, the modification timestamp of the SWF file, its size, and its hash. By default, the cached info will be used for 30 days before re-checking.</p>
<dt><code>&#8211;swfAge<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-X</code>&nbsp;<i>days</i></p>
<dd> Specify how many days to use the cached SWF info before re-checking. Use<br />
 0 to always check the SWF URL. Note that if the check shows that the SWF file has the same modification timestamp as before, it will not be retrieved again.</dl>
<h3>Miscellaneous</h3>
<dl>
<dt><code>&#8211;flv<tt>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-o</code>&nbsp;<i>output</i></p>
<dd> Specify the output file name. If the name is &#8211; or is omitted, the<br />
 stream is written to stdout.</p>
<dt><code>&#8211;hashes<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-#</code></p>
<dd> Display streaming progress with a hash mark for each 1% of progress, instead<br />
 of a byte counter.</p>
<dt><code>&#8211;quiet<tt>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-q</code></p>
<dd> Suppress all command output.</p>
<dt><code>&#8211;verbose<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-V</code></p>
<dd> Verbose command output.</p>
<dt><code>&#8211;debug<tt>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-z</code></p>
<dd> Debug level output. Extremely verbose, including hex dumps of all packet data.</p>
<dt><code>&#8211;help<tt>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-h</code></p>
<dd> Print a summary of command options.
</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> Successful program execution.</p>
<dt><code>1</code></p>
<dd> Unrecoverable error.</p>
<dt><code>2</code></p>
<dd> Incomplete transfer, resuming may get further.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>HOME</code></p>
<dd> The value of $<code>HOME</code> is used as the location for the <i>.swfinfo</i> file.</dl>
<h2>FILES</h2>
<dl>
<dt><i>$HOME/.swfinfo</i></p>
<dd> Cache of SWF Verification information</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-rtmpgw/">rtmpgw</a></code>(8)</p>
<h2>AUTHORS</h2>
<p> Andrej Stepanchuk, Howard Chu, The Flvstreamer Team<br />
 &lt;<a rel="nofollow" href="http://rtmpdump.mplayerhq.hu">http://rtmpdump.mplayerhq.hu</a>&gt; </p>
<h2>Index</h2>
