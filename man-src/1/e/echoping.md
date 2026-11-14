---
title: "echoping(1)"
name: "echoping"
section: "1"
letter: "e"
url: "/docs/linux/man/1-echoping/"
description: "echoping – tests a remote host with TCP or UDP"
---

<h2>NAME</h2>
<p> echoping &#8211; tests a remote host with TCP or UDP </p>
<h2>SYNOPSIS</h2>
<p> <code>echoping</code> [-4] [-6] [-v] [-V] [-f<i>fill]</i> [-t<i>timeout]</i> [-c] [-d] [-u] [-s<i>size]</i> [-n<i>number]</i> [-w<i>delay]</i> [-h<i>url-or-path]</i> [-R] [-i<i>url]</i> [-p<i>priority]</i> [-P<i>tos]</i> [-C] [-S] [-A] [-a] [-m<i>plugin]</i> <code>hostname</code> [:port] [plugin options&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>echoping</code> is a small program to test (approximatively) performances of a remote Internet host by sending it TCP &quot;echo&quot; packets. It can use other protocols as well (HTTP &#8211; which makes it a good tool to test Web servers, UDP &quot;echo&quot;, etc). </p>
<p> <code>echoping </code> simply shows the elapsed time, including the time to set up the TCP connection and to transfer the data. Therefore, it is unsuitable to physical line raw throughput measures (unlike bing or treno). On the other end, the action it performs are close from, for instance, a HTTP request and it is meaningful to use it (carefully) to measure Web performances. </p>
<h2>ARGUMENT</h2>
<dl>
<dt>hostname[:port]</p>
<dd> Name (or address) of the server to test. For HTTP, you can specify a port number. For HTTP and IPv6, you can use RFC 2732 syntax (you will probably need to escape the brackets from the shell). The name can be an IDN (Unicode domain name). </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt>-v</p>
<dd> Verbose</p>
<dt>-V</p>
<dd> Displays the compiled-in configuration of echoping. Useful for bug reports.</p>
<dt>-s nnn</p>
<dd> Size of the data to send. Large values can produce strange results with some echo servers.</p>
<dt>-n nnn</p>
<dd> Numbers of repeated tests. With this option, you have also the minimum, maximum, average and median time, as well as the standard deviation. The median is the value such that half of the measures are under it and the other half is above. When you measure highly variables values, like it is often the case on the whole Internet, median is better than average to avoid &quot;extreme&quot; values. You can check the &quot;value&quot; of the average by looking at the standard deviation: very roughly, if the standard deviation is more than the half of the average, the average does not mean anything. (See a book about statistics for the details: the reality is far more complicated.)</p>
<dt>-w nnn</p>
<dd> Number of seconds to wait between two tests (default is one). On systems which have usleep(), you can write it as a fractional number, such as 3.14. Otherwise, use integers.</p>
<dt>-t nnn</p>
<dd> Number of seconds to wait a reply before giving up. For TCP, this is the maximum number of seconds for the whole connection (setup and data exchange).</p>
<dt>-u</p>
<dd> Use UDP instead of TCP</p>
<dt>-d</p>
<dd> Use the &quot;discard&quot; service instead of echo</p>
<dt>-c</p>
<dd> Use the &quot;chargen&quot; service instead of echo</p>
<dt>-h url-or-path</p>
<dd> Use the HTTP protocol (instead of echo) for the given URL. If the hostname is the Web server, the argument has to be a path, a relative URL (for instance &#8216;/&#8217; or &#8216;/pics/foobar.gif&#8217;). If the hostname is a proxy/cache like Squid, the argument has to be an absolute URL.</p>
<dt>-R</p>
<dd> Accept HTTP status codes 3xx (redirections) as normal responses (the default is to regard them as errors)</p>
<dt>-i url</p>
<dd> Use the ICP protocol (instead of echo) for the given URL. The URL has to be an absolute one. This is mostly for testing Squid Web proxy/caches.</p>
<dt>-A</p>
<dd> Force the proxy (if you use one) to ignore the cache</p>
<dt>-a</p>
<dd> Force the proxy (if you use one) to revalidate data with the original server</p>
<dt>-C</p>
<dd> Use the SSL/TLS (cryptography) protocol. For HTTP tests only.</p>
<dt>-S</p>
<dd> Use the SMTP protocol (instead of echo) for the given server.</p>
<dt>-4</p>
<dd> Use only IPv4 (even if the target machine has an IPv6 address)</p>
<dt>-6</p>
<dd> Use only IPv6 (even if the target machine has an IPv4 address)</p>
<dt>-f character</p>
<dd> Fill the packet with this character (default is random filling)</p>
<dt>-D</p>
<dd> Tries to display actual data transfer duration only, not total time</p>
<dt>-N n</p>
<dd> Displays an average which excludes values (&quot;outliers&quot;) which are further than +/- N*standard deviation</p>
<dt>-p n</p>
<dd> Send packets with the socket priority to the integer <i>n</i>. The mapping of the socket priority into a network layer or a link layer priority depends upon the network protocol and link protocol in use. For more details see <code>SO_PRIORITY</code> in <code><a href="/docs/linux/man/7-socket/">socket</a>(7).</code></p>
<dt>-P n</p>
<dd> Set the IP type of service octet in the transmitted packets to the least significant eight bits of the integer <i>n</i>. See <code><a href="/docs/linux/man/7-ip/">ip</a>(7)</code> or <code><a href="/docs/linux/man/4-ip/">ip</a>(4)</code> (depending on your Unix). /usr/include/netinet/ip.h may contain interesting constants for setting Type Of Service.</p>
<dt>-m plugin</p>
<dd> Load the given plugin. The plugin is first searched in the normal library directories (see <code><a href="/docs/linux/man/8-ld-so/">ld.so</a>(8)</code> ) then in /usr/lib64/echoping. You can type <code>ls</code> in /usr/lib64/echoping to get an idea of the available plugins. The documentation for a given plugin is in <code><a href="/docs/linux/man/1-echoping_pluginname/">echoping_PLUGINNAME</a>(1)</code> The plugin-specific options appear <code>after</code> the hostname.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>echoping -v foobar.example.com</p>
<dd> Tests the remote machine with TCP echo (one test).</p>
<dt>echoping -n 5 -w 10 foobar.example.com</p>
<dd> Tests the remote machine with TCP echo (five tests, every ten seconds).</p>
<dt>echoping -h&nbsp;<wbr>/&nbsp;<wbr>foobar.example.com</p>
<dd> Tests the remote Web server and asks its home page. Note you don&#8217;t indicate the whole URL.</p>
<dt>echoping -h&nbsp;<wbr><a rel="nofollow" href="http://www.example.com/">http://www.example.com/</a>&nbsp;<wbr>cache.example.com:3128</p>
<dd> Tests the remote Web proxy-cache and asks a Web page. Note that you must indicate the whole URL.</p>
<dt>echoping -n 3 -m whois foobar.example.com -d tao.example.org</p>
<dd> Loads the whois plugin and query the host foobar.example.com. &quot;-d tao.example.org&quot; are options specific to the whois plugin.</p>
<dt>echoping -u -P 0xa0 foobar.example.com</p>
<dd> Sends several UDP Echo packets with an IP Precedence of 5.</dl>
<h2>IP TYPE OF SERVICE OCTET</h2>
<p> The IP packet header contains 8 bits named the &quot;type of service octet&quot;. The value of the octet is set with the <code>-P</code> option. The effects of the octet are defined differently in RFC791 <i>Internet Protocol</i> and RFC2474 <i>Definition of the Differentiated Services Field (DS Field) in the IPv4 and IPv6 Headers.</i> </p>
<p> RFC791 defines <i>Precedence</i> which has ascending priorities 0 through to 7, and the bits <i>Delay</i>, <i>Throughput</i>, <i>Reliability</i>, and <i>Cost</i> which indicates the application&#8217;s preference for the properties of the packet&#8217;s path through the network. <i>Precedence</i> is in the most significant three bits of the type of service octet, followed in decending significance order by the <i>D</i>, <i>T</i>, <i>R</i> and <i>C</i> bits. The least significant bit must be zero. Only one of the <i>D</i>, <i>T</i>, <i>R</i> or <i>C</i> bits may be set. </p>
<p> RFC2474 defines the Distributed Services Code Point, or DSCP. This acts as a selector between 64 possible behaviours that the network can apply to the packet. The <i>DSCP</i> is in the most significant six bits of the type of service octet. The remaining least significant two bits of the octet must be zero. </p>
<p> The numeric arguments to <code>-p</code> and <code>-P</code> can be in decimal (such as 11), octal (such as 013) or hexadecimal (such as 0x0b). So padding decimal arguments with leading zeros will change the value read. </p>
<p> You may need to be superuser to set some <code>-p</code> or <code>-P</code> values (precedence on Linux, for instance). </p>
<h2>BUGS</h2>
<p> See SourceForge bug tracking system at &lt;<a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=4581">http://sourceforge.net/tracker/?group_id=4581</a>&amp;atid=104581&gt;. </p>
<h2>SEE ALSO</h2>
<p> See the README for information about other network measurements programs. </p>
<h2>FILES</h2>
<dl>
<dt><code>/usr/lib64/echoping </code></p>
<dd> Plugins directory </p>
</dl>
<h2>AUTHOR</h2>
<p> Stephane Bortzmeyer &lt;bortz [at] users.sourceforge.net&gt; </p>
<h2>Index</h2>
