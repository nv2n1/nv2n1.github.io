---
title: "lg-conf(5)"
name: "lg-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-lg-conf/"
description: "lg.conf – looking glass configuration file"
---

<p>lg.conf &#8211; looking glass configuration file</p>
<h2>Description</h2>
<p><code>lg.conf</code> contains configuration for the looking glass scripts. </p>
<p> The syntax is that of <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1). It is used to set variables that affect run-time behavior and/or to locate resources.</p>
<h2>Variables</h2>
<p>The following variables are used (alphabetically):</p>
<dl>
<dt><code>LG_AS_REG</code></p>
<dd>*** not implemented.</p>
<dt><code>LG_BGP_RT</code></p>
<dd>Allows show ip bgp neighbor commands that can produce heavy output, such as sh ip bgp neighbor &lt;ip&gt; advertised-routes for a transit customer when the neighbor address is followed by &#8216;advertised-routes&#8217; for the sh ip bgp neighbor query.</p>
<dt><code>LG_CACHE_DIR</code></p>
<dd>Sets the location of the cache directory. The looking glass uses this to hold lock files, log files, and output from cached commands. </p>
<p> Default: ./tmp </p>
<p> Note that the default is relative to the directory where <i>lg.cgi</i> runs in the server&#8217;s document root (e.g.: /usr/local/www/data/lg/tmp).</p>
<dt><code>LG_CACHE_TIME</code></p>
<dd>Sets the number of seconds that the looking glass should cache output from commands that tend to produce a lot of output, such as &#8216;show ip bgp dampened-paths&#8217;. </p>
<p> Default: 600</p>
<dt><code>LG_CLOGINRC</code></p>
<dd>Defines the location of the <code><a href="/docs/linux/man/5-cloginrc/">cloginrc</a></code>(5) that the looking glass should use. The path may be relative to the directory where the CGI scripts run in the server&#8217;s document root. </p>
<p> Default: $HOME/.cloginrc </p>
<p> Note that the .cloginrc must be readable by the user or group that will be running the CGI and that <code><a href="/docs/linux/man/1-clogin/">clogin</a></code>(1) will not allow a world readable <i>.cloginrc</i>. The user is normally that of the http server (httpd).</p>
<dt><code>LG_IMAGE</code></p>
<dd>Defines a html image tag (&lt;img&gt;) which, if defined, will be included at the top of the looking glass pages. It may contain any html as it is simply handed off to print(). </p>
<p> Example: $LG_IMAGE=&quot;&lt;img src=/icons/rancid.gif hspace=0&gt;
 &lt;font size=+2&gt;FOO&lt;/font&gt;&quot;;</p>
<dt><code>LG_INFO</code></p>
<dd>Defines information in html format which, if defined, will be included at the bottom of the looking glass form page. It may contain any html as it is simply handed off to print(). </p>
<p> Example: $LG_INFO=&quot;For Support contact &lt;a href=mailto:webmaster [at] localhost&gt;webmaster&lt;/a&gt;&quot;;</p>
<dt><code>LG_LOG</code></p>
<dd>Defines the fully qualified path name (i.e.: begins with &#8216;/&#8217;) for the log file or the <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) facility to use for logging. For syslog, the argument is the lowercase name of a syslog facility (see syslog.h) without the &#8216;LOG_&#8217; prefix. </p>
<p> Example: local0 </p>
<p> Default: $LG_CACHE_DIR/lg.log</p>
<dt><code>LG_ROUTERDB</code></p>
<dd>Sets the location for the <i>router.db</i> file in rancid&#8217;s <code><a href="/docs/linux/man/5-router-db/">router.db</a></code>(5) format. It lists the devices that should be available to the looking glass users. Only those devices of supported types and with state &#8216;up&#8217; are made available. If not defined and the default file does not exist, the looking glass will compile a list from the router.db files of all the groups present in rancid, that is, the list will be a concatenation of the available <i><a href="/docs/linux/man/5-router-db/">router.db</a></i>(5) files. </p>
<p> Note that if the concatenation method is used, it may be necessary to alter the mode of the router.db files in the rancid group directories, since rancid&#8217;s default umask is 027 (see <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5)).</p>
<dt><code>LG_STRIP</code></p>
<dd>Causes the LG to strip login information from the looking glass results. Since Expect often munges disabling echo when passwords are entered, this is a SECURITY CONCERN! However, this output can be very useful for debugging clogin problems.</p>
<dt><code>LG_STYLE</code></p>
<dd>Defines the URL of a style sheet to be used for HTML formatting.</p>
<dt><code>PATH</code></p>
<dd>Is a colon separated list of directory pathnames in the file system where rancid&#8217;s login scripts, <i><a href="/docs/linux/man/1-clogin/">clogin</a></i>(1) etc.) and programs needed within these, such as <i><a href="/docs/linux/man/1-telnet/">telnet</a></i>(1), are located. Its value is set by configure. Should it be necessary to modify PATH, note that it must include $BASEDIR/bin (see above).</p>
<dt>Queries<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;&#8230;..</p>
<dd></dl>
<h2>Environment</h2>
<dl>
<dt><code>LG_CONF</code></p>
<dd>Location of<br />
 <code>lg.conf</code> file. See the <i>FILES</i> section for more information.</dl>
<h2>Errors</h2>
<p><code>lg.conf</code> is interpreted directly by <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1), so its syntax follows that of perl. Syntax errors may produce quite unexpected results.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/rancid/lg.conf</code></p>
<dd>Configuration file described here. </p>
<p> <code>lg.conf</code> is located by the value of the environment variable LG_CONF, in the CWD (current working directory), or the sysconfdir defined when rancid was installed, in that order.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-cloginrc/">cloginrc</a></code>(5), <code><a href="/docs/linux/man/1-lg_intro/">lg_intro</a></code>(1), <code><a href="/docs/linux/man/5-router-db/">router.db</a></code>(5)</p>
<h2>History</h2>
<p>In RANCID releases prior to 2.3, <code>lg.conf</code> was located in the util/lg sub-directory of the install path. This was changed to be more consistent with common file location practices.</p>
