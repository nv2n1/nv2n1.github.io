---
title: "flatpak-installation(5)"
name: "flatpak-installation"
section: "5"
letter: "f"
url: "/docs/linux/man/5-flatpak-installation/"
description: "flatpak-installation – Configuration for an installation location"
---

<p>flatpak-installation &#8211; Configuration for an installation location</p>
<h2>Description</h2>
<p>flatpak can operate in system-wide or per-user mode. The system-wide data is located in $prefix/var/lib/flatpak/, and the per-user data is in $HOME/.local/share/flatpak/. </p>
<p> In addition to the default installation locations, more system-wide installations can be defined via configuration files /etc/flatpak/installations.d/, which must have the .conf extension and follow the format described below.</p>
<h2>File Format</h2>
<p>The installation config file format is using the same .ini file format that is used for systemd unit files or application .desktop files.</p>
<h3>[Installation &#8230;]</h3>
<p>All the configuration for the the installation location with name NAME is contained in the [Installation &quot;NAME&quot;] group. </p>
<p> The following keys are recognized: </p>
<p> <code>Path</code> (string)</p>
<dl>
<dd>The path for this installation. This key is mandatory.</dl>
<p> <code>DisplayName</code> (string)</p>
<dl>
<dd>The name to use when showing this installation in the UI.</dl>
<p> <code>Priority</code> (integer)</p>
<dl>
<dd>A priority for this installation.</dl>
<p> <code>StorageType</code> (string)</p>
<dl>
<dd>The type of storage used for this installation. Possible values include: network, mmc, sdcard, harddisk.</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre>[Installation &quot;extra&quot;]
Path=/location/of/sdcard
DisplayName=Extra Installation
StorageType=sdcard</pre>
</dl>
