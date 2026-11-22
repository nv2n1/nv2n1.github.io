---

title: "pdc_client(1)"
name: "pdc_client"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdc_client/"
description: "pdc_client – work with a PDC instance"
---

<p> pdc_client &#8211; work with a PDC instance</p>
<h2>SYNOPSIS</h2>
<p> <code>pdc_client</code> <code>-s</code> <i>SERVER</i> [<i>OPTIONS</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>pdc_client</code> provides access a given PDC instance for reading and writing data. If you have a Kerberos ticket, it will automatically obtain an access token.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code>, <code>&#8211;server</code>=<i>SERVER</i></dt>
<dd> Set which URL to connect to. There are shortcuts available for RedHat hosted instances (<i>prod</i>, <i>stage</i>, <i>qa</i>, <i>dev</i>). The server URL needs to include path to the API root (usually <i>/rest_api/v1/</i>). This argument is always required.</dd>
<dt><code>-x</code>, <code>&#8211;request</code>=<i>METHOD</i></dt>
<dd> Select which method to perform on the resource. This maps directly to HTTP methods, so <code>GET</code>, <code>POST</code>, <code>PUT</code>, <code>PATCH</code> and <code>DELETE</code> are available. Default is <code>GET</code>.</dd>
<dt><code>-r</code>, <code>&#8211;resource</code>=<i>RESOURCE</i></dt>
<dd> Select which resource to manipulate. If omitted, a list of available resource is printed. For accessing a single instance of a resource, specify <i>RESOURCE_NAME/INSTANCE_ID</i>. The instance identifier depends on what resource you are operating on.</dd>
<dt><code>-d</code>, <code>&#8211;data</code>=<i>DATA</i></dt>
<dd> Specify data to be sent to the server. The data must be formatted as JSON.</dd>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>FILE</i></dt>
<dd> Like <code>-d</code>, but reads data from file instead of command line argument. If <i>FILE</i> is specified as <code>&#8211;</code>, standard input will be read. Only one of <code>-d</code> and <code>-f</code> can be used simultaneously.</dd>
<dt><code>-t</code>, <code>&#8211;traceback</code></dt>
<dd> Print traceback information in case of an error.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Show details about performed requests.</dd></dl>
<h2>FILES</h2>
<p> <i>/etc/pdc/client_config.json</i></p>
<dl>
<dt>
</dt><dd> Site-wide host configuration file. Has to be valid JSON.</dd></dl>
<p> <i>$HOME/.config/pdc/client_config.json</i></p>
<dl>
<dt>
</dt><dd> Personal host configuration file which overrides identical keys from site-wide configuration file.</dd></dl>
<h2>BUGS</h2>
<p> If you find a bug in the client, report at<br/>
 <a rel="nofollow" href="https://github.com/product-definition-center/pdc-client/issues/.">https://github.com/product-definition-center/pdc-client/issues/.</a> </p>
