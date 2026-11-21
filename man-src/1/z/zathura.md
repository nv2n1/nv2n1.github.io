---

title: "zathura(1)"
name: "zathura"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zathura/"
description: "zathura – a document viewer"
---

<p> zathura &#8211; a document viewer</p>
<h2>SYNOPOSIS</h2>
<pre><code>
zathura[OPTION]... zathura[OPTION]... FILE[FILE...] zathura-- syntex - forward INPUT FILE
</code></pre>
<h2>DESCRIPTION</h2>
<p> zathura is a highly customizable and functional document viewer. It provides a minimalistic and space saving interface as well as an easy usage that mainly focuses on keyboard interaction.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e [xid], &#8211;reparent [xid]</code></dt>
<dd> Reparents to window specified by xid</dd>
<dt><code>-c [path], &#8211;config-dir [path]</code></dt>
<dd> Path to the config directory</dd>
<dt><code>-d [path], &#8211;data-dir [path]</code></dt>
<dd> Path to the data directory</dd>
<dt><code>-p [path], &#8211;plugins-dir [path]</code></dt>
<dd> Path to the directory containing plugins</dd>
<dt><code>-w [password], &#8211;password [password]</code></dt>
<dd> The documents password. If multiple documents are opened at once, the password will be used for the first one and zathura will ask for the passwords of the remaining files if needed.</dd>
<dt><code>-P [number], &#8211;page [number]</code></dt>
<dd> Open the document at the given page number. Pages are numbered starting with 1, and negative numbers indicate page numbers starting from the end of the document, -1 being the last page.</dd>
<dt><code>&#8211;fork</code></dt>
<dd> Fork into the background</dd>
<dt><code>-l [level], &#8211;debug [level]</code></dt>
<dd> Set log debug level (debug, info, warning, error)</dd>
<dt><code>-s</code>,<code> &#8211;synctex</code></dt>
<dd> Enable synctex support for backwards synchronization.</dd>
<dt><code>-x [cmd], &#8211;synctex-editor-command [cmd]</code></dt>
<dd> Set the synctex editor command for backwards synchronization.</dd>
<dt><code>&#8211;synctex-forward [input]</code></dt>
<dd> Jump to the given position. The switch expcects the same format as specified for syntex&#8217;s view -i.</dd>
<dt><code>&#8211;synctex-pid [pid]</code></dt>
<dd> If not -1, forward synctex input to process with the given pid. Otherwise, try all zathura process to find the correct one.</dd>
<dt><code>&#8211;mode [mode]</code></dt>
<dd> Switch to mode (presentation, fullscreen) after opening a document.</dd></dl>
<h2>MOUSE AND KEY BINDINGS</h2>
<dl>
<dt><code>J, PgDn</code></dt>
<dd> Go to the next page</dd>
<dt><code>K, PgUp</code></dt>
<dd> Go to the previous page</dd>
<dt><code>h, k, j, l</code></dt>
<dd> Scroll to the left, down, up or right direction</dd>
<dt><code>Left, Down, Up, Right</code></dt>
<dd> Scroll to the left, down, up or right direction</dd>
<dt><code>^t, ^d, ^u, ^y</code></dt>
<dd> Scroll a half page left, down, up or right</dd>
<dt><code>t, ^f, ^b, space, &lt;S-space&gt;, y</code></dt>
<dd> Scroll a full page left, down, up or right</dd>
<dt><code>gg, G, nG</code></dt>
<dd> Goto to the first, the last or to the nth page</dd>
<dt><code>H, L</code></dt>
<dd> Goto top or bottom of the current page</dd>
<dt><code>^o, ^i</code></dt>
<dd> Move backward and forward through the jump list</dd>
<dt><code>^j, ^k</code></dt>
<dd> Bisect forward and backward between the last two jump points</dd>
<dt><code>^c, Escape</code></dt>
<dd> Abort</dd>
<dt><code>a, s</code></dt>
<dd> Adjust window in best-fit or width mode</dd>
<dt><code>/, ?</code></dt>
<dd> Search for text</dd>
<dt><code>n, N</code></dt>
<dd> Search for the next or previous result</dd>
<dt><code>o, O</code></dt>
<dd> Open document</dd>
<dt><code>f</code></dt>
<dd> Follow links</dd>
<dt><code>F</code></dt>
<dd> Display link target</dd>
<dt><code>:</code></dt>
<dd> Enter command</dd>
<dt><code>r</code></dt>
<dd> Rotate by 90 degrees</dd>
<dt><code>^r</code></dt>
<dd> Recolor</dd>
<dt><code>R</code></dt>
<dd> Reload document</dd>
<dt><code>Tab</code></dt>
<dd> Show index and switch to <code>Index mode</code></dd>
<dt><code>d</code></dt>
<dd> Toggle dual page view</dd>
<dt><code>F5</code></dt>
<dd> Switch to fullscreen mode</dd>
<dt><code>^m</code></dt>
<dd> Toggle inputbar</dd>
<dt><code>^n</code></dt>
<dd> Toggle statusbar</dd>
<dt><code>+, -, =</code></dt>
<dd> Zoom in, out or to the original size</dd>
<dt><code>zI, zO, z0</code></dt>
<dd> Zoom in, out or to the original size</dd>
<dt><code>n=</code></dt>
<dd> Zoom to size n</dd>
<dt><code>mX</code></dt>
<dd> Set a quickmark to a letter or number X</dd>
<dt><code>&#8216;X</code></dt>
<dd> Goto quickmark saved at letter or number X</dd>
<dt><code>q</code></dt>
<dd> Quit</dd></dl>
<h3>Fullscreen mode</h3>
<dl>
<dt><code>J, K</code></dt>
<dd> Go to the next or previous page</dd>
<dt><code>space, &lt;S-space&gt;, &lt;BackSpace&gt;</code></dt>
<dd> Scroll a full page down or up</dd>
<dt><code>gg, G, nG</code></dt>
<dd> Goto to the first, the last or to the nth page</dd>
<dt><code>^c, Escape</code></dt>
<dd> Abort</dd>
<dt><code>F5</code></dt>
<dd> Switch to normal mode</dd>
<dt><code>+, -, =</code></dt>
<dd> Zoom in, out or to the original size</dd>
<dt><code>zI, zO, z0</code></dt>
<dd> Zoom in, out or to the original size</dd>
<dt><code>n=</code></dt>
<dd> Zoom to size n</dd>
<dt><code>q</code></dt>
<dd> Quit</dd></dl>
<h3>Index mode</h3>
<dl>
<dt><code>k, j</code></dt>
<dd> Move to upper or lower entry</dd>
<dt><code>l</code></dt>
<dd> Expand entry</dd>
<dt><code>L</code></dt>
<dd> Expand all entries</dd>
<dt><code>h</code></dt>
<dd> Collapse entry</dd>
<dt><code>H</code></dt>
<dd> Collapse all entries</dd>
<dt><code>space, Return</code></dt>
<dd> Select and open entry</dd></dl>
<h3>Mouse bindings</h3>
<dl>
<dt><code>Scroll</code></dt>
<dd> Scroll up or down</dd>
<dt><code>^Scroll</code></dt>
<dd> Zoom in or out</dd>
<dt><code>Hold Button2</code></dt>
<dd> Pan the document</dd>
<dt><code>Button1</code></dt>
<dd> Follow link</dd></dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>bmark</code></dt>
<dd> Save a bookmark</dd>
<dt><code>bdelete</code></dt>
<dd> Delete a bookmark</dd>
<dt><code>blist</code></dt>
<dd> List bookmarks</dd>
<dt><code>close</code></dt>
<dd> Close document</dd>
<dt><code>exec</code></dt>
<dd> Execute an external command</dd>
<dt><code>info</code></dt>
<dd> Show document information</dd>
<dt><code>help</code></dt>
<dd> Show help page</dd>
<dt><code>open, o</code></dt>
<dd> Open a document</dd>
<dt><code>offset</code></dt>
<dd> Set page offset</dd>
<dt><code>print</code></dt>
<dd> Print document</dd>
<dt><code>write, write!</code></dt>
<dd> Save document (and force overwriting)</dd>
<dt><code>export</code></dt>
<dd> Export attachments</dd></dl>
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
