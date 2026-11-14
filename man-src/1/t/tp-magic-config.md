---
title: "tp-magic-config(1)"
name: "tp-magic-config"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tp-magic-config/"
description: "tp-magic-config — Helps creating ‘Magic’ tool plugins for Tux Paint(1)"
---

<h2>NAME</h2>
<p> tp-magic-config &#8212; Helps creating &#8216;Magic&#8217; tool plugins for Tux <a href="/docs/linux/man/1-paint/">Paint</a>(1) </p>
<h2>SYNOPSYS</h2>
<dl>
<dt><code>tp-magic-config [&#8211;apiversion | &#8211;version | &#8211;cflags | &#8211;pluginprefix | &#8211;plugindocprefix | &#8211;dataprefix | &#8211;localpluginprefix | &#8211;localdataprefix]</code></p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <i>tp-magic-config</i> is a simple shell script that responds with various pieces of information about the currently-installed version of <i>Tux <a href="/docs/linux/man/1-paint/">Paint</a></i>(1) that are useful when building &#8216;Magic&#8217; tool plugins. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;apiversion</code></p>
<dd> Outputs the version of the <i>Tux Paint</i> &#8216;Magic&#8217; tool plugin API that the installed copy of <i>Tux Paint</i> supports. (For API compatibility testing.)</p>
<dt><code>&#8211;version</code></p>
<dd> Outputs the version of <i>Tux Paint</i> that <i>tp-magic-config</i> corresponds to.</p>
<dt><code>&#8211;cflags</code></p>
<dd> Outputs the compiler flags that <i>Tux Paint</i> &#8216;Magic&#8217; tool plugins should be compiled with. (For example, a &quot;-I&quot; include path option that tells the compiler where it can find the plugin API header file, &quot;tp_magic_config.h&quot;, that plugins must #include.)</p>
<dt><code>&#8211;pluginprefix</code></p>
<dd> Outputs the system directory where the installed copy of <i>Tux Paint</i> expects to find &#8216;Magic&#8217; tool plugins (&quot;.so&quot; shared objects). (e.g., &quot;/usr/share/tuxpaint/plugins&quot;)</p>
<dt><code>&#8211;localpluginprefix</code></p>
<dd> Outputs the user directory where the installed copy of <i>Tux Paint</i> expects to find &#8216;Magic&#8217; tool plugins (&quot;.so&quot; shared objects). (e.g., &quot;/home/username/.tuxpaint/plugins&quot;)</p>
<dt><code>&#8211;plugindocprefix</code></p>
<dd> Outputs the directory where the installed copy of <i>Tux Paint</i> expects to find documentation for &#8216;Magic&#8217; tool plugins (&quot;.html&quot; and &quot;.txt&quot; files). <i>Tux Paint&#8217;s</i> main documentation includes a link to this directory under the section on &quot;Magic&quot; tools.</p>
<dt><code>&#8211;dataprefix</code></p>
<dd> Outputs the system directory where the installed copy of <i>Tux Paint</i> keeps its global data files (e.g., &quot;/usr/share/tuxpaint/&quot;). This is the same value that plugins installed system-wide will receive in the &quot;data_directory&quot; string within the &quot;magic_api&quot; structure sent to the plugins&#8217; functions.</p>
<dt><code>&#8211;localdataprefix</code></p>
<dd> Outputs the user directory where the installed copy of <i>Tux Paint</i> expects plugins to install their local data files. (e.g., &quot;/home/username/.tuxpaint/plugins/data&quot;). This is the same value that plugins installed locally will receive in the &quot;data_directory&quot; string within the &quot;magic_api&quot; structure sent to the plugins&#8217; functions. </p>
</dl>
<h2>SYSTEM-WIDE SHELL EXAMPLES</h2>
<p> $ gcc -shared `tp-magic-config &#8211;cflags` my_plugin.c -o my_plugin.so<br />
 # cp my_plugin.so `tp-magic-config &#8211;pluginprefix`<br />
 # cp my_plugin_icon.png `tp-magic-config &#8211;dataprefix`/images/magic<br />
 # cp my_plugin.html `tp-magic-config &#8211;plugindocrefix`/html<br />
 # cp my_plugin.txt `tp-magic-config &#8211;plugindocrefix` </p>
<h2>LOCAL SHELL EXAMPLES</h2>
<p> $ gcc -shared `tp-magic-config &#8211;cflags` my_plugin.c -o my_plugin.so<br />
 $ mkdir -p `tp-magic-config &#8211;localpluginprefix`<br />
 $ cp my_plugin.so `tp-magic-config &#8211;localpluginprefix`<br />
 $ mkdir -p `tp-magic-config &#8211;localdataprefix`/images/magic<br />
 $ cp my_plugin_icon.png `tp-magic-config &#8211;localdataprefix`/images/magic </p>
<h2>SYSTEM-WIDE MAKEFILE EXAMPLE</h2>
<p> MAGIC_CFLAGS=$(shell tp-magic-config &#8211;cflags)<br />
 MAGIC_PREFIX=$(shell tp-magic-config &#8211;pluginprefix)<br />
 MAGIC_DOC_PREFIX=$(shell tp-magic-config &#8211;plugindocprefix)<br />
 DATA_PREFIX=$(shell tp-magic-config &#8211;dataprefix) </p>
<p> all: my_plugin.so </p>
<p> my_plugin.so: my_plugin.c </p>
<p> install: install-so install-data install-docs </p>
<p> install-so:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mkdir -p $(MAGIC_PREFIX)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cp my_plugin.so $(MAGIC_PREFIX)/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>chmod 644 $(MAGIC_PREFIX)/my_plugin.so</p>
<p> install-data:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mkdir -p $(DATA_PREFIX)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cp icons/my_plugin_icon.png $(DATA_PREFIX)/images/magic/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>chmod 644 $(DATA_PREFIX)/images/magic/my_plugin_icon.png</p>
<p> install-docs:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mkdir -p $(MAGIC_DOC_PREFIX)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cp docs/my_plugin.html $(MAGIC_DOC_PREFIX)/html/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>chmod 644 $(MAGIC_DOC_PREFIX)/html/my_plugin.html</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cp docs/my_plugin.txt $(MAGIC_DOC_PREFIX)/</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>chmod 644 $(MAGIC_DOC_PREFIX)/my_plugin.txt</p>
<h2>AUTHOR</h2>
<p> Bill Kendrick. &lt;bill [at] newbreedsoftware.com&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tuxpaint/">tuxpaint</a></code>(1), </p>
<p> And documentation within /usr/[local/]share/doc/tuxpaint/. </p>
<h2>Index</h2>
