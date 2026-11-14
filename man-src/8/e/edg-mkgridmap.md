---
title: "edg-mkgridmap(8)"
name: "edg-mkgridmap"
section: "8"
letter: "e"
url: "/docs/linux/man/8-edg-mkgridmap/"
description: "edg-mkgridmap – a tool to build the grid-mapfile"
---

<p>edg-mkgridmap &#8211; a tool to build the grid-mapfile</p>
<h2>Synopsis</h2>
<p><code>edg-mkgridmap</code> [<code>&#8211;help</code>] [<code>&#8211;version</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;conf</code>=<i>config_file</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;output</code>[=<i>output_file</i>]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;quiet</code>]&nbsp;<wbr>[<code>&#8211;verbose</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;safe</code>]&nbsp;<wbr>[<code>&#8211;nosafe</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;cache</code>]&nbsp;<wbr>[<code>&#8211;nocache</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;proxy</code>]&nbsp;<wbr>[<code>&#8211;noproxy</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;usermode</code>]</p>
<h2>Description</h2>
<p><code>edg-mkgridmap</code> is a tool to build the grid-mapfile from <font SIZE="-1">VO</font> servers, taking into account both <font SIZE="-1">VO</font> and local policies.</p>
<h2>Configuration</h2>
<p><i>edg-mkgridmap.conf</i> file contains configuration information for <code>edg-mkgridmap</code>. </p>
<p> The syntax of the <i>edg-mkgridmap.conf</i> file is discussed seperately. The <i><a href="/docs/linux/man/5-edg-mkgridmap-conf/">edg-mkgridmap.conf</a></i>(5) documentation should be consulted for detailed reference information. </p>
<p> The default location is <i>/etc/edg-mkgridmap.conf</i>. </p>
<p> The file essentially consists of a list of directives composed by a keyword and one or more arguments. Optional arguments are put in square brackets.</p>
<dl>
<dt>* <code>group</code> <i></i><font SIZE="-1"><i>URI</i></font><i></i> <i>[lcluser]</i></p>
<dd>
<dt>* <code>default_lcluser</code> <i>default_lcluser</i></p>
<dd>
<dt>* <code>auth</code> <i></i><font SIZE="-1"><i>URI</i></font><i></i></p>
<dd>
<dt>* <code>allow</code>|<code>deny</code> <i>pattern_to_match</i></p>
<dd>
<dt>* <code>gmf_local</code> <i>grid-mapfile-local</i></p>
<dd></dl>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Print a summary of the command line options end exit.</p>
<dt><code>&#8211;version</code></p>
<dd>Print the version of <code>edg-mkgridmap</code> end exit.</p>
<dt><code>&#8211;conf</code>=<i>config_file</i></p>
<dd>Specifies the configuration file that is used by <code>edg-mkgridmap</code>. If omitted, <code>edg-mkgridmap</code> checks <i>/var/lib/edg-mkgridmap/etc/edg-mkgridmap.conf</i> to see if a machine-specific configuration has been setup. If such a file is not present, <code>edg-mkgridmap</code> uses the default configuration file <i>/etc/edg-mkgridmap.conf</i>.</p>
<dt><code>&#8211;output</code>[=<i>output_file</i>]</p>
<dd>Specifies the output file. If omitted, <i>stdout</i> is used. If the optional argument <i>output_file</i> is omitted, the value of the environment variable <font SIZE="-1"><code>GRIDMAP</code></font> is used. If <font SIZE="-1"><code>GRIDMAP</code></font> is not set, then the default value <i>/etc/grid-security/grid-mapfile</i> is used.</p>
<dt><code>&#8211;quiet</code></p>
<dd>Turn off error messages.</p>
<dt><code>&#8211;verbose</code></p>
<dd>Print lots of useful informations. Ignored if <code>&#8211;quiet</code> is specified.</p>
<dt><code>&#8211;safe</code>, <code>&#8211;nosafe</code></p>
<dd>Per <code>group</code> keep (<code>&#8211;safe</code>) or remove (<code>&#8211;nosafe</code>) the old grid-mapfile entries that are not found back, when at least one of the sources for that <code>group</code> directive had a problem. Default is remove (<code>&#8211;nosafe</code>).</p>
<dt><code>&#8211;cache</code>, <code>&#8211;nocache</code></p>
<dd>Disable (<code>&#8211;cache</code>) or enable (<code>&#8211;nocache</code>) the grid-mapfile update when its contents remain unchanged. Default is enable (<code>&#8211;nocache</code>).</p>
<dt><code>&#8211;proxy</code>, <code>&#8211;noproxy</code></p>
<dd>Enable (<code>&#8211;proxy</code>) or disable (<code>&#8211;noproxy</code>) proxy support for <font SIZE="-1">HTTP/HTTPS</font> and <font SIZE="-1">VOMS/VOMSS</font> connections. Default is disable (<code>&#8211;noproxy</code>). </p>
<p> The proxy support must be configured through appropriate environmental variables.</p>
<dt><code>&#8211;usermode</code></p>
<dd>Facilitate running the script as an ordinary user by having the relevant environment variables point to the user&#8217;s X509 proxy instead of using the personal certificate and key. The user&#8217;s proxy is taken from the <code>X509_USER_PROXY</code> environment variable, if defined, else from the default location <i>/tmp/x509up_u$UID</i>.</dl>
<h2>Errors</h2>
<p>In case of one or more errors, <code>edg-mkgridmap</code> returns an exit code which is computed adding these possible values:</p>
<dl>
<dt>* <code>1</code></p>
<dd>per <code>group</code> directive for which a server could not be contacted.</p>
<dt>* <code>16</code></p>
<dd>error reading the configuration file.</p>
<dt>* <code>32</code></p>
<dd>error writing the grid-mapfile.</p>
<dt>* <code>64</code></p>
<dd>error with a <code>group</code> directive.</p>
<dt>* <code>128</code></p>
<dd>error with an <code>auth</code> directive.</dl>
<h2>Diagnostics</h2>
<p>The <code>&#8211;verbose</code> option produces some useful diagnostics. </p>
<p> Any error message generated by <code>edg-mkgridmap</code> is logged to the <code>syslogd</code>.</p>
<h2>Environment</h2>
<dl>
<dt><font SIZE="-1"><code>EDG_MKGRIDMAP_OPTIONS</code></font></p>
<dd>Used to specify command line options.</p>
<dt><font SIZE="-1"><code>GRIDMAP</code></font></p>
<dd>Used to determine the location of the grid-mapfile. If not set, then the default value <i>/etc/grid-security/grid-mapfile</i> is used.</p>
<dt><font SIZE="-1"><code>CERTDIR</code></font></p>
<dd>Used to determine the directory containing <font SIZE="-1">CA</font> certificates. If not set, then the default value <i>/etc/grid-security/certificates</i> is used.</p>
<dt><code>X509_USER_CERT</code></p>
<dd>Used to determine the location of the host certificate. If not set, then the default value <i>/etc/grid-security/hostcert.pem</i> is used.</p>
<dt><code>X509_USER_KEY</code></p>
<dd>Used to determine the location of the host private key. If not set, then the default value <i>/etc/grid-security/hostkey.pem</i> is used.</p>
<dt><code>X509_USER_PROXY</code></p>
<dd>Used to determine the location of the user&#8217;s proxy when the <code>&#8211;usermode</code> option is given. If not set, the default value <i>/tmp/x509up_u$UID</i> is used.</p>
<dt><code>http_proxy</code></p>
<dd>Used to determine the proxy for <font SIZE="-1">HTTP</font> connections. The syntax is: </p>
<pre> http_proxy=&quot;[<a rel="nofollow" href="http://]">http://]</a>&lt;host&gt;:&lt;port&gt;&quot;</pre>
<dt><code>https_proxy</code></p>
<dd>Used to determine the proxy for <font SIZE="-1">HTTPS</font> connections. The syntax is: </p>
<pre> https_proxy=&quot;[<a rel="nofollow" href="http://]">http://]</a>&lt;host&gt;:&lt;port&gt;&quot;</pre>
</dl>
<h2>Examples</h2>
<pre> edg-mkgridmap</pre>
<p>Writes the grid-mapfile to the standard output. </p>
<pre> edg-mkgridmap --output=-</pre>
<p>Writes the grid-mapfile to the standard output. </p>
<pre> edg-mkgridmap --output</pre>
<p>Writes the grid-mapfile to the default location of the grid-mapfile. </p>
<pre> edg-mkgridmap --output=&lt;output_file&gt;</pre>
<p>Writes the grid-mapfile to &lt;output_file&gt;.</p>
<h2>Files</h2>
<p><i>/var/lib/edg-mkgridmap/etc/edg-mkgridmap.conf</i> </p>
<p> <i>/etc/edg-mkgridmap.conf</i> </p>
<p> <i>/usr/libexec/edg-mkgridmap/local-subject2user</i></p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-edg-mkgridmap-conf/">edg-mkgridmap.conf</a></i>(5)</p>
<h2>Authors</h2>
<p><font SIZE="-1">EU</font> DataGrid Authorization Working Group, <font SIZE="-1">EGEE</font> Middleware Security Group, Maarten Litmaath (<font SIZE="-1">CERN/WLCG</font>)</p>
