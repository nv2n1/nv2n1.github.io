---
title: "darktable(1)"
name: "darktable"
section: "1"
letter: "d"
url: "/docs/linux/man/1-darktable/"
description: "darktable – a digital photography workflow application"
---

<h2 class="name">NAME</h2>
<p> darktable &#8211; a digital photography workflow application </p>
<h2>SYNOPSIS</h2>
<pre><code>
darktable[options][IMG_1234.{RAW, ...} | image_folder / ]
</code></pre>
<p> Options: </p>
<pre><code>
- d
{
    all, cache, camctl, camsupport, control, dev, fswatch,
        input, lighttable, masks, memory, nan, opencl,
        perf, pwstorage, print, sql
}
--disable - opencl-- library&lt;library file&gt; --datadir&lt;data directory&gt; --moduledir&lt;module directory&gt; --tmpdir&lt;tmp directory&gt; --configdir&lt;user config directory&gt; --cachedir&lt;user cache directory&gt; --localedir&lt;locale directory&gt; --luacmd&lt;lua command&gt; --conf &lt; key &gt;= &lt;value&gt; --noiseprofiles&lt;noiseprofiles json file&gt; --help-- version
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>darktable</code> is a digital photography workflow application for <code>Linux</code>, <code>Mac </code><font SIZE="-1"><code>OS X</code></font> and several other <code>Unices</code>. </p>
<p> The application is designed to ease editing and consistent processing of large photo sessions and provides an easy to use digital light-table and a set of sophisticated post-processing tools. </p>
<p> Most processing is done in 32-bit floating point per channel mode in device independent <font SIZE="-1"><code>CIE</code></font><code> L*a*b*</code> color space. <code>darktable</code> is also fully color managed, which gives you full control over the look of the photos. </p>
<p> The application relies on a modern plug-in architecture thus making it easy for 3rd party developers to extend the existing capabilities of the application. All lighttable and darkroom features are implemented as plug-ins, so you can create your plug-ins reusing existing code. Most workflow specific things can also be scripted in <code>Lua</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><font SIZE="-1"><code>IMG_1234.RAW</code></font><code> or image_folder/</code></p>
<dd> You may optionally supply the filename of an image or the name of a folder containing image files. If a filename is given darktable starts in darkroom view with that file opened. If a folder is given darktable starts in lighttable view with the content of that folder as the current collection. If there is already an instance of darktable running (using the same library) the image or folder will be opened there, using <code>D-Bus</code> to communicate between the two processes.</p>
<dt><code>-d &lt;debug option&gt;</code></p>
<dd> This option enables debug output to the terminal. There are several subsystems of darktable and debugging of each of them can be activated separately. You can use this option multiple times if you want debugging output of more than one subsystem. </p>
<p> A few of those debug options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>control</code></p>
<dd> Enable job queue debugging. If you redirect darktable&#8217;s output to <code>control.log</code> and call <code>./tools/create_control_svg.sh control.log</code>, you will get a nice <code>control.svg</code> with a visualization of the threads&#8217; work.</p>
<dt><code>cache</code></p>
<dd> This will give you a lot of debugging info about the thumbnail cache for lighttable mode. If compiled in debug mode, this will also tell you where in the code a certain buffer has last been locked.</p>
<dt><code>perf</code></p>
<dd> Use this for performance tweaking your darkroom modules. It will rdtsc-measure the runtimes of all plugins and print them to stdout.</p>
<dt><code>all</code></p>
<dd> Enable all debugging output.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;disable-opencl</code></p>
<dd> Prevent darktable from initializing the OpenCL subsystem. Use this option in case darktable crashes at startup due to a defective OpenCL implementation.</p>
<dt><code>&#8211;library &lt;library file&gt;</code></p>
<dd> darktable keeps image information in an sqlite database for fast access. The default location of that database file is <tt>&quot;$HOME/.config/darktable/library.db&quot;</tt>. You may give an alternative location, e.g. if you want to do some experiments without compromising your original library.db. If the database file does not exist, darktable creates it for you. You may also give <tt>&quot;:memory:&quot;</tt> as a library file in which case the database is kept in system memory &#8211; all changes are discarded when darktable terminates.</p>
<dt><code>&#8211;datadir &lt;data directory&gt;</code></p>
<dd> This option defines the directory where darktable finds its runtime data. The default place depends on your installation. Typical places are <tt>&quot;/opt/darktable/share/darktable/&quot;</tt> and <tt>&quot;/usr/share/darktable/&quot;</tt>.</p>
<dt><code>&#8211;moduledir &lt;module directory&gt;</code></p>
<dd> darktable has a modular structure and organizes its modules as shared libraries for loading at runtime. With this option you tell darktable where to look for its shared libraries. The default place depends on your installation; typical places are <tt>&quot;/opt/darktable/lib/darktable/&quot;</tt> and <tt>&quot;/usr/lib/darktable/&quot;</tt>.</p>
<dt><code>&#8211;tmpdir &lt;tmp directory&gt;</code></p>
<dd> The place where darktable stores its temporary files. If this option is not supplied darktable uses the system default.</p>
<dt><code>&#8211;configdir &lt;config directory&gt;</code></p>
<dd> This option defines the directory where darktable stores the user specific configuration. The default place is <tt>&quot;$HOME/.config/darktable/&quot;</tt>.</p>
<dt><code>&#8211;cachedir &lt;cache directory&gt;</code></p>
<dd> darktable keeps a cache of image thumbnails for fast image preview and of precompiled OpenCL binaries for fast startup. By default the cache is located in <tt>&quot;$HOME/.cache/darktable/&quot;</tt>. There may exist multiple thumbnail caches in parallel &#8211; one for each library file.</p>
<dt><code>&#8211;localedir &lt;locale directory&gt;</code></p>
<dd> The place where darktable finds its language specific text strings. The default place depends on your installation. Typical places are <tt>&quot;/opt/darktable/share/locale/&quot;</tt> and <tt>&quot;/usr/share/locale/&quot;</tt>.</p>
<dt><code>&#8211;luacmd &lt;lua command&gt;</code></p>
<dd> A string containing lua commands to execute after lua initialization. These commands will be run after your <tt>&quot;luarc&quot;</tt> file. </p>
<p> If lua is not compiled in, this option will be accepted but won&#8217;t do anything.</p>
<dt><code>&#8211;conf &lt;key&gt;=&lt;value&gt;</code></p>
<dd> darktable supports a rich set of configuration parameters which the user defines in <tt>&quot;darktablerc&quot;</tt> &#8211; darktable&#8217;s configuration file in the user config directory. You may temporarily overwrite individual settings on the command line with this option &#8211; however, these settings will not be stored in <tt>&quot;darktablerc&quot;</tt>.</p>
<dt><code>&#8211;noiseprofiles &lt;noiseprofiles json file&gt;</code></p>
<dd> darktable&#8217;s profiled denoise module uses camera specific profile data that gets loaded from an external <font SIZE="-1">JSON</font> file. With this option the file to be loaded can be changed to allow testing alternative profiles. The default profile file is <tt>&quot;noiseprofiles.json&quot;</tt> and is typically found in <tt>&quot;/opt/darktable/share/darktable/&quot;</tt> or <tt>&quot;/usr/share/darktable/&quot;</tt>.</dl>
<h2>DEFAULT KEYBINDINGS</h2>
<p> <i>All modes</i></p>
<dl>
<dt><code>l</code></p>
<dd> Switch to lighttable view</p>
<dt><code>d</code></p>
<dd> Switch to darkroom view</p>
<dt><code>t</code></p>
<dd> Switch to tethered capture view</p>
<dt><code>m</code></p>
<dd> Switch to map view</p>
<dt><code>s</code></p>
<dd> Switch to slideshow view</p>
<dt><code>p</code></p>
<dd> Switch to print view</p>
<dt><code>.</code></p>
<dd> Switch between lighttable and darkroom views</p>
<dt><code>Ctrl-q</code></p>
<dd> Quit</p>
<dt><code>F11</code></p>
<dd> Switch between fullscreen and normal modes of the application&#8217;s window</p>
<dt><code>Esc</code></p>
<dd> Leave fullscreen mode</p>
<dt><code>Ctrl-h</code></p>
<dd> Show/hide header</p>
<dt><code>Tab</code></p>
<dd> Show/hide sidebars</dl>
<p> <i>Lighttable mode</i></p>
<dl>
<dt><code>g, Shift-g</code></p>
<dd> Navigate to top, bottom row</p>
<dt><code>PageUp, PageDown</code></p>
<dd> Navigate one page up, down</p>
<dt><code>&#8216;</code></p>
<dd> Scroll center</p>
<dt><code>Down, Left, Right, Up</code></p>
<dd> Scroll down, left, right, up</p>
<dt><code>z</code></p>
<dd> Preview image</p>
<dt><code>Ctrl-z</code></p>
<dd> Preview image with focus detection</p>
<dt><code>F1, F2, F3, F4, F5</code></p>
<dd> Color labels: toggle red, yellow, green, blue and purple</p>
<dt><code>1, 2, 3, 4, 5</code></p>
<dd> Star rating</p>
<dt><code>0</code></p>
<dd> Strip all stars</p>
<dt><code>r</code></p>
<dd> Mark as rejected</p>
<dt><code>l</code></p>
<dd> Realign images to the grid</p>
<dt><code>Alt-1</code></p>
<dd> Zoom in on first visible image</p>
<dt><code>Alt-2, 3</code></p>
<dd> Adjust zoom</p>
<dt><code>Alt-4</code></p>
<dd> Zoom out completely</p>
<dt><code>Ctrl-a</code></p>
<dd> Select all images</p>
<dt><code>Ctrl-Shift-a</code></p>
<dd> Select no images</p>
<dt><code>Ctrl-i</code></p>
<dd> Invert selection</p>
<dt><code>Ctrl-d</code></p>
<dd> Duplicate image</p>
<dt><code>Ctrl-g, Ctrl-Shift-g</code></p>
<dd> Group/ungroup selected images</p>
<dt><code>Delete</code></p>
<dd> Remove image from collection</p>
<dt><code>Ctrl-c, Ctrl-Shift-c</code></p>
<dd> Copy all, selected history</p>
<dt><code>Ctrl-v, Ctrl-Shift-v</code></p>
<dd> Paste all, selected history</p>
<dt><code>Space</code></p>
<dd> Toggle selection of an image</p>
<dt><code>Return</code></p>
<dd> Select an image</p>
<dt><code>Ctrl-e</code></p>
<dd> Export currently selected images</p>
<dt><code>Ctrl-k</code></p>
<dd> Jump back to the previous collection</p>
<dt><code>Ctrl-t</code></p>
<dd> Open a popup to quickly tag an image</p>
<dt><code>Ctrl-Shift-i</code></p>
<dd> Import a folder</p>
<dt><code>Ctrl-j</code></p>
<dd> Jump to the filmroll of an image</dl>
<p> <i>Darkroom mode</i></p>
<dl>
<dt><code>Alt-1, 2, 3</code></p>
<dd> Zoom to 1:1, fill, and fit, respectively</p>
<dt><code>Ctrl-f</code></p>
<dd> Show/hide filmstrip</p>
<dt><code>Space, Backspace</code></p>
<dd> Step to next, previous image</p>
<dt><code>Ctrl-e</code></p>
<dd> Export current image</p>
<dt><code>Ctrl-c, Ctrl-Shift-c</code></p>
<dd> Copy all, selected history</p>
<dt><code>Ctrl-v, Ctrl-Shift-v</code></p>
<dd> Paste all, selected history</p>
<dt><code>o</code></p>
<dd> Toggle show of over- and under-exposure</p>
<dt><code>Ctrl-g</code></p>
<dd> Toggle gamut check</p>
<dt><code>Ctrl-s</code></p>
<dd> Toggle softproofing</p>
<dt><code>Enter</code></p>
<dd> In Crop &amp; Rotate module, commit the crop</p>
<dt><code>[, ]</code></p>
<dd> In Flip module, rotate 90 degrees ccw, cw</p>
<dt><code>&lt;, &gt;</code></p>
<dd> When drawing masks, decrease, increase brush opacity, respectively</p>
<dt><code>{, }</code></p>
<dd> When drawing masks, decrease, increase brush hardness, respectively</p>
<dt><code>[, ]</code></p>
<dd> When drawing masks, decrease, increase brush size, respectively</dl>
<p> <i>Tethered mode</i></p>
<dl>
<dt><code>Ctrl-f</code></p>
<dd> Show/hide filmstrip</p>
<dt><code>v</code></p>
<dd> Toggle live view</dl>
<p> <i>Map mode</i></p>
<dl>
<dt><code>Ctrl-f</code></p>
<dd> Show/hide filmstrip</p>
<dt><code>Ctrl-z</code></p>
<dd> Undo</p>
<dt><code>Ctrl-r</code></p>
<dd> Redo</dl>
<p> <i>Filmstrip (when the cursor is on top of the filmstrip)</i></p>
<dl>
<dt><code>F1, F2, F3, F4, F5</code></p>
<dd> Color labels: toggle red, yellow, green, blue and purple</p>
<dt><code>1, 2, 3, 4, 5</code></p>
<dd> Star rating</p>
<dt><code>0</code></p>
<dd> Strip all stars</p>
<dt><code>r</code></p>
<dd> Mark as rejected</p>
<dt><code>Ctrl-d</code></p>
<dd> Duplicate image</p>
<dt><code>Ctrl-a</code></p>
<dd> Select all images</p>
<dt><code>Ctrl-Shift-a</code></p>
<dd> Select no images</p>
<dt><code>Ctrl-i</code></p>
<dd> Invert selection</p>
<dt><code>Ctrl-c, Ctrl-Shift-c</code></p>
<dd> Copy all, selected history</p>
<dt><code>Ctrl-v, Ctrl-Shift-v</code></p>
<dd> Paste all, selected history</dl>
<p> <i>Slideshow mode</i></p>
<dl>
<dt><code>Space</code></p>
<dd> Start/stop playback</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-darktable-cli/">darktable-cli</a></i>(1)</p>
<h2>OTHER INFO</h2>
<p> Please visit <code>darktable</code>&#8216;s website for news, blog and bug tracker: &lt;<a rel="nofollow" href="http://www.darktable.org/">http://www.darktable.org/</a>&gt; </p>
<p> &lt;<a rel="nofollow" href="http://www.darktable.org/usermanual/">http://www.darktable.org/usermanual/</a>&gt; The complete darktable usermanual. </p>
<p> <code>darktablerc.html</code> An overview over all default config settings. The default place depends on your installation. Typical places are <tt>&quot;/opt/darktable/share/doc/darktable/&quot;</tt> and <tt>&quot;/usr/share/doc/darktable/&quot;</tt>.</p>
<h2>RELATED</h2>
<dl>
<dt><code>darktable-viewer</code> screensaver version of darktable. Shows the last active collection in full screen as a slideshow. Using the slideshow mode of darktable is encouraged.</p>
<dd></dl>
<h2>REPORTING BUGS</h2>
<p> Please use the bug tracker on &lt;<a rel="nofollow" href="http://www.darktable.org/redmine/projects/darktable/issues/">http://www.darktable.org/redmine/projects/darktable/issues/</a>&gt; to report bugs, feature requests and so on.</p>
<h2>AUTHORS</h2>
<p> The principal developer of darktable is Johannes Hanika. The (hopefully) complete list of contributors to the project is: </p>
<p> * developers: Henrik Andersson, Johannes Hanika, Tobias Ellinghaus, Ulrich Pegelow. </p>
<p> * ubuntu packaging, color management, video tutorials: Pascal de Bruijn. </p>
<p> * opencl pipeline, usermanual: Ulrich Pegelow. </p>
<p> * networking, battle testing, translation expert: Alexandre Prokoudine. </p>
<p> * translation: a3novy, Alexandre Prokoudine, Anocha Yimsiriwattana, Artur de Sousa Rocha, Daniele Giorgis, Dimitrios Psychogios, Ger Siemerink, Guilherme Brondani Torri, Henrik Andersson, José Carlos Casimiro, Josep Puigdemont, María Leandro, Mauro Bartoccelli, Michał Prędotka, Mikko Ruohola, Milan Knížek, Olivier Tribout, Pascal Obry, Richard Levitte, Roberto Quintero, Sebastien Delcoigne, Thomas Costis, Thomas Pryds, Tobias Ellinghaus, Victor Lamoine. </p>
<p> * contributors: Aldric Renaudin, Alexandre Prokoudine, Alexey Dokuchaev, Ammon Riley, Anton Keks, Antony Dovgal, Ari Makela, Benjamin Cahill, Brian Teague, Bruce Guenter, Cherrot Luo, Chris Mason, Christian Tellefsen, David Morel, Denis Cheremisov, Dennis Gnad, Diego Segura, Dimitrios Psychogios, Eckhart Pedersen, Edouard Gomez, Edward Herr, František Šidák, Gaspard Jankowiak, Ger Siemerink, Gianluigi Calcaterra, Guilherme Brondani Torri, Ivan Tarozzi, James C. McPherson, Jan Kundrát, Jean-Sébastien Pédron, Jérémy Rosen, Jesper Pedersen, Joao Trindade, Jon Leighton, Jose Carlos Garcia Sogo, Josef Wells, Julian J. M, Mattias Eriksson, Michal Babej, Michał Prędotka, Moritz Lipp, Olivier Tribout, Pascal de Bruijn, Pascal Obry, parafin, Petr Styblo, Pierre Le Magourou, Richard Levitte, Richard Tollerton, Robert Bieber, Roland Riegel, Roman Lebedev, Rostyslav Pidgornyi, Sergey Pavlov, Simon Harhues, Simon Spannagel, Stuart Henderson, Terry Jeffress, Tim Harder, Togan Muftuoglu, Tom Vanderpoel, Ulrich Pegelow, Wolfgang Goetz, Wolfgang Kuehnel, Yari Adan, hal, jan, maigl, tuxuser. And all those of you that made previous releases possible. </p>
<p> This man page was written by Alexandre Prokoudine &lt;alexandre.prokoudine [at] gmail.com&gt; and Richard Levitte &lt;richard [at] levittr.org&gt;. Additions were made by Tobias Ellinghaus &lt;me [at] houz.org&gt;.</p>
<h2>HISTORY</h2>
<p> The project was started by Johannes Hanika in early 2009 to fill the gap (or, rather, a black hole) of a digital photography workflow tool on Linux.</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> <code>Copyright (C)</code> 2009-2015 by Authors. </p>
<p> <code>darktable</code> is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GPL</font> v3 or (at your option) any later version. </p>
<h2>Index</h2>
