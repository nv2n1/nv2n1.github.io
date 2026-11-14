---
title: "pipewire-conf(5)"
name: "pipewire-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pipewire-conf/"
description: "pipewire.conf – The PipeWire server configuration file"
---

<p>pipewire.conf &#8211; The PipeWire server configuration file</p>
<h2>Synopsis</h2>
<p><i>$XDG_CONFIG_HOME/pipewire/pipewire.conf</i> </p>
<p> <i>/etc/pipewire/pipewire.conf</i> </p>
<p> <i>/usr/share/pipewire/pipewire.conf</i> </p>
<p> <i>/usr/share/pipewire/pipewire.conf.d/</i> </p>
<p> <i>/etc/pipewire/pipewire.conf.d/</i> </p>
<p> <i>$XDG_CONFIG_HOME/pipewire/pipewire.conf.d/</i></p>
<h2>Description</h2>
<p>PipeWire is a service that facilitates sharing of multimedia content between devices and applications. </p>
<p> On startup, the daemon reads a main configuration file to configure itself. It executes a series of commands listed in the config file. </p>
<p> The config files are loaded in the order listed in the <i>SYNOPSIS</i>. The environment variables <code>PIPEWIRE_CONFIG_DIR</code>, <code>PIPEWIRE_CONFIG_PREFIX</code> and <code>PIPEWIRE_CONFIG_NAME</code> can be used to specify an alternative config directory, subdirectory and file respectively. </p>
<p> Next to the configuration file can be a directory with the same name as the file with a <code>.d/</code> suffix. All directories in the <i>SYNOPSIS</i> directory search paths are traversed in the listed order and the contents of the <code>*.conf</code> files inside them are appended to the main configuration file as overrides. Object sections are merged and array sections are appended.</p>
<h2>Configuration File Format</h2>
<p>The configuration file format is grouped into sections. A section is either a dictionary, {}, or an array, []. Dictionary and array entries are separated by whitespace and may be simple value assignment, an array or a dictionary. For example: </p>
<p> name = value # simple assignment </p>
<p> name = { key1 = value1 key2 = value2 } # a dictionary with two entries </p>
<p> name = [ value1 value2 ] # an array with two entries </p>
<p> name = [ { k = v1 } { k = v2 } ] # an array of dictionaries </p>
<p> The configuration files can be expressed in full JSON syntax but for ease of use, a relaxed format may be used where:</p>
<dl>
<dt>&bull;</p>
<dd><code>:</code> to delimit keys and values can be substuted by <code>=</code> or a space.</p>
<dt>&bull;</p>
<dd>
<dt> around keys and string can be omited as long as no special characters</p>
<dd>are used in the strings.</p>
<dt>&bull;</p>
<dd><code>,</code> to separate objects can be replaced with a whitespace character.</p>
<dt>&bull;</p>
<dd><code>#</code> can be used to start a comment until the line end</dl>
<h2>Configuration File Sections</h2>
<dl>
<dt><code>context.properties</code></p>
<dd>Dictionary. These properties configure the PipeWire instance.</p>
<dt><code>context.spa-libs</code></p>
<dd>Dictionary. Maps plugin features with globs to a spa library.</p>
<dt><code>context.modules</code></p>
<dd>Array of dictionaries. Each entry in the array is a dictionary with the <i>name</i> of the module to load, including optional <i>args</i> and <i>flags</i>. Most modules support being loaded multiple times.</p>
<dt><code>context.objects</code></p>
<dd>Array of dictionaries. Each entry in the array is a dictionary containing the <i>factory</i> to create an object from and optional extra arguments specific to that factory.</p>
<dt><code>context.exec</code></p>
<dd>Array of dictionaries. Each entry in the array is dictionary containing the <i>path</i> of a program to execute on startup and optional <i>args</i>. </p>
<p> This array used to contain an entry to start the session manager but this mode of operation has since been demoted to development aid. Avoid starting a session manager in this way in production environment.</dl>
<h2>Authors</h2>
<p>The PipeWire Developers &lt;<i><a rel="nofollow" href="https://gitlab.freedesktop.org/pipewire/pipewire/issues">https://gitlab.freedesktop.org/pipewire/pipewire/issues</a></i>&gt;; PipeWire is available from <i><a rel="nofollow" href="https://pipewire.org">https://pipewire.org</a></i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pipewire/">pipewire</a>(1)</code>, <code><a href="/docs/linux/man/1-pw-mon/">pw-mon</a>(1)</code>, </p>
