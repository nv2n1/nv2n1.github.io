---
title: "netplan-generate(8)"
name: "netplan-generate"
section: "8"
letter: "n"
url: "/docs/linux/man/8-netplan-generate/"
description: "netplan-generate – generate backend configuration from netplan YAML files"
---

<p>netplan-generate &#8211; generate backend configuration from netplan YAML files</p>
<h2>Synopsis</h2>
<p>netplan [-debug] generate -h | -help </p>
<p> netplan [-debug] generate [-root-dir ROOT_DIR] [-mapping MAPPING]</p>
<h2>Description</h2>
<p>netplan generate converts netplan YAML into configuration files understood by the backends (<a href="/docs/linux/man/8-systemd-networkd/">systemd-networkd</a>(8) or <a href="/docs/linux/man/8-networkmanager/">NetworkManager</a>(8)). It does not apply the generated configuration. </p>
<p> You will not normally need to run this directly as it is run by netplan apply, netplan try, or at boot. </p>
<p> For details of the configuration file format, see <a href="/docs/linux/man/5-netplan/">netplan</a>(5).</p>
<h2>Options</h2>
<dl>
<dt><code>-h, -help</code></dt>
<dd>Print basic help.</dd>
<dt><code>-debug</code></dt>
<dd>Print debugging output during the process.</dd>
<dt><code>-root-dir </code>ROOT_DIR</dt>
<dd>Instead of looking in /{lib,etc,run}/netplan, look in /ROOT_DIR/{lib,etc,run}/netplan</dd>
<dt><code>-mapping </code>MAPPING</dt>
<dd>Instead of generating output files, parse the configuration files and print some internal information about the device specified in MAPPING.</dd></dl>
<h2>Handling Multiple Files</h2>
<p>There are 3 locations that netplan generate considers:</p>
<dl>
<dt>&bull;</dt>
<dd>/lib/netplan/*.yaml</dd>
<dt>&bull;</dt>
<dd>/etc/netplan/*.yaml</dd>
<dt>&bull;</dt>
<dd>/run/netplan/*.yaml</dd></dl>
<p> If there are multiple files with exactly the same name, then only one will be read. A file in /run/netplan will shadow &#8211; completely replace &#8211; a file with the same name in /etc/netplan. A file in /etc/netplan will itself shadow a file in /lib/netplan. </p>
<p> Or in other words, /run/netplan is top priority, then /etc/netplan, with /lib/netplan having the lowest priority. </p>
<p> If there are files with different names, then they are considered in lexicographical order &#8211; regardless of the directory they are in. Later files add to or override earlier files. For example, /run/netplan/10-foo.yaml would be updated by /lib/netplan/20-abc.yaml. </p>
<p> If you have two files with the same key/setting, the following rules apply:</p>
<dl>
<dt>&bull;</dt>
<dd>If the values are YAML boolean or scalar values (numbers and strings) the old value is overwritten by the new value.</dd>
<dt>&bull;</dt>
<dd>If the values are sequences, the sequences are concatenated &#8211; the new values are appended to the old list.</dd>
<dt>&bull;</dt>
<dd>If the values are mappings, netplan will examine the elements of the mappings in turn using these rules.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-netplan/">netplan</a>(5), <a href="/docs/linux/man/8-netplan-apply/">netplan-apply</a>(8), <a href="/docs/linux/man/8-netplan-try/">netplan-try</a>(8), <a href="/docs/linux/man/8-systemd-networkd/">systemd-networkd</a>(8), <a href="/docs/linux/man/8-networkmanager/">NetworkManager</a>(8)</p>
<h2>Authors</h2>
<p>Daniel Axtens (&lt;daniel.axtens [at] canonical.com&gt;).</p>
