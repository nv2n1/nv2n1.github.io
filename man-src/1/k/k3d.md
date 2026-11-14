---
title: "k3d(1)"
name: "k3d"
section: "1"
letter: "k"
url: "/docs/linux/man/1-k3d/"
description: "k3d – 3D modeling and animation system"
---

<h2>NAME</h2>
<p> k3d &#8211; 3D modeling and animation system </p>
<h2>SYNOPSIS</h2>
<p> <code>k3d</code> [options] </p>
<h2>DESCRIPTION</h2>
<p> K-3D is a free (as in freedom) 3D modeling, animation, and rendering system for GNU/Linux and Win32. K-3D features a robust, object-oriented plugin architecture and is capable of producing motion-picture-quality output when paired with a RenderMan Interface compliant render engine such as Aqsis. </p>
<p> Please visit <i><a rel="nofollow" href="http://www.k-3d.org">http://www.k-3d.org</a></i> for more information. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;add-path</code> [path]</p>
<dl>
<dt>
<dd> Prepends a filesystem path to the PATH environment variable.</dl>
<p> <code>&#8211;color</code></p>
<dl>
<dt>
<dd> Color-codes log messages based on their priority. Requires an ANSI color-capable terminal.</dl>
<p> <code>&#8211;disable-gl-extension</code> [extension]</p>
<dl>
<dt>
<dd> Disables the given OpenGL extension.</dl>
<p> <code>&#8211;exit</code></p>
<dl>
<dt>
<dd> Exits the program (useful after running scripts in batch mode).</dl>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Prints this help information and exits.</dl>
<p> <code>&#8211;log-level</code> [level]</p>
<dl>
<dt>
<dd> Specifies the minimum message priority to log (valid values are &quot;warning&quot;, &quot;information&quot;, or &quot;debug&quot;).</dl>
<p> <code>&#8211;options</code> [path]</p>
<dl>
<dt>
<dd> Overrides the filepath for storing user options (this overrides both defaults and the K3D_OPTIONS_PATH environment variable, below).</dl>
<p> <code>&#8211;plugins</code> [path]</p>
<dl>
<dt>
<dd> Overrides the path(s) for loading plugin libraries (this overrides both defaults and the K3D_PLUGIN_PATHS environment variable, below). Multiple colon-delimited paths are allowed. Use &quot;&amp;&quot; as a synonym for the default paths.</dl>
<p> <code>&#8211;script </code> [file]</p>
<dl>
<dt>
<dd> Play the given script after startup (use &#8211; for stdin).</dl>
<p> <code>&#8211;shadercache</code> [path]</p>
<dl>
<dt>
<dd> Overrides the path where compiled shaders will be cached (this overrides both defaults and the K3D_SHADER_CACHE_PATH environment variable, below).</dl>
<p> <code>&#8211;share</code> [path]</p>
<dl>
<dt>
<dd> Overrides the path for loading shared data files (this overrides both defaults and the K3D_SHARE_PATH environment variable, below).</dl>
<p> <code>&#8211;show-process</code></p>
<dl>
<dt>
<dd> Prints the process name next to log messages.</dl>
<p> <code>&#8211;show-timestamps</code></p>
<dl>
<dt>
<dd> Prints timestamps next to log messages.</dl>
<p> <code>&#8211;syslog</code></p>
<dl>
<dt>
<dd> Logs messages to syslog.</dl>
<p> <code>-u, &#8211;ui</code> [ui path]</p>
<dl>
<dt>
<dd> Specifies the path to a user interface plugin (this overrides both the default and the K3D_USER_INTERFACE_PATH environment variable, below). As a special-case the string &quot;none&quot; can be used as a synonym for the Null (no gui) User Interface.</dl>
<p> <code>-H, &#8211;user-interface-help</code></p>
<dl>
<dt>
<dd> Prints a user-interface specific help message and exits.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Prints program version information and exits.</dl>
<h2>USER INTERFACE OPTIONS</h2>
<p> <code>&#8211;batch</code></p>
<dl>
<dt>
<dd> Operate in batch (no user intervention) mode.</dl>
<p> <code>-n, &#8211;new</code></p>
<dl>
<dt>
<dd> Creates a new document after startup.</dl>
<p> <code>&#8211;no-custom-layouts</code></p>
<dl>
<dt>
<dd> Disable custom user interface layouts (useful when playing-back recorded tutorials, which rely on the default layout).</dl>
<p> <code>&#8211;no-splash</code></p>
<dl>
<dt>
<dd> Disables the startup splash screen.</dl>
<p> <code>-o, &#8211;open </code> [file]</p>
<dl>
<dt>
<dd> Opens the given file after startup.</dl>
<p> <code>&#8211;show-tutorials</code></p>
<dl>
<dt>
<dd> Opens the tutorials menu immediately following startup.</dl>
<p> <code>&#8211;tutorials</code> [path]</p>
<dl>
<dt>
<dd> Overrides the path for loading interactive tutorials (this overrides both defaults and the K3D_TUTORIALS_PATH environment variable, below).</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>K3D_EXTRA_OPTIONS</code></p>
<dl>
<dt>
<dd> Provides additional options that are appended to the command-line at startup. Note that unlike other K-3D environment variables, options specified via K3D_EXTRA_OPTIONS will override options specified on the command line.</dl>
<p> <code>K3D_OPTIONS_PATH</code></p>
<dl>
<dt>
<dd> Overrides the path for storing user options (this overrides the default, but can be overridden by the &#8211;options option, above).</dl>
<p> <code>K3D_PLUGIN_PATHS</code></p>
<dl>
<dt>
<dd> Overrides the path(s) for loading plugin libraries (this overrides the default, but can be overridden by the &#8211;plugins option, above). Multiple colon-delimited paths are allowed. Use &quot;&amp;&quot; as a synonym for the default paths.</dl>
<p> <code>K3D_SHADER_CACHE_PATH</code></p>
<dl>
<dt>
<dd> Overrides the path where compiled shaders are cached (this overrides the default, but can be overridden by the &#8211;shadercache option, above).</dl>
<p> <code>K3D_SHARE_PATH</code></p>
<dl>
<dt>
<dd> Overrides the path for loading shared data files (this overrides the default, but can be overridden by the &#8211;share option, above).</dl>
<p> <code>K3D_USER_INTERFACE_PATH</code></p>
<dl>
<dt>
<dd> Overrides the path to the user interface plugin (this overrides the default, but can be overridden by the &#8211;ui option, above).</dl>
<h2>AUTHORS</h2>
<p> Written by Timothy M. Shead &lt;tshead [at] k-3d.com&gt;, and many others. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;k3d-development [at] lists.sourceforge.net&gt; </p>
<h2>COPYRIGHT</h2>
<p> This software is licensed under the GNU General Public License; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> The full documentation for K-3D is maintained as an online wiki at <a rel="nofollow" href="http://www.k-3d.org/wiki">http://www.k-3d.org/wiki</a> </p>
<h2>Index</h2>
