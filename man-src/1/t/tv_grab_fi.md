---
title: "tv_grab_fi(1)"
name: "tv_grab_fi"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_grab_fi/"
description: "tv_grab_fi – Grab TV listings for Finland"
---

<h2 class="name">NAME</h2>
<p> tv_grab_fi &#8211; Grab TV listings for Finland </p>
<h2>SYNOPSIS</h2>
<p> tv_grab_fi [&#8211;cache &lt;<font SIZE="-1">FILE</font>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;config-file&nbsp;<wbr>&lt;<font SIZE="-1">FILE</font>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;days&nbsp;<wbr>&lt;N&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;gui&nbsp;<wbr>[&lt;<font SIZE="-1">OPTION</font>&gt;]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;offset&nbsp;<wbr>&lt;N&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;output&nbsp;<wbr>&lt;<font SIZE="-1">FILE</font>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;quiet] </p>
<p> tv_grab_fi &#8211;capabilities </p>
<p> tv_grab_fi &#8211;configure<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;cache&nbsp;<wbr>&lt;<font SIZE="-1">FILE</font>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;config-file&nbsp;<wbr>&lt;<font SIZE="-1">FILE</font>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;gui&nbsp;<wbr>[&lt;<font SIZE="-1">OPTION</font>&gt;]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;quiet] </p>
<p> tv_grab_fi &#8211;description </p>
<p> tv_grab_fi &#8211;help|-h|-? </p>
<p> tv_grab_fi &#8211;list-channels<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;cache&nbsp;<wbr>&lt;<font SIZE="-1">FILE</font>&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;gui&nbsp;<wbr>[&lt;<font SIZE="-1">OPTION</font>&gt;]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&#8211;quiet] </p>
<p> tv_grab_fi &#8211;version</p>
<h2>DESCRIPTION</h2>
<p> Grab <font SIZE="-1">TV</font> listings for several channels available in Finland. The data comes from various sources, e.g. <a rel="nofollow" href="http://www.telkku.com">www.telkku.com</a>. The grabber relies on parsing <font SIZE="-1">HTML,</font> so it might stop working when the web page layout is changed. </p>
<p> You need to run <tt>&quot;tv_grab_fi --configure&quot;</tt> first to create the channel configuration for your setup. Subsequently runs of <tt>&quot;tv_grab_fi&quot;</tt> will grab the latest data, process them and produce <font SIZE="-1">XML</font> data on the standard output.</p>
<h2>COMMANDS</h2>
<dl>
<dt><font SIZE="-1"><code>NONE</code></font></p>
<dd> Grab mode.</p>
<dt><code>&#8211;capabilities</code></p>
<dd> Show the capabilities this grabber supports. See also &lt;<a rel="nofollow" href="http://wiki.xmltv.org/index.php/XmltvCapabilities">http://wiki.xmltv.org/index.php/XmltvCapabilities</a>&gt;.</p>
<dt><code>&#8211;configure</code></p>
<dd> Generate the configuration file by asking the users which channels to grab.</p>
<dt><code>&#8211;description</code></p>
<dd> Print the description for this grabber.</p>
<dt><code>&#8211;help|-h|-?</code></p>
<dd> Show this help page.</p>
<dt><code>&#8211;list-channels</code></p>
<dd> Fetch all available channels from the various sources and write them to the standard output.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version of this grabber.</dl>
<h2>GENERIC OPTIONS</h2>
<dl>
<dt><code>&#8211;cache </code><font SIZE="-1">FILE</font></p>
<dd> File name to cache the fetched <font SIZE="-1">HTML</font> data in. This speeds up subsequent runs using the same data.</p>
<dt><code>&#8211;gui [</code><font SIZE="-1"><code>OPTION</code></font><code>]</code></p>
<dd> Enable the graphical user interface. If you don&#8217;t specify <font SIZE="-1"><code>OPTION</code></font> then <font SIZE="-1">XMLTV</font> will automatically choose the best available <font SIZE="-1">GUI.</font> Allowed values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Term</code></p>
<dd> Terminal output with a progress bar</p>
<dt><code>TermNoProgressBar</code></p>
<dd> Terminal output without progress bar</p>
<dt><code>Tk</code></p>
<dd> Tk-based <font SIZE="-1">GUI</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;quiet</code></p>
<dd> Suppress any progress messages to the standard output.</dl>
<h2>CONFIGURE MODE OPTIONS</h2>
<dl>
<dt><code>&#8211;config-file </code><font SIZE="-1">FILE</font></p>
<dd> File name to write the configuration to. </p>
<p> Default is <i></i>$HOME<i>/.xmltv/tv_grab_fi.conf</i>.</dl>
<h2>GRAB MODE OPTIONS</h2>
<dl>
<dt><code>&#8211;config-file </code><font SIZE="-1">FILE</font></p>
<dd> File name to read the configuration from. </p>
<p> Default is <i></i>$HOME<i>/.xmltv/tv_grab_fi.conf</i>.</p>
<dt><code>&#8211;days &quot;N&quot;</code></p>
<dd> Grab <tt>&quot;N&quot;</tt> days of <font SIZE="-1">TV</font> data. </p>
<p> Default is 14 days.</p>
<dt><code>&#8211;offset &quot;N&quot;</code></p>
<dd> Grab <font SIZE="-1">TV</font> data starting at <tt>&quot;N&quot;</tt> days in the future. </p>
<p> Default is 0, i.e. today.</p>
<dt><code>&#8211;output </code><font SIZE="-1">FILE</font></p>
<dd> Write the <font SIZE="-1">XML</font> data to <i></i><font SIZE="-1"><i>FILE</i></font><i></i> instead of the standard output.</dl>
<h2>CONFIGURATION FILE SYNTAX</h2>
<p> The configuration file is line oriented, each line can contain one command. Empty lines and everything after the <tt>&quot;#&quot;</tt> comment character is ignored. Supported commands are:</p>
<dl>
<dt><code>channel </code><font SIZE="-1"><code>ID NAME</code></font></p>
<dd> Grab information for this channel. <tt>&quot;ID&quot;</tt> depends on the source, <tt>&quot;NAME&quot;</tt> is ignored and forwarded as is to the <font SIZE="-1">XMLTV</font> output file. This information can be automatically generated using the grabber in the configuration mode.</p>
<dt><code>series description </code><font SIZE="-1"><code>NAME</code></font></p>
<dd> If a programme title matches <tt>&quot;NAME&quot;</tt> then the first sentence of the description, i.e. everything up to the first period (<tt>&quot;.&quot;</tt>), question mark (<tt>&quot;?&quot;</tt>) or exclamation mark (<tt>&quot;!&quot;</tt>), is removed from the description and is used as the name of the episode.</p>
<dt><code>series title </code><font SIZE="-1"><code>NAME</code></font></p>
<dd> If a programme title contains a colon (<tt>&quot;:&quot;</tt>) then the grabber checks if the left-hand side of the colon matches <tt>&quot;NAME&quot;</tt>. If it does then the left-hand side is used as programme title and the right-hand side as the name of the episode.</p>
<dt><code>title map &quot;</code><font SIZE="-1"><code>FROM&quot; </code></font><code>&#8216;</code><font SIZE="-1"><code>TO</code></font><code>&#8216;</code></p>
<dd> If the programme title starts with the string <tt>&quot;FROM&quot;</tt> then replace this part with the string <tt>&quot;TO&quot;</tt>. The strings must be enclosed in single quotes (<tt>&quot;'&quot;</tt>) or double quotes (<tt>&quot;&quot;&quot;</tt>). The title mapping occurs before the <tt>&quot;series&quot;</tt> command processing.</p>
<dt><code>title strip parental level</code></p>
<dd> At the beginning of 2012 some programme descriptions started to include parental levels at the end of the title, e.g. <tt>&quot;(S)&quot;</tt>. With this command all parental levels will be removed from the titles automatically. This removal occurs before the title mapping.</dl>
<h2>SEE ALSO</h2>
<p> xmltv.</p>
<h2>AUTHORS</h2>
<h3>Current</h3>
<dl>
<dt>Stefan Becker &quot;stefan dot becker at nokia dot com&quot;</p>
<dd>
<dt>Ville Ahonen &quot;ville dot ahonen at iki dot fi&quot;</p>
<dd></dl>
<h3>Retired</h3>
<dl>
<dt>Matti Airas</p>
<dd></dl>
<h2>BUGS</h2>
<p> The channels are identified by channel number rather than the <font SIZE="-1">RFC2838</font> form recommended by the <font SIZE="-1">XMLTV DTD.</font> </p>
<h2>Index</h2>
