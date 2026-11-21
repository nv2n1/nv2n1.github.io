---

title: "xstdcmap(1)"
name: "xstdcmap"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xstdcmap/"
description: "xstdcmap – X standard colormap utility"
---

<p> xstdcmap &#8211; X standard colormap utility </p>
<h2>SYNOPSIS</h2>
<p> <code>xstdcmap</code> [-all] [-best] [-blue] [-default] [-delete <i>map</i>] [-display <i>dpy</i>] [-gray] [-green] [-help] [-red] [-verbose] [-version]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xstdcmap</i> utility can be used to selectively define standard colormap properties. It is intended to be run from a user&#8217;s X startup script to create standard colormap definitions in order to facilitate sharing of scarce colormap resources among clients. Where at all possible, colormaps are created with read-only allocations.</p>
<h2>OPTIONS</h2>
<p> The following options may be used with <i>xstdcmap</i>:</p>
<dl>
<dt><code>-all</code></dt>
<dd> This option indicates that all six standard colormap properties should be defined on each screen of the display. Not all screens will support visuals under which all six standard colormap properties are meaningful. <i>xstdcmap</i> will determine the best allocations and visuals for the colormap properties of a screen. Any previously existing standard colormap properties will be replaced.</dd>
<dt><code>-best</code></dt>
<dd> This option indicates that the RGB_BEST_MAP should be defined.</dd>
<dt><code>-blue</code></dt>
<dd> This option indicates that the RGB_BLUE_MAP should be defined.</dd>
<dt><code>-default</code></dt>
<dd> This option indicates that the RGB_DEFAULT_MAP should be defined.</dd>
<dt><code>-delete </code><i>map</i></dt>
<dd> This option specifies that a specific standard colormap property, or all such properties, should be removed. <i>map</i> may be one of: default, best, red, green, blue, gray, or all.</dd>
<dt><code>-display </code><i>dpy</i></dt>
<dd> This option specifies the host and display to use; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</dd>
<dt><code>-gray</code></dt>
<dd> This option indicates that the RGB_GRAY_MAP should be defined.</dd>
<dt><code>-green</code></dt>
<dd> This option indicates that the RGB_GREEN_MAP should be defined.</dd>
<dt><code>-help</code></dt>
<dd> This option indicates that a brief description of the command line arguments should be printed on the standard error. This will be done whenever an unhandled argument is given to <i>xstdcmap.</i></dd>
<dt><code>-red</code></dt>
<dd> This option indicates that the RGB_RED_MAP should be defined.</dd>
<dt><code>-verbose</code></dt>
<dd> This option indicates that <i>xstdcmap</i> should print logging information as it parses its input and defines the standard colormap properties.</dd>
<dt><code>-version</code></dt>
<dd> This option indicates that <i>xstdcmap</i> should print its version and exit.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></dt>
<dd> to get default host and display number.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7)</p>
<h2>AUTHOR</h2>
<p> Donna Converse, MIT X Consortium </p>
