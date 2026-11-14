---
title: "ddupdate(8)"
name: "ddupdate"
section: "8"
letter: "d"
url: "/docs/linux/man/8-ddupdate/"
description: "ddupdate – Update dns data for dynamic IP addresses"
---

<p><code>ddupdate</code> &#8211; Update dns data for dynamic IP addresses</p>
<h2>Synopsis</h2>
<p><code>ddupdate</code> [<i>options</i>]</p>
<h2>Description</h2>
<p>A tool to update dynamic IP addresses typically obtained using DHCP with dynamic DNS service providers such as changeip.com, duckdns.org or no-ip.com. It makes it possible to access a machine with a fixed name like myhost.duckdns.org even if the ip address changes. <code>ddupdate</code> caches the address, and only attempts the update if the address actually is changed. The tool has a plugin structure with plugins for obtaining the actual address (typically hardware-dependent) and to update it (service dependent). The normal usecase is to specify all commandline options in the config file. However, all options in this file could be overridden by actual command line options e. g., while testing. Using service providers and possibly also firewalls requires use of username/password credentials. For these, the <a href="/docs/linux/man/5-netrc/">netrc</a>(5) file is used. <code>ddupdate</code> is distributed with systemd support to run at regular intervals, and with NetworkManager templates to run when interfaces goes up or down. It fully supports ipv6 addresses and also using proxies (see ENVIRONMENT). </p>
<h2>Options</h2>
<p>Options for normal operation, typically defined in config file: </p>
<dl>
<dt><code>-H, &#8211;hostname</code> &lt;<i>hostname</i>&gt;</p>
<dd>Hostname to update, typically fully qualified. Defaults to the not really usable host.nowhere.net </p>
<dt><code>-s, &#8211;service-plugin</code> &lt;<i>plugin</i>&gt;</p>
<dd>Plugin used to update the dns data for the address obtained from the address-plugin. Defaults to dry-run, which just prints the address. Use <i>&#8211;list-services</i> to list available plugins. </p>
<dt><code>-a, &#8211;address-plugin</code> &lt;<i>plugin</i>&gt;</p>
<dd>Plugin used to obtain the actual ip address. Defaults to default-if, which localizes the default interface using /usr/sbin/ip and uses it&#8217;s primary address. Use <i>&#8211;list-addressers</i> to list available plugins. </p>
<dt><code>-v, &#8211;ip-version</code> &lt;<i>v4</i>|<i>v6</i>|<i>all</i>&gt;</p>
<dd>The kind of ip addresses to register. The addresses obtained by the address-plugin could be either v6, v4 or both. However, the actual addresses sent to the service plugin is filtered using this option so for example an unused ipv6 address not becomes an official address to the host. Defaults to <i>v4</i>. </p>
<dt><code>-L, &#8211;loglevel</code> [<i>level</i>]</p>
<dd>Determine the amount of logging information. <i>level</i> is a symbolic syslog level: <i>error</i>,<i>warning, info</i>, or <i>debug</i>. It defaults to <i>warning</i>. </p>
<dt><code>-o, &#8211;service-option</code> &lt;<i>plugin option</i>&gt;</p>
<dd>Option interpreted by service plugin, documented in <i>&#8211;help &lt;plugin&gt;</i>. May be given multiple times as required. Any option on the command line will clear the list of options as of the config file. See PLUGIN OPTIONS. </p>
<dt><code>-O, &#8211;address-option</code> &lt;<i>plugin option</i>&gt;</p>
<dd>Option interpreted by address-plugin. See <i>&#8211;service-option</i> and PLUGIN OPTIONS. </p>
</dl>
<p> Other options: </p>
<dl>
<dt><code>-c, &#8211;config-file</code> &lt;<i>path</i>&gt;</p>
<dd>File containing default values for all command line options. The path must be absolute. An example file is distributed with the sources. See [FILES] below. </p>
<dt><code>-f, &#8211;force</code></p>
<dd>Force <code>ddupdate</code> to run even if the cached value is still valid. </p>
<dt><code>-h, &#8211;help [plugin] </code></p>
<dd>Print help. If given a plugin argument, prints help for this plugin. </p>
<dt><code>-S, &#8211;list-services</code></p>
<dd>List service provider plugins. </p>
<dt><code>-A, &#8211;list-addressers</code></p>
<dd>List plugins providing one or more ip addresses </p>
<dt><code>-V, &#8211;version</code></p>
<dd>Print <code>ddupdate</code> version. </p>
</dl>
<h2>Plugin Options</h2>
<p>The plugin options are generally just handed to the plugins without any further interpretation. An option is either a single keyword or a <i>key=value</i> string. No whitespace is allowed in <i>key</i> or <i>value</i>.</p>
<h2>Plugin Loading</h2>
<p><code>ddupdate</code> looks for a directory named <i>plugins</i> and tries to load plugins from all files in this directory. The search for <i>plugins</i> is done, in descending priority:</p>
<dl>
<dt>&bull;</p>
<dd>The directory <i>plugins</i> in the same directory as the main.py module. This is the development case, and the highest priority.</p>
<dt>&bull;</p>
<dd>User plugins are searched in <i>~/.local/share/ddupdate/plugins</i>. Setting the XDG_DATA_HOME environment relocates this to <i>$XDG_DATA_HOME/ddupdate/plugins</i></p>
<dt>&bull;</p>
<dd>The directories listed in the XDG_DATA_DIRS environment variable, by default <i>/usr/local/share:/usr/share</i>, are searched for <i>ddupdate/plugins</i>. </p>
</dl>
<h2>Examples</h2>
<p>Please note that the command line options are normally stored in <i>/etc/ddupdate.conf</i>, allowing an invocation without command line options. Update on dyndns.com using the external address as seen from the internet, displaying the address used: </p>
<pre> ddupdate -a default-web-ip -s dtdns.com -H myhost.dyndns.org -l info</pre>
<p>Make a debug run without actually updating, displaying the address on the local, default interface: </p>
<pre> ddupdate -a default-if -s dry-run --loglevel info -H host.dyndns.org</pre>
<h2>Environment</h2>
<p><code>ddupdate</code> respects the data paths defined by freedesktop.org. </p>
<dl>
<dt><code>XDG_CACHE_HOME</code></p>
<dd>Locates the cached addresses files. See FILES. </p>
<dt><code>XDG_DATA_HOME</code></p>
<dd>Locates user plugins. See PLUGIN LOADING. </p>
<dt><code>XDG_DATA_DIRS</code></p>
<dd>Involved in system plugins, see PLUGIN LOADING. </p>
<dt><code>XDG_CONFIG_HOME</code></p>
<dd>User configuration file parent directory location, defaults to <i>~/.config</i>.</dl>
<p> <code>ddupdate</code> also accepts the standard proxy environment: </p>
<dl>
<dt><code>http_proxy, https_proxy</code></p>
<dd>URL to used proxies for http and https connections. The systemd service files distributed has provisions to define these as required. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><code>~/.netrc</code></p>
<dd>Used to store username and password for logging in to service providers to update, firewalls to get the IP address etc. See <a href="/docs/linux/man/5-netrc/">netrc</a>(5) for the format used. The file must have restricted permissions like 600 to be accepted.</p>
<dt><code>/etc/netrc</code></p>
<dd>Fallback location for credentials when <i>~/.netrc</i> is not found.</p>
<dt><code>~/.config/ddupdate.conf</code></p>
<dd>Default config file location. If defined, the XDG_CONFIG_HOME variable relocates this to <i>$XDG_CONFIG_HOME/ddupdate.conf</i>.</p>
<dt><code>/etc/ddupdate.conf</code></p>
<dd>Fallback configuration file location.</p>
<dt><code>/usr/share/ddupdate/plugins</code></p>
<dd>Default directory for upstream plugins, see PLUGIN LOADING.</p>
<dt><code>/usr/local/share/ddupdate/plugins</code></p>
<dd>Default directory for site plugins, see PLUGIN LOADING.</p>
<dt><code>~/.local/share/ddupdate/plugins</code></p>
<dd>Default directory for user plugins, see PLUGIN LOADING.</p>
<dt><code>~/.cache/ddupdate/*</code></p>
<dd>Cached address from last update with an actual change, one for each update service. Setting the XDG_CACHE_HOME environment variable relocates these files to $XDG_CACHE_HOME/ddupdate/*. </p>
</dl>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/5-ddupdate-conf/">ddupdate.conf</a>(5)</code></p>
<dd>Configuration file</p>
<dt><code><a href="/docs/linux/man/5-netrc/">netrc</a>(5)</code></p>
<dd>Authentication tokens file, originally used by <a href="/docs/linux/man/1-ftp/">ftp</a>(1).</p>
<dt><code><a href="/docs/linux/man/8-ddupdate-config/">ddupdate-config</a>(8)</code></p>
<dd>Configuration tool</p>
<dt><code><a rel="nofollow" href="https://github.com/leamas/ddupdate">https://github.com/leamas/ddupdate</a></code></p>
<dd>Project homesite and README </p>
