---
title: "rrdcgi(1)"
name: "rrdcgi"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdcgi/"
description: "rrdcgi – Create web pages containing RRD graphs based on templates"
---

<h2 class="name">NAME</h2>
<p> rrdcgi &#8211; Create web pages containing RRD graphs based on templates </p>
<h2>SYNOPSIS</h2>
<p> <tt>&quot;#!/path/to/&quot;</tt><code>rrdcgi</code> [<code>&#8211;filter</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>rrdcgi</code> is a sort of very limited script interpreter. Its purpose is to run as a cgi-program and parse a web page template containing special &lt;<font SIZE="-1">RRD::</font> tags. <code>rrdcgi</code> will interpret and act according to these tags. In the end it will printout a web page including the necessary <font SIZE="-1">CGI</font> headers. </p>
<p> <code>rrdcgi</code> parses the contents of the template in 3 steps. In each step it looks only for a subset of tags. This allows nesting of tags. </p>
<p> The argument parser uses the same semantics as you are used from your C-shell.</p>
<dl>
<dt><code>&#8211;filter</code></p>
<dd> Assume that rrdcgi is run as a filter and not as a cgi.</dl>
<h3>Keywords</h3>
<dl>
<dt><font SIZE="-1">RRD::CV</font> <i>name</i></p>
<dd> Inserts the <font SIZE="-1">CGI</font> variable of the given name.</p>
<dt><font SIZE="-1">RRD::CV::QUOTE</font> <i>name</i></p>
<dd> Inserts the <font SIZE="-1">CGI</font> variable of the given name but quotes it, ready for use as an argument in another <font SIZE="-1">RRD::</font> tag. So even when there are spaces in the value of the <font SIZE="-1">CGI</font> variable it will still be considered to be one argument.</p>
<dt><font SIZE="-1">RRD::CV::PATH</font> <i>name</i></p>
<dd> Inserts the <font SIZE="-1">CGI</font> variable of the given name, quotes it and makes sure it starts neither with a &#8216;/&#8217; nor contains &#8216;..&#8217;. This is to make sure that no problematic pathnames can be introduced through the <font SIZE="-1">CGI</font> interface.</p>
<dt><font SIZE="-1">RRD::GETENV</font> <i>variable</i></p>
<dd> Get the value of an environment variable. </p>
<pre>
 &lt;RRD::GETENV REMOTE_USER&gt;
</pre>
<p> might give you the name of the remote user given you are using some sort of access control on the directory.</p>
<dt><font SIZE="-1">RRD::GOODFOR</font> <i>seconds</i></p>
<dd> Specify the number of seconds this page should remain valid. This will prompt the rrdcgi to output a Last-Modified, an Expire and if the number of seconds is <i>negative</i> a Refresh header.</p>
<dt><font SIZE="-1">RRD::INCLUDE</font> <i>filename</i></p>
<dd> Include the contents of the specified file into the page returned from the cgi.</p>
<dt><font SIZE="-1">RRD::SETENV</font> <i>variable</i> <i>value</i></p>
<dd> If you want to present your graphs in another time zone than your own, you could use </p>
<pre>
 &lt;RRD::SETENV TZ UTC&gt;
</pre>
<p> to make sure everything is presented in Universal Time. Note that the values permitted to <font SIZE="-1">TZ</font> depend on your <font SIZE="-1">OS</font>.</p>
<dt><font SIZE="-1">RRD::SETVAR</font> <i>variable</i> <i>value</i></p>
<dd> Analog to <font SIZE="-1">SETENV</font> but for local variables.</p>
<dt><font SIZE="-1">RRD::GETVAR</font> <i>variable</i></p>
<dd> Analog to <font SIZE="-1">GETENV</font> but for local variables.</p>
<dt><font SIZE="-1">RRD::TIME::LAST</font> <i>rrd-file</i> <i>strftime-format</i></p>
<dd> This gets replaced by the last modification time of the selected <font SIZE="-1">RRD</font>. The time is <i>strftime</i>-formatted with the string specified in the second argument.</p>
<dt><font SIZE="-1">RRD::TIME::NOW</font> <i>strftime-format</i></p>
<dd> This gets replaced by the current time of day. The time is <i>strftime</i>-formatted with the string specified in the argument. </p>
<p> Note that if you return : (colons) from your strftime format you may have to escape them using \ if the time is to be used as an argument to a <font SIZE="-1">GRAPH</font> command.</p>
<dt><font SIZE="-1">RRD::TIME::STRFTIME</font> <i>START|END</i> <i>start-spec</i> <i>end-spec</i> <i>strftime-format</i></p>
<dd> This gets replaced by a strftime-formatted time using the format <i>strftime-format</i> on either <i>start-spec</i> or <i>end-spec</i> depending on whether <i></i><font SIZE="-1"><i>START</i></font><i></i> or <i></i><font SIZE="-1"><i>END</i></font><i></i> is specified. Both <i>start-spec</i> and <i>end-spec</i> must be supplied as either could be relative to the other. This is intended to allow pretty titles on graphs with times that are easier for non RRDtool folks to figure out than &#8220;-2weeks&#8221;. </p>
<p> Note that again, if you return : (colon) from your strftime format, you may have to escape them using \ if the time is to be used as an argument to a <font SIZE="-1">GRAPH</font> command.</p>
<dt><font SIZE="-1">RRD::GRAPH</font> <i>rrdgraph arguments</i></p>
<dd> This tag creates the <font SIZE="-1">RRD</font> graph defined by its argument and then is replaced by an appropriate &lt;<font SIZE="-1">IMG</font> &#8230; &gt; tag referring to the graph. The <code>&#8211;lazy</code> option in <font SIZE="-1">RRD</font> graph can be used to make sure that graphs are only regenerated when they are out of date. The arguments to the <font SIZE="-1"><code>RRD::GRAPH</code></font> tag work as described in the <code>rrdgraph</code> manual page. </p>
<p> Use the <code>&#8211;lazy</code> option in your <font SIZE="-1">RRD::GRAPH</font> tags, to reduce the load on your server. This option makes sure that graphs are only regenerated when the old ones are out of date. </p>
<p> If you do not specify your own <code>&#8211;imginfo</code> format, the following will be used: </p>
<pre>
 &lt;IMG SRC=&quot;%s&quot; WIDTH=&quot;%lu&quot; HEIGHT=&quot;%lu&quot;&gt;
