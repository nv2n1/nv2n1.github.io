---
title: "zathura(1)"
name: "zathura"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zathura/"
description: "zathura – a document viewer"
---

<h2>NAME</h2>
<p> zathura &#8211; a document viewer</p>
<h2>SYNOPOSIS</h2>
<pre><code>
zathura[OPTION]... zathura[OPTION]... FILE[FILE...] zathura-- syntex - forward INPUT FILE
</code></pre>
<h2>DESCRIPTION</h2>
<p> zathura is a highly customizable and functional document viewer. It provides a minimalistic and space saving interface as well as an easy usage that mainly focuses on keyboard interaction.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e [xid], &#8211;reparent [xid]</code></p>
<dd> Reparents to window specified by xid</p>
<dt><code>-c [path], &#8211;config-dir [path]</code></p>
<dd> Path to the config directory</p>
<dt><code>-d [path], &#8211;data-dir [path]</code></p>
<dd> Path to the data directory</p>
<dt><code>-p [path], &#8211;plugins-dir [path]</code></p>
<dd> Path to the directory containing plugins</p>
<dt><code>-w [password], &#8211;password [password]</code></p>
<dd> The documents password. If multiple documents are opened at once, the password will be used for the first one and zathura will ask for the passwords of the remaining files if needed.</p>
<dt><code>-P [number], &#8211;page [number]</code></p>
<dd> Open the document at the given page number. Pages are numbered starting with 1, and negative numbers indicate page numbers starting from the end of the document, -1 being the last page.</p>
<dt><code>&#8211;fork</code></p>
<dd> Fork into the background</p>
<dt><code>-l [level], &#8211;debug [level]</code></p>
<dd> Set log debug level (debug, info, warning, error)</p>
<dt><code>-s</code>,<code> &#8211;synctex</code></p>
<dd> Enable synctex support for backwards synchronization.</p>
<dt><code>-x [cmd], &#8211;synctex-editor-command [cmd]</code></p>
<dd> Set the synctex editor command for backwards synchronization.</p>
<dt><code>&#8211;synctex-forward [input]</code></p>
<dd> Jump to the given position. The switch expcects the same format as specified for syntex&#8217;s view -i.</p>
<dt><code>&#8211;synctex-pid [pid]</code></p>
<dd> If not -1, forward synctex input to process with the given pid. Otherwise, try all zathura process to find the correct one.</p>
<dt><code>&#8211;mode [mode]</code></p>
<dd> Switch to mode (presentation, fullscreen) after opening a document.</dl>
<h2>MOUSE AND KEY BINDINGS</h2>
<dl>
<dt><code>J, PgDn</code></p>
<dd> Go to the next page</p>
<dt><code>K, PgUp</code></p>
<dd> Go to the previous page</p>
<dt><code>h, k, j, l</code></p>
<dd> Scroll to the left, down, up or right direction</p>
<dt><code>Left, Down, Up, Right</code></p>
<dd> Scroll to the left, down, up or right direction</p>
<dt><code>^t, ^d, ^u, ^y</code></p>
<dd> Scroll a half page left, down, up or right</p>
<dt><code>t, ^f, ^b, space, &lt;S-space&gt;, y</code></p>
<dd> Scroll a full page left, down, up or right</p>
<dt><code>gg, G, nG</code></p>
<dd> Goto to the first, the last or to the nth page</p>
<dt><code>H, L</code></p>
<dd> Goto top or bottom of the current page</p>
<dt><code>^o, ^i</code></p>
<dd> Move backward and forward through the jump list</p>
<dt><code>^j, ^k</code></p>
<dd> Bisect forward and backward between the last two jump points</p>
<dt><code>^c, Escape</code></p>
<dd> Abort</p>
<dt><code>a, s</code></p>
<dd> Adjust window in best-fit or width mode</p>
<dt><code>/, ?</code></p>
<dd> Search for text</p>
<dt><code>n, N</code></p>
<dd> Search for the next or previous result</p>
<dt><code>o, O</code></p>
<dd> Open document</p>
<dt><code>f</code></p>
<dd> Follow links</p>
<dt><code>F</code></p>
<dd> Display link target</p>
<dt><code>:</code></p>
<dd> Enter command</p>
<dt><code>r</code></p>
<dd> Rotate by 90 degrees</p>
<dt><code>^r</code></p>
<dd> Recolor</p>
<dt><code>R</code></p>
<dd> Reload document</p>
<dt><code>Tab</code></p>
<dd> Show index and switch to <code>Index mode</code></p>
<dt><code>d</code></p>
<dd> Toggle dual page view</p>
<dt><code>F5</code></p>
<dd> Switch to fullscreen mode</p>
<dt><code>^m</code></p>
<dd> Toggle inputbar</p>
<dt><code>^n</code></p>
<dd> Toggle statusbar</p>
<dt><code>+, -, =</code></p>
<dd> Zoom in, out or to the original size</p>
<dt><code>zI, zO, z0</code></p>
<dd> Zoom in, out or to the original size</p>
<dt><code>n=</code></p>
<dd> Zoom to size n</p>
<dt><code>mX</code></p>
<dd> Set a quickmark to a letter or number X</p>
<dt><code>&#8216;X</code></p>
<dd> Goto quickmark saved at letter or number X</p>
<dt><code>q</code></p>
<dd> Quit</dl>
<h3>Fullscreen mode</h3>
<dl>
<dt><code>J, K</code></p>
<dd> Go to the next or previous page</p>
<dt><code>space, &lt;S-space&gt;, &lt;BackSpace&gt;</code></p>
<dd> Scroll a full page down or up</p>
<dt><code>gg, G, nG</code></p>
<dd> Goto to the first, the last or to the nth page</p>
<dt><code>^c, Escape</code></p>
<dd> Abort</p>
<dt><code>F5</code></p>
<dd> Switch to normal mode</p>
<dt><code>+, -, =</code></p>
<dd> Zoom in, out or to the original size</p>
<dt><code>zI, zO, z0</code></p>
<dd> Zoom in, out or to the original size</p>
<dt><code>n=</code></p>
<dd> Zoom to size n</p>
<dt><code>q</code></p>
<dd> Quit</dl>
<h3>Index mode</h3>
<dl>
<dt><code>k, j</code></p>
<dd> Move to upper or lower entry</p>
<dt><code>l</code></p>
<dd> Expand entry</p>
<dt><code>L</code></p>
<dd> Expand all entries</p>
<dt><code>h</code></p>
<dd> Collapse entry</p>
<dt><code>H</code></p>
<dd> Collapse all entries</p>
<dt><code>space, Return</code></p>
<dd> Select and open entry</dl>
<h3>Mouse bindings</h3>
<dl>
<dt><code>Scroll</code></p>
<dd> Scroll up or down</p>
<dt><code>^Scroll</code></p>
<dd> Zoom in or out</p>
<dt><code>Hold Button2</code></p>
<dd> Pan the document</p>
<dt><code>Button1</code></p>
<dd> Follow link</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>bmark</code></p>
<dd> Save a bookmark</p>
<dt><code>bdelete</code></p>
<dd> Delete a bookmark</p>
<dt><code>blist</code></p>
<dd> List bookmarks</p>
<dt><code>close</code></p>
<dd> Close document</p>
<dt><code>exec</code></p>
<dd> Execute an external command</p>
<dt><code>info</code></p>
<dd> Show document information</p>
<dt><code>help</code></p>
<dd> Show help page</p>
<dt><code>open, o</code></p>
<dd> Open a document</p>
<dt><code>offset</code></p>
<dd> Set page offset</p>
<dt><code>print</code></p>
<dd> Print document</p>
<dt><code>write, write!</code></p>
<dd> Save document (and force overwriting)</p>
<dt><code>export</code></p>
<dd> Export attachments</dl>
<h2>CONFIGURATION</h2>
<p> The default appearance and behaviour of zathura can be overwritten by modifying the <i>zathurarc</i> file (default path: ~/.config/zathura/zathurarc). For a detailed description please consult <a href="/docs/linux/man/5-zathurarc/">zathurarc</a>(5).</p>
<h2>SYNCTEX SUPPORT</h2>
<p> Both synctex forward and backwards synchronization are supported by zathura, To enable synctex forward synchronization, please look at the <i>&#8211;syntex</i> and <i>&#8211;synctex-editor</i> options. To support synctex backwards synchronization, zathura provides a D-Bus interface that can be called by the editor. For convince zathura also knows how to parse the output of the <i>synctex view</i> command. It is enough to pass the arguments to <i>synctex view</i>&#8216;s <i>-i</i> option to zathura via <i>&#8211;syntex-forward</i> and zathura will pass the information to the correct instance.</p>
<h2>KNOWN BUGS</h2>
<p> If GDK_NATIVE_WINDOWS is enabled you will experience problems with large documents. In this case zathura might crash or pages cannot be rendered properly. Disabling GDK_NATIVE_WINDOWS fixes this issue.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-zathurarc/">zathurarc</a>(5)</p>
<h2>AUTHOR</h2>
<p> pwmt.org </p>
<h2>Index</h2>
