---
title: "reporter-bugzilla(1)"
name: "reporter-bugzilla"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reporter-bugzilla/"
description: "reporter-bugzilla – Reports problem to Bugzilla."
---

<h2 class="name">NAME</h2>
<p> reporter-bugzilla &#8211; Reports problem to Bugzilla. </p>
<h2>SYNOPSIS</h2>
<p> <i>reporter-bugzilla</i> [-vbf] [-g GROUP]&#8230; [-c CONFFILE]&#8230; [-F FMTFILE] [-A FMTFILE2] -d DIR </p>
<p> Or: </p>
<p> <i>reporter-bugzilla</i> [-v] [-c CONFFILE]&#8230; [-d DIR] -t[ID] FILE&#8230; </p>
<p> Or: </p>
<p> <i>reporter-bugzilla</i> [-v] [-c CONFFILE]&#8230; [-d DIR] -t[ID] -w </p>
<p> Or: </p>
<p> <i>reporter-bugzilla</i> [-v] [-c CONFFILE]&#8230; -h DUPHASH</p>
<h2>DESCRIPTION</h2>
<p> The tool reads problem directory DIR. Then it logs in to Bugzilla and tries to find a bug with the same abrt_hash:HEXSTRING in <i>Whiteboard</i>. </p>
<p> If such bug is not found, then a new bug is created. Elements of DIR are stored in the bug as part of bug description or as attachments, depending on their type and size. </p>
<p> Otherwise, if such bug is found and it is marked as CLOSED DUPLICATE, the tool follows the chain of duplicates until it finds a non-DUPLICATE bug. The tool adds a new comment to found bug. </p>
<p> The URL to new or modified bug is printed to stdout and recorded in <i>reported_to</i> element in DIR. </p>
<p> Option -t uploads FILEs to the already created bug on Bugzilla site. The bug ID is retrieved from directory specified by -d DIR. If problem data in DIR was never reported to Bugzilla, upload will fail. </p>
<p> Option -tID uploads FILEs to the bug with specified ID on Bugzilla site. -d DIR is ignored. </p>
<p> Option -w adds bugzilla user to bug&#8217;s CC list. </p>
<p> Option -r sets the last url from reporter_to element which is prefixed with TRACKER_NAME to URL field. This option is applied only when a new bug is to be filed. The default value is <i>ABRT Server</i>&quot;</p>
<h3>Configuration file</h3>
<p> If not specified, CONFFILE defaults to /etc/libreport/plugins/bugzilla.conf. Configuration file lines should have <i>PARAM = VALUE</i> format. The parameters are: </p>
<p> <i>Login</i></p>
<dl>
<dt>
<dd> Login to Bugzilla account.</dl>
<p> <i>Password</i></p>
<dl>
<dt>
<dd> Password to Bugzilla account.</dl>
<p> <i>BugzillaURL</i></p>
<dl>
<dt>
<dd> Bugzilla HTTP(S) address. (default: m[blue]<code><a rel="nofollow" href="https://bugzilla.redhat.com">https://bugzilla.redhat.com</a></code>m[])</dl>
<p> <i>SSLVerify</i></p>
<dl>
<dt>
<dd> Use yes/true/on/1 to verify server&#8217;s SSL certificate. (default: yes)</dl>
<p> <i>Product</i></p>
<dl>
<dt>
<dd> Product bug field value. Useful if you needed different product than specified in /etc/os-release</dl>
<p> <i>ProductVersion</i></p>
<dl>
<dt>
<dd> Version bug field value. Useful if you needed different product version than specified in /etc/os-release</dl>
<p> Parameters can be overridden via $Bugzilla_PARAM environment variables.</p>
<h3>Formatting configuration files</h3>
<p> Lines starting with # are ignored. </p>
<p> Lines can be continued on the next line using trailing backslash. </p>
<p> Format: </p>
<p> &quot;%summary</p>
<dl>
<dt>
<dd> summary format&quot;</dl>
<p> &quot;section</p>
<dl>
<dt>
<dd> element1[,element2]&#8230;&quot; The literal text line to be added to Bugzilla comment. Can be empty. (Empty lines are NOT ignored!) </p>
<dl>
<dt>
<dd>
<pre><code>
Summary format is a line of text, where % element % is replaced by text element's content, and [[...%element%...]] block is used only if % element % exists.[[...]] blocks can nest.
</code></pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Sections can be:
- %summary: bug summary format string.
- %attach: a list of elements to attach.
- text, double colon (::) and the list of comma-separated elements.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Elements can be:
- problem directory element names, which get formatted as
  &lt;element_name&gt;: &lt;contents&gt;
  or
  &lt;element_name&gt;:
  :&lt;contents&gt;
  :&lt;contents&gt;
  :&lt;contents&gt;
- problem directory element names prefixed by &quot;%bare_&quot;,
  which is formatted as-is, without &quot;&lt;element_name&gt;:&quot; and colons
- %oneline, %multiline, %text wildcards, which select all corresponding
  elements for output or attachment
- %binary wildcard, valid only for %attach section, instructs to attach
  binary elements
- problem directory element names prefixed by &quot;-&quot;,
  which excludes given element from all wildcards
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Nonexistent elements are silently ignored.
If none of elements exists, the section will not be created.
</pre>
</dl>
</dl>
<h3>Integration with ABRT events</h3>
<p> <i>reporter-bugzilla</i> can be used as an ABRT reporter. Example fragment for /etc/libreport/report_event.conf: </p>
<dl>
<dt>
<dd>
<pre>
# Report Python crashes
EVENT=report_Bugzilla analyzer=Python
      reporter-bugzilla -d . -c /etc/libreport/plugins/bugzilla.conf
</pre>
</dl>
<h2>OPTIONS</h2>
<p> -d DIR</p>
<dl>
<dt>
<dd> Path to problem directory.</dl>
<p> -c CONFFILE</p>
<dl>
<dt>
<dd> Path to configuration file.</dl>
<p> -b</p>
<dl>
<dt>
<dd> When creating bug, attach binary files too.</dl>
<p> -f</p>
<dl>
<dt>
<dd> Force reporting even if this problem is already reported.</dl>
<p> -F CONF_FORMAT_FILE</p>
<dl>
<dt>
<dd> Formatting file for initial comment. Default: /etc/libreport/plugins/bugzilla_format.conf</dl>
<p> -A CONF_FORMAT_FILE</p>
<dl>
<dt>
<dd> Formatting file for duplicates. Default: /etc/libreport/plugins/bugzilla_format.conf</dl>
<p> -t[ID]</p>
<dl>
<dt>
<dd> Upload FILEs to the already created bug on Bugzilla site.</dl>
<p> -w</p>
<dl>
<dt>
<dd> Add bugzilla user to CC list [of bug with this ID]. Applicable only with -t.</dl>
<p> -h, &#8211;duphash DUPHASH</p>
<dl>
<dt>
<dd> Search in Bugzilla by abrt&#8217;s DUPHASH and print BUG_ID.</dl>
<p> -g, &#8211;group GROUP</p>
<dl>
<dt>
<dd> When creating a new ticket restrict access to this group only.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> Environment variables take precedence over values provided in the configuration file. </p>
<p> <i>Bugzilla_Login</i></p>
<dl>
<dt>
<dd> Login to Bugzilla account.</dl>
<p> <i>Bugzilla_Password</i></p>
<dl>
<dt>
<dd> Password to Bugzilla account.</dl>
<p> <i>Bugzilla_BugzillaURL</i></p>
<dl>
<dt>
<dd> Bugzilla HTTP(S) address. (default: m[blue]<code><a rel="nofollow" href="https://bugzilla.redhat.com">https://bugzilla.redhat.com</a></code>m[])</dl>
<p> <i>Bugzilla_SSLVerify</i></p>
<dl>
<dt>
<dd> Use yes/true/on/1 to verify server&#8217;s SSL certificate. (default: yes)</dl>
<p> <i>Bugzilla_Product</i></p>
<dl>
<dt>
<dd> Product bug field value. Useful if you needed different product than specified in /etc/os-release</dl>
<p> <i>Bugzilla_ProductVersion</i></p>
<dl>
<dt>
<dd> Version bug field value. Useful if you needed different product version than specified in /etc/os-release</dl>
<p> <i>http_proxy</i></p>
<dl>
<dt>
<dd> the proxy server to use for HTTP</dl>
<p> <i>HTTPS_PROXY</i></p>
<dl>
<dt>
<dd> the proxy server to use for HTTPS</dl>
<h2>FILES</h2>
<p> /usr/share/libreport/conf.d/plugins/bugzilla.conf</p>
<dl>
<dt>
<dd> Readonly default configuration files.</dl>
<p> /etc/libreport/plugins/bugzilla.conf</p>
<dl>
<dt>
<dd> Configuration file.</dl>
<p> /etc/libreport/plugins/bugzilla_format.conf</p>
<dl>
<dt>
<dd> Configure formating for reporting.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-report_event-conf/">report_event.conf</a>(5), <a href="/docs/linux/man/5-bugzilla_format-conf/">bugzilla_format.conf</a>(5)</p>
<h2>AUTHORS</h2>
<dl>
<dt>
<dd> &bull; ABRT team</dl>
<h2>Index</h2>
