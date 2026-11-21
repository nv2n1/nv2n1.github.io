---

title: "ctan-o-mat(1)"
name: "ctan-o-mat"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctan-o-mat/"
description: "ctan-o-mat – Validate and upload a package for CTAN"
---

<p> ctan-o-mat [options] [&lt;package configuration&gt;]</p>
<p> This program can be used to automate the upload of a package to the Comprehensive TeX Archive Network (<a rel="nofollow" href="https://www.ctan.org">https://www.ctan.org</a>). The description of the package is taken from a configuration file. Thus it can be updated easily without the need to fill a Web form with the same old information again and again. </p>
<p> The provided information is validated in any case. If the validation succeeds and not only the validation is requested then the provided archive file is placed in the incoming area of the <font SIZE="-1">CTAN</font> for further processing by the <font SIZE="-1">CTAN</font> team. </p>
<p> In any case any finding during the validation is reported at the end of the processing. Note that the validation is the default and a official submission has to be requested by the an appropriate command line option. </p>
<p> <code>ctan-o-mat</code> requires an Internet connection to the <font SIZE="-1">CTAN</font> server. Even the validation retrieves the known attributes and the basic constraints from the server.</p>
<h2>CONFIGURATION</h2>
<p> The default configuration is read from a file with the same name as the current directory an the extension .pkg. This file name can be overwritten on the command line. </p>
<p> The configuration depends on the features currently supported by the <font SIZE="-1">CTAN</font> server. Since these features can change over time the configuration is not hard-coded in <code>ctan-o-mat</code>. You can request an empty template of the configuration via the command line parameter <tt>&quot;--init&quot;</tt>.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-h</dt>
<dd>
</dd><dt>&#8211;help</dt>
<dd> Print this short summary about the usage and exit the program.</dd>
<dt>-i</dt>
<dd>
</dd><dt>&#8211;init</dt>
<dd> Create an empty template for a configuration.</dd>
<dt>&#8211;list licenses</dt>
<dd> List the known licenses of <font SIZE="-1">CTAN</font> to the standard output stream. Each license is represented as one line. The line contains the fields key, name, free indicator. Those fields are separated by tab characters. Afterwards the program terminates without processing any further arguments.</dd>
<dt>&#8211;config &lt;package configuration&gt;</dt>
<dd>
</dd><dt>&#8211;pkg &lt;package configuration&gt;</dt>
<dd>
</dd><dt>&#8211;package &lt;package configuration&gt;</dt>
<dd> Set the package configuration file.</dd>
<dt>-s</dt>
<dd>
</dd><dt>&#8211;submit</dt>
<dd> Upload the submission, validate it and officially submit it to <font SIZE="-1">CTAN</font> it the validation succeeds.</dd>
<dt>-v</dt>
<dd>
</dd><dt>&#8211;verbose</dt>
<dd> Print some more information during the processing (verbose mode).</dd>
<dt>&#8211;version</dt>
<dd> Print the version number of this program and exit.</dd>
<dt>&#8211;validate</dt>
<dd>
</dd><dt>-n</dt>
<dd>
</dd><dt>&#8211;noaction</dt>
<dd> Do not perform the final upload. The package is validated and the resulting messages are printed.</dd>
<dt>&lt;package&gt;</dt>
<dd> This parameter is the name of a package configuration (see section <font SIZE="-1">CONFIGURATION</font>) contained in a file. If not set otherwise the package configuration defaults to the name of the current directory with <tt>&quot;.pkg&quot;</tt> appended.</dd></dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables are recognized by <code>ctan-o-mat</code>.</p>
<dl>
<dt><font SIZE="-1">CTAN_O_MAT_URL</font></dt>
<dd> The value is the <font SIZE="-1">URL</font> prefix for the <font SIZE="-1">CTAN</font> server to be contacted. The default is <tt>&quot;<a rel="nofollow" href="https://ctan.org/submit">https://ctan.org/submit</a>&quot;</tt>. The complete <font SIZE="-1">URL</font> is constructed by appending <tt>&quot;validate&quot;</tt>, <tt>&quot;upload&quot;</tt>, or <tt>&quot;fields&quot;</tt> to use the respective <font SIZE="-1">CTAN REST API.</font></dd></dl>
<h2>CONNECTING VIA PROXIES</h2>
<p> If you need to connect to the Internet via a proxy then this can be achieved by setting some environment variables before running <code>ctan-o-mat</code>. To redirect the request via the proxy simply define an environment variable <tt>&quot;http_proxy&quot;</tt> to point to the proxy host &#8212; including protocol and port as required. Note that the name of the environment variable is supposed to be in <code>lower</code> case.</p>
<h2>AUTHOR</h2>
<p> Gerd Neugebauer (gene [at] gerd-neugebauer.de)</p>
<h2>BUGS</h2>
<dl>
<dt>&bull;</dt>
<dd> The program can not be used without a working connection to the Internet. </dd>
</dl>
