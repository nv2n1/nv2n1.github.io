---
title: "sc(1)"
name: "sc"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sc/"
description: "sc – Splunk Client"
---

<h2 class="name">NAME</h2>
<p> sc &#8211; Splunk Client </p>
<h2>SYNOPSIS</h2>
<p> <code>sc</code> [&#8211;host &lt;host&gt;] [&#8211;port &lt;port&gt;] [&#8211;login &lt;login&gt;] [&#8211;password &lt;password&gt;] [&#8211;insecure] &lt;subcommand&gt; [&lt;arguments&gt;,&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This is remote client for Splunk log search engine based upon WWW::Splunk. It is currently quite limited in capabilities, but intended and designed to be extended in future.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;host &lt;host&gt;</code></p>
<dd> Sets remote server to connect to. Defaults to localhost.</p>
<dt><code>&#8211;port &lt;port&gt;</code></p>
<dd> Sets port of remote server to connect to. Defaults to 8089. Please note that this is the management port, not the <font SIZE="-1">WWW</font> interface port.</p>
<dt><code>&#8211;login &lt;login&gt;</code></p>
<dd> User name of the user to connect to Splunk as. Defaults to admin. The defaults for username and password will probably (hopefully?) not suit your configuration.</p>
<dt><code>&#8211;password &lt;password&gt;</code></p>
<dd> Password of the user to connect to Splunk as. Defaults to changeme.</p>
<dt><code>&#8211;insecure</code></p>
<dd> Tolerate <font SIZE="-1">SSL</font> errors.</p>
<dt><code>&lt;subcommand&gt; [&lt;arguments&gt;]</code></p>
<dd> Subcommand to run. Currently defined is just <code>search</code>.</dl>
<h2>COMMANDS</h2>
<h3><code>search</code> [-t|&#8211;since &lt;time&gt;] [-T|&#8211;until &lt;time&gt;] [-f|&#8211;format compact|long|raw] &lt;search string&gt;</h3>
<p> Conduct a search, output the raw log data as they are looked up. Terminate when the search is finished.</p>
<dl>
<dt><code>-t</code>, <code>&#8211;since</code> <code>&lt;time&gt;</code></p>
<dd> Cut off at given time. The time specification is any string understood by Date::Manip. Most common formats apply as well as human-readable relative time specifications (see <font SIZE="-1">EXAMPLES</font>). </p>
<p> Use <tt>&quot;rt&quot;</tt> for real time search, optionally with specifcation of the search window, such as <tt>&quot;rt-10&quot;</tt> for 10-second window, or <tt>&quot;rt-1m&quot;</tt> for one minute. </p>
<p> Defaults to unlimited.</p>
<dt><code>-T</code>, <code>&#8211;until</code> <code>&lt;time&gt;</code></p>
<dd> Do not look for entries newer than given time. The format of the time specification is the same as for <code>&#8211;since</code> option. </p>
<p> If this or <i>&#8211;since</i> is <tt>&quot;rt&quot;</tt> a real-time search is conducted.</p>
<dt><code>-f</code>, <code>&#8211;format</code> <i>compact</i>|<i>long</i>|<i>raw</i></p>
<dd> Switch output format style.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>sc &#8211;host splunk.example.net &#8211;login user &#8211;password s1kr3t2 &#8211;since &#8216;2 days ago&#8217; &#8211;until yesterday search &#8216;network </code><font SIZE="-1"><code>AND</code></font><code> error | head 10&#8242;</code></p>
<dd> Perform a simple search query limited by given time frame.</p>
<dt><code>sc &#8211;since &#8216;rt-30&#8217; search &#8216;source=/var/log/httpd/access_log |stats count by http_status_code&#8217;</code></p>
<dd> Perform a simple real-time search.</dl>
<h2>SEE ALSO</h2>
<p> WWW::Splunk, WWW::Splunk::API</p>
<h2>AUTHORS</h2>
<p> Lubomir Rintel, &lt;lkundrak [at] v3.sk&gt; </p>
<p> The code is hosted on GitHub &lt;<a rel="nofollow" href="http://github.com/lkundrak/perl-WWW-Splunk">http://github.com/lkundrak/perl-WWW-Splunk</a>&gt;. Bug fixes and feature enhancements are always welcome. </p>
<h2>Index</h2>
<dt><a href="#lbAH">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAI">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAJ">AUTHORS</a></p>
<dd></dl>
