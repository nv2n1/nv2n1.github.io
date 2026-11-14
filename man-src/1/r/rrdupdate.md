---
title: "rrdupdate(1)"
name: "rrdupdate"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdupdate/"
description: "rrdupdate – Store a new set of values into the RRD"
---

<h2 class="name">NAME</h2>
<p> rrdupdate &#8211; Store a new set of values into the RRD </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdtool</code> {<code>update</code> | <code>updatev</code>} <i>filename</i> [<code>&#8211;template</code>|<code>-t</code>&nbsp;<wbr><i>ds-name</i>[<code>:</code><i>ds-name</i>]&#8230;] [<code>&#8211;daemon</code>|<code>-d</code>&nbsp;<wbr><i>address</i>] [<code>&#8212;</code>] <code>N</code>|<i>timestamp</i><code>:</code><i>value</i>[<code>:</code><i>value</i>&#8230;] <i>at-timestamp</i><code>@</code><i>value</i>[<code>:</code><i>value</i>&#8230;] [<i>timestamp</i><code>:</code><i>value</i>[<code>:</code><i>value</i>&#8230;]&nbsp;<wbr>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <code>update</code> function feeds new data values into an <font SIZE="-1"><code>RRD</code></font>. The data is time aligned (interpolated) according to the properties of the <font SIZE="-1"><code>RRD</code></font> to which the data is written.</p>
<dl>
<dt><code>updatev</code></p>
<dd> This alternate version of <code>update</code> takes the same arguments and performs the same function. The <i>v</i> stands for <i>verbose</i>, which describes the output returned. <code>updatev</code> returns a list of any and all consolidated data points (CDPs) written to disk as a result of the invocation of update. The values are indexed by timestamp (time_t), <font SIZE="-1">RRA</font> (consolidation function and PDPs per <font SIZE="-1">CDP</font>), and data source (name). Note that depending on the arguments of the current and previous call to update, the list may have no entries or a large number of entries. </p>
<p> Since <code>updatev</code> requires direct disk access, the <code>&#8211;daemon</code> option cannot be used with this command.</p>
<dt><i>filename</i></p>
<dd> The name of the <font SIZE="-1"><code>RRD</code></font> you want to update.</p>
<dt><code>&#8211;template</code>|<code>-t</code> <i>ds-name</i>[<code>:</code><i>ds-name</i>]&#8230;</p>
<dd> By default, the <code>update</code> function expects its data input in the order the data sources are defined in the <font SIZE="-1">RRD</font>, excluding any <font SIZE="-1">COMPUTE</font> data sources (i.e. if the third data source <font SIZE="-1"><code>DST</code></font> is <font SIZE="-1">COMPUTE</font>, the third input value will be mapped to the fourth data source in the <font SIZE="-1"><code>RRD</code></font> and so on). This is not very error resistant, as you might be sending the wrong data into an <font SIZE="-1">RRD</font>. </p>
<p> The template switch allows you to specify which data sources you are going to update and in which order. If the data sources specified in the template are not available in the <font SIZE="-1">RRD</font> file, the update process will abort with an error message. </p>
<p> While it appears possible with the template switch to update data sources asynchronously, <code>RRDtool</code> implicitly assigns non-COMPUTE data sources missing from the template the <i>*UNKNOWN*</i> value. </p>
<p> Do not specify a value for a <font SIZE="-1">COMPUTE</font> <font SIZE="-1"><code>DST</code></font> in the <code>update</code> function. If this is done accidentally (and this can only be done using the template switch), <code>RRDtool</code> will ignore the value specified for the <font SIZE="-1">COMPUTE</font> <font SIZE="-1"><code>DST</code></font>.</p>
<dt><code>&#8211;daemon</code>|<code>-d</code> <i>address</i></p>
<dd> If given, <code>RRDTool</code> will try to connect to the caching daemon rrdcached at <i>address</i> and will fail if the connection cannot be established. If the connection is successfully established the values will be sent to the daemon instead of accessing the files directly. </p>
<p> For a list of accepted formats, see the <code>-l</code> option in the rrdcached manual.</p>
<dt><code>N</code>|<i>timestamp</i><code>:</code><i>value</i>[<code>:</code><i>value</i>&#8230;]</p>
<dd> The data used for updating the <font SIZE="-1">RRD</font> was acquired at a certain time. This time can either be defined in seconds since 1970-01-01 or by using the letter &#8216;N&#8217;, in which case the update time is set to be the current time. Negative time values are subtracted from the current time. An <font SIZE="-1">AT_STYLE</font> <font SIZE="-1">TIME</font> <font SIZE="-1">SPECIFICATION</font> (see the <i>rrdfetch</i> documentation) may also be used by delimiting the end of the time specification with the &#8216;@&#8217; character instead of a &#8216;:&#8217;. Getting the timing right to the second is especially important when you are working with data-sources of type <font SIZE="-1"><code>COUNTER</code></font>, <font SIZE="-1"><code>DERIVE</code></font> or <font SIZE="-1"><code>ABSOLUTE</code></font>. </p>
<p> When using negative time values, options and data have to be separated by two dashes (<code>&#8212;</code>), else the time value would be parsed as an option. See below for an example. </p>
<p> When using negative time values, options and data have to be separated by two dashes (<code>&#8212;</code>), else the time value would be parsed as an option. See below for an example. </p>
<p> The remaining elements of the argument are <font SIZE="-1">DS</font> updates. The order of this list is the same as the order the data sources were defined in the <font SIZE="-1">RRA</font>. If there is no data for a certain data-source, the letter <code>U</code> (e.g., N:0.1:U:1) can be specified. </p>
<p> The format of the value acquired from the data source is dependent on the data source type chosen. Normally it will be numeric, but the data acquisition modules may impose their very own parsing of this parameter as long as the colon (<code>:</code>) remains the data source value separator.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables may be used to change the behavior of <tt>&quot;rrdtool update&quot;</tt>:</p>
<dl>
<dt><font SIZE="-1"><code>RRDCACHED_ADDRESS</code></font></p>
<dd> If this environment variable is set it will have the same effect as specifying the <tt>&quot;--daemon&quot;</tt> option on the command line. If both are present, the command line argument takes precedence.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;rrdtool update demo1.rrd N:3.44:3.15:U:23&quot;</tt> </p>
<p> Update the database file demo1.rrd with 3 known and one <i>*UNKNOWN*</i> value. Use the current time as the update time.</p>
<dt>&bull;</p>
<dd> <tt>&quot;rrdtool update demo2.rrd 887457267:U 887457521:22 887457903:2.7&quot;</tt> </p>
<p> Update the database file demo2.rrd which expects data from a single data-source, three times. First with an <i>*UNKNOWN*</i> value then with two regular readings. The update interval seems to be around 300 seconds.</p>
<dt>&bull;</p>
<dd> <tt>&quot;rrdtool update demo3.rrd -- -5:21 N:42&quot;</tt> </p>
<p> Update the database file demo3.rrd two times, using five seconds in the past and the current time as the update times.</p>
<dt>&bull;</p>
<dd> <tt>&quot;rrdtool update --cache /var/lib/rrd/demo3.rrd N:42&quot;</tt> </p>
<p> Update the file <tt>&quot;/var/lib/rrd/demo3.rrd&quot;</tt> with a single data source, using the current time. If the caching daemon cannot be reached, do <code>not</code> fall back to direct file access.</p>
<dt>&bull;</p>
<dd> <tt>&quot;rrdtool update --daemon unix:/tmp/rrdd.sock demo4.rrd N:23&quot;</tt> </p>
<p> Use the <font SIZE="-1">UNIX</font> domain socket <tt>&quot;/tmp/rrdd.sock&quot;</tt> to contact the caching daemon. If the caching daemon is not available, update the file <tt>&quot;demo4.rrd&quot;</tt> directly. <font SIZE="-1"><code>WARNING:</code></font> Since a relative path is specified, the following disturbing effect may occur: If the daemon is available, the file relative to the working directory <code>of the daemon</code> is used. If the daemon is not available, the file relative to the current working directory of the invoking process is used. <code>This may update two different files depending on whether the daemon could be reached or not.</code> Don&#8217;t do relative paths, kids!</dl>
<h2>AUTHORS</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;, Florian Forster &lt;octo at verplant.org&gt; </p>
<h2>Index</h2>