</pre>
<p> Note that <tt>%s</tt> stands for the filename part of the graph generated, all directories given in the <font SIZE="-1">PNG</font> file argument will get dropped.</p>
<dt><font SIZE="-1">RRD::PRINT</font> <i>number</i></p>
<dd> If the preceding <font SIZE="-1"><code>RRD::GRAPH</code></font> tag contained and <font SIZE="-1"><code>PRINT</code></font> arguments, then you can access their output with this tag. The <i>number</i> argument refers to the number of the <font SIZE="-1"><code>PRINT</code></font> argument. This first <font SIZE="-1"><code>PRINT</code></font> has <i>number</i> 0.</p>
<dt><font SIZE="-1">RRD::INTERNAL</font> &lt;var&gt;</p>
<dd> This tag gets replaced by an internal var. Currently these vars are known: <font SIZE="-1">VERSION</font>, <font SIZE="-1">COMPILETIME</font>. These vars represent the compiled-in values.</dl>
<h2>EXAMPLE 1</h2>
<p> The example below creates a web pages with a single <font SIZE="-1">RRD</font> graph. </p>
<pre>
 #!/usr/local/bin/rrdcgi
 &lt;HTML&gt;
 &lt;HEAD&gt;&lt;TITLE&gt;RRDCGI Demo&lt;/TITLE&gt;&lt;/HEAD&gt;
 &lt;BODY&gt;
 &lt;H1&gt;RRDCGI Example Page&lt;/H1&gt;
 &lt;P&gt;
 &lt;RRD::GRAPH demo.png --lazy --title=&quot;Temperatures&quot;
          DEF:cel=demo.rrd:exhaust:AVERAGE
          LINE2:cel#00a000:&quot;D. Celsius&quot;&gt;
 &lt;/P&gt;
 &lt;/BODY&gt;
 &lt;/HTML&gt;
</pre>
<h2>EXAMPLE 2</h2>
<p> This script is slightly more elaborate, it allows you to run it from a form which sets <font SIZE="-1">RRD_NAME</font>. <font SIZE="-1">RRD_NAME</font> is then used to select which <font SIZE="-1">RRD</font> you want to use as source for your graph. </p>
<pre><code>
#!/ usr / local / bin / rrdcgi
&lt;HTML&gt;
 &lt;HEAD&gt;&lt;TITLE&gt;RRDCGI Demo&lt;/TITLE&gt;&lt;/HEAD&gt;
 &lt;BODY&gt;
 &lt;H1&gt;RRDCGI Example Page for &lt;RRD::CV RRD_NAME&gt;&lt;/H1&gt;
 &lt;H2&gt;Selection&lt;/H2&gt;
 &lt;FORM&gt;&lt;INPUT NAME=RRD_NAME TYPE=RADIO VALUE=roomA&gt; Room A,
       &lt;INPUT NAME=RRD_NAME TYPE=RADIO VALUE=roomB&gt; Room B.
       &lt;INPUT TYPE=SUBMIT&gt;&lt;/FORM&gt;
 &lt;H2&gt;Graph&lt;/H2&gt;
 &lt;P&gt;
 &lt;RRD::GRAPH &lt;RRD::CV::PATH RRD_NAME&gt;.png --lazy
          --title "Temperatures for "&lt;RRD::CV::QUOTE RRD_NAME&gt;
          DEF:cel=&lt;RRD::CV::PATH RRD_NAME&gt;.rrd:exhaust:AVERAGE
          LINE2:cel#00a000:"D. Celsius"&gt;
 &lt;/P&gt;
 &lt;/BODY&gt;
 &lt;/HTML&gt;
</code></pre>
<h2>EXAMPLE 3</h2>
<p> This example shows how to handle the case where the <font SIZE="-1">RRD</font>, graphs and cgi-bins are separate directories </p>
<pre><code>
#!/... / bin / rrdcgi
&lt;HTML&gt;
 &lt;HEAD&gt;&lt;TITLE&gt;RRDCGI Demo&lt;/TITLE&gt;&lt;/HEAD&gt;
 &lt;BODY&gt;
 &lt;H1&gt;RRDCGI test Page&lt;/H1&gt;
 &lt;RRD::GRAPH
  /.../web/pngs/testhvt.png
  --imginfo '&lt;IMG SRC=/.../pngs/%s WIDTH=%lu HEIGHT=%lu &gt;'
  --lazy --start -1d --end now
  DEF:http_src=/.../rrds/test.rrd:http_src:AVERAGE
  AREA:http_src#00ff00:http_src
 &gt;
 &lt;/BODY&gt;
 &lt;/HTML&gt;
</code></pre>
<p> Note 1: Replace /&#8230;/ with the relevant directories </p>
<p> Note 2: The SRC=/&#8230;/pngs should be paths from the view of the webserver/browser</p>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<h2>Index</h2>
