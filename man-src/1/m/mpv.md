---
title: "mpv(1)"
name: "mpv"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpv/"
description: "mpv – a media player"
---

<p>mpv &#8211; a media player </p>
<h2>Synopsis</h2>
<pre><code>mpv</code> [options] [file|URL|PLAYLIST|-]
<code>mpv</code> [options] files</pre>
<h2>Description</h2>
<p><code>mpv</code> is a media player based on MPlayer and mplayer2. It supports a wide variety of video file formats, audio and video codecs, and subtitle types. Special input URL types are available to read input from a variety of sources other than disk files. Depending on platform, a variety of different video and audio output methods are supported. </p>
<p> Usage examples to get you started quickly can be found at the end of this man page.</p>
<h2>Interactive Control</h2>
<p>mpv has a fully configurable, command-driven control layer which allows you to control mpv using keyboard, mouse, or remote control (there is no LIRC support &#8211; configure remotes as input devices instead). </p>
<p> See the <code>&#8211;input-</code> options for ways to customize it. </p>
<p> The following listings are not necessarily complete. See <code>etc/input.conf</code> for a list of default bindings. User <code>input.conf</code> files and Lua scripts can define additional key bindings. </p>
<p> See also <code>&#8211;input-test</code> for interactive binding details by key, and the <i>stats</i> built-in script for key bindings list (including print to terminal).</p>
<h3>Keyboard Control</h3>
<dl COMPACT>
<dt><code>LEFT and RIGHT</code></p>
<dd>Seek backward/forward 5 seconds. Shift+arrow does a 1 second exact seek (see <code>&#8211;hr-seek</code>).</p>
<dt><code>UP and DOWN</code></p>
<dd>Seek forward/backward 1 minute. Shift+arrow does a 5 second exact seek (see <code>&#8211;hr-seek</code>).</p>
<dt><code>Ctrl+LEFT and Ctrl+RIGHT</code></p>
<dd>Seek to the previous/next subtitle. Subject to some restrictions and might not always work; see <code>sub-seek</code> command.</p>
<dt><code>Ctrl+Shift+Left and Ctrl+Shift+Right</code></p>
<dd>Adjust subtitle delay so that the next or previous subtitle is displayed now. This is especially useful to sync subtitles to audio.</p>
<dt><code>[ and ]</code></p>
<dd>Decrease/increase current playback speed by 10%.</p>
<dt><code>{ and }</code></p>
<dd>Halve/double current playback speed.</p>
<dt><code>BACKSPACE</code></p>
<dd>Reset playback speed to normal.</p>
<dt><code>Shift+BACKSPACE</code></p>
<dd>Undo the last seek. This works only if the playlist entry was not changed. Hitting it a second time will go back to the original position. See <code>revert-seek</code> command for details.</p>
<dt><code>Shift+Ctrl+BACKSPACE</code></p>
<dd>Mark the current position. This will then be used by <code>Shift+BACKSPACE</code> as revert position (once you seek back, the marker will be reset). You can use this to seek around in the file and then return to the exact position where you left off.</p>
<dt><code>&lt; and &gt;</code></p>
<dd>Go backward/forward in the playlist.</p>
<dt><code>ENTER</code></p>
<dd>Go forward in the playlist.</p>
<dt><code>p / SPACE</code></p>
<dd>Pause (pressing again unpauses).</p>
<dt><code>.</code></p>
<dd>Step forward. Pressing once will pause, every consecutive press will play one frame and then go into pause mode again.</p>
<dt><code>,</code></p>
<dd>Step backward. Pressing once will pause, every consecutive press will play one frame in reverse and then go into pause mode again.</p>
<dt><code>q</code></p>
<dd>Stop playing and quit.</p>
<dt><code>Q</code></p>
<dd>Like <code>q</code>, but store the current playback position. Playing the same file later will resume at the old playback position if possible.</p>
<dt><code>/ and *</code></p>
<dd>Decrease/increase volume.</p>
<dt><code>9 and 0</code></p>
<dd>Decrease/increase volume.</p>
<dt><code>m</code></p>
<dd>Mute sound.</p>
<dt><code>_</code></p>
<dd>Cycle through the available video tracks.</p>
<dt><code>#</code></p>
<dd>Cycle through the available audio tracks.</p>
<dt><code>f</code></p>
<dd>Toggle fullscreen (see also <code>&#8211;fs</code>).</p>
<dt><code>ESC</code></p>
<dd>Exit fullscreen mode.</p>
<dt><code>T</code></p>
<dd>Toggle stay-on-top (see also <code>&#8211;ontop</code>).</p>
<dt><code>w and W</code></p>
<dd>Decrease/increase pan-and-scan range. The <code>e</code> key does the same as <code>W</code> currently, but use is discouraged.</p>
<dt><code>o (also P)</code></p>
<dd>Show progression bar, elapsed time and total duration on the OSD.</p>
<dt><code>O</code></p>
<dd>Toggle OSD states between normal and playback time/duration.</p>
<dt><code>v</code></p>
<dd>Toggle subtitle visibility.</p>
<dt><code>j and J</code></p>
<dd>Cycle through the available subtitles.</p>
<dt><code>z and Z</code></p>
<dd>Adjust subtitle delay by +/- 0.1 seconds. The <code>x</code> key does the same as <code>Z</code> currently, but use is discouraged.</p>
<dt><code>l</code></p>
<dd>Set/clear A-B loop points. See <code>ab-loop</code> command for details.</p>
<dt><code>L</code></p>
<dd>Toggle infinite looping.</p>
<dt><code>Ctrl + and Ctrl &#8211;</code></p>
<dd>Adjust audio delay (A/V sync) by +/- 0.1 seconds.</p>
<dt><code>Shift+g and Shift+f</code></p>
<dd>Adjust subtitle font size by +/- 10%.</p>
<dt><code>u</code></p>
<dd>Switch between applying no style overrides to SSA/ASS subtitles, and overriding them almost completely with the normal subtitle style. See <code>&#8211;sub-ass-override</code> for more info.</p>
<dt><code>V</code></p>
<dd>Toggle subtitle VSFilter aspect compatibility mode. See <code>&#8211;sub-ass-vsfilter-aspect-compat</code> for more info.</p>
<dt><code>r and R</code></p>
<dd>Move subtitles up/down. The <code>t</code> key does the same as <code>R</code> currently, but use is discouraged.</p>
<dt><code>s</code></p>
<dd>Take a screenshot.</p>
<dt><code>S</code></p>
<dd>Take a screenshot, without subtitles. (Whether this works depends on VO driver support.)</p>
<dt><code>Ctrl s</code></p>
<dd>Take a screenshot, as the window shows it (with subtitles, OSD, and scaled video).</p>
<dt><code>PGUP and PGDWN</code></p>
<dd>Seek to the beginning of the previous/next chapter. In most cases, &quot;previous&quot; will actually go to the beginning of the current chapter; see <code>&#8211;chapter-seek-threshold</code>.</p>
<dt><code>Shift+PGUP and Shift+PGDWN</code></p>
<dd>Seek backward or forward by 10 minutes. (This used to be mapped to PGUP/PGDWN without Shift.)</p>
<dt><code>d</code></p>
<dd>Activate/deactivate deinterlacer.</p>
<dt><code>A</code></p>
<dd>Cycle aspect ratio override.</p>
<dt><code>Ctrl h</code></p>
<dd>Toggle hardware video decoding on/off.</p>
<dt><code>Alt+LEFT, Alt+RIGHT, Alt+UP, Alt+DOWN</code></p>
<dd>Move the video rectangle (panning).</p>
<dt><code>Alt + and Alt &#8211;</code></p>
<dd>Combining <code>Alt</code> with the <code>+</code> or <code>&#8211;</code> keys changes video zoom.</p>
<dt><code>Alt+BACKSPACE</code></p>
<dd>Reset the pan/zoom settings.</p>
<dt><code>F8</code></p>
<dd>Show the playlist and the current position in it (useful only if a UI window is used, broken on the terminal).</p>
<dt><code>F9</code></p>
<dd>Show the list of audio and subtitle streams (useful only if a UI window is used, broken on the terminal).</p>
<dt><code>i and I</code></p>
<dd>Show/toggle an overlay displaying statistics about the currently playing file such as codec, framerate, number of dropped frames and so on. See <i>STATS</i> for more information.</p>
<dt><code>del</code></p>
<dd>Cycle OSC visibility between never / auto (mouse-move) / always</p>
<dt><code>`</code></p>
<dd>Show the console. (ESC closes it again. See <i>CONSOLE</i>.) </p>
<p> (The following keys are valid only when using a video output that supports the corresponding adjustment.)</p>
<dt><code>1 and 2</code></p>
<dd>Adjust contrast.</p>
<dt><code>3 and 4</code></p>
<dd>Adjust brightness.</p>
<dt><code>5 and 6</code></p>
<dd>Adjust gamma.</p>
<dt><code>7 and 8</code></p>
<dd>Adjust saturation.</p>
<dt><code>Alt+0 (and command+0 on macOS)</code></p>
<dd>Resize video window to half its original size.</p>
<dt><code>Alt+1 (and command+1 on macOS)</code></p>
<dd>Resize video window to its original size.</p>
<dt><code>Alt+2 (and command+2 on macOS)</code></p>
<dd>Resize video window to double its original size.</p>
<dt><code>command + f (macOS only)</code></p>
<dd>Toggle fullscreen (see also <code>&#8211;fs</code>). </p>
<p> (The following keys are valid if you have a keyboard with multimedia keys.)</p>
<dt><code>PAUSE</code></p>
<dd>Pause.</p>
<dt><code>STOP</code></p>
<dd>Stop playing and quit.</p>
<dt><code>PREVIOUS and NEXT</code></p>
<dd>Seek backward/forward 1 minute. </p>
<p> If you miss some older key bindings, look at <code>etc/restore-old-bindings.conf</code> in the mpv git repository.</dl>
<h3>Mouse Control</h3>
<dl COMPACT>
<dt><code>Left double click</code></p>
<dd>Toggle fullscreen on/off.</p>
<dt><code>Right click</code></p>
<dd>Toggle pause on/off.</p>
<dt><code>Forward/Back button</code></p>
<dd>Skip to next/previous entry in playlist.</p>
<dt><code>Wheel up/down</code></p>
<dd>Seek forward/backward 10 seconds.</p>
<dt><code>Wheel left/right</code></p>
<dd>Decrease/increase volume.</dl>
<h2>Usage</h2>
<p>Command line arguments starting with <code>&#8211;</code> are interpreted as options, everything else as filenames or URLs. All options except <i>flag</i> options (or choice options which include <code>yes</code>) require a parameter in the form <code>&#8211;option=value</code>. </p>
<p> One exception is the lone <code>&#8211;</code> (without anything else), which means media data will be read from stdin. Also, <code>&#8212;</code> (without anything else) will make the player interpret all following arguments as filenames, even if they start with <code>&#8211;</code>. (To play a file named <code>&#8211;</code>, you need to use <code>./-</code>.) </p>
<p> Every <i>flag</i> option has a <i>no-flag</i> counterpart, e.g. the opposite of the <code>&#8211;fs</code> option is <code>&#8211;no-fs</code>. <code>&#8211;fs=yes</code> is same as <code>&#8211;fs</code>, <code>&#8211;fs=no</code> is the same as <code>&#8211;no-fs</code>. </p>
<p> If an option is marked as <i>(XXX only)</i>, it will only work in combination with the <i>XXX</i> option or if <i>XXX</i> is compiled in.</p>
<h3>Legacy option syntax</h3>
<p>The <code>&#8211;option=value</code> syntax is not strictly enforced, and the alternative legacy syntax <code>-option value</code> and <code>-option=value</code> will also work. This is mostly for compatibility with MPlayer. Using these should be avoided. Their semantics can change any time in the future. </p>
<p> For example, the alternative syntax will consider an argument following the option a filename. <code>mpv -fs no</code> will attempt to play a file named <code>no</code>, because <code>&#8211;fs</code> is a flag option that requires no parameter. If an option changes and its parameter becomes optional, then a command line using the alternative syntax will break. </p>
<p> Until mpv 0.31.0, there was no difference whether an option started with <code>&#8212;</code> or a single <code>&#8211;</code>. Newer mpv releases strictly expect that you pass the option value after a <code>=</code>. For example, before <code>mpv &#8211;log-file f.txt</code> would write a log to <code>f.txt</code>, but now this command line fails, as <code>&#8211;log-file</code> expects an option value, and <code>f.txt</code> is simply considered a normal file to be played (as in <code>mpv f.txt</code>). </p>
<p> The future plan is that <code>-option value</code> will not work anymore, and options with a single <code>&#8211;</code> behave the same as <code>&#8212;</code> options.</p>
<h3>Escaping spaces and other special characters</h3>
<p>Keep in mind that the shell will partially parse and mangle the arguments you pass to mpv. For example, you might need to quote or escape options and filenames: <code>mpv &quot;filename with spaces.mkv&quot; &#8211;title=&quot;window title&quot;</code> </p>
<p> It gets more complicated if the suboption parser is involved. The suboption parser puts several options into a single string, and passes them to a component at once, instead of using multiple options on the level of the command line. </p>
<p> The suboption parser can quote strings with <code>&quot;</code> and <code>[&#8230;]</code>. Additionally, there is a special form of quoting with <code>%n%</code> described below. </p>
<p> For example, assume the hypothetical <code>foo</code> filter can take multiple options: <code>mpv test.mkv &#8211;vf=foo:option1=value1:option2:option3=value3,bar</code> </p>
<p> This passes <code>option1</code> and <code>option3</code> to the <code>foo</code> filter, with <code>option2</code> as flag (implicitly <code>option2=yes</code>), and adds a <code>bar</code> filter after that. If an option contains spaces or characters like <code>,</code> or <code>:</code>, you need to quote them: <code>mpv &#8216;&#8211;vf=foo:option1=&quot;option value with spaces&quot;,bar&#8217;</code> </p>
<p> Shells may actually strip some quotes from the string passed to the commandline, so the example quotes the string twice, ensuring that mpv receives the <code>&quot;</code> quotes. </p>
<p> The <code>[&#8230;]</code> form of quotes wraps everything between <code>[</code> and <code>]</code>. It&#8217;s useful with shells that don&#8217;t interpret these characters in the middle of an argument (like bash). These quotes are balanced (since mpv 0.9.0): the <code>[</code> and <code>]</code> nest, and the quote terminates on the last <code>]</code> that has no matching <code>[</code> within the string. (For example, <code>[a[b]c]</code> results in <code>a[b]c</code>.) </p>
<p> The fixed-length quoting syntax is intended for use with external scripts and programs. </p>
<p> It is started with <code>%</code> and has the following format: </p>
<pre>%n%string_of_length_n</pre>
<dl COMPACT>
<dt>Examples</p>
<dd><code>mpv &#8216;&#8211;vf=foo:option1=%11%quoted text&#8217; test.avi</code> </p>
<p> Or in a script: </p>
<p> <code>mpv &#8211;vf=foo:option1=%`expr length &quot;$NAME&quot;`%&quot;$NAME&quot; test.avi</code> </p>
<p> Note: where applicable with JSON-IPC, <code>%n%</code> is the length in UTF-8 bytes, after decoding the JSON data. </p>
<p> Suboptions passed to the client API are also subject to escaping. Using <code>mpv_set_option_string()</code> is exactly like passing <code>&#8211;name=data</code> to the command line (but without shell processing of the string). Some options support passing values in a more structured way instead of flat strings, and can avoid the suboption parsing mess. For example, <code>&#8211;vf</code> supports <code>MPV_FORMAT_NODE</code>, which lets you pass suboptions as a nested data structure of maps and arrays.</dl>
<h3>Paths</h3>
<p>Some care must be taken when passing arbitrary paths and filenames to mpv. For example, paths starting with <code>&#8211;</code> will be interpreted as options. Likewise, if a path contains the sequence <code>://</code>, the string before that might be interpreted as protocol prefix, even though <code>://</code> can be part of a legal UNIX path. To avoid problems with arbitrary paths, you should be sure that absolute paths passed to mpv start with <code>/</code>, and prefix relative paths with <code>./</code>. </p>
<p> Using the <code>file://</code> pseudo-protocol is discouraged, because it involves strange URL unescaping rules. </p>
<p> The name <code>&#8211;</code> itself is interpreted as stdin, and will cause mpv to disable console controls. (Which makes it suitable for playing data piped to stdin.) </p>
<p> The special argument <code>&#8212;</code> can be used to stop mpv from interpreting the following arguments as options. </p>
<p> When using the client API, you should strictly avoid using <code>mpv_command_string</code> for invoking the <code>loadfile</code> command, and instead prefer e.g. <code>mpv_command</code> to avoid the need for filename escaping. </p>
<p> For paths passed to suboptions, the situation is further complicated by the need to escape special characters. To work this around, the path can be additionally wrapped in the fixed-length syntax, e.g. <code>%n%string_of_length_n</code> (see above). </p>
<p> Some mpv options interpret paths starting with <code>~</code>. Currently, the prefix <code>~~home/</code> expands to the mpv configuration directory (usually <code>~/.config/mpv/</code>). <code>~/</code> expands to the user&#8217;s home directory. (The trailing <code>/</code> is always required.) The following paths are currently recognized: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Name </td>
<td> Meaning
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>~~/</code> </td>
<td> If the subpath exists in any of the mpv&#8217;s config directories the path of the existing file/dir is returned. Otherwise this is equivalent to <code>~~home/</code>. Note that if &#8211;no-config is used <code>~~/foobar</code> will resolve to <code>foobar</code> which can be unexpected.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>~/</code> </td>
<td> user home directory root (similar to shell, <code>$HOME</code>)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>~~home/</code> </td>
<td> mpv config dir (for example <code>~/.config/mpv/</code>)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>~~global/</code> </td>
<td> the global config path, if available (not on win32)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>~~osxbundle/</code> </td>
<td> the macOS bundle resource path (macOS only)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>~~desktop/</code> </td>
<td> the path to the desktop (win32, macOS)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>~~exe_dir/</code> </td>
<td> win32 only: the path to the directory containing the exe (for config file purposes; <code>$MPV_HOME</code> overrides it)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>~~old_home/</code> </td>
<td> do not use
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h3>Per-File Options</h3>
<p>When playing multiple files, any option given on the command line usually affects all files. Example: </p>
<pre>mpv --a file1.mkv --b file2.mkv --c</pre>
<p><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> File </td>
<td> Active options
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> file1.mkv </td>
<td> <code>&#8211;a &#8211;b &#8211;c</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> file2.mkv </td>
<td> <code>&#8211;a &#8211;b &#8211;c</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> (This is different from MPlayer and mplayer2.) </p>
<p> Also, if any option is changed at runtime (via input commands), they are not reset when a new file is played. </p>
<p> Sometimes, it is useful to change options per-file. This can be achieved by adding the special per-file markers <code>&#8211;{</code> and <code>&#8211;}</code>. (Note that you must escape these on some shells.) Example: </p>
<pre>mpv --a file1.mkv --b --\{ --c file2.mkv --d file3.mkv --e --\} file4.mkv --f</pre>
<p><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> File </td>
<td> Active options
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> file1.mkv </td>
<td> <code>&#8211;a &#8211;b &#8211;f</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> file2.mkv </td>
<td> <code>&#8211;a &#8211;b &#8211;f &#8211;c &#8211;d &#8211;e</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> file3.mkv </td>
<td> <code>&#8211;a &#8211;b &#8211;f &#8211;c &#8211;d &#8211;e</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> file4.mkv </td>
<td> <code>&#8211;a &#8211;b &#8211;f</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Additionally, any file-local option changed at runtime is reset when the current file stops playing. If option <code>&#8211;c</code> is changed during playback of <code>file2.mkv</code>, it is reset when advancing to <code>file3.mkv</code>. This only affects file-local options. The option <code>&#8211;a</code> is never reset here.</p>
<h3>List Options</h3>
<p>Some options which store lists of option values can have action suffixes. For example, the <code>&#8211;display-tags</code> option takes a <code>,</code>-separated list of tags, but the option also allows you to append a single tag with <code>&#8211;display-tags-append</code>, and the tag name can for example contain a literal <code>,</code> without the need for escaping.</p>
<h3>String list and path list options</h3>
<p>String lists are separated by <code>,</code>. The strings are not parsed or interpreted by the option system itself. However, most </p>
<p> Path or file list options use <code>:</code> (Unix) or <code>;</code> (Windows) as separator, instead of <code>,</code>. </p>
<p> They support the following operations: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Suffix </td>
<td> Meaning
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -set </td>
<td> Set a list of items (using the list separator, escaped with backslash)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -append </td>
<td> Append single item (does not interpret escapes)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -add </td>
<td> Append 1 or more items (same syntax as -set)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -pre </td>
<td> Prepend 1 or more items (same syntax as -set)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -clr </td>
<td> Clear the option (remove all items)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -remove </td>
<td> Delete item if present (does not interpret escapes)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -del </td>
<td> Delete 1 or more items by integer index (deprecated)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -toggle </td>
<td> Append an item, or remove if if it already exists (no escapes)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> <code>-append</code> is meant as a simple way to append a single item without having to escape the argument (you may still need to escape on the shell level).</p>
<h3>Key/value list options</h3>
<p>A key/value list is a list of key/value string pairs. In programming languages, this type of data structure is often called a map or a dictionary. The order normally does not matter, although in some cases the order might matter. </p>
<p> They support the following operations: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Suffix </td>
<td> Meaning
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -set </td>
<td> Set a list of items (using <code>,</code> as separator)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -append </td>
<td> Append a single item (escapes for the key, no escapes for the value)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -add </td>
<td> Append 1 or more items (same syntax as -set)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -remove </td>
<td> Delete item by key if present (does not interpret escapes)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Keys are unique within the list. If an already present key is set, the existing key is removed before the new value is appended. </p>
<p> If you want to pass a value without interpreting it for escapes or <code>,</code>, it is recommended to use the <code>-add</code> variant. When using libmpv, prefer using <code>MPV_FORMAT_NODE_MAP</code>; when using a scripting backend or the JSON IPC, use an appropriate structured data type. </p>
<p> Prior to mpv 0.33, <code>:</code> was also recognized as separator by <code>-set</code>.</p>
<h3>Filter options</h3>
<p>This is a very complex option type for the <code>&#8211;af</code> and <code>&#8211;vf</code> options only. They often require complicated escaping. See <i>VIDEO FILTERS</i> for details. They support the following operations: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Suffix </td>
<td> Meaning
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -set </td>
<td> Set a list of filters (using <code>,</code> as separator)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -append </td>
<td> Append single filter
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -add </td>
<td> Append 1 or more filters (same syntax as -set)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -pre </td>
<td> Prepend 1 or more filters (same syntax as -set)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -clr </td>
<td> Clear the option (remove all filters)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -remove </td>
<td> Delete filter if present
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -del </td>
<td> Delete 1 or more filters by integer index or filter label (deprecated)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -toggle </td>
<td> Append a filter, or remove if if it already exists
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> -help </td>
<td> Pseudo operation that prints a help text to the terminal
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h3>General</h3>
<p>Without suffix, the operation used is normally <code>-set</code>. </p>
<p> Although some operations allow specifying multiple items, using this is strongly discouraged and deprecated, except for <code>-set</code>. There is a chance that operations like <code>-add</code> and <code>-pre</code> will work like <code>-append</code> and accept a single, unescaped item only (so the <code>,</code> separator will not be interpreted and is passed on as part of the value). </p>
<p> Some options (like <code>&#8211;sub-file</code>, <code>&#8211;audio-file</code>, <code>&#8211;glsl-shader</code>) are aliases for the proper option with <code>-append</code> action. For example, <code>&#8211;sub-file</code> is an alias for <code>&#8211;sub-files-append</code>. </p>
<p> Options of this type can be changed at runtime using the <code>change-list</code> command, which takes the suffix (without the <code>&#8211;</code>) as separate operation parameter.</p>
<h2>Configuration Files</h2>
<h3>Location and Syntax</h3>
<p>You can put all of the options in configuration files which will be read every time mpv is run. The system-wide configuration file &#8216;mpv.conf&#8217; is in your configuration directory (e.g. <code>/etc/mpv</code> or <code>/usr/local/etc/mpv</code>), the user-specific one is <code>~/.config/mpv/mpv.conf</code>. For details and platform specifics (in particular Windows paths) see the <i>FILES</i> section. </p>
<p> User-specific options override system-wide options and options given on the command line override either. The syntax of the configuration files is <code>option=value</code>. Everything after a <i>#</i> is considered a comment. Options that work without values can be enabled by setting them to <i>yes</i> and disabled by setting them to <i>no</i>. Even suboptions can be specified in this way.</p>
<dl COMPACT>
<dt>Example configuration file</p>
<dd>
<pre># Use GPU-accelerated video output by default.
vo=gpu
# Use quotes for text that can contain spaces:
term-status-msg=&quot;Time: ${time-pos}&quot;</pre>
</dl>
<h3>Escaping spaces and special characters</h3>
<p>This is done like with command line options. The shell is not involved here, but option values still need to be quoted as a whole if it contains certain characters like spaces. A config entry can be quoted with <code>&quot;</code>, as well as with the fixed-length syntax (<code>%n%</code>) mentioned before. This is like passing the exact contents of the quoted string as command line option. C-style escapes are currently _not_ interpreted on this level, although some options do this manually. (This is a mess and should probably be changed at some point.)</p>
<h3>Putting Command Line Options into the Configuration File</h3>
<p>Almost all command line options can be put into the configuration file. Here is a small guide: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Option </td>
<td> Configuration file entry
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>&#8211;flag</code> </td>
<td> <code>flag</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>-opt val</code> </td>
<td> <code>opt=val</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>&#8211;opt=val</code> </td>
<td> <code>opt=val</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>-opt &quot;has spaces&quot;</code> </td>
<td> <code>opt=&quot;has spaces&quot;</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h3>File-specific Configuration Files</h3>
<p>You can also write file-specific configuration files. If you wish to have a configuration file for a file called &#8216;video.avi&#8217;, create a file named &#8216;video.avi.conf&#8217; with the file-specific options in it and put it in <code>~/.config/mpv/</code>. You can also put the configuration file in the same directory as the file to be played. Both require you to set the <code>&#8211;use-filedir-conf</code> option (either on the command line or in your global config file). If a file-specific configuration file is found in the same directory, no file-specific configuration is loaded from <code>~/.config/mpv</code>. In addition, the <code>&#8211;use-filedir-conf</code> option enables directory-specific configuration files. For this, mpv first tries to load a mpv.conf from the same directory as the file played and then tries to load any file-specific configuration.</p>
<h3>Profiles</h3>
<p>To ease working with different configurations, profiles can be defined in the configuration files. A profile starts with its name in square brackets, e.g. <code>[my-profile]</code>. All following options will be part of the profile. A description (shown by <code>&#8211;profile=help</code>) can be defined with the <code>profile-desc</code> option. To end the profile, start another one or use the profile name <code>default</code> to continue with normal options. </p>
<p> You can list profiles with <code>&#8211;profile=help</code>, and show the contents of a profile with <code>&#8211;show-profile=&lt;name&gt;</code> (replace <code>&lt;name&gt;</code> with the profile name). You can apply profiles on start with the <code>&#8211;profile=&lt;name&gt;</code> option, or at runtime with the <code>apply-profile &lt;name&gt;</code> command.</p>
<dl COMPACT>
<dt>Example mpv config file with profiles</p>
<dd>
<pre># normal top-level option
fullscreen=yes
# a profile that can be enabled with --profile=big-cache
[big-cache]
cache=yes
demuxer-max-bytes=123400KiB
demuxer-readahead-secs=20
[slow]
profile-desc=&quot;some profile name&quot;
# reference a builtin profile
profile=gpu-hq
[fast]
vo=vdpau
# using a profile again extends it
[slow]
framedrop=no
# you can also include other profiles
profile=big-cache</pre>
</dl>
<h3>Runtime profiles</h3>
<p>Profiles can be set at runtime with <code>apply-profile</code> command. Since this operation is &quot;destructive&quot; (every item in a profile is simply set as an option, overwriting the previous value), you can&#8217;t just enable and disable profiles again. </p>
<p> As a partial remedy, there is a way to make profiles save old option values before overwriting them with the profile values, and then restoring the old values at a later point using <code>apply-profile &lt;profile-name&gt; restore</code>. </p>
<p> This can be enabled with the <code>profile-restore</code> option, which takes one of the following options:</p>
<dl COMPACT>
<dt><code>default</code></p>
<dd>Does nothing, and nothing can be restored (default).</p>
<dt><code>copy</code></p>
<dd>When applying a profile, copy the old values of all profile options to a backup before setting them from the profile. These options are reset to their old values using the backup when restoring. </p>
<p> Every profile has its own list of backed up values. If the backup already exists (e.g. if <code>apply-profile name</code> was called more than once in a row), the existing backup is no changed. The restore operation will remove the backup. </p>
<p> It&#8217;s important to know that restoring does not &quot;undo&quot; setting an option, but simply copies the old option value. Consider for example <code>vf-add</code>, appends an entry to <code>vf</code>. This mechanism will simply copy the entire <code>vf</code> list, and does _not_ execute the inverse of <code>vf-add</code> (that would be <code>vf-remove</code>) on restoring. </p>
<p> Note that if a profile contains recursive profiles (via the <code>profile</code> option), the options in these recursive profiles are treated as if they were part of this profile. The referenced profile&#8217;s backup list is not used when creating or using the backup. Restoring a profile does not restore referenced profiles, only the options of referenced profiles (as if they were part of the main profile).</p>
<dt><code>copy-equal</code></p>
<dd>Similar to <code>copy</code>, but restore an option only if it has the same value as the value effectively set by the profile. This tries to deal with the situation when the user does not want the option to be reset after interactively changing it.</p>
<dt>Example</p>
<dd>
<pre>[something]
profile-restore=copy-equal
vf-add=rotate=90</pre>
<p>Then running these commands will result in behavior as commented: </p>
<pre>set vf vflip
apply-profile something
vf-add=hflip
apply-profile something
# vf == vflip,rotate=90,hflip,rotate=90
apply-profile something restore
# vf == vflip</pre>
</dl>
<h3>Conditional auto profiles</h3>
<p>Profiles which have the <code>profile-cond</code> option set are applied automatically if the associated condition matches (unless auto profiles are disabled). The option takes a string, which is interpreted as Lua condition. If evaluating the expression returns true, the profile is applied, if it returns false, it is ignored. This Lua code execution is not sandboxed. </p>
<p> Any variables in condition expressions can reference properties. If an identifier is not already defined by Lua or mpv, it is interpreted as property. For example, <code>pause</code> would return the current pause status. You cannot reference properties with <code>&#8211;</code> this way since that would denote a subtraction, but if the variable name contains any <code>_</code> characters, they are turned into <code>&#8211;</code>. For example, <code>playback_time</code> would return the property <code>playback-time</code>. </p>
<p> A more robust way to access properties is using <code>p.property_name</code> or <code>get(&quot;property-name&quot;, default_value)</code>. The automatic variable to property magic will break if a new identifier with the same name is introduced (for example, if a function named <code>pause()</code> were added, <code>pause</code> would return a function value instead of the value of the <code>pause</code> property). </p>
<p> Note that if a property is not available, it will return <code>nil</code>, which can cause errors if used in expressions. These are logged in verbose mode, and the expression is considered to be false. </p>
<p> Whenever a property referenced by a profile condition changes, the condition is re-evaluated. If the return value of the condition changes from false or error to true, the profile is applied. </p>
<p> This mechanism tries to &quot;unapply&quot; profiles once the condition changes from true to false. If you want to use this, you need to set <code>profile-restore</code> for the profile. Another possibility it to create another profile with an inverse condition to undo the other profile. </p>
<p> Recursive profiles can be used. But it is discouraged to reference other conditional profiles in a conditional profile, since this can lead to tricky and unintuitive behavior.</p>
<dl COMPACT>
<dt>Example</p>
<dd>Make only HD video look funny: </p>
<pre>[something]
profile-desc=HD video sucks
profile-cond=width &gt;= 1280
hue=-50</pre>
<p>If you want the profile to be reverted if the condition goes to false again, you can set <code>profile-restore</code>: </p>
<pre>[something]
profile-desc=Mess up video when entering fullscreen
profile-cond=fullscreen
profile-restore=copy
vf-add=rotate=90</pre>
<p>This appends the <code>rotate</code> filter to the video filter chain when entering fullscreen. When leaving fullscreen, the <code>vf</code> option is set to the value it had before entering fullscreen. Note that this would also remove any other filters that were added during fullscreen mode by the user. Avoiding this is trickier, and could for example be solved by adding a second profile with an inverse condition and operation: </p>
<pre>[something]
profile-cond=fullscreen
vf-add=@rot:rotate=90
[something-inv]
profile-cond=not fullscreen
vf-remove=@rot</pre>
<p><code>WARNING:</code> Every time an involved property changes, the condition is evaluated again. If your condition uses <code>p.playback_time</code> for example, the condition is re-evaluated approximately on every video frame. This is probably slow. </p>
<p> This feature is managed by an internal Lua script. Conditions are executed as Lua code within this script. Its environment contains at least the following things:</p>
<dt><code>(function environment table)</code></p>
<dd>Every Lua function has an environment table. This is used for identifier access. There is no named Lua symbol for it; it is implicit. </p>
<p> The environment does &quot;magic&quot; accesses to mpv properties. If an identifier is not already defined in <code>_G</code>, it retrieves the mpv property of the same name. Any occurrences of <code>_</code> in the name are replaced with <code>&#8211;</code> before reading the property. The returned value is as retrieved by <code>mp.get_property_native(name)</code>. Internally, a cache of property values, updated by observing the property is used instead, so properties that are not observable will be stuck at the initial value forever. </p>
<p> If you want to access properties, that actually contain <code>_</code> in the name, use <code>get()</code> (which does not perform transliteration). </p>
<p> Internally, the environment table has a <code>__index</code> meta method set, which performs the access logic.</p>
<dt><code>p</code></p>
<dd>A &quot;magic&quot; table similar to the environment table. Unlike the latter, this does not prefer accessing variables defined in <code>_G</code> &#8211; it always accesses properties.</p>
<dt><code>get(name [, def])</code></p>
<dd>Read a property and return its value. If the property value is <code>nil</code> (e.g. if the property does not exist), <code>def</code> is returned. </p>
<p> This is superficially similar to <code>mp.get_property_native(name)</code>. An important difference is that this accesses the property cache, and enables the change detection logic (which is essential to the dynamic runtime behavior of auto profiles). Also, it does not return an error value as second return value. </p>
<p> The &quot;magic&quot; tables mentioned above use this function as backend. It does not perform the <code>_</code> transliteration. </p>
<p> In addition, the same environment as in a blank mpv Lua script is present. For example, <code>math</code> is defined and gives access to the Lua standard math library. </p>
<p> <code>WARNING:</code> This feature is subject to change indefinitely. You might be forced to adjust your profiles on mpv updates.</dl>
<h3>Legacy auto profiles</h3>
<p>Some profiles are loaded automatically using a legacy mechanism. The following example demonstrates this:</p>
<dl COMPACT>
<dt>Auto profile loading</p>
<dd>
<pre>[extension.mkv]
profile-desc=&quot;profile for .mkv files&quot;
vf=vflip</pre>
<p>The profile name follows the schema <code>type.name</code>, where type can be <code>protocol</code> for the input/output protocol in use (see <code>&#8211;list-protocols</code>), and <code>extension</code> for the extension of the path of the currently played file (<i>not</i> the file format). </p>
<p> This feature is very limited, and is considered soft-deprecated. Use conditional auto profiles.</dl>
<h2>Using Mpv From Other Programs Or Scripts</h2>
<p>There are three choices for using mpv from other programs or scripts:</p>
<dl COMPACT>
<dt>1.</p>
<dd>Calling it as UNIX process. If you do this, <i>do not parse terminal output</i>. The terminal output is intended for humans, and may change any time. In addition, terminal behavior itself may change any time. Compatibility cannot be guaranteed. </p>
<p> Your code should work even if you pass <code>&#8211;no-terminal</code>. Do not attempt to simulate user input by sending terminal control codes to mpv&#8217;s stdin. If you need interactive control, using <code>&#8211;input-ipc-server</code> is recommended. This gives you access to the <i>JSON IPC</i> over unix domain sockets (or named pipes on Windows). </p>
<p> Depending on what you do, passing <code>&#8211;no-config</code> or <code>&#8211;config-dir</code> may be a good idea to avoid conflicts with the normal mpv user configuration intended for CLI playback. </p>
<p> Using <code>&#8211;input-ipc-server</code> is also suitable for purposes like remote control (however, the IPC protocol itself is not &quot;secure&quot; and not intended to be so).</p>
<dt>2.</p>
<dd>Using libmpv. This is generally recommended when mpv is used as playback backend for a completely different application. The provided C API is very close to CLI mechanisms and the scripting API. </p>
<p> Note that even though libmpv has different defaults, it can be configured to work exactly like the CLI player (except command line parsing is unavailable). </p>
<p> See <i>EMBEDDING INTO OTHER PROGRAMS (LIBMPV)</i>.</p>
<dt>3.</p>
<dd>As a user script (<i>LUA SCRIPTING</i>, <i>JAVASCRIPT</i>, <i>C PLUGINS</i>). This is recommended when the goal is to &quot;enhance&quot; the CLI player. Scripts get access to the entire client API of mpv. </p>
<p> This is the standard way to create third-party extensions for the player. </p>
<p> All these access the client API, which is the sum of the various mechanisms provided by the player core, as documented here: <i>OPTIONS</i>, <i>List of Input Commands</i>, <i>Properties</i>, <i>List of events</i> (also see C API), <i>Hooks</i>.</dl>
<h2>Taking Screenshots</h2>
<p>Screenshots of the currently played file can be taken using the &#8216;screenshot&#8217; input mode command, which is by default bound to the <code>s</code> key. Files named <code>mpv-shotNNNN.jpg</code> will be saved in the working directory, using the first available number &#8211; no files will be overwritten. In pseudo-GUI mode, the screenshot will be saved somewhere else. See <i>PSEUDO GUI MODE</i>. </p>
<p> A screenshot will usually contain the unscaled video contents at the end of the video filter chain and subtitles. By default, <code>S</code> takes screenshots without subtitles, while <code>s</code> includes subtitles. </p>
<p> Unlike with MPlayer, the <code>screenshot</code> video filter is not required. This filter was never required in mpv, and has been removed.</p>
<h2>Terminal Status Line</h2>
<p>During playback, mpv shows the playback status on the terminal. It looks like something like this: <code>AV: 00:03:12 / 00:24:25 (13%) A-V: -0.000</code> </p>
<p> The status line can be overridden with the <code>&#8211;term-status-msg</code> option. </p>
<p> The following is a list of things that can show up in the status line. Input properties, that can be used to get the same information manually, are also listed.</p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>AV:</code> or <code>V:</code> (video only) or <code>A:</code> (audio only)</p>
<dt>&bull;</p>
<dd>The current time position in <code>HH:MM:SS</code> format (<code>playback-time</code> property)</p>
<dt>&bull;</p>
<dd>The total file duration (absent if unknown) (<code>duration</code> property)</p>
<dt>&bull;</p>
<dd>Playback speed, e.g. <code>x2.0</code>. Only visible if the speed is not normal. This is the user-requested speed, and not the actual speed (usually they should be the same, unless playback is too slow). (<code>speed</code> property.)</p>
<dt>&bull;</p>
<dd>Playback percentage, e.g. <code>(13%)</code>. How much of the file has been played. Normally calculated out of playback position and duration, but can fallback to other methods (like byte position) if these are not available. (<code>percent-pos</code> property.)</p>
<dt>&bull;</p>
<dd>The audio/video sync as <code>A-V: 0.000</code>. This is the difference between audio and video time. Normally it should be 0 or close to 0. If it&#8217;s growing, it might indicate a playback problem. (<code>avsync</code> property.)</p>
<dt>&bull;</p>
<dd>Total A/V sync change, e.g. <code>ct: -0.417</code>. Normally invisible. Can show up if there is audio &quot;missing&quot;, or not enough frames can be dropped. Usually this will indicate a problem. (<code>total-avsync-change</code> property.)</p>
<dt>&bull;</p>
<dd>Encoding state in <code>{&#8230;}</code>, only shown in encoding mode.</p>
<dt>&bull;</p>
<dd>Display sync state. If display sync is active (<code>display-sync-active</code> property), this shows <code>DS: 2.500/13</code>, where the first number is average number of vsyncs per video frame (e.g. 2.5 when playing 24Hz videos on 60Hz screens), which might jitter if the ratio doesn&#8217;t round off, or there are mistimed frames (<code>vsync-ratio</code>), and the second number of estimated number of vsyncs which took too long (<code>vo-delayed-frame-count</code> property). The latter is a heuristic, as it&#8217;s generally not possible to determine this with certainty.</p>
<dt>&bull;</p>
<dd>Dropped frames, e.g. <code>Dropped: 4</code>. Shows up only if the count is not 0. Can grow if the video framerate is higher than that of the display, or if video rendering is too slow. May also be incremented on &quot;hiccups&quot; and when the video frame couldn&#8217;t be displayed on time. (<code>frame-drop-count</code> property.) If the decoder drops frames, the number of decoder-dropped frames is appended to the display as well, e.g.: <code>Dropped: 4/34</code>. This happens only if decoder frame dropping is enabled with the <code>&#8211;framedrop</code> options. (<code>decoder-frame-drop-count</code> property.)</p>
<dt>&bull;</p>
<dd>Cache state, e.g. <code>Cache: 2s/134KB</code>. Visible if the stream cache is enabled. The first value shows the amount of video buffered in the demuxer in seconds, the second value shows the estimated size of the buffered amount in kilobytes. (<code>demuxer-cache-duration</code> and <code>demuxer-cache-state</code> properties.)</dl>
<h2>Low Latency Playback</h2>
<p>mpv is optimized for normal video playback, meaning it actually tries to buffer as much data as it seems to make sense. This will increase latency. Reducing latency is possible only by specifically disabling features which increase latency. </p>
<p> The builtin <code>low-latency</code> profile tries to apply some of the options which can reduce latency. You can use <code>&#8211;profile=low-latency</code> to apply all of them. You can list the contents with <code>&#8211;show-profile=low-latency</code> (some of the options are quite obscure, and may change every mpv release). </p>
<p> Be aware that some of the options can reduce playback quality. </p>
<p> Most latency is actually caused by inconvenient timing behavior. You can disable this with <code>&#8211;untimed</code>, but it will likely break, unless the stream has no audio, and the input feeds data to the player at a constant rate. </p>
<p> Another common problem is with MJPEG streams. These do not signal the correct framerate. Using <code>&#8211;untimed</code> or <code>&#8211;no-correct-pts &#8211;fps=60</code> might help. </p>
<p> For livestreams, data can build up due to pausing the stream, due to slightly lower playback rate, or &quot;buffering&quot; pauses. If the demuxer cache is enabled, these can be skipped manually. The experimental <code>drop-buffers</code> command can be used to discard any buffered data, though it&#8217;s very disruptive. </p>
<p> In some cases, manually tuning TCP buffer sizes and such can help to reduce latency. </p>
<p> Additional options that can be tried:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>&#8211;opengl-glfinish=yes</code>, can reduce buffering in the graphics driver</p>
<dt>&bull;</p>
<dd><code>&#8211;opengl-swapinterval=0</code>, same</p>
<dt>&bull;</p>
<dd><code>&#8211;vo=xv</code>, same</p>
<dt>&bull;</p>
<dd>without audio <code>&#8211;framedrop=no &#8211;speed=1.01</code> may help for live sources (results can be mixed)</dl>
<h2>Protocols</h2>
<p><code><a rel="nofollow" href="http://...">http://&#8230;</a></code>, <code>https://</code>, &#8230; Many network protocols are supported, but the protocol prefix must always be specified. mpv will never attempt to guess whether a filename is actually a network address. A protocol prefix is always required. </p>
<p> Note that not all prefixes are documented here. Undocumented prefixes are either aliases to documented protocols, or are just redirections to protocols implemented and documented in FFmpeg. </p>
<p> <code>data:</code> is supported in FFmpeg (not in Libav), but needs to be in the format <code>data://</code>. This is done to avoid ambiguity with filenames. You can also prefix it with <code>lavf://</code> or <code>ffmpeg://</code>. </p>
<p> <code><a href="ytdl://...">ytdl://&#8230;</a></code> By default, the youtube-dl hook script only looks at http(s) URLs. Prefixing an URL with <code>ytdl://</code> forces it to be always processed by the script. This can also be used to invoke special youtube-dl functionality like playing a video by ID or invoking search. </p>
<p> Keep in mind that you can&#8217;t pass youtube-dl command line options by this, and you have to use <code>&#8211;ytdl-raw-options</code> instead. </p>
<p> <code>&#8211;</code> Play data from stdin. </p>
<p> <code><a href="smb://PATH">smb://PATH</a></code> Play a path from Samba share. (Requires FFmpeg support.) </p>
<p> <code>bd://[title][/device]</code> <code>&#8211;bluray-device=PATH</code> Play a Blu-ray disc. Since libbluray 1.0.1, you can read from ISO files by passing them to <code>&#8211;bluray-device</code>. </p>
<p> <code>title</code> can be: <code>longest</code> or <code>first</code> (selects the default playlist); <code>mpls/&lt;number&gt;</code> (selects &lt;number&gt;.mpls playlist); <code>&lt;number&gt;</code> (select playlist with the same index). mpv will list the available playlists on loading. </p>
<p> <code>bluray://</code> is an alias. </p>
<p> <code><a href="dvd://[title][/device]">dvd://[title][/device]</a></code> <code>&#8211;dvd-device=PATH</code> Play a DVD. DVD menus are not supported. If no title is given, the longest title is auto-selected. Without <code>&#8211;dvd-device</code>, it will probably try to open an actual optical drive, if available and implemented for the OS. </p>
<p> <code>dvdnav://</code> is an old alias for <code>dvd://</code> and does exactly the same thing. </p>
<p> <code><a href="dvb://[cardnumber@]channel">dvb://[cardnumber@]channel</a></code> <code>&#8211;dvbin-&#8230;</code> Digital TV via DVB. (Linux only.) </p>
<p> <code>mf://[filemask|@listfile]</code> <code>&#8211;mf-&#8230;</code> Play a series of images as video. </p>
<p> <code><a href="cdda://[device]">cdda://[device]</a></code> <code>&#8211;cdrom-device=PATH</code> <code>&#8211;cdda-&#8230;</code> Play CD. </p>
<p> <code><a href="lavf://...">lavf://&#8230;</a></code> Access any FFmpeg/Libav libavformat protocol. Basically, this passed the string after the <code>//</code> directly to libavformat. </p>
<p> <code>av://type:options</code> This is intended for using libavdevice inputs. <code>type</code> is the libavdevice demuxer name, and <code>options</code> is the (pseudo-)filename passed to the demuxer.</p>
<dl COMPACT>
<dt>Example</p>
<dd>
<pre>mpv av://v4l2:/dev/video0 --profile=low-latency --untimed</pre>
<p>This plays video from the first v4l input with nearly the lowest latency possible. It&#8217;s a good replacement for the removed <code>tv://</code> input. Using <code>&#8211;untimed</code> is a hack to output a captured frame immediately, instead of respecting the input framerate. (There may be better ways to handle this in the future.) </p>
<p> <code>avdevice://</code> is an alias. </p>
<p> <code>file://PATH</code> A local path as URL. Might be useful in some special use-cases. Note that <code>PATH</code> itself should start with a third <code>/</code> to make the path an absolute path. </p>
<p> <code>appending://PATH</code> Play a local file, but assume it&#8217;s being appended to. This is useful for example for files that are currently being downloaded to disk. This will block playback, and stop playback only if no new data was appended after a timeout of about 2 seconds. </p>
<p> Using this is still a bit of a bad idea, because there is no way to detect if a file is actually being appended, or if it&#8217;s still written. If you&#8217;re trying to play the output of some program, consider using a pipe (<code>something | mpv &#8211;</code>). If it really has to be a file on disk, use tail to make it wait forever, e.g. <code>tail -f -c +0 file.mkv | mpv &#8211;</code>. </p>
<p> <code>fd://123</code> Read data from the given file descriptor (for example 123). This is similar to piping data to stdin via <code>&#8211;</code>, but can use an arbitrary file descriptor. mpv may modify some file descriptor properties when the stream layer &quot;opens&quot; it. </p>
<p> <code>fdclose://123</code> Like <code>fd://</code>, but the file descriptor is closed after use. When using this you need to ensure that the same fd URL will only be used once. </p>
<p> <code><a href="edl://[edl">edl://[edl</a> specification as in edl-mpv.rst]</code> Stitch together parts of multiple files and play them. </p>
<p> <code><a href="slice://start[-end]@URL">slice://start[-end]@URL</a></code> Read a slice of a stream. </p>
<p> <code>start</code> and <code>end</code> represent a byte range and accept suffixes such as <code>KiB</code> and <code>MiB</code>. <code>end</code> is optional. </p>
<p> if <code>end</code> starts with <code>+</code>, it is considered as offset from <code>start</code>. </p>
<p> Only works with seekable streams. </p>
<p> Examples: </p>
<pre>mpv <a href="slice://1g-2g@cap.ts">slice://1g-2g@cap.ts</a>
This starts reading from cap.ts after seeking 1 GiB, then
reads until reaching 2 GiB or end of file.
mpv <a href="slice://1g-+2g@cap.ts">slice://1g-+2g@cap.ts</a>
This starts reading from cap.ts after seeking 1 GiB, then
reads until reaching 3 GiB or end of file.
mpv <a href="slice://100m@appending://cap.ts">slice://100m@appending://cap.ts</a>
This starts reading from cap.ts after seeking 100MiB, then
reads until end of file.</pre>
<p><code>null://</code> Simulate an empty file. If opened for writing, it will discard all data. The <code>null</code> demuxer will specifically pass autoprobing if this protocol is used (while it&#8217;s not automatically invoked for empty files). </p>
<p> <code><a href="memory://data">memory://data</a></code> Use the <code>data</code> part as source data. </p>
<p> <code><a href="hex://data">hex://data</a></code> Like <code>memory://</code>, but the string is interpreted as hexdump.</dl>
<h2>Pseudo Gui Mode</h2>
<p>mpv has no official GUI, other than the OSC (<i>ON SCREEN CONTROLLER</i>), which is not a full GUI and is not meant to be. However, to compensate for the lack of expected GUI behavior, mpv will in some cases start with some settings changed to behave slightly more like a GUI mode. </p>
<p> Currently this happens only in the following cases:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>if started using the <code>mpv.desktop</code> file on Linux (e.g. started from menus or file associations provided by desktop environments)</p>
<dt>&bull;</p>
<dd>if started from explorer.exe on Windows (technically, if it was started on Windows, and all of the stdout/stderr/stdin handles are unset)</p>
<dt>&bull;</p>
<dd>started out of the bundle on macOS</p>
<dt>&bull;</p>
<dd>if you manually use <code>&#8211;player-operation-mode=pseudo-gui</code> on the command line </p>
<p> This mode applies options from the builtin profile <code>builtin-pseudo-gui</code>, but only if these haven&#8217;t been set in the user&#8217;s config file or on the command line, which is the main difference to using <code>&#8211;profile=builtin-pseudo-gui</code>. </p>
<p> The profile is currently defined as follows: </p>
<pre>[builtin-pseudo-gui]
terminal=no
force-window=yes
idle=once
screenshot-directory=~~desktop/</pre>
<p>The <code>pseudo-gui</code> profile exists for compatibility. The options in the <code>pseudo-gui</code> profile are applied unconditionally. In addition, the profile makes sure to enable the pseudo-GUI mode, so that <code>&#8211;profile=pseudo-gui</code> works like in older mpv releases: </p>
<pre>[pseudo-gui]
player-operation-mode=pseudo-gui</pre>
<p><code>WARNING:</code> Currently, you can extend the <code>pseudo-gui</code> profile in the config file the normal way. This is deprecated. In future mpv releases, the behavior might change, and not apply your additional settings, and/or use a different profile name.</dl>
<h2>Linux Desktop Issues</h2>
<p>This subsection describes common problems on the Linux desktop. None of these problems exist on systems like Windows or macOS.</p>
<h3>Disabling Screensaver</h3>
<p>By default, mpv tries to disable the OS screensaver during playback (only if a VO using the OS GUI API is active). <code>&#8211;stop-screensaver=no</code> disables this. </p>
<p> A common problem is that Linux desktop environments ignore the standard screensaver APIs on which mpv relies. In particular, mpv uses the Screen Saver extension (XSS) on X11, and the idle-inhibit on Wayland. </p>
<p> GNOME is one of the worst offenders, and ignores even the now widely supported idle-inhibit protocol. (This is either due to a combination of malice and incompetence, but since implementing this protocol would only take a few lines of code, it is most likely the former. You will also notice how GNOME advocates react offended whenever their sabotage is pointed out, which indicates either hypocrisy, or even worse ignorance.) </p>
<p> Such incompatible desktop environments (i.e. which ignore standards) typically require using a DBus API. This is ridiculous in several ways. The immediate practical problem is that it would require adding a quite unwieldy dependency for a DBus library, somehow integrating its mainloop into mpv, and other generally unacceptable things. </p>
<p> However, since mpv does not officially support GNOME, this is not much of a problem. If you are one of those miserable users who want to use mpv on GNOME, report a bug on the GNOME issue tracker: <i><a rel="nofollow" href="https://gitlab.gnome.org/groups/GNOME/-/issues">https://gitlab.gnome.org/groups/GNOME/-/issues</a></i> </p>
<p> Alternatively, you may be able to write a Lua script that calls the <code>xdg-screensaver</code> command line program. (By the way, this a command line program is an utterly horrible kludge that tries to identify your DE, and then tries to send the correct DBus command via a DBus CLI tool.) If you find the idea of having to write a script just so your screensaver doesn&#8217;t kick in ridiculous, do not use GNOME, or use GNOME video software instead of mpv (good luck). </p>
<p> Before mpv 0.33.0, the X11 backend ran <code>xdg-screensaver reset</code> in 10 second intervals when not paused. This hack was removed in 0.33.0.</p>
<h2>Options</h2>
<h3>Track Selection</h3>
<dl COMPACT>
<dt><code>&#8211;alang=&lt;languagecode[,languagecode,&#8230;]&gt;</code></p>
<dd>Specify a priority list of audio languages to use. Different container formats employ different language codes. DVDs use ISO 639-1 two-letter language codes, Matroska, MPEG-TS and NUT use ISO 639-2 three-letter language codes, while OGM uses a free-form identifier. See also <code>&#8211;aid</code>. </p>
<p> This is a string list option. See <i>List Options</i> for details.</p>
<dt>Examples</p>
<dd>
<dt>&bull;</p>
<dd><code>mpv <a href="dvd://1">dvd://1</a> &#8211;alang=hu,en</code> chooses the Hungarian language track on a DVD and falls back on English if Hungarian is not available.</p>
<dt>&bull;</p>
<dd><code>mpv &#8211;alang=jpn example.mkv</code> plays a Matroska file with Japanese audio.</p>
<dt><code>&#8211;slang=&lt;languagecode[,languagecode,&#8230;]&gt;</code></p>
<dd>Specify a priority list of subtitle languages to use. Different container formats employ different language codes. DVDs use ISO 639-1 two letter language codes, Matroska uses ISO 639-2 three letter language codes while OGM uses a free-form identifier. See also <code>&#8211;sid</code>. </p>
<p> This is a string list option. See <i>List Options</i> for details.</p>
<dt>Examples</p>
<dd>
<dt>&bull;</p>
<dd><code>mpv <a href="dvd://1">dvd://1</a> &#8211;slang=hu,en</code> chooses the Hungarian subtitle track on a DVD and falls back on English if Hungarian is not available.</p>
<dt>&bull;</p>
<dd><code>mpv &#8211;slang=jpn example.mkv</code> plays a Matroska file with Japanese subtitles.</p>
<dt><code>&#8211;vlang=&lt;&#8230;&gt;</code></p>
<dd>Equivalent to <code>&#8211;alang</code> and <code>&#8211;slang</code>, for video tracks. </p>
<p> This is a string list option. See <i>List Options</i> for details.</p>
<dt><code>&#8211;aid=&lt;ID|auto|no&gt;</code></p>
<dd>Select audio track. <code>auto</code> selects the default, <code>no</code> disables audio. See also <code>&#8211;alang</code>. mpv normally prints available audio tracks on the terminal when starting playback of a file. </p>
<p> <code>&#8211;audio</code> is an alias for <code>&#8211;aid</code>. </p>
<p> <code>&#8211;aid=no</code> or <code>&#8211;audio=no</code> or <code>&#8211;no-audio</code> disables audio playback. (The latter variant does not work with the client API.) </p>
<p> <code>NOTE:</code> The track selection options (<code>&#8211;aid</code> but also <code>&#8211;sid</code> and the others) sometimes expose behavior that may appear strange. Also, the behavior tends to change around with each mpv release. </p>
<p> The track selection properties will return the option value outside of playback (as expected), but during playback, the affective track selection is returned. For example, with <code>&#8211;aid=auto</code>, the <code>aid</code> property will suddenly return <code>2</code> after playback initialization (assuming the file has at least 2 audio tracks, and the second is the default). </p>
<p> At mpv 0.32.0 (and some releases before), if you passed a track value for which a corresponding track didn&#8217;t exist (e.g. <code>&#8211;aid=2</code> and there was only 1 audio track), the <code>aid</code> property returned <code>no</code>. However if another audio track was added during playback, and you tried to set the <code>aid</code> property to <code>2</code>, nothing happened, because the <code>aid</code> option still had the value <code>2</code>, and writing the same value has no effect. </p>
<p> With mpv 0.33.0, the behavior was changed. Now track selection options are reset to <code>auto</code> at playback initialization, if the option had tries to select a track that does not exist. The same is done if the track exists, but fails to initialize. The consequence is that unlike before mpv 0.33.0, the user&#8217;s track selection parameters are clobbered in certain situations. </p>
<p> Also since mpv 0.33.0, trying to select a track by number will strictly select this track. Before this change, trying to select a track which did not exist would fall back to track default selection at playback initialization. The new behavior is more consistent. </p>
<p> Setting a track selection property at runtime, and then playing a new file might reset the track selection to defaults, if the fingerprint of the track list of the new file is different. </p>
<p> Be aware of tricky combinations of all of all of the above: for example, <code>mpv &#8211;aid=2 file_with_2_audio_tracks.mkv file_with_1_audio_track.mkv</code> would first play the correct track, and the second file without audio. If you then go back the first file, its first audio track will be played, and the second file is played with audio. If you do the same thing again but instead of using <code>&#8211;aid=2</code> you run <code>set aid 2</code> while the file is playing, then changing to the second file will play its audio track. This is because runtime selection enables the fingerprint heuristic. </p>
<p> Most likely this is not the end.</p>
<dt><code>&#8211;sid=&lt;ID|auto|no&gt;</code></p>
<dd>Display the subtitle stream specified by <code>&lt;ID&gt;</code>. <code>auto</code> selects the default, <code>no</code> disables subtitles. </p>
<p> <code>&#8211;sub</code> is an alias for <code>&#8211;sid</code>. </p>
<p> <code>&#8211;sid=no</code> or <code>&#8211;sub=no</code> or <code>&#8211;no-sub</code> disables subtitle decoding. (The latter variant does not work with the client API.)</p>
<dt><code>&#8211;vid=&lt;ID|auto|no&gt;</code></p>
<dd>Select video channel. <code>auto</code> selects the default, <code>no</code> disables video. </p>
<p> <code>&#8211;video</code> is an alias for <code>&#8211;vid</code>. </p>
<p> <code>&#8211;vid=no</code> or <code>&#8211;video=no</code> or <code>&#8211;no-video</code> disables video playback. (The latter variant does not work with the client API.) </p>
<p> If video is disabled, mpv will try to download the audio only if media is streamed with youtube-dl, because it saves bandwidth. This is done by setting the ytdl_format to &quot;bestaudio/best&quot; in the ytdl_hook.lua script.</p>
<dt><code>&#8211;edition=&lt;ID|auto&gt;</code></p>
<dd>(Matroska files only) Specify the edition (set of chapters) to use, where 0 is the first. If set to <code>auto</code> (the default), mpv will choose the first edition declared as a default, or if there is no default, the first edition defined.</p>
<dt><code>&#8211;track-auto-selection=&lt;yes|no&gt;</code></p>
<dd>Enable the default track auto-selection (default: yes). Enabling this will make the player select streams according to <code>&#8211;aid</code>, <code>&#8211;alang</code>, and others. If it is disabled, no tracks are selected. In addition, the player will not exit if no tracks are selected, and wait instead (this wait mode is similar to pausing, but the pause option is not set). </p>
<p> This is useful with <code>&#8211;lavfi-complex</code>: you can start playback in this mode, and then set select tracks at runtime by setting the filter graph. Note that if <code>&#8211;lavfi-complex</code> is set before playback is started, the referenced tracks are always selected.</p>
<dt><code>&#8211;subs-with-matching-audio=&lt;yes|no&gt;</code></p>
<dd>When autoselecting a subtitle track, select a non-forced one even if the selected audio stream matches your preferred subtitle language (default: yes). Disable this if you&#8217;d like to only show subtitles for foreign audio or onscreen text.</dl>
<h3>Playback Control</h3>
<dl COMPACT>
<dt><code>&#8211;start=&lt;relative time&gt;</code></p>
<dd>Seek to given time position. </p>
<p> The general format for times is <code>[+|-][[hh:]mm:]ss[.ms]</code>. If the time is prefixed with <code>&#8211;</code>, the time is considered relative from the end of the file (as signaled by the demuxer/the file). A <code>+</code> is usually ignored (but see below). </p>
<p> The following alternative time specifications are recognized: </p>
<p> <code>pp%</code> seeks to percent position pp (0-100). </p>
<p> <code>#c</code> seeks to chapter number c. (Chapters start from 1.) </p>
<p> <code>none</code> resets any previously set option (useful for libmpv). </p>
<p> If <code>&#8211;rebase-start-time=no</code> is given, then prefixing times with <code>+</code> makes the time relative to the start of the file. A timestamp without prefix is considered an absolute time, i.e. should seek to a frame with a timestamp as the file contains it. As a bug, but also a hidden feature, putting 1 or more spaces before the <code>+</code> or <code>&#8211;</code> always interprets the time as absolute, which can be used to seek to negative timestamps (useful for debugging at most).</p>
<dt>Examples</p>
<dd>
<dt><code>&#8211;start=+56</code>, <code>&#8211;start=00:56</code></p>
<dd>Seeks to the start time + 56 seconds.</p>
<dt><code>&#8211;start=-56</code>, <code>&#8211;start=-00:56</code></p>
<dd>Seeks to the end time &#8211; 56 seconds.</p>
<dt><code>&#8211;start=01:10:00</code></p>
<dd>Seeks to 1 hour 10 min.</p>
<dt><code>&#8211;start=50%</code></p>
<dd>Seeks to the middle of the file.</p>
<dt><code>&#8211;start=30 &#8211;end=40</code></p>
<dd>Seeks to 30 seconds, plays 10 seconds, and exits.</p>
<dt><code>&#8211;start=-3:20 &#8211;length=10</code></p>
<dd>Seeks to 3 minutes and 20 seconds before the end of the file, plays 10 seconds, and exits.</p>
<dt><code>&#8211;start=&#8217;#2&#8242; &#8211;end=&#8217;#4&#8242;</code></p>
<dd>Plays chapters 2 and 3, and exits.</p>
<dt><code>&#8211;end=&lt;relative time&gt;</code></p>
<dd>Stop at given time. Use <code>&#8211;length</code> if the time should be relative to <code>&#8211;start</code>. See <code>&#8211;start</code> for valid option values and examples.</p>
<dt><code>&#8211;length=&lt;relative time&gt;</code></p>
<dd>Stop after a given time relative to the start time. See <code>&#8211;start</code> for valid option values and examples. </p>
<p> If both <code>&#8211;end</code> and <code>&#8211;length</code> are provided, playback will stop when it reaches either of the two endpoints. </p>
<p> Obscurity note: this does not work correctly if <code>&#8211;rebase-start-time=no</code>, and the specified time is not an &quot;absolute&quot; time, as defined in the <code>&#8211;start</code> option description.</p>
<dt><code>&#8211;rebase-start-time=&lt;yes|no&gt;</code></p>
<dd>Whether to move the file start time to <code>00:00:00</code> (default: yes). This is less awkward for files which start at a random timestamp, such as transport streams. On the other hand, if there are timestamp resets, the resulting behavior can be rather weird. For this reason, and in case you are actually interested in the real timestamps, this behavior can be disabled with <code>no</code>.</p>
<dt><code>&#8211;speed=&lt;0.01-100&gt;</code></p>
<dd>Slow down or speed up playback by the factor given as parameter. </p>
<p> If <code>&#8211;audio-pitch-correction</code> (on by default) is used, playing with a speed higher than normal automatically inserts the <code>scaletempo2</code> audio filter.</p>
<dt><code>&#8211;pause</code></p>
<dd>Start the player in paused state.</p>
<dt><code>&#8211;shuffle</code></p>
<dd>Play files in random order.</p>
<dt><code>&#8211;playlist-start=&lt;auto|index&gt;</code></p>
<dd>Set which file on the internal playlist to start playback with. The index is an integer, with 0 meaning the first file. The value <code>auto</code> means that the selection of the entry to play is left to the playback resume mechanism (default). If an entry with the given index doesn&#8217;t exist, the behavior is unspecified and might change in future mpv versions. The same applies if the playlist contains further playlists (don&#8217;t expect any reasonable behavior). Passing a playlist file to mpv should work with this option, though. E.g. <code>mpv playlist.m3u &#8211;playlist-start=123</code> will work as expected, as long as <code>playlist.m3u</code> does not link to further playlists. </p>
<p> The value <code>no</code> is a deprecated alias for <code>auto</code>.</p>
<dt><code>&#8211;playlist=&lt;filename&gt;</code></p>
<dd>Play files according to a playlist file. Supports some common formats. If no format is detected, it will be treated as list of files, separated by newline characters. You may need this option to load plaintext files as a playlist. Note that XML playlist formats are not supported. </p>
<p> This option forces <code>&#8211;demuxer=playlist</code> to interpret the playlist file. Some playlist formats, notably CUE and optical disc formats, need to use different demuxers and will not work with this option. They still can be played directly, without using this option. </p>
<p> You can play playlists directly, without this option. Before mpv version 0.31.0, this option disabled any security mechanisms that might be in place, but since 0.31.0 it uses the same security mechanisms as playing a playlist file directly. If you trust the playlist file, you can disable any security checks with <code>&#8211;load-unsafe-playlists</code>. Because playlists can load other playlist entries, consider applying this option only to the playlist itself and not its entries, using something along these lines: <code>mpv &#8211;{ &#8211;playlist=filename &#8211;load-unsafe-playlists &#8211;}</code> </p>
<p> <code>WARNING:</code> The way older versions of mpv played playlist files via <code>&#8211;playlist</code> was not safe against maliciously constructed files. Such files may trigger harmful actions. This has been the case for all verions of mpv prior to 0.31.0, and all MPlayer versions, but unfortunately this fact was not well documented earlier, and some people have even misguidedly recommended the use of <code>&#8211;playlist</code> with untrusted sources. Do NOT use <code>&#8211;playlist</code> with random internet sources or files you do not trust if you are not sure your mpv is at least 0.31.0. </p>
<p> In particular, playlists can contain entries using protocols other than local files, such as special protocols like <code>avdevice://</code> (which are inherently unsafe).</p>
<dt><code>&#8211;chapter-merge-threshold=&lt;number&gt;</code></p>
<dd>Threshold for merging almost consecutive ordered chapter parts in milliseconds (default: 100). Some Matroska files with ordered chapters have inaccurate chapter end timestamps, causing a small gap between the end of one chapter and the start of the next one when they should match. If the end of one playback part is less than the given threshold away from the start of the next one then keep playing video normally over the chapter change instead of doing a seek.</p>
<dt><code>&#8211;chapter-seek-threshold=&lt;seconds&gt;</code></p>
<dd>Distance in seconds from the beginning of a chapter within which a backward chapter seek will go to the previous chapter (default: 5.0). Past this threshold, a backward chapter seek will go to the beginning of the current chapter instead. A negative value means always go back to the previous chapter.</p>
<dt><code>&#8211;hr-seek=&lt;no|absolute|yes|default&gt;</code></p>
<dd>Select when to use precise seeks that are not limited to keyframes. Such seeks require decoding video from the previous keyframe up to the target position and so can take some time depending on decoding performance. For some video formats, precise seeks are disabled. This option selects the default choice to use for seeks; it is possible to explicitly override that default in the definition of key bindings and in input commands.</p>
<dt><code>no</code></p>
<dd>Never use precise seeks.</p>
<dt><code>absolute</code></p>
<dd>Use precise seeks if the seek is to an absolute position in the file, such as a chapter seek, but not for relative seeks like the default behavior of arrow keys (default).</p>
<dt><code>default</code></p>
<dd>Like <code>absolute</code>, but enable hr-seeks in audio-only cases. The exact behavior is implementation specific and may change with new releases.</p>
<dt><code>yes</code></p>
<dd>Use precise seeks whenever possible.</p>
<dt><code>always</code></p>
<dd>Same as <code>yes</code> (for compatibility).</p>
<dt><code>&#8211;hr-seek-demuxer-offset=&lt;seconds&gt;</code></p>
<dd>This option exists to work around failures to do precise seeks (as in <code>&#8211;hr-seek</code>) caused by bugs or limitations in the demuxers for some file formats. Some demuxers fail to seek to a keyframe before the given target position, going to a later position instead. The value of this option is subtracted from the time stamp given to the demuxer. Thus, if you set this option to 1.5 and try to do a precise seek to 60 seconds, the demuxer is told to seek to time 58.5, which hopefully reduces the chance that it erroneously goes to some time later than 60 seconds. The downside of setting this option is that precise seeks become slower, as video between the earlier demuxer position and the real target may be unnecessarily decoded.</p>
<dt><code>&#8211;hr-seek-framedrop=&lt;yes|no&gt;</code></p>
<dd>Allow the video decoder to drop frames during seek, if these frames are before the seek target. If this is enabled, precise seeking can be faster, but if you&#8217;re using video filters which modify timestamps or add new frames, it can lead to precise seeking skipping the target frame. This e.g. can break frame backstepping when deinterlacing is enabled. </p>
<p> Default: <code>yes</code></p>
<dt><code>&#8211;index=&lt;mode&gt;</code></p>
<dd>Controls how to seek in files. Note that if the index is missing from a file, it will be built on the fly by default, so you don&#8217;t need to change this. But it might help with some broken files.</p>
<dt><code>default</code></p>
<dd>use an index if the file has one, or build it if missing</p>
<dt><code>recreate</code></p>
<dd>don&#8217;t read or use the file&#8217;s index </p>
<p> <code>NOTE:</code> This option only works if the underlying media supports seeking (i.e. not with stdin, pipe, etc).</p>
<dt><code>&#8211;load-unsafe-playlists</code></p>
<dd>Load URLs from playlists which are considered unsafe (default: no). This includes special protocols and anything that doesn&#8217;t refer to normal files. Local files and HTTP links on the other hand are always considered safe. </p>
<p> In addition, if a playlist is loaded while this is set, the added playlist entries are not marked as originating from network or potentially unsafe location. (Instead, the behavior is as if the playlist entries were provided directly to mpv command line or <code>loadfile</code> command.)</p>
<dt><code>&#8211;access-references=&lt;yes|no&gt;</code></p>
<dd>Follow any references in the file being opened (default: yes). Disabling this is helpful if the file is automatically scanned (e.g. thumbnail generation). If the thumbnail scanner for example encounters a playlist file, which contains network URLs, and the scanner should not open these, enabling this option will prevent it. This option also disables ordered chapters, mov reference files, opening of archives, and a number of other features. </p>
<p> On older FFmpeg versions, this will not work in some cases. Some FFmpeg demuxers might not respect this option. </p>
<p> This option does not prevent opening of paired subtitle files and such. Use <code>&#8211;autoload-files=no</code> to prevent this. </p>
<p> This option does not always work if you open non-files (for example using <code><a href="dvd://directory">dvd://directory</a></code> would open a whole bunch of files in the given directory). Prefixing the filename with <code>./</code> if it doesn&#8217;t start with a <code>/</code> will avoid this.</p>
<dt><code>&#8211;loop-playlist=&lt;N|inf|force|no&gt;</code>, <code>&#8211;loop-playlist</code></p>
<dd>Loops playback <code>N</code> times. A value of <code>1</code> plays it one time (default), <code>2</code> two times, etc. <code>inf</code> means forever. <code>no</code> is the same as <code>1</code> and disables looping. If several files are specified on command line, the entire playlist is looped. <code>&#8211;loop-playlist</code> is the same as <code>&#8211;loop-playlist=inf</code>. </p>
<p> The <code>force</code> mode is like <code>inf</code>, but does not skip playlist entries which have been marked as failing. This means the player might waste CPU time trying to loop a file that doesn&#8217;t exist. But it might be useful for playing webradios under very bad network conditions.</p>
<dt><code>&#8211;loop-file=&lt;N|inf|no&gt;</code>, <code>&#8211;loop=&lt;N|inf|no&gt;</code></p>
<dd>Loop a single file N times. <code>inf</code> means forever, <code>no</code> means normal playback. For compatibility, <code>&#8211;loop-file</code> and <code>&#8211;loop-file=yes</code> are also accepted, and are the same as <code>&#8211;loop-file=inf</code>. </p>
<p> The difference to <code>&#8211;loop-playlist</code> is that this doesn&#8217;t loop the playlist, just the file itself. If the playlist contains only a single file, the difference between the two option is that this option performs a seek on loop, instead of reloading the file. </p>
<p> <code>NOTE:</code> <code>&#8211;loop-file</code> counts the number of times it causes the player to seek to the beginning of the file, not the number of full playthroughs. This means <code>&#8211;loop-file=1</code> will end up playing the file twice. Contrast with <code>&#8211;loop-playlist</code>, which counts the number of full playthroughs. </p>
<p> <code>&#8211;loop</code> is an alias for this option.</p>
<dt><code>&#8211;ab-loop-a=&lt;time&gt;</code>, <code>&#8211;ab-loop-b=&lt;time&gt;</code></p>
<dd>Set loop points. If playback passes the <code>b</code> timestamp, it will seek to the <code>a</code> timestamp. Seeking past the <code>b</code> point doesn&#8217;t loop (this is intentional). </p>
<p> If <code>a</code> is after <code>b</code>, the behavior is as if the points were given in the right order, and the player will seek to <code>b</code> after crossing through <code>a</code>. This is different from old behavior, where looping was disabled (and as a bug, looped back to <code>a</code> on the end of the file). </p>
<p> If either options are set to <code>no</code> (or unset), looping is disabled. This is different from old behavior, where an unset <code>a</code> implied the start of the file, and an unset <code>b</code> the end of the file. </p>
<p> The loop-points can be adjusted at runtime with the corresponding properties. See also <code>ab-loop</code> command.</p>
<dt><code>&#8211;ab-loop-count=&lt;N|inf&gt;</code></p>
<dd>Run A-B loops only N times, then ignore the A-B loop points (default: inf). Every finished loop iteration will decrement this option by 1 (unless it is set to <code>inf</code> or 0). <code>inf</code> means that looping goes on forever. If this option is set to 0, A-B looping is ignored, and even the <code>ab-loop</code> command will not enable looping again (the command will show <code>(disabled)</code> on the OSD message if both loop points are set, but <code>ab-loop-count</code> is 0).</p>
<dt><code>&#8211;ordered-chapters</code>, <code>&#8211;no-ordered-chapters</code></p>
<dd>Enabled by default. Disable support for Matroska ordered chapters. mpv will not load or search for video segments from other files, and will also ignore any chapter order specified for the main file.</p>
<dt><code>&#8211;ordered-chapters-files=&lt;playlist-file&gt;</code></p>
<dd>Loads the given file as playlist, and tries to use the files contained in it as reference files when opening a Matroska file that uses ordered chapters. This overrides the normal mechanism for loading referenced files by scanning the same directory the main file is located in. </p>
<p> Useful for loading ordered chapter files that are not located on the local filesystem, or if the referenced files are in different directories. </p>
<p> Note: a playlist can be as simple as a text file containing filenames separated by newlines.</p>
<dt><code>&#8211;chapters-file=&lt;filename&gt;</code></p>
<dd>Load chapters from this file, instead of using the chapter metadata found in the main file. </p>
<p> This accepts a media file (like mkv) or even a pseudo-format like ffmetadata and uses its chapters to replace the current file&#8217;s chapters. This doesn&#8217;t work with OGM or XML chapters directly.</p>
<dt><code>&#8211;sstep=&lt;sec&gt;</code></p>
<dd>Skip &lt;sec&gt; seconds after every frame. </p>
<p> <code>NOTE:</code> Without <code>&#8211;hr-seek</code>, skipping will snap to keyframes.</p>
<dt><code>&#8211;stop-playback-on-init-failure=&lt;yes|no&gt;</code></p>
<dd>Stop playback if either audio or video fails to initialize (default: no). With <code>no</code>, playback will continue in video-only or audio-only mode if one of them fails. This doesn&#8217;t affect playback of audio-only or video-only files.</p>
<dt><code>&#8211;play-dir=&lt;forward|+|backward|-&gt;</code></p>
<dd>Control the playback direction (default: forward). Setting <code>backward</code> will attempt to play the file in reverse direction, with decreasing playback time. If this is set on playback starts, playback will start from the end of the file. If this is changed at during playback, a hr-seek will be issued to change the direction. </p>
<p> <code>+</code> and <code>&#8211;</code> are aliases for <code>forward</code> and <code>backward</code>. </p>
<p> The rest of this option description pertains to the <code>backward</code> mode. </p>
<p> <code>NOTE:</code> Backward playback is extremely fragile. It may not always work, is much slower than forward playback, and breaks certain other features. How well it works depends mainly on the file being played. Generally, it will show good results (or results at all) only if the stars align. </p>
<p> mpv, as well as most media formats, were designed for forward playback only. Backward playback is bolted on top of mpv, and tries to make a medium effort to make backward playback work. Depending on your use-case, another tool may work much better. </p>
<p> Backward playback is not exactly a 1st class feature. Implementation tradeoffs were made, that are bad for backward playback, but in turn do not cause disadvantages for normal playback. Various possible optimizations are not implemented in order to keep the complexity down. Normally, a media player is highly pipelined (future data is prepared in separate threads, so it is available in realtime when the next stage needs it), but backward playback will essentially stall the pipeline at various random points. </p>
<p> For example, for intra-only codecs are trivially backward playable, and tools built around them may make efficient use of them (consider video editors or camera viewers). mpv won&#8217;t be efficient in this case, because it uses its generic backward playback algorithm, that on top of it is not very optimized. </p>
<p> If you just want to quickly go backward through the video and just show &quot;keyframes&quot;, just use forward playback, and hold down the left cursor key (which on CLI with default config sends many small relative seek commands). </p>
<p> The implementation consists of mostly 3 parts:</p>
<dt>&bull;</p>
<dd>Backward demuxing. This relies on the demuxer cache, so the demuxer cache should (or must, didn&#8217;t test it) be enabled, and its size will affect performance. If the cache is too small or too large, quadratic runtime behavior may result.</p>
<dt>&bull;</p>
<dd>Backward decoding. The decoder library used (libavcodec) does not support this. It is emulated by feeding bits of data in forward, putting the result in a queue, returning the queue data to the VO in reverse, and then starting over at an earlier position. This can require buffering an extreme amount of decoded data, and also completely breaks pipelining.</p>
<dt>&bull;</p>
<dd>Backward output. This is relatively simple, because the decoder returns the frames in the needed order. However, this may cause various problems because filters see audio and video going backward. </p>
<p> Known problems:</p>
<dt>&bull;</p>
<dd>It&#8217;s fragile. If anything doesn&#8217;t work, random non-useful behavior may occur. In simple cases, the player will just play nonsense and artifacts. In other cases, it may get stuck or heat the CPU. (Exceeding memory usage significantly beyond the user-set limits would be a bug, though.)</p>
<dt>&bull;</p>
<dd>Performance and resource usage isn&#8217;t good. In part this is inherent to backward playback of normal media formats, and in parts due to implementation choices and tradeoffs.</p>
<dt>&bull;</p>
<dd>This is extremely reliant on good demuxer behavior. Although backward demuxing requires no special demuxer support, it is required that the demuxer performs seeks reliably, fulfills some specific requirements about packet metadata, and has deterministic behavior.</p>
<dt>&bull;</p>
<dd>Starting playback exactly from the end may or may not work, depending on seeking behavior and file duration detection.</p>
<dt>&bull;</p>
<dd>Some container formats, audio, and video codecs are not supported due to their behavior. There is no list, and the player usually does not detect them. Certain live streams (including TV captures) may exhibit problems in particular, as well as some lossy audio codecs. h264 intra-refresh is known not to work due to problems with libavcodec. WAV and some other raw audio formats tend to have problems &#8211; there are hacks for dealing with them, which may or may not work.</p>
<dt>&bull;</p>
<dd>Backward demuxing of subtitles is not supported. Subtitle display still works for some external text subtitle formats. (These are fully read into memory, and only backward display is needed.) Text subtitles that are cached in the subtitle renderer also have a chance to be displayed correctly.</p>
<dt>&bull;</p>
<dd>Some features dealing with playback of broken or hard to deal with files will not work fully (such as timestamp correction).</p>
<dt>&bull;</p>
<dd>If demuxer low level seeks (i.e. seeking the actual demuxer instead of just within the demuxer cache) are performed by backward playback, the created seek ranges may not join, because not enough overlap is achieved.</p>
<dt>&bull;</p>
<dd>Trying to use this with hardware video decoding will probably exhaust all your GPU memory and then crash a thing or two. Or it will fail because <code>&#8211;hwdec-extra-frames</code> will certainly be set too low.</p>
<dt>&bull;</p>
<dd>Stream recording is broken. <code>&#8211;stream-record</code> may keep working if you backward play within a cached region only.</p>
<dt>&bull;</p>
<dd>Relative seeks may behave weird. Small seeks backward (towards smaller time, i.e. <code>seek -1</code>) may not really seek properly, and audio will remain muted for a while. Using hr-seek is recommended, which should have none of these problems.</p>
<dt>&bull;</p>
<dd>Some things are just weird. For example, while seek commands manipulate playback time in the expected way (provided they work correctly), the framestep commands are transposed. Backstepping will perform very expensive work to step forward by 1 frame. </p>
<p> Tuning:</p>
<dt>&bull;</p>
<dd>Remove all <code>&#8211;vf</code>/<code>&#8211;af</code> filters you have set. Disable hardware decoding. Disable idiotic nonsense like SPDIF passthrough.</p>
<dt>&bull;</p>
<dd>Increasing <code>&#8211;video-reversal-buffer</code> might help if reversal queue overflow is reported, which may happen in high bitrate video, or video with large GOP. Hardware decoding mostly ignores this, and you need to increase <code>&#8211;hwdec-extra-frames</code> instead (until you get playback without logged errors).</p>
<dt>&bull;</p>
<dd>The demuxer cache is essential for backward demuxing. Make sure to set <code>&#8211;cache=yes</code>. The cache size might matter. If it&#8217;s too small, a queue overflow will be logged, and backward playback cannot continue, or it performs too many low level seeks. If it&#8217;s too large, implementation tradeoffs may cause general performance issues. Use <code>&#8211;demuxer-max-bytes</code> to potentially increase the amount of packets the demuxer layer can queue for reverse demuxing (basically it&#8217;s the <code>&#8211;video-reversal-buffer</code> equivalent for the demuxer layer).</p>
<dt>&bull;</p>
<dd>Setting <code>&#8211;vd-queue-enable=yes</code> can help a lot to make playback smooth (once it works).</p>
<dt>&bull;</p>
<dd><code>&#8211;demuxer-backward-playback-step</code> also factors into how many seeks may be performed, and whether backward demuxing could break due to queue overflow. If it&#8217;s set too high, the backstep operation needs to search through more packets all the time, even if the cache is large enough.</p>
<dt>&bull;</p>
<dd>Setting <code>&#8211;demuxer-cache-wait</code> may be useful to cache the entire file into the demuxer cache. Set <code>&#8211;demuxer-max-bytes</code> to a large size to make sure it can read the entire cache; <code>&#8211;demuxer-max-back-bytes</code> should also be set to a large size to prevent that tries to trim the cache.</p>
<dt>&bull;</p>
<dd>If audio artifacts are audible, even though the AO does not underrun, increasing <code>&#8211;audio-backward-overlap</code> might help in some cases.</p>
<dt><code>&#8211;video-reversal-buffer=&lt;bytesize&gt;</code>, <code>&#8211;audio-reversal-buffer=&lt;bytesize&gt;</code></p>
<dd>For backward decoding. Backward decoding decodes forward in steps, and then reverses the decoder output. These options control the approximate maximum amount of bytes that can be buffered. The main use of this is to avoid unbounded resource usage; during normal backward playback, it&#8217;s not supposed to hit the limit, and if it does, it will drop frames and complain about it. </p>
<p> Use this option if you get reversal queue overflow errors during backward playback. Increase the size until the warning disappears. Usually, the video buffer will overflow first, especially if it&#8217;s high resolution video. </p>
<p> This does not work correctly if video hardware decoding is used. The video frame size will not include the referenced GPU and driver memory. Some hardware decoders may also be limited by <code>&#8211;hwdec-extra-frames</code>. </p>
<p> How large the queue size needs to be depends entirely on the way the media was encoded. Audio typically requires a very small buffer, while video can require excessively large buffers. </p>
<p> (Technically, this allows the last frame to exceed the limit. Also, this does not account for other buffered frames, such as inside the decoder or the video output.) </p>
<p> This does not affect demuxer cache behavior at all. </p>
<p> See <code>&#8211;list-options</code> for defaults and value range. <code>&lt;bytesize&gt;</code> options accept suffixes such as <code>KiB</code> and <code>MiB</code>.</p>
<dt><code>&#8211;video-backward-overlap=&lt;auto|number&gt;</code>, <code>&#8211;audio-backward-overlap=&lt;auto|number&gt;</code></p>
<dd>Number of overlapping keyframe ranges to use for backward decoding (default: auto) (&quot;keyframe&quot; to be understood as in the mpv/ffmpeg specific meaning). Backward decoding works by forward decoding in small steps. Some codecs cannot restart decoding from any packet (even if it&#8217;s marked as seek point), which becomes noticeable with backward decoding (in theory this is a problem with seeking too, but <code>&#8211;hr-seek-demuxer-offset</code> can fix it for seeking). In particular, MDCT based audio codecs are affected. </p>
<p> The solution is to feed a previous packet to the decoder each time, and then discard the output. This option controls how many packets to feed. The <code>auto</code> choice is currently hardcoded to 0 for video, and uses 1 for lossy audio, 0 for lossless audio. For some specific lossy audio codecs, this is set to 2. </p>
<p> <code>&#8211;video-backward-overlap</code> can potentially handle intra-refresh video, depending on the exact conditions. You may have to use the <code>&#8211;vd-lavc-show-all</code> option as well.</p>
<dt><code>&#8211;video-backward-batch=&lt;number&gt;</code>, <code>&#8211;audio-backward-batch=&lt;number&gt;</code></p>
<dd>Number of keyframe ranges to decode at once when backward decoding (default: 1 for video, 10 for audio). Another pointless tuning parameter nobody should use. This should affect performance only. In theory, setting a number higher than 1 for audio will reduce overhead due to less frequent backstep operations and less redundant decoding work due to fewer decoded overlap frames (see <code>&#8211;audio-backward-overlap</code>). On the other hand, it requires a larger reversal buffer, and could make playback less smooth due to breaking pipelining (e.g. by decoding a lot, and then doing nothing for a while). </p>
<p> It probably never makes sense to set <code>&#8211;video-backward-batch</code>. But in theory, it could help with intra-only video codecs by reducing backstep operations.</p>
<dt><code>&#8211;demuxer-backward-playback-step=&lt;seconds&gt;</code></p>
<dd>Number of seconds the demuxer should seek back to get new packets during backward playback (default: 60). This is useful for tuning backward playback, see <code>&#8211;play-dir</code> for details. </p>
<p> Setting this to a very low value or 0 may make the player think seeking is broken, or may make it perform multiple seeks. </p>
<p> Setting this to a high value may lead to quadratic runtime behavior.</dl>
<h3>Program Behavior</h3>
<dl COMPACT>
<dt><code>&#8211;help</code>, <code>&#8211;h</code></p>
<dd>Show short summary of options. </p>
<p> You can also pass a string to this option, which will list all top-level options which contain the string in the name, e.g. <code>&#8211;h=scale</code> for all options that contain the word <code>scale</code>. The special string <code>*</code> lists all top-level options.</p>
<dt><code>-v</code></p>
<dd>Increment verbosity level, one level for each <code>-v</code> found on the command line.</p>
<dt><code>&#8211;version, -V</code></p>
<dd>Print version string and exit.</p>
<dt><code>&#8211;no-config</code></p>
<dd>Do not load default configuration files. This prevents loading of both the user-level and system-wide <code>mpv.conf</code> and <code>input.conf</code> files. Other configuration files are blocked as well, such as resume playback files. </p>
<p> <code>NOTE:</code> Files explicitly requested by command line options, like <code>&#8211;include</code> or <code>&#8211;use-filedir-conf</code>, will still be loaded. </p>
<p> See also: <code>&#8211;config-dir</code>.</p>
<dt><code>&#8211;list-options</code></p>
<dd>Prints all available options.</p>
<dt><code>&#8211;list-properties</code></p>
<dd>Print a list of the available properties.</p>
<dt><code>&#8211;list-protocols</code></p>
<dd>Print a list of the supported protocols.</p>
<dt><code>&#8211;log-file=&lt;path&gt;</code></p>
<dd>Opens the given path for writing, and print log messages to it. Existing files will be truncated. The log level is at least <code>-v -v</code>, but can be raised via <code>&#8211;msg-level</code> (the option cannot lower it below the forced minimum log level). </p>
<p> A special case is the macOS bundle, it will create a log file at <code>~/Library/Logs/mpv.log</code> by default.</p>
<dt><code>&#8211;config-dir=&lt;path&gt;</code></p>
<dd>Force a different configuration directory. If this is set, the given directory is used to load configuration files, and all other configuration directories are ignored. This means the global mpv configuration directory as well as per-user directories are ignored, and overrides through environment variables (<code>MPV_HOME</code>) are also ignored. </p>
<p> Note that the <code>&#8211;no-config</code> option takes precedence over this option.</p>
<dt><code>&#8211;save-position-on-quit</code></p>
<dd>Always save the current playback position on quit. When this file is played again later, the player will seek to the old playback position on start. This does not happen if playback of a file is stopped in any other way than quitting. For example, going to the next file in the playlist will not save the position, and start playback at beginning the next time the file is played. </p>
<p> This behavior is disabled by default, but is always available when quitting the player with Shift+Q.</p>
<dt><code>&#8211;watch-later-directory=&lt;path&gt;</code></p>
<dd>The directory in which to store the &quot;watch later&quot; temporary files. </p>
<p> The default is a subdirectory named &quot;watch_later&quot; underneath the config directory (usually <code>~/.config/mpv/</code>).</p>
<dt><code>&#8211;dump-stats=&lt;filename&gt;</code></p>
<dd>Write certain statistics to the given file. The file is truncated on opening. The file will contain raw samples, each with a timestamp. To make this file into a readable, the script <code>TOOLS/stats-conv.py</code> can be used (which currently displays it as a graph). </p>
<p> This option is useful for debugging only.</p>
<dt><code>&#8211;idle=&lt;no|yes|once&gt;</code></p>
<dd>Makes mpv wait idly instead of quitting when there is no file to play. Mostly useful in input mode, where mpv can be controlled through input commands. (Default: <code>no</code>) </p>
<p> <code>once</code> will only idle at start and let the player close once the first playlist has finished playing back.</p>
<dt><code>&#8211;include=&lt;configuration-file&gt;</code></p>
<dd>Specify configuration file to be parsed after the default ones.</p>
<dt><code>&#8211;load-scripts=&lt;yes|no&gt;</code></p>
<dd>If set to <code>no</code>, don&#8217;t auto-load scripts from the <code>scripts</code> configuration subdirectory (usually <code>~/.config/mpv/scripts/</code>). (Default: <code>yes</code>)</p>
<dt><code>&#8211;script=&lt;filename&gt;</code>, <code>&#8211;scripts=file1.lua:file2.lua:&#8230;</code></p>
<dd>Load a Lua script. The second option allows you to load multiple scripts by separating them with the path separator (<code>:</code> on Unix, <code>;</code> on Windows). </p>
<p> <code>&#8211;scripts</code> is a path list option. See <i>List Options</i> for details.</p>
<dt><code>&#8211;script-opts=key1=value1,key2=value2,&#8230;</code></p>
<dd>Set options for scripts. A script can query an option by key. If an option is used and what semantics the option value has depends entirely on the loaded scripts. Values not claimed by any scripts are ignored. </p>
<p> This is a key/value list option. See <i>List Options</i> for details.</p>
<dt><code>&#8211;merge-files</code></p>
<dd>Pretend that all files passed to mpv are concatenated into a single, big file. This uses timeline/EDL support internally.</p>
<dt><code>&#8211;no-resume-playback</code></p>
<dd>Do not restore playback position from the <code>watch_later</code> configuration subdirectory (usually <code>~/.config/mpv/watch_later/</code>). See <code>quit-watch-later</code> input command.</p>
<dt><code>&#8211;resume-playback-check-mtime</code></p>
<dd>Only restore the playback position from the <code>watch_later</code> configuration subdirectory (usually <code>~/.config/mpv/watch_later/</code>) if the file&#8217;s modification time is the same as at the time of saving. This may prevent skipping forward in files with the same name which have different content. (Default: <code>no</code>)</p>
<dt><code>&#8211;profile=&lt;profile1,profile2,&#8230;&gt;</code></p>
<dd>Use the given profile(s), <code>&#8211;profile=help</code> displays a list of the defined profiles.</p>
<dt><code>&#8211;reset-on-next-file=&lt;all|option1,option2,&#8230;&gt;</code></p>
<dd>Normally, mpv will try to keep all settings when playing the next file on the playlist, even if they were changed by the user during playback. (This behavior is the opposite of MPlayer&#8217;s, which tries to reset all settings when starting next file.) </p>
<p> Default: Do not reset anything. </p>
<p> This can be changed with this option. It accepts a list of options, and mpv will reset the value of these options on playback start to the initial value. The initial value is either the default value, or as set by the config file or command line. </p>
<p> In some cases, this might not work as expected. For example, <code>&#8211;volume</code> will only be reset if it is explicitly set in the config file or the command line. </p>
<p> The special name <code>all</code> resets as many options as possible. </p>
<p> This is a string list option. See <i>List Options</i> for details.</p>
<dt>Examples</p>
<dd>
<dt>&bull;</p>
<dd><code>&#8211;reset-on-next-file=pause</code> Reset pause mode when switching to the next file.</p>
<dt>&bull;</p>
<dd><code>&#8211;reset-on-next-file=fullscreen,speed</code> Reset fullscreen and playback speed settings if they were changed during playback.</p>
<dt>&bull;</p>
<dd><code>&#8211;reset-on-next-file=all</code> Try to reset all settings that were changed during playback.</p>
<dt><code>&#8211;watch-later-options=option1,option2,&#8230;</code></p>
<dd>The options that are saved in &quot;watch later&quot; files if they have been changed since when mpv started. These values will be restored the next time the files are played. The playback position is always saved as <code>start</code>, so adding <code>start</code> to this list has no effect. </p>
<p> When removing options, existing watch later data won&#8217;t be modified and will still be applied fully, but new watch later data won&#8217;t contain these options. </p>
<p> This is a string list option. See <i>List Options</i> for details.</p>
<dt>Examples</p>
<dd>
<dt>&bull;</p>
<dd><code>&#8211;watch-later-options-remove=fullscreen</code> The fullscreen state won&#8217;t be saved to watch later files.</p>
<dt>&bull;</p>
<dd><code>&#8211;watch-later-options-remove=volume</code> <code>&#8211;watch-later-options-remove=mute</code> The volume and mute state won&#8217;t be saved to watch later files.</p>
<dt>&bull;</p>
<dd><code>&#8211;watch-later-options-clr</code> No option will be saved to watch later files except the starting position.</p>
<dt><code>&#8211;write-filename-in-watch-later-config</code></p>
<dd>Prepend the watch later config files with the name of the file they refer to. This is simply written as comment on the top of the file. </p>
<p> <code>WARNING:</code> This option may expose privacy-sensitive information and is thus disabled by default.</p>
<dt><code>&#8211;ignore-path-in-watch-later-config</code></p>
<dd>Ignore path (i.e. use filename only) when using watch later feature. (Default: disabled)</p>
<dt><code>&#8211;show-profile=&lt;profile&gt;</code></p>
<dd>Show the description and content of a profile. Lists all profiles if no parameter is provided.</p>
<dt><code>&#8211;use-filedir-conf</code></p>
<dd>Look for a file-specific configuration file in the same directory as the file that is being played. See <i>File-specific Configuration Files</i>. </p>
<p> <code>WARNING:</code> May be dangerous if playing from untrusted media.</p>
<dt><code>&#8211;ytdl</code>, <code>&#8211;no-ytdl</code></p>
<dd>Enable the youtube-dl hook-script. It will look at the input URL, and will play the video located on the website. This works with many streaming sites, not just the one that the script is named after. This requires a recent version of youtube-dl to be installed on the system. (Enabled by default.) </p>
<p> If the script can&#8217;t do anything with an URL, it will do nothing. </p>
<p> This accepts a set of options, which can be passed to it with the <code>&#8211;script-opts</code> option (using <code>ytdl_hook-</code> as prefix):</p>
<dt><code>try_ytdl_first=&lt;yes|no&gt;</code></p>
<dd>If &#8216;yes&#8217; will try parsing the URL with youtube-dl first, instead of the default where it&#8217;s only after mpv failed to open it. This mostly depends on whether most of your URLs need youtube-dl parsing.</p>
<dt><code>exclude=&lt;URL1|URL2|&#8230;</code></p>
<dd>A <code>|</code>-separated list of URL patterns which mpv should not use with youtube-dl. The patterns are matched after the <code>http(s)://</code> part of the URL. </p>
<p> <code>^</code> matches the beginning of the URL, <code>$</code> matches its end, and you should use <code>%</code> before any of the characters <code>^$()%|,.[]*+-?</code> to match that character.</p>
<dt>Examples</p>
<dd>
<dt>&bull;</p>
<dd><code>&#8211;script-opts=ytdl_hook-exclude=&#8217;^youtube%.com&#8217;</code> will exclude any URL that starts with <code><a rel="nofollow" href="http://youtube.com">http://youtube.com</a></code> or <code><a rel="nofollow" href="https://youtube.com">https://youtube.com</a></code>.</p>
<dt>&bull;</p>
<dd><code>&#8211;script-opts=ytdl_hook-exclude=&#8217;%.mkv$|%.mp4$&#8217;</code> will exclude any URL that ends with <code>.mkv</code> or <code>.mp4</code>. </p>
<p> See more lua patterns here: <i><a rel="nofollow" href="https://www.lua.org/manual/5.1/manual.html#5.4.1">https://www.lua.org/manual/5.1/manual.html#5.4.1</a></i></p>
<dt><code>all_formats=&lt;yes|no&gt;</code></p>
<dd>If &#8216;yes&#8217; will attempt to add all formats found reported by youtube-dl (default: no). Each format is added as a separate track. In addition, they are delay-loaded, and actually opened only when a track is selected (this should keep load times as low as without this option). </p>
<p> It adds average bitrate metadata, if available, which means you can use <code>&#8211;hls-bitrate</code> to decide which track to select. (HLS used to be the only format whose alternative quality streams were exposed in a similar way, thus the option name.) </p>
<p> Tracks which represent formats that were selected by youtube-dl as default will have the default flag set. This means mpv should generally still select formats chosen with <code>&#8211;ytdl-format</code> by default. </p>
<p> Although this mechanism makes it possible to switch streams at runtime, it&#8217;s not suitable for this purpose for various technical reasons. (It&#8217;s slow, which can&#8217;t be really fixed.) In general, this option is not useful, and was only added to show that it&#8217;s possible. </p>
<p> There are two cases that must be considered when doing quality/bandwidth selection:</p>
<dt>1.</p>
<dd>Completely separate audio and video streams (DASH-like). Each of these streams contain either only audio or video, so you can mix and combine audio/video bandwidths without restriction. This intuitively matches best with the concept of selecting quality by track (what <code>all_formats</code> is supposed to do).</p>
<dt>2.</p>
<dd>Separate sets of muxed audio and video streams. Each version of the media contains both an audio and video stream, and they are interleaved. In order not to waste bandwidth, you should only select one of these versions (if, for example, you select an audio stream, then video will be downloaded, even if you selected video from a different stream). </p>
<p> mpv will still represent them as separate tracks, but will set the title of each track to <code>muxed-N</code>, where <code>N</code> is replaced with the youtube-dl format ID of the originating stream. </p>
<p> Some sites will mix 1. and 2., but we assume that they do so for compatibility reasons, and there is no reason to use them at all.</p>
<dt><code>force_all_formats=&lt;yes|no&gt;</code></p>
<dd>If set to &#8216;yes&#8217;, and <code>all_formats</code> is also set to &#8216;yes&#8217;, this will try to represent all youtube-dl reported formats as tracks, even if mpv would normally use the direct URL reported by it (default: yes). </p>
<p> It appears this normally makes a difference if youtube-dl works on a master HLS playlist. </p>
<p> If this is set to &#8216;no&#8217;, this specific kind of stream is treated like <code>all_formats</code> is set to &#8216;no&#8217;, and the stream selection as done by youtube-dl (via <code>&#8211;ytdl-format</code>) is used.</p>
<dt><code>use_manifests=&lt;yes|no&gt;</code></p>
<dd>Make mpv use the master manifest URL for formats like HLS and DASH, if available, allowing for video/audio selection in runtime (default: no). It&#8217;s disabled (&quot;no&quot;) by default for performance reasons.</p>
<dt><code>ytdl_path=youtube-dl</code></p>
<dd>Configure paths to youtube-dl&#8217;s executable or a compatible fork&#8217;s. The paths should be separated by : on Unix and ; on Windows. mpv looks in order for the configured paths in PATH and in mpv&#8217;s config directory. The defaults are &quot;yt-dlp&quot;, &quot;yt-dlp_x86&quot; and &quot;youtube-dl&quot;. On Windows the suffix extension &quot;.exe&quot; is always appended.</p>
<dt>Why do the option names mix <code>_</code> and <code>&#8211;</code>?</p>
<dd>I have no idea.</p>
<dt><code>&#8211;ytdl-format=&lt;ytdl|best|worst|mp4|webm|&#8230;&gt;</code></p>
<dd>Video format/quality that is directly passed to youtube-dl. The possible values are specific to the website and the video, for a given url the available formats can be found with the command <code>youtube-dl &#8211;list-formats URL</code>. See youtube-dl&#8217;s documentation for available aliases. (Default: <code>bestvideo+bestaudio/best</code>) </p>
<p> The <code>ytdl</code> value does not pass a <code>&#8211;format</code> option to youtube-dl at all, and thus does not override its default. Note that sometimes youtube-dl returns a format that mpv cannot use, and in these cases the mpv default may work better.</p>
<dt><code>&#8211;ytdl-raw-options=&lt;key&gt;=&lt;value&gt;[,&lt;key&gt;=&lt;value&gt;[,&#8230;]]</code></p>
<dd>Pass arbitrary options to youtube-dl. Parameter and argument should be passed as a key-value pair. Options without argument must include <code>=</code>. </p>
<p> There is no sanity checking so it&#8217;s possible to break things (i.e. passing invalid parameters to youtube-dl). </p>
<p> A proxy URL can be passed for youtube-dl to use it in parsing the website. This is useful for geo-restricted URLs. After youtube-dl parsing, some URLs also require a proxy for playback, so this can pass that proxy information to mpv. Take note that SOCKS proxies aren&#8217;t supported and https URLs also bypass the proxy. This is a limitation in FFmpeg. </p>
<p> This is a key/value list option. See <i>List Options</i> for details.</p>
<dt>Example</p>
<dd>
<dt>&bull;</p>
<dd><code>&#8211;ytdl-raw-options=username=user,password=pass</code></p>
<dt>&bull;</p>
<dd><code>&#8211;ytdl-raw-options=force-ipv6=</code></p>
<dt>&bull;</p>
<dd><code>&#8211;ytdl-raw-options=proxy=[<a rel="nofollow" href="http://127.0.0.1:3128]">http://127.0.0.1:3128]</a></code></p>
<dt>&bull;</p>
<dd><code>&#8211;ytdl-raw-options-append=proxy=<a rel="nofollow" href="http://127.0.0.1:3128">http://127.0.0.1:3128</a></code></p>
<dt><code>&#8211;load-stats-overlay=&lt;yes|no&gt;</code></p>
<dd>Enable the builtin script that shows useful playback information on a key binding (default: yes). By default, the <code>i</code> key is used (<code>I</code> to make the overlay permanent).</p>
<dt><code>&#8211;load-osd-console=&lt;yes|no&gt;</code></p>
<dd>Enable the builtin script that shows a console on a key binding and lets you enter commands (default: yes). By default,. The <code>&#8216;</code> key is used to show the console, and <code>ESC</code> to hide it again. (This is based on a user script called <code>repl.lua</code>.)</p>
<dt><code>&#8211;load-auto-profiles=&lt;yes|no|auto&gt;</code></p>
<dd>Enable the builtin script that does auto profiles (default: auto). See <i>Conditional auto profiles</i> for details. <code>auto</code> will load the script, but immediately unload it if there are no conditional profiles.</p>
<dt><code>&#8211;player-operation-mode=&lt;cplayer|pseudo-gui&gt;</code></p>
<dd>For enabling &quot;pseudo GUI mode&quot;, which means that the defaults for some options are changed. This option should not normally be used directly, but only by mpv internally, or mpv-provided scripts, config files, or .desktop files. See <i>PSEUDO GUI MODE</i> for details.</dl>
<h3>Video</h3>
<dl COMPACT>
<dt><code>&#8211;vo=&lt;driver&gt;</code></p>
<dd>Specify the video output backend to be used. See <i>VIDEO OUTPUT DRIVERS</i> for details and descriptions of available drivers.</p>
<dt><code>&#8211;vd=&lt;&#8230;&gt;</code></p>
<dd>Specify a priority list of video decoders to be used, according to their family and name. See <code>&#8211;ad</code> for further details. Both of these options use the same syntax and semantics; the only difference is that they operate on different codec lists. </p>
<p> <code>NOTE:</code> See <code>&#8211;vd=help</code> for a full list of available decoders.</p>
<dt><code>&#8211;vf=&lt;filter1[=parameter1:parameter2:&#8230;],filter2,&#8230;&gt;</code></p>
<dd>Specify a list of video filters to apply to the video stream. See <i>VIDEO FILTERS</i> for details and descriptions of the available filters. The option variants <code>&#8211;vf-add</code>, <code>&#8211;vf-pre</code>, <code>&#8211;vf-del</code> and <code>&#8211;vf-clr</code> exist to modify a previously specified list, but you should not need these for typical use.</p>
<dt><code>&#8211;untimed</code></p>
<dd>Do not sleep when outputting video frames. Useful for benchmarks when used with <code>&#8211;no-audio.</code></p>
<dt><code>&#8211;framedrop=&lt;mode&gt;</code></p>
<dd>Skip displaying some frames to maintain A/V sync on slow systems, or playing high framerate video on video outputs that have an upper framerate limit. </p>
<p> The argument selects the drop methods, and can be one of the following:</p>
<dt><code>&lt;no&gt;</code></p>
<dd>Disable any frame dropping. Not recommended, for testing only.</p>
<dt><code>&lt;vo&gt;</code></p>
<dd>Drop late frames on video output (default). This still decodes and filters all frames, but doesn&#8217;t render them on the VO. Drops are indicated in the terminal status line as <code>Dropped:</code> field. </p>
<p> In audio sync. mode, this drops frames that are outdated at the time of display. If the decoder is too slow, in theory all frames would have to be dropped (because all frames are too late) &#8211; to avoid this, frame dropping stops if the effective framerate is below 10 FPS. </p>
<p> In display-sync. modes (see <code>&#8211;video-sync</code>), this affects only how A/V drops or repeats frames. If this mode is disabled, A/V desync will in theory not affect video scheduling anymore (much like the <code>display-resample-desync</code> mode). However, even if disabled, frames will still be skipped (i.e. dropped) according to the ratio between video and display frequencies. </p>
<p> This is the recommended mode, and the default.</p>
<dt><code>&lt;decoder&gt;</code></p>
<dd>Old, decoder-based framedrop mode. (This is the same as <code>&#8211;framedrop=yes</code> in mpv 0.5.x and before.) This tells the decoder to skip frames (unless they are needed to decode future frames). May help with slow systems, but can produce unwatchable choppy output, or even freeze the display completely. </p>
<p> This uses a heuristic which may not make sense, and in general cannot achieve good results, because the decoder&#8217;s frame dropping cannot be controlled in a predictable manner. Not recommended. </p>
<p> Even if you want to use this, prefer <code>decoder+vo</code> for better results. </p>
<p> The <code>&#8211;vd-lavc-framedrop</code> option controls what frames to drop.</p>
<dt><code>&lt;decoder+vo&gt;</code></p>
<dd>Enable both modes. Not recommended. Better than just <code>decoder</code> mode. </p>
<p> <code>NOTE:</code> <code>&#8211;vo=vdpau</code> has its own code for the <code>vo</code> framedrop mode. Slight differences to other VOs are possible.</p>
<dt><code>&#8211;video-latency-hacks=&lt;yes|no&gt;</code></p>
<dd>Enable some things which tend to reduce video latency by 1 or 2 frames (default: no). Note that this option might be removed without notice once the player&#8217;s timing code does not inherently need to do these things anymore. </p>
<p> This does:</p>
<dt>&bull;</p>
<dd>Use the demuxer reported FPS for frame dropping. This avoids the player needing to decode 1 frame in advance, lowering total latency in effect. This also means that if the demuxer reported FPS is wrong, or the video filter chain changes FPS (e.g. deinterlacing), then it could drop too many or not enough frames.</p>
<dt>&bull;</p>
<dd>Disable waiting for the first video frame. Normally the player waits for the first video frame to be fully rendered before starting playback properly. Some VOs will lazily initialize stuff when rendering the first frame, so if this is not done, there is some likeliness that the VO has to drop some frames if rendering the first frame takes longer than needed.</p>
<dt><code>&#8211;override-display-fps=&lt;fps&gt;</code></p>
<dd>Set the display FPS used with the <code>&#8211;video-sync=display-*</code> modes. By default, a detected value is used. Keep in mind that setting an incorrect value (even if slightly incorrect) can ruin video playback. On multi-monitor systems, there is a chance that the detected value is from the wrong monitor. </p>
<p> Set this option only if you have reason to believe the automatically determined value is wrong.</p>
<dt><code>&#8211;display-fps=&lt;fps&gt;</code></p>
<dd>Deprecated alias for <code>&#8211;override-display-fps</code>.</p>
<dt><code>&#8211;hwdec=&lt;api&gt;</code></p>
<dd>Specify the hardware video decoding API that should be used if possible. Whether hardware decoding is actually done depends on the video codec. If hardware decoding is not possible, mpv will fall back on software decoding. </p>
<p> Hardware decoding is not enabled by default, because it is typically an additional source of errors. It is worth using only if your CPU is too slow to decode a specific video. </p>
<p> <code>NOTE:</code> Use the <code>Ctrl+h</code> shortcut to toggle hardware decoding at runtime. It toggles this option between <code>auto</code> and <code>no</code>. </p>
<p> Always enabling HW decoding by putting it into the config file is discouraged. If you use the Ubuntu package, delete <code>/etc/mpv/mpv.conf</code>, as the package tries to enable HW decoding by default by setting <code>hwdec=vaapi</code> (which is less than ideal, and may even cause sub-optimal wrappers to be used). Or at least change it to <code>hwdec=auto-safe</code>. </p>
<p> Use one of the auto modes if you want to enable hardware decoding. Explicitly selecting the mode is mostly meant for testing and debugging. It&#8217;s a bad idea to put explicit selection into the config file if you want thing to just keep working after updates and so on. </p>
<p> <code>NOTE:</code> Even if enabled, hardware decoding is still only white-listed for some codecs. See <code>&#8211;hwdec-codecs</code> to enable hardware decoding in more cases.</p>
<dt>Which method to choose?</p>
<dd>
<dt>&bull;</p>
<dd>If you only want to enable hardware decoding at runtime, don&#8217;t set the parameter, or put <code>hwdec=no</code> into your <code>mpv.conf</code> (relevant on distros which force-enable it by default, such as on Ubuntu). Use the <code>Ctrl+h</code> default binding to enable it at runtime.</p>
<dt>&bull;</p>
<dd>If you&#8217;re not sure, but want hardware decoding always enabled by default, put <code>hwdec=auto-safe</code> into your <code>mpv.conf</code>, and acknowledge that this use case is not &quot;really&quot; supported and may cause problems.</p>
<dt>&bull;</p>
<dd>If you want to test available hardware decoding methods, pass <code>&#8211;hwdec=auto &#8211;hwdec-codecs=all</code> and look at the terminal output.</p>
<dt>&bull;</p>
<dd>If you&#8217;re a developer, or want to perform elaborate tests, you may need any of the other possible option values. </p>
<p> <code>&lt;api&gt;</code> can be one of the following:</p>
<dt><code>no</code></p>
<dd>always use software decoding (default)</p>
<dt><code>auto</code></p>
<dd>forcibly enable any hw decoder found (see below)</p>
<dt><code>yes</code></p>
<dd>exactly the same as <code>auto</code></p>
<dt><code>auto-safe</code></p>
<dd>enable any whitelisted hw decoder (see below)</p>
<dt><code>auto-copy</code></p>
<dd>enable best hw decoder with copy-back (see below)</p>
<dt><code>vdpau</code></p>
<dd>requires <code>&#8211;vo=gpu</code> with X11, or <code>&#8211;vo=vdpau</code> (Linux only)</p>
<dt><code>vdpau-copy</code></p>
<dd>copies video back into system RAM (Linux with some GPUs only)</p>
<dt><code>vaapi</code></p>
<dd>requires <code>&#8211;vo=gpu</code> or <code>&#8211;vo=vaapi</code> (Linux only)</p>
<dt><code>vaapi-copy</code></p>
<dd>copies video back into system RAM (Linux with some GPUs only)</p>
<dt><code>videotoolbox</code></p>
<dd>requires <code>&#8211;vo=gpu</code> (macOS 10.8 and up), or <code>&#8211;vo=libmpv</code> (iOS 9.0 and up)</p>
<dt><code>videotoolbox-copy</code></p>
<dd>copies video back into system RAM (macOS 10.8 or iOS 9.0 and up)</p>
<dt><code>dxva2</code></p>
<dd>requires <code>&#8211;vo=gpu</code> with <code>&#8211;gpu-context=d3d11</code>, <code>&#8211;gpu-context=angle</code> or <code>&#8211;gpu-context=dxinterop</code> (Windows only)</p>
<dt><code>dxva2-copy</code></p>
<dd>copies video back to system RAM (Windows only)</p>
<dt><code>d3d11va</code></p>
<dd>requires <code>&#8211;vo=gpu</code> with <code>&#8211;gpu-context=d3d11</code> or <code>&#8211;gpu-context=angle</code> (Windows 8+ only)</p>
<dt><code>d3d11va-copy</code></p>
<dd>copies video back to system RAM (Windows 8+ only)</p>
<dt><code>mediacodec</code></p>
<dd>requires <code>&#8211;vo=mediacodec_embed</code> (Android only)</p>
<dt><code>mediacodec-copy</code></p>
<dd>copies video back to system RAM (Android only)</p>
<dt><code>mmal</code></p>
<dd>requires <code>&#8211;vo=gpu</code> (Raspberry Pi only &#8211; default if available)</p>
<dt><code>mmal-copy</code></p>
<dd>copies video back to system RAM (Raspberry Pi only)</p>
<dt><code>nvdec</code></p>
<dd>requires <code>&#8211;vo=gpu</code> (Any platform CUDA is available)</p>
<dt><code>nvdec-copy</code></p>
<dd>copies video back to system RAM (Any platform CUDA is available)</p>
<dt><code>cuda</code></p>
<dd>requires <code>&#8211;vo=gpu</code> (Any platform CUDA is available)</p>
<dt><code>cuda-copy</code></p>
<dd>copies video back to system RAM (Any platform CUDA is available)</p>
<dt><code>crystalhd</code></p>
<dd>copies video back to system RAM (Any platform supported by hardware)</p>
<dt><code>rkmpp</code></p>
<dd>requires <code>&#8211;vo=gpu</code> (some RockChip devices only) </p>
<p> <code>auto</code> tries to automatically enable hardware decoding using the first available method. This still depends what VO you are using. For example, if you are not using <code>&#8211;vo=gpu</code> or <code>&#8211;vo=vdpau</code>, vdpau decoding will never be enabled. Also note that if the first found method doesn&#8217;t actually work, it will always fall back to software decoding, instead of trying the next method (might matter on some Linux systems). </p>
<p> <code>auto-safe</code> is similar to <code>auto</code>, but allows only whitelisted methods that are considered &quot;safe&quot;. This is supposed to be a reasonable way to enable hardware decdoding by default in a config file (even though you shouldn&#8217;t do that anyway; prefer runtime enabling with <code>Ctrl+h</code>). Unlike <code>auto</code>, this will not try to enable unknown or known-to-be-bad methods. In addition, this may disable hardware decoding in other situations when it&#8217;s known to cause problems, but currently this mechanism is quite primitive. (As an example for something that still causes problems: certain combinations of HEVC and Intel chips on Windows tend to cause mpv to crash, most likely due to driver bugs.) </p>
<p> <code>auto-copy-safe</code> selects the union of methods selected with <code>auto-safe</code> and <code>auto-copy</code>. </p>
<p> <code>auto-copy</code> selects only modes that copy the video data back to system memory after decoding. This selects modes like <code>vaapi-copy</code> (and so on). If none of these work, hardware decoding is disabled. This mode is usually guaranteed to incur no additional quality loss compared to software decoding (assuming modern codecs and an error free video stream), and will allow CPU processing with video filters. This mode works with all video filters and VOs. </p>
<p> Because these copy the decoded video back to system RAM, they&#8217;re often less efficient than the direct modes, and may not help too much over software decoding. </p>
<p> <code>NOTE:</code> Most non-copy methods only work with the OpenGL GPU backend. Currently, only the <code>vaapi</code>, <code>nvdec</code> and <code>cuda</code> methods work with Vulkan. </p>
<p> The <code>vaapi</code> mode, if used with <code>&#8211;vo=gpu</code>, requires Mesa 11, and most likely works with Intel and AMD GPUs only. It also requires the opengl EGL backend. </p>
<p> <code>nvdec</code> and <code>nvdec-copy</code> are the newest, and recommended method to do hardware decoding on Nvidia GPUs. </p>
<p> <code>cuda</code> and <code>cuda-copy</code> are an older implementation of hardware decoding on Nvidia GPUs that uses Nvidia&#8217;s bitstream parsers rather than FFmpeg&#8217;s. This can lead to feature deficiencies, such as incorrect playback of HDR content, and <code>nvdec</code>/<code>nvdec-copy</code> should always be preferred unless you specifically need Nvidia&#8217;s deinterlacing algorithms. To use this deinterlacing you must pass the option: <code>vd-lavc-o=deint=[weave|bob|adaptive]</code>. Pass <code>weave</code> (or leave the option unset) to not attempt any deinterlacing.</p>
<dt>Quality reduction with hardware decoding</p>
<dd>In theory, hardware decoding does not reduce video quality (at least for the codecs h264 and HEVC). However, due to restrictions in video output APIs, as well as bugs in the actual hardware decoders, there can be some loss, or even blatantly incorrect results. </p>
<p> In some cases, RGB conversion is forced, which means the RGB conversion is performed by the hardware decoding API, instead of the shaders used by <code>&#8211;vo=gpu</code>. This means certain colorspaces may not display correctly, and certain filtering (such as debanding) cannot be applied in an ideal way. This will also usually force the use of low quality chroma scalers instead of the one specified by <code>&#8211;cscale</code>. In other cases, hardware decoding can also reduce the bit depth of the decoded image, which can introduce banding or precision loss for 10-bit files. </p>
<p> <code>vdpau</code> always does RGB conversion in hardware, which does not support newer colorspaces like BT.2020 correctly. However, <code>vdpau</code> doesn&#8217;t support 10 bit or HDR encodings, so these limitations are unlikely to be relevant. </p>
<p> <code>vaapi</code> and <code>d3d11va</code> are safe. Enabling deinterlacing (or simply their respective post-processing filters) will possibly at least reduce color quality by converting the output to a 8 bit format. </p>
<p> <code>dxva2</code> is not safe. It appears to always use BT.601 for forced RGB conversion, but actual behavior depends on the GPU drivers. Some drivers appear to convert to limited range RGB, which gives a faded appearance. In addition to driver-specific behavior, global system settings might affect this additionally. This can give incorrect results even with completely ordinary video sources. </p>
<p> <code>rpi</code> always uses the hardware overlay renderer, even with <code>&#8211;vo=gpu</code>. </p>
<p> <code>cuda</code> should usually be safe, but depending on how a file/stream has been mixed, it has been reported to corrupt the timestamps causing glitched, flashing frames. It can also sometimes cause massive framedrops for unknown reasons. Caution is advised, and <code>nvdec</code> should always be preferred. </p>
<p> <code>crystalhd</code> is not safe. It always converts to 4:2:2 YUV, which may be lossy, depending on how chroma sub-sampling is done during conversion. It also discards the top left pixel of each frame for some reason. </p>
<p> All other methods, in particular the copy-back methods (like <code>dxva2-copy</code> etc.) should hopefully be safe, although they can still cause random decoding issues. At the very least, they shouldn&#8217;t affect the colors of the image. </p>
<p> In particular, <code>auto-copy</code> will only select &quot;safe&quot; modes (although potentially slower than other methods), but there&#8217;s still no guarantee the chosen hardware decoder will actually work correctly. </p>
<p> In general, it&#8217;s very strongly advised to avoid hardware decoding unless <code>absolutely</code> necessary, i.e. if your CPU is insufficient to decode the file in questions. If you run into any weird decoding issues, frame glitches or discoloration, and you have <code>&#8211;hwdec</code> turned on, the first thing you should try is disabling it.</p>
<dt><code>&#8211;gpu-hwdec-interop=&lt;auto|all|no|name&gt;</code></p>
<dd>This option is for troubleshooting hwdec interop issues. Since it&#8217;s a debugging option, its semantics may change at any time. </p>
<p> This is useful for the <code>gpu</code> and <code>libmpv</code> VOs for selecting which hwdec interop context to use exactly. Effectively it also can be used to block loading of certain backends. </p>
<p> If set to <code>auto</code> (default), the behavior depends on the VO: for <code>gpu</code>, it does nothing, and the interop context is loaded on demand (when the decoder probes for <code>&#8211;hwdec</code> support). For <code>libmpv</code>, which has has no on-demand loading, this is equivalent to <code>all</code>. </p>
<p> The empty string is equivalent to <code>auto</code>. </p>
<p> If set to <code>all</code>, it attempts to load all interop contexts at GL context creation time. </p>
<p> Other than that, a specific backend can be set, and the list of them can be queried with <code>help</code> (mpv CLI only). </p>
<p> Runtime changes to this are ignored (the current option value is used whenever the renderer is created). </p>
<p> The old aliases <code>&#8211;opengl-hwdec-interop</code> and <code>&#8211;hwdec-preload</code> are barely related to this anymore, but will be somewhat compatible in some cases.</p>
<dt><code>&#8211;hwdec-extra-frames=&lt;N&gt;</code></p>
<dd>Number of GPU frames hardware decoding should preallocate (default: see <code>&#8211;list-options</code> output). If this is too low, frame allocation may fail during decoding, and video frames might get dropped and/or corrupted. Setting it too high simply wastes GPU memory and has no advantages. </p>
<p> This value is used only for hardware decoding APIs which require preallocating surfaces (known examples include <code>d3d11va</code> and <code>vaapi</code>). For other APIs, frames are allocated as needed. The details depend on the libavcodec implementations of the hardware decoders. </p>
<p> The required number of surfaces depends on dynamic runtime situations. The default is a fixed value that is thought to be sufficient for most uses. But in certain situations, it may not be enough.</p>
<dt><code>&#8211;hwdec-image-format=&lt;name&gt;</code></p>
<dd>Set the internal pixel format used by hardware decoding via <code>&#8211;hwdec</code> (default <code>no</code>). The special value <code>no</code> selects an implementation specific standard format. Most decoder implementations support only one format, and will fail to initialize if the format is not supported. </p>
<p> Some implementations might support multiple formats. In particular, videotoolbox is known to require <code>uyvy422</code> for good performance on some older hardware. d3d11va can always use <code>yuv420p</code>, which uses an opaque format, with likely no advantages.</p>
<dt><code>&#8211;cuda-decode-device=&lt;auto|0..&gt;</code></p>
<dd>Choose the GPU device used for decoding when using the <code>cuda</code> or <code>nvdec</code> hwdecs with the OpenGL GPU backend, and with the <code>cuda-copy</code> or <code>nvdec-copy</code> hwdecs in all cases. </p>
<p> For the OpenGL GPU backend, the default device used for decoding is the one being used to provide <code>gpu</code> output (and in the vast majority of cases, only one GPU will be present). </p>
<p> For the <code>copy</code> hwdecs, the default device will be the first device enumerated by the CUDA libraries &#8211; however that is done. </p>
<p> For the Vulkan GPU backend, decoding must always happen on the display device, and this option has no effect.</p>
<dt><code>&#8211;vaapi-device=&lt;device file&gt;</code></p>
<dd>Choose the DRM device for <code>vaapi-copy</code>. This should be the path to a DRM device file. (Default: <code>/dev/dri/renderD128</code>)</p>
<dt><code>&#8211;panscan=&lt;0.0-1.0&gt;</code></p>
<dd>Enables pan-and-scan functionality (cropping the sides of e.g. a 16:9 video to make it fit a 4:3 display without black bands). The range controls how much of the image is cropped. May not work with all video output drivers. </p>
<p> This option has no effect if <code>&#8211;video-unscaled</code> option is used.</p>
<dt><code>&#8211;video-aspect-override=&lt;ratio|no&gt;</code></p>
<dd>Override video aspect ratio, in case aspect information is incorrect or missing in the file being played. </p>
<p> These values have special meaning:</p>
<dt><code>0</code></p>
<dd>disable aspect ratio handling, pretend the video has square pixels</p>
<dt><code>no</code></p>
<dd>same as <code>0</code></p>
<dt><code>-1</code></p>
<dd>use the video stream or container aspect (default) </p>
<p> But note that handling of these special values might change in the future.</p>
<dt>Examples</p>
<dd>
<dt>&bull;</p>
<dd><code>&#8211;video-aspect-override=4:3</code> or <code>&#8211;video-aspect-override=1.3333</code></p>
<dt>&bull;</p>
<dd><code>&#8211;video-aspect-override=16:9</code> or <code>&#8211;video-aspect-override=1.7777</code></p>
<dt>&bull;</p>
<dd><code>&#8211;no-video-aspect-override</code> or <code>&#8211;video-aspect-override=no</code></p>
<dt><code>&#8211;video-aspect-method=&lt;bitstream|container&gt;</code></p>
<dd>This sets the default video aspect determination method (if the aspect is _not_ overridden by the user with <code>&#8211;video-aspect-override</code> or others).</p>
<dt><code>container</code></p>
<dd>Strictly prefer the container aspect ratio. This is apparently the default behavior with VLC, at least with Matroska. Note that if the container has no aspect ratio set, the behavior is the same as with bitstream.</p>
<dt><code>bitstream</code></p>
<dd>Strictly prefer the bitstream aspect ratio, unless the bitstream aspect ratio is not set. This is apparently the default behavior with XBMC/kodi, at least with Matroska. </p>
<p> The current default for mpv is <code>container</code>. </p>
<p> Normally you should not set this. Try the various choices if you encounter video that has the wrong aspect ratio in mpv, but seems to be correct in other players.</p>
<dt><code>&#8211;video-unscaled=&lt;no|yes|downscale-big&gt;</code></p>
<dd>Disable scaling of the video. If the window is larger than the video, black bars are added. Otherwise, the video is cropped, unless the option is set to <code>downscale-big</code>, in which case the video is fit to window. The video still can be influenced by the other <code>&#8211;video-&#8230;</code> options. This option disables the effect of <code>&#8211;panscan</code>. </p>
<p> Note that the scaler algorithm may still be used, even if the video isn&#8217;t scaled. For example, this can influence chroma conversion. The video will also still be scaled in one dimension if the source uses non-square pixels (e.g. anamorphic widescreen DVDs). </p>
<p> This option is disabled if the <code>&#8211;no-keepaspect</code> option is used.</p>
<dt><code>&#8211;video-pan-x=&lt;value&gt;</code>, <code>&#8211;video-pan-y=&lt;value&gt;</code></p>
<dd>Moves the displayed video rectangle by the given value in the X or Y direction. The unit is in fractions of the size of the scaled video (the full size, even if parts of the video are not visible due to panscan or other options). </p>
<p> For example, displaying a 1280&#215;720 video fullscreen on a 1680&#215;1050 screen with <code>&#8211;video-pan-x=-0.1</code> would move the video 168 pixels to the left (making 128 pixels of the source video invisible). </p>
<p> This option is disabled if the <code>&#8211;no-keepaspect</code> option is used.</p>
<dt><code>&#8211;video-rotate=&lt;0-359|no&gt;</code></p>
<dd>Rotate the video clockwise, in degrees. If <code>no</code> is given, the video is never rotated, even if the file has rotation metadata. (The rotation value is added to the rotation metadata, which means the value <code>0</code> would rotate the video according to the rotation metadata.) </p>
<p> When using hardware decoding without copy-back, only 90° steps work, while software decoding and hardware decoding methods that copy the video back to system memory support all values between 0 and 359.</p>
<dt><code>&#8211;video-zoom=&lt;value&gt;</code></p>
<dd>Adjust the video display scale factor by the given value. The parameter is given log 2. For example, <code>&#8211;video-zoom=0</code> is unscaled, <code>&#8211;video-zoom=1</code> is twice the size, <code>&#8211;video-zoom=-2</code> is one fourth of the size, and so on. </p>
<p> This option is disabled if the <code>&#8211;no-keepaspect</code> option is used.</p>
<dt><code>&#8211;video-scale-x=&lt;value&gt;</code>, <code>&#8211;video-scale-y=&lt;value&gt;</code></p>
<dd>Multiply the video display size with the given value (default: 1.0). If a non-default value is used, this will be different from the window size, so video will be either cut off, or black bars are added. </p>
<p> This value is multiplied with the value derived from <code>&#8211;video-zoom</code> and the normal video aspect aspect ratio. This option is disabled if the <code>&#8211;no-keepaspect</code> option is used.</p>
<dt><code>&#8211;video-align-x=&lt;-1-1&gt;</code>, <code>&#8211;video-align-y=&lt;-1-1&gt;</code></p>
<dd>Moves the video rectangle within the black borders, which are usually added to pad the video to screen if video and screen aspect ratios are different. <code>&#8211;video-align-y=-1</code> would move the video to the top of the screen (leaving a border only on the bottom), a value of <code>0</code> centers it (default), and a value of <code>1</code> would put the video at the bottom of the screen. </p>
<p> If video and screen aspect match perfectly, these options do nothing. </p>
<p> This option is disabled if the <code>&#8211;no-keepaspect</code> option is used.</p>
<dt><code>&#8211;video-margin-ratio-left=&lt;val&gt;</code>, <code>&#8211;video-margin-ratio-right=&lt;val&gt;</code>, <code>&#8211;video-margin-ratio-top=&lt;val&gt;</code>, <code>&#8211;video-margin-ratio-bottom=&lt;val&gt;</code></p>
<dd>Set extra video margins on each border (default: 0). Each value is a ratio of the window size, using a range 0.0-1.0. For example, setting the option <code>&#8211;video-margin-ratio-right=0.2</code> at a window size of 1000 pixels will add a 200 pixels border on the right side of the window. </p>
<p> The video is &quot;boxed&quot; by these margins. The window size is not changed. In particular it does not enlarge the window, and the margins will cause the video to be downscaled by default. This may or may not change in the future. </p>
<p> The margins are applied after 90° video rotation, but before any other video transformations. </p>
<p> This option is disabled if the <code>&#8211;no-keepaspect</code> option is used. </p>
<p> Subtitles still may use the margins, depending on <code>&#8211;sub-use-margins</code> and similar options. </p>
<p> These options were created for the OSC. Some odd decisions, such as making the margin values a ratio (instead of pixels), were made for the sake of the OSC. It&#8217;s possible that these options may be replaced by ones that are more generally useful. The behavior of these options may change to fit OSC requirements better, too.</p>
<dt><code>&#8211;correct-pts</code>, <code>&#8211;no-correct-pts</code></p>
<dd><code>&#8211;no-correct-pts</code> switches mpv to a mode where video timing is determined using a fixed framerate value (either using the <code>&#8211;fps</code> option, or using file information). Sometimes, files with very broken timestamps can be played somewhat well in this mode. Note that video filters, subtitle rendering, seeking (including hr-seeks and backstepping), and audio synchronization can be completely broken in this mode.</p>
<dt><code>&#8211;fps=&lt;float&gt;</code></p>
<dd>Override video framerate. Useful if the original value is wrong or missing. </p>
<p> <code>NOTE:</code> Works in <code>&#8211;no-correct-pts</code> mode only.</p>
<dt><code>&#8211;deinterlace=&lt;yes|no&gt;</code></p>
<dd>Enable or disable interlacing (default: no). Interlaced video shows ugly comb-like artifacts, which are visible on fast movement. Enabling this typically inserts the yadif video filter in order to deinterlace the video, or lets the video output apply deinterlacing if supported. </p>
<p> This behaves exactly like the <code>deinterlace</code> input property (usually mapped to <code>d</code>). </p>
<p> Keep in mind that this <code>will</code> conflict with manually inserted deinterlacing filters, unless you take care. (Since mpv 0.27.0, even the hardware deinterlace filters will conflict. Also since that version, <code>&#8211;deinterlace=auto</code> was removed, which used to mean that the default interlacing option of possibly inserted video filters was used.) </p>
<p> Note that this will make video look worse if it&#8217;s not actually interlaced.</p>
<dt><code>&#8211;frames=&lt;number&gt;</code></p>
<dd>Play/convert only first <code>&lt;number&gt;</code> video frames, then quit. </p>
<p> <code>&#8211;frames=0</code> loads the file, but immediately quits before initializing playback. (Might be useful for scripts which just want to determine some file properties.) </p>
<p> For audio-only playback, any value greater than 0 will quit playback immediately after initialization. The value 0 works as with video.</p>
<dt><code>&#8211;video-output-levels=&lt;outputlevels&gt;</code></p>
<dd>RGB color levels used with YUV to RGB conversion. Normally, output devices such as PC monitors use full range color levels. However, some TVs and video monitors expect studio RGB levels. Providing full range output to a device expecting studio level input results in crushed blacks and whites, the reverse in dim gray blacks and dim whites. </p>
<p> Not all VOs support this option. Some will silently ignore it. </p>
<p> Available color ranges are:</p>
<dt><code>auto</code></p>
<dd>automatic selection (equals to full range) (default)</p>
<dt><code>limited</code></p>
<dd>limited range (16-235 per component), studio levels</p>
<dt><code>full</code></p>
<dd>full range (0-255 per component), PC levels </p>
<p> <code>NOTE:</code> It is advisable to use your graphics driver&#8217;s color range option instead, if available.</p>
<dt><code>&#8211;hwdec-codecs=&lt;codec1,codec2,&#8230;|all&gt;</code></p>
<dd>Allow hardware decoding for a given list of codecs only. The special value <code>all</code> always allows all codecs. </p>
<p> You can get the list of allowed codecs with <code>mpv &#8211;vd=help</code>. Remove the prefix, e.g. instead of <code>lavc:h264</code> use <code>h264</code>. </p>
<p> By default, this is set to <code>h264,vc1,hevc,vp8,vp9,av1</code>. Note that the hardware acceleration special codecs like <code>h264_vdpau</code> are not relevant anymore, and in fact have been removed from Libav in this form. </p>
<p> This is usually only needed with broken GPUs, where a codec is reported as supported, but decoding causes more problems than it solves.</p>
<dt>Example</p>
<dd>
<dt><code>mpv &#8211;hwdec=vdpau &#8211;vo=vdpau &#8211;hwdec-codecs=h264,mpeg2video</code></p>
<dd>Enable vdpau decoding for h264 and mpeg2 only.</p>
<dt><code>&#8211;vd-lavc-check-hw-profile=&lt;yes|no&gt;</code></p>
<dd>Check hardware decoder profile (default: yes). If <code>no</code> is set, the highest profile of the hardware decoder is unconditionally selected, and decoding is forced even if the profile of the video is higher than that. The result is most likely broken decoding, but may also help if the detected or reported profiles are somehow incorrect.</p>
<dt><code>&#8211;vd-lavc-software-fallback=&lt;yes|no|N&gt;</code></p>
<dd>Fallback to software decoding if the hardware-accelerated decoder fails (default: 3). If this is a number, then fallback will be triggered if N frames fail to decode in a row. 1 is equivalent to <code>yes</code>. </p>
<p> Setting this to a higher number might break the playback start fallback: if a fallback happens, parts of the file will be skipped, approximately by to the number of packets that could not be decoded. Values below an unspecified count will not have this problem, because mpv retains the packets.</p>
<dt><code>&#8211;vd-lavc-dr=&lt;yes|no&gt;</code></p>
<dd>Enable direct rendering (default: yes). If this is set to <code>yes</code>, the video will be decoded directly to GPU video memory (or staging buffers). This can speed up video upload, and may help with large resolutions or slow hardware. This works only with the following VOs:</p>
<dt>&bull;</p>
<dd><code>gpu</code>: requires at least OpenGL 4.4 or Vulkan. </p>
<p> (In particular, this can&#8217;t be made work with <code>opengl-cb</code>, but the libmpv render API has optional support.) </p>
<p> Using video filters of any kind that write to the image data (or output newly allocated frames) will silently disable the DR code path.</p>
<dt><code>&#8211;vd-lavc-bitexact</code></p>
<dd>Only use bit-exact algorithms in all decoding steps (for codec testing).</p>
<dt><code>&#8211;vd-lavc-fast</code> (MPEG-2, MPEG-4, and H.264 only)</p>
<dd>Enable optimizations which do not comply with the format specification and potentially cause problems, like simpler dequantization, simpler motion compensation, assuming use of the default quantization matrix, assuming YUV 4:2:0 and skipping a few checks to detect damaged bitstreams.</p>
<dt><code>&#8211;vd-lavc-o=&lt;key&gt;=&lt;value&gt;[,&lt;key&gt;=&lt;value&gt;[,&#8230;]]</code></p>
<dd>Pass AVOptions to libavcodec decoder. Note, a patch to make the <code>o=</code> unneeded and pass all unknown options through the AVOption system is welcome. A full list of AVOptions can be found in the FFmpeg manual. </p>
<p> Some options which used to be direct options can be set with this mechanism, like <code>bug</code>, <code>gray</code>, <code>idct</code>, <code>ec</code>, <code>vismv</code>, <code>skip_top</code> (was <code>st</code>), <code>skip_bottom</code> (was <code>sb</code>), <code>debug</code>. </p>
<p> This is a key/value list option. See <i>List Options</i> for details.</p>
<dt>Example</p>
<dd><code>&#8211;vd-lavc-o=debug=pict</code></p>
<dt><code>&#8211;vd-lavc-show-all=&lt;yes|no&gt;</code></p>
<dd>Show even broken/corrupt frames (default: no). If this option is set to no, libavcodec won&#8217;t output frames that were either decoded before an initial keyframe was decoded, or frames that are recognized as corrupted.</p>
<dt><code>&#8211;vd-lavc-skiploopfilter=&lt;skipvalue&gt; (H.264 only)</code></p>
<dd>Skips the loop filter (AKA deblocking) during H.264 decoding. Since the filtered frame is supposed to be used as reference for decoding dependent frames, this has a worse effect on quality than not doing deblocking on e.g. MPEG-2 video. But at least for high bitrate HDTV, this provides a big speedup with little visible quality loss. </p>
<p> <code>&lt;skipvalue&gt;</code> can be one of the following:</p>
<dt><code>none</code></p>
<dd>Never skip.</p>
<dt><code>default</code></p>
<dd>Skip useless processing steps (e.g. 0 size packets in AVI).</p>
<dt><code>nonref</code></p>
<dd>Skip frames that are not referenced (i.e. not used for decoding other frames, the error cannot &quot;build up&quot;).</p>
<dt><code>bidir</code></p>
<dd>Skip B-Frames.</p>
<dt><code>nonkey</code></p>
<dd>Skip all frames except keyframes.</p>
<dt><code>all</code></p>
<dd>Skip all frames.</p>
<dt><code>&#8211;vd-lavc-skipidct=&lt;skipvalue&gt; (MPEG-1/2 only)</code></p>
<dd>Skips the IDCT step. This degrades quality a lot in almost all cases (see skiploopfilter for available skip values).</p>
<dt><code>&#8211;vd-lavc-skipframe=&lt;skipvalue&gt;</code></p>
<dd>Skips decoding of frames completely. Big speedup, but jerky motion and sometimes bad artifacts (see skiploopfilter for available skip values).</p>
<dt><code>&#8211;vd-lavc-framedrop=&lt;skipvalue&gt;</code></p>
<dd>Set framedropping mode used with <code>&#8211;framedrop</code> (see skiploopfilter for available skip values).</p>
<dt><code>&#8211;vd-lavc-threads=&lt;N&gt;</code></p>
<dd>Number of threads to use for decoding. Whether threading is actually supported depends on codec (default: 0). 0 means autodetect number of cores on the machine and use that, up to the maximum of 16. You can set more than 16 threads manually.</p>
<dt><code>&#8211;vd-lavc-assume-old-x264=&lt;yes|no&gt;</code></p>
<dd>Assume the video was encoded by an old, buggy x264 version (default: no). Normally, this is autodetected by libavcodec. But if the bitstream contains no x264 version info (or it was somehow skipped), and the stream was in fact encoded by an old x264 version (build 150 or earlier), and if the stream uses <code>4:4:4</code> chroma, then libavcodec will by default show corrupted video. This option sets the libavcodec <code>x264_build</code> option to <code>150</code>, which means that if the stream contains no version info, or was not encoded by x264 at all, it assumes it was encoded by the old version. Enabling this option is pretty safe if you want your broken files to work, but in theory this can break on streams not encoded by x264, or if a stream encoded by a newer x264 version contains no version info.</p>
<dt><code>&#8211;swapchain-depth=&lt;N&gt;</code></p>
<dd>Allow up to N in-flight frames. This essentially controls the frame latency. Increasing the swapchain depth can improve pipelining and prevent missed vsyncs, but increases visible latency. This option only mandates an upper limit, the implementation can use a lower latency than requested internally. A setting of 1 means that the VO will wait for every frame to become visible before starting to render the next frame. (Default: 3)</dl>
<h3>Audio</h3>
<dl COMPACT>
<dt><code>&#8211;audio-pitch-correction=&lt;yes|no&gt;</code></p>
<dd>If this is enabled (default), playing with a speed different from normal automatically inserts the <code>scaletempo2</code> audio filter. For details, see audio filter section.</p>
<dt><code>&#8211;audio-device=&lt;name&gt;</code></p>
<dd>Use the given audio device. This consists of the audio output name, e.g. <code>alsa</code>, followed by <code>/</code>, followed by the audio output specific device name. The default value for this option is <code>auto</code>, which tries every audio output in preference order with the default device. </p>
<p> You can list audio devices with <code>&#8211;audio-device=help</code>. This outputs the device name in quotes, followed by a description. The device name is what you have to pass to the <code>&#8211;audio-device</code> option. The list of audio devices can be retrieved by API by using the <code>audio-device-list</code> property. </p>
<p> While the option normally takes one of the strings as indicated by the methods above, you can also force the device for most AOs by building it manually. For example <code>name/foobar</code> forces the AO <code>name</code> to use the device <code>foobar</code>. However, the <code>&#8211;ao</code> option will strictly force a specific AO. To avoid confusion, don&#8217;t use <code>&#8211;ao</code> and <code>&#8211;audio-device</code> together.</p>
<dt>Example for ALSA</p>
<dd>MPlayer and mplayer2 required you to replace any &#8216;,&#8217; with &#8216;.&#8217; and any &#8216;:&#8217; with &#8216;=&#8217; in the ALSA device name. For example, to use the device named <code>dmix:default</code>, you had to do: <code>-ao alsa:device=dmix=default</code> </p>
<p> In mpv you could instead use: <code>&#8211;audio-device=alsa/dmix:default</code></p>
<dt><code>&#8211;audio-exclusive=&lt;yes|no&gt;</code></p>
<dd>Enable exclusive output mode. In this mode, the system is usually locked out, and only mpv will be able to output audio. </p>
<p> This only works for some audio outputs, such as <code>wasapi</code> and <code>coreaudio</code>. Other audio outputs silently ignore this options. They either have no concept of exclusive mode, or the mpv side of the implementation is missing.</p>
<dt><code>&#8211;audio-fallback-to-null=&lt;yes|no&gt;</code></p>
<dd>If no audio device can be opened, behave as if <code>&#8211;ao=null</code> was given. This is useful in combination with <code>&#8211;audio-device</code>: instead of causing an error if the selected device does not exist, the client API user (or a Lua script) could let playback continue normally, and check the <code>current-ao</code> and <code>audio-device-list</code> properties to make high-level decisions about how to continue.</p>
<dt><code>&#8211;ao=&lt;driver&gt;</code></p>
<dd>Specify the audio output drivers to be used. See <i>AUDIO OUTPUT DRIVERS</i> for details and descriptions of available drivers.</p>
<dt><code>&#8211;af=&lt;filter1[=parameter1:parameter2:&#8230;],filter2,&#8230;&gt;</code></p>
<dd>Specify a list of audio filters to apply to the audio stream. See <i>AUDIO FILTERS</i> for details and descriptions of the available filters. The option variants <code>&#8211;af-add</code>, <code>&#8211;af-pre</code>, <code>&#8211;af-del</code> and <code>&#8211;af-clr</code> exist to modify a previously specified list, but you should not need these for typical use.</p>
<dt><code>&#8211;audio-spdif=&lt;codecs&gt;</code></p>
<dd>List of codecs for which compressed audio passthrough should be used. This works for both classic S/PDIF and HDMI. </p>
<p> Possible codecs are <code>ac3</code>, <code>dts</code>, <code>dts-hd</code>, <code>eac3</code>, <code>truehd</code>. Multiple codecs can be specified by separating them with <code>,</code>. <code>dts</code> refers to low bitrate DTS core, while <code>dts-hd</code> refers to DTS MA (receiver and OS support varies). If both <code>dts</code> and <code>dts-hd</code> are specified, it behaves equivalent to specifying <code>dts-hd</code> only. </p>
<p> In earlier mpv versions you could use <code>&#8211;ad</code> to force the spdif wrapper. This does not work anymore.</p>
<dt>Warning</p>
<dd>There is not much reason to use this. HDMI supports uncompressed multichannel PCM, and mpv supports lossless DTS-HD decoding via FFmpeg&#8217;s new DCA decoder (based on libdcadec).</p>
<dt><code>&#8211;ad=&lt;decoder1,decoder2,&#8230;[-]&gt;</code></p>
<dd>Specify a priority list of audio decoders to be used, according to their decoder name. When determining which decoder to use, the first decoder that matches the audio format is selected. If that is unavailable, the next decoder is used. Finally, it tries all other decoders that are not explicitly selected or rejected by the option. </p>
<p> <code>&#8211;</code> at the end of the list suppresses fallback on other available decoders not on the <code>&#8211;ad</code> list. <code>+</code> in front of an entry forces the decoder. Both of these should not normally be used, because they break normal decoder auto-selection! Both of these methods are deprecated.</p>
<dt>Examples</p>
<dd>
<dt><code>&#8211;ad=mp3float</code></p>
<dd>Prefer the FFmpeg/Libav <code>mp3float</code> decoder over all other MP3 decoders.</p>
<dt><code>&#8211;ad=help</code></p>
<dd>List all available decoders.</p>
<dt>Warning</p>
<dd>Enabling compressed audio passthrough (AC3 and DTS via SPDIF/HDMI) with this option is not possible. Use <code>&#8211;audio-spdif</code> instead.</p>
<dt><code>&#8211;volume=&lt;value&gt;</code></p>
<dd>Set the startup volume. 0 means silence, 100 means no volume reduction or amplification. Negative values can be passed for compatibility, but are treated as 0. </p>
<p> Since mpv 0.18.1, this always controls the internal mixer (aka &quot;softvol&quot;).</p>
<dt><code>&#8211;replaygain=&lt;no|track|album&gt;</code></p>
<dd>Adjust volume gain according to replaygain values stored in the file metadata. With <code>&#8211;replaygain=no</code> (the default), perform no adjustment. With <code>&#8211;replaygain=track</code>, apply track gain. With <code>&#8211;replaygain=album</code>, apply album gain if present and fall back to track gain otherwise.</p>
<dt><code>&#8211;replaygain-preamp=&lt;db&gt;</code></p>
<dd>Pre-amplification gain in dB to apply to the selected replaygain gain (default: 0).</p>
<dt><code>&#8211;replaygain-clip=&lt;yes|no&gt;</code></p>
<dd>Prevent clipping caused by replaygain by automatically lowering the gain (default). Use <code>&#8211;replaygain-clip=no</code> to disable this.</p>
<dt><code>&#8211;replaygain-fallback=&lt;db&gt;</code></p>
<dd>Gain in dB to apply if the file has no replay gain tags. This option is always applied if the replaygain logic is somehow inactive. If this is applied, no other replaygain options are applied.</p>
<dt><code>&#8211;audio-delay=&lt;sec&gt;</code></p>
<dd>Audio delay in seconds (positive or negative float value). Positive values delay the audio, and negative values delay the video.</p>
<dt><code>&#8211;mute=&lt;yes|no|auto&gt;</code></p>
<dd>Set startup audio mute status (default: no). </p>
<p> <code>auto</code> is a deprecated possible value that is equivalent to <code>no</code>. </p>
<p> See also: <code>&#8211;volume</code>.</p>
<dt><code>&#8211;softvol=&lt;no|yes|auto&gt;</code></p>
<dd>Deprecated/unfunctional. Before mpv 0.18.1, this used to control whether to use the volume controls of the audio output driver or the internal mpv volume filter. </p>
<p> The current behavior is that softvol is always enabled, i.e. as if this option is set to <code>yes</code>. The other behaviors are not available anymore, although <code>auto</code> almost matches current behavior in most cases. </p>
<p> The <code>no</code> behavior is still partially available through the <code>ao-volume</code> and <code>ao-mute</code> properties. But there are no options to reset these.</p>
<dt><code>&#8211;audio-demuxer=&lt;[+]name&gt;</code></p>
<dd>Use this audio demuxer type when using <code>&#8211;audio-file</code>. Use a &#8216;+&#8217; before the name to force it; this will skip some checks. Give the demuxer name as printed by <code>&#8211;audio-demuxer=help</code>.</p>
<dt><code>&#8211;ad-lavc-ac3drc=&lt;level&gt;</code></p>
<dd>Select the Dynamic Range Compression level for AC-3 audio streams. <code>&lt;level&gt;</code> is a float value ranging from 0 to 1, where 0 means no compression (which is the default) and 1 means full compression (make loud passages more silent and vice versa). Values up to 6 are also accepted, but are purely experimental. This option only shows an effect if the AC-3 stream contains the required range compression information. </p>
<p> The standard mandates that DRC is enabled by default, but mpv (and some other players) ignore this for the sake of better audio quality.</p>
<dt><code>&#8211;ad-lavc-downmix=&lt;yes|no&gt;</code></p>
<dd>Whether to request audio channel downmixing from the decoder (default: no). Some decoders, like AC-3, AAC and DTS, can remix audio on decoding. The requested number of output channels is set with the <code>&#8211;audio-channels</code> option. Useful for playing surround audio on a stereo system.</p>
<dt><code>&#8211;ad-lavc-threads=&lt;0-16&gt;</code></p>
<dd>Number of threads to use for decoding. Whether threading is actually supported depends on codec. As of this writing, it&#8217;s supported for some lossless codecs only. 0 means autodetect number of cores on the machine and use that, up to the maximum of 16 (default: 1).</p>
<dt><code>&#8211;ad-lavc-o=&lt;key&gt;=&lt;value&gt;[,&lt;key&gt;=&lt;value&gt;[,&#8230;]]</code></p>
<dd>Pass AVOptions to libavcodec decoder. Note, a patch to make the o= unneeded and pass all unknown options through the AVOption system is welcome. A full list of AVOptions can be found in the FFmpeg manual. </p>
<p> This is a key/value list option. See <i>List Options</i> for details.</p>
<dt><code>&#8211;ad-spdif-dtshd=&lt;yes|no&gt;</code>, <code>&#8211;dtshd</code>, <code>&#8211;no-dtshd</code></p>
<dd>If DTS is passed through, use DTS-HD.</p>
<dt>Warning</p>
<dd>This and enabling passthrough via <code>&#8211;ad</code> are deprecated in favor of using <code>&#8211;audio-spdif=dts-hd</code>.</p>
<dt><code>&#8211;audio-channels=&lt;auto-safe|auto|layouts&gt;</code></p>
<dd>Control which audio channels are output (e.g. surround vs. stereo). There are the following possibilities:</p>
<dt>&bull;</p>
<dd>
<dt><code>&#8211;audio-channels=auto-safe</code></p>
<dd>Use the system&#8217;s preferred channel layout. If there is none (such as when accessing a hardware device instead of the system mixer), force stereo. Some audio outputs might simply accept any layout and do downmixing on their own. </p>
<p> This is the default.</p>
<dt>&bull;</p>
<dd>
<dt><code>&#8211;audio-channels=auto</code></p>
<dd>Send the audio device whatever it accepts, preferring the audio&#8217;s original channel layout. Can cause issues with HDMI (see the warning below).</p>
<dt>&bull;</p>
<dd>
<dt><code>&#8211;audio-channels=layout1,layout2,&#8230;</code></p>
<dd>List of <code>,</code>-separated channel layouts which should be allowed. Technically, this only adjusts the filter chain output to the best matching layout in the list, and passes the result to the audio API. It&#8217;s possible that the audio API will select a different channel layout. </p>
<p> Using this mode is recommended for direct hardware output, especially over HDMI (see HDMI warning below).</p>
<dt>&bull;</p>
<dd>
<dt><code>&#8211;audio-channels=stereo</code></p>
<dd>Force a plain stereo downmix. This is a special-case of the previous item. (See paragraphs below for implications.) </p>
<p> If a list of layouts is given, each item can be either an explicit channel layout name (like <code>5.1</code>), or a channel number. Channel numbers refer to default layouts, e.g. 2 channels refer to stereo, 6 refers to 5.1. </p>
<p> See <code>&#8211;audio-channels=help</code> output for defined default layouts. This also lists speaker names, which can be used to express arbitrary channel layouts (e.g. <code>fl-fr-lfe</code> is 2.1). </p>
<p> If the list of channel layouts has only 1 item, the decoder is asked to produce according output. This sometimes triggers decoder-downmix, which might be different from the normal mpv downmix. (Only some decoders support remixing audio, like AC-3, AAC or DTS. You can use <code>&#8211;ad-lavc-downmix=no</code> to make the decoder always output its native layout.) One consequence is that <code>&#8211;audio-channels=stereo</code> triggers decoder downmix, while <code>auto</code> or <code>auto-safe</code> never will, even if they end up selecting stereo. This happens because the decision whether to use decoder downmix happens long before the audio device is opened. </p>
<p> If the channel layout of the media file (i.e. the decoder) and the AO&#8217;s channel layout don&#8217;t match, mpv will attempt to insert a conversion filter. You may need to change the channel layout of the system mixer to achieve your desired output as mpv does not have control over it. Another work-around for this on some AOs is to use <code>&#8211;audio-exclusive=yes</code> to circumvent the system mixer entirely.</p>
<dt>Warning</p>
<dd>Using <code>auto</code> can cause issues when using audio over HDMI. The OS will typically report all channel layouts that _can_ go over HDMI, even if the receiver does not support them. If a receiver gets an unsupported channel layout, random things can happen, such as dropping the additional channels, or adding noise. </p>
<p> You are recommended to set an explicit whitelist of the layouts you want. For example, most A/V receivers connected via HDMI and that can do 7.1 would be served by: <code>&#8211;audio-channels=7.1,5.1,stereo</code></p>
<dt><code>&#8211;audio-display=&lt;no|embedded-first|external-first&gt;</code></p>
<dd>Determines whether to display cover art when playing audio files and with what priority. It will display the first image found, and additional images are available as video tracks.</p>
<dt><code>no</code></p>
<dd>Disable display of video entirely when playing audio files.</p>
<dt><code>embedded-first</code></p>
<dd>Display embedded images and external cover art, giving priority to embedded images (default).</p>
<dt><code>external-first</code></p>
<dd>Display embedded images and external cover art, giving priority to external files. </p>
<p> This option has no influence on files with normal video tracks.</p>
<dt><code>&#8211;audio-files=&lt;files&gt;</code></p>
<dd>Play audio from an external file while viewing a video. </p>
<p> This is a path list option. See <i>List Options</i> for details.</p>
<dt><code>&#8211;audio-file=&lt;file&gt;</code></p>
<dd>CLI/config file only alias for <code>&#8211;audio-files-append</code>. Each use of this option will add a new audio track. The details are similar to how <code>&#8211;sub-file</code> works.</p>
<dt><code>&#8211;audio-format=&lt;format&gt;</code></p>
<dd>Select the sample format used for output from the audio filter layer to the sound card. The values that <code>&lt;format&gt;</code> can adopt are listed below in the description of the <code>format</code> audio filter.</p>
<dt><code>&#8211;audio-samplerate=&lt;Hz&gt;</code></p>
<dd>Select the output sample rate to be used (of course sound cards have limits on this). If the sample frequency selected is different from that of the current media, the lavrresample audio filter will be inserted into the audio filter layer to compensate for the difference.</p>
<dt><code>&#8211;gapless-audio=&lt;no|yes|weak&gt;</code></p>
<dd>Try to play consecutive audio files with no silence or disruption at the point of file change. Default: <code>weak</code>.</p>
<dt><code>no</code></p>
<dd>Disable gapless audio.</p>
<dt><code>yes</code></p>
<dd>The audio device is opened using parameters chosen for the first file played and is then kept open for gapless playback. This means that if the first file for example has a low sample rate, then the following files may get resampled to the same low sample rate, resulting in reduced sound quality. If you play files with different parameters, consider using options such as <code>&#8211;audio-samplerate</code> and <code>&#8211;audio-format</code> to explicitly select what the shared output format will be.</p>
<dt><code>weak</code></p>
<dd>Normally, the audio device is kept open (using the format it was first initialized with). If the audio format the decoder output changes, the audio device is closed and reopened. This means that you will normally get gapless audio with files that were encoded using the same settings, but might not be gapless in other cases. The exact conditions under which the audio device is kept open is an implementation detail, and can change from version to version. Currently, the device is kept even if the sample format changes, but the sample formats are convertible. If video is still going on when there is still audio, trying to use gapless is also explicitly given up. </p>
<p> <code>NOTE:</code> This feature is implemented in a simple manner and relies on audio output device buffering to continue playback while moving from one file to another. If playback of the new file starts slowly, for example because it is played from a remote network location or because you have specified cache settings that require time for the initial cache fill, then the buffered audio may run out before playback of the new file can start.</p>
<dt><code>&#8211;initial-audio-sync</code>, <code>&#8211;no-initial-audio-sync</code></p>
<dd>When starting a video file or after events such as seeking, mpv will by default modify the audio stream to make it start from the same timestamp as video, by either inserting silence at the start or cutting away the first samples. Disabling this option makes the player behave like older mpv versions did: video and audio are both started immediately even if their start timestamps differ, and then video timing is gradually adjusted if necessary to reach correct synchronization later.</p>
<dt><code>&#8211;volume-max=&lt;100.0-1000.0&gt;</code>, <code>&#8211;softvol-max=&lt;&#8230;&gt;</code></p>
<dd>Set the maximum amplification level in percent (default: 130). A value of 130 will allow you to adjust the volume up to about double the normal level. </p>
<p> <code>&#8211;softvol-max</code> is a deprecated alias and should not be used.</p>
<dt><code>&#8211;audio-file-auto=&lt;no|exact|fuzzy|all&gt;</code>, <code>&#8211;no-audio-file-auto</code></p>
<dd>Load additional audio files matching the video filename. The parameter specifies how external audio files are matched.</p>
<dt><code>no</code></p>
<dd>Don&#8217;t automatically load external audio files (default).</p>
<dt><code>exact</code></p>
<dd>Load the media filename with audio file extension.</p>
<dt><code>fuzzy</code></p>
<dd>Load all audio files containing the media filename.</p>
<dt><code>all</code></p>
<dd>Load all audio files in the current and <code>&#8211;audio-file-paths</code> directories.</p>
<dt><code>&#8211;audio-file-paths=&lt;path1:path2:&#8230;&gt;</code></p>
<dd>Equivalent to <code>&#8211;sub-file-paths</code> option, but for auto-loaded audio files. </p>
<p> This is a path list option. See <i>List Options</i> for details.</p>
<dt><code>&#8211;audio-client-name=&lt;name&gt;</code></p>
<dd>The application name the player reports to the audio API. Can be useful if you want to force a different audio profile (e.g. with PulseAudio), or to set your own application name when using libmpv.</p>
<dt><code>&#8211;audio-buffer=&lt;seconds&gt;</code></p>
<dd>Set the audio output minimum buffer. The audio device might actually create a larger buffer if it pleases. If the device creates a smaller buffer, additional audio is buffered in an additional software buffer. </p>
<p> Making this larger will make soft-volume and other filters react slower, introduce additional issues on playback speed change, and block the player on audio format changes. A smaller buffer might lead to audio dropouts. </p>
<p> This option should be used for testing only. If a non-default value helps significantly, the mpv developers should be contacted. </p>
<p> Default: 0.2 (200 ms).</p>
<dt><code>&#8211;audio-stream-silence=&lt;yes|no&gt;</code></p>
<dd>Cash-grab consumer audio hardware (such as A/V receivers) often ignore initial audio sent over HDMI. This can happen every time audio over HDMI is stopped and resumed. In order to compensate for this, you can enable this option to not to stop and restart audio on seeks, and fill the gaps with silence. Likewise, when pausing playback, audio is not stopped, and silence is played while paused. Note that if no audio track is selected, the audio device will still be closed immediately. </p>
<p> Not all AOs support this.</p>
<dt>Warning</p>
<dd>This modifies certain subtle player behavior, like A/V-sync and underrun handling. Enabling this option is strongly discouraged.</p>
<dt><code>&#8211;audio-wait-open=&lt;secs&gt;</code></p>
<dd>This makes sense for use with <code>&#8211;audio-stream-silence=yes</code>. If this option is given, the player will wait for the given amount of seconds after opening the audio device before sending actual audio data to it. Useful if your expensive hardware discards the first 1 or 2 seconds of audio data sent to it. If <code>&#8211;audio-stream-silence=yes</code> is not set, this option will likely just waste time.</dl>
<h3>Subtitles</h3>
<p><code>NOTE:</code> Changing styling and position does not work with all subtitles. Image-based subtitles (DVD, Bluray/PGS, DVB) cannot changed for fundamental reasons. Subtitles in ASS format are normally not changed intentionally, but overriding them can be controlled with <code>&#8211;sub-ass-override</code>. </p>
<p> Previously some options working on text subtitles were called <code>&#8211;sub-text-*</code>, they are now named <code>&#8211;sub-*</code>, and those specifically for ASS have been renamed from <code>&#8211;ass-*</code> to <code>&#8211;sub-ass-*</code>. They are now all in this section.</p>
<dl COMPACT>
<dt><code>&#8211;sub-demuxer=&lt;[+]name&gt;</code></p>
<dd>Force subtitle demuxer type for <code>&#8211;sub-file</code>. Give the demuxer name as printed by <code>&#8211;sub-demuxer=help</code>.</p>
<dt><code>&#8211;sub-delay=&lt;sec&gt;</code></p>
<dd>Delays subtitles by <code>&lt;sec&gt;</code> seconds. Can be negative.</p>
<dt><code>&#8211;sub-files=&lt;file-list&gt;</code>, <code>&#8211;sub-file=&lt;filename&gt;</code></p>
<dd>Add a subtitle file to the list of external subtitles. </p>
<p> If you use <code>&#8211;sub-file</code> only once, this subtitle file is displayed by default. </p>
<p> If <code>&#8211;sub-file</code> is used multiple times, the subtitle to use can be switched at runtime by cycling subtitle tracks. It&#8217;s possible to show two subtitles at once: use <code>&#8211;sid</code> to select the first subtitle index, and <code>&#8211;secondary-sid</code> to select the second index. (The index is printed on the terminal output after the <code>&#8211;sid=</code> in the list of streams.) </p>
<p> <code>&#8211;sub-files</code> is a path list option (see <i>List Options</i> for details), and can take multiple file names separated by <code>:</code> (Unix) or <code>;</code> (Windows), while <code>&#8211;sub-file</code> takes a single filename, but can be used multiple times to add multiple files. Technically, <code>&#8211;sub-file</code> is a CLI/config file only alias for <code>&#8211;sub-files-append</code>.</p>
<dt><code>&#8211;secondary-sid=&lt;ID|auto|no&gt;</code></p>
<dd>Select a secondary subtitle stream. This is similar to <code>&#8211;sid</code>. If a secondary subtitle is selected, it will be rendered as toptitle (i.e. on the top of the screen) alongside the normal subtitle, and provides a way to render two subtitles at once. </p>
<p> There are some caveats associated with this feature. For example, bitmap subtitles will always be rendered in their usual position, so selecting a bitmap subtitle as secondary subtitle will result in overlapping subtitles. Secondary subtitles are never shown on the terminal if video is disabled. </p>
<p> <code>NOTE:</code> Styling and interpretation of any formatting tags is disabled for the secondary subtitle. Internally, the same mechanism as <code>&#8211;no-sub-ass</code> is used to strip the styling. </p>
<p> <code>NOTE:</code> If the main subtitle stream contains formatting tags which display the subtitle at the top of the screen, it will overlap with the secondary subtitle. To prevent this, you could use <code>&#8211;no-sub-ass</code> to disable styling in the main subtitle stream.</p>
<dt><code>&#8211;sub-scale=&lt;0-100&gt;</code></p>
<dd>Factor for the text subtitle font size (default: 1). </p>
<p> <code>NOTE:</code> This affects ASS subtitles as well, and may lead to incorrect subtitle rendering. Use with care, or use <code>&#8211;sub-font-size</code> instead.</p>
<dt><code>&#8211;sub-scale-by-window=&lt;yes|no&gt;</code></p>
<dd>Whether to scale subtitles with the window size (default: yes). If this is disabled, changing the window size won&#8217;t change the subtitle font size. </p>
<p> Like <code>&#8211;sub-scale</code>, this can break ASS subtitles.</p>
<dt><code>&#8211;sub-scale-with-window=&lt;yes|no&gt;</code></p>
<dd>Make the subtitle font size relative to the window, instead of the video. This is useful if you always want the same font size, even if the video doesn&#8217;t cover the window fully, e.g. because screen aspect and window aspect mismatch (and the player adds black bars). </p>
<p> Default: yes. </p>
<p> This option is misnamed. The difference to the confusingly similar sounding option <code>&#8211;sub-scale-by-window</code> is that <code>&#8211;sub-scale-with-window</code> still scales with the approximate window size, while the other option disables this scaling. </p>
<p> Affects plain text subtitles only (or ASS if <code>&#8211;sub-ass-override</code> is set high enough).</p>
<dt><code>&#8211;sub-ass-scale-with-window=&lt;yes|no&gt;</code></p>
<dd>Like <code>&#8211;sub-scale-with-window</code>, but affects subtitles in ASS format only. Like <code>&#8211;sub-scale</code>, this can break ASS subtitles. </p>
<p> Default: no.</p>
<dt><code>&#8211;embeddedfonts=&lt;yes|no&gt;</code></p>
<dd>Use fonts embedded in Matroska container files and ASS scripts (default: yes). These fonts can be used for SSA/ASS subtitle rendering.</p>
<dt><code>&#8211;sub-pos=&lt;0-150&gt;</code></p>
<dd>Specify the position of subtitles on the screen. The value is the vertical position of the subtitle in % of the screen height. 100 is the original position, which is often not the absolute bottom of the screen, but with some margin between the bottom and the subtitle. Values above 100 move the subtitle further down.</p>
<dt>Warning</p>
<dd>Text subtitles (as opposed to image subtitles) may be cut off if the value of the option is above 100. This is a libass restriction. </p>
<p> This affects ASS subtitles as well, and may lead to incorrect subtitle rendering in addition to the problem above. </p>
<p> Using <code>&#8211;sub-margin-y</code> can achieve this in a better way.</p>
<dt><code>&#8211;sub-speed=&lt;0.1-10.0&gt;</code></p>
<dd>Multiply the subtitle event timestamps with the given value. Can be used to fix the playback speed for frame-based subtitle formats. Affects text subtitles only.</p>
<dt>Example</p>
<dd><code>&#8211;sub-speed=25/23.976</code> plays frame based subtitles which have been loaded assuming a framerate of 23.976 at 25 FPS.</p>
<dt><code>&#8211;sub-ass-force-style=&lt;[Style.]Param=Value[,&#8230;]&gt;</code></p>
<dd>Override some style or script info parameters. </p>
<p> This is a string list option. See <i>List Options</i> for details.</p>
<dt>Examples</p>
<dd>
<dt>&bull;</p>
<dd><code>&#8211;sub-ass-force-style=FontName=Arial,Default.Bold=1</code></p>
<dt>&bull;</p>
<dd><code>&#8211;sub-ass-force-style=PlayResY=768</code> </p>
<p> <code>NOTE:</code> Using this option may lead to incorrect subtitle rendering.</p>
<dt><code>&#8211;sub-ass-hinting=&lt;none|light|normal|native&gt;</code></p>
<dd>Set font hinting type. &lt;type&gt; can be:</p>
<dt><code>none</code></p>
<dd>no hinting (default)</p>
<dt><code>light</code></p>
<dd>FreeType autohinter, light mode</p>
<dt><code>normal</code></p>
<dd>FreeType autohinter, normal mode</p>
<dt><code>native</code></p>
<dd>font native hinter</p>
<dt>Warning</p>
<dd>Enabling hinting can lead to mispositioned text (in situations it&#8217;s supposed to match up video background), or reduce the smoothness of animations with some badly authored ASS scripts. It is recommended to not use this option, unless really needed.</p>
<dt><code>&#8211;sub-ass-line-spacing=&lt;value&gt;</code></p>
<dd>Set line spacing value for SSA/ASS renderer.</p>
<dt><code>&#8211;sub-ass-shaper=&lt;simple|complex&gt;</code></p>
<dd>Set the text layout engine used by libass.</p>
<dt><code>simple</code></p>
<dd>uses Fribidi only, fast, doesn&#8217;t render some languages correctly</p>
<dt><code>complex</code></p>
<dd>uses HarfBuzz, slower, wider language support </p>
<p> <code>complex</code> is the default. If libass hasn&#8217;t been compiled against HarfBuzz, libass silently reverts to <code>simple</code>.</p>
<dt><code>&#8211;sub-ass-styles=&lt;filename&gt;</code></p>
<dd>Load all SSA/ASS styles found in the specified file and use them for rendering text subtitles. The syntax of the file is exactly like the <code>[V4 Styles]</code> / <code>[V4+ Styles]</code> section of SSA/ASS. </p>
<p> <code>NOTE:</code> Using this option may lead to incorrect subtitle rendering.</p>
<dt><code>&#8211;sub-ass-override=&lt;yes|no|force|scale|strip&gt;</code></p>
<dd>Control whether user style overrides should be applied. Note that all of these overrides try to be somewhat smart about figuring out whether or not a subtitle is considered a &quot;sign&quot;.</p>
<dt><code>no</code></p>
<dd>Render subtitles as specified by the subtitle scripts, without overrides.</p>
<dt><code>yes</code></p>
<dd>Apply all the <code>&#8211;sub-ass-*</code> style override options. Changing the default for any of these options can lead to incorrect subtitle rendering (default).</p>
<dt><code>force</code></p>
<dd>Like <code>yes</code>, but also force all <code>&#8211;sub-*</code> options. Can break rendering easily.</p>
<dt><code>scale</code></p>
<dd>Like <code>yes</code>, but also apply <code>&#8211;sub-scale</code>.</p>
<dt><code>strip</code></p>
<dd>Radically strip all ASS tags and styles from the subtitle. This is equivalent to the old <code>&#8211;no-ass</code> / <code>&#8211;no-sub-ass</code> options. </p>
<p> This also controls some bitmap subtitle overrides, as well as HTML tags in formats like SRT, despite the name of the option.</p>
<dt><code>&#8211;sub-ass-force-margins</code></p>
<dd>Enables placing toptitles and subtitles in black borders when they are available, if the subtitles are in the ASS format. </p>
<p> Default: no.</p>
<dt><code>&#8211;sub-use-margins</code></p>
<dd>Enables placing toptitles and subtitles in black borders when they are available, if the subtitles are in a plain text format (or ASS if <code>&#8211;sub-ass-override</code> is set high enough). </p>
<p> Default: yes. </p>
<p> Renamed from <code>&#8211;sub-ass-use-margins</code>. To place ASS subtitles in the borders too (like the old option did), also add <code>&#8211;sub-ass-force-margins</code>.</p>
<dt><code>&#8211;sub-ass-vsfilter-aspect-compat=&lt;yes|no&gt;</code></p>
<dd>Stretch SSA/ASS subtitles when playing anamorphic videos for compatibility with traditional VSFilter behavior. This switch has no effect when the video is stored with square pixels. </p>
<p> The renderer historically most commonly used for the SSA/ASS subtitle formats, VSFilter, had questionable behavior that resulted in subtitles being stretched too if the video was stored in anamorphic format that required scaling for display. This behavior is usually undesirable and newer VSFilter versions may behave differently. However, many existing scripts compensate for the stretching by modifying things in the opposite direction. Thus, if such scripts are displayed &quot;correctly&quot;, they will not appear as intended. This switch enables emulation of the old VSFilter behavior (undesirable but expected by many existing scripts). </p>
<p> Enabled by default.</p>
<dt><code>&#8211;sub-ass-vsfilter-blur-compat=&lt;yes|no&gt;</code></p>
<dd>Scale <code>lur</code> tags by video resolution instead of script resolution (enabled by default). This is bug in VSFilter, which according to some, can&#8217;t be fixed anymore in the name of compatibility. </p>
<p> Note that this uses the actual video resolution for calculating the offset scale factor, not what the video filter chain or the video output use.</p>
<dt><code>&#8211;sub-ass-vsfilter-color-compat=&lt;basic|full|force-601|no&gt;</code></p>
<dd>Mangle colors like (xy-)vsfilter do (default: basic). Historically, VSFilter was not color space aware. This was no problem as long as the color space used for SD video (BT.601) was used. But when everything switched to HD (BT.709), VSFilter was still converting RGB colors to BT.601, rendered them into the video frame, and handled the frame to the video output, which would use BT.709 for conversion to RGB. The result were mangled subtitle colors. Later on, bad hacks were added on top of the ASS format to control how colors are to be mangled.</p>
<dt><code>basic</code></p>
<dd>Handle only BT.601-&gt;BT.709 mangling, if the subtitles seem to indicate that this is required (default).</p>
<dt><code>full</code></p>
<dd>Handle the full <code>YCbCr Matrix</code> header with all video color spaces supported by libass and mpv. This might lead to bad breakages in corner cases and is not strictly needed for compatibility (hopefully), which is why this is not default.</p>
<dt><code>force-601</code></p>
<dd>Force BT.601-&gt;BT.709 mangling, regardless of subtitle headers or video color space.</p>
<dt><code>no</code></p>
<dd>Disable color mangling completely. All colors are RGB. </p>
<p> Choosing anything other than <code>no</code> will make the subtitle color depend on the video color space, and it&#8217;s for example in theory not possible to reuse a subtitle script with another video file. The <code>&#8211;sub-ass-override</code> option doesn&#8217;t affect how this option is interpreted.</p>
<dt><code>&#8211;stretch-dvd-subs=&lt;yes|no&gt;</code></p>
<dd>Stretch DVD subtitles when playing anamorphic videos for better looking fonts on badly mastered DVDs. This switch has no effect when the video is stored with square pixels &#8211; which for DVD input cannot be the case though. </p>
<p> Many studios tend to use bitmap fonts designed for square pixels when authoring DVDs, causing the fonts to look stretched on playback on DVD players. This option fixes them, however at the price of possibly misaligning some subtitles (e.g. sign translations). </p>
<p> Disabled by default.</p>
<dt><code>&#8211;stretch-image-subs-to-screen=&lt;yes|no&gt;</code></p>
<dd>Stretch DVD and other image subtitles to the screen, ignoring the video margins. This has a similar effect as <code>&#8211;sub-use-margins</code> for text subtitles, except that the text itself will be stretched, not only just repositioned. (At least in general it is unavoidable, as an image bitmap can in theory consist of a single bitmap covering the whole screen, and the player won&#8217;t know where exactly the text parts are located.) </p>
<p> This option does not display subtitles correctly. Use with care. </p>
<p> Disabled by default.</p>
<dt><code>&#8211;image-subs-video-resolution=&lt;yes|no&gt;</code></p>
<dd>Override the image subtitle resolution with the video resolution (default: no). Normally, the subtitle canvas is fit into the video canvas (e.g. letterboxed). Setting this option uses the video size as subtitle canvas size. Can be useful to test broken subtitles, which often happen when the video was trancoded, while attempting to keep the old subtitles.</p>
<dt><code>&#8211;sub-ass</code>, <code>&#8211;no-sub-ass</code></p>
<dd>Render ASS subtitles natively (enabled by default). </p>
<p> <code>NOTE:</code> This has been deprecated by <code>&#8211;sub-ass-override=strip</code>. You also may need <code>&#8211;embeddedfonts=no</code> to get the same behavior. Also, using <code>&#8211;sub-ass-override=style</code> should give better results without breaking subtitles too much. </p>
<p> If <code>&#8211;no-sub-ass</code> is specified, all tags and style declarations are stripped and ignored on display. The subtitle renderer uses the font style as specified by the <code>&#8211;sub-</code> options instead. </p>
<p> <code>NOTE:</code> Using <code>&#8211;no-sub-ass</code> may lead to incorrect or completely broken rendering of ASS/SSA subtitles. It can sometimes be useful to forcibly override the styling of ASS subtitles, but should be avoided in general.</p>
<dt><code>&#8211;sub-auto=&lt;no|exact|fuzzy|all&gt;</code>, <code>&#8211;no-sub-auto</code></p>
<dd>Load additional subtitle files matching the video filename. The parameter specifies how external subtitle files are matched. <code>exact</code> is enabled by default.</p>
<dt><code>no</code></p>
<dd>Don&#8217;t automatically load external subtitle files.</p>
<dt><code>exact</code></p>
<dd>Load the media filename with subtitle file extension and possibly language suffixes (default).</p>
<dt><code>fuzzy</code></p>
<dd>Load all subs containing the media filename.</p>
<dt><code>all</code></p>
<dd>Load all subs in the current and <code>&#8211;sub-file-paths</code> directories.</p>
<dt><code>&#8211;sub-codepage=&lt;codepage&gt;</code></p>
<dd>You can use this option to specify the subtitle codepage. uchardet will be used to guess the charset. (If mpv was not compiled with uchardet, then <code>utf-8</code> is the effective default.) </p>
<p> The default value for this option is <code>auto</code>, which enables autodetection. </p>
<p> The following steps are taken to determine the final codepage, in order:</p>
<dt>&bull;</p>
<dd>if the specific codepage has a <code>+</code>, use that codepage</p>
<dt>&bull;</p>
<dd>if the data looks like UTF-8, assume it is UTF-8</p>
<dt>&bull;</p>
<dd>if <code>&#8211;sub-codepage</code> is set to a specific codepage, use that</p>
<dt>&bull;</p>
<dd>run uchardet, and if successful, use that</p>
<dt>&bull;</p>
<dd>otherwise, use <code>UTF-8-BROKEN</code></p>
<dt>Examples</p>
<dd>
<dt>&bull;</p>
<dd><code>&#8211;sub-codepage=latin2</code> Use Latin 2 if input is not UTF-8.</p>
<dt>&bull;</p>
<dd><code>&#8211;sub-codepage=+cp1250</code> Always force recoding to cp1250. </p>
<p> The pseudo codepage <code>UTF-8-BROKEN</code> is used internally. If it&#8217;s set, subtitles are interpreted as UTF-8 with &quot;Latin 1&quot; as fallback for bytes which are not valid UTF-8 sequences. iconv is never involved in this mode. </p>
<p> This option changed in mpv 0.23.0. Support for the old syntax was fully removed in mpv 0.24.0. </p>
<p> <code>NOTE:</code> This works for text subtitle files only. Other types of subtitles (in particular subtitles in mkv files) are always assumed to be UTF-8.</p>
<dt><code>&#8211;sub-fix-timing=&lt;yes|no&gt;</code></p>
<dd>Adjust subtitle timing is to remove minor gaps or overlaps between subtitles (if the difference is smaller than 210 ms, the gap or overlap is removed).</p>
<dt><code>&#8211;sub-forced-only=&lt;auto|yes|no&gt;</code></p>
<dd>Display only forced subtitles for the DVD subtitle stream selected by e.g. <code>&#8211;slang</code> (default: <code>auto</code>). When set to <code>auto</code>, enabled when the <code>&#8211;subs-with-matching-audio</code> option is on and a non-forced stream is selected. Enabling this will hide all subtitles in streams that don&#8217;t make a distinction between forced and unforced events within a stream.</p>
<dt><code>&#8211;sub-fps=&lt;rate&gt;</code></p>
<dd>Specify the framerate of the subtitle file (default: video fps). Affects text subtitles only. </p>
<p> <code>NOTE:</code> <code>&lt;rate&gt;</code> &gt; video fps speeds the subtitles up for frame-based subtitle files and slows them down for time-based ones. </p>
<p> See also: <code>&#8211;sub-speed</code>.</p>
<dt><code>&#8211;sub-gauss=&lt;0.0-3.0&gt;</code></p>
<dd>Apply Gaussian blur to image subtitles (default: 0). This can help to make pixelated DVD/Vobsubs look nicer. A value other than 0 also switches to software subtitle scaling. Might be slow. </p>
<p> <code>NOTE:</code> Never applied to text subtitles.</p>
<dt><code>&#8211;sub-gray</code></p>
<dd>Convert image subtitles to grayscale. Can help to make yellow DVD/Vobsubs look nicer. </p>
<p> <code>NOTE:</code> Never applied to text subtitles.</p>
<dt><code>&#8211;sub-paths=&lt;path1:path2:&#8230;&gt;</code></p>
<dd>Deprecated, use <code>&#8211;sub-file-paths</code>.</p>
<dt><code>&#8211;sub-file-paths=&lt;path-list&gt;</code></p>
<dd>Specify extra directories to search for subtitles matching the video. Multiple directories can be separated by &quot;:&quot; (&quot;;&quot; on Windows). Paths can be relative or absolute. Relative paths are interpreted relative to video file directory. If the file is a URL, only absolute paths and <code>sub</code> configuration subdirectory will be scanned.</p>
<dt>Example</p>
<dd>Assuming that <code>/path/to/video/video.avi</code> is played and <code>&#8211;sub-file-paths=sub:subtitles</code> is specified, mpv searches for subtitle files in these directories:</p>
<dt>&bull;</p>
<dd><code>/path/to/video/</code></p>
<dt>&bull;</p>
<dd><code>/path/to/video/sub/</code></p>
<dt>&bull;</p>
<dd><code>/path/to/video/subtitles/</code></p>
<dt>&bull;</p>
<dd>the <code>sub</code> configuration subdirectory (usually <code>~/.config/mpv/sub/</code>) </p>
<p> This is a path list option. See <i>List Options</i> for details.</p>
<dt><code>&#8211;sub-visibility</code>, <code>&#8211;no-sub-visibility</code></p>
<dd>Can be used to disable display of subtitles, but still select and decode them.</p>
<dt><code>&#8211;secondary-sub-visibility</code>, <code>&#8211;no-secondary-sub-visibility</code></p>
<dd>Can be used to disable display of secondary subtitles, but still select and decode them. </p>
<p> <code>NOTE:</code> If <code>&#8211;sub-visibility=no</code>, secondary subtitles are hidden regardless of <code>&#8211;secondary-sub-visibility</code>.</p>
<dt><code>&#8211;sub-clear-on-seek</code></p>
<dd>(Obscure, rarely useful.) Can be used to play broken mkv files with duplicate ReadOrder fields. ReadOrder is the first field in a Matroska-style ASS subtitle packets. It should be unique, and libass uses it for fast elimination of duplicates. This option disables caching of subtitles across seeks, so after a seek libass can&#8217;t eliminate subtitle packets with the same ReadOrder as earlier packets.</p>
<dt><code>&#8211;teletext-page=&lt;1-999&gt;</code></p>
<dd>This works for <code>dvb_teletext</code> subtitle streams, and if FFmpeg has been compiled with support for it.</p>
<dt><code>&#8211;sub-past-video-end</code></p>
<dd>After the last frame of video, if this option is enabled, subtitles will continue to update based on audio timestamps. Otherwise, the subtitles for the last video frame will stay onscreen. </p>
<p> Default: disabled</p>
<dt><code>&#8211;sub-font=&lt;name&gt;</code></p>
<dd>Specify font to use for subtitles that do not themselves specify a particular font. The default is <code>sans-serif</code>.</p>
<dt>Examples</p>
<dd>
<dt>&bull;</p>
<dd><code>&#8211;sub-font=&#8217;Bitstream Vera Sans&#8217;</code></p>
<dt>&bull;</p>
<dd><code>&#8211;sub-font=&#8217;Comic Sans MS&#8217;</code> </p>
<p> <code>NOTE:</code> The <code>&#8211;sub-font</code> option (and many other style related <code>&#8211;sub-</code> options) are ignored when ASS-subtitles are rendered, unless the <code>&#8211;no-sub-ass</code> option is specified. </p>
<p> This used to support fontconfig patterns. Starting with libass 0.13.0, this stopped working.</p>
<dt><code>&#8211;sub-font-size=&lt;size&gt;</code></p>
<dd>Specify the sub font size. The unit is the size in scaled pixels at a window height of 720. The actual pixel size is scaled with the window height: if the window height is larger or smaller than 720, the actual size of the text increases or decreases as well. </p>
<p> Default: 55.</p>
<dt><code>&#8211;sub-back-color=&lt;color&gt;</code></p>
<dd>See <code>&#8211;sub-color</code>. Color used for sub text background. You can use <code>&#8211;sub-shadow-offset</code> to change its size relative to the text.</p>
<dt><code>&#8211;sub-blur=&lt;0..20.0&gt;</code></p>
<dd>Gaussian blur factor. 0 means no blur applied (default).</p>
<dt><code>&#8211;sub-bold=&lt;yes|no&gt;</code></p>
<dd>Format text on bold.</p>
<dt><code>&#8211;sub-italic=&lt;yes|no&gt;</code></p>
<dd>Format text on italic.</p>
<dt><code>&#8211;sub-border-color=&lt;color&gt;</code></p>
<dd>See <code>&#8211;sub-color</code>. Color used for the sub font border. </p>
<p> <code>NOTE:</code> ignored when <code>&#8211;sub-back-color</code> is specified (or more exactly: when that option is not set to completely transparent).</p>
<dt><code>&#8211;sub-border-size=&lt;size&gt;</code></p>
<dd>Size of the sub font border in scaled pixels (see <code>&#8211;sub-font-size</code> for details). A value of 0 disables borders. </p>
<p> Default: 3.</p>
<dt><code>&#8211;sub-color=&lt;color&gt;</code></p>
<dd>Specify the color used for unstyled text subtitles. </p>
<p> The color is specified in the form <code>r/g/b</code>, where each color component is specified as number in the range 0.0 to 1.0. It&#8217;s also possible to specify the transparency by using <code>r/g/b/a</code>, where the alpha value 0 means fully transparent, and 1.0 means opaque. If the alpha component is not given, the color is 100% opaque. </p>
<p> Passing a single number to the option sets the sub to gray, and the form <code>gray/a</code> lets you specify alpha additionally.</p>
<dt>Examples</p>
<dd>
<dt>&bull;</p>
<dd><code>&#8211;sub-color=1.0/0.0/0.0</code> set sub to opaque red</p>
<dt>&bull;</p>
<dd><code>&#8211;sub-color=1.0/0.0/0.0/0.75</code> set sub to opaque red with 75% alpha</p>
<dt>&bull;</p>
<dd><code>&#8211;sub-color=0.5/0.75</code> set sub to 50% gray with 75% alpha </p>
<p> Alternatively, the color can be specified as a RGB hex triplet in the form <code>#RRGGBB</code>, where each 2-digit group expresses a color value in the range 0 (<code>00</code>) to 255 (<code>FF</code>). For example, <code>#FF0000</code> is red. This is similar to web colors. Alpha is given with <code>#AARRGGBB</code>.</p>
<dt>Examples</p>
<dd>
<dt>&bull;</p>
<dd><code>&#8211;sub-color=&#8217;#FF0000&#8242;</code> set sub to opaque red</p>
<dt>&bull;</p>
<dd><code>&#8211;sub-color=&#8217;#C0808080&#8242;</code> set sub to 50% gray with 75% alpha</p>
<dt><code>&#8211;sub-margin-x=&lt;size&gt;</code></p>
<dd>Left and right screen margin for the subs in scaled pixels (see <code>&#8211;sub-font-size</code> for details). </p>
<p> This option specifies the distance of the sub to the left, as well as at which distance from the right border long sub text will be broken. </p>
<p> Default: 25.</p>
<dt><code>&#8211;sub-margin-y=&lt;size&gt;</code></p>
<dd>Top and bottom screen margin for the subs in scaled pixels (see <code>&#8211;sub-font-size</code> for details). </p>
<p> This option specifies the vertical margins of unstyled text subtitles. If you just want to raise the vertical subtitle position, use <code>&#8211;sub-pos</code>. </p>
<p> Default: 22.</p>
<dt><code>&#8211;sub-align-x=&lt;left|center|right&gt;</code></p>
<dd>Control to which corner of the screen text subtitles should be aligned to (default: <code>center</code>). </p>
<p> Never applied to ASS subtitles, except in <code>&#8211;no-sub-ass</code> mode. Likewise, this does not apply to image subtitles.</p>
<dt><code>&#8211;sub-align-y=&lt;top|center|bottom&gt;</code></p>
<dd>Vertical position (default: <code>bottom</code>). Details see <code>&#8211;sub-align-x</code>.</p>
<dt><code>&#8211;sub-justify=&lt;auto|left|center|right&gt;</code></p>
<dd>Control how multi line subs are justified irrespective of where they are aligned (default: <code>auto</code> which justifies as defined by <code>&#8211;sub-align-y</code>). Left justification is recommended to make the subs easier to read as it is easier for the eyes.</p>
<dt><code>&#8211;sub-ass-justify=&lt;yes|no&gt;</code></p>
<dd>Applies justification as defined by <code>&#8211;sub-justify</code> on ASS subtitles if <code>&#8211;sub-ass-override</code> is not set to <code>no</code>. Default: <code>no</code>.</p>
<dt><code>&#8211;sub-shadow-color=&lt;color&gt;</code></p>
<dd>See <code>&#8211;sub-color</code>. Color used for sub text shadow.</p>
<dt><code>&#8211;sub-shadow-offset=&lt;size&gt;</code></p>
<dd>Displacement of the sub text shadow in scaled pixels (see <code>&#8211;sub-font-size</code> for details). A value of 0 disables shadows. </p>
<p> Default: 0.</p>
<dt><code>&#8211;sub-spacing=&lt;size&gt;</code></p>
<dd>Horizontal sub font spacing in scaled pixels (see <code>&#8211;sub-font-size</code> for details). This value is added to the normal letter spacing. Negative values are allowed. </p>
<p> Default: 0.</p>
<dt><code>&#8211;sub-filter-sdh=&lt;yes|no&gt;</code></p>
<dd>Applies filter removing subtitle additions for the deaf or hard-of-hearing (SDH). This is intended for English, but may in part work for other languages too. The intention is that it can be always enabled so may not remove all parts added. It removes speaker labels (like MAN:), upper case text in parentheses and any text in brackets. </p>
<p> Default: <code>no</code>.</p>
<dt><code>&#8211;sub-filter-sdh-harder=&lt;yes|no&gt;</code></p>
<dd>Do harder SDH filtering (if enabled by <code>&#8211;sub-filter-sdh</code>). Will also remove speaker labels and text within parentheses using both lower and upper case letters. </p>
<p> Default: <code>no</code>.</p>
<dt><code>&#8211;sub-filter-regex-&#8230;=&#8230;</code></p>
<dd>Set a list of regular expressions to match on text subtitles, and remove any lines that match (default: empty). This is a string list option. See <i>List Options</i> for details. Normally, you should use <code>&#8211;sub-filter-regex-append=&lt;regex&gt;</code>, where each option use will append a new regular expression, without having to fight escaping problems. </p>
<p> List items are matched in order. If a regular expression matches, the process is stopped, and the subtitle line is discarded. The text matched against is, by default, the <code>Text</code> field of ASS events (if the subtitle format is different, it is always converted). This may include formatting tags. Matching is case-insensitive, but how this is done depends on the libc, and most likely works in ASCII only. It does not work on bitmap/image subtitles. Unavailable on inferior OSes (requires POSIX regex support).</p>
<dt>Example</p>
<dd><code>&#8211;sub-filter-regex-append=opensubtitles\.org</code> filters some ads. </p>
<p> Technically, using a list for matching is redundant, since you could just use a single combined regular expression. But it helps with diagnosis, ease of use, and temporarily disabling or enabling individual filters. </p>
<p> <code>WARNING:</code> This is experimental. The semantics most likely will change, and if you use this, you should be prepared to update the option later. Ideas include replacing the regexes with a very primitive and small subset of sed, or some method to control case-sensitivity.</p>
<dt><code>&#8211;sub-filter-jsre-&#8230;=&#8230;</code></p>
<dd>Same as <code>&#8211;sub-filter-regex</code> but with JavaScript regular expressions. Shares/affected-by all <code>&#8211;sub-filter-regex-*</code> control options (see below), and also experimental. Requires only JavaScript support.</p>
<dt><code>&#8211;sub-filter-regex-plain=&lt;yes|no&gt;</code></p>
<dd>Whether to first convert the ASS &quot;Text&quot; field to plain-text (default: no). This strips ASS tags and applies ASS directives, like <code>\N</code> to new-line. If the result is multi-line then the regexp anchors <code>^</code> and <code>$</code> match each line, but still any match discards all lines.</p>
<dt><code>&#8211;sub-filter-regex-warn=&lt;yes|no&gt;</code></p>
<dd>Log dropped lines with warning log level, instead of verbose (default: no). Helpful for testing.</p>
<dt><code>&#8211;sub-filter-regex-enable=&lt;yes|no&gt;</code></p>
<dd>Whether to enable regex filtering (default: yes). Note that if no regexes are added to the <code>&#8211;sub-filter-regex</code> list, setting this option to <code>yes</code> has no effect. It&#8217;s meant to easily disable or enable filtering temporarily.</p>
<dt><code>&#8211;sub-create-cc-track=&lt;yes|no&gt;</code></p>
<dd>For every video stream, create a closed captions track (default: no). The only purpose is to make the track available for selection at the start of playback, instead of creating it lazily. This applies only to <code>ATSC A53 Part 4 Closed Captions</code> (displayed by mpv as subtitle tracks using the codec <code>eia_608</code>). The CC track is marked &quot;default&quot; and selected according to the normal subtitle track selection rules. You can then use <code>&#8211;sid</code> to explicitly select the correct track too. </p>
<p> If the video stream contains no closed captions, or if no video is being decoded, the CC track will remain empty and will not show any text.</p>
<dt><code>&#8211;sub-font-provider=&lt;auto|none|fontconfig&gt;</code></p>
<dd>Which libass font provider backend to use (default: auto). <code>auto</code> will attempt to use the native font provider: fontconfig on Linux, CoreText on macOS, DirectWrite on Windows. <code>fontconfig</code> forces fontconfig, if libass was built with support (if not, it behaves like <code>none</code>). </p>
<p> The <code>none</code> font provider effectively disables system fonts. It will still attempt to use embedded fonts (unless <code>&#8211;embeddedfonts=no</code> is set; this is the same behavior as with all other font providers), <code>subfont.ttf</code> if provided, and fonts in the <code>fonts</code> sub-directory if provided. (The fallback is more strict than that of other font providers, and if a font name does not match, it may prefer not to render any text that uses the missing font.)</dl>
<h3>Window</h3>
<dl COMPACT>
<dt><code>&#8211;title=&lt;string&gt;</code></p>
<dd>Set the window title. This is used for the video window, and if possible, also sets the audio stream title. </p>
<p> Properties are expanded. (See <i>Property Expansion</i>.) </p>
<p> <code>WARNING:</code> There is a danger of this causing significant CPU usage, depending on the properties used. Changing the window title is often a slow operation, and if the title changes every frame, playback can be ruined.</p>
<dt><code>&#8211;screen=&lt;default|0-32&gt;</code></p>
<dd>In multi-monitor configurations (i.e. a single desktop that spans across multiple displays), this option tells mpv which screen to display the video on.</p>
<dt>Note (X11)</p>
<dd>This option does not work properly with all window managers. In these cases, you can try to use <code>&#8211;geometry</code> to position the window explicitly. It&#8217;s also possible that the window manager provides native features to control which screens application windows should use. </p>
<p> See also <code>&#8211;fs-screen</code>.</p>
<dt><code>&#8211;screen-name=&lt;string&gt;</code></p>
<dd>In multi-monitor configurations, this option tells mpv which screen to display the video on based on the screen name from the video backend. The same caveats in the <code>&#8211;screen</code> option also apply here. This option is ignored and does nothing if <code>&#8211;screen</code> is explicitly set.</p>
<dt><code>&#8211;fullscreen</code>, <code>&#8211;fs</code></p>
<dd>Fullscreen playback.</p>
<dt><code>&#8211;fs-screen=&lt;all|current|0-32&gt;</code></p>
<dd>In multi-monitor configurations (i.e. a single desktop that spans across multiple displays), this option tells mpv which screen to go fullscreen to. If <code>current</code> is used mpv will fallback on what the user provided with the <code>screen</code> option.</p>
<dt>Note (X11)</p>
<dd>This option works properly only with window managers which understand the EWMH <code>_NET_WM_FULLSCREEN_MONITORS</code> hint.</p>
<dt>Note (macOS)</p>
<dd><code>all</code> does not work on macOS and will behave like <code>current</code>. </p>
<p> See also <code>&#8211;screen</code>.</p>
<dt><code>&#8211;fs-screen-name=&lt;string&gt;</code></p>
<dd>In multi-monitor configurations, this option tells mpv which screen to go fullscreen to based on the screen name from the video backend. The same caveats in the <code>&#8211;fs-screen</code> option also apply here. This option is ignored and does nothing if <code>&#8211;fs-screen</code> is explicitly set.</p>
<dt><code>&#8211;keep-open=&lt;yes|no|always&gt;</code></p>
<dd>Do not terminate when playing or seeking beyond the end of the file, and there is not next file to be played (and <code>&#8211;loop</code> is not used). Instead, pause the player. When trying to seek beyond end of the file, the player will attempt to seek to the last frame. </p>
<p> Normally, this will act like <code>set pause yes</code> on EOF, unless the <code>&#8211;keep-open-pause=no</code> option is set. </p>
<p> The following arguments can be given:</p>
<dt><code>no</code></p>
<dd>If the current file ends, go to the next file or terminate. (Default.)</p>
<dt><code>yes</code></p>
<dd>Don&#8217;t terminate if the current file is the last playlist entry. Equivalent to <code>&#8211;keep-open</code> without arguments.</p>
<dt><code>always</code></p>
<dd>Like <code>yes</code>, but also applies to files before the last playlist entry. This means playback will never automatically advance to the next file. </p>
<p> <code>NOTE:</code> This option is not respected when using <code>&#8211;frames</code>. Explicitly skipping to the next file if the binding uses <code>force</code> will terminate playback as well. </p>
<p> Also, if errors or unusual circumstances happen, the player can quit anyway. </p>
<p> Since mpv 0.6.0, this doesn&#8217;t pause if there is a next file in the playlist, or the playlist is looped. Approximately, this will pause when the player would normally exit, but in practice there are corner cases in which this is not the case (e.g. <code>mpv &#8211;keep-open file.mkv /dev/null</code> will play file.mkv normally, then fail to open <code>/dev/null</code>, then exit). (In mpv 0.8.0, <code>always</code> was introduced, which restores the old behavior.)</p>
<dt><code>&#8211;keep-open-pause=&lt;yes|no&gt;</code></p>
<dd>If set to <code>no</code>, instead of pausing when <code>&#8211;keep-open</code> is active, just stop at end of file and continue playing forward when you seek backwards until end where it stops again. Default: <code>yes</code>.</p>
<dt><code>&#8211;image-display-duration=&lt;seconds|inf&gt;</code></p>
<dd>If the current file is an image, play the image for the given amount of seconds (default: 1). <code>inf</code> means the file is kept open forever (until the user stops playback manually). </p>
<p> Unlike <code>&#8211;keep-open</code>, the player is not paused, but simply continues playback until the time has elapsed. (It should not use any resources during &quot;playback&quot;.) </p>
<p> This affects image files, which are defined as having only 1 video frame and no audio. The player may recognize certain non-images as images, for example if <code>&#8211;length</code> is used to reduce the length to 1 frame, or if you seek to the last frame. </p>
<p> This option does not affect the framerate used for <code>mf://</code> or <code>&#8211;merge-files</code>. For that, use <code>&#8211;mf-fps</code> instead. </p>
<p> Setting <code>&#8211;image-display-duration</code> hides the OSC and does not track playback time on the command-line output, and also does not duplicate the image frame when encoding. To force the player into &quot;dumb mode&quot; and actually count out seconds, or to duplicate the image when encoding, you need to use <code>&#8211;demuxer=lavf &#8211;demuxer-lavf-o=loop=1</code>, and use <code>&#8211;length</code> or <code>&#8211;frames</code> to stop after a particular time.</p>
<dt><code>&#8211;force-window=&lt;yes|no|immediate&gt;</code></p>
<dd>Create a video output window even if there is no video. This can be useful when pretending that mpv is a GUI application. Currently, the window always has the size 640&#215;480, and is subject to <code>&#8211;geometry</code>, <code>&#8211;autofit</code>, and similar options. </p>
<p> <code>WARNING:</code> The window is created only after initialization (to make sure default window placement still works if the video size is different from the <code>&#8211;force-window</code> default window size). This can be a problem if initialization doesn&#8217;t work perfectly, such as when opening URLs with bad network connection, or opening broken video files. The <code>immediate</code> mode can be used to create the window always on program start, but this may cause other issues.</p>
<dt><code>&#8211;taskbar-progress</code>, <code>&#8211;no-taskbar-progress</code></p>
<dd>(Windows only) Enable/disable playback progress rendering in taskbar (Windows 7 and above). </p>
<p> Enabled by default.</p>
<dt><code>&#8211;snap-window</code></p>
<dd>(Windows only) Snap the player window to screen edges.</p>
<dt><code>&#8211;ontop</code></p>
<dd>Makes the player window stay on top of other windows. </p>
<p> On Windows, if combined with fullscreen mode, this causes mpv to be treated as exclusive fullscreen window that bypasses the Desktop Window Manager.</p>
<dt><code>&#8211;ontop-level=&lt;window|system|desktop|level&gt;</code></p>
<dd>(macOS only) Sets the level of an ontop window (default: window).</p>
<dt><code>window</code></p>
<dd>On top of all other windows.</p>
<dt><code>system</code></p>
<dd>On top of system elements like Taskbar, Menubar and Dock.</p>
<dt><code>desktop</code></p>
<dd>On top of the Dekstop behind windows and Desktop icons.</p>
<dt><code>level</code></p>
<dd>A level as integer.</p>
<dt><code>&#8211;focus-on-open</code>, <code>&#8211;no-focus-on-open</code></p>
<dd>(macOS only) Focus the video window on creation and makes it the front most window. This is on by default.</p>
<dt><code>&#8211;border</code>, <code>&#8211;no-border</code></p>
<dd>Play video with window border and decorations. Since this is on by default, use <code>&#8211;no-border</code> to disable the standard window decorations.</p>
<dt><code>&#8211;on-all-workspaces</code></p>
<dd>(X11 and macOS only) Show the video window on all virtual desktops.</p>
<dt><code>&#8211;geometry=&lt;[W[xH]][+-x+-y][/WS]&gt;</code>, <code>&#8211;geometry=&lt;x:y&gt;</code></p>
<dd>Adjust the initial window position or size. <code>W</code> and <code>H</code> set the window size in pixels. <code>x</code> and <code>y</code> set the window position, measured in pixels from the top-left corner of the screen to the top-left corner of the image being displayed. If a percentage sign (<code>%</code>) is given after the argument, it turns the value into a percentage of the screen size in that direction. Positions are specified similar to the standard X11 <code>&#8211;geometry</code> option format, in which e.g. +10-50 means &quot;place 10 pixels from the left border and 50 pixels from the lower border&quot; and &quot;&#8211;20+-10&quot; means &quot;place 20 pixels beyond the right and 10 pixels beyond the top border&quot;. A trailing <code>/</code> followed by an integer denotes on which workspace (virtual desktop) the window should appear (X11 only). </p>
<p> If an external window is specified using the <code>&#8211;wid</code> option, this option is ignored. </p>
<p> The coordinates are relative to the screen given with <code>&#8211;screen</code> for the video output drivers that fully support <code>&#8211;screen</code>. </p>
<p> <code>NOTE:</code> Generally only supported by GUI VOs. Ignored for encoding.</p>
<dt>Note (X11)</p>
<dd>This option does not work properly with all window managers.</p>
<dt>Examples</p>
<dd>
<dt><code>50:40</code></p>
<dd>Places the window at x=50, y=40.</p>
<dt><code>50%:50%</code></p>
<dd>Places the window in the middle of the screen.</p>
<dt><code>100%:100%</code></p>
<dd>Places the window at the bottom right corner of the screen.</p>
<dt><code>50%</code></p>
<dd>Sets the window width to half the screen width. Window height is set so that the window has the video aspect ratio.</p>
<dt><code>50%x50%</code></p>
<dd>Forces the window width and height to half the screen width and height. Will show black borders to compensate for the video aspect ratio (with most VOs and without <code>&#8211;no-keepaspect</code>).</p>
<dt><code>50%+10+10/2</code></p>
<dd>Sets the window to half the screen widths, and positions it 10 pixels below/left of the top left corner of the screen, on the second workspace. </p>
<p> See also <code>&#8211;autofit</code> and <code>&#8211;autofit-larger</code> for fitting the window into a given size without changing aspect ratio.</p>
<dt><code>&#8211;autofit=&lt;[W[xH]]&gt;</code></p>
<dd>Set the initial window size to a maximum size specified by <code>WxH</code>, without changing the window&#8217;s aspect ratio. The size is measured in pixels, or if a number is followed by a percentage sign (<code>%</code>), in percents of the screen size. </p>
<p> This option never changes the aspect ratio of the window. If the aspect ratio mismatches, the window&#8217;s size is reduced until it fits into the specified size. </p>
<p> Window position is not taken into account, nor is it modified by this option (the window manager still may place the window differently depending on size). Use <code>&#8211;geometry</code> to change the window position. Its effects are applied after this option. </p>
<p> See <code>&#8211;geometry</code> for details how this is handled with multi-monitor setups. </p>
<p> Use <code>&#8211;autofit-larger</code> instead if you just want to limit the maximum size of the window, rather than always forcing a window size. </p>
<p> Use <code>&#8211;geometry</code> if you want to force both window width and height to a specific size. </p>
<p> <code>NOTE:</code> Generally only supported by GUI VOs. Ignored for encoding.</p>
<dt>Examples</p>
<dd>
<dt><code>70%</code></p>
<dd>Make the window width 70% of the screen size, keeping aspect ratio.</p>
<dt><code>1000</code></p>
<dd>Set the window width to 1000 pixels, keeping aspect ratio.</p>
<dt><code>70%x60%</code></p>
<dd>Make the window as large as possible, without being wider than 70% of the screen width, or higher than 60% of the screen height.</p>
<dt><code>&#8211;autofit-larger=&lt;[W[xH]]&gt;</code></p>
<dd>This option behaves exactly like <code>&#8211;autofit</code>, except the window size is only changed if the window would be larger than the specified size.</p>
<dt>Example</p>
<dd>
<dt><code>90%x80%</code></p>
<dd>If the video is larger than 90% of the screen width or 80% of the screen height, make the window smaller until either its width is 90% of the screen, or its height is 80% of the screen.</p>
<dt><code>&#8211;autofit-smaller=&lt;[W[xH]]&gt;</code></p>
<dd>This option behaves exactly like <code>&#8211;autofit</code>, except that it sets the minimum size of the window (just as <code>&#8211;autofit-larger</code> sets the maximum).</p>
<dt>Example</p>
<dd>
<dt><code>500&#215;500</code></p>
<dd>Make the window at least 500 pixels wide and 500 pixels high (depending on the video aspect ratio, the width or height will be larger than 500 in order to keep the aspect ratio the same).</p>
<dt><code>&#8211;window-scale=&lt;factor&gt;</code></p>
<dd>Resize the video window to a multiple (or fraction) of the video size. This option is applied before <code>&#8211;autofit</code> and other options are applied (so they override this option). </p>
<p> For example, <code>&#8211;window-scale=0.5</code> would show the window at half the video size.</p>
<dt><code>&#8211;window-minimized=&lt;yes|no&gt;</code></p>
<dd>Whether the video window is minimized or not. Setting this will minimize, or unminimize, the video window if the current VO supports it. Note that some VOs may support minimization while not supporting unminimization (eg: Wayland). </p>
<p> Whether this option and <code>&#8211;window-maximized</code> work on program start or at runtime, and whether they&#8217;re (at runtime) updated to reflect the actual window state, heavily depends on the VO and the windowing system. Some VOs simply do not implement them or parts of them, while other VOs may be restricted by the windowing systems (especially Wayland).</p>
<dt><code>&#8211;window-maximized=&lt;yes|no&gt;</code></p>
<dd>Whether the video window is maximized or not. Setting this will maximize, or unmaximize, the video window if the current VO supports it. See <code>&#8211;window-minimized</code> for further remarks.</p>
<dt><code>&#8211;cursor-autohide=&lt;number|no|always&gt;</code></p>
<dd>Make mouse cursor automatically hide after given number of milliseconds. <code>no</code> will disable cursor autohide. <code>always</code> means the cursor will stay hidden.</p>
<dt><code>&#8211;cursor-autohide-fs-only</code></p>
<dd>If this option is given, the cursor is always visible in windowed mode. In fullscreen mode, the cursor is shown or hidden according to <code>&#8211;cursor-autohide</code>.</p>
<dt><code>&#8211;no-fixed-vo</code>, <code>&#8211;fixed-vo</code></p>
<dd><code>&#8211;no-fixed-vo</code> enforces closing and reopening the video window for multiple files (one (un)initialization for each file).</p>
<dt><code>&#8211;force-rgba-osd-rendering</code></p>
<dd>Change how some video outputs render the OSD and text subtitles. This does not change appearance of the subtitles and only has performance implications. For VOs which support native ASS rendering (like <code>gpu</code>, <code>vdpau</code>, <code>direct3d</code>), this can be slightly faster or slower, depending on GPU drivers and hardware. For other VOs, this just makes rendering slower.</p>
<dt><code>&#8211;force-window-position</code></p>
<dd>Forcefully move mpv&#8217;s video output window to default location whenever there is a change in video parameters, video stream or file. This used to be the default behavior. Currently only affects X11 VOs.</p>
<dt><code>&#8211;no-keepaspect</code>, <code>&#8211;keepaspect</code></p>
<dd><code>&#8211;no-keepaspect</code> will always stretch the video to window size, and will disable the window manager hints that force the window aspect ratio. (Ignored in fullscreen mode.)</p>
<dt><code>&#8211;no-keepaspect-window</code>, <code>&#8211;keepaspect-window</code></p>
<dd><code>&#8211;keepaspect-window</code> (the default) will lock the window size to the video aspect. <code>&#8211;no-keepaspect-window</code> disables this behavior, and will instead add black bars if window aspect and video aspect mismatch. Whether this actually works depends on the VO backend. (Ignored in fullscreen mode.)</p>
<dt><code>&#8211;monitoraspect=&lt;ratio&gt;</code></p>
<dd>Set the aspect ratio of your monitor or TV screen. A value of 0 disables a previous setting (e.g. in the config file). Overrides the <code>&#8211;monitorpixelaspect</code> setting if enabled. </p>
<p> See also <code>&#8211;monitorpixelaspect</code> and <code>&#8211;video-aspect-override</code>.</p>
<dt>Examples</p>
<dd>
<dt>&bull;</p>
<dd><code>&#8211;monitoraspect=4:3</code> or <code>&#8211;monitoraspect=1.3333</code></p>
<dt>&bull;</p>
<dd><code>&#8211;monitoraspect=16:9</code> or <code>&#8211;monitoraspect=1.7777</code></p>
<dt><code>&#8211;hidpi-window-scale</code>, <code>&#8211;no-hidpi-window-scale</code></p>
<dd>(macOS, Windows, X11, and Wayland only) Scale the window size according to the backing scale factor (default: yes). On regular HiDPI resolutions the window opens with double the size but appears as having the same size as on non-HiDPI resolutions. This is enabled by default on macOS.</p>
<dt><code>&#8211;native-fs</code>, <code>&#8211;no-native-fs</code></p>
<dd>(macOS only) Uses the native fullscreen mechanism of the OS (default: yes).</p>
<dt><code>&#8211;monitorpixelaspect=&lt;ratio&gt;</code></p>
<dd>Set the aspect of a single pixel of your monitor or TV screen (default: 1). A value of 1 means square pixels (correct for (almost?) all LCDs). See also <code>&#8211;monitoraspect</code> and <code>&#8211;video-aspect-override</code>.</p>
<dt><code>&#8211;stop-screensaver</code>, <code>&#8211;no-stop-screensaver</code></p>
<dd>Turns off the screensaver (or screen blanker and similar mechanisms) at startup and turns it on again on exit (default: yes). The screensaver is always re-enabled when the player is paused. </p>
<p> This is not supported on all video outputs or platforms. Sometimes it is implemented, but does not work (especially with Linux &quot;desktops&quot;). Read the <i>Disabling Screensaver</i> section very carefully.</p>
<dt><code>&#8211;wid=&lt;ID&gt;</code></p>
<dd>This tells mpv to attach to an existing window. If a VO is selected that supports this option, it will use that window for video output. mpv will scale the video to the size of this window, and will add black bars to compensate if the aspect ratio of the video is different. </p>
<p> On X11, the ID is interpreted as a <code>Window</code> on X11. Unlike MPlayer/mplayer2, mpv always creates its own window, and sets the wid window as parent. The window will always be resized to cover the parent window fully. The value <code>0</code> is interpreted specially, and mpv will draw directly on the root window. </p>
<p> On win32, the ID is interpreted as <code>HWND</code>. Pass it as value cast to <code>intptr_t</code>. mpv will create its own window, and set the wid window as parent, like with X11. </p>
<p> On macOS/Cocoa, the ID is interpreted as <code>NSView*</code>. Pass it as value cast to <code>intptr_t</code>. mpv will create its own sub-view. Because macOS does not support window embedding of foreign processes, this works only with libmpv, and will crash when used from the command line. </p>
<p> On Android, the ID is interpreted as <code>android.view.Surface</code>. Pass it as a value cast to <code>intptr_t</code>. Use with <code>&#8211;vo=mediacodec_embed</code> and <code>&#8211;hwdec=mediacodec</code> for direct rendering using MediaCodec, or with <code>&#8211;vo=gpu &#8211;gpu-context=android</code> (with or without <code>&#8211;hwdec=mediacodec-copy</code>).</p>
<dt><code>&#8211;no-window-dragging</code></p>
<dd>Don&#8217;t move the window when clicking on it and moving the mouse pointer.</p>
<dt><code>&#8211;x11-name</code></p>
<dd>Set the window class name for X11-based video output methods.</p>
<dt><code>&#8211;x11-netwm=&lt;yes|no|auto&gt;</code></p>
<dd>(X11 only) Control the use of NetWM protocol features. </p>
<p> This may or may not help with broken window managers. This provides some functionality that was implemented by the now removed <code>&#8211;fstype</code> option. Actually, it is not known to the developers to which degree this option was needed, so feedback is welcome. </p>
<p> Specifically, <code>yes</code> will force use of NetWM fullscreen support, even if not advertised by the WM. This can be useful for WMs that are broken on purpose, like XMonad. (XMonad supposedly doesn&#8217;t advertise fullscreen support, because Flash uses it. Apparently, applications which want to use fullscreen anyway are supposed to either ignore the NetWM support hints, or provide a workaround. Shame on XMonad for deliberately breaking X protocols (as if X isn&#8217;t bad enough already). </p>
<p> By default, NetWM support is autodetected (<code>auto</code>). </p>
<p> This option might be removed in the future.</p>
<dt><code>&#8211;x11-bypass-compositor=&lt;yes|no|fs-only|never&gt;</code></p>
<dd>If set to <code>yes</code>, then ask the compositor to unredirect the mpv window (default: <code>fs-only</code>). This uses the <code>_NET_WM_BYPASS_COMPOSITOR</code> hint. </p>
<p> <code>fs-only</code> asks the window manager to disable the compositor only in fullscreen mode. </p>
<p> <code>no</code> sets <code>_NET_WM_BYPASS_COMPOSITOR</code> to 0, which is the default value as declared by the EWMH specification, i.e. no change is done. </p>
<p> <code>never</code> asks the window manager to never disable the compositor.</dl>
<h3>Disc Devices</h3>
<dl COMPACT>
<dt><code>&#8211;cdrom-device=&lt;path&gt;</code></p>
<dd>Specify the CD-ROM device (default: <code>/dev/cdrom</code>).</p>
<dt><code>&#8211;dvd-device=&lt;path&gt;</code></p>
<dd>Specify the DVD device or .iso filename (default: <code>/dev/dvd</code>). You can also specify a directory that contains files previously copied directly from a DVD (with e.g. vobcopy).</p>
<dt>Example</p>
<dd><code>mpv dvd:// &#8211;dvd-device=/path/to/dvd/</code></p>
<dt><code>&#8211;bluray-device=&lt;path&gt;</code></p>
<dd>(Blu-ray only) Specify the Blu-ray disc location. Must be a directory with Blu-ray structure.</p>
<dt>Example</p>
<dd><code>mpv bd:// &#8211;bluray-device=/path/to/bd/</code></p>
<dt><code>&#8211;cdda-&#8230;</code></p>
<dd>These options can be used to tune the CD Audio reading feature of mpv.</p>
<dt><code>&#8211;cdda-speed=&lt;value&gt;</code></p>
<dd>Set CD spin speed.</p>
<dt><code>&#8211;cdda-paranoia=&lt;0-2&gt;</code></p>
<dd>Set paranoia level. Values other than 0 seem to break playback of anything but the first track.</p>
<dt><code>0</code></p>
<dd>disable checking (default)</p>
<dt><code>1</code></p>
<dd>overlap checking only</p>
<dt><code>2</code></p>
<dd>full data correction and verification</p>
<dt><code>&#8211;cdda-sector-size=&lt;value&gt;</code></p>
<dd>Set atomic read size.</p>
<dt><code>&#8211;cdda-overlap=&lt;value&gt;</code></p>
<dd>Force minimum overlap search during verification to &lt;value&gt; sectors.</p>
<dt><code>&#8211;cdda-toc-bias</code></p>
<dd>Assume that the beginning offset of track 1 as reported in the TOC will be addressed as LBA 0. Some discs need this for getting track boundaries correctly.</p>
<dt><code>&#8211;cdda-toc-offset=&lt;value&gt;</code></p>
<dd>Add <code>&lt;value&gt;</code> sectors to the values reported when addressing tracks. May be negative.</p>
<dt><code>&#8211;cdda-skip=&lt;yes|no&gt;</code></p>
<dd>(Never) accept imperfect data reconstruction.</p>
<dt><code>&#8211;cdda-cdtext=&lt;yes|no&gt;</code></p>
<dd>Print CD text. This is disabled by default, because it ruins performance with CD-ROM drives for unknown reasons.</p>
<dt><code>&#8211;dvd-speed=&lt;speed&gt;</code></p>
<dd>Try to limit DVD speed (default: 0, no change). DVD base speed is 1385 kB/s, so an 8x drive can read at speeds up to 11080 kB/s. Slower speeds make the drive more quiet. For watching DVDs, 2700 kB/s should be quiet and fast enough. mpv resets the speed to the drive default value on close. Values of at least 100 mean speed in kB/s. Values less than 100 mean multiples of 1385 kB/s, i.e. <code>&#8211;dvd-speed=8</code> selects 11080 kB/s. </p>
<p> <code>NOTE:</code> You need write access to the DVD device to change the speed.</p>
<dt><code>&#8211;dvd-angle=&lt;ID&gt;</code></p>
<dd>Some DVDs contain scenes that can be viewed from multiple angles. This option tells mpv which angle to use (default: 1).</dl>
<h3>Equalizer</h3>
<dl COMPACT>
<dt><code>&#8211;brightness=&lt;-100-100&gt;</code></p>
<dd>Adjust the brightness of the video signal (default: 0). Not supported by all video output drivers.</p>
<dt><code>&#8211;contrast=&lt;-100-100&gt;</code></p>
<dd>Adjust the contrast of the video signal (default: 0). Not supported by all video output drivers.</p>
<dt><code>&#8211;saturation=&lt;-100-100&gt;</code></p>
<dd>Adjust the saturation of the video signal (default: 0). You can get grayscale output with this option. Not supported by all video output drivers.</p>
<dt><code>&#8211;gamma=&lt;-100-100&gt;</code></p>
<dd>Adjust the gamma of the video signal (default: 0). Not supported by all video output drivers.</p>
<dt><code>&#8211;hue=&lt;-100-100&gt;</code></p>
<dd>Adjust the hue of the video signal (default: 0). You can get a colored negative of the image with this option. Not supported by all video output drivers.</dl>
<h3>Demuxer</h3>
<dl COMPACT>
<dt><code>&#8211;demuxer=&lt;[+]name&gt;</code></p>
<dd>Force demuxer type. Use a &#8216;+&#8217; before the name to force it; this will skip some checks. Give the demuxer name as printed by <code>&#8211;demuxer=help</code>.</p>
<dt><code>&#8211;demuxer-lavf-analyzeduration=&lt;value&gt;</code></p>
<dd>Maximum length in seconds to analyze the stream properties.</p>
<dt><code>&#8211;demuxer-lavf-probe-info=&lt;yes|no|auto|nostreams&gt;</code></p>
<dd>Whether to probe stream information (default: auto). Technically, this controls whether libavformat&#8217;s <code>avformat_find_stream_info()</code> function is called. Usually it&#8217;s safer to call it, but it can also make startup slower. </p>
<p> The <code>auto</code> choice (the default) tries to skip this for a few know-safe whitelisted formats, while calling it for everything else. </p>
<p> The <code>nostreams</code> choice only calls it if and only if the file seems to contain no streams after opening (helpful in cases when calling the function is needed to detect streams at all, such as with FLV files).</p>
<dt><code>&#8211;demuxer-lavf-probescore=&lt;1-100&gt;</code></p>
<dd>Minimum required libavformat probe score. Lower values will require less data to be loaded (makes streams start faster), but makes file format detection less reliable. Can be used to force auto-detected libavformat demuxers, even if libavformat considers the detection not reliable enough. (Default: 26.)</p>
<dt><code>&#8211;demuxer-lavf-allow-mimetype=&lt;yes|no&gt;</code></p>
<dd>Allow deriving the format from the HTTP MIME type (default: yes). Set this to no in case playing things from HTTP mysteriously fails, even though the same files work from local disk. </p>
<p> This is default in order to reduce latency when opening HTTP streams.</p>
<dt><code>&#8211;demuxer-lavf-format=&lt;name&gt;</code></p>
<dd>Force a specific libavformat demuxer.</p>
<dt><code>&#8211;demuxer-lavf-hacks=&lt;yes|no&gt;</code></p>
<dd>By default, some formats will be handled differently from other formats by explicitly checking for them. Most of these compensate for weird or imperfect behavior from libavformat demuxers. Passing <code>no</code> disables these. For debugging and testing only.</p>
<dt><code>&#8211;demuxer-lavf-o=&lt;key&gt;=&lt;value&gt;[,&lt;key&gt;=&lt;value&gt;[,&#8230;]]</code></p>
<dd>Pass AVOptions to libavformat demuxer. </p>
<p> Note, a patch to make the <i>o=</i> unneeded and pass all unknown options through the AVOption system is welcome. A full list of AVOptions can be found in the FFmpeg manual. Note that some options may conflict with mpv options. </p>
<p> This is a key/value list option. See <i>List Options</i> for details.</p>
<dt>Example</p>
<dd><code>&#8211;demuxer-lavf-o=fflags=+ignidx</code></p>
<dt><code>&#8211;demuxer-lavf-probesize=&lt;value&gt;</code></p>
<dd>Maximum amount of data to probe during the detection phase. In the case of MPEG-TS this value identifies the maximum number of TS packets to scan.</p>
<dt><code>&#8211;demuxer-lavf-buffersize=&lt;value&gt;</code></p>
<dd>Size of the stream read buffer allocated for libavformat in bytes (default: 32768). Lowering the size could lower latency. Note that libavformat might reallocate the buffer internally, or not fully use all of it.</p>
<dt><code>&#8211;demuxer-lavf-linearize-timestamps=&lt;yes|no|auto&gt;</code></p>
<dd>Attempt to linearize timestamp resets in demuxed streams (default: auto). This was tested only for single audio streams. It&#8217;s unknown whether it works correctly for video (but likely won&#8217;t). Note that the implementation is slightly incorrect either way, and will introduce a discontinuity by about 1 codec frame size. </p>
<p> The <code>auto</code> mode enables this for OGG audio stream. This covers the common and annoying case of OGG web radio streams. Some of these will reset timestamps to 0 every time a new song begins. This breaks the mpv seekable cache, which can&#8217;t deal with timestamp resets. Note that FFmpeg/libavformat&#8217;s seeking API can&#8217;t deal with this either; it&#8217;s likely that if this option breaks this even more, while if it&#8217;s disabled, you can at least seek within the first song in the stream. Well, you won&#8217;t get anything useful either way if the seek is outside of mpv&#8217;s cache.</p>
<dt><code>&#8211;demuxer-lavf-propagate-opts=&lt;yes|no&gt;</code></p>
<dd>Propagate FFmpeg-level options to recursively opened connections (default: yes). This is needed because FFmpeg will apply these settings to nested AVIO contexts automatically. On the other hand, this could break in certain situations &#8211; it&#8217;s the FFmpeg API, you just can&#8217;t win. </p>
<p> This affects in particular the <code>&#8211;timeout</code> option and anything passed with <code>&#8211;demuxer-lavf-o</code>. </p>
<p> If this option is deemed unnecessary at some point in the future, it will be removed without notice.</p>
<dt><code>&#8211;demuxer-mkv-subtitle-preroll=&lt;yes|index|no&gt;</code>, <code>&#8211;mkv-subtitle-preroll</code></p>
<dd>Try harder to show embedded soft subtitles when seeking somewhere. Normally, it can happen that the subtitle at the seek target is not shown due to how some container file formats are designed. The subtitles appear only if seeking before or exactly to the position a subtitle first appears. To make this worse, subtitles are often timed to appear a very small amount before the associated video frame, so that seeking to the video frame typically does not demux the subtitle at that position. </p>
<p> Enabling this option makes the demuxer start reading data a bit before the seek target, so that subtitles appear correctly. Note that this makes seeking slower, and is not guaranteed to always work. It only works if the subtitle is close enough to the seek target. </p>
<p> Works with the internal Matroska demuxer only. Always enabled for absolute and hr-seeks, and this option changes behavior with relative or imprecise seeks only. </p>
<p> You can use the <code>&#8211;demuxer-mkv-subtitle-preroll-secs</code> option to specify how much data the demuxer should pre-read at most in order to find subtitle packets that may overlap. Setting this to 0 will effectively disable this preroll mechanism. Setting a very large value can make seeking very slow, and an extremely large value would completely reread the entire file from start to seek target on every seek &#8211; seeking can become slower towards the end of the file. The details are messy, and the value is actually rounded down to the cluster with the previous video keyframe. </p>
<p> Some files, especially files muxed with newer mkvmerge versions, have information embedded that can be used to determine what subtitle packets overlap with a seek target. In these cases, mpv will reduce the amount of data read to a minimum. (Although it will still read <i>all</i> data between the cluster that contains the first wanted subtitle packet, and the seek target.) If the <code>index</code> choice (which is the default) is specified, then prerolling will be done only if this information is actually available. If this method is used, the maximum amount of data to skip can be additionally controlled by <code>&#8211;demuxer-mkv-subtitle-preroll-secs-index</code> (it still uses the value of the option without <code>-index</code> if that is higher). </p>
<p> See also <code>&#8211;hr-seek-demuxer-offset</code> option. This option can achieve a similar effect, but only if hr-seek is active. It works with any demuxer, but makes seeking much slower, as it has to decode audio and video data instead of just skipping over it. </p>
<p> <code>&#8211;mkv-subtitle-preroll</code> is a deprecated alias.</p>
<dt><code>&#8211;demuxer-mkv-subtitle-preroll-secs=&lt;value&gt;</code></p>
<dd>See <code>&#8211;demuxer-mkv-subtitle-preroll</code>.</p>
<dt><code>&#8211;demuxer-mkv-subtitle-preroll-secs-index=&lt;value&gt;</code></p>
<dd>See <code>&#8211;demuxer-mkv-subtitle-preroll</code>.</p>
<dt><code>&#8211;demuxer-mkv-probe-start-time=&lt;yes|no&gt;</code></p>
<dd>Check the start time of Matroska files (default: yes). This simply reads the first cluster timestamps and assumes it is the start time. Technically, this also reads the first timestamp, which may increase latency by one frame (which may be relevant for live streams).</p>
<dt><code>&#8211;demuxer-mkv-probe-video-duration=&lt;yes|no|full&gt;</code></p>
<dd>When opening the file, seek to the end of it, and check what timestamp the last video packet has, and report that as file duration. This is strictly for compatibility with Haali only. In this mode, it&#8217;s possible that opening will be slower (especially when playing over http), or that behavior with broken files is much worse. So don&#8217;t use this option. </p>
<p> The <code>yes</code> mode merely uses the index and reads a small number of blocks from the end of the file. The <code>full</code> mode actually traverses the entire file and can make a reliable estimate even without an index present (such as partial files).</p>
<dt><code>&#8211;demuxer-rawaudio-channels=&lt;value&gt;</code></p>
<dd>Number of channels (or channel layout) if <code>&#8211;demuxer=rawaudio</code> is used (default: stereo).</p>
<dt><code>&#8211;demuxer-rawaudio-format=&lt;value&gt;</code></p>
<dd>Sample format for <code>&#8211;demuxer=rawaudio</code> (default: s16le). Use <code>&#8211;demuxer-rawaudio-format=help</code> to get a list of all formats.</p>
<dt><code>&#8211;demuxer-rawaudio-rate=&lt;value&gt;</code></p>
<dd>Sample rate for <code>&#8211;demuxer=rawaudio</code> (default: 44 kHz).</p>
<dt><code>&#8211;demuxer-rawvideo-fps=&lt;value&gt;</code></p>
<dd>Rate in frames per second for <code>&#8211;demuxer=rawvideo</code> (default: 25.0).</p>
<dt><code>&#8211;demuxer-rawvideo-w=&lt;value&gt;</code>, <code>&#8211;demuxer-rawvideo-h=&lt;value&gt;</code></p>
<dd>Image dimension in pixels for <code>&#8211;demuxer=rawvideo</code>.</p>
<dt>Example</p>
<dd>Play a raw YUV sample: </p>
<pre>mpv sample-720x576.yuv --demuxer=rawvideo \
--demuxer-rawvideo-w=720 --demuxer-rawvideo-h=576</pre>
<dt><code>&#8211;demuxer-rawvideo-format=&lt;value&gt;</code></p>
<dd>Color space (fourcc) in hex or string for <code>&#8211;demuxer=rawvideo</code> (default: <code>YV12</code>).</p>
<dt><code>&#8211;demuxer-rawvideo-mp-format=&lt;value&gt;</code></p>
<dd>Color space by internal video format for <code>&#8211;demuxer=rawvideo</code>. Use <code>&#8211;demuxer-rawvideo-mp-format=help</code> for a list of possible formats.</p>
<dt><code>&#8211;demuxer-rawvideo-codec=&lt;value&gt;</code></p>
<dd>Set the video codec instead of selecting the rawvideo codec when using <code>&#8211;demuxer=rawvideo</code>. This uses the same values as codec names in <code>&#8211;vd</code> (but it does not accept decoder names).</p>
<dt><code>&#8211;demuxer-rawvideo-size=&lt;value&gt;</code></p>
<dd>Frame size in bytes when using <code>&#8211;demuxer=rawvideo</code>.</p>
<dt><code>&#8211;demuxer-cue-codepage=&lt;codepage&gt;</code></p>
<dd>Specify the CUE sheet codepage. (See <code>&#8211;sub-codepage</code> for details.)</p>
<dt><code>&#8211;demuxer-max-bytes=&lt;bytesize&gt;</code></p>
<dd>This controls how much the demuxer is allowed to buffer ahead. The demuxer will normally try to read ahead as much as necessary, or as much is requested with <code>&#8211;demuxer-readahead-secs</code>. The option can be used to restrict the maximum readahead. This limits excessive readahead in case of broken files or desynced playback. The demuxer will stop reading additional packets as soon as one of the limits is reached. (The limits still can be slightly overstepped due to technical reasons.) </p>
<p> Set these limits higher if you get a packet queue overflow warning, and you think normal playback would be possible with a larger packet queue. </p>
<p> See <code>&#8211;list-options</code> for defaults and value range. <code>&lt;bytesize&gt;</code> options accept suffixes such as <code>KiB</code> and <code>MiB</code>.</p>
<dt><code>&#8211;demuxer-max-back-bytes=&lt;bytesize&gt;</code></p>
<dd>This controls how much past data the demuxer is allowed to preserve. This is useful only if the cache is enabled. </p>
<p> Unlike the forward cache, there is no control how many seconds are actually cached &#8211; it will simply use as much memory this option allows. Setting this option to 0 will strictly disable any back buffer, but this will lead to the situation that the forward seek range starts after the current playback position (as it removes past packets that are seek points). </p>
<p> If the end of the file is reached, the remaining unused forward buffer space is &quot;donated&quot; to the backbuffer (unless the backbuffer size is set to 0, or <code>&#8211;demuxer-donate-buffer</code> is set to <code>no</code>). This still limits the total cache usage to the sum of the forward and backward cache, and effectively makes better use of the total allowed memory budget. (The opposite does not happen: free backward buffer is never &quot;donated&quot; to the forward buffer.) </p>
<p> Keep in mind that other buffers in the player (like decoders) will cause the demuxer to cache &quot;future&quot; frames in the back buffer, which can skew the impression about how much data the backbuffer contains. </p>
<p> See <code>&#8211;list-options</code> for defaults and value range.</p>
<dt><code>&#8211;demuxer-donate-buffer=&lt;yes|no&gt;</code></p>
<dd>Whether to let the back buffer use part of the forward buffer (default: yes). If set to <code>yes</code>, the &quot;donation&quot; behavior described in the option description for <code>&#8211;demuxer-max-back-bytes</code> is enabled. This means the back buffer may use up memory up to the sum of the forward and back buffer options, minus the active size of the forward buffer. If set to <code>no</code>, the options strictly limit the forward and back buffer sizes separately. </p>
<p> Note that if the end of the file is reached, the buffered data stays the same, even if you seek back within the cache. This is because the back buffer is only reduced when new data is read.</p>
<dt><code>&#8211;demuxer-seekable-cache=&lt;yes|no|auto&gt;</code></p>
<dd>Debugging option to control whether seeking can use the demuxer cache (default: auto). Normally you don&#8217;t ever need to set this; the default <code>auto</code> does the right thing and enables cache seeking it if <code>&#8211;cache</code> is set to <code>yes</code> (or is implied <code>yes</code> if <code>&#8211;cache=auto</code>). </p>
<p> If enabled, short seek offsets will not trigger a low level demuxer seek (which means for example that slow network round trips or FFmpeg seek bugs can be avoided). If a seek cannot happen within the cached range, a low level seek will be triggered. Seeking outside of the cache will start a new cached range, but can discard the old cache range if the demuxer exhibits certain unsupported behavior. </p>
<p> The special value <code>auto</code> means <code>yes</code> in the same situation as <code>&#8211;cache-secs</code> is used (i.e. when the stream appears to be a network stream or the stream cache is enabled).</p>
<dt><code>&#8211;demuxer-force-retry-on-eof=&lt;yes|no&gt;</code></p>
<dd>Whether to keep retrying making the demuxer thread read more packets each time the decoder dequeues a packet, even if the end of the file was reached (default: no). This does not really make sense, but was the default behavior in mpv 0.32.0 and earlier. This option will be silently removed after a while, and exists only to restore the old behavior for testing, in case this was actually needed somewhere. This does _not_ help with files that are being appended to (in these cases use <code>appending://</code>, or disable the cache).</p>
<dt><code>&#8211;demuxer-thread=&lt;yes|no&gt;</code></p>
<dd>Run the demuxer in a separate thread, and let it prefetch a certain amount of packets (default: yes). Having this enabled leads to smoother playback, enables features like prefetching, and prevents that stuck network freezes the player. On the other hand, it can add overhead, or the background prefetching can hog CPU resources. </p>
<p> Disabling this option is not recommended. Use it for debugging only.</p>
<dt><code>&#8211;demuxer-termination-timeout=&lt;seconds&gt;</code></p>
<dd>Number of seconds the player should wait to shutdown the demuxer (default: 0.1). The player will wait up to this much time before it closes the stream layer forcefully. Forceful closing usually means the network I/O is given no chance to close its connections gracefully (of course the OS can still close TCP connections properly), and might result in annoying messages being logged, and in some cases, confused remote servers. </p>
<p> This timeout is usually only applied when loading has finished properly. If loading is aborted by the user, or in some corner cases like removing external tracks sourced from network during playback, forceful closing is always used.</p>
<dt><code>&#8211;demuxer-readahead-secs=&lt;seconds&gt;</code></p>
<dd>If <code>&#8211;demuxer-thread</code> is enabled, this controls how much the demuxer should buffer ahead in seconds (default: 1). As long as no packet has a timestamp difference higher than the readahead amount relative to the last packet returned to the decoder, the demuxer keeps reading. </p>
<p> Note that enabling the cache (such as <code>&#8211;cache=yes</code>, or if the input is considered a network stream, and <code>&#8211;cache=auto</code> is used), this option is mostly ignored. (<code>&#8211;cache-secs</code> will override this. Technically, the maximum of both options is used.) </p>
<p> The main purpose of this option is to limit the readhead for local playback, since a large readahead value is not overly useful in this case. </p>
<p> (This value tends to be fuzzy, because many file formats don&#8217;t store linear timestamps.)</p>
<dt><code>&#8211;prefetch-playlist=&lt;yes|no&gt;</code></p>
<dd>Prefetch next playlist entry while playback of the current entry is ending (default: no). </p>
<p> This does not prefill the cache with the video data of the next URL. Prefetching video data is supported only for the current playlist entry, and depends on the demuxer cache settings (on by default). This merely opens the URL of the next playlist entry as soon the current URL is fully read. </p>
<p> This does <code>not</code> work with URLs resolved by the <code>youtube-dl</code> wrapper, and it won&#8217;t. </p>
<p> This can give subtly wrong results if per-file options are used, or if options are changed in the time window between prefetching start and next file played. </p>
<p> This can occasionally make wrong prefetching decisions. For example, it can&#8217;t predict whether you go backwards in the playlist, and assumes you won&#8217;t edit the playlist. </p>
<p> Highly experimental.</p>
<dt><code>&#8211;force-seekable=&lt;yes|no&gt;</code></p>
<dd>If the player thinks that the media is not seekable (e.g. playing from a pipe, or it&#8217;s an http stream with a server that doesn&#8217;t support range requests), seeking will be disabled. This option can forcibly enable it. For seeks within the cache, there&#8217;s a good chance of success.</p>
<dt><code>&#8211;demuxer-cache-wait=&lt;yes|no&gt;</code></p>
<dd>Before starting playback, read data until either the end of the file was reached, or the demuxer cache has reached maximum capacity. Only once this is done, playback starts. This intentionally happens before the initial seek triggered with <code>&#8211;start</code>. This does not change any runtime behavior after the initial caching. This option is useless if the file cannot be cached completely.</p>
<dt><code>&#8211;rar-list-all-volumes=&lt;yes|no&gt;</code></p>
<dd>When opening multi-volume rar files, open all volumes to create a full list of contained files (default: no). If disabled, only the archive entries whose headers are located within the first volume are listed (and thus played when opening a .rar file with mpv). Doing so speeds up opening, and the typical idiotic use-case of playing uncompressed multi-volume rar files that contain a single media file is made faster. </p>
<p> Opening is still slow, because for unknown, idiotic, and unnecessary reasons libarchive opens all volumes anyway when playing the main file, even though mpv iterated no archive entries yet.</dl>
<h3>Input</h3>
<dl COMPACT>
<dt><code>&#8211;native-keyrepeat</code></p>
<dd>Use system settings for keyrepeat delay and rate, instead of <code>&#8211;input-ar-delay</code> and <code>&#8211;input-ar-rate</code>. (Whether this applies depends on the VO backend and how it handles keyboard input. Does not apply to terminal input.)</p>
<dt><code>&#8211;input-ar-delay</code></p>
<dd>Delay in milliseconds before we start to autorepeat a key (0 to disable).</p>
<dt><code>&#8211;input-ar-rate</code></p>
<dd>Number of key presses to generate per second on autorepeat.</p>
<dt><code>&#8211;input-conf=&lt;filename&gt;</code></p>
<dd>Specify input configuration file other than the default location in the mpv configuration directory (usually <code>~/.config/mpv/input.conf</code>).</p>
<dt><code>&#8211;no-input-default-bindings</code></p>
<dd>Disable default-level (&quot;weak&quot;) key bindings. These are bindings which config files like <code>input.conf</code> can override. It currently affects the builtin key bindings, and keys which scripts bind using <code>mp.add_key_binding</code> (but not <code>mp.add_forced_key_binding</code> because this overrides <code>input.conf</code>).</p>
<dt><code>&#8211;no-input-builtin-bindings</code></p>
<dd>Disable loading of built-in key bindings during start-up. This option is applied only during (lib)mpv initialization, and if used then it will not be not possible to enable them later. May be useful to libmpv clients.</p>
<dt><code>&#8211;input-cmdlist</code></p>
<dd>Prints all commands that can be bound to keys.</p>
<dt><code>&#8211;input-doubleclick-time=&lt;milliseconds&gt;</code></p>
<dd>Time in milliseconds to recognize two consecutive button presses as a double-click (default: 300).</p>
<dt><code>&#8211;input-keylist</code></p>
<dd>Prints all keys that can be bound to commands.</p>
<dt><code>&#8211;input-key-fifo-size=&lt;2-65000&gt;</code></p>
<dd>Specify the size of the FIFO that buffers key events (default: 7). If it is too small, some events may be lost. The main disadvantage of setting it to a very large value is that if you hold down a key triggering some particularly slow command then the player may be unresponsive while it processes all the queued commands.</p>
<dt><code>&#8211;input-test</code></p>
<dd>Input test mode. Instead of executing commands on key presses, mpv will show the keys and the bound commands on the OSD. Has to be used with a dummy video, and the normal ways to quit the player will not work (key bindings that normally quit will be shown on OSD only, just like any other binding). See <i>INPUT.CONF</i>.</p>
<dt><code>&#8211;input-terminal</code>, <code>&#8211;no-input-terminal</code></p>
<dd><code>&#8211;no-input-terminal</code> prevents the player from reading key events from standard input. Useful when reading data from standard input. This is automatically enabled when <code>&#8211;</code> is found on the command line. There are situations where you have to set it manually, e.g. if you open <code>/dev/stdin</code> (or the equivalent on your system), use stdin in a playlist or intend to read from stdin later on via the loadfile or loadlist input commands.</p>
<dt><code>&#8211;input-ipc-server=&lt;filename&gt;</code></p>
<dd>Enable the IPC support and create the listening socket at the given path. </p>
<p> On Linux and Unix, the given path is a regular filesystem path. On Windows, named pipes are used, so the path refers to the pipe namespace (<code>\.\pipe\&lt;name&gt;</code>). If the <code>\.\pipe\</code> prefix is missing, mpv will add it automatically before creating the pipe, so <code>&#8211;input-ipc-server=/tmp/mpv-socket</code> and <code>&#8211;input-ipc-server=\.\pipe	mp\mpv-socket</code> are equivalent for IPC on Windows. </p>
<p> See <i>JSON IPC</i> for details.</p>
<dt><code>&#8211;input-ipc-client=fd://&lt;N&gt;</code></p>
<dd>Connect a single IPC client to the given FD. This is somewhat similar to <code>&#8211;input-ipc-server</code>, except no socket is created, and instead the passed FD is treated like a socket connection received from <code>accept()</code>. In practice, you could pass either a FD created by <code>socketpair()</code>, or a pipe. In both cases, you must sure the FD is actually inherited by mpv (do not set the POSIX <code>CLOEXEC</code> flag). </p>
<p> The player quits when the connection is closed. </p>
<p> This is somewhat similar to the removed <code>&#8211;input-file</code> option, except it supports only integer FDs, and cannot open actual paths.</p>
<dt>Example</p>
<dd><code>&#8211;input-ipc-client=fd://123</code> </p>
<p> <code>NOTE:</code> Does not and will not work on Windows. </p>
<p> <code>WARNING:</code> Writing to the <code>input-ipc-server</code> option at runtime will start another instance of an IPC client handler for the <code>input-ipc-client</code> option, because initialization is bundled, and this thing is stupid. This is a bug. Writing to <code>input-ipc-client</code> at runtime will start another IPC client handler for the new value, without stopping the old one, even if the FD value is the same (but the string is different e.g. due to whitespace). This is not a bug.</p>
<dt><code>&#8211;input-gamepad=&lt;yes|no&gt;</code></p>
<dd>Enable/disable SDL2 Gamepad support. Disabled by default.</p>
<dt><code>&#8211;input-cursor</code>, <code>&#8211;no-input-cursor</code></p>
<dd>Permit mpv to receive pointer events reported by the video output driver. Necessary to use the OSC, or to select the buttons in DVD menus. Support depends on the VO in use.</p>
<dt><code>&#8211;input-media-keys=&lt;yes|no&gt;</code></p>
<dd>On systems where mpv can choose between receiving media keys or letting the system handle them &#8211; this option controls whether mpv should receive them. </p>
<p> Default: yes (except for libmpv). macOS and Windows only, because elsewhere mpv doesn&#8217;t have a choice &#8211; the system decides whether to send media keys to mpv. For instance, on X11 or Wayland, system-wide media keys are not implemented. Whether media keys work when the mpv window is focused is implementation-defined.</p>
<dt><code>&#8211;input-right-alt-gr</code>, <code>&#8211;no-input-right-alt-gr</code></p>
<dd>(Cocoa and Windows only) Use the right Alt key as Alt Gr to produce special characters. If disabled, count the right Alt as an Alt modifier key. Enabled by default.</p>
<dt><code>&#8211;input-vo-keyboard=&lt;yes|no&gt;</code></p>
<dd>Disable all keyboard input on for VOs which can&#8217;t participate in proper keyboard input dispatching. May not affect all VOs. Generally useful for embedding only. </p>
<p> On X11, a sub-window with input enabled grabs all keyboard input as long as it is 1. a child of a focused window, and 2. the mouse is inside of the sub-window. It can steal away all keyboard input from the application embedding the mpv window, and on the other hand, the mpv window will receive no input if the mouse is outside of the mpv window, even though mpv has focus. Modern toolkits work around this weird X11 behavior, but naively embedding foreign windows breaks it. </p>
<p> The only way to handle this reasonably is using the XEmbed protocol, which was designed to solve these problems. GTK provides <code>GtkSocket</code>, which supports XEmbed. Qt doesn&#8217;t seem to provide anything working in newer versions. </p>
<p> If the embedder supports XEmbed, input should work with default settings and with this option disabled. Note that <code>input-default-bindings</code> is disabled by default in libmpv as well &#8211; it should be enabled if you want the mpv default key bindings. </p>
<p> (This option was renamed from <code>&#8211;input-x11-keyboard</code>.)</dl>
<h3>Osd</h3>
<dl COMPACT>
<dt><code>&#8211;osc</code>, <code>&#8211;no-osc</code></p>
<dd>Whether to load the on-screen-controller (default: yes).</p>
<dt><code>&#8211;no-osd-bar</code>, <code>&#8211;osd-bar</code></p>
<dd>Disable display of the OSD bar. </p>
<p> You can configure this on a per-command basis in input.conf using <code>osd-</code> prefixes, see <code>Input Command Prefixes</code>. If you want to disable the OSD completely, use <code>&#8211;osd-level=0</code>.</p>
<dt><code>&#8211;osd-on-seek=&lt;no,bar,msg,msg-bar&gt;</code></p>
<dd>Set what is displayed on the OSD during seeks. The default is <code>bar</code>. </p>
<p> You can configure this on a per-command basis in input.conf using <code>osd-</code> prefixes, see <code>Input Command Prefixes</code>.</p>
<dt><code>&#8211;osd-duration=&lt;time&gt;</code></p>
<dd>Set the duration of the OSD messages in ms (default: 1000).</p>
<dt><code>&#8211;osd-font=&lt;name&gt;</code></p>
<dd>Specify font to use for OSD. The default is <code>sans-serif</code>.</p>
<dt>Examples</p>
<dd>
<dt>&bull;</p>
<dd><code>&#8211;osd-font=&#8217;Bitstream Vera Sans&#8217;</code></p>
<dt>&bull;</p>
<dd><code>&#8211;osd-font=&#8217;Comic Sans MS&#8217;</code></p>
<dt><code>&#8211;osd-font-size=&lt;size&gt;</code></p>
<dd>Specify the OSD font size. See <code>&#8211;sub-font-size</code> for details. </p>
<p> Default: 55.</p>
<dt><code>&#8211;osd-msg1=&lt;string&gt;</code></p>
<dd>Show this string as message on OSD with OSD level 1 (visible by default). The message will be visible by default, and as long as no other message covers it, and the OSD level isn&#8217;t changed (see <code>&#8211;osd-level</code>). Expands properties; see <i>Property Expansion</i>.</p>
<dt><code>&#8211;osd-msg2=&lt;string&gt;</code></p>
<dd>Similar to <code>&#8211;osd-msg1</code>, but for OSD level 2. If this is an empty string (default), then the playback time is shown.</p>
<dt><code>&#8211;osd-msg3=&lt;string&gt;</code></p>
<dd>Similar to <code>&#8211;osd-msg1</code>, but for OSD level 3. If this is an empty string (default), then the playback time, duration, and some more information is shown. </p>
<p> This is used for the <code>show-progress</code> command (by default mapped to <code>P</code>), and when seeking if enabled with <code>&#8211;osd-on-seek</code> or by <code>osd-</code> prefixes in input.conf (see <code>Input Command Prefixes</code>). </p>
<p> <code>&#8211;osd-status-msg</code> is a legacy equivalent (but with a minor difference).</p>
<dt><code>&#8211;osd-status-msg=&lt;string&gt;</code></p>
<dd>Show a custom string during playback instead of the standard status text. This overrides the status text used for <code>&#8211;osd-level=3</code>, when using the <code>show-progress</code> command (by default mapped to <code>P</code>), and when seeking if enabled with <code>&#8211;osd-on-seek</code> or <code>osd-</code> prefixes in input.conf (see <code>Input Command Prefixes</code>). Expands properties. See <i>Property Expansion</i>. </p>
<p> This option has been replaced with <code>&#8211;osd-msg3</code>. The only difference is that this option implicitly includes <code>${osd-sym-cc}</code>. This option is ignored if <code>&#8211;osd-msg3</code> is not empty.</p>
<dt><code>&#8211;osd-playing-msg=&lt;string&gt;</code></p>
<dd>Show a message on OSD when playback starts. The string is expanded for properties, e.g. <code>&#8211;osd-playing-msg=&#8217;file: ${filename}&#8217;</code> will show the message <code>file:</code> followed by a space and the currently played filename. </p>
<p> See <i>Property Expansion</i>.</p>
<dt><code>&#8211;osd-bar-align-x=&lt;-1-1&gt;</code></p>
<dd>Position of the OSD bar. -1 is far left, 0 is centered, 1 is far right. Fractional values (like 0.5) are allowed.</p>
<dt><code>&#8211;osd-bar-align-y=&lt;-1-1&gt;</code></p>
<dd>Position of the OSD bar. -1 is top, 0 is centered, 1 is bottom. Fractional values (like 0.5) are allowed.</p>
<dt><code>&#8211;osd-bar-w=&lt;1-100&gt;</code></p>
<dd>Width of the OSD bar, in percentage of the screen width (default: 75). A value of 50 means the bar is half the screen wide.</p>
<dt><code>&#8211;osd-bar-h=&lt;0.1-50&gt;</code></p>
<dd>Height of the OSD bar, in percentage of the screen height (default: 3.125).</p>
<dt><code>&#8211;osd-back-color=&lt;color&gt;</code></p>
<dd>See <code>&#8211;sub-color</code>. Color used for OSD text background.</p>
<dt><code>&#8211;osd-blur=&lt;0..20.0&gt;</code></p>
<dd>Gaussian blur factor. 0 means no blur applied (default).</p>
<dt><code>&#8211;osd-bold=&lt;yes|no&gt;</code></p>
<dd>Format text on bold.</p>
<dt><code>&#8211;osd-italic=&lt;yes|no&gt;</code></p>
<dd>Format text on italic.</p>
<dt><code>&#8211;osd-border-color=&lt;color&gt;</code></p>
<dd>See <code>&#8211;sub-color</code>. Color used for the OSD font border. </p>
<p> <code>NOTE:</code> ignored when <code>&#8211;osd-back-color</code> is specified (or more exactly: when that option is not set to completely transparent).</p>
<dt><code>&#8211;osd-border-size=&lt;size&gt;</code></p>
<dd>Size of the OSD font border in scaled pixels (see <code>&#8211;sub-font-size</code> for details). A value of 0 disables borders. </p>
<p> Default: 3.</p>
<dt><code>&#8211;osd-color=&lt;color&gt;</code></p>
<dd>Specify the color used for OSD. See <code>&#8211;sub-color</code> for details.</p>
<dt><code>&#8211;osd-fractions</code></p>
<dd>Show OSD times with fractions of seconds (in millisecond precision). Useful to see the exact timestamp of a video frame.</p>
<dt><code>&#8211;osd-level=&lt;0-3&gt;</code></p>
<dd>Specifies which mode the OSD should start in.</p>
<dt><code>0</code></p>
<dd>OSD completely disabled (subtitles only)</p>
<dt><code>1</code></p>
<dd>enabled (shows up only on user interaction)</p>
<dt><code>2</code></p>
<dd>enabled + current time visible by default</p>
<dt><code>3</code></p>
<dd>enabled + <code>&#8211;osd-status-msg</code> (current time and status by default)</p>
<dt><code>&#8211;osd-margin-x=&lt;size&gt;</code></p>
<dd>Left and right screen margin for the OSD in scaled pixels (see <code>&#8211;sub-font-size</code> for details). </p>
<p> This option specifies the distance of the OSD to the left, as well as at which distance from the right border long OSD text will be broken. </p>
<p> Default: 25.</p>
<dt><code>&#8211;osd-margin-y=&lt;size&gt;</code></p>
<dd>Top and bottom screen margin for the OSD in scaled pixels (see <code>&#8211;sub-font-size</code> for details). </p>
<p> This option specifies the vertical margins of the OSD. </p>
<p> Default: 22.</p>
<dt><code>&#8211;osd-align-x=&lt;left|center|right&gt;</code></p>
<dd>Control to which corner of the screen OSD should be aligned to (default: <code>left</code>).</p>
<dt><code>&#8211;osd-align-y=&lt;top|center|bottom&gt;</code></p>
<dd>Vertical position (default: <code>top</code>). Details see <code>&#8211;osd-align-x</code>.</p>
<dt><code>&#8211;osd-scale=&lt;factor&gt;</code></p>
<dd>OSD font size multiplier, multiplied with <code>&#8211;osd-font-size</code> value.</p>
<dt><code>&#8211;osd-scale-by-window=&lt;yes|no&gt;</code></p>
<dd>Whether to scale the OSD with the window size (default: yes). If this is disabled, <code>&#8211;osd-font-size</code> and other OSD options that use scaled pixels are always in actual pixels. The effect is that changing the window size won&#8217;t change the OSD font size.</p>
<dt><code>&#8211;osd-shadow-color=&lt;color&gt;</code></p>
<dd>See <code>&#8211;sub-color</code>. Color used for OSD shadow.</p>
<dt><code>&#8211;osd-shadow-offset=&lt;size&gt;</code></p>
<dd>Displacement of the OSD shadow in scaled pixels (see <code>&#8211;sub-font-size</code> for details). A value of 0 disables shadows. </p>
<p> Default: 0.</p>
<dt><code>&#8211;osd-spacing=&lt;size&gt;</code></p>
<dd>Horizontal OSD/sub font spacing in scaled pixels (see <code>&#8211;sub-font-size</code> for details). This value is added to the normal letter spacing. Negative values are allowed. </p>
<p> Default: 0.</p>
<dt><code>&#8211;video-osd=&lt;yes|no&gt;</code></p>
<dd>Enabled OSD rendering on the video window (default: yes). This can be used in situations where terminal OSD is preferred. If you just want to disable all OSD rendering, use <code>&#8211;osd-level=0</code>. </p>
<p> It does not affect subtitles or overlays created by scripts (in particular, the OSC needs to be disabled with <code>&#8211;no-osc</code>). </p>
<p> This option is somewhat experimental and could be replaced by another mechanism in the future.</p>
<dt><code>&#8211;osd-font-provider=&lt;&#8230;&gt;</code></p>
<dd>See <code>&#8211;sub-font-provider</code> for details and accepted values. Note that unlike subtitles, OSD never uses embedded fonts from media files.</dl>
<h3>Screenshot</h3>
<dl COMPACT>
<dt><code>&#8211;screenshot-format=&lt;type&gt;</code></p>
<dd>Set the image file type used for saving screenshots. </p>
<p> Available choices:</p>
<dt><code>png</code></p>
<dd>PNG</p>
<dt><code>jpg</code></p>
<dd>JPEG (default)</p>
<dt><code>jpeg</code></p>
<dd>JPEG (alias for jpg)</p>
<dt><code>webp</code></p>
<dd>WebP</p>
<dt><code>&#8211;screenshot-tag-colorspace=&lt;yes|no&gt;</code></p>
<dd>Tag screenshots with the appropriate colorspace. </p>
<p> Note that not all formats are supported. </p>
<p> Default: <code>no</code>.</p>
<dt><code>&#8211;screenshot-high-bit-depth=&lt;yes|no&gt;</code></p>
<dd>If possible, write screenshots with a bit depth similar to the source video (default: yes). This is interesting in particular for PNG, as this sometimes triggers writing 16 bit PNGs with huge file sizes. This will also include an unused alpha channel in the resulting files if 16 bit is used.</p>
<dt><code>&#8211;screenshot-template=&lt;template&gt;</code></p>
<dd>Specify the filename template used to save screenshots. The template specifies the filename without file extension, and can contain format specifiers, which will be substituted when taking a screenshot. By default, the template is <code>mpv-shot%n</code>, which results in filenames like <code>mpv-shot0012.png</code> for example. </p>
<p> The template can start with a relative or absolute path, in order to specify a directory location where screenshots should be saved. </p>
<p> If the final screenshot filename points to an already existing file, the file will not be overwritten. The screenshot will either not be saved, or if the template contains <code>%n</code>, saved using different, newly generated filename. </p>
<p> Allowed format specifiers:</p>
<dt><code>%[#][0X]n</code></p>
<dd>A sequence number, padded with zeros to length X (default: 04). E.g. passing the format <code>%04n</code> will yield <code>0012</code> on the 12th screenshot. The number is incremented every time a screenshot is taken or if the file already exists. The length <code>X</code> must be in the range 0-9. With the optional # sign, mpv will use the lowest available number. For example, if you take three screenshots&#8211;0001, 0002, 0003&#8211;and delete the first two, the next two screenshots will not be 0004 and 0005, but 0001 and 0002 again.</p>
<dt><code>%f</code></p>
<dd>Filename of the currently played video.</p>
<dt><code>%F</code></p>
<dd>Same as <code>%f</code>, but strip the file extension, including the dot.</p>
<dt><code>%x</code></p>
<dd>Directory path of the currently played video. If the video is not on the filesystem (but e.g. <code>http://</code>), this expand to an empty string.</p>
<dt><code>%X{fallback}</code></p>
<dd>Same as <code>%x</code>, but if the video file is not on the filesystem, return the fallback string inside the <code>{&#8230;}</code>.</p>
<dt><code>%p</code></p>
<dd>Current playback time, in the same format as used in the OSD. The result is a string of the form &quot;HH:MM:SS&quot;. For example, if the video is at the time position 5 minutes and 34 seconds, <code>%p</code> will be replaced with &quot;00:05:34&quot;.</p>
<dt><code>%P</code></p>
<dd>Similar to <code>%p</code>, but extended with the playback time in milliseconds. It is formatted as &quot;HH:MM:SS.mmm&quot;, with &quot;mmm&quot; being the millisecond part of the playback time. </p>
<p> <code>NOTE:</code> This is a simple way for getting unique per-frame timestamps. (Frame numbers would be more intuitive, but are not easily implementable because container formats usually use time stamps for identifying frames.)</p>
<dt><code>%wX</code></p>
<dd>Specify the current playback time using the format string <code>X</code>. <code>%p</code> is like <code>%wH:%wM:%wS</code>, and <code>%P</code> is like <code>%wH:%wM:%wS.%wT</code>.</p>
<dt><code>Valid format specifiers:</code></p>
<dd>
<dt><code>%wH</code></p>
<dd>hour (padded with 0 to two digits)</p>
<dt><code>%wh</code></p>
<dd>hour (not padded)</p>
<dt><code>%wM</code></p>
<dd>minutes (00-59)</p>
<dt><code>%wm</code></p>
<dd>total minutes (includes hours, unlike <code>%wM</code>)</p>
<dt><code>%wS</code></p>
<dd>seconds (00-59)</p>
<dt><code>%ws</code></p>
<dd>total seconds (includes hours and minutes)</p>
<dt><code>%wf</code></p>
<dd>like <code>%ws</code>, but as float</p>
<dt><code>%wT</code></p>
<dd>milliseconds (000-999)</p>
<dt><code>%tX</code></p>
<dd>Specify the current local date/time using the format <code>X</code>. This format specifier uses the UNIX <code>strftime()</code> function internally, and inserts the result of passing &quot;%X&quot; to <code>strftime</code>. For example, <code>%tm</code> will insert the number of the current month as number. You have to use multiple <code>%tX</code> specifiers to build a full date/time string.</p>
<dt><code>%{prop[:fallback text]}</code></p>
<dd>Insert the value of the input property &#8216;prop&#8217;. E.g. <code>%{filename}</code> is the same as <code>%f</code>. If the property does not exist or is not available, an error text is inserted, unless a fallback is specified.</p>
<dt><code>%%</code></p>
<dd>Replaced with the <code>%</code> character itself.</p>
<dt><code>&#8211;screenshot-directory=&lt;path&gt;</code></p>
<dd>Store screenshots in this directory. This path is joined with the filename generated by <code>&#8211;screenshot-template</code>. If the template filename is already absolute, the directory is ignored. </p>
<p> If the directory does not exist, it is created on the first screenshot. If it is not a directory, an error is generated when trying to write a screenshot. </p>
<p> This option is not set by default, and thus will write screenshots to the directory from which mpv was started. In pseudo-gui mode (see <i>PSEUDO GUI MODE</i>), this is set to the desktop.</p>
<dt><code>&#8211;screenshot-jpeg-quality=&lt;0-100&gt;</code></p>
<dd>Set the JPEG quality level. Higher means better quality. The default is 90.</p>
<dt><code>&#8211;screenshot-jpeg-source-chroma=&lt;yes|no&gt;</code></p>
<dd>Write JPEG files with the same chroma subsampling as the video (default: yes). If disabled, the libjpeg default is used.</p>
<dt><code>&#8211;screenshot-png-compression=&lt;0-9&gt;</code></p>
<dd>Set the PNG compression level. Higher means better compression. This will affect the file size of the written screenshot file and the time it takes to write a screenshot. Too high compression might occupy enough CPU time to interrupt playback. The default is 7.</p>
<dt><code>&#8211;screenshot-png-filter=&lt;0-5&gt;</code></p>
<dd>Set the filter applied prior to PNG compression. 0 is none, 1 is &quot;sub&quot;, 2 is &quot;up&quot;, 3 is &quot;average&quot;, 4 is &quot;Paeth&quot;, and 5 is &quot;mixed&quot;. This affects the level of compression that can be achieved. For most images, &quot;mixed&quot; achieves the best compression ratio, hence it is the default.</p>
<dt><code>&#8211;screenshot-webp-lossless=&lt;yes|no&gt;</code></p>
<dd>Write lossless WebP files. <code>&#8211;screenshot-webp-quality</code> is ignored if this is set. The default is no.</p>
<dt><code>&#8211;screenshot-webp-quality=&lt;0-100&gt;</code></p>
<dd>Set the WebP quality level. Higher means better quality. The default is 75.</p>
<dt><code>&#8211;screenshot-webp-compression=&lt;0-6&gt;</code></p>
<dd>Set the WebP compression level. Higher means better compression, but takes more CPU time. Note that this also affects the screenshot quality when used with lossy WebP files. The default is 4.</p>
<dt><code>&#8211;screenshot-sw=&lt;yes|no&gt;</code></p>
<dd>Whether to use software rendering for screenshots (default: no). </p>
<p> If set to no, the screenshot will be rendered by the current VO if possible (only vo_gpu currently). The advantage is that this will (probably) always show up as in the video window, because the same code is used for rendering. But since the renderer needs to be reinitialized, this can be slow and interrupt playback. (Unless the <code>window</code> mode is used with the <code>screenshot</code> command.) </p>
<p> If set to yes, the software scaler is used to convert the video to RGB (or whatever the target screenshot requires). In this case, conversion will run in a separate thread and will probably not interrupt playback. The software renderer may lack some capabilities, such as HDR rendering.</dl>
<h3>Software Scaler</h3>
<dl COMPACT>
<dt><code>&#8211;sws-scaler=&lt;name&gt;</code></p>
<dd>Specify the software scaler algorithm to be used with <code>&#8211;vf=scale</code>. This also affects video output drivers which lack hardware acceleration, e.g. <code>x11</code>. See also <code>&#8211;vf=scale</code>. </p>
<p> To get a list of available scalers, run <code>&#8211;sws-scaler=help</code>. </p>
<p> Default: <code>bicubic</code>.</p>
<dt><code>&#8211;sws-lgb=&lt;0-100&gt;</code></p>
<dd>Software scaler Gaussian blur filter (luma). See <code>&#8211;sws-scaler</code>.</p>
<dt><code>&#8211;sws-cgb=&lt;0-100&gt;</code></p>
<dd>Software scaler Gaussian blur filter (chroma). See <code>&#8211;sws-scaler</code>.</p>
<dt><code>&#8211;sws-ls=&lt;-100-100&gt;</code></p>
<dd>Software scaler sharpen filter (luma). See <code>&#8211;sws-scaler</code>.</p>
<dt><code>&#8211;sws-cs=&lt;-100-100&gt;</code></p>
<dd>Software scaler sharpen filter (chroma). See <code>&#8211;sws-scaler</code>.</p>
<dt><code>&#8211;sws-chs=&lt;h&gt;</code></p>
<dd>Software scaler chroma horizontal shifting. See <code>&#8211;sws-scaler</code>.</p>
<dt><code>&#8211;sws-cvs=&lt;v&gt;</code></p>
<dd>Software scaler chroma vertical shifting. See <code>&#8211;sws-scaler</code>.</p>
<dt><code>&#8211;sws-bitexact=&lt;yes|no&gt;</code></p>
<dd>Unknown functionality (default: no). Consult libswscale source code. The primary purpose of this, as far as libswscale API goes), is to produce exactly the same output for the same input on all platforms (output has the same &quot;bits&quot; everywhere, thus &quot;bitexact&quot;). Typically disables optimizations.</p>
<dt><code>&#8211;sws-fast=&lt;yes|no&gt;</code></p>
<dd>Allow optimizations that help with performance, but reduce quality (default: no). </p>
<p> VOs like <code>drm</code> and <code>x11</code> will benefit a lot from using <code>&#8211;sws-fast</code>. You may need to set other options, like <code>&#8211;sws-scaler</code>. The builtin <code>sws-fast</code> profile sets this option and some others to gain performance for reduced quality. Also see <code>&#8211;sws-allow-zimg</code>.</p>
<dt><code>&#8211;sws-allow-zimg=&lt;yes|no&gt;</code></p>
<dd>Allow using zimg (if the component using the internal swscale wrapper explicitly allows so) (default: yes). In this case, zimg <i>may</i> be used, if the internal zimg wrapper supports the input and output formats. It will silently or noisily fall back to libswscale if one of these conditions does not apply. </p>
<p> If zimg is used, the other <code>&#8211;sws-</code> options are ignored, and the <code>&#8211;zimg-</code> options are used instead. </p>
<p> If the internal component using the swscale wrapper hooks up logging correctly, a verbose priority log message will indicate whether zimg is being used. </p>
<p> Most things which need software conversion can make use of this. </p>
<p> <code>NOTE:</code> Do note that zimg <i>may</i> be slower than libswscale. Usually, it&#8217;s faster on x86 platforms, but slower on ARM (due to lack of ARM specific optimizations). The mpv zimg wrapper uses unoptimized repacking for some formats, for which zimg cannot be blamed.</p>
<dt><code>&#8211;zimg-scaler=&lt;point|bilinear|bicubic|spline16|spline36|lanczos&gt;</code></p>
<dd>Zimg luma scaler to use (default: lanczos).</p>
<dt><code>&#8211;zimg-scaler-param-a=&lt;default|float&gt;</code>, <code>&#8211;zimg-scaler-param-b=&lt;default|float&gt;</code></p>
<dd>Set scaler parameters. By default, these are set to the special string <code>default</code>, which maps to a scaler-specific default value. Ignored if the scaler is not tunable.</p>
<dt><code>lanczos</code></p>
<dd><code>&#8211;zimg-scaler-param-a</code> is the number of taps.</p>
<dt><code>bicubic</code></p>
<dd>a and b are the bicubic b and c parameters.</p>
<dt><code>&#8211;zimg-scaler-chroma=&#8230;</code></p>
<dd>Same as <code>&#8211;zimg-scaler</code>, for for chroma interpolation (default: bilinear).</p>
<dt><code>&#8211;zimg-scaler-chroma-param-a</code>, <code>&#8211;zimg-scaler-chroma-param-b</code></p>
<dd>Same as <code>&#8211;zimg-scaler-param-a</code> / <code>&#8211;zimg-scaler-param-b</code>, for chroma.</p>
<dt><code>&#8211;zimg-dither=&lt;no|ordered|random|error-diffusion&gt;</code></p>
<dd>Dithering (default: random).</p>
<dt><code>&#8211;zimg-threads=&lt;auto|integer&gt;</code></p>
<dd>Set the maximum number of threads to use for scaling (default: auto). <code>auto</code> uses the number of logical cores on the current machine. Note that the scaler may use less threads (or even just 1 thread) depending on stuff. Passing a value of 1 disables threading and always scales the image in a single operation. Higher thread counts waste resources, but make it typically faster. </p>
<p> Note that some zimg git versions had bugs that will corrupt the output if threads are used.</p>
<dt><code>&#8211;zimg-fast=&lt;yes|no&gt;</code></p>
<dd>Allow optimizations that help with performance, but reduce quality (default: yes). Currently, this may simplify gamma conversion operations.</dl>
<h3>Audio Resampler</h3>
<p>This controls the default options of any resampling done by mpv (but not within libavfilter, within the system audio API resampler, or any other places). </p>
<p> It also sets the defaults for the <code>lavrresample</code> audio filter.</p>
<dl COMPACT>
<dt><code>&#8211;audio-resample-filter-size=&lt;length&gt;</code></p>
<dd>Length of the filter with respect to the lower sampling rate. (default: 16)</p>
<dt><code>&#8211;audio-resample-phase-shift=&lt;count&gt;</code></p>
<dd>Log2 of the number of polyphase entries. (&#8230;, 10-&gt;1024, 11-&gt;2048, 12-&gt;4096, &#8230;) (default: 10-&gt;1024)</p>
<dt><code>&#8211;audio-resample-cutoff=&lt;cutoff&gt;</code></p>
<dd>Cutoff frequency (0.0-1.0), default set depending upon filter length.</p>
<dt><code>&#8211;audio-resample-linear=&lt;yes|no&gt;</code></p>
<dd>If set then filters will be linearly interpolated between polyphase entries. (default: no)</p>
<dt><code>&#8211;audio-normalize-downmix=&lt;yes|no&gt;</code></p>
<dd>Enable/disable normalization if surround audio is downmixed to stereo (default: no). If this is disabled, downmix can cause clipping. If it&#8217;s enabled, the output might be too quiet. It depends on the source audio. </p>
<p> Technically, this changes the <code>normalize</code> suboption of the <code>lavrresample</code> audio filter, which performs the downmixing. </p>
<p> If downmix happens outside of mpv for some reason, or in the decoder (decoder downmixing), or in the audio output (system mixer), this has no effect.</p>
<dt><code>&#8211;audio-resample-max-output-size=&lt;length&gt;</code></p>
<dd>Limit maximum size of audio frames filtered at once, in ms (default: 40). The output size size is limited in order to make resample speed changes react faster. This is necessary especially if decoders or filters output very large frame sizes (like some lossless codecs or some DRC filters). This option does not affect the resampling algorithm in any way. </p>
<p> For testing/debugging only. Can be removed or changed any time.</p>
<dt><code>&#8211;audio-swresample-o=&lt;string&gt;</code></p>
<dd>Set AVOptions on the SwrContext or AVAudioResampleContext. These should be documented by FFmpeg or Libav. </p>
<p> This is a key/value list option. See <i>List Options</i> for details.</dl>
<h3>Terminal</h3>
<dl COMPACT>
<dt><code>&#8211;quiet</code></p>
<dd>Make console output less verbose; in particular, prevents the status line (i.e. AV: 3.4 (00:00:03.37) / 5320.6 &#8230;) from being displayed. Particularly useful on slow terminals or broken ones which do not properly handle carriage return (i.e. <code></code>). </p>
<p> See also: <code>&#8211;really-quiet</code> and <code>&#8211;msg-level</code>.</p>
<dt><code>&#8211;really-quiet</code></p>
<dd>Display even less output and status messages than with <code>&#8211;quiet</code>.</p>
<dt><code>&#8211;no-terminal</code>, <code>&#8211;terminal</code></p>
<dd>Disable any use of the terminal and stdin/stdout/stderr. This completely silences any message output. </p>
<p> Unlike <code>&#8211;really-quiet</code>, this disables input and terminal initialization as well.</p>
<dt><code>&#8211;no-msg-color</code></p>
<dd>Disable colorful console output on terminals.</p>
<dt><code>&#8211;msg-level=&lt;module1=level1,module2=level2,&#8230;&gt;</code></p>
<dd>Control verbosity directly for each module. The <code>all</code> module changes the verbosity of all the modules. The verbosity changes from this option are applied in order from left to right, and each item can override a previous one. </p>
<p> Run mpv with <code>&#8211;msg-level=all=trace</code> to see all messages mpv outputs. You can use the module names printed in the output (prefixed to each line in <code>[&#8230;]</code>) to limit the output to interesting modules. </p>
<p> This also affects <code>&#8211;log-file</code>, and in certain cases libmpv API logging. </p>
<p> <code>NOTE:</code> Some messages are printed before the command line is parsed and are therefore not affected by <code>&#8211;msg-level</code>. To control these messages, you have to use the <code>MPV_VERBOSE</code> environment variable; see <i>ENVIRONMENT VARIABLES</i> for details. </p>
<p> Available levels:</p>
<dt><code>no</code></p>
<dd>complete silence</p>
<dt><code>fatal</code></p>
<dd>fatal messages only</p>
<dt><code>error</code></p>
<dd>error messages</p>
<dt><code>warn</code></p>
<dd>warning messages</p>
<dt><code>info</code></p>
<dd>informational messages</p>
<dt><code>status</code></p>
<dd>status messages (default)</p>
<dt><code>v</code></p>
<dd>verbose messages</p>
<dt><code>debug</code></p>
<dd>debug messages</p>
<dt><code>trace</code></p>
<dd>very noisy debug messages</p>
<dt>Example</p>
<dd>
<pre>mpv --msg-level=ao/sndio=no</pre>
<p>Completely silences the output of ao_sndio, which uses the log prefix <code>[ao/sndio]</code>. </p>
<pre>mpv --msg-level=all=warn,ao/alsa=error</pre>
<p>Only show warnings or worse, and let the ao_alsa output show errors only.</p>
<dt><code>&#8211;term-osd=&lt;auto|no|force&gt;</code></p>
<dd>Control whether OSD messages are shown on the console when no video output is available (default: auto).</p>
<dt><code>auto</code></p>
<dd>use terminal OSD if no video output active</p>
<dt><code>no</code></p>
<dd>disable terminal OSD</p>
<dt><code>force</code></p>
<dd>use terminal OSD even if video output active </p>
<p> The <code>auto</code> mode also enables terminal OSD if <code>&#8211;video-osd=no</code> was set.</p>
<dt><code>&#8211;term-osd-bar</code>, <code>&#8211;no-term-osd-bar</code></p>
<dd>Enable printing a progress bar under the status line on the terminal. (Disabled by default.)</p>
<dt><code>&#8211;term-osd-bar-chars=&lt;string&gt;</code></p>
<dd>Customize the <code>&#8211;term-osd-bar</code> feature. The string is expected to consist of 5 characters (start, left space, position indicator, right space, end). You can use Unicode characters, but note that double- width characters will not be treated correctly. </p>
<p> Default: <code>[-+-]</code>.</p>
<dt><code>&#8211;term-playing-msg=&lt;string&gt;</code></p>
<dd>Print out a string after starting playback. The string is expanded for properties, e.g. <code>&#8211;term-playing-msg=&#8217;file: ${filename}&#8217;</code> will print the string <code>file:</code> followed by a space and the currently played filename. </p>
<p> See <i>Property Expansion</i>.</p>
<dt><code>&#8211;term-status-msg=&lt;string&gt;</code></p>
<dd>Print out a custom string during playback instead of the standard status line. Expands properties. See <i>Property Expansion</i>.</p>
<dt><code>&#8211;term-title=&lt;string&gt;</code></p>
<dd>Set the terminal title. Currently, this simply concatenates the escape sequence setting the window title with the provided (property expanded) string. This will mess up if the expanded string contain bytes that end the escape sequence, or if the terminal does not understand the sequence. The latter probably includes the regrettable win32. </p>
<p> Expands properties. See <i>Property Expansion</i>.</p>
<dt><code>&#8211;msg-module</code></p>
<dd>Prepend module name to each console message.</p>
<dt><code>&#8211;msg-time</code></p>
<dd>Prepend timing information to each console message. The time is in seconds since the player process was started (technically, slightly later actually), using a monotonic time source depending on the OS. This is <code>CLOCK_MONOTONIC</code> on sane UNIX variants.</dl>
<h3>Cache</h3>
<dl COMPACT>
<dt><code>&#8211;cache=&lt;yes|no|auto&gt;</code></p>
<dd>Decide whether to use network cache settings (default: auto). </p>
<p> If enabled, use up to <code>&#8211;cache-secs</code> for the cache size (but still limited to <code>&#8211;demuxer-max-bytes</code>), and make the cached data seekable (if possible). If disabled, <code>&#8211;cache-pause</code> and related are implicitly disabled. </p>
<p> The <code>auto</code> choice enables this depending on whether the stream is thought to involve network accesses or other slow media (this is an imperfect heuristic). </p>
<p> Before mpv 0.30.0, this used to accept a number, which specified the size of the cache in kilobytes. Use e.g. <code>&#8211;cache &#8211;demuxer-max-bytes=123k</code> instead.</p>
<dt><code>&#8211;no-cache</code></p>
<dd>Turn off input stream caching. See <code>&#8211;cache</code>.</p>
<dt><code>&#8211;cache-secs=&lt;seconds&gt;</code></p>
<dd>How many seconds of audio/video to prefetch if the cache is active. This overrides the <code>&#8211;demuxer-readahead-secs</code> option if and only if the cache is enabled and the value is larger. The default value is set to something very high, so the actually achieved readahead will usually be limited by the value of the <code>&#8211;demuxer-max-bytes</code> option. Setting this option is usually only useful for limiting readahead.</p>
<dt><code>&#8211;cache-on-disk=&lt;yes|no&gt;</code></p>
<dd>Write packet data to a temporary file, instead of keeping them in memory. This makes sense only with <code>&#8211;cache</code>. If the normal cache is disabled, this option is ignored. </p>
<p> You need to set <code>&#8211;cache-dir</code> to use this. </p>
<p> The cache file is append-only. Even if the player appears to prune data, the file space freed by it is not reused. The cache file is deleted when playback is closed. </p>
<p> Note that packet metadata is still kept in memory. <code>&#8211;demuxer-max-bytes</code> and related options are applied to metadata <i>only</i>. The size of this metadata varies, but 50 MB per hour of media is typical. The cache statistics will report this metadats size, instead of the size of the cache file. If the metadata hits the size limits, the metadata is pruned (but not the cache file). </p>
<p> When the media is closed, the cache file is deleted. A cache file is generally worthless after the media is closed, and it&#8217;s hard to retrieve any media data from it (it&#8217;s not supported by design). </p>
<p> If the option is enabled at runtime, the cache file is created, but old data will remain in the memory cache. If the option is disabled at runtime, old data remains in the disk cache, and the cache file is not closed until the media is closed. If the option is disabled and enabled again, it will continue to use the cache file that was opened first.</p>
<dt><code>&#8211;cache-dir=&lt;path&gt;</code></p>
<dd>Directory where to create temporary files (default: none). </p>
<p> Currently, this is used for <code>&#8211;cache-on-disk</code> only.</p>
<dt><code>&#8211;cache-pause=&lt;yes|no&gt;</code></p>
<dd>Whether the player should automatically pause when the cache runs out of data and stalls decoding/playback (default: yes). If enabled, it will pause and unpause once more data is available, aka &quot;buffering&quot;.</p>
<dt><code>&#8211;cache-pause-wait=&lt;seconds&gt;</code></p>
<dd>Number of seconds the packet cache should have buffered before starting playback again if &quot;buffering&quot; was entered (default: 1). This can be used to control how long the player rebuffers if <code>&#8211;cache-pause</code> is enabled, and the demuxer underruns. If the given time is higher than the maximum set with <code>&#8211;cache-secs</code> or <code>&#8211;demuxer-readahead-secs</code>, or prefetching ends before that for some other reason (like file end or maximum configured cache size reached), playback resumes earlier.</p>
<dt><code>&#8211;cache-pause-initial=&lt;yes|no&gt;</code></p>
<dd>Enter &quot;buffering&quot; mode before starting playback (default: no). This can be used to ensure playback starts smoothly, in exchange for waiting some time to prefetch network data (as controlled by <code>&#8211;cache-pause-wait</code>). For example, some common behavior is that playback starts, but network caches immediately underrun when trying to decode more data as playback progresses. </p>
<p> Another thing that can happen is that the network prefetching is so CPU demanding (due to demuxing in the background) that playback drops frames at first. In these cases, it helps enabling this option, and setting <code>&#8211;cache-secs</code> and <code>&#8211;cache-pause-wait</code> to roughly the same value. </p>
<p> This option also triggers when playback is restarted after seeking.</p>
<dt><code>&#8211;cache-unlink-files=&lt;immediate|whendone|no&gt;</code></p>
<dd>Whether or when to unlink cache files (default: immediate). This affects cache files which are inherently temporary, and which make no sense to remain on disk after the player terminates. This is a debugging option.</p>
<dt><code>immediate</code></p>
<dd>Unlink cache file after they were created. The cache files won&#8217;t be visible anymore, even though they&#8217;re in use. This ensures they are guaranteed to be removed from disk when the player terminates, even if it crashes.</p>
<dt><code>whendone</code></p>
<dd>Delete cache files after they are closed.</p>
<dt><code>no</code></p>
<dd>Don&#8217;t delete cache files. They will consume disk space without having a use. </p>
<p> Currently, this is used for <code>&#8211;cache-on-disk</code> only.</p>
<dt><code>&#8211;stream-buffer-size=&lt;bytesize&gt;</code></p>
<dd>Size of the low level stream byte buffer (default: 128KB). This is used as buffer between demuxer and low level I/O (e.g. sockets). Generally, this can be very small, and the main purpose is similar to the internal buffer FILE in the C standard library will have. </p>
<p> Half of the buffer is always used for guaranteed seek back, which is important for unseekable input. </p>
<p> There are known cases where this can help performance to set a large buffer:</p>
<dt>1.</p>
<dd>mp4 files. libavformat may trigger many small seeks in both directions, depending on how the file was muxed.</p>
<dt>2.</p>
<dd>Certain network filesystems, which do not have a cache, and where small reads can be inefficient. </p>
<p> In other cases, setting this to a large value can reduce performance. </p>
<p> Usually, read accesses are at half the buffer size, but it may happen that accesses are done alternating with smaller and larger sizes (this is due to the internal ring buffer wrap-around). </p>
<p> See <code>&#8211;list-options</code> for defaults and value range. <code>&lt;bytesize&gt;</code> options accept suffixes such as <code>KiB</code> and <code>MiB</code>.</p>
<dt><code>&#8211;vd-queue-enable=&lt;yes|no&gt;, &#8211;ad-queue-enable</code></p>
<dd>Enable running the video/audio decoder on a separate thread (default: no). If enabled, the decoder is run on a separate thread, and a frame queue is put between decoder and higher level playback logic. The size of the frame queue is defined by the other options below. </p>
<p> This is probably quite pointless. libavcodec already has multithreaded decoding (enabled by default), which makes this largely unnecessary. It might help in some corner cases with high bandwidth video that is slow to decode (in these cases libavcodec would block the playback logic, while using a decoding thread would distribute the decoding time evenly without affecting the playback logic). In other situations, it will simply make seeking slower and use significantly more memory. </p>
<p> The queue size is restricted by the other <code>&#8211;vd-queue-&#8230;</code> options. The final queue size is the minimum as indicated by the option with the lowest limit. Each decoder/track has its own queue that may use the full configured queue size. </p>
<p> Most queue options can be changed at runtime. <code>&#8211;vd-queue-enable</code> itself (and the audio equivalent) update only if decoding is completely reinitialized. However, setting <code>&#8211;vd-queue-max-samples=1</code> should almost lead to the same behavior as <code>&#8211;vd-queue-enable=no</code>, so that value can be used for effectively runtime enabling/disabling the queue. </p>
<p> This should not be used with hardware decoding. It is possible to enable this for audio, but it makes even less sense.</p>
<dt><code>&#8211;vd-queue-max-bytes=&lt;bytesize&gt;</code>, <code>&#8211;ad-queue-max-bytes</code></p>
<dd>Maximum approximate allowed size of the queue. If exceeded, decoding will be stopped. The maximum size can be exceeded by about 1 frame. </p>
<p> See <code>&#8211;list-options</code> for defaults and value range. <code>&lt;bytesize&gt;</code> options accept suffixes such as <code>KiB</code> and <code>MiB</code>.</p>
<dt><code>&#8211;vd-queue-max-samples=&lt;int&gt;</code>, <code>&#8211;ad-queue-max-samples</code></p>
<dd>Maximum number of frames (video) or samples (audio) of the queue. The audio size may be exceeded by about 1 frame. </p>
<p> See <code>&#8211;list-options</code> for defaults and value range.</p>
<dt><code>&#8211;vd-queue-max-secs=&lt;seconds&gt;</code>, <code>&#8211;ad-queue-max-secs</code></p>
<dd>Maximum number of seconds of media in the queue. The special value 0 means no limit is set. The queue size may be exceeded by about 2 frames. Timestamp resets may lead to random queue size usage. </p>
<p> See <code>&#8211;list-options</code> for defaults and value range.</dl>
<h3>Network</h3>
<dl COMPACT>
<dt><code>&#8211;user-agent=&lt;string&gt;</code></p>
<dd>Use <code>&lt;string&gt;</code> as user agent for HTTP streaming.</p>
<dt><code>&#8211;cookies</code>, <code>&#8211;no-cookies</code></p>
<dd>Support cookies when making HTTP requests. Disabled by default.</p>
<dt><code>&#8211;cookies-file=&lt;filename&gt;</code></p>
<dd>Read HTTP cookies from &lt;filename&gt;. The file is assumed to be in Netscape format.</p>
<dt><code>&#8211;http-header-fields=&lt;field1,field2&gt;</code></p>
<dd>Set custom HTTP fields when accessing HTTP stream. </p>
<p> This is a string list option. See <i>List Options</i> for details.</p>
<dt>Example</p>
<dd>
<pre>mpv --http-header-fields='Field1: value1','Field2: value2' \
<a rel="nofollow" href="http://localhost:1234">http://localhost:1234</a></pre>
<p>Will generate HTTP request: </p>
<pre>GET / HTTP/1.0
Host: localhost:1234
User-Agent: MPlayer
Icy-MetaData: 1
Field1: value1
Field2: value2
Connection: close</pre>
<dt><code>&#8211;http-proxy=&lt;proxy&gt;</code></p>
<dd>URL of the HTTP/HTTPS proxy. If this is set, the <code>http_proxy</code> environment is ignored. The <code>no_proxy</code> environment variable is still respected. This option is silently ignored if it does not start with <code>http://</code>. Proxies are not used for https URLs. Setting this option does not try to make the ytdl script use the proxy.</p>
<dt><code>&#8211;tls-ca-file=&lt;filename&gt;</code></p>
<dd>Certificate authority database file for use with TLS. (Silently fails with older FFmpeg or Libav versions.)</p>
<dt><code>&#8211;tls-verify</code></p>
<dd>Verify peer certificates when using TLS (e.g. with <code><a rel="nofollow" href="https://...">https://&#8230;</a></code>). (Silently fails with older FFmpeg or Libav versions.)</p>
<dt><code>&#8211;tls-cert-file</code></p>
<dd>A file containing a certificate to use in the handshake with the peer.</p>
<dt><code>&#8211;tls-key-file</code></p>
<dd>A file containing the private key for the certificate.</p>
<dt><code>&#8211;referrer=&lt;string&gt;</code></p>
<dd>Specify a referrer path or URL for HTTP requests.</p>
<dt><code>&#8211;network-timeout=&lt;seconds&gt;</code></p>
<dd>Specify the network timeout in seconds (default: 60 seconds). This affects at least HTTP. The special value 0 uses the FFmpeg/Libav defaults. If a protocol is used which does not support timeouts, this option is silently ignored. </p>
<p> <code>WARNING:</code> This breaks the RTSP protocol, because of inconsistent FFmpeg API regarding its internal timeout option. Not only does the RTSP timeout option accept different units (seconds instead of microseconds, causing mpv to pass it huge values), it will also overflow FFmpeg internal calculations. The worst is that merely setting the option will put RTSP into listening mode, which breaks any client uses. At time of this writing, the fix was not made effective yet. For this reason, this option is ignored (or should be ignored) on RTSP URLs. You can still set the timeout option directly with <code>&#8211;demuxer-lavf-o</code>.</p>
<dt><code>&#8211;rtsp-transport=&lt;lavf|udp|udp_multicast|tcp|http&gt;</code></p>
<dd>Select RTSP transport method (default: tcp). This selects the underlying network transport when playing <code><a href="rtsp://...">rtsp://&#8230;</a></code> URLs. The value <code>lavf</code> leaves the decision to libavformat.</p>
<dt><code>&#8211;hls-bitrate=&lt;no|min|max|&lt;rate&gt;&gt;</code></p>
<dd>If HLS streams are played, this option controls what streams are selected by default. The option allows the following parameters:</p>
<dt><code>no</code></p>
<dd>Don&#8217;t do anything special. Typically, this will simply pick the first audio/video streams it can find.</p>
<dt><code>min</code></p>
<dd>Pick the streams with the lowest bitrate.</p>
<dt><code>max</code></p>
<dd>Same, but highest bitrate. (Default.) </p>
<p> Additionally, if the option is a number, the stream with the highest rate equal or below the option value is selected. </p>
<p> The bitrate as used is sent by the server, and there&#8217;s no guarantee it&#8217;s actually meaningful.</dl>
<h3>Dvb</h3>
<dl COMPACT>
<dt><code>&#8211;dvbin-prog=&lt;string&gt;</code></p>
<dd>This defines the program to tune to. Usually, you may specify this by using a stream URI like <code>&quot;<a href="dvb://ZDF">dvb://ZDF</a> HD&quot;</code>, but you can tune to a different channel by writing to this property at runtime. Also see <code>dvbin-channel-switch-offset</code> for more useful channel switching functionality.</p>
<dt><code>&#8211;dvbin-card=&lt;0-15&gt;</code></p>
<dd>Specifies using card number 0-15 (default: 0).</p>
<dt><code>&#8211;dvbin-file=&lt;filename&gt;</code></p>
<dd>Instructs mpv to read the channels list from <code>&lt;filename&gt;</code>. The default is in the mpv configuration directory (usually <code>~/.config/mpv</code>) with the filename <code>channels.conf.{sat,ter,cbl,atsc}</code> (based on your card type) or <code>channels.conf</code> as a last resort. For DVB-S/2 cards, a VDR 1.7.x format channel list is recommended as it allows tuning to DVB-S2 channels, enabling subtitles and decoding the PMT (which largely improves the demuxing). Classic mplayer format channel lists are still supported (without these improvements), and for other card types, only limited VDR format channel list support is implemented (patches welcome). For channels with dynamic PID switching or incomplete <code>channels.conf</code>, <code>&#8211;dvbin-full-transponder</code> or the magic PID <code>8192</code> are recommended.</p>
<dt><code>&#8211;dvbin-timeout=&lt;1-30&gt;</code></p>
<dd>Maximum number of seconds to wait when trying to tune a frequency before giving up (default: 30).</p>
<dt><code>&#8211;dvbin-full-transponder=&lt;yes|no&gt;</code></p>
<dd>Apply no filters on program PIDs, only tune to frequency and pass full transponder to demuxer. The player frontend selects the streams from the full TS in this case, so the program which is shown initially may not match the chosen channel. Switching between the programs is possible by cycling the <code>program</code> property. This is useful to record multiple programs on a single transponder, or to work around issues in the <code>channels.conf</code>. It is also recommended to use this for channels which switch PIDs on-the-fly, e.g. for regional news. </p>
<p> Default: <code>no</code></p>
<dt><code>&#8211;dvbin-channel-switch-offset=&lt;integer&gt;</code></p>
<dd>This value is not meant for setting via configuration, but used in channel switching. An <code>input.conf</code> can <code>cycle</code> this value <code>up</code> and <code>down</code> to perform channel switching. This number effectively gives the offset to the initially tuned to channel in the channel list. </p>
<p> An example <code>input.conf</code> could contain: <code>H cycle dvbin-channel-switch-offset up</code>, <code>K cycle dvbin-channel-switch-offset down</code></dl>
<h3>ALSA audio output options</h3>
<dl COMPACT>
<dt><code>&#8211;alsa-device=&lt;device&gt;</code></p>
<dd>Deprecated, use <code>&#8211;audio-device</code> (requires <code>alsa/</code> prefix).</p>
<dt><code>&#8211;alsa-resample=yes</code></p>
<dd>Enable ALSA resampling plugin. (This is disabled by default, because some drivers report incorrect audio delay in some cases.)</p>
<dt><code>&#8211;alsa-mixer-device=&lt;device&gt;</code></p>
<dd>Set the mixer device used with <code>ao-volume</code> (default: <code>default</code>).</p>
<dt><code>&#8211;alsa-mixer-name=&lt;name&gt;</code></p>
<dd>Set the name of the mixer element (default: <code>Master</code>). This is for example <code>PCM</code> or <code>Master</code>.</p>
<dt><code>&#8211;alsa-mixer-index=&lt;number&gt;</code></p>
<dd>Set the index of the mixer channel (default: 0). Consider the output of &quot;<code>amixer scontrols</code>&quot;, then the index is the number that follows the name of the element.</p>
<dt><code>&#8211;alsa-non-interleaved</code></p>
<dd>Allow output of non-interleaved formats (if the audio decoder uses this format). Currently disabled by default, because some popular ALSA plugins are utterly broken with non-interleaved formats.</p>
<dt><code>&#8211;alsa-ignore-chmap</code></p>
<dd>Don&#8217;t read or set the channel map of the ALSA device &#8211; only request the required number of channels, and then pass the audio as-is to it. This option most likely should not be used. It can be useful for debugging, or for static setups with a specially engineered ALSA configuration (in this case you should always force the same layout with <code>&#8211;audio-channels</code>, or it will work only for files which use the layout implicit to your ALSA device).</p>
<dt><code>&#8211;alsa-buffer-time=&lt;microseconds&gt;</code></p>
<dd>Set the requested buffer time in microseconds. A value of 0 skips requesting anything from the ALSA API. This and the <code>&#8211;alsa-periods</code> option uses the ALSA <code>near</code> functions to set the requested parameters. If doing so results in an empty configuration set, setting these parameters is skipped. </p>
<p> Both options control the buffer size. A low buffer size can lead to higher CPU usage and audio dropouts, while a high buffer size can lead to higher latency in volume changes and other filtering.</p>
<dt><code>&#8211;alsa-periods=&lt;number&gt;</code></p>
<dd>Number of periods requested from the ALSA API. See <code>&#8211;alsa-buffer-time</code> for further remarks.</dl>
<h3>GPU renderer options</h3>
<p>The following video options are currently all specific to <code>&#8211;vo=gpu</code> and <code>&#8211;vo=libmpv</code> only, which are the only VOs that implement them.</p>
<dl COMPACT>
<dt><code>&#8211;scale=&lt;filter&gt;</code></p>
<dd>The filter function to use when upscaling video.</p>
<dt><code>bilinear</code></p>
<dd>Bilinear hardware texture filtering (fastest, very low quality). This is the default for compatibility reasons.</p>
<dt><code>spline36</code></p>
<dd>Mid quality and speed. This is the default when using <code>gpu-hq</code>.</p>
<dt><code>lanczos</code></p>
<dd>Lanczos scaling. Provides mid quality and speed. Generally worse than <code>spline36</code>, but it results in a slightly sharper image which is good for some content types. The number of taps can be controlled with <code>scale-radius</code>, but is best left unchanged. </p>
<p> (This filter is an alias for <code>sinc</code>-windowed <code>sinc</code>)</p>
<dt><code>ewa_lanczos</code></p>
<dd>Elliptic weighted average Lanczos scaling. Also known as Jinc. Relatively slow, but very good quality. The radius can be controlled with <code>scale-radius</code>. Increasing the radius makes the filter sharper but adds more ringing. </p>
<p> (This filter is an alias for <code>jinc</code>-windowed <code>jinc</code>)</p>
<dt><code>ewa_lanczossharp</code></p>
<dd>A slightly sharpened version of ewa_lanczos, preconfigured to use an ideal radius and parameter. If your hardware can run it, this is probably what you should use by default.</p>
<dt><code>mitchell</code></p>
<dd>Mitchell-Netravali. The <code>B</code> and <code>C</code> parameters can be set with <code>&#8211;scale-param1</code> and <code>&#8211;scale-param2</code>. This filter is very good at downscaling (see <code>&#8211;dscale</code>).</p>
<dt><code>oversample</code></p>
<dd>A version of nearest neighbour that (naively) oversamples pixels, so that pixels overlapping edges get linearly interpolated instead of rounded. This essentially removes the small imperfections and judder artifacts caused by nearest-neighbour interpolation, in exchange for adding some blur. This filter is good at temporal interpolation, and also known as &quot;smoothmotion&quot; (see <code>&#8211;tscale</code>).</p>
<dt><code>linear</code></p>
<dd>A <code>&#8211;tscale</code> filter. </p>
<p> There are some more filters, but most are not as useful. For a complete list, pass <code>help</code> as value, e.g.: </p>
<pre>mpv --scale=help</pre>
<dt><code>&#8211;cscale=&lt;filter&gt;</code></p>
<dd>As <code>&#8211;scale</code>, but for interpolating chroma information. If the image is not subsampled, this option is ignored entirely.</p>
<dt><code>&#8211;dscale=&lt;filter&gt;</code></p>
<dd>Like <code>&#8211;scale</code>, but apply these filters on downscaling instead. If this option is unset, the filter implied by <code>&#8211;scale</code> will be applied.</p>
<dt><code>&#8211;tscale=&lt;filter&gt;</code></p>
<dd>The filter used for interpolating the temporal axis (frames). This is only used if <code>&#8211;interpolation</code> is enabled. The only valid choices for <code>&#8211;tscale</code> are separable convolution filters (use <code>&#8211;tscale=help</code> to get a list). The default is <code>mitchell</code>. </p>
<p> Common <code>&#8211;tscale</code> choices include <code>oversample</code>, <code>linear</code>, <code>catmull_rom</code>, <code>mitchell</code>, <code>gaussian</code>, or <code>bicubic</code>. These are listed in increasing order of smoothness/blurriness, with <code>bicubic</code> being the smoothest/blurriest and <code>oversample</code> being the sharpest/least smooth.</p>
<dt><code>&#8211;scale-param1=&lt;value&gt;</code>, <code>&#8211;scale-param2=&lt;value&gt;</code>, <code>&#8211;cscale-param1=&lt;value&gt;</code>, <code>&#8211;cscale-param2=&lt;value&gt;</code>, <code>&#8211;dscale-param1=&lt;value&gt;</code>, <code>&#8211;dscale-param2=&lt;value&gt;</code>, <code>&#8211;tscale-param1=&lt;value&gt;</code>, <code>&#8211;tscale-param2=&lt;value&gt;</code></p>
<dd>Set filter parameters. By default, these are set to the special string <code>default</code>, which maps to a scaler-specific default value. Ignored if the filter is not tunable. Currently, this affects the following filter parameters:</p>
<dt><code>bcspline</code></p>
<dd>Spline parameters (<code>B</code> and <code>C</code>). Defaults to 0.5 for both.</p>
<dt><code>gaussian</code></p>
<dd>Scale parameter (<code>t</code>). Increasing this makes the result blurrier. Defaults to 1.</p>
<dt><code>oversample</code></p>
<dd>Minimum distance to an edge before interpolation is used. Setting this to 0 will always interpolate edges, whereas setting it to 0.5 will never interpolate, thus behaving as if the regular nearest neighbour algorithm was used. Defaults to 0.0.</p>
<dt><code>&#8211;scale-blur=&lt;value&gt;</code>, <code>&#8211;scale-wblur=&lt;value&gt;</code>, <code>&#8211;cscale-blur=&lt;value&gt;</code>, <code>&#8211;cscale-wblur=&lt;value&gt;</code>, <code>&#8211;dscale-blur=&lt;value&gt;</code>, <code>&#8211;dscale-wblur=&lt;value&gt;</code>, <code>&#8211;tscale-blur=&lt;value&gt;</code>, <code>&#8211;tscale-wblur=&lt;value&gt;</code></p>
<dd>Kernel/window scaling factor (also known as a blur factor). Decreasing this makes the result sharper, increasing it makes it blurrier (default 0). If set to 0, the kernel&#8217;s preferred blur factor is used. Note that setting this too low (eg. 0.5) leads to bad results. It&#8217;s generally recommended to stick to values between 0.8 and 1.2.</p>
<dt><code>&#8211;scale-clamp=&lt;0.0-1.0&gt;</code>, <code>&#8211;cscale-clamp</code>, <code>&#8211;dscale-clamp</code>, <code>&#8211;tscale-clamp</code></p>
<dd>Specifies a weight bias to multiply into negative coefficients. Specifying <code>&#8211;scale-clamp=1</code> has the effect of removing negative weights completely, thus effectively clamping the value range to [0-1]. Values between 0.0 and 1.0 can be specified to apply only a moderate diminishment of negative weights. This is especially useful for <code>&#8211;tscale</code>, where it reduces excessive ringing artifacts in the temporal domain (which typically manifest themselves as short flashes or fringes of black, mostly around moving edges) in exchange for potentially adding more blur. The default for <code>&#8211;tscale-clamp</code> is 1.0, the others default to 0.0.</p>
<dt><code>&#8211;scale-cutoff=&lt;value&gt;</code>, <code>&#8211;cscale-cutoff=&lt;value&gt;</code>, <code>&#8211;dscale-cutoff=&lt;value&gt;</code></p>
<dd>Cut off the filter kernel prematurely once the value range drops below this threshold. Doing so allows more aggressive pruning of skippable coefficients by disregarding parts of the LUT which are effectively zeroed out by the window function. Only affects polar (EWA) filters. The default is 0.001 for each, which is perceptually transparent but provides a 10%-20% speedup, depending on the exact radius and filter kernel chosen.</p>
<dt><code>&#8211;scale-taper=&lt;value&gt;</code>, <code>&#8211;scale-wtaper=&lt;value&gt;</code>, <code>&#8211;dscale-taper=&lt;value&gt;</code>, <code>&#8211;dscale-wtaper=&lt;value&gt;</code>, <code>&#8211;cscale-taper=&lt;value&gt;</code>, <code>&#8211;cscale-wtaper=&lt;value&gt;</code>, <code>&#8211;tscale-taper=&lt;value&gt;</code>, <code>&#8211;tscale-wtaper=&lt;value&gt;</code></p>
<dd>Kernel/window taper factor. Increasing this flattens the filter function. Value range is 0 to 1. A value of 0 (the default) means no flattening, a value of 1 makes the filter completely flat (equivalent to a box function). Values in between mean that some portion will be flat and the actual filter function will be squeezed into the space in between.</p>
<dt><code>&#8211;scale-radius=&lt;value&gt;</code>, <code>&#8211;cscale-radius=&lt;value&gt;</code>, <code>&#8211;dscale-radius=&lt;value&gt;</code>, <code>&#8211;tscale-radius=&lt;value&gt;</code></p>
<dd>Set radius for tunable filters, must be a float number between 0.5 and 16.0. Defaults to the filter&#8217;s preferred radius if not specified. Doesn&#8217;t work for every scaler and VO combination. </p>
<p> Note that depending on filter implementation details and video scaling ratio, the radius that actually being used might be different (most likely being increased a bit).</p>
<dt><code>&#8211;scale-antiring=&lt;value&gt;</code>, <code>&#8211;cscale-antiring=&lt;value&gt;</code>, <code>&#8211;dscale-antiring=&lt;value&gt;</code>, <code>&#8211;tscale-antiring=&lt;value&gt;</code></p>
<dd>Set the antiringing strength. This tries to eliminate ringing, but can introduce other artifacts in the process. Must be a float number between 0.0 and 1.0. The default value of 0.0 disables antiringing entirely. </p>
<p> Note that this doesn&#8217;t affect the special filters <code>bilinear</code> and <code>bicubic_fast</code>, nor does it affect any polar (EWA) scalers.</p>
<dt><code>&#8211;scale-window=&lt;window&gt;</code>, <code>&#8211;cscale-window=&lt;window&gt;</code>, <code>&#8211;dscale-window=&lt;window&gt;</code>, <code>&#8211;tscale-window=&lt;window&gt;</code></p>
<dd>(Advanced users only) Choose a custom windowing function for the kernel. Defaults to the filter&#8217;s preferred window if unset. Use <code>&#8211;scale-window=help</code> to get a list of supported windowing functions.</p>
<dt><code>&#8211;scale-wparam=&lt;window&gt;</code>, <code>&#8211;cscale-wparam=&lt;window&gt;</code>, <code>&#8211;cscale-wparam=&lt;window&gt;</code>, <code>&#8211;tscale-wparam=&lt;window&gt;</code></p>
<dd>(Advanced users only) Configure the parameter for the window function given by <code>&#8211;scale-window</code> etc. By default, these are set to the special string <code>default</code>, which maps to a window-specific default value. Ignored if the window is not tunable. Currently, this affects the following window parameters:</p>
<dt><code>kaiser</code></p>
<dd>Window parameter (alpha). Defaults to 6.33.</p>
<dt><code>blackman</code></p>
<dd>Window parameter (alpha). Defaults to 0.16.</p>
<dt><code>gaussian</code></p>
<dd>Scale parameter (t). Increasing this makes the window wider. Defaults to 1.</p>
<dt><code>&#8211;scaler-lut-size=&lt;4..10&gt;</code></p>
<dd>Set the size of the lookup texture for scaler kernels (default: 6). The actual size of the texture is <code>2^N</code> for an option value of <code>N</code>. So the lookup texture with the default setting uses 64 samples. </p>
<p> All weights are linearly interpolated from those samples, so increasing the size of lookup table might improve the accuracy of scaler.</p>
<dt><code>&#8211;scaler-resizes-only</code></p>
<dd>Disable the scaler if the video image is not resized. In that case, <code>bilinear</code> is used instead of whatever is set with <code>&#8211;scale</code>. Bilinear will reproduce the source image perfectly if no scaling is performed. Enabled by default. Note that this option never affects <code>&#8211;cscale</code>.</p>
<dt><code>&#8211;correct-downscaling</code></p>
<dd>When using convolution based filters, extend the filter size when downscaling. Increases quality, but reduces performance while downscaling. </p>
<p> This will perform slightly sub-optimally for anamorphic video (but still better than without it) since it will extend the size to match only the milder of the scale factors between the axes. </p>
<p> Note: this option is ignored when using bilinear downscaling (the default).</p>
<dt><code>&#8211;linear-downscaling</code></p>
<dd>Scale in linear light when downscaling. It should only be used with a <code>&#8211;fbo-format</code> that has at least 16 bit precision. This option has no effect on HDR content.</p>
<dt><code>&#8211;linear-upscaling</code></p>
<dd>Scale in linear light when upscaling. Like <code>&#8211;linear-downscaling</code>, it should only be used with a <code>&#8211;fbo-format</code> that has at least 16 bits precisions. This is not usually recommended except for testing/specific purposes. Users are advised to either enable <code>&#8211;sigmoid-upscaling</code> or keep both options disabled (i.e. scaling in gamma light).</p>
<dt><code>&#8211;sigmoid-upscaling</code></p>
<dd>When upscaling, use a sigmoidal color transform to avoid emphasizing ringing artifacts. This is incompatible with and replaces <code>&#8211;linear-upscaling</code>. (Note that sigmoidization also requires linearization, so the <code>LINEAR</code> rendering step fires in both cases)</p>
<dt><code>&#8211;sigmoid-center</code></p>
<dd>The center of the sigmoid curve used for <code>&#8211;sigmoid-upscaling</code>, must be a float between 0.0 and 1.0. Defaults to 0.75 if not specified.</p>
<dt><code>&#8211;sigmoid-slope</code></p>
<dd>The slope of the sigmoid curve used for <code>&#8211;sigmoid-upscaling</code>, must be a float between 1.0 and 20.0. Defaults to 6.5 if not specified.</p>
<dt><code>&#8211;interpolation</code></p>
<dd>Reduce stuttering caused by mismatches in the video fps and display refresh rate (also known as judder). </p>
<p> <code>WARNING:</code> This requires setting the <code>&#8211;video-sync</code> option to one of the <code>display-</code> modes, or it will be silently disabled. This was not required before mpv 0.14.0. </p>
<p> This essentially attempts to interpolate the missing frames by convoluting the video along the temporal axis. The filter used can be controlled using the <code>&#8211;tscale</code> setting.</p>
<dt><code>&#8211;interpolation-threshold=&lt;0..1,-1&gt;</code></p>
<dd>Threshold below which frame ratio interpolation gets disabled (default: <code>0.01</code>). This is calculated as <code>abs(disphz/vfps &#8211; 1) &lt; threshold</code>, where <code>vfps</code> is the speed-adjusted video FPS, and <code>disphz</code> the display refresh rate. (The speed-adjusted video FPS is roughly equal to the normal video FPS, but with slowdown and speedup applied. This matters if you use <code>&#8211;video-sync=display-resample</code> to make video run synchronously to the display FPS, or if you change the <code>speed</code> property.) </p>
<p> The default is intended to enable interpolation in scenarios where retiming with the <code>&#8211;video-sync=display-*</code> cannot adjust the speed of the video sufficiently for smooth playback. For example if a video is 60.00 FPS and your display refresh rate is 59.94 Hz, interpolation will never be activated, since the mismatch is within 1% of the refresh rate. The default also handles the scenario when mpv cannot determine the container FPS, such as during certain live streams, and may dynamically toggle interpolation on and off. In this scenario, the default would be to not use interpolation but rather to allow <code>&#8211;video-sync=display-*</code> to retime the video to match display refresh rate. See <code>&#8211;video-sync-max-video-change</code> for more information about how mpv will retime video. </p>
<p> Also note that if you use e.g. <code>&#8211;video-sync=display-vdrop</code>, small deviations in the rate can disable interpolation and introduce a discontinuity every other minute. </p>
<p> Set this to <code>-1</code> to disable this logic.</p>
<dt><code>&#8211;opengl-pbo</code></p>
<dd>Enable use of PBOs. On some drivers this can be faster, especially if the source video size is huge (e.g. so called &quot;4K&quot; video). On other drivers it might be slower or cause latency issues.</p>
<dt><code>&#8211;dither-depth=&lt;N|no|auto&gt;</code></p>
<dd>Set dither target depth to N. Default: no.</p>
<dt><code>no</code></p>
<dd>Disable any dithering done by mpv.</p>
<dt><code>auto</code></p>
<dd>Automatic selection. If output bit depth cannot be detected, 8 bits per component are assumed.</p>
<dt><code>8</code></p>
<dd>Dither to 8 bit output. </p>
<p> Note that the depth of the connected video display device cannot be detected. Often, LCD panels will do dithering on their own, which conflicts with this option and leads to ugly output.</p>
<dt><code>&#8211;dither-size-fruit=&lt;2-8&gt;</code></p>
<dd>Set the size of the dither matrix (default: 6). The actual size of the matrix is <code>(2^N) x (2^N)</code> for an option value of <code>N</code>, so a value of 6 gives a size of 64&#215;64. The matrix is generated at startup time, and a large matrix can take rather long to compute (seconds). </p>
<p> Used in <code>&#8211;dither=fruit</code> mode only.</p>
<dt><code>&#8211;dither=&lt;fruit|ordered|error-diffusion|no&gt;</code></p>
<dd>Select dithering algorithm (default: fruit). (Normally, the <code>&#8211;dither-depth</code> option controls whether dithering is enabled.) </p>
<p> The <code>error-diffusion</code> option requires compute shader support. It also requires large amount of shared memory to run, the size of which depends on both the kernel (see <code>&#8211;error-diffusion</code> option below) and the height of video window. It will fallback to <code>fruit</code> dithering if there is no enough shared memory to run the shader.</p>
<dt><code>&#8211;temporal-dither</code></p>
<dd>Enable temporal dithering. (Only active if dithering is enabled in general.) This changes between 8 different dithering patterns on each frame by changing the orientation of the tiled dithering matrix. Unfortunately, this can lead to flicker on LCD displays, since these have a high reaction time.</p>
<dt><code>&#8211;temporal-dither-period=&lt;1-128&gt;</code></p>
<dd>Determines how often the dithering pattern is updated when <code>&#8211;temporal-dither</code> is in use. 1 (the default) will update on every video frame, 2 on every other frame, etc.</p>
<dt><code>&#8211;error-diffusion=&lt;kernel&gt;</code></p>
<dd>The error diffusion kernel to use when <code>&#8211;dither=error-diffusion</code> is set.</p>
<dt><code>simple</code></p>
<dd>Propagate error to only two adjacent pixels. Fastest but low quality.</p>
<dt><code>sierra-lite</code></p>
<dd>Fast with reasonable quality. This is the default.</p>
<dt><code>floyd-steinberg</code></p>
<dd>Most notable error diffusion kernel.</p>
<dt><code>atkinson</code></p>
<dd>Looks different from other kernels because only fraction of errors will be propagated during dithering. A typical use case of this kernel is saving dithered screenshot (in window mode). This kernel produces slightly smaller file, with still reasonable dithering quality. </p>
<p> There are other kernels (use <code>&#8211;error-diffusion=help</code> to list) but most of them are much slower and demanding even larger amount of shared memory. Among these kernels, <code>burkes</code> achieves a good balance between performance and quality, and probably is the one you want to try first.</p>
<dt><code>&#8211;gpu-debug</code></p>
<dd>Enables GPU debugging. What this means depends on the API type. For OpenGL, it calls <code>glGetError()</code>, and requests a debug context. For Vulkan, it enables validation layers.</p>
<dt><code>&#8211;opengl-swapinterval=&lt;n&gt;</code></p>
<dd>Interval in displayed frames between two buffer swaps. 1 is equivalent to enable VSYNC, 0 to disable VSYNC. Defaults to 1 if not specified. </p>
<p> Note that this depends on proper OpenGL vsync support. On some platforms and drivers, this only works reliably when in fullscreen mode. It may also require driver-specific hacks if using multiple monitors, to ensure mpv syncs to the right one. Compositing window managers can also lead to bad results, as can missing or incorrect display FPS information (see <code>&#8211;override-display-fps</code>).</p>
<dt><code>&#8211;vulkan-device=&lt;device name&gt;</code></p>
<dd>The name of the Vulkan device to use for rendering and presentation. Use <code>&#8211;vulkan-device=help</code> to see the list of available devices and their names. If left unspecified, the first enumerated hardware Vulkan device will be used.</p>
<dt><code>&#8211;vulkan-swap-mode=&lt;mode&gt;</code></p>
<dd>Controls the presentation mode of the vulkan swapchain. This is similar to the <code>&#8211;opengl-swapinterval</code> option.</p>
<dt><code>auto</code></p>
<dd>Use the preferred swapchain mode for the vulkan context. (Default)</p>
<dt><code>fifo</code></p>
<dd>Non-tearing, vsync blocked. Similar to &quot;VSync on&quot;.</p>
<dt><code>fifo-relaxed</code></p>
<dd>Tearing, vsync blocked. Late frames will tear instead of stuttering.</p>
<dt><code>mailbox</code></p>
<dd>Non-tearing, not vsync blocked. Similar to &quot;triple buffering&quot;.</p>
<dt><code>immediate</code></p>
<dd>Tearing, not vsync blocked. Similar to &quot;VSync off&quot;.</p>
<dt><code>&#8211;vulkan-queue-count=&lt;1..8&gt;</code></p>
<dd>Controls the number of VkQueues used for rendering (limited by how many your device supports). In theory, using more queues could enable some parallelism between frames (when using a <code>&#8211;swapchain-depth</code> higher than 1), but it can also slow things down on hardware where there&#8217;s no true parallelism between queues. (Default: 1)</p>
<dt><code>&#8211;vulkan-async-transfer</code></p>
<dd>Enables the use of async transfer queues on supported vulkan devices. Using them allows transfer operations like texture uploads and blits to happen concurrently with the actual rendering, thus improving overall throughput and power consumption. Enabled by default, and should be relatively safe.</p>
<dt><code>&#8211;vulkan-async-compute</code></p>
<dd>Enables the use of async compute queues on supported vulkan devices. Using this, in theory, allows out-of-order scheduling of compute shaders with graphics shaders, thus enabling the hardware to do more effective work while waiting for pipeline bubbles and memory operations. Not beneficial on all GPUs. It&#8217;s worth noting that if async compute is enabled, and the device supports more compute queues than graphics queues (bound by the restrictions set by <code>&#8211;vulkan-queue-count</code>), mpv will internally try and prefer the use of compute shaders over fragment shaders wherever possible. Enabled by default, although Nvidia users may want to disable it.</p>
<dt><code>&#8211;vulkan-disable-events</code></p>
<dd>Disable the use of VkEvents, for debugging purposes or for compatibility with some older drivers / vulkan portability layers that don&#8217;t provide working VkEvent support.</p>
<dt><code>&#8211;vulkan-display-display=&lt;n&gt;</code></p>
<dd>The index of the display, on the selected Vulkan device, to present on when using the <code>displayvk</code> GPU context. Use <code>&#8211;vulkan-display-display=help</code> to see the list of available displays. If left unspecified, the first enumerated display will be used.</p>
<dt><code>&#8211;vulkan-display-mode=&lt;n&gt;</code></p>
<dd>The index of the display mode, of the selected Vulkan display, to use when using the <code>displayvk</code> GPU context. Use <code>&#8211;vulkan-display-mode=help</code> to see the list of available modes. If left unspecified, the first enumerated mode will be used.</p>
<dt><code>&#8211;vulkan-display-plane=&lt;n&gt;</code></p>
<dd>The index of the plane, on the selected Vulkan device, to present on when using the <code>displayvk</code> GPU context. Use <code>&#8211;vulkan-display-plane=help</code> to see the list of available planes. If left unspecified, the first enumerated plane will be used.</p>
<dt><code>&#8211;d3d11-exclusive-fs=&lt;yes|no&gt;</code></p>
<dd>Switches the D3D11 swap chain fullscreen state to &#8216;fullscreen&#8217; when fullscreen video is requested. Also known as &quot;exclusive fullscreen&quot; or &quot;D3D fullscreen&quot; in other applications. Gives mpv full control of rendering on the swap chain&#8217;s screen. Off by default.</p>
<dt><code>&#8211;d3d11-warp=&lt;yes|no|auto&gt;</code></p>
<dd>Use WARP (Windows Advanced Rasterization Platform) with the D3D11 GPU backend (default: auto). This is a high performance software renderer. By default, it is only used when the system has no hardware adapters that support D3D11. While the extended GPU features will work with WARP, they can be very slow.</p>
<dt><code>&#8211;d3d11-feature-level=&lt;12_1|12_0|11_1|11_0|10_1|10_0|9_3|9_2|9_1&gt;</code></p>
<dd>Select a specific feature level when using the D3D11 GPU backend. By default, the highest available feature level is used. This option can be used to select a lower feature level, which is mainly useful for debugging. Most extended GPU features will not work at 9_x feature levels.</p>
<dt><code>&#8211;d3d11-flip=&lt;yes|no&gt;</code></p>
<dd>Enable flip-model presentation, which avoids unnecessarily copying the backbuffer by sharing surfaces with the DWM (default: yes). This may cause performance issues with older drivers. If flip-model presentation is not supported (for example, on Windows 7 without the platform update), mpv will automatically fall back to the older bitblt presentation model.</p>
<dt><code>&#8211;d3d11-sync-interval=&lt;0..4&gt;</code></p>
<dd>Schedule each frame to be presented for this number of VBlank intervals. (default: 1) Setting to 1 will enable VSync, setting to 0 will disable it.</p>
<dt><code>&#8211;d3d11-adapter=&lt;adapter name|help&gt;</code></p>
<dd>Select a specific D3D11 adapter to utilize for D3D11 rendering. Will pick the default adapter if unset. Alternatives are listed when the name &quot;help&quot; is given. </p>
<p> Checks for matches based on the start of the string, case insensitive. Thus, if the description of the adapter starts with the vendor name, that can be utilized as the selection parameter. </p>
<p> Hardware decoders utilizing the D3D11 rendering abstraction&#8217;s helper functionality to receive a device, such as D3D11VA or DXVA2&#8217;s DXGI mode, will be affected by this choice.</p>
<dt><code>&#8211;d3d11-output-format=&lt;auto|rgba8|bgra8|rgb10_a2|rgba16f&gt;</code></p>
<dd>Select a specific D3D11 output format to utilize for D3D11 rendering. &quot;auto&quot; is the default, which will pick either rgba8 or rgb10_a2 depending on the configured desktop bit depth. rgba16f and bgra8 are left out of the autodetection logic, and are available for manual testing. </p>
<p> <code>NOTE:</code> Desktop bit depth querying is only available from an API available from Windows 10. Thus on older systems it will only automatically utilize the rgba8 output format.</p>
<dt><code>&#8211;d3d11-output-csp=&lt;auto|srgb|linear|pq|bt.2020&gt;</code></p>
<dd>Select a specific D3D11 output color space to utilize for D3D11 rendering. &quot;auto&quot; is the default, which will select the color space of the desktop on which the swap chain is located. </p>
<p> Values other than &quot;srgb&quot; and &quot;pq&quot; have had issues in testing, so they are mostly available for manual testing. </p>
<p> <code>NOTE:</code> Swap chain color space configuration is only available from an API available from Windows 10. Thus on older systems it will not work.</p>
<dt><code>&#8211;d3d11va-zero-copy=&lt;yes|no&gt;</code></p>
<dd>By default, when using hardware decoding with <code>&#8211;gpu-api=d3d11</code>, the video image will be copied (GPU-to-GPU) from the decoder surface to a shader resource. Set this option to avoid that copy by sampling directly from the decoder image. This may increase performance and reduce power usage, but can cause the image to be sampled incorrectly on the bottom and right edges due to padding, and may invoke driver bugs, since Direct3D 11 technically does not allow sampling from a decoder surface (though most drivers support it.) </p>
<p> Currently only relevant for <code>&#8211;gpu-api=d3d11</code>.</p>
<dt><code>&#8211;wayland-app-id=&lt;string&gt;</code></p>
<dd>Set the client app id for Wayland-based video output methods (default: <code>mpv</code>).</p>
<dt><code>&#8211;wayland-disable-vsync=&lt;yes|no&gt;</code></p>
<dd>Disable vsync for the wayland contexts (default: no). Useful for benchmarking the wayland context when combined with <code>video-sync=display-desync</code>, <code>&#8211;no-audio</code>, and <code>&#8211;untimed=yes</code>. Only works with <code>&#8211;gpu-context=wayland</code> and <code>&#8211;gpu-context=waylandvk</code>.</p>
<dt><code>&#8211;wayland-edge-pixels-pointer=&lt;value&gt;</code></p>
<dd>Defines the size of an edge border (default: 10) to initiate client side resize events in the wayland contexts with the mouse. This is only active if there are no server side decorations from the compositor.</p>
<dt><code>&#8211;wayland-edge-pixels-touch=&lt;value&gt;</code></p>
<dd>Defines the size of an edge border (default: 32) to initiate client side resizes events in the wayland contexts with touch events.</p>
<dt><code>&#8211;spirv-compiler=&lt;compiler&gt;</code></p>
<dd>Controls which compiler is used to translate GLSL to SPIR-V. This is (currently) only relevant for <code>&#8211;gpu-api=vulkan</code> and <i>&#8211;gpu-api=d3d11</i>. The possible choices are currently only:</p>
<dt><code>auto</code></p>
<dd>Use the first available compiler. (Default)</p>
<dt><code>shaderc</code></p>
<dd>Use libshaderc, which is an API wrapper around glslang. This is generally the most preferred, if available. </p>
<p> <code>NOTE:</code> This option is deprecated, since there is only one reasonable value. It may be removed in the future.</p>
<dt><code>&#8211;glsl-shader=&lt;file&gt;</code>, <code>&#8211;glsl-shaders=&lt;file-list&gt;</code></p>
<dd>Custom GLSL hooks. These are a flexible way to add custom fragment shaders, which can be injected at almost arbitrary points in the rendering pipeline, and access all previous intermediate textures. </p>
<p> Each use of the <code>&#8211;glsl-shader</code> option will add another file to the internal list of shaders, while <code>&#8211;glsl-shaders</code> takes a list of files, and overwrites the internal list with it. The latter is a path list option (see <i>List Options</i> for details).</p>
<dt>Warning</p>
<dd>The syntax is not stable yet and may change any time. </p>
<p> The general syntax of a user shader looks like this: </p>
<pre>//!METADATA ARGS...
//!METADATA ARGS...
vec4 hook() {
 ...
 return something;
}
//!METADATA ARGS...
//!METADATA ARGS...
...</pre>
<p>Each section of metadata, along with the non-metadata lines after it, defines a single block. There are currently two types of blocks, HOOKs and TEXTUREs. </p>
<p> A <code>TEXTURE</code> block can set the following options:</p>
<dt><code>TEXTURE &lt;name&gt; (required)</code></p>
<dd>The name of this texture. Hooks can then bind the texture under this name using BIND. This must be the first option of the texture block.</p>
<dt><code>SIZE &lt;width&gt; [&lt;height&gt;] [&lt;depth&gt;] (required)</code></p>
<dd>The dimensions of the texture. The height and depth are optional. The type of texture (1D, 2D or 3D) depends on the number of components specified.</p>
<dt><code>FORMAT &lt;name&gt; (required)</code></p>
<dd>The texture format for the samples. Supported texture formats are listed in debug logging when the <code>gpu</code> VO is initialized (look for <code>Texture formats:</code>). Usually, this follows OpenGL naming conventions. For example, <code>rgb16</code> provides 3 channels with normalized 16 bit components. One oddity are float formats: for example, <code>rgba16f</code> has 16 bit internal precision, but the texture data is provided as 32 bit floats, and the driver converts the data on texture upload. </p>
<p> Although format names follow a common naming convention, not all of them are available on all hardware, drivers, GL versions, and so on.</p>
<dt><code>FILTER &lt;LINEAR|NEAREST&gt;</code></p>
<dd>The min/magnification filter used when sampling from this texture.</p>
<dt><code>BORDER &lt;CLAMP|REPEAT|MIRROR&gt;</code></p>
<dd>The border wrapping mode used when sampling from this texture. </p>
<p> Following the metadata is a string of bytes in hexadecimal notation that define the raw texture data, corresponding to the format specified by <i>FORMAT</i>, on a single line with no extra whitespace. </p>
<p> A <code>HOOK</code> block can set the following options:</p>
<dt><code>HOOK &lt;name&gt; (required)</code></p>
<dd>The texture which to hook into. May occur multiple times within a metadata block, up to a predetermined limit. See below for a list of hookable textures.</p>
<dt><code>DESC &lt;title&gt;</code></p>
<dd>User-friendly description of the pass. This is the name used when representing this shader in the list of passes for property <i>vo-passes</i>.</p>
<dt><code>BIND &lt;name&gt;</code></p>
<dd>Loads a texture (either coming from mpv or from a <code>TEXTURE</code> block) and makes it available to the pass. When binding textures from mpv, this will also set up macros to facilitate accessing it properly. See below for a list. By default, no textures are bound. The special name HOOKED can be used to refer to the texture that triggered this pass.</p>
<dt><code>SAVE &lt;name&gt;</code></p>
<dd>Gives the name of the texture to save the result of this pass into. By default, this is set to the special name HOOKED which has the effect of overwriting the hooked texture.</p>
<dt><code>WIDTH &lt;szexpr&gt;, HEIGHT &lt;szexpr&gt;</code></p>
<dd>Specifies the size of the resulting texture for this pass. <code>szexpr</code> refers to an expression in RPN (reverse polish notation), using the operators + &#8211; * / &gt; &lt; !, floating point literals, and references to sizes of existing texture (such as MAIN.width or CHROMA.height), OUTPUT, or NATIVE_CROPPED (size of an input texture cropped after pan-and-scan, video-align-x/y, video-pan-x/y, etc. and possibly prescaled). By default, these are set to HOOKED.w and HOOKED.h, espectively.</p>
<dt><code>WHEN &lt;szexpr&gt;</code></p>
<dd>Specifies a condition that needs to be true (non-zero) for the shader stage to be evaluated. If it fails, it will silently be omitted. (Note that a shader stage like this which has a dependency on an optional hook point can still cause that hook point to be saved, which has some minor overhead)</p>
<dt><code>OFFSET &lt;ox oy | ALIGN&gt;</code></p>
<dd>Indicates a pixel shift (offset) introduced by this pass. These pixel offsets will be accumulated and corrected during the next scaling pass (<code>cscale</code> or <code>scale</code>). The default values are 0 0 which correspond to no shift. Note that offsets are ignored when not overwriting the hooked texture. </p>
<p> A special value of <code>ALIGN</code> will attempt to fix existing offset of HOOKED by align it with reference. It requires HOOKED to be resizable (see below). It works transparently with fragment shader. For compute shader, the predefined <code>texmap</code> macro is required to handle coordinate mapping.</p>
<dt><code>COMPONENTS &lt;n&gt;</code></p>
<dd>Specifies how many components of this pass&#8217;s output are relevant and should be stored in the texture, up to 4 (rgba). By default, this value is equal to the number of components in HOOKED.</p>
<dt><code>COMPUTE &lt;bw&gt; &lt;bh&gt; [&lt;tw&gt; &lt;th&gt;]</code></p>
<dd>Specifies that this shader should be treated as a compute shader, with the block size bw and bh. The compute shader will be dispatched with however many blocks are necessary to completely tile over the output. Within each block, there will be tw*th threads, forming a single work group. In other words: tw and th specify the work group size, which can be different from the block size. So for example, a compute shader with bw, bh = 32 and tw, th = 8 running on a 500&#215;500 texture would dispatch 16&#215;16 blocks (rounded up), each with 8&#215;8 threads. </p>
<p> Compute shaders in mpv are treated a bit different from fragment shaders. Instead of defining a <code>vec4 hook</code> that produces an output sample, you directly define <code>void hook</code> which writes to a fixed writeonly image unit named <code>out_image</code> (this is bound by mpv) using <i>imageStore</i>. To help translate texture coordinates in the absence of vertices, mpv provides a special function <code>NAME_map(id)</code> to map from the texel space of the output image to the texture coordinates for all bound textures. In particular, <code>NAME_pos</code> is equivalent to <code>NAME_map(gl_GlobalInvocationID)</code>, although using this only really makes sense if (tw,th) == (bw,bh). </p>
<p> Each bound mpv texture (via <code>BIND</code>) will make available the following definitions to that shader pass, where NAME is the name of the bound texture:</p>
<dt><code>vec4 NAME_tex(vec2 pos)</code></p>
<dd>The sampling function to use to access the texture at a certain spot (in texture coordinate space, range [0,1]). This takes care of any necessary normalization conversions.</p>
<dt><code>vec4 NAME_texOff(vec2 offset)</code></p>
<dd>Sample the texture at a certain offset in pixels. This works like NAME_tex but additionally takes care of necessary rotations, so that sampling at e.g. vec2(-1,0) is always one pixel to the left.</p>
<dt><code>vec2 NAME_pos</code></p>
<dd>The local texture coordinate of that texture, range [0,1].</p>
<dt><code>vec2 NAME_size</code></p>
<dd>The (rotated) size in pixels of the texture.</p>
<dt><code>mat2 NAME_rot</code></p>
<dd>The rotation matrix associated with this texture. (Rotates pixel space to texture coordinates)</p>
<dt><code>vec2 NAME_pt</code></p>
<dd>The (unrotated) size of a single pixel, range [0,1].</p>
<dt><code>float NAME_mul</code></p>
<dd>The coefficient that needs to be multiplied into the texture contents in order to normalize it to the range [0,1].</p>
<dt><code>sampler NAME_raw</code></p>
<dd>The raw bound texture itself. The use of this should be avoided unless absolutely necessary. </p>
<p> Normally, users should use either NAME_tex or NAME_texOff to read from the texture. For some shaders however , it can be better for performance to do custom sampling from NAME_raw, in which case care needs to be taken to respect NAME_mul and NAME_rot. </p>
<p> In addition to these parameters, the following uniforms are also globally available:</p>
<dt><code>float random</code></p>
<dd>A random number in the range [0-1], different per frame.</p>
<dt><code>int frame</code></p>
<dd>A simple count of frames rendered, increases by one per frame and never resets (regardless of seeks).</p>
<dt><code>vec2 input_size</code></p>
<dd>The size in pixels of the input image (possibly cropped and prescaled).</p>
<dt><code>vec2 target_size</code></p>
<dd>The size in pixels of the visible part of the scaled (and possibly cropped) image.</p>
<dt><code>vec2 tex_offset</code></p>
<dd>Texture offset introduced by user shaders or options like panscan, video-align-x/y, video-pan-x/y. </p>
<p> Internally, vo_gpu may generate any number of the following textures. Whenever a texture is rendered and saved by vo_gpu, all of the passes that have hooked into it will run, in the order they were added by the user. This is a list of the legal hook points:</p>
<dt><code>RGB, LUMA, CHROMA, ALPHA, XYZ (resizable)</code></p>
<dd>Source planes (raw). Which of these fire depends on the image format of the source.</p>
<dt><code>CHROMA_SCALED, ALPHA_SCALED (fixed)</code></p>
<dd>Source planes (upscaled). These only fire on subsampled content.</p>
<dt><code>NATIVE (resizable)</code></p>
<dd>The combined image, in the source colorspace, before conversion to RGB.</p>
<dt><code>MAINPRESUB (resizable)</code></p>
<dd>The image, after conversion to RGB, but before <code>&#8211;blend-subtitles=video</code> is applied.</p>
<dt><code>MAIN (resizable)</code></p>
<dd>The main image, after conversion to RGB but before upscaling.</p>
<dt><code>LINEAR (fixed)</code></p>
<dd>Linear light image, before scaling. This only fires when <code>&#8211;linear-upscaling</code>, <code>&#8211;linear-downscaling</code> or <code>&#8211;sigmoid-upscaling</code> is in effect.</p>
<dt><code>SIGMOID (fixed)</code></p>
<dd>Sigmoidized light, before scaling. This only fires when <code>&#8211;sigmoid-upscaling</code> is in effect.</p>
<dt><code>PREKERNEL (fixed)</code></p>
<dd>The image immediately before the scaler kernel runs.</p>
<dt><code>POSTKERNEL (fixed)</code></p>
<dd>The image immediately after the scaler kernel runs.</p>
<dt><code>SCALED (fixed)</code></p>
<dd>The final upscaled image, before color management.</p>
<dt><code>OUTPUT (fixed)</code></p>
<dd>The final output image, after color management but before dithering and drawing to screen. </p>
<p> Only the textures labelled with <code>resizable</code> may be transformed by the pass. When overwriting a texture marked <code>fixed</code>, the WIDTH, HEIGHT and OFFSET must be left at their default values.</p>
<dt><code>&#8211;glsl-shader=&lt;file&gt;</code></p>
<dd>CLI/config file only alias for <code>&#8211;glsl-shaders-append</code>.</p>
<dt><code>&#8211;deband</code></p>
<dd>Enable the debanding algorithm. This greatly reduces the amount of visible banding, blocking and other quantization artifacts, at the expense of very slightly blurring some of the finest details. In practice, it&#8217;s virtually always an improvement &#8211; the only reason to disable it would be for performance.</p>
<dt><code>&#8211;deband-iterations=&lt;1..16&gt;</code></p>
<dd>The number of debanding steps to perform per sample. Each step reduces a bit more banding, but takes time to compute. Note that the strength of each step falls off very quickly, so high numbers (&gt;4) are practically useless. (Default 1)</p>
<dt><code>&#8211;deband-threshold=&lt;0..4096&gt;</code></p>
<dd>The debanding filter&#8217;s cut-off threshold. Higher numbers increase the debanding strength dramatically but progressively diminish image details. (Default 32)</p>
<dt><code>&#8211;deband-range=&lt;1..64&gt;</code></p>
<dd>The debanding filter&#8217;s initial radius. The radius increases linearly for each iteration. A higher radius will find more gradients, but a lower radius will smooth more aggressively. (Default 16) </p>
<p> If you increase the <code>&#8211;deband-iterations</code>, you should probably decrease this to compensate.</p>
<dt><code>&#8211;deband-grain=&lt;0..4096&gt;</code></p>
<dd>Add some extra noise to the image. This significantly helps cover up remaining quantization artifacts. Higher numbers add more noise. (Default 48)</p>
<dt><code>&#8211;sharpen=&lt;value&gt;</code></p>
<dd>If set to a value other than 0, enable an unsharp masking filter. Positive values will sharpen the image (but add more ringing and aliasing). Negative values will blur the image. If your GPU is powerful enough, consider alternatives like the <code>ewa_lanczossharp</code> scale filter, or the <code>&#8211;scale-blur</code> option.</p>
<dt><code>&#8211;opengl-glfinish</code></p>
<dd>Call <code>glFinish()</code> before swapping buffers (default: disabled). Slower, but might improve results when doing framedropping. Can completely ruin performance. The details depend entirely on the OpenGL driver.</p>
<dt><code>&#8211;opengl-waitvsync</code></p>
<dd>Call <code>glXWaitVideoSyncSGI</code> after each buffer swap (default: disabled). This may or may not help with video timing accuracy and frame drop. It&#8217;s possible that this makes video output slower, or has no effect at all. </p>
<p> X11/GLX only.</p>
<dt><code>&#8211;opengl-dwmflush=&lt;no|windowed|yes|auto&gt;</code></p>
<dd>Calls <code>DwmFlush</code> after swapping buffers on Windows (default: auto). It also sets <code>SwapInterval(0)</code> to ignore the OpenGL timing. Values are: no (disabled), windowed (only in windowed mode), yes (also in full screen). </p>
<p> The value <code>auto</code> will try to determine whether the compositor is active, and calls <code>DwmFlush</code> only if it seems to be. </p>
<p> This may help to get more consistent frame intervals, especially with high-fps clips &#8211; which might also reduce dropped frames. Typically, a value of <code>windowed</code> should be enough, since full screen may bypass the DWM. </p>
<p> Windows only.</p>
<dt><code>&#8211;angle-d3d11-feature-level=&lt;11_0|10_1|10_0|9_3&gt;</code></p>
<dd>Selects a specific feature level when using the ANGLE backend with D3D11. By default, the highest available feature level is used. This option can be used to select a lower feature level, which is mainly useful for debugging. Note that OpenGL ES 3.0 is only supported at feature level 10_1 or higher. Most extended OpenGL features will not work at lower feature levels (similar to <code>&#8211;gpu-dumb-mode</code>). </p>
<p> Windows with ANGLE only.</p>
<dt><code>&#8211;angle-d3d11-warp=&lt;yes|no|auto&gt;</code></p>
<dd>Use WARP (Windows Advanced Rasterization Platform) when using the ANGLE backend with D3D11 (default: auto). This is a high performance software renderer. By default, it is used when the Direct3D hardware does not support Direct3D 11 feature level 9_3. While the extended OpenGL features will work with WARP, they can be very slow. </p>
<p> Windows with ANGLE only.</p>
<dt><code>&#8211;angle-egl-windowing=&lt;yes|no|auto&gt;</code></p>
<dd>Use ANGLE&#8217;s built in EGL windowing functions to create a swap chain (default: auto). If this is set to <code>no</code> and the D3D11 renderer is in use, ANGLE&#8217;s built in swap chain will not be used and a custom swap chain that is optimized for video rendering will be created instead. If set to <code>auto</code>, a custom swap chain will be used for D3D11 and the built in swap chain will be used for D3D9. This option is mainly for debugging purposes, in case the custom swap chain has poor performance or does not work. </p>
<p> If set to <code>yes</code>, the <code>&#8211;angle-max-frame-latency</code>, <code>&#8211;angle-swapchain-length</code> and <code>&#8211;angle-flip</code> options will have no effect. </p>
<p> Windows with ANGLE only.</p>
<dt><code>&#8211;angle-flip=&lt;yes|no&gt;</code></p>
<dd>Enable flip-model presentation, which avoids unnecessarily copying the backbuffer by sharing surfaces with the DWM (default: yes). This may cause performance issues with older drivers. If flip-model presentation is not supported (for example, on Windows 7 without the platform update), mpv will automatically fall back to the older bitblt presentation model. </p>
<p> If set to <code>no</code>, the <code>&#8211;angle-swapchain-length</code> option will have no effect. </p>
<p> Windows with ANGLE only.</p>
<dt><code>&#8211;angle-renderer=&lt;d3d9|d3d11|auto&gt;</code></p>
<dd>Forces a specific renderer when using the ANGLE backend (default: auto). In auto mode this will pick D3D11 for systems that support Direct3D 11 feature level 9_3 or higher, and D3D9 otherwise. This option is mainly for debugging purposes. Normally there is no reason to force a specific renderer, though <code>&#8211;angle-renderer=d3d9</code> may give slightly better performance on old hardware. Note that the D3D9 renderer only supports OpenGL ES 2.0, so most extended OpenGL features will not work if this renderer is selected (similar to <code>&#8211;gpu-dumb-mode</code>). </p>
<p> Windows with ANGLE only.</p>
<dt><code>&#8211;macos-force-dedicated-gpu=&lt;yes|no&gt;</code></p>
<dd>Deactivates the automatic graphics switching and forces the dedicated GPU. (default: no) </p>
<p> macOS only.</p>
<dt><code>&#8211;cocoa-cb-sw-renderer=&lt;yes|no|auto&gt;</code></p>
<dd>Use the Apple Software Renderer when using cocoa-cb (default: auto). If set to <code>no</code> the software renderer is never used and instead fails when a the usual pixel format could not be created, <code>yes</code> will always only use the software renderer, and <code>auto</code> only falls back to the software renderer when the usual pixel format couldn&#8217;t be created. </p>
<p> macOS only.</p>
<dt><code>&#8211;cocoa-cb-10bit-context=&lt;yes|no&gt;</code></p>
<dd>Creates a 10bit capable pixel format for the context creation (default: yes). Instead of 8bit integer framebuffer a 16bit half-float framebuffer is requested. </p>
<p> macOS only.</p>
<dt><code>&#8211;macos-title-bar-appearance=&lt;appearance&gt;</code></p>
<dd>Sets the appearance of the title bar (default: auto). Not all combinations of appearances and <code>&#8211;macos-title-bar-material</code> materials make sense or are unique. Appearances that are not supported by you current macOS version fall back to the default value. macOS and cocoa-cb only </p>
<p> <code>&lt;appearance&gt;</code> can be one of the following:</p>
<dt><code>auto</code></p>
<dd>Detects the system settings and sets the title bar appearance appropriately. On macOS 10.14 it also detects run time changes.</p>
<dt><code>aqua</code></p>
<dd>The standard macOS Light appearance.</p>
<dt><code>darkAqua</code></p>
<dd>The standard macOS Dark appearance. (macOS 10.14+)</p>
<dt><code>vibrantLight</code></p>
<dd>Light vibrancy appearance with.</p>
<dt><code>vibrantDark</code></p>
<dd>Dark vibrancy appearance with.</p>
<dt><code>aquaHighContrast</code></p>
<dd>Light Accessibility appearance. (macOS 10.14+)</p>
<dt><code>darkAquaHighContrast</code></p>
<dd>Dark Accessibility appearance. (macOS 10.14+)</p>
<dt><code>vibrantLightHighContrast</code></p>
<dd>Light vibrancy Accessibility appearance. (macOS 10.14+)</p>
<dt><code>vibrantDarkHighContrast</code></p>
<dd>Dark vibrancy Accessibility appearance. (macOS 10.14+)</p>
<dt><code>&#8211;macos-title-bar-material=&lt;material&gt;</code></p>
<dd>Sets the material of the title bar (default: titlebar). All deprecated materials should not be used on macOS 10.14+ because their functionality is not guaranteed. Not all combinations of materials and <code>&#8211;macos-title-bar-appearance</code> appearances make sense or are unique. Materials that are not supported by you current macOS version fall back to the default value. macOS and cocoa-cb only </p>
<p> <code>&lt;material&gt;</code> can be one of the following:</p>
<dt><code>titlebar</code></p>
<dd>The standard macOS titel bar material.</p>
<dt><code>selection</code></p>
<dd>The standard macOS selection material.</p>
<dt><code>menu</code></p>
<dd>The standard macOS menu material. (macOS 10.11+)</p>
<dt><code>popover</code></p>
<dd>The standard macOS popover material. (macOS 10.11+)</p>
<dt><code>sidebar</code></p>
<dd>The standard macOS sidebar material. (macOS 10.11+)</p>
<dt><code>headerView</code></p>
<dd>The standard macOS header view material. (macOS 10.14+)</p>
<dt><code>sheet</code></p>
<dd>The standard macOS sheet material. (macOS 10.14+)</p>
<dt><code>windowBackground</code></p>
<dd>The standard macOS window background material. (macOS 10.14+)</p>
<dt><code>hudWindow</code></p>
<dd>The standard macOS hudWindow material. (macOS 10.14+)</p>
<dt><code>fullScreen</code></p>
<dd>The standard macOS full screen material. (macOS 10.14+)</p>
<dt><code>toolTip</code></p>
<dd>The standard macOS tool tip material. (macOS 10.14+)</p>
<dt><code>contentBackground</code></p>
<dd>The standard macOS content background material. (macOS 10.14+)</p>
<dt><code>underWindowBackground</code></p>
<dd>The standard macOS under window background material. (macOS 10.14+)</p>
<dt><code>underPageBackground</code></p>
<dd>The standard macOS under page background material. (deprecated in macOS 10.14+)</p>
<dt><code>dark</code></p>
<dd>The standard macOS dark material. (deprecated in macOS 10.14+)</p>
<dt><code>light</code></p>
<dd>The standard macOS light material. (macOS 10.14+)</p>
<dt><code>mediumLight</code></p>
<dd>The standard macOS mediumLight material. (macOS 10.11+, deprecated in macOS 10.14+)</p>
<dt><code>ultraDark</code></p>
<dd>The standard macOS ultraDark material. (macOS 10.11+ deprecated in macOS 10.14+)</p>
<dt><code>&#8211;macos-title-bar-color=&lt;color&gt;</code></p>
<dd>Sets the color of the title bar (default: completely transparent). Is influenced by <code>&#8211;macos-title-bar-appearance</code> and <code>&#8211;macos-title-bar-material</code>. See <code>&#8211;sub-color</code> for color syntax.</p>
<dt><code>&#8211;macos-fs-animation-duration=&lt;default|0-1000&gt;</code></p>
<dd>Sets the fullscreen resize animation duration in ms (default: default). The default value is slightly less than the system&#8217;s animation duration (500ms) to prevent some problems when the end of an async animation happens at the same time as the end of the system wide fullscreen animation. Setting anything higher than 500ms will only prematurely cancel the resize animation after the system wide animation ended. The upper limit is still set at 1000ms since it&#8217;s possible that Apple or the user changes the system defaults. Anything higher than 1000ms though seems too long and shouldn&#8217;t be set anyway. (macOS and cocoa-cb only)</p>
<dt><code>&#8211;macos-app-activation-policy=&lt;regular|accessory|prohibited&gt;</code></p>
<dd>Changes the App activation policy. With accessory the mpv icon in the Dock can be hidden. (default: regular) </p>
<p> macOS only.</p>
<dt><code>&#8211;macos-geometry-calculation=&lt;visible|whole&gt;</code></p>
<dd>This changes the rectangle which is used to calculate the screen position and size of the window (default: visible). <code>visible</code> takes the the menu bar and Dock into account and the window is only positioned/sized within the visible screen frame rectangle, <code>whole</code> takes the whole screen frame rectangle and ignores the menu bar and Dock. Other previous restrictions still apply, like the window can&#8217;t be placed on top of the menu bar etc. </p>
<p> macOS only.</p>
<dt><code>&#8211;android-surface-size=&lt;WxH&gt;</code></p>
<dd>Set dimensions of the rendering surface used by the Android gpu context. Needs to be set by the embedding application if the dimensions change during runtime (i.e. if the device is rotated), via the surfaceChanged callback. </p>
<p> Android with <code>&#8211;gpu-context=android</code> only.</p>
<dt><code>&#8211;gpu-sw</code></p>
<dd>Continue even if a software renderer is detected.</p>
<dt><code>&#8211;gpu-context=&lt;sys&gt;</code></p>
<dd>The value <code>auto</code> (the default) selects the GPU context. You can also pass <code>help</code> to get a complete list of compiled in backends (sorted by autoprobe order).</p>
<dt><code>auto</code></p>
<dd>auto-select (default)</p>
<dt><code>cocoa</code></p>
<dd>Cocoa/macOS (deprecated, use &#8211;vo=libmpv instead)</p>
<dt><code>win</code></p>
<dd>Win32/WGL</p>
<dt><code>winvk</code></p>
<dd>VK_KHR_win32_surface</p>
<dt><code>angle</code></p>
<dd>Direct3D11 through the OpenGL ES translation layer ANGLE. This supports almost everything the <code>win</code> backend does (if the ANGLE build is new enough).</p>
<dt><code>dxinterop (experimental)</code></p>
<dd>Win32, using WGL for rendering and Direct3D 9Ex for presentation. Works on Nvidia and AMD. Newer Intel chips with the latest drivers may also work.</p>
<dt><code>d3d11</code></p>
<dd>Win32, with native Direct3D 11 rendering.</p>
<dt><code>x11</code></p>
<dd>X11/GLX</p>
<dt><code>x11vk</code></p>
<dd>VK_KHR_xlib_surface</p>
<dt><code>wayland</code></p>
<dd>Wayland/EGL</p>
<dt><code>waylandvk</code></p>
<dd>VK_KHR_wayland_surface</p>
<dt><code>drm</code></p>
<dd>DRM/EGL</p>
<dt><code>displayvk</code></p>
<dd>VK_KHR_display. This backend is roughly the Vukan equivalent of DRM/EGL, allowing for direct rendering via Vulkan without a display manager.</p>
<dt><code>x11egl</code></p>
<dd>X11/EGL</p>
<dt><code>android</code></p>
<dd>Android/EGL. Requires <code>&#8211;wid</code> be set to an <code>android.view.Surface</code>.</p>
<dt><code>&#8211;gpu-api=&lt;type&gt;</code></p>
<dd>Controls which type of graphics APIs will be accepted:</p>
<dt><code>auto</code></p>
<dd>Use any available API (default)</p>
<dt><code>opengl</code></p>
<dd>Allow only OpenGL (requires OpenGL 2.1+ or GLES 2.0+)</p>
<dt><code>vulkan</code></p>
<dd>Allow only Vulkan (requires a valid/working <code>&#8211;spirv-compiler</code>)</p>
<dt><code>d3d11</code></p>
<dd>Allow only <code>&#8211;gpu-context=d3d11</code></p>
<dt><code>&#8211;opengl-es=&lt;mode&gt;</code></p>
<dd>Controls which type of OpenGL context will be accepted:</p>
<dt><code>auto</code></p>
<dd>Allow all types of OpenGL (default)</p>
<dt><code>yes</code></p>
<dd>Only allow GLES</p>
<dt><code>no</code></p>
<dd>Only allow desktop/core GL</p>
<dt><code>&#8211;fbo-format=&lt;fmt&gt;</code></p>
<dd>Selects the internal format of textures used for FBOs. The format can influence performance and quality of the video output. <code>fmt</code> can be one of: rgb8, rgb10, rgb10_a2, rgb16, rgb16f, rgb32f, rgba12, rgba16, rgba16f, rgba16hf, rgba32f. </p>
<p> Default: <code>auto</code>, which first attempts to utilize 16bit float (rgba16f, rgba16hf), and falls back to rgba16 if those are not available. Finally, attempts to utilize rgb10_a2 or rgba8 if all of the previous formats are not available.</p>
<dt><code>&#8211;gamma-factor=&lt;0.1..2.0&gt;</code></p>
<dd>Set an additional raw gamma factor (default: 1.0). If gamma is adjusted in other ways (like with the <code>&#8211;gamma</code> option or key bindings and the <code>gamma</code> property), the value is multiplied with the other gamma value. </p>
<p> Recommended values based on the environmental brightness:</p>
<dt><code>1.0</code></p>
<dd>Pitch black or dimly lit room (default)</p>
<dt><code>1.1</code></p>
<dd>Moderately lit room, home</p>
<dt><code>1.2</code></p>
<dd>Brightly illuminated room, office </p>
<p> NOTE: This is based around the assumptions of typical movie content, which contains an implicit end-to-end of about 0.8 from scene to display. For bright environments it can be useful to cancel that out.</p>
<dt><code>&#8211;gamma-auto</code></p>
<dd>Automatically corrects the gamma value depending on ambient lighting conditions (adding a gamma boost for bright rooms). </p>
<p> With ambient illuminance of 16 lux, mpv will pick the 1.0 gamma value (no boost), and slightly increase the boost up until 1.2 for 256 lux. </p>
<p> NOTE: Only implemented on macOS.</p>
<dt><code>&#8211;target-prim=&lt;value&gt;</code></p>
<dd>Specifies the primaries of the display. Video colors will be adapted to this colorspace when ICC color management is not being used. Valid values are:</p>
<dt><code>auto</code></p>
<dd>Disable any adaptation, except for atypical color spaces. Specifically, wide/unusual gamuts get automatically adapted to BT.709, while standard gamut (i.e. BT.601 and BT.709) content is not touched. (default)</p>
<dt><code>bt.470m</code></p>
<dd>ITU-R BT.470 M</p>
<dt><code>bt.601-525</code></p>
<dd>ITU-R BT.601 (525-line SD systems, eg. NTSC), SMPTE 170M/240M</p>
<dt><code>bt.601-625</code></p>
<dd>ITU-R BT.601 (625-line SD systems, eg. PAL/SECAM), ITU-R BT.470 B/G</p>
<dt><code>bt.709</code></p>
<dd>ITU-R BT.709 (HD), IEC 61966-2-4 (sRGB), SMPTE RP177 Annex B</p>
<dt><code>bt.2020</code></p>
<dd>ITU-R BT.2020 (UHD)</p>
<dt><code>apple</code></p>
<dd>Apple RGB</p>
<dt><code>adobe</code></p>
<dd>Adobe RGB (1998)</p>
<dt><code>prophoto</code></p>
<dd>ProPhoto RGB (ROMM)</p>
<dt><code>cie1931</code></p>
<dd>CIE 1931 RGB (not to be confused with CIE XYZ)</p>
<dt><code>dci-p3</code></p>
<dd>DCI-P3 (Digital Cinema Colorspace), SMPTE RP431-2</p>
<dt><code>v-gamut</code></p>
<dd>Panasonic V-Gamut (VARICAM) primaries</p>
<dt><code>s-gamut</code></p>
<dd>Sony S-Gamut (S-Log) primaries</p>
<dt><code>&#8211;target-trc=&lt;value&gt;</code></p>
<dd>Specifies the transfer characteristics (gamma) of the display. Video colors will be adjusted to this curve when ICC color management is not being used. Valid values are:</p>
<dt><code>auto</code></p>
<dd>Disable any adaptation, except for atypical transfers. Specifically, HDR or linear light source material gets automatically converted to gamma 2.2, while SDR content is not touched. (default)</p>
<dt><code>bt.1886</code></p>
<dd>ITU-R BT.1886 curve (assuming infinite contrast)</p>
<dt><code>srgb</code></p>
<dd>IEC 61966-2-4 (sRGB)</p>
<dt><code>linear</code></p>
<dd>Linear light output</p>
<dt><code>gamma1.8</code></p>
<dd>Pure power curve (gamma 1.8), also used for Apple RGB</p>
<dt><code>gamma2.0</code></p>
<dd>Pure power curve (gamma 2.0)</p>
<dt><code>gamma2.2</code></p>
<dd>Pure power curve (gamma 2.2)</p>
<dt><code>gamma2.4</code></p>
<dd>Pure power curve (gamma 2.4)</p>
<dt><code>gamma2.6</code></p>
<dd>Pure power curve (gamma 2.6)</p>
<dt><code>gamma2.8</code></p>
<dd>Pure power curve (gamma 2.8), also used for BT.470-BG</p>
<dt><code>prophoto</code></p>
<dd>ProPhoto RGB (ROMM)</p>
<dt><code>pq</code></p>
<dd>ITU-R BT.2100 PQ (Perceptual quantizer) curve, aka SMPTE ST2084</p>
<dt><code>hlg</code></p>
<dd>ITU-R BT.2100 HLG (Hybrid Log-gamma) curve, aka ARIB STD-B67</p>
<dt><code>v-log</code></p>
<dd>Panasonic V-Log (VARICAM) curve</p>
<dt><code>s-log1</code></p>
<dd>Sony S-Log1 curve</p>
<dt><code>s-log2</code></p>
<dd>Sony S-Log2 curve </p>
<p> <code>NOTE:</code> When using HDR output formats, mpv will encode to the specified curve but it will not set any HDMI flags or other signalling that might be required for the target device to correctly display the HDR signal. The user should independently guarantee this before using these signal formats for display.</p>
<dt><code>&#8211;target-peak=&lt;auto|nits&gt;</code></p>
<dd>Specifies the measured peak brightness of the output display, in cd/m^2 (AKA nits). The interpretation of this brightness depends on the configured <code>&#8211;target-trc</code>. In all cases, it imposes a limit on the signal values that will be sent to the display. If the source exceeds this brightness level, a tone mapping filter will be inserted. For HLG, it has the additional effect of parametrizing the inverse OOTF, in order to get colorimetrically consistent results with the mastering display. For SDR, or when using an ICC (profile (<code>&#8211;icc-profile</code>), setting this to a value above 203 essentially causes the display to be treated as if it were an HDR display in disguise. (See the note below) </p>
<p> In <code>auto</code> mode (the default), the chosen peak is an appropriate value based on the TRC in use. For SDR curves, it uses 203. For HDR curves, it uses 203 * the transfer function&#8217;s nominal peak. </p>
<p> <code>NOTE:</code> When using an SDR transfer function, this is normally not needed, and setting it may lead to very unexpected results. The one time it <i>is</i> useful is if you want to calibrate a HDR display using traditional transfer functions and calibration equipment. In such cases, you can set your HDR display to a high brightness such as 800 cd/m^2, and then calibrate it to a standard curve like gamma2.8. Setting this value to 800 would then instruct mpv to essentially treat it as an HDR display with the given peak. This may be a good alternative in environments where PQ or HLG input to the display is not possible, and makes it possible to use HDR displays with mpv regardless of operating system support for HDMI HDR metadata. </p>
<p> In such a configuration, we highly recommend setting <code>&#8211;tone-mapping</code> to <code>mobius</code> or even <code>clip</code>.</p>
<dt><code>&#8211;tone-mapping=&lt;value&gt;</code></p>
<dd>Specifies the algorithm used for tone-mapping images onto the target display. This is relevant for both HDR-&gt;SDR conversion as well as gamut reduction (e.g. playing back BT.2020 content on a standard gamut display). Valid values are:</p>
<dt><code>clip</code></p>
<dd>Hard-clip any out-of-range values. Use this when you care about perfect color accuracy for in-range values at the cost of completely distorting out-of-range values. Not generally recommended.</p>
<dt><code>mobius</code></p>
<dd>Generalization of Reinhard to a Möbius transform with linear section. Smoothly maps out-of-range values while retaining contrast and colors for in-range material as much as possible. Use this when you care about color accuracy more than detail preservation. This is somewhere in between <code>clip</code> and <code>reinhard</code>, depending on the value of <code>&#8211;tone-mapping-param</code>.</p>
<dt><code>reinhard</code></p>
<dd>Reinhard tone mapping algorithm. Very simple continuous curve. Preserves overall image brightness but uses nonlinear contrast, which results in flattening of details and degradation in color accuracy.</p>
<dt><code>hable</code></p>
<dd>Similar to <code>reinhard</code> but preserves both dark and bright details better (slightly sigmoidal), at the cost of slightly darkening / desaturating everything. Developed by John Hable for use in video games. Use this when you care about detail preservation more than color/brightness accuracy. This is roughly equivalent to <code>&#8211;tone-mapping=reinhard &#8211;tone-mapping-param=0.24</code>. If possible, you should also enable <code>&#8211;hdr-compute-peak</code> for the best results.</p>
<dt><code>bt.2390</code></p>
<dd>Perceptual tone mapping curve (EETF) specified in ITU-R Report BT.2390. This is the recommended curve to use for typical HDR-mastered content. (Default)</p>
<dt><code>gamma</code></p>
<dd>Fits a logarithmic transfer between the tone curves.</p>
<dt><code>linear</code></p>
<dd>Linearly stretches the entire reference gamut to (a linear multiple of) the display.</p>
<dt><code>&#8211;tone-mapping-param=&lt;value&gt;</code></p>
<dd>Set tone mapping parameters. By default, this is set to the special string <code>default</code>, which maps to an algorithm-specific default value. Ignored if the tone mapping algorithm is not tunable. This affects the following tone mapping algorithms:</p>
<dt><code>clip</code></p>
<dd>Specifies an extra linear coefficient to multiply into the signal before clipping. Defaults to 1.0.</p>
<dt><code>mobius</code></p>
<dd>Specifies the transition point from linear to mobius transform. Every value below this point is guaranteed to be mapped 1:1. The higher the value, the more accurate the result will be, at the cost of losing bright details. Defaults to 0.3, which due to the steep initial slope still preserves in-range colors fairly accurately.</p>
<dt><code>reinhard</code></p>
<dd>Specifies the local contrast coefficient at the display peak. Defaults to 0.5, which means that in-gamut values will be about half as bright as when clipping.</p>
<dt><code>gamma</code></p>
<dd>Specifies the exponent of the function. Defaults to 1.8.</p>
<dt><code>linear</code></p>
<dd>Specifies the scale factor to use while stretching. Defaults to 1.0.</p>
<dt><code>&#8211;tone-mapping-max-boost=&lt;1.0..10.0&gt;</code></p>
<dd>Upper limit for how much the tone mapping algorithm is allowed to boost the average brightness by over-exposing the image. The default value of 1.0 allows no additional brightness boost. A value of 2.0 would allow over-exposing by a factor of 2, and so on. Raising this setting can help reveal details that would otherwise be hidden in dark scenes, but raising it too high will make dark scenes appear unnaturally bright.</p>
<dt><code>&#8211;hdr-compute-peak=&lt;auto|yes|no&gt;</code></p>
<dd>Compute the HDR peak and frame average brightness per-frame instead of relying on tagged metadata. These values are averaged over local regions as well as over several frames to prevent the value from jittering around too much. This option basically gives you dynamic, per-scene tone mapping. Requires compute shaders, which is a fairly recent OpenGL feature, and will probably also perform horribly on some drivers, so enable at your own risk. The special value <code>auto</code> (default) will enable HDR peak computation automatically if compute shaders and SSBOs are supported.</p>
<dt><code>&#8211;hdr-peak-decay-rate=&lt;1.0..1000.0&gt;</code></p>
<dd>The decay rate used for the HDR peak detection algorithm (default: 100.0). This is only relevant when <code>&#8211;hdr-compute-peak</code> is enabled. Higher values make the peak decay more slowly, leading to more stable values at the cost of more &quot;eye adaptation&quot;-like effects (although this is mitigated somewhat by <code>&#8211;hdr-scene-threshold</code>). A value of 1.0 (the lowest possible) disables all averaging, meaning each frame&#8217;s value is used directly as measured, but doing this is not recommended for &quot;noisy&quot; sources since it may lead to excessive flicker. (In signal theory terms, this controls the time constant &quot;tau&quot; of an IIR low pass filter)</p>
<dt><code>&#8211;hdr-scene-threshold-low=&lt;0.0..100.0&gt;</code>, <code>&#8211;hdr-scene-threshold-high=&lt;0.0..100.0&gt;</code></p>
<dd>The lower and upper thresholds (in dB) for a brightness difference to be considered a scene change (default: 5.5 low, 10.0 high). This is only relevant when <code>&#8211;hdr-compute-peak</code> is enabled. Normally, small fluctuations in the frame brightness are compensated for by the peak averaging mechanism, but for large jumps in the brightness this can result in the frame remaining too bright or too dark for up to several seconds, depending on the value of <code>&#8211;hdr-peak-decay-rate</code>. To counteract this, when the brightness between the running average and the current frame exceeds the low threshold, mpv will make the averaging filter more aggressive, up to the limit of the high threshold (at which point the filter becomes instant).</p>
<dt><code>&#8211;tone-mapping-desaturate=&lt;0.0..1.0&gt;</code></p>
<dd>Apply desaturation for highlights (default: 0.75). The parameter controls the strength of the desaturation curve. A value of 0.0 completely disables it, while a value of 1.0 means that overly bright colors will tend towards white. (This is not always the case, especially not for highlights that are near primary colors) </p>
<p> Values in between apply progressively more/less aggressive desaturation. This setting helps prevent unnaturally oversaturated colors for super-highlights, by (smoothly) turning them into less saturated (per channel tone mapped) colors instead. This makes images feel more natural, at the cost of chromatic distortions for out-of-range colors. The default value of 0.75 provides a good balance. Setting this to 0.0 preserves the chromatic accuracy of the tone mapping process.</p>
<dt><code>&#8211;tone-mapping-desaturate-exponent=&lt;0.0..20.0&gt;</code></p>
<dd>This setting controls the exponent of the desaturation curve, which controls how bright a color needs to be in order to start being desaturated. The default of 1.5 provides a reasonable balance. Decreasing this exponent makes the curve more aggressive.</p>
<dt><code>&#8211;gamut-warning</code></p>
<dd>If enabled, mpv will mark all clipped/out-of-gamut pixels that exceed a given threshold (currently hard-coded to 101%). The affected pixels will be inverted to make them stand out. Note: This option applies after the effects of all of mpv&#8217;s color space transformation / tone mapping options, so it&#8217;s a good idea to combine this with <code>&#8211;tone-mapping=clip</code> and use <code>&#8211;target-prim</code> to set the gamut to simulate. For example, <code>&#8211;target-prim=bt.709</code> would make mpv highlight all pixels that exceed the gamut of a standard gamut (sRGB) display. This option also does not work well with ICC profiles, since the 3DLUTs are always generated against the source color space and have chromatically-accurate clipping built in.</p>
<dt><code>&#8211;gamut-clipping</code></p>
<dd>If enabled (default: yes), mpv will colorimetrically clip out-of-gamut colors by desaturating them (preserving luma), rather than hard-clipping each component individually. This should make playback of wide gamut content on typical (standard gamut) monitors look much more aesthetically pleasing and less blown-out.</p>
<dt><code>&#8211;use-embedded-icc-profile</code></p>
<dd>Load the embedded ICC profile contained in media files such as PNG images. (Default: yes). Note that this option only works when also using a display ICC profile (<code>&#8211;icc-profile</code> or <code>&#8211;icc-profile-auto</code>), and also requires LittleCMS 2 support.</p>
<dt><code>&#8211;icc-profile=&lt;file&gt;</code></p>
<dd>Load an ICC profile and use it to transform video RGB to screen output. Needs LittleCMS 2 support compiled in. This option overrides the <code>&#8211;target-prim</code>, <code>&#8211;target-trc</code> and <code>&#8211;icc-profile-auto</code> options.</p>
<dt><code>&#8211;icc-profile-auto</code></p>
<dd>Automatically select the ICC display profile currently specified by the display settings of the operating system. </p>
<p> NOTE: On Windows, the default profile must be an ICC profile. WCS profiles are not supported. </p>
<p> Applications using libmpv with the render API need to provide the ICC profile via <code>MPV_RENDER_PARAM_ICC_PROFILE</code>.</p>
<dt><code>&#8211;icc-cache-dir=&lt;dirname&gt;</code></p>
<dd>Store and load the 3D LUTs created from the ICC profile in this directory. This can be used to speed up loading, since LittleCMS 2 can take a while to create a 3D LUT. Note that these files contain uncompressed LUTs. Their size depends on the <code>&#8211;icc-3dlut-size</code>, and can be very big. </p>
<p> NOTE: This is not cleaned automatically, so old, unused cache files may stick around indefinitely.</p>
<dt><code>&#8211;icc-intent=&lt;value&gt;</code></p>
<dd>Specifies the ICC intent used for the color transformation (when using <code>&#8211;icc-profile</code>).</p>
<dt><code>0</code></p>
<dd>perceptual</p>
<dt><code>1</code></p>
<dd>relative colorimetric (default)</p>
<dt><code>2</code></p>
<dd>saturation</p>
<dt><code>3</code></p>
<dd>absolute colorimetric</p>
<dt><code>&#8211;icc-3dlut-size=&lt;r&gt;x&lt;g&gt;x&lt;b&gt;</code></p>
<dd>Size of the 3D LUT generated from the ICC profile in each dimension. Default is 64x64x64. Sizes may range from 2 to 512.</p>
<dt><code>&#8211;icc-force-contrast=&lt;no|0-1000000|inf&gt;</code></p>
<dd>Override the target device&#8217;s detected contrast ratio by a specific value. This is detected automatically from the profile if possible, but for some profiles it might be missing, causing the contrast to be assumed as infinite. As a result, video may appear darker than intended. If this is the case, setting this option might help. This only affects BT.1886 content. The default of <code>no</code> means to use the profile values. The special value <code>inf</code> causes the BT.1886 curve to be treated as a pure power gamma 2.4 function.</p>
<dt><code>&#8211;blend-subtitles=&lt;yes|video|no&gt;</code></p>
<dd>Blend subtitles directly onto upscaled video frames, before interpolation and/or color management (default: no). Enabling this causes subtitles to be affected by <code>&#8211;icc-profile</code>, <code>&#8211;target-prim</code>, <code>&#8211;target-trc</code>, <code>&#8211;interpolation</code>, <code>&#8211;gamma-factor</code> and <code>&#8211;glsl-shaders</code>. It also increases subtitle performance when using <code>&#8211;interpolation</code>. </p>
<p> The downside of enabling this is that it restricts subtitles to the visible portion of the video, so you can&#8217;t have subtitles exist in the black margins below a video (for example). </p>
<p> If <code>video</code> is selected, the behavior is similar to <code>yes</code>, but subs are drawn at the video&#8217;s native resolution, and scaled along with the video. </p>
<p> <code>WARNING:</code> This changes the way subtitle colors are handled. Normally, subtitle colors are assumed to be in sRGB and color managed as such. Enabling this makes them treated as being in the video&#8217;s color space instead. This is good if you want things like softsubbed ASS signs to match the video colors, but may cause SRT subtitles or similar to look slightly off.</p>
<dt><code>&#8211;alpha=&lt;blend-tiles|blend|yes|no&gt;</code></p>
<dd>Decides what to do if the input has an alpha component.</p>
<dt><code>blend-tiles</code></p>
<dd>Blend the frame against a 16&#215;16 gray/white tiles background (default).</p>
<dt><code>blend</code></p>
<dd>Blend the frame against the background color (<code>&#8211;background</code>, normally black).</p>
<dt><code>yes</code></p>
<dd>Try to create a framebuffer with alpha component. This only makes sense if the video contains alpha information (which is extremely rare) or if you make the background color transparent. May not be supported on all platforms. If alpha framebuffers are unavailable, it silently falls back on a normal framebuffer. Note that if you set the <code>&#8211;fbo-format</code> option to a non-default value, a format with alpha must be specified, or this won&#8217;t work. Whether this really works depends on the windowing system and desktop environment.</p>
<dt><code>no</code></p>
<dd>Ignore alpha component.</p>
<dt><code>&#8211;opengl-rectangle-textures</code></p>
<dd>Force use of rectangle textures (default: no). Normally this shouldn&#8217;t have any advantages over normal textures. Note that hardware decoding overrides this flag. Could be removed any time.</p>
<dt><code>&#8211;background=&lt;color&gt;</code></p>
<dd>Color used to draw parts of the mpv window not covered by video. See the <code>&#8211;sub-color</code> option for how colors are defined.</p>
<dt><code>&#8211;gpu-tex-pad-x</code>, <code>&#8211;gpu-tex-pad-y</code></p>
<dd>Enlarge the video source textures by this many pixels. For debugging only (normally textures are sized exactly, but due to hardware decoding interop we may have to deal with additional padding, which can be tested with these options). Could be removed any time.</p>
<dt><code>&#8211;opengl-early-flush=&lt;yes|no|auto&gt;</code></p>
<dd>Call <code>glFlush()</code> after rendering a frame and before attempting to display it (default: auto). Can fix stuttering in some cases, in other cases probably causes it. The <code>auto</code> mode will call <code>glFlush()</code> only if the renderer is going to wait for a while after rendering, instead of flipping GL front and backbuffers immediately (i.e. it doesn&#8217;t call it in display-sync mode). </p>
<p> On macOS this is always deactivated because it only causes performance problems and other regressions.</p>
<dt><code>&#8211;gpu-dumb-mode=&lt;yes|no|auto&gt;</code></p>
<dd>This mode is extremely restricted, and will disable most extended features. That includes high quality scalers and custom shaders! </p>
<p> It is intended for hardware that does not support FBOs (including GLES, which supports it insufficiently), or to get some more performance out of bad or old hardware. </p>
<p> This mode is forced automatically if needed, and this option is mostly useful for debugging. The default of <code>auto</code> will enable it automatically if nothing uses features which require FBOs. </p>
<p> This option might be silently removed in the future.</p>
<dt><code>&#8211;gpu-shader-cache-dir=&lt;dirname&gt;</code></p>
<dd>Store and load compiled GLSL shaders in this directory. Normally, shader compilation is very fast, so this is usually not needed. It mostly matters for GPU APIs that require internally recompiling shaders to other languages, for example anything based on ANGLE or Vulkan. Enabling this can improve startup performance on these platforms. </p>
<p> NOTE: This is not cleaned automatically, so old, unused cache files may stick around indefinitely.</dl>
<h3>Miscellaneous</h3>
<dl COMPACT>
<dt><code>&#8211;display-tags=tag1,tags2,&#8230;</code></p>
<dd>Set the list of tags that should be displayed on the terminal. Tags that are in the list, but are not present in the played file, will not be shown. If a value ends with <code>*</code>, all tags are matched by prefix (though there is no general globbing). Just passing <code>*</code> essentially filtering. </p>
<p> The default includes a common list of tags, call mpv with <code>&#8211;list-options</code> to see it. </p>
<p> This is a string list option. See <i>List Options</i> for details.</p>
<dt><code>&#8211;mc=&lt;seconds/frame&gt;</code></p>
<dd>Maximum A-V sync correction per frame (in seconds)</p>
<dt><code>&#8211;autosync=&lt;factor&gt;</code></p>
<dd>Gradually adjusts the A/V sync based on audio delay measurements. Specifying <code>&#8211;autosync=0</code>, the default, will cause frame timing to be based entirely on audio delay measurements. Specifying <code>&#8211;autosync=1</code> will do the same, but will subtly change the A/V correction algorithm. An uneven video framerate in a video which plays fine with <code>&#8211;no-audio</code> can often be helped by setting this to an integer value greater than 1. The higher the value, the closer the timing will be to <code>&#8211;no-audio</code>. Try <code>&#8211;autosync=30</code> to smooth out problems with sound drivers which do not implement a perfect audio delay measurement. With this value, if large A/V sync offsets occur, they will only take about 1 or 2 seconds to settle out. This delay in reaction time to sudden A/V offsets should be the only side effect of turning this option on, for all sound drivers.</p>
<dt><code>&#8211;video-timing-offset=&lt;seconds&gt;</code></p>
<dd>Control how long before video display target time the frame should be rendered (default: 0.050). If a video frame should be displayed at a certain time, the VO will start rendering the frame earlier, and then will perform a blocking wait until the display time, and only then &quot;swap&quot; the frame to display. The rendering cannot start before the previous frame is displayed, so this value is implicitly limited by the video framerate. With normal video frame rates, the default value will ensure that rendering is always immediately started after the previous frame was displayed. On the other hand, setting a too high value can reduce responsiveness with low FPS value. </p>
<p> For client API users using the render API (or the deprecated <code>opengl-cb</code> API), this option is interesting, because you can stop the render API from limiting your FPS (see <code>mpv_render_context_render()</code> documentation). </p>
<p> This applies only to audio timing modes (e.g. <code>&#8211;video-sync=audio</code>). In other modes (<code>&#8211;video-sync=display-&#8230;</code>), video timing relies on vsync blocking, and this option is not used.</p>
<dt><code>&#8211;video-sync=&lt;audio|&#8230;&gt;</code></p>
<dd>How the player synchronizes audio and video. </p>
<p> If you use this option, you usually want to set it to <code>display-resample</code> to enable a timing mode that tries to not skip or repeat frames when for example playing 24fps video on a 24Hz screen. </p>
<p> The modes starting with <code>display-</code> try to output video frames completely synchronously to the display, using the detected display vertical refresh rate as a hint how fast frames will be displayed on average. These modes change video speed slightly to match the display. See <code>&#8211;video-sync-&#8230;</code> options for fine tuning. The robustness of this mode is further reduced by making a some idealized assumptions, which may not always apply in reality. Behavior can depend on the VO and the system&#8217;s video and audio drivers. Media files must use constant framerate. Section-wise VFR might work as well with some container formats (but not e.g. mkv). </p>
<p> Under some circumstances, the player automatically reverts to <code>audio</code> mode for some time or permanently. This can happen on very low framerate video, or if the framerate cannot be detected. </p>
<p> Also in display-sync modes it can happen that interruptions to video playback (such as toggling fullscreen mode, or simply resizing the window) will skip the video frames that should have been displayed, while <code>audio</code> mode will display them after the renderer has resumed (typically resulting in a short A/V desync and the video &quot;catching up&quot;). </p>
<p> Before mpv 0.30.0, there was a fallback to <code>audio</code> mode on severe A/V desync. This was changed for the sake of not sporadically stopping. Now, <code>display-desync</code> does what it promises and may desync with audio by an arbitrary amount, until it is manually fixed with a seek. </p>
<p> These modes also require a vsync blocked presentation mode. For OpenGL, this translates to <code>&#8211;opengl-swapinterval=1</code>. For Vulkan, it translates to <code>&#8211;vulkan-swap-mode=fifo</code> (or <code>fifo-relaxed</code>). </p>
<p> The modes with <code>desync</code> in their names do not attempt to keep audio/video in sync. They will slowly (or quickly) desync, until e.g. the next seek happens. These modes are meant for testing, not serious use.</p>
<dt><code>audio</code></p>
<dd>Time video frames to audio. This is the most robust mode, because the player doesn&#8217;t have to assume anything about how the display behaves. The disadvantage is that it can lead to occasional frame drops or repeats. If audio is disabled, this uses the system clock. This is the default mode.</p>
<dt><code>display-resample</code></p>
<dd>Resample audio to match the video. This mode will also try to adjust audio speed to compensate for other drift. (This means it will play the audio at a different speed every once in a while to reduce the A/V difference.)</p>
<dt><code>display-resample-vdrop</code></p>
<dd>Resample audio to match the video. Drop video frames to compensate for drift.</p>
<dt><code>display-resample-desync</code></p>
<dd>Like the previous mode, but no A/V compensation.</p>
<dt><code>display-vdrop</code></p>
<dd>Drop or repeat video frames to compensate desyncing video. (Although it should have the same effects as <code>audio</code>, the implementation is very different.)</p>
<dt><code>display-adrop</code></p>
<dd>Drop or repeat audio data to compensate desyncing video. This mode will cause severe audio artifacts if the real monitor refresh rate is too different from the reported or forced rate. Since mpv 0.33.0, this acts on entire audio frames, instead of single samples.</p>
<dt><code>display-desync</code></p>
<dd>Sync video to display, and let audio play on its own.</p>
<dt><code>desync</code></p>
<dd>Sync video according to system clock, and let audio play on its own.</p>
<dt><code>&#8211;video-sync-max-factor=&lt;value&gt;</code></p>
<dd>Maximum multiple for which to try to fit the video&#8217;s FPS to the display&#8217;s FPS (default: 5). </p>
<p> For example, if this is set to 1, the video FPS is forced to an integer multiple of the display FPS, as long as the speed change does not exceed the value set by <code>&#8211;video-sync-max-video-change</code>. </p>
<p> See <code>&#8211;interpolation-threshold</code> for how this option affects interpolation. </p>
<p> This is mostly for testing, and the option may be randomly changed in the future without notice.</p>
<dt><code>&#8211;video-sync-max-video-change=&lt;value&gt;</code></p>
<dd>Maximum speed difference in percent that is applied to video with <code>&#8211;video-sync=display-&#8230;</code> (default: 1). Display sync mode will be disabled if the monitor and video refresh way do not match within the given range. It tries multiples as well: playing 30 fps video on a 60 Hz screen will duplicate every second frame. Playing 24 fps video on a 60 Hz screen will play video in a 2-3-2-3-&#8230; pattern. </p>
<p> The default settings are not loose enough to speed up 23.976 fps video to 25 fps. We consider the pitch change too extreme to allow this behavior by default. Set this option to a value of <code>5</code> to enable it. </p>
<p> Note that in the <code>&#8211;video-sync=display-resample</code> mode, audio speed will additionally be changed by a small amount if necessary for A/V sync. See <code>&#8211;video-sync-max-audio-change</code>.</p>
<dt><code>&#8211;video-sync-max-audio-change=&lt;value&gt;</code></p>
<dd>Maximum <i>additional</i> speed difference in percent that is applied to audio with <code>&#8211;video-sync=display-&#8230;</code> (default: 0.125). Normally, the player plays the audio at the speed of the video. But if the difference between audio and video position is too high, e.g. due to drift or other timing errors, it will attempt to speed up or slow down audio by this additional factor. Too low values could lead to video frame dropping or repeating if the A/V desync cannot be compensated, too high values could lead to chaotic frame dropping due to the audio &quot;overshooting&quot; and skipping multiple video frames before the sync logic can react.</p>
<dt><code>&#8211;mf-fps=&lt;value&gt;</code></p>
<dd>Framerate used when decoding from multiple PNG or JPEG files with <code>mf://</code> (default: 1).</p>
<dt><code>&#8211;mf-type=&lt;value&gt;</code></p>
<dd>Input file type for <code>mf://</code> (available: jpeg, png, tga, sgi). By default, this is guessed from the file extension.</p>
<dt><code>&#8211;stream-dump=&lt;destination-filename&gt;</code></p>
<dd>Instead of playing a file, read its byte stream and write it to the given destination file. The destination is overwritten. Can be useful to test network-related behavior.</p>
<dt><code>&#8211;stream-lavf-o=opt1=value1,opt2=value2,&#8230;</code></p>
<dd>Set AVOptions on streams opened with libavformat. Unknown or misspelled options are silently ignored. (They are mentioned in the terminal output in verbose mode, i.e. <code>&#8211;v</code>. In general we can&#8217;t print errors, because other options such as e.g. user agent are not available with all protocols, and printing errors for unknown options would end up being too noisy.) </p>
<p> This is a key/value list option. See <i>List Options</i> for details.</p>
<dt><code>&#8211;vo-mmcss-profile=&lt;name&gt;</code></p>
<dd>(Windows only.) Set the MMCSS profile for the video renderer thread (default: <code>Playback</code>).</p>
<dt><code>&#8211;priority=&lt;prio&gt;</code></p>
<dd>(Windows only.) Set process priority for mpv according to the predefined priorities available under Windows. </p>
<p> Possible values of <code>&lt;prio&gt;</code>: idle|belownormal|normal|abovenormal|high|realtime </p>
<p> <code>WARNING:</code> Using realtime priority can cause system lockup.</p>
<dt><code>&#8211;force-media-title=&lt;string&gt;</code></p>
<dd>Force the contents of the <code>media-title</code> property to this value. Useful for scripts which want to set a title, without overriding the user&#8217;s setting in <code>&#8211;title</code>.</p>
<dt><code>&#8211;external-files=&lt;file-list&gt;</code></p>
<dd>Load a file and add all of its tracks. This is useful to play different files together (for example audio from one file, video from another), or for advanced <code>&#8211;lavfi-complex</code> used (like playing two video files at the same time). </p>
<p> Unlike <code>&#8211;sub-files</code> and <code>&#8211;audio-files</code>, this includes all tracks, and does not cause default stream selection over the &quot;proper&quot; file. This makes it slightly less intrusive. (In mpv 0.28.0 and before, this was not quite strictly enforced.) </p>
<p> This is a path list option. See <i>List Options</i> for details.</p>
<dt><code>&#8211;external-file=&lt;file&gt;</code></p>
<dd>CLI/config file only alias for <code>&#8211;external-files-append</code>. Each use of this option will add a new external file.</p>
<dt><code>&#8211;cover-art-files=&lt;file-list&gt;</code></p>
<dd>Use an external file as cover art while playing audio. This makes it appear on the track list and subject to automatic track selection. Options like <code>&#8211;audio-display</code> control whether such tracks are supposed to be selected. </p>
<p> (The difference to loading a file with <code>&#8211;external-files</code> is that video tracks will be marked as being pictures, which affects the auto-selection method. If the passed file is a video, only the first frame will be decoded and displayed. Enabling the cover art track during playback may show a random frame if the source file is a video. Normally you&#8217;re not supposed to pass videos to this option, so this paragraph describes the behavior coincidentally resulting from implementation details.) </p>
<p> This is a path list option. See <i>List Options</i> for details.</p>
<dt><code>&#8211;cover-art-file=&lt;file&gt;</code></p>
<dd>CLI/config file only alias for <code>&#8211;cover-art-files-append</code>. Each use of this option will add a new external file.</p>
<dt><code>&#8211;cover-art-auto=&lt;no|exact|fuzzy|all&gt;</code></p>
<dd>Whether to load _external_ cover art automatically. Similar to <code>&#8211;sub-auto</code> and <code>&#8211;audio-file-auto</code>. If a video already has tracks (which are not marked as cover art), external cover art will not be loaded.</p>
<dt><code>no</code></p>
<dd>Don&#8217;t automatically load cover art.</p>
<dt><code>exact</code></p>
<dd>Load the media filename with an image file extension.</p>
<dt><code>fuzzy</code></p>
<dd>Load all cover art containing the media filename and filenames in an internal whitelist, such as <code>cover.jpg</code> (default).</p>
<dt><code>all</code></p>
<dd>Load all images in the current directory. </p>
<p> See <code>&#8211;cover-art-files</code> for details about what constitutes cover art. </p>
<p> See <code>&#8211;audio-display</code> how to control display of cover art (this can be used to disable cover art that is part of the file).</p>
<dt><code>&#8211;autoload-files=&lt;yes|no&gt;</code></p>
<dd>Automatically load/select external files (default: yes). </p>
<p> If set to <code>no</code>, then do not automatically load external files as specified by <code>&#8211;sub-auto</code>, <code>&#8211;audio-file-auto</code> and <code>&#8211;cover-art-auto</code>. If external files are forcibly added (like with <code>&#8211;sub-files</code>), they will not be auto-selected. </p>
<p> This does not affect playlist expansion, redirection, or other loading of referenced files like with ordered chapters.</p>
<dt><code>&#8211;record-file=&lt;file&gt;</code></p>
<dd>Deprecated, use <code>&#8211;stream-record</code>, or the <code>dump-cache</code> command. </p>
<p> Record the current stream to the given target file. The target file will always be overwritten without asking. </p>
<p> This was deprecated because it isn&#8217;t very nice to use. For one, seeking while this is enabled will be directly reflected in the output, which was not useful and annoying.</p>
<dt><code>&#8211;stream-record=&lt;file&gt;</code></p>
<dd>Write received/read data from the demuxer to the given output file. The output file will always be overwritten without asking. The output format is determined by the extension of the output file. </p>
<p> Switching streams or seeking during recording might result in recording being stopped and/or broken files. Use with care. </p>
<p> Seeking outside of the demuxer cache will result in &quot;skips&quot; in the output file, but seeking within the demuxer cache should not affect recording. One exception is when you seek back far enough to exceed the forward buffering size, in which case the cache stops actively reading. This will return in dropped data if it&#8217;s a live stream. </p>
<p> If this is set at runtime, the old file is closed, and the new file is opened. Note that this will write only data that is appended at the end of the cache, and the already cached data cannot be written. You can try the <code>dump-cache</code> command as an alternative. </p>
<p> External files (<code>&#8211;audio-file</code> etc.) are ignored by this, it works on the &quot;main&quot; file only. Using this with files using ordered chapters or EDL files will also not work correctly in general. </p>
<p> There are some glitches with this because it uses FFmpeg&#8217;s libavformat for writing the output file. For example, it&#8217;s typical that it will only work if the output format is the same as the input format. This is the case even if it works with the <code>ffmpeg</code> tool. One reason for this is that <code>ffmpeg</code> and its libraries contain certain hacks and workarounds for these issues, that are unavailable to outside users. </p>
<p> This replaces <code>&#8211;record-file</code>. It is similar to the ancient/removed <code>&#8211;stream-capture</code>/<code>-capture</code> options, and provides better behavior in most cases (i.e. actually works).</p>
<dt><code>&#8211;lavfi-complex=&lt;string&gt;</code></p>
<dd>Set a &quot;complex&quot; libavfilter filter, which means a single filter graph can take input from multiple source audio and video tracks. The graph can result in a single audio or video output (or both). </p>
<p> Currently, the filter graph labels are used to select the participating input tracks and audio/video output. The following rules apply:</p>
<dt>&bull;</p>
<dd>A label of the form <code>aidN</code> selects audio track N as input (e.g. <code>aid1</code>).</p>
<dt>&bull;</p>
<dd>A label of the form <code>vidN</code> selects video track N as input.</p>
<dt>&bull;</p>
<dd>A label named <code>ao</code> will be connected to the audio output.</p>
<dt>&bull;</p>
<dd>A label named <code>vo</code> will be connected to the video output. </p>
<p> Each label can be used only once. If you want to use e.g. an audio stream for multiple filters, you need to use the <code>asplit</code> filter. Multiple video or audio outputs are not possible, but you can use filters to merge them into one. </p>
<p> It&#8217;s not possible to change the tracks connected to the filter at runtime, unless you explicitly change the <code>lavfi-complex</code> property and set new track assignments. When the graph is changed, the track selection is changed according to the used labels as well. </p>
<p> Other tracks, as long as they&#8217;re not connected to the filter, and the corresponding output is not connected to the filter, can still be freely changed with the normal methods. </p>
<p> Note that the normal filter chains (<code>&#8211;af</code>, <code>&#8211;vf</code>) are applied between the complex graphs (e.g. <code>ao</code> label) and the actual output.</p>
<dt>Examples</p>
<dd>
<dt>&bull;</p>
<dd><code>&#8211;lavfi-complex='[aid1] [aid2] amix [ao]&#8217;</code> Play audio track 1 and 2 at the same time.</p>
<dt>&bull;</p>
<dd><code>&#8211;lavfi-complex='[vid1] [vid2] vstack [vo]&#8217;</code> Stack video track 1 and 2 and play them at the same time. Note that both tracks need to have the same width, or filter initialization will fail (you can add <code>scale</code> filters before the <code>vstack</code> filter to fix the size). To load a video track from another file, you can use <code>&#8211;external-file=other.mkv</code>.</p>
<dt>&bull;</p>
<dd><code>&#8211;lavfi-complex='[aid1] asplit [t1] [ao] ; [t1] showvolume [t2] ; [vid1] [t2] overlay [vo]&#8217;</code> Play audio track 1, and overlay the measured volume for each speaker over video track 1.</p>
<dt>&bull;</p>
<dd><code>null:// &#8211;lavfi-complex=&#8217;life [vo]&#8217;</code> A libavfilter source-only filter (Conways&#8217; Life Game). </p>
<p> See the FFmpeg libavfilter documentation for details on the available filters.</p>
<dt><code>&#8211;metadata-codepage=&lt;codepage&gt;</code></p>
<dd>Codepage for various input metadata (default: <code>utf-8</code>). This affects how file tags, chapter titles, etc. are interpreted. You can for example set this to <code>auto</code> to enable autodetection of the codepage. (This is not the default because non-UTF-8 codepages are an obscure fringe use-case.) </p>
<p> See <code>&#8211;sub-codepage</code> option on how codepages are specified and further details regarding autodetection and codepage conversion. (The underlying code is the same.) </p>
<p> Conversion is not applied to metadata that is updated at runtime.</dl>
<h3>Debugging</h3>
<dl COMPACT>
<dt><code>&#8211;unittest=&lt;name&gt;</code></p>
<dd>Run an internal unit test. There are multiple, and the name specifies which. </p>
<p> The special value <code>all-simple</code> runs all tests which do not need further setup (other arguments and such). Some tests may need additional arguments to do anything useful. </p>
<p> On success, the player binary exits with exit status 0, otherwise it returns with an undefined non-0 exit status (it may crash or abort itself on test failures). </p>
<p> This is only enabled if built with <code>&#8211;enable-tests</code>, and should normally be enabled and used by developers only.</dl>
<h2>Audio Output Drivers</h2>
<p>Audio output drivers are interfaces to different audio output facilities. The syntax is:</p>
<dl COMPACT>
<dt><code>&#8211;ao=&lt;driver1,driver2,&#8230;[,]&gt;</code></p>
<dd>Specify a priority list of audio output drivers to be used. </p>
<p> If the list has a trailing &#8216;,&#8217;, mpv will fall back on drivers not contained in the list. </p>
<p> <code>NOTE:</code> See <code>&#8211;ao=help</code> for a list of compiled-in audio output drivers. The driver <code>&#8211;ao=alsa</code> is preferred. <code>&#8211;ao=pulse</code> is preferred on systems where PulseAudio is used. On BSD systems, <code>&#8211;ao=oss</code> is preferred. </p>
<p> Available audio output drivers are:</p>
<dt><code>alsa</code> (Linux only)</p>
<dd>ALSA audio output driver </p>
<p> See <i>ALSA audio output options</i> for options specific to this AO. </p>
<p> <code>WARNING:</code> To get multichannel/surround audio, use <code>&#8211;audio-channels=auto</code>. The default for this option is <code>auto-safe</code>, which makes this audio output explicitly reject multichannel output, as there is no way to detect whether a certain channel layout is actually supported. </p>
<p> You can also try <i>using the upmix plugin</i>. This setup enables multichannel audio on the <code>default</code> device with automatic upmixing with shared access, so playing stereo and multichannel audio at the same time will work as expected.</p>
<dt><code>oss</code></p>
<dd>OSS audio output driver</p>
<dt><code>jack</code></p>
<dd>JACK (Jack Audio Connection Kit) audio output driver. </p>
<p> The following global options are supported by this audio output:</p>
<dt><code>&#8211;jack-port=&lt;name&gt;</code></p>
<dd>Connects to the ports with the given name (default: physical ports).</p>
<dt><code>&#8211;jack-name=&lt;client&gt;</code></p>
<dd>Client name that is passed to JACK (default: <code>mpv</code>). Useful if you want to have certain connections established automatically.</p>
<dt><code>&#8211;jack-autostart=&lt;yes|no&gt;</code></p>
<dd>Automatically start jackd if necessary (default: disabled). Note that this tends to be unreliable and will flood stdout with server messages.</p>
<dt><code>&#8211;jack-connect=&lt;yes|no&gt;</code></p>
<dd>Automatically create connections to output ports (default: enabled). When enabled, the maximum number of output channels will be limited to the number of available output ports.</p>
<dt><code>&#8211;jack-std-channel-layout=&lt;waveext|any&gt;</code></p>
<dd>Select the standard channel layout (default: waveext). JACK itself has no notion of channel layouts (i.e. assigning which speaker a given channel is supposed to map to) &#8211; it just takes whatever the application outputs, and reroutes it to whatever the user defines. This means the user and the application are in charge of dealing with the channel layout. <code>waveext</code> uses WAVE_FORMAT_EXTENSIBLE order, which, even though it was defined by Microsoft, is the standard on many systems. The value <code>any</code> makes JACK accept whatever comes from the audio filter chain, regardless of channel layout and without reordering. This mode is probably not very useful, other than for debugging or when used with fixed setups.</p>
<dt><code>coreaudio</code> (macOS only)</p>
<dd>Native macOS audio output driver using AudioUnits and the CoreAudio sound server. </p>
<p> Automatically redirects to <code>coreaudio_exclusive</code> when playing compressed formats. </p>
<p> The following global options are supported by this audio output:</p>
<dt><code>&#8211;coreaudio-change-physical-format=&lt;yes|no&gt;</code></p>
<dd>Change the physical format to one similar to the requested audio format (default: no). This has the advantage that multichannel audio output will actually work. The disadvantage is that it will change the system-wide audio settings. This is equivalent to changing the <code>Format</code> setting in the <code>Audio Devices</code> dialog in the <code>Audio MIDI Setup</code> utility. Note that this does not affect the selected speaker setup.</p>
<dt><code>&#8211;coreaudio-spdif-hack=&lt;yes|no&gt;</code></p>
<dd>Try to pass through AC3/DTS data as PCM. This is useful for drivers which do not report AC3 support. It converts the AC3 data to float, and assumes the driver will do the inverse conversion, which means a typical A/V receiver will pick it up as compressed IEC framed AC3 stream, ignoring that it&#8217;s marked as PCM. This disables normal AC3 passthrough (even if the device reports it as supported). Use with extreme care.</p>
<dt><code>coreaudio_exclusive</code> (macOS only)</p>
<dd>Native macOS audio output driver using direct device access and exclusive mode (bypasses the sound server).</p>
<dt><code>openal</code></p>
<dd>OpenAL audio output driver. This is broken and does not work.</p>
<dt><code>&#8211;openal-num-buffers=&lt;2-128&gt;</code></p>
<dd>Specify the number of audio buffers to use. Lower values are better for lower CPU usage. Default: 4.</p>
<dt><code>&#8211;openal-num-samples=&lt;256-32768&gt;</code></p>
<dd>Specify the number of complete samples to use for each buffer. Higher values are better for lower CPU usage. Default: 8192.</p>
<dt><code>&#8211;openal-direct-channels=&lt;yes|no&gt;</code></p>
<dd>Enable OpenAL Soft&#8217;s direct channel extension when available to avoid tinting the sound with ambisonics or HRTF. Channels are dropped when when they are not available as downmixing will be disabled. Default: no.</p>
<dt><code>pulse</code></p>
<dd>PulseAudio audio output driver </p>
<p> The following global options are supported by this audio output:</p>
<dt><code>&#8211;pulse-host=&lt;host&gt;</code></p>
<dd>Specify the host to use. An empty &lt;host&gt; string uses a local connection, &quot;localhost&quot; uses network transfer (most likely not what you want).</p>
<dt><code>&#8211;pulse-buffer=&lt;1-2000|native&gt;</code></p>
<dd>Set the audio buffer size in milliseconds. A higher value buffers more data, and has a lower probability of buffer underruns. A smaller value makes the audio stream react faster, e.g. to playback speed changes.</p>
<dt><code>&#8211;pulse-latency-hacks=&lt;yes|no&gt;</code></p>
<dd>Enable hacks to workaround PulseAudio timing bugs (default: no). If enabled, mpv will do elaborate latency calculations on its own. If disabled, it will use PulseAudio automatically updated timing information. Disabling this might help with e.g. networked audio or some plugins, while enabling it might help in some unknown situations (it used to be required to get good behavior on old PulseAudio versions). </p>
<p> If you have stuttering video when using pulse, try to enable this option. (Or try to update PulseAudio.)</p>
<dt><code>&#8211;pulse-allow-suspended=&lt;yes|no&gt;</code></p>
<dd>Allow mpv to use PulseAudio even if the sink is suspended (default: no). Can be useful if PulseAudio is running as a bridge to jack and mpv has its sink-input set to the one jack is using.</p>
<dt><code>sdl</code></p>
<dd>SDL 1.2+ audio output driver. Should work on any platform supported by SDL 1.2, but may require the <code>SDL_AUDIODRIVER</code> environment variable to be set appropriately for your system. </p>
<p> <code>NOTE:</code> This driver is for compatibility with extremely foreign environments, such as systems where none of the other drivers are available. </p>
<p> The following global options are supported by this audio output:</p>
<dt><code>&#8211;sdl-buflen=&lt;length&gt;</code></p>
<dd>Sets the audio buffer length in seconds. Is used only as a hint by the sound system. Playing a file with <code>-v</code> will show the requested and obtained exact buffer size. A value of 0 selects the sound system default.</p>
<dt><code>null</code></p>
<dd>Produces no audio output but maintains video playback speed. You can use <code>&#8211;ao=null &#8211;ao-null-untimed</code> for benchmarking. </p>
<p> The following global options are supported by this audio output:</p>
<dt><code>&#8211;ao-null-untimed</code></p>
<dd>Do not simulate timing of a perfect audio device. This means audio decoding will go as fast as possible, instead of timing it to the system clock.</p>
<dt><code>&#8211;ao-null-buffer</code></p>
<dd>Simulated buffer length in seconds.</p>
<dt><code>&#8211;ao-null-outburst</code></p>
<dd>Simulated chunk size in samples.</p>
<dt><code>&#8211;ao-null-speed</code></p>
<dd>Simulated audio playback speed as a multiplier. Usually, a real audio device will not go exactly as fast as the system clock. It will deviate just a little, and this option helps to simulate this.</p>
<dt><code>&#8211;ao-null-latency</code></p>
<dd>Simulated device latency. This is additional to EOF.</p>
<dt><code>&#8211;ao-null-broken-eof</code></p>
<dd>Simulate broken audio drivers, which always add the fixed device latency to the reported audio playback position.</p>
<dt><code>&#8211;ao-null-broken-delay</code></p>
<dd>Simulate broken audio drivers, which don&#8217;t report latency correctly.</p>
<dt><code>&#8211;ao-null-channel-layouts</code></p>
<dd>If not empty, this is a <code>,</code> separated list of channel layouts the AO allows. This can be used to test channel layout selection.</p>
<dt><code>&#8211;ao-null-format</code></p>
<dd>Force the audio output format the AO will accept. If unset accepts any.</p>
<dt><code>pcm</code></p>
<dd>Raw PCM/WAVE file writer audio output </p>
<p> The following global options are supported by this audio output:</p>
<dt><code>&#8211;ao-pcm-waveheader=&lt;yes|no&gt;</code></p>
<dd>Include or do not include the WAVE header (default: included). When not included, raw PCM will be generated.</p>
<dt><code>&#8211;ao-pcm-file=&lt;filename&gt;</code></p>
<dd>Write the sound to <code>&lt;filename&gt;</code> instead of the default <code>audiodump.wav</code>. If <code>no-waveheader</code> is specified, the default is <code>audiodump.pcm</code>.</p>
<dt><code>&#8211;ao-pcm-append=&lt;yes|no&gt;</code></p>
<dd>Append to the file, instead of overwriting it. Always use this with the <code>no-waveheader</code> option &#8211; with <code>waveheader</code> it&#8217;s broken, because it will write a WAVE header every time the file is opened.</p>
<dt><code>wasapi</code></p>
<dd>Audio output to the Windows Audio Session API.</dl>
<h2>Video Output Drivers</h2>
<p>Video output drivers are interfaces to different video output facilities. The syntax is:</p>
<dl COMPACT>
<dt><code>&#8211;vo=&lt;driver1,driver2,&#8230;[,]&gt;</code></p>
<dd>Specify a priority list of video output drivers to be used. </p>
<p> If the list has a trailing <code>,</code>, mpv will fall back on drivers not contained in the list. </p>
<p> <code>NOTE:</code> See <code>&#8211;vo=help</code> for a list of compiled-in video output drivers. </p>
<p> The recommended output driver is <code>&#8211;vo=gpu</code>, which is the default. All other drivers are for compatibility or special purposes. If the default does not work, it will fallback to other drivers (in the same order as listed by <code>&#8211;vo=help</code>). </p>
<p> Available video output drivers are:</p>
<dt><code>xv</code> (X11 only)</p>
<dd>Uses the XVideo extension to enable hardware-accelerated display. This is the most compatible VO on X, but may be low-quality, and has issues with OSD and subtitle display. </p>
<p> <code>NOTE:</code> This driver is for compatibility with old systems. </p>
<p> The following global options are supported by this video output:</p>
<dt><code>&#8211;xv-adaptor=&lt;number&gt;</code></p>
<dd>Select a specific XVideo adapter (check xvinfo results).</p>
<dt><code>&#8211;xv-port=&lt;number&gt;</code></p>
<dd>Select a specific XVideo port.</p>
<dt><code>&#8211;xv-ck=&lt;cur|use|set&gt;</code></p>
<dd>Select the source from which the color key is taken (default: cur).</p>
<dt><code>cur</code></p>
<dd>The default takes the color key currently set in Xv.</p>
<dt><code>use</code></p>
<dd>Use but do not set the color key from mpv (use the <code>&#8211;colorkey</code> option to change it).</p>
<dt><code>set</code></p>
<dd>Same as use but also sets the supplied color key.</p>
<dt><code>&#8211;xv-ck-method=&lt;none|man|bg|auto&gt;</code></p>
<dd>Sets the color key drawing method (default: man).</p>
<dt><code>none</code></p>
<dd>Disables color-keying.</p>
<dt><code>man</code></p>
<dd>Draw the color key manually (reduces flicker in some cases).</p>
<dt><code>bg</code></p>
<dd>Set the color key as window background.</p>
<dt><code>auto</code></p>
<dd>Let Xv draw the color key.</p>
<dt><code>&#8211;xv-colorkey=&lt;number&gt;</code></p>
<dd>Changes the color key to an RGB value of your choice. <code>0x000000</code> is black and <code>0xffffff</code> is white.</p>
<dt><code>&#8211;xv-buffers=&lt;number&gt;</code></p>
<dd>Number of image buffers to use for the internal ringbuffer (default: 2). Increasing this will use more memory, but might help with the X server not responding quickly enough if video FPS is close to or higher than the display refresh rate.</p>
<dt><code>x11</code> (X11 only)</p>
<dd>Shared memory video output driver without hardware acceleration that works whenever X11 is present. </p>
<p> Since mpv 0.30.0, you may need to use <code>&#8211;profile=sw-fast</code> to get decent performance. </p>
<p> <code>NOTE:</code> This is a fallback only, and should not be normally used.</p>
<dt><code>vdpau</code> (X11 only)</p>
<dd>Uses the VDPAU interface to display and optionally also decode video. Hardware decoding is used with <code>&#8211;hwdec=vdpau</code>. </p>
<p> <code>NOTE:</code> Earlier versions of mpv (and MPlayer, mplayer2) provided sub-options to tune vdpau post-processing, like <code>deint</code>, <code>sharpen</code>, <code>denoise</code>, <code>chroma-deint</code>, <code>pullup</code>, <code>hqscaling</code>. These sub-options are deprecated, and you should use the <code>vdpaupp</code> video filter instead. </p>
<p> The following global options are supported by this video output:</p>
<dt><code>&#8211;vo-vdpau-sharpen=&lt;-1-1&gt;</code></p>
<dd>(Deprecated. See note about <code>vdpaupp</code>.) </p>
<p> For positive values, apply a sharpening algorithm to the video, for negative values a blurring algorithm (default: 0).</p>
<dt><code>&#8211;vo-vdpau-denoise=&lt;0-1&gt;</code></p>
<dd>(Deprecated. See note about <code>vdpaupp</code>.) </p>
<p> Apply a noise reduction algorithm to the video (default: 0; no noise reduction).</p>
<dt><code>&#8211;vo-vdpau-chroma-deint</code></p>
<dd>(Deprecated. See note about <code>vdpaupp</code>.) </p>
<p> Makes temporal deinterlacers operate both on luma and chroma (default). Use no-chroma-deint to solely use luma and speed up advanced deinterlacing. Useful with slow video memory.</p>
<dt><code>&#8211;vo-vdpau-pullup</code></p>
<dd>(Deprecated. See note about <code>vdpaupp</code>.) </p>
<p> Try to apply inverse telecine, needs motion adaptive temporal deinterlacing.</p>
<dt><code>&#8211;vo-vdpau-hqscaling=&lt;0-9&gt;</code></p>
<dd>(Deprecated. See note about <code>vdpaupp</code>.)</p>
<dt><code>0</code></p>
<dd>Use default VDPAU scaling (default).</p>
<dt><code>1-9</code></p>
<dd>Apply high quality VDPAU scaling (needs capable hardware).</p>
<dt><code>&#8211;vo-vdpau-fps=&lt;number&gt;</code></p>
<dd>Override autodetected display refresh rate value (the value is needed for framedrop to allow video playback rates higher than display refresh rate, and for vsync-aware frame timing adjustments). Default 0 means use autodetected value. A positive value is interpreted as a refresh rate in Hz and overrides the autodetected value. A negative value disables all timing adjustment and framedrop logic.</p>
<dt><code>&#8211;vo-vdpau-composite-detect</code></p>
<dd>NVIDIA&#8217;s current VDPAU implementation behaves somewhat differently under a compositing window manager and does not give accurate frame timing information. With this option enabled, the player tries to detect whether a compositing window manager is active. If one is detected, the player disables timing adjustments as if the user had specified <code>fps=-1</code> (as they would be based on incorrect input). This means timing is somewhat less accurate than without compositing, but with the composited mode behavior of the NVIDIA driver, there is no hard playback speed limit even without the disabled logic. Enabled by default, use <code>&#8211;vo-vdpau-composite-detect=no</code> to disable.</p>
<dt><code>&#8211;vo-vdpau-queuetime-windowed=&lt;number&gt;</code> and <code>queuetime-fs=&lt;number&gt;</code></p>
<dd>Use VDPAU&#8217;s presentation queue functionality to queue future video frame changes at most this many milliseconds in advance (default: 50). See below for additional information.</p>
<dt><code>&#8211;vo-vdpau-output-surfaces=&lt;2-15&gt;</code></p>
<dd>Allocate this many output surfaces to display video frames (default: 3). See below for additional information.</p>
<dt><code>&#8211;vo-vdpau-colorkey=&lt;#RRGGBB|#AARRGGBB&gt;</code></p>
<dd>Set the VDPAU presentation queue background color, which in practice is the colorkey used if VDPAU operates in overlay mode (default: <code>#020507</code>, some shade of black). If the alpha component of this value is 0, the default VDPAU colorkey will be used instead (which is usually green).</p>
<dt><code>&#8211;vo-vdpau-force-yuv</code></p>
<dd>Never accept RGBA input. This means mpv will insert a filter to convert to a YUV format before the VO. Sometimes useful to force availability of certain YUV-only features, like video equalizer or deinterlacing. </p>
<p> Using the VDPAU frame queuing functionality controlled by the queuetime options makes mpv&#8217;s frame flip timing less sensitive to system CPU load and allows mpv to start decoding the next frame(s) slightly earlier, which can reduce jitter caused by individual slow-to-decode frames. However, the NVIDIA graphics drivers can make other window behavior such as window moves choppy if VDPAU is using the blit queue (mainly happens if you have the composite extension enabled) and this feature is active. If this happens on your system and it bothers you then you can set the queuetime value to 0 to disable this feature. The settings to use in windowed and fullscreen mode are separate because there should be no reason to disable this for fullscreen mode (as the driver issue should not affect the video itself). </p>
<p> You can queue more frames ahead by increasing the queuetime values and the <code>output_surfaces</code> count (to ensure enough surfaces to buffer video for a certain time ahead you need at least as many surfaces as the video has frames during that time, plus two). This could help make video smoother in some cases. The main downsides are increased video RAM requirements for the surfaces and laggier display response to user commands (display changes only become visible some time after they&#8217;re queued). The graphics driver implementation may also have limits on the length of maximum queuing time or number of queued surfaces that work well or at all.</p>
<dt><code>direct3d</code> (Windows only)</p>
<dd>Video output driver that uses the Direct3D interface. </p>
<p> <code>NOTE:</code> This driver is for compatibility with systems that don&#8217;t provide proper OpenGL drivers, and where ANGLE does not perform well. </p>
<p> The following global options are supported by this video output:</p>
<dt><code>&#8211;vo-direct3d-disable-texture-align</code></p>
<dd>Normally texture sizes are always aligned to 16. With this option enabled, the video texture will always have exactly the same size as the video itself. </p>
<p> Debug options. These might be incorrect, might be removed in the future, might crash, might cause slow downs, etc. Contact the developers if you actually need any of these for performance or proper operation.</p>
<dt><code>&#8211;vo-direct3d-force-power-of-2</code></p>
<dd>Always force textures to power of 2, even if the device reports non-power-of-2 texture sizes as supported.</p>
<dt><code>&#8211;vo-direct3d-texture-memory=&lt;mode&gt;</code></p>
<dd>Only affects operation with shaders/texturing enabled, and (E)OSD. Possible values:</p>
<dt><code>default</code> (default)</p>
<dd>Use <code>D3DPOOL_DEFAULT</code>, with a <code>D3DPOOL_SYSTEMMEM</code> texture for locking. If the driver supports <code>D3DDEVCAPS_TEXTURESYSTEMMEMORY</code>, <code>D3DPOOL_SYSTEMMEM</code> is used directly.</p>
<dt><code>default-pool</code></p>
<dd>Use <code>D3DPOOL_DEFAULT</code>. (Like <code>default</code>, but never use a shadow-texture.)</p>
<dt><code>default-pool-shadow</code></p>
<dd>Use <code>D3DPOOL_DEFAULT</code>, with a <code>D3DPOOL_SYSTEMMEM</code> texture for locking. (Like <code>default</code>, but always force the shadow-texture.)</p>
<dt><code>managed</code></p>
<dd>Use <code>D3DPOOL_MANAGED</code>.</p>
<dt><code>scratch</code></p>
<dd>Use <code>D3DPOOL_SCRATCH</code>, with a <code>D3DPOOL_SYSTEMMEM</code> texture for locking.</p>
<dt><code>&#8211;vo-direct3d-swap-discard</code></p>
<dd>Use <code>D3DSWAPEFFECT_DISCARD</code>, which might be faster. Might be slower too, as it must(?) clear every frame.</p>
<dt><code>&#8211;vo-direct3d-exact-backbuffer</code></p>
<dd>Always resize the backbuffer to window size.</p>
<dt><code>gpu</code></p>
<dd>General purpose, customizable, GPU-accelerated video output driver. It supports extended scaling methods, dithering, color management, custom shaders, HDR, and more. </p>
<p> See <i>GPU renderer options</i> for options specific to this VO. </p>
<p> By default, it tries to use fast and fail-safe settings. Use the <code>gpu-hq</code> profile to use this driver with defaults set to high quality rendering. The profile can be applied with <code>&#8211;profile=gpu-hq</code> and its contents can be viewed with <code>&#8211;show-profile=gpu-hq</code>. </p>
<p> This VO abstracts over several possible graphics APIs and windowing contexts, which can be influenced using the <code>&#8211;gpu-api</code> and <code>&#8211;gpu-context</code> options. </p>
<p> Hardware decoding over OpenGL-interop is supported to some degree. Note that in this mode, some corner case might not be gracefully handled, and color space conversion and chroma upsampling is generally in the hand of the hardware decoder APIs. </p>
<p> <code>gpu</code> makes use of FBOs by default. Sometimes you can achieve better quality or performance by changing the <code>&#8211;fbo-format</code> option to <code>rgb16f</code>, <code>rgb32f</code> or <code>rgb</code>. Known problems include Mesa/Intel not accepting <code>rgb16</code>, Mesa sometimes not being compiled with float texture support, and some macOS setups being very slow with <code>rgb16</code> but fast with <code>rgb32f</code>. If you have problems, you can also try enabling the <code>&#8211;gpu-dumb-mode=yes</code> option.</p>
<dt><code>sdl</code></p>
<dd>SDL 2.0+ Render video output driver, depending on system with or without hardware acceleration. Should work on all platforms supported by SDL 2.0. For tuning, refer to your copy of the file <code>SDL_hints.h</code>. </p>
<p> <code>NOTE:</code> This driver is for compatibility with systems that don&#8217;t provide proper graphics drivers. </p>
<p> The following global options are supported by this video output:</p>
<dt><code>&#8211;sdl-sw</code></p>
<dd>Continue even if a software renderer is detected.</p>
<dt><code>&#8211;sdl-switch-mode</code></p>
<dd>Instruct SDL to switch the monitor video mode when going fullscreen.</p>
<dt><code>vaapi</code></p>
<dd>Intel VA API video output driver with support for hardware decoding. Note that there is absolutely no reason to use this, other than compatibility. This is low quality, and has issues with OSD. </p>
<p> <code>NOTE:</code> This driver is for compatibility with crappy systems. You can use vaapi hardware decoding with <code>&#8211;vo=gpu</code> too. </p>
<p> The following global options are supported by this video output:</p>
<dt><code>&#8211;vo-vaapi-scaling=&lt;algorithm&gt;</code></p>
<dd>
<dt><code>default</code></p>
<dd>Driver default (mpv default as well).</p>
<dt><code>fast</code></p>
<dd>Fast, but low quality.</p>
<dt><code>hq</code></p>
<dd>Unspecified driver dependent high-quality scaling, slow.</p>
<dt><code>nla</code></p>
<dd><code>non-linear anamorphic scaling</code></p>
<dt><code>&#8211;vo-vaapi-deint-mode=&lt;mode&gt;</code></p>
<dd>Select deinterlacing algorithm. Note that by default deinterlacing is initially always off, and needs to be enabled with the <code>d</code> key (default key binding for <code>cycle deinterlace</code>). </p>
<p> This option doesn&#8217;t apply if libva supports video post processing (vpp). In this case, the default for <code>deint-mode</code> is <code>no</code>, and enabling deinterlacing via user interaction using the methods mentioned above actually inserts the <code>vavpp</code> video filter. If vpp is not actually supported with the libva backend in use, you can use this option to forcibly enable VO based deinterlacing.</p>
<dt><code>no</code></p>
<dd>Don&#8217;t allow deinterlacing (default for newer libva).</p>
<dt><code>first-field</code></p>
<dd>Show only first field.</p>
<dt><code>bob</code></p>
<dd>bob deinterlacing (default for older libva).</p>
<dt><code>&#8211;vo-vaapi-scaled-osd=&lt;yes|no&gt;</code></p>
<dd>If enabled, then the OSD is rendered at video resolution and scaled to display resolution. By default, this is disabled, and the OSD is rendered at display resolution if the driver supports it.</p>
<dt><code>null</code></p>
<dd>Produces no video output. Useful for benchmarking. </p>
<p> Usually, it&#8217;s better to disable video with <code>&#8211;no-video</code> instead. </p>
<p> The following global options are supported by this video output:</p>
<dt><code>&#8211;vo-null-fps=&lt;value&gt;</code></p>
<dd>Simulate display FPS. This artificially limits how many frames the VO accepts per second.</p>
<dt><code>caca</code></p>
<dd>Color ASCII art video output driver that works on a text console. </p>
<p> <code>NOTE:</code> This driver is a joke.</p>
<dt><code>tct</code></p>
<dd>Color Unicode art video output driver that works on a text console. By default depends on support of true color by modern terminals to display the images at full color range, but 256-colors output is also supported (see below). On Windows it requires an ansi terminal such as mintty. </p>
<p> Since mpv 0.30.0, you may need to use <code>&#8211;profile=sw-fast</code> to get decent performance. </p>
<p> Note: the TCT image output is not synchronized with other terminal output from mpv, which can lead to broken images. The options <code>&#8211;no-terminal</code> or <code>&#8211;really-quiet</code> can help with that.</p>
<dt><code>&#8211;vo-tct-algo=&lt;algo&gt;</code></p>
<dd>Select how to write the pixels to the terminal.</p>
<dt><code>half-blocks</code></p>
<dd>Uses unicode LOWER HALF BLOCK character to achieve higher vertical resolution. (Default.)</p>
<dt><code>plain</code></p>
<dd>Uses spaces. Causes vertical resolution to drop twofolds, but in theory works in more places.</p>
<dt><code>&#8211;vo-tct-width=&lt;width&gt;</code> <code>&#8211;vo-tct-height=&lt;height&gt;</code></p>
<dd>Assume the terminal has the specified character width and/or height. These default to 80&#215;25 if the terminal size cannot be determined.</p>
<dt><code>&#8211;vo-tct-256=&lt;yes|no&gt;</code> (default: no)</p>
<dd>Use 256 colors &#8211; for terminals which don&#8217;t support true color.</p>
<dt><code>sixel</code></p>
<dd>Graphical output for the terminal, using sixels. Tested with <code>mlterm</code> and <code>xterm</code>. </p>
<p> Note: the Sixel image output is not synchronized with other terminal output from mpv, which can lead to broken images. The option <code>&#8211;really-quiet</code> can help with that, and is recommended. </p>
<p> You may need to use <code>&#8211;profile=sw-fast</code> to get decent performance. </p>
<p> Note: at the time of writing, <code>xterm</code> does not enable sixel by default &#8211; launching it as <code>xterm -ti 340</code> is one way to enable it. Also, <code>xterm</code> does not display images bigger than 1000&#215;1000 pixels by default. </p>
<p> To render and align sixel images correctly, mpv needs to know the terminal size both in cells and in pixels. By default it tries to use values which the terminal reports, however, due to differences between terminals this is an error-prone process which cannot be automated with certainty &#8211; some terminals report the size in pixels including the padding &#8211; e.g. <code>xterm</code>, while others report the actual usable number of pixels &#8211; like <code>mlterm</code>. Additionally, they may behave differently when maximized or in fullscreen, and mpv cannot detect this state using standard methods. </p>
<p> Sixel size and alignment options:</p>
<dt><code>&#8211;vo-sixel-cols=&lt;columns&gt;</code>, <code>&#8211;vo-sixel-rows=&lt;rows&gt;</code> (default: 0)</p>
<dd>Specify the terminal size in character cells, otherwise (0) read it from the terminal, or fall back to 80&#215;25. Note that mpv doesn&#8217;t use the the last row with sixel because this seems to result in scrolling.</p>
<dt><code>&#8211;vo-sixel-width=&lt;width&gt;</code>, <code>&#8211;vo-sixel-height=&lt;height&gt;</code> (default: 0)</p>
<dd>Specify the available size in pixels, otherwise (0) read it from the terminal, or fall back to 320&#215;240. Other than excluding the last line, the height is also further rounded down to a multiple of 6 (sixel unit height) to avoid overflowing below the designated size.</p>
<dt><code>&#8211;vo-sixel-left=&lt;col&gt;</code>, <code>&#8211;vo-sixel-top=&lt;row&gt;</code> (default: 0)</p>
<dd>Specify the position in character cells where the image starts (1 is the first column or row). If 0 (default) then try to automatically determine it according to the other values and the image aspect ratio and zoom.</p>
<dt><code>&#8211;vo-sixel-pad-x=&lt;pad_x&gt;</code>, <code>&#8211;vo-sixel-pad-y=&lt;pad_y&gt;</code> (default: -1)</p>
<dd>Used only when mpv reads the size in pixels from the terminal. Specify the number of padding pixels (on one side) which are included at the size which the terminal reports. If -1 (default) then the number of pixels is rounded down to a multiple of number of cells (per axis), to take into account padding at the report &#8211; this only works correctly when the overall padding per axis is smaller than the number of cells.</p>
<dt><code>&#8211;vo-sixel-exit-clear=&lt;yes|no&gt;</code> (default: yes)</p>
<dd>Whether or not to clear the terminal on quit. When set to no &#8211; the last sixel image stays on screen after quit, with the cursor following it. </p>
<p> Sixel image quality options:</p>
<dt><code>&#8211;vo-sixel-dither=&lt;algo&gt;</code></p>
<dd>Selects the dither algorithm which libsixel should apply. Can be one of the below list as per libsixel&#8217;s documentation.</p>
<dt><code>auto (Default)</code></p>
<dd>Let libsixel choose the dithering method.</p>
<dt><code>none</code></p>
<dd>Don&#8217;t diffuse</p>
<dt><code>atkinson</code></p>
<dd>Diffuse with Bill Atkinson&#8217;s method.</p>
<dt><code>fs</code></p>
<dd>Diffuse with Floyd-Steinberg method</p>
<dt><code>jajuni</code></p>
<dd>Diffuse with Jarvis, Judice &amp; Ninke method</p>
<dt><code>stucki</code></p>
<dd>Diffuse with Stucki&#8217;s method</p>
<dt><code>burkes</code></p>
<dd>Diffuse with Burkes&#8217; method</p>
<dt><code>arithmetic</code></p>
<dd>Positionally stable arithmetic dither</p>
<dt><code>xor</code></p>
<dd>Positionally stable arithmetic xor based dither</p>
<dt><code>&#8211;vo-sixel-fixedpalette=&lt;yes|no&gt;</code> (default: yes)</p>
<dd>Use libsixel&#8217;s built-in static palette using the XTERM256 profile for dither. Fixed palette uses 256 colors for dithering. Note that using <code>no</code> (at the time of writing) will slow down <code>xterm</code>.</p>
<dt><code>&#8211;vo-sixel-reqcolors=&lt;colors&gt;</code> (default: 256)</p>
<dd>Has no effect with fixed palette. Set up libsixel to use required number of colors for dynamic palette. This value depends on the terminal emulator as well. Xterm supports 256 colors. Can set this to a lower value for faster performance.</p>
<dt><code>&#8211;vo-sixel-threshold=&lt;threshold&gt;</code> (default: -1)</p>
<dd>Has no effect with fixed palette. Defines the threshold to change the palette &#8211; as percentage of the number of colors, e.g. 20 will change the palette when the number of colors changed by 20%. It&#8217;s a simple measure to reduce the number of palette changes, because it can be slow in some terminals (<code>xterm</code>). The default (-1) will choose a palette on every frame and will have better quality.</p>
<dt><code>image</code></p>
<dd>Output each frame into an image file in the current directory. Each file takes the frame number padded with leading zeros as name. </p>
<p> The following global options are supported by this video output:</p>
<dt><code>&#8211;vo-image-format=&lt;format&gt;</code></p>
<dd>Select the image file format.</p>
<dt><code>jpg</code></p>
<dd>JPEG files, extension .jpg. (Default.)</p>
<dt><code>jpeg</code></p>
<dd>JPEG files, extension .jpeg.</p>
<dt><code>png</code></p>
<dd>PNG files.</p>
<dt><code>webp</code></p>
<dd>WebP files.</p>
<dt><code>&#8211;vo-image-png-compression=&lt;0-9&gt;</code></p>
<dd>PNG compression factor (speed vs. file size tradeoff) (default: 7)</p>
<dt><code>&#8211;vo-image-png-filter=&lt;0-5&gt;</code></p>
<dd>Filter applied prior to PNG compression (0 = none; 1 = sub; 2 = up; 3 = average; 4 = Paeth; 5 = mixed) (default: 5)</p>
<dt><code>&#8211;vo-image-jpeg-quality=&lt;0-100&gt;</code></p>
<dd>JPEG quality factor (default: 90)</p>
<dt><code>&#8211;vo-image-jpeg-optimize=&lt;0-100&gt;</code></p>
<dd>JPEG optimization factor (default: 100)</p>
<dt><code>&#8211;vo-image-webp-lossless=&lt;yes|no&gt;</code></p>
<dd>Enable writing lossless WebP files (default: no)</p>
<dt><code>&#8211;vo-image-webp-quality=&lt;0-100&gt;</code></p>
<dd>WebP quality (default: 75)</p>
<dt><code>&#8211;vo-image-webp-compression=&lt;0-6&gt;</code></p>
<dd>WebP compression factor (default: 4)</p>
<dt><code>&#8211;vo-image-outdir=&lt;dirname&gt;</code></p>
<dd>Specify the directory to save the image files to (default: <code>./</code>).</p>
<dt><code>libmpv</code></p>
<dd>For use with libmpv direct embedding. As a special case, on macOS it is used like a normal VO within mpv (cocoa-cb). Otherwise useless in any other contexts. (See <code>&lt;mpv/render.h&gt;</code>.) </p>
<p> This also supports many of the options the <code>gpu</code> VO has, depending on the backend.</p>
<dt><code>rpi</code> (Raspberry Pi)</p>
<dd>Native video output on the Raspberry Pi using the MMAL API. </p>
<p> This is deprecated. Use <code>&#8211;vo=gpu</code> instead, which is the default and provides the same functionality. The <code>rpi</code> VO will be removed in mpv 0.23.0. Its functionality was folded into &#8211;vo=gpu, which now uses RPI hardware decoding by treating it as a hardware overlay (without applying GL filtering). Also to be changed in 0.23.0: the &#8211;fs flag will be reset to &quot;no&quot; by default (like on the other platforms). </p>
<p> The following deprecated global options are supported by this video output:</p>
<dt><code>&#8211;rpi-display=&lt;number&gt;</code></p>
<dd>Select the display number on which the video overlay should be shown (default: 0).</p>
<dt><code>&#8211;rpi-layer=&lt;number&gt;</code></p>
<dd>Select the dispmanx layer on which the video overlay should be shown (default: -10). Note that mpv will also use the 2 layers above the selected layer, to handle the window background and OSD. Actual video rendering will happen on the layer above the selected layer.</p>
<dt><code>&#8211;rpi-background=&lt;yes|no&gt;</code></p>
<dd>Whether to render a black background behind the video (default: no). Normally it&#8217;s better to kill the console framebuffer instead, which gives better performance.</p>
<dt><code>&#8211;rpi-osd=&lt;yes|no&gt;</code></p>
<dd>Enabled by default. If disabled with <code>no</code>, no OSD layer is created. This also means there will be no subtitles rendered.</p>
<dt><code>drm</code> (Direct Rendering Manager)</p>
<dd>Video output driver using Kernel Mode Setting / Direct Rendering Manager. Should be used when one doesn&#8217;t want to install full-blown graphical environment (e.g. no X). Does not support hardware acceleration (if you need this, check the <code>drm</code> backend for <code>gpu</code> VO). </p>
<p> Since mpv 0.30.0, you may need to use <code>&#8211;profile=sw-fast</code> to get decent performance. </p>
<p> The following global options are supported by this video output:</p>
<dt><code>&#8211;drm-connector=[&lt;gpu_number&gt;.]&lt;name&gt;</code></p>
<dd>Select the connector to use (usually this is a monitor.) If <code>&lt;name&gt;</code> is empty or <code>auto</code>, mpv renders the output on the first available connector. Use <code>&#8211;drm-connector=help</code> to get a list of available connectors. The <code>&lt;gpu_number&gt;</code> argument can be used to disambiguate multiple graphic cards, but is deprecated in favor of <code>&#8211;drm-device</code>. (default: empty)</p>
<dt><code>&#8211;drm-device=&lt;path&gt;</code></p>
<dd>Select the DRM device file to use. If specified this overrides automatic card selection and any card number specified <code>&#8211;drm-connector</code>. (default: empty)</p>
<dt><code>&#8211;drm-mode=&lt;preferred|highest|N|WxH[@R]&gt;</code></p>
<dd>Mode to use (resolution and frame rate). Possible values:</p>
<dt><code>preferred</code></p>
<dd>Use the preferred mode for the screen on the selected connector. (default)</p>
<dt><code>highest</code></p>
<dd>Use the mode with the highest resolution available on the selected connector.</p>
<dt><code>N</code></p>
<dd>Select mode by index.</p>
<dt><code>WxH[@R]</code></p>
<dd>Specify mode by width, height, and optionally refresh rate. In case several modes match, selects the mode that comes first in the EDID list of modes. </p>
<p> Use <code>&#8211;drm-mode=help</code> to get a list of available modes for all active connectors.</p>
<dt><code>&#8211;drm-atomic=&lt;no|auto&gt;</code></p>
<dd>Toggle use of atomic modesetting. Mostly useful for debugging.</p>
<dt><code>no</code></p>
<dd>Use legacy modesetting.</p>
<dt><code>auto</code></p>
<dd>Use atomic modesetting, falling back to legacy modesetting if not available. (default) </p>
<p> Note: Only affects <code>gpu-context=drm</code>. <code>vo=drm</code> supports legacy modesetting only.</p>
<dt><code>&#8211;drm-draw-plane=&lt;primary|overlay|N&gt;</code></p>
<dd>Select the DRM plane to which video and OSD is drawn to, under normal circumstances. The plane can be specified as <code>primary</code>, which will pick the first applicable primary plane; <code>overlay</code>, which will pick the first applicable overlay plane; or by index. The index is zero based, and related to the CRTC. (default: primary) </p>
<p> When using this option with the drmprime-drm hwdec interop, only the OSD is rendered to this plane.</p>
<dt><code>&#8211;drm-drmprime-video-plane=&lt;primary|overlay|N&gt;</code></p>
<dd>Select the DRM plane to use for video with the drmprime-drm hwdec interop (used by e.g. the rkmpp hwdec on RockChip SoCs, and v4l2 hwdec:s on various other SoC:s). The plane is unused otherwise. This option accepts the same values as <code>&#8211;drm-draw-plane</code>. (default: overlay) </p>
<p> To be able to successfully play 4K video on various SoCs you might need to set <code>&#8211;drm-draw-plane=overlay &#8211;drm-drmprime-video-plane=primary</code> and setting <code>&#8211;drm-draw-surface-size=1920&#215;1080</code>, to render the OSD at a lower resolution (the video when handled by the hwdec will be on the drmprime-video plane and at full 4K resolution)</p>
<dt><code>&#8211;drm-format=&lt;xrgb8888|xrgb2101010&gt;</code></p>
<dd>Select the DRM format to use (default: xrgb8888). This allows you to choose the bit depth of the DRM mode. xrgb8888 is your usual 24 bit per pixel/8 bits per channel packed RGB format with 8 bits of padding. xrgb2101010 is a packed 30 bits per pixel/10 bits per channel packed RGB format with 2 bits of padding. </p>
<p> There are cases when xrgb2101010 will work with the <code>drm</code> VO, but not with the <code>drm</code> backend for the <code>gpu</code> VO. This is because with the <code>gpu</code> VO, in addition to requiring support in your DRM driver, requires support for xrgb2101010 in your EGL driver</p>
<dt><code>&#8211;drm-draw-surface-size=&lt;[WxH]&gt;</code></p>
<dd>Sets the size of the surface used on the draw plane. The surface will then be upscaled to the current screen resolution. This option can be useful when used together with the drmprime-drm hwdec interop at high resolutions, as it allows scaling the draw plane (which in this case only handles the OSD) down to a size the GPU can handle. </p>
<p> When used without the drmprime-drm hwdec interop this option will just cause the video to get rendered at a different resolution and then scaled to screen size. </p>
<p> Note: this option is only available with DRM atomic support. (default: display resolution)</p>
<dt><code>mediacodec_embed</code> (Android)</p>
<dd>Renders <code>IMGFMT_MEDIACODEC</code> frames directly to an <code>android.view.Surface</code>. Requires <code>&#8211;hwdec=mediacodec</code> for hardware decoding, along with <code>&#8211;vo=mediacodec_embed</code> and <code>&#8211;wid=(intptr_t)(*android.view.Surface)</code>. </p>
<p> Since this video output driver uses native decoding and rendering routines, many of mpv&#8217;s features (subtitle rendering, OSD/OSC, video filters, etc) are not available with this driver. </p>
<p> To use hardware decoding with <code>&#8211;vo=gpu</code> instead, use <code>&#8211;hwdec=mediacodec-copy</code> along with <code>&#8211;gpu-context=android</code>.</p>
<dt><code>wlshm</code> (Wayland only)</p>
<dd>Shared memory video output driver without hardware acceleration that works whenever Wayland is present. </p>
<p> Since mpv 0.30.0, you may need to use <code>&#8211;profile=sw-fast</code> to get decent performance. </p>
<p> <code>NOTE:</code> This is a fallback only, and should not be normally used.</dl>
<h2>Audio Filters</h2>
<p>Audio filters allow you to modify the audio stream and its properties. The syntax is:</p>
<dl COMPACT>
<dt><code>&#8211;af=&#8230;</code></p>
<dd>Setup a chain of audio filters. See <code>&#8211;vf</code> (<i>VIDEO FILTERS</i>) for the full syntax. </p>
<p> <code>NOTE:</code> To get a full list of available audio filters, see <code>&#8211;af=help</code>. </p>
<p> Also, keep in mind that most actual filters are available via the <code>lavfi</code> wrapper, which gives you access to most of libavfilter&#8217;s filters. This includes all filters that have been ported from MPlayer to libavfilter. </p>
<p> The <code>&#8211;vf</code> description describes how libavfilter can be used and how to workaround deprecated mpv filters. </p>
<p> See <code>&#8211;vf</code> group of options for info on how <code>&#8211;af-defaults</code>, <code>&#8211;af-add</code>, <code>&#8211;af-pre</code>, <code>&#8211;af-del</code>, <code>&#8211;af-clr</code>, and possibly others work. </p>
<p> Available filters are:</p>
<dt><code>lavcac3enc[=options]</code></p>
<dd>Encode multi-channel audio to AC-3 at runtime using libavcodec. Supports 16-bit native-endian input format, maximum 6 channels. The output is big-endian when outputting a raw AC-3 stream, native-endian when outputting to S/PDIF. If the input sample rate is not 48 kHz, 44.1 kHz or 32 kHz, it will be resampled to 48 kHz.</p>
<dt><code>tospdif=&lt;yes|no&gt;</code></p>
<dd>Output raw AC-3 stream if <code>no</code>, output to S/PDIF for pass-through if <code>yes</code> (default).</p>
<dt><code>bitrate=&lt;rate&gt;</code></p>
<dd>The bitrate use for the AC-3 stream. Set it to 384 to get 384 kbps. </p>
<p> The default is 640. Some receivers might not be able to handle this. </p>
<p> Valid values: 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 384, 448, 512, 576, 640. </p>
<p> The special value <code>auto</code> selects a default bitrate based on the input channel number:</p>
<dt><code>1ch</code></p>
<dd>96</p>
<dt><code>2ch</code></p>
<dd>192</p>
<dt><code>3ch</code></p>
<dd>224</p>
<dt><code>4ch</code></p>
<dd>384</p>
<dt><code>5ch</code></p>
<dd>448</p>
<dt><code>6ch</code></p>
<dd>448</p>
<dt><code>minch=&lt;n&gt;</code></p>
<dd>If the input channel number is less than <code>&lt;minch&gt;</code>, the filter will detach itself (default: 3).</p>
<dt><code>encoder=&lt;name&gt;</code></p>
<dd>Select the libavcodec encoder used. Currently, this should be an AC-3 encoder, and using another codec will fail horribly.</p>
<dt><code>format=format:srate:channels:out-srate:out-channels</code></p>
<dd>Does not do any format conversion itself. Rather, it may cause the filter system to insert necessary conversion filters before or after this filter if needed. It is primarily useful for controlling the audio format going into other filters. To specify the format for audio output, see <code>&#8211;audio-format</code>, <code>&#8211;audio-samplerate</code>, and <code>&#8211;audio-channels</code>. This filter is able to force a particular format, whereas <code>&#8211;audio-*</code> may be overridden by the ao based on output compatibility. </p>
<p> All parameters are optional. The first 3 parameters restrict what the filter accepts as input. They will therefore cause conversion filters to be inserted before this one. The <code>out-</code> parameters tell the filters or audio outputs following this filter how to interpret the data without actually doing a conversion. Setting these will probably just break things unless you really know you want this for some reason, such as testing or dealing with broken media.</p>
<dt><code>&lt;format&gt;</code></p>
<dd>Force conversion to this format. Use <code>&#8211;af=format=format=help</code> to get a list of valid formats.</p>
<dt><code>&lt;srate&gt;</code></p>
<dd>Force conversion to a specific sample rate. The rate is an integer, 48000 for example.</p>
<dt><code>&lt;channels&gt;</code></p>
<dd>Force mixing to a specific channel layout. See <code>&#8211;audio-channels</code> option for possible values. </p>
<p> <code>&lt;out-srate&gt;</code> </p>
<p> <code>&lt;out-channels&gt;</code> </p>
<p> <i>NOTE</i>: this filter used to be named <code>force</code>. The old <code>format</code> filter used to do conversion itself, unlike this one which lets the filter system handle the conversion.</p>
<dt><code>scaletempo[=option1:option2:&#8230;]</code></p>
<dd>Scales audio tempo without altering pitch, optionally synced to playback speed (default). </p>
<p> This works by playing &#8216;stride&#8217; ms of audio at normal speed then consuming &#8216;stride*scale&#8217; ms of input audio. It pieces the strides together by blending &#8216;overlap&#8217;% of stride with audio following the previous stride. It optionally performs a short statistical analysis on the next &#8216;search&#8217; ms of audio to determine the best overlap position.</p>
<dt><code>scale=&lt;amount&gt;</code></p>
<dd>Nominal amount to scale tempo. Scales this amount in addition to speed. (default: 1.0)</p>
<dt><code>stride=&lt;amount&gt;</code></p>
<dd>Length in milliseconds to output each stride. Too high of a value will cause noticeable skips at high scale amounts and an echo at low scale amounts. Very low values will alter pitch. Increasing improves performance. (default: 60)</p>
<dt><code>overlap=&lt;percent&gt;</code></p>
<dd>Percentage of stride to overlap. Decreasing improves performance. (default: .20)</p>
<dt><code>search=&lt;amount&gt;</code></p>
<dd>Length in milliseconds to search for best overlap position. Decreasing improves performance greatly. On slow systems, you will probably want to set this very low. (default: 14)</p>
<dt><code>speed=&lt;tempo|pitch|both|none&gt;</code></p>
<dd>Set response to speed change.</p>
<dt><code>tempo</code></p>
<dd>Scale tempo in sync with speed (default).</p>
<dt><code>pitch</code></p>
<dd>Reverses effect of filter. Scales pitch without altering tempo. Add this to your <code>input.conf</code> to step by musical semi-tones: </p>
<pre>[ multiply speed 0.9438743126816935
] multiply speed 1.059463094352953</pre>
<p><code>WARNING:</code> Loses sync with video.</p>
<dt><code>both</code></p>
<dd>Scale both tempo and pitch.</p>
<dt><code>none</code></p>
<dd>Ignore speed changes.</p>
<dt>Examples</p>
<dd>
<dt><code>mpv &#8211;af=scaletempo &#8211;speed=1.2 media.ogg</code></p>
<dd>Would play media at 1.2x normal speed, with audio at normal pitch. Changing playback speed would change audio tempo to match.</p>
<dt><code>mpv &#8211;af=scaletempo=scale=1.2:speed=none &#8211;speed=1.2 media.ogg</code></p>
<dd>Would play media at 1.2x normal speed, with audio at normal pitch, but changing playback speed would have no effect on audio tempo.</p>
<dt><code>mpv &#8211;af=scaletempo=stride=30:overlap=.50:search=10 media.ogg</code></p>
<dd>Would tweak the quality and performance parameters.</p>
<dt><code>mpv &#8211;af=scaletempo=scale=1.2:speed=pitch audio.ogg</code></p>
<dd>Would play media at 1.2x normal speed, with audio at normal pitch. Changing playback speed would change pitch, leaving audio tempo at 1.2x.</p>
<dt><code>scaletempo2[=option1:option2:&#8230;]</code></p>
<dd>Scales audio tempo without altering pitch. The algorithm is ported from chromium and uses the Waveform Similarity Overlap-and-add (WSOLA) method. It seems to achieve a higher audio quality than scaletempo and rubberband. </p>
<p> By default, the <code>search-interval</code> and <code>window-size</code> parameters have the same values as in chromium.</p>
<dt><code>min-speed=&lt;speed&gt;</code></p>
<dd>Mute audio if the playback speed is below <code>&lt;speed&gt;</code>. (default: 0.25)</p>
<dt><code>max-speed=&lt;speed&gt;</code></p>
<dd>Mute audio if the playback speed is above <code>&lt;speed&gt;</code> and <code>&lt;speed&gt; != 0</code>. (default: 4.0)</p>
<dt><code>search-interval=&lt;amount&gt;</code></p>
<dd>Length in milliseconds to search for best overlap position. (default: 30)</p>
<dt><code>window-size=&lt;amount&gt;</code></p>
<dd>Length in milliseconds of the overlap-and-add window. (default: 20)</p>
<dt><code>rubberband</code></p>
<dd>High quality pitch correction with librubberband. This can be used in place of <code>scaletempo</code>, and will be used to adjust audio pitch when playing at speed different from normal. It can also be used to adjust audio pitch without changing playback speed.</p>
<dt><code>&lt;pitch-scale&gt;</code></p>
<dd>Sets the pitch scaling factor. Frequencies are multiplied by this value. </p>
<p> This filter has a number of additional sub-options. You can list them with <code>mpv &#8211;af=rubberband=help</code>. This will also show the default values for each option. The options are not documented here, because they are merely passed to librubberband. Look at the librubberband documentation to learn what each option does: <i><a rel="nofollow" href="https://breakfastquay.com/rubberband/code-doc/classRubberBand_1_1RubberBandStretcher.html">https://breakfastquay.com/rubberband/code-doc/classRubberBand_1_1RubberBandStretcher.html</a></i> (The mapping of the mpv rubberband filter sub-option names and values to those of librubberband follows a simple pattern: <code>&quot;Option&quot; + Name + Value</code>.) </p>
<p> This filter supports the following <code>af-command</code> commands:</p>
<dt><code>set-pitch</code></p>
<dd>Set the <code>&lt;pitch-scale&gt;</code> argument dynamically. This can be used to change the playback pitch at runtime. Note that speed is controlled using the standard <code>speed</code> property, not <code>af-command</code>.</p>
<dt><code>multiply-pitch &lt;factor&gt;</code></p>
<dd>Multiply the current value of <code>&lt;pitch-scale&gt;</code> dynamically. For example: 0.5 to go down by an octave, 1.5 to go up by a perfect fifth. If you want to go up or down by semi-tones, use 1.059463094352953 and 0.9438743126816935</p>
<dt><code>lavfi=graph</code></p>
<dd>Filter audio using FFmpeg&#8217;s libavfilter.</p>
<dt><code>&lt;graph&gt;</code></p>
<dd>Libavfilter graph. See <code>lavfi</code> video filter for details &#8211; the graph syntax is the same. </p>
<p> <code>WARNING:</code> Don&#8217;t forget to quote libavfilter graphs as described in the lavfi video filter section.</p>
<dt><code>o=&lt;string&gt;</code></p>
<dd>AVOptions.</p>
<dt><code>fix-pts=&lt;yes|no&gt;</code></p>
<dd>Determine PTS based on sample count (default: no). If this is enabled, the player won&#8217;t rely on libavfilter passing through PTS accurately. Instead, it pass a sample count as PTS to libavfilter, and compute the PTS used by mpv based on that and the input PTS. This helps with filters which output a recomputed PTS instead of the original PTS (including filters which require the PTS to start at 0). mpv normally expects filters to not touch the PTS (or only to the extent of changing frame boundaries), so this is not the default, but it will be needed to use broken filters. In practice, these broken filters will either cause slow A/V desync over time (with some files), or break playback completely if you seek or start playback from the middle of a file.</p>
<dt><code>drop</code></p>
<dd>This filter drops or repeats audio frames to adapt to playback speed. It always operates on full audio frames, because it was made to handle SPDIF (compressed audio passthrough). This is used automatically if the <code>&#8211;video-sync=display-adrop</code> option is used. Do not use this filter (or the given option); they are extremely low quality.</dl>
<h2>Video Filters</h2>
<p>Video filters allow you to modify the video stream and its properties. All of the information described in this section applies to audio filters as well (generally using the prefix <code>&#8211;af</code> instead of <code>&#8211;vf</code>). </p>
<p> The exact syntax is:</p>
<dl COMPACT>
<dt><code>&#8211;vf=&lt;filter1[=parameter1:parameter2:&#8230;],filter2,&#8230;&gt;</code></p>
<dd>Setup a chain of video filters. This consists on the filter name, and an option list of parameters after <code>=</code>. The parameters are separated by <code>:</code> (not <code>,</code>, as that starts a new filter entry). </p>
<p> Before the filter name, a label can be specified with <code>@name:</code>, where name is an arbitrary user-given name, which identifies the filter. This is only needed if you want to toggle the filter at runtime. </p>
<p> A <code>!</code> before the filter name means the filter is disabled by default. It will be skipped on filter creation. This is also useful for runtime filter toggling. </p>
<p> See the <code>vf</code> command (and <code>toggle</code> sub-command) for further explanations and examples. </p>
<p> The general filter entry syntax is: <code>[&quot;@&quot;&lt;label-name&gt;&quot;:&quot;] [&quot;!&quot;] &lt;filter-name&gt; [ &quot;=&quot; &lt;filter-parameter-list&gt; ]</code> </p>
<p> or for the special &quot;toggle&quot; syntax (see <code>vf</code> command): <code>&quot;@&quot;&lt;label-name&gt;</code> </p>
<p> and the <code>filter-parameter-list</code>: <code>&lt;filter-parameter&gt; | &lt;filter-parameter&gt; &quot;,&quot; &lt;filter-parameter-list&gt;</code> </p>
<p> and <code>filter-parameter</code>: <code>( &lt;param-name&gt; &quot;=&quot; &lt;param-value&gt; ) | &lt;param-value&gt;</code> </p>
<p> <code>param-value</code> can further be quoted in <code>[</code> / <code>]</code> in case the value contains characters like <code>,</code> or <code>=</code>. This is used in particular with the <code>lavfi</code> filter, which uses a very similar syntax as mpv (MPlayer historically) to specify filters and their parameters. </p>
<p> Filters can be manipulated at run time. You can use <code>@</code> labels as described above in combination with the <code>vf</code> command (see <i>COMMAND INTERFACE</i>) to get more control over this. Initially disabled filters with <code>!</code> are useful for this as well. </p>
<p> You can also set defaults for each filter. The defaults are applied before the normal filter parameters. This is deprecated and never worked for the libavfilter bridge.</p>
<dt><code>&#8211;vf-defaults=&lt;filter1[=parameter1:parameter2:&#8230;],filter2,&#8230;&gt;</code></p>
<dd>Set defaults for each filter. (Deprecated. <code>&#8211;af-defaults</code> is deprecated as well.) </p>
<p> <code>NOTE:</code> To get a full list of available video filters, see <code>&#8211;vf=help</code> and <i><a rel="nofollow" href="https://ffmpeg.org/ffmpeg-filters.html">https://ffmpeg.org/ffmpeg-filters.html</a></i> . </p>
<p> Also, keep in mind that most actual filters are available via the <code>lavfi</code> wrapper, which gives you access to most of libavfilter&#8217;s filters. This includes all filters that have been ported from MPlayer to libavfilter. </p>
<p> Most builtin filters are deprecated in some ways, unless they&#8217;re only available in mpv (such as filters which deal with mpv specifics, or which are implemented in mpv only). </p>
<p> If a filter is not builtin, the <code>lavfi-bridge</code> will be automatically tried. This bridge does not support help output, and does not verify parameters before the filter is actually used. Although the mpv syntax is rather similar to libavfilter&#8217;s, it&#8217;s not the same. (Which means not everything accepted by vf_lavfi&#8217;s <code>graph</code> option will be accepted by <code>&#8211;vf</code>.) </p>
<p> You can also prefix the filter name with <code>lavfi-</code> to force the wrapper. This is helpful if the filter name collides with a deprecated mpv builtin filter. For example <code>&#8211;vf=lavfi-scale=args</code> would use libavfilter&#8217;s <code>scale</code> filter over mpv&#8217;s deprecated builtin one. </p>
<p> Video filters are managed in lists. There are a few commands to manage the filter list.</p>
<dt><code>&#8211;vf-append=filter</code></p>
<dd>Appends the filter given as arguments to the filter list.</p>
<dt><code>&#8211;vf-add=filter</code></p>
<dd>Appends the filter given as arguments to the filter list. (Passing multiple filters is currently still possible, but deprecated.)</p>
<dt><code>&#8211;vf-pre=filter</code></p>
<dd>Prepends the filters given as arguments to the filter list. (Passing multiple filters is currently still possible, but deprecated.)</p>
<dt><code>&#8211;vf-remove=filter</code></p>
<dd>Deletes the filter from the list. The filter can be either given the way it was added (filter name and its full argument list), or by label (prefixed with <code>@</code>). Matching of filters works as follows: if either of the compared filters has a label set, only the labels are compared. If none of the filters have a label, the filter name, arguments, and argument order are compared. (Passing multiple filters is currently still possible, but deprecated.)</p>
<dt><code>-vf-toggle=filter</code></p>
<dd>Add the given filter to the list if it was not present yet, or remove it from the list if it was present. Matching of filters works as described in <code>&#8211;vf-remove</code>.</p>
<dt><code>&#8211;vf-del=filter</code></p>
<dd>Sort of like <code>&#8211;vf-remove</code>, but also accepts an index number. Index numbers start at 0, negative numbers address the end of the list (-1 is the last). Deprecated.</p>
<dt><code>&#8211;vf-clr</code></p>
<dd>Completely empties the filter list. </p>
<p> With filters that support it, you can access parameters by their name.</p>
<dt><code>&#8211;vf=&lt;filter&gt;=help</code></p>
<dd>Prints the parameter names and parameter value ranges for a particular filter. </p>
<p> Available mpv-only filters are:</p>
<dt><code>format=fmt=&lt;value&gt;:colormatrix=&lt;value&gt;:&#8230;</code></p>
<dd>Applies video parameter overrides, with optional conversion. By default, this overrides the video&#8217;s parameters without conversion (except for the <code>fmt</code> parameter), but can be made to perform an appropriate conversion with <code>convert=yes</code> for parameters for which conversion is supported.</p>
<dt><code>&lt;fmt&gt;</code></p>
<dd>Image format name, e.g. rgb15, bgr24, 420p, etc. (default: don&#8217;t change). </p>
<p> This filter always performs conversion to the given format. </p>
<p> <code>NOTE:</code> For a list of available formats, use <code>&#8211;vf=format=fmt=help</code>.</p>
<dt><code>&lt;convert=yes|no&gt;</code></p>
<dd>Force conversion of color parameters (default: no). </p>
<p> If this is disabled (the default), the only conversion that is possibly performed is format conversion if <code>&lt;fmt&gt;</code> is set. All other parameters (like <code>&lt;colormatrix&gt;</code>) are forced without conversion. This mode is typically useful when files have been incorrectly tagged. </p>
<p> If this is enabled, libswscale or zimg is used if any of the parameters mismatch. zimg is used of the input/output image formats are supported by mpv&#8217;s zimg wrapper, and if <code>&#8211;sws-allow-zimg=yes</code> is used. Both libraries may not support all kinds of conversions. This typically results in silent incorrect conversion. zimg has in many cases a better chance of performing the conversion correctly. </p>
<p> In both cases, the color parameters are set on the output stage of the image format conversion (if <code>fmt</code> was set). The difference is that with <code>convert=no</code>, the color parameters are not passed on to the converter. </p>
<p> If input and output video parameters are the same, conversion is always skipped.</p>
<dt>Examples</p>
<dd>
<dt><code>mpv test.mkv &#8211;vf=format:colormatrix=ycgco</code></p>
<dd>Results in incorrect colors (if test.mkv was tagged correctly).</p>
<dt><code>mpv test.mkv &#8211;vf=format:colormatrix=ycgco:convert=yes &#8211;sws-allow-zimg</code></p>
<dd>Results in true conversion to <code>ycgco</code>, assuming the renderer supports it (<code>&#8211;vo=gpu</code> normally does). You can add <code>&#8211;vo=xv</code> to force a VO which definitely does not support it, which should show incorrect colors as confirmation. </p>
<p> Using <code>&#8211;sws-allow-zimg=no</code> (or disabling zimg at build time) will use libswscale, which cannot perform this conversion as of this writing.</p>
<dt><code>&lt;colormatrix&gt;</code></p>
<dd>Controls the YUV to RGB color space conversion when playing video. There are various standards. Normally, BT.601 should be used for SD video, and BT.709 for HD video. (This is done by default.) Using incorrect color space results in slightly under or over saturated and shifted colors. </p>
<p> These options are not always supported. Different video outputs provide varying degrees of support. The <code>gpu</code> and <code>vdpau</code> video output drivers usually offer full support. The <code>xv</code> output can set the color space if the system video driver supports it, but not input and output levels. The <code>scale</code> video filter can configure color space and input levels, but only if the output format is RGB (if the video output driver supports RGB output, you can force this with <code>-vf scale,format=rgba</code>). </p>
<p> If this option is set to <code>auto</code> (which is the default), the video&#8217;s color space flag will be used. If that flag is unset, the color space will be selected automatically. This is done using a simple heuristic that attempts to distinguish SD and HD video. If the video is larger than 1279&#215;576 pixels, BT.709 (HD) will be used; otherwise BT.601 (SD) is selected. </p>
<p> Available color spaces are:</p>
<dt><code>auto</code></p>
<dd>automatic selection (default)</p>
<dt><code>bt.601</code></p>
<dd>ITU-R BT.601 (SD)</p>
<dt><code>bt.709</code></p>
<dd>ITU-R BT.709 (HD)</p>
<dt><code>bt.2020-ncl</code></p>
<dd>ITU-R BT.2020 non-constant luminance system</p>
<dt><code>bt.2020-cl</code></p>
<dd>ITU-R BT.2020 constant luminance system</p>
<dt><code>smpte-240m</code></p>
<dd>SMPTE-240M</p>
<dt><code>&lt;colorlevels&gt;</code></p>
<dd>YUV color levels used with YUV to RGB conversion. This option is only necessary when playing broken files which do not follow standard color levels or which are flagged wrong. If the video does not specify its color range, it is assumed to be limited range. </p>
<p> The same limitations as with <code>&lt;colormatrix&gt;</code> apply. </p>
<p> Available color ranges are:</p>
<dt><code>auto</code></p>
<dd>automatic selection (normally limited range) (default)</p>
<dt><code>limited</code></p>
<dd>limited range (16-235 for luma, 16-240 for chroma)</p>
<dt><code>full</code></p>
<dd>full range (0-255 for both luma and chroma)</p>
<dt><code>&lt;primaries&gt;</code></p>
<dd>RGB primaries the source file was encoded with. Normally this should be set in the file header, but when playing broken or mistagged files this can be used to override the setting. </p>
<p> This option only affects video output drivers that perform color management, for example <code>gpu</code> with the <code>target-prim</code> or <code>icc-profile</code> suboptions set. </p>
<p> If this option is set to <code>auto</code> (which is the default), the video&#8217;s primaries flag will be used. If that flag is unset, the color space will be selected automatically, using the following heuristics: If the <code>&lt;colormatrix&gt;</code> is set or determined as BT.2020 or BT.709, the corresponding primaries are used. Otherwise, if the video height is exactly 576 (PAL), BT.601-625 is used. If it&#8217;s exactly 480 or 486 (NTSC), BT.601-525 is used. If the video resolution is anything else, BT.709 is used. </p>
<p> Available primaries are:</p>
<dt><code>auto</code></p>
<dd>automatic selection (default)</p>
<dt><code>bt.601-525</code></p>
<dd>ITU-R BT.601 (SD) 525-line systems (NTSC, SMPTE-C)</p>
<dt><code>bt.601-625</code></p>
<dd>ITU-R BT.601 (SD) 625-line systems (PAL, SECAM)</p>
<dt><code>bt.709</code></p>
<dd>ITU-R BT.709 (HD) (same primaries as sRGB)</p>
<dt><code>bt.2020</code></p>
<dd>ITU-R BT.2020 (UHD)</p>
<dt><code>apple</code></p>
<dd>Apple RGB</p>
<dt><code>adobe</code></p>
<dd>Adobe RGB (1998)</p>
<dt><code>prophoto</code></p>
<dd>ProPhoto RGB (ROMM)</p>
<dt><code>cie1931</code></p>
<dd>CIE 1931 RGB</p>
<dt><code>dci-p3</code></p>
<dd>DCI-P3 (Digital Cinema)</p>
<dt><code>v-gamut</code></p>
<dd>Panasonic V-Gamut primaries</p>
<dt><code>&lt;gamma&gt;</code></p>
<dd>Gamma function the source file was encoded with. Normally this should be set in the file header, but when playing broken or mistagged files this can be used to override the setting. </p>
<p> This option only affects video output drivers that perform color management. </p>
<p> If this option is set to <code>auto</code> (which is the default), the gamma will be set to BT.1886 for YCbCr content, sRGB for RGB content and Linear for XYZ content. </p>
<p> Available gamma functions are:</p>
<dt><code>auto</code></p>
<dd>automatic selection (default)</p>
<dt><code>bt.1886</code></p>
<dd>ITU-R BT.1886 (EOTF corresponding to BT.601/BT.709/BT.2020)</p>
<dt><code>srgb</code></p>
<dd>IEC 61966-2-4 (sRGB)</p>
<dt><code>linear</code></p>
<dd>Linear light</p>
<dt><code>gamma1.8</code></p>
<dd>Pure power curve (gamma 1.8)</p>
<dt><code>gamma2.0</code></p>
<dd>Pure power curve (gamma 2.0)</p>
<dt><code>gamma2.2</code></p>
<dd>Pure power curve (gamma 2.2)</p>
<dt><code>gamma2.4</code></p>
<dd>Pure power curve (gamma 2.4)</p>
<dt><code>gamma2.6</code></p>
<dd>Pure power curve (gamma 2.6)</p>
<dt><code>gamma2.8</code></p>
<dd>Pure power curve (gamma 2.8)</p>
<dt><code>prophoto</code></p>
<dd>ProPhoto RGB (ROMM) curve</p>
<dt><code>pq</code></p>
<dd>ITU-R BT.2100 PQ (Perceptual quantizer) curve</p>
<dt><code>hlg</code></p>
<dd>ITU-R BT.2100 HLG (Hybrid Log-gamma) curve</p>
<dt><code>v-log</code></p>
<dd>Panasonic V-Log transfer curve</p>
<dt><code>s-log1</code></p>
<dd>Sony S-Log1 transfer curve</p>
<dt><code>s-log2</code></p>
<dd>Sony S-Log2 transfer curve</p>
<dt><code>&lt;sig-peak&gt;</code></p>
<dd>Reference peak illumination for the video file, relative to the signal&#8217;s reference white level. This is mostly interesting for HDR, but it can also be used tone map SDR content to simulate a different exposure. Normally inferred from tags such as MaxCLL or mastering metadata. </p>
<p> The default of 0.0 will default to the source&#8217;s nominal peak luminance.</p>
<dt><code>&lt;light&gt;</code></p>
<dd>Light type of the scene. This is mostly correctly inferred based on the gamma function, but it can be useful to override this when viewing raw camera footage (e.g. V-Log), which is normally scene-referred instead of display-referred. </p>
<p> Available light types are:</p>
<dt><code>auto</code></p>
<dd>Automatic selection (default)</p>
<dt><code>display</code></p>
<dd>Display-referred light (most content)</p>
<dt><code>hlg</code></p>
<dd>Scene-referred using the HLG OOTF (e.g. HLG content)</p>
<dt><code>709-1886</code></p>
<dd>Scene-referred using the BT709+BT1886 interaction</p>
<dt><code>gamma1.2</code></p>
<dd>Scene-referred using a pure power OOTF (gamma=1.2)</p>
<dt><code>&lt;stereo-in&gt;</code></p>
<dd>Set the stereo mode the video is assumed to be encoded in. Use <code>&#8211;vf=format:stereo-in=help</code> to list all available modes. Check with the <code>stereo3d</code> filter documentation to see what the names mean.</p>
<dt><code>&lt;stereo-out&gt;</code></p>
<dd>Set the stereo mode the video should be displayed as. Takes the same values as the <code>stereo-in</code> option.</p>
<dt><code>&lt;rotate&gt;</code></p>
<dd>Set the rotation the video is assumed to be encoded with in degrees. The special value <code>-1</code> uses the input format.</p>
<dt><code>&lt;w&gt;</code>, <code>&lt;h&gt;</code></p>
<dd>If not 0, perform conversion to the given size. Ignored if <code>convert=yes</code> is not set.</p>
<dt><code>&lt;dw&gt;</code>, <code>&lt;dh&gt;</code></p>
<dd>Set the display size. Note that setting the display size such that the video is scaled in both directions instead of just changing the aspect ratio is an implementation detail, and might change later.</p>
<dt><code>&lt;dar&gt;</code></p>
<dd>Set the display aspect ratio of the video frame. This is a float, but values such as <code>[16:9]</code> can be passed too (<code>[&#8230;]</code> for quoting to prevent the option parser from interpreting the <code>:</code> character).</p>
<dt><code>&lt;force-scaler=auto|zimg|sws&gt;</code></p>
<dd>Force a specific scaler backend, if applicable. This is a debug option and could go away any time.</p>
<dt><code>&lt;alpha=auto|straight|premul&gt;</code></p>
<dd>Set the kind of alpha the video uses. Undefined effect if the image format has no alpha channel (could be ignored or cause an error, depending on how mpv internals evolve). Setting this may or may not cause downstream image processing to treat alpha differently, depending on support. With <code>convert</code> and zimg used, this will convert the alpha. libswscale and other FFmpeg components completely ignore this.</p>
<dt><code>lavfi=graph[:sws-flags[:o=opts]]</code></p>
<dd>Filter video using FFmpeg&#8217;s libavfilter.</p>
<dt><code>&lt;graph&gt;</code></p>
<dd>The libavfilter graph string. The filter must have a single video input pad and a single video output pad. </p>
<p> See <i><a rel="nofollow" href="https://ffmpeg.org/ffmpeg-filters.html">https://ffmpeg.org/ffmpeg-filters.html</a></i> for syntax and available filters. </p>
<p> <code>WARNING:</code> If you want to use the full filter syntax with this option, you have to quote the filter graph in order to prevent mpv&#8217;s syntax and the filter graph syntax from clashing. To prevent a quoting and escaping mess, consider using <code>&#8211;lavfi-complex</code> if you know which video track you want to use from the input file. (There is only one video track for nearly all video files anyway.)</p>
<dt>Examples</p>
<dd>
<dt><code>&#8211;vf=lavfi=[gradfun=20:30,vflip]</code></p>
<dd><code>gradfun</code> filter with nonsense parameters, followed by a <code>vflip</code> filter. (This demonstrates how libavfilter takes a graph and not just a single filter.) The filter graph string is quoted with <code>[</code> and <code>]</code>. This requires no additional quoting or escaping with some shells (like bash), while others (like zsh) require additional <code>&quot;</code> quotes around the option string.</p>
<dt><code>&#8216;&#8211;vf=lavfi=gradfun=20:30,vflip&#8217;</code></p>
<dd>Same as before, but uses quoting that should be safe with all shells. The outer <code>&#8216;</code> quotes make sure that the shell does not remove the <code>&quot;</code> quotes needed by mpv.</p>
<dt><code>&#8216;&#8211;vf=lavfi=graph=gradfun=radius=30:strength=20,vflip&#8217;</code></p>
<dd>Same as before, but uses named parameters for everything.</p>
<dt><code>&lt;sws-flags&gt;</code></p>
<dd>If libavfilter inserts filters for pixel format conversion, this option gives the flags which should be passed to libswscale. This option is numeric and takes a bit-wise combination of <code>SWS_</code> flags. </p>
<p> See <code><a rel="nofollow" href="https://git.videolan.org/?p=ffmpeg.git;a=blob;f=libswscale/swscale.h">https://git.videolan.org/?p=ffmpeg.git;a=blob;f=libswscale/swscale.h</a></code>.</p>
<dt><code>&lt;o&gt;</code></p>
<dd>Set AVFilterGraph options. These should be documented by FFmpeg.</p>
<dt>Example</p>
<dd>
<dt><code>&#8216;&#8211;vf=lavfi=yadif:o=threads=2,thread_type=slice&#8217;</code></p>
<dd>forces a specific threading configuration.</p>
<dt><code>sub=[=bottom-margin:top-margin]</code></p>
<dd>Moves subtitle rendering to an arbitrary point in the filter chain, or force subtitle rendering in the video filter as opposed to using video output OSD support.</p>
<dt><code>&lt;bottom-margin&gt;</code></p>
<dd>Adds a black band at the bottom of the frame. The SSA/ASS renderer can place subtitles there (with <code>&#8211;sub-use-margins</code>).</p>
<dt><code>&lt;top-margin&gt;</code></p>
<dd>Black band on the top for toptitles (with <code>&#8211;sub-use-margins</code>).</p>
<dt>Examples</p>
<dd>
<dt><code>&#8211;vf=sub,eq</code></p>
<dd>Moves sub rendering before the eq filter. This will put both subtitle colors and video under the influence of the video equalizer settings.</p>
<dt><code>vapoursynth=file:buffered-frames:concurrent-frames</code></p>
<dd>Loads a VapourSynth filter script. This is intended for streamed processing: mpv actually provides a source filter, instead of using a native VapourSynth video source. The mpv source will answer frame requests only within a small window of frames (the size of this window is controlled with the <code>buffered-frames</code> parameter), and requests outside of that will return errors. As such, you can&#8217;t use the full power of VapourSynth, but you can use certain filters. </p>
<p> <code>WARNING:</code> Do not use this filter, unless you have expert knowledge in VapourSynth, and know how to fix bugs in the mpv VapourSynth wrapper code. </p>
<p> If you just want to play video generated by VapourSynth (i.e. using a native VapourSynth video source), it&#8217;s better to use <code>vspipe</code> and a pipe or FIFO to feed the video to mpv. The same applies if the filter script requires random frame access (see <code>buffered-frames</code> parameter).</p>
<dt><code>file</code></p>
<dd>Filename of the script source. Currently, this is always a python script (<code>.vpy</code> in VapourSynth convention). </p>
<p> The variable <code>video_in</code> is set to the mpv video source, and it is expected that the script reads video from it. (Otherwise, mpv will decode no video, and the video packet queue will overflow, eventually leading to only audio playing, or worse.) </p>
<p> The filter graph created by the script is also expected to pass through timestamps using the <code>_DurationNum</code> and <code>_DurationDen</code> frame properties. </p>
<p> See the end of the option list for a full list of script variables defined by mpv.</p>
<dt>Example:</p>
<dd>
<pre>import vapoursynth as vs
core = vs.get_core()
core.std.AddBorders(video_in, 10, 10, 20, 20).set_output()</pre>
<p><code>WARNING:</code> The script will be reloaded on every seek. This is done to reset the filter properly on discontinuities.</p>
<dt><code>buffered-frames</code></p>
<dd>Maximum number of decoded video frames that should be buffered before the filter (default: 4). This specifies the maximum number of frames the script can request in backward direction. </p>
<p> E.g. if <code>buffered-frames=5</code>, and the script just requested frame 15, it can still request frame 10, but frame 9 is not available anymore. If it requests frame 30, mpv will decode 15 more frames, and keep only frames 25-30. </p>
<p> The only reason why this buffer exists is to serve the random access requests the VapourSynth filter can make. </p>
<p> The VapourSynth API has a <code>getFrameAsync</code> function, which takes an absolute frame number. Source filters must respond to all requests. For example, a source filter can request frame 2432, and then frame 3. Source filters typically implement this by pre-indexing the entire file. </p>
<p> mpv on the other hand is stream oriented, and does not allow filters to seek. (And it would not make sense to allow it, because it would ruin performance.) Filters get frames sequentially in playback direction, and cannot request them out of order. </p>
<p> To compensate for this mismatch, mpv allows the filter to access frames within a certain window. <code>buffered-frames</code> controls the size of this window. Most VapourSynth filters happen to work with this, because mpv requests frames sequentially increasing from it, and most filters only require frames &quot;close&quot; to the requested frame. </p>
<p> If the filter requests a frame that has a higher frame number than the highest buffered frame, new frames will be decoded until the requested frame number is reached. Excessive frames will be flushed out in a FIFO manner (there are only at most <code>buffered-frames</code> in this buffer). </p>
<p> If the filter requests a frame that has a lower frame number than the lowest buffered frame, the request cannot be satisfied, and an error is returned to the filter. This kind of error is not supposed to happen in a &quot;proper&quot; VapourSynth environment. What exactly happens depends on the filters involved. </p>
<p> Increasing this buffer will not improve performance. Rather, it will waste memory, and slow down seeks (when enough frames to fill the buffer need to be decoded at once). It is only needed to prevent the error described in the previous paragraph. </p>
<p> How many frames a filter requires depends on filter implementation details, and mpv has no way of knowing. A scale filter might need only 1 frame, an interpolation filter may require a small number of frames, and the <code>Reverse</code> filter will require an infinite number of frames. </p>
<p> If you want reliable operation to the full extend VapourSynth is capable, use <code>vspipe</code>. </p>
<p> The actual number of buffered frames also depends on the value of the <code>concurrent-frames</code> option. Currently, both option values are multiplied to get the final buffer size.</p>
<dt><code>concurrent-frames</code></p>
<dd>Number of frames that should be requested in parallel. The level of concurrency depends on the filter and how quickly mpv can decode video to feed the filter. This value should probably be proportional to the number of cores on your machine. Most time, making it higher than the number of cores can actually make it slower. </p>
<p> Technically, mpv will call the VapourSynth <code>getFrameAsync</code> function in a loop, until there are <code>concurrent-frames</code> frames that have not been returned by the filter yet. This also assumes that the rest of the mpv filter chain reads the output of the <code>vapoursynth</code> filter quickly enough. (For example, if you pause the player, filtering will stop very soon, because the filtered frames are waiting in a queue.) </p>
<p> Actual concurrency depends on many other factors. </p>
<p> By default, this uses the special value <code>auto</code>, which sets the option to the number of detected logical CPU cores. </p>
<p> The following <code>.vpy</code> script variables are defined by mpv:</p>
<dt><code>video_in</code></p>
<dd>The mpv video source as vapoursynth clip. Note that this has an incorrect (very high) length set, which confuses many filters. This is necessary, because the true number of frames is unknown. You can use the <code>Trim</code> filter on the clip to reduce the length.</p>
<dt><code>video_in_dw</code>, <code>video_in_dh</code></p>
<dd>Display size of the video. Can be different from video size if the video does not use square pixels (e.g. DVD).</p>
<dt><code>container_fps</code></p>
<dd>FPS value as reported by file headers. This value can be wrong or completely broken (e.g. 0 or NaN). Even if the value is correct, if another filter changes the real FPS (by dropping or inserting frames), the value of this variable will not be useful. Note that the <code>&#8211;fps</code> command line option overrides this value. </p>
<p> Useful for some filters which insist on having a FPS.</p>
<dt><code>display_fps</code></p>
<dd>Refresh rate of the current display. Note that this value can be 0.</p>
<dt><code>vavpp</code></p>
<dd>VA-API video post processing. Requires the system to support VA-API, i.e. Linux/BSD only. Works with <code>&#8211;vo=vaapi</code> and <code>&#8211;vo=gpu</code> only. Currently deinterlaces. This filter is automatically inserted if deinterlacing is requested (either using the <code>d</code> key, by default mapped to the command <code>cycle deinterlace</code>, or the <code>&#8211;deinterlace</code> option).</p>
<dt><code>deint=&lt;method&gt;</code></p>
<dd>Select the deinterlacing algorithm.</p>
<dt><code>no</code></p>
<dd>Don&#8217;t perform deinterlacing.</p>
<dt><code>auto</code></p>
<dd>Select the best quality deinterlacing algorithm (default). This goes by the order of the options as documented, with <code>motion-compensated</code> being considered best quality.</p>
<dt><code>first-field</code></p>
<dd>Show only first field.</p>
<dt><code>bob</code></p>
<dd>bob deinterlacing.</p>
<dt><code>weave, motion-adaptive, motion-compensated</code></p>
<dd>Advanced deinterlacing algorithms. Whether these actually work depends on the GPU hardware, the GPU drivers, driver bugs, and mpv bugs.</p>
<dt><code>&lt;interlaced-only&gt;</code></p>
<dd>
<dt><code>no</code></p>
<dd>Deinterlace all frames (default).</p>
<dt><code>yes</code></p>
<dd>Only deinterlace frames marked as interlaced.</p>
<dt><code>reversal-bug=&lt;yes|no&gt;</code></p>
<dd>
<dt><code>no</code></p>
<dd>Use the API as it was interpreted by older Mesa drivers. While this interpretation was more obvious and intuitive, it was apparently wrong, and not shared by Intel driver developers.</p>
<dt><code>yes</code></p>
<dd>Use Intel interpretation of surface forward and backwards references (default). This is what Intel drivers and newer Mesa drivers expect. Matters only for the advanced deinterlacing algorithms.</p>
<dt><code>vdpaupp</code></p>
<dd>VDPAU video post processing. Works with <code>&#8211;vo=vdpau</code> and <code>&#8211;vo=gpu</code> only. This filter is automatically inserted if deinterlacing is requested (either using the <code>d</code> key, by default mapped to the command <code>cycle deinterlace</code>, or the <code>&#8211;deinterlace</code> option). When enabling deinterlacing, it is always preferred over software deinterlacer filters if the <code>vdpau</code> VO is used, and also if <code>gpu</code> is used and hardware decoding was activated at least once (i.e. vdpau was loaded).</p>
<dt><code>sharpen=&lt;-1-1&gt;</code></p>
<dd>For positive values, apply a sharpening algorithm to the video, for negative values a blurring algorithm (default: 0).</p>
<dt><code>denoise=&lt;0-1&gt;</code></p>
<dd>Apply a noise reduction algorithm to the video (default: 0; no noise reduction).</p>
<dt><code>deint=&lt;yes|no&gt;</code></p>
<dd>Whether deinterlacing is enabled (default: no). If enabled, it will use the mode selected with <code>deint-mode</code>.</p>
<dt><code>deint-mode=&lt;first-field|bob|temporal|temporal-spatial&gt;</code></p>
<dd>Select deinterlacing mode (default: temporal). </p>
<p> Note that there&#8217;s currently a mechanism that allows the <code>vdpau</code> VO to change the <code>deint-mode</code> of auto-inserted <code>vdpaupp</code> filters. To avoid confusion, it&#8217;s recommended not to use the <code>&#8211;vo=vdpau</code> suboptions related to filtering.</p>
<dt><code>first-field</code></p>
<dd>Show only first field.</p>
<dt><code>bob</code></p>
<dd>Bob deinterlacing.</p>
<dt><code>temporal</code></p>
<dd>Motion-adaptive temporal deinterlacing. May lead to A/V desync with slow video hardware and/or high resolution.</p>
<dt><code>temporal-spatial</code></p>
<dd>Motion-adaptive temporal deinterlacing with edge-guided spatial interpolation. Needs fast video hardware.</p>
<dt><code>chroma-deint</code></p>
<dd>Makes temporal deinterlacers operate both on luma and chroma (default). Use no-chroma-deint to solely use luma and speed up advanced deinterlacing. Useful with slow video memory.</p>
<dt><code>pullup</code></p>
<dd>Try to apply inverse telecine, needs motion adaptive temporal deinterlacing.</p>
<dt><code>interlaced-only=&lt;yes|no&gt;</code></p>
<dd>If <code>yes</code>, only deinterlace frames marked as interlaced (default: no).</p>
<dt><code>hqscaling=&lt;0-9&gt;</code></p>
<dd>
<dt><code>0</code></p>
<dd>Use default VDPAU scaling (default).</p>
<dt><code>1-9</code></p>
<dd>Apply high quality VDPAU scaling (needs capable hardware).</p>
<dt><code>d3d11vpp</code></p>
<dd>Direct3D 11 video post processing. Currently requires D3D11 hardware decoding for use.</p>
<dt><code>deint=&lt;yes|no&gt;</code></p>
<dd>Whether deinterlacing is enabled (default: no).</p>
<dt><code>interlaced-only=&lt;yes|no&gt;</code></p>
<dd>If <code>yes</code>, only deinterlace frames marked as interlaced (default: no).</p>
<dt><code>mode=&lt;blend|bob|adaptive|mocomp|ivctc|none&gt;</code></p>
<dd>Tries to select a video processor with the given processing capability. If a video processor supports multiple capabilities, it is not clear which algorithm is actually selected. <code>none</code> always falls back. On most if not all hardware, this option will probably do nothing, because a video processor usually supports all modes or none.</p>
<dt><code>fingerprint=&#8230;</code></p>
<dd>Compute video frame fingerprints and provide them as metadata. Actually, it currently barely deserved to be called <code>fingerprint</code>, because it does not compute &quot;proper&quot; fingerprints, only tiny downscaled images (but which can be used to compute image hashes or for similarity matching). </p>
<p> The main purpose of this filter is to support the <code>skip-logo.lua</code> script. If this script is dropped, or mpv ever gains a way to load user-defined filters (other than VapourSynth), this filter will be removed. Due to the &quot;special&quot; nature of this filter, it will be removed without warning. </p>
<p> The intended way to read from the filter is using <code>vf-metadata</code> (also see <code>clear-on-query</code> filter parameter). The property will return a list of key/value pairs as follows: </p>
<pre>fp0.pts = 1.2345
fp0.hex = 1234abcdef...bcde
fp1.pts = 1.4567
fp1.hex = abcdef1234...6789
...
fpN.pts = ...
fpN.hex = ...
type = gray-hex-16x16</pre>
<p>Each <code>fp&lt;N&gt;</code> entry is for a frame. The <code>pts</code> entry specifies the timestamp of the frame (within the filter chain; in simple cases this is the same as the display timestamp). The <code>hex</code> field is the hex encoded fingerprint, whose size and meaning depend on the <code>type</code> filter option. The <code>type</code> field has the same value as the option the filter was created with. </p>
<p> This returns the frames that were filtered since the last query of the property. If <code>clear-on-query=no</code> was set, a query doesn&#8217;t reset the list of frames. In both cases, a maximum of 10 frames is returned. If there are more frames, the oldest frames are discarded. Frames are returned in filter order. </p>
<p> (This doesn&#8217;t return a structured list for the per-frame details because the internals of the <code>vf-metadata</code> mechanism suck. The returned format may change in the future.) </p>
<p> This filter uses zimg for speed and profit. However, it will fallback to libswscale in a number of situations: lesser pixel formats, unaligned data pointers or strides, or if zimg fails to initialize for unknown reasons. In these cases, the filter will use more CPU. Also, it will output different fingerprints, because libswscale cannot perform the full range expansion we normally request from zimg. As a consequence, the filter may be slower and not work correctly in random situations.</p>
<dt><code>type=&#8230;</code></p>
<dd>What fingerprint to compute. Available types are:</p>
<dt><code>gray-hex-8&#215;8</code></p>
<dd>grayscale, 8 bit, 8&#215;8 size</p>
<dt><code>gray-hex-16&#215;16</code></p>
<dd>grayscale, 8 bit, 16&#215;16 size (default) </p>
<p> Both types simply remove all colors, downscale the image, concatenate all pixel values to a byte array, and convert the array to a hex string.</p>
<dt><code>clear-on-query=yes|no</code></p>
<dd>Clear the list of frame fingerprints if the <code>vf-metadata</code> property for this filter is queried (default: yes). This requires some care by the user. Some types of accesses might query the filter multiple times, which leads to lost frames.</p>
<dt><code>print=yes|no</code></p>
<dd>Print computed fingerprints to the terminal (default: no). This is mostly for testing and such. Scripts should use <code>vf-metadata</code> to read information from this filter instead.</p>
<dt><code>gpu=&#8230;</code></p>
<dd>Convert video to RGB using the OpenGL renderer normally used with <code>&#8211;vo=gpu</code>. This requires that the EGL implementation supports off-screen rendering on the default display. (This is the case with Mesa.) </p>
<p> Sub-options:</p>
<dt><code>w=&lt;pixels&gt;</code>, <code>h=&lt;pixels&gt;</code></p>
<dd>Size of the output in pixels (default: 0). If not positive, this will use the size of the first filtered input frame. </p>
<p> <code>WARNING:</code> This is highly experimental. Performance is bad, and it will not work everywhere in the first place. Some features are not supported. </p>
<p> <code>WARNING:</code> This does not do OSD rendering. If you see OSD, then it has been rendered by the VO backend. (Subtitles are rendered by the <code>gpu</code> filter, if possible.) </p>
<p> <code>WARNING:</code> If you use this with encoding mode, keep in mind that encoding mode will convert the RGB filter&#8217;s output back to yuv420p in software, using the configured software scaler. Using <code>zimg</code> might improve this, but in any case it might go against your goals when using this filter. </p>
<p> <code>WARNING:</code> Do not use this with <code>&#8211;vo=gpu</code>. It will apply filtering twice, since most <code>&#8211;vo=gpu</code> options are unconditionally applied to the <code>gpu</code> filter. There is no mechanism in mpv to prevent this.</dl>
<h2>Encoding</h2>
<p>You can encode files from one format/codec to another using this facility.</p>
<dl COMPACT>
<dt><code>&#8211;o=&lt;filename&gt;</code></p>
<dd>Enables encoding mode and specifies the output file name.</p>
<dt><code>&#8211;of=&lt;format&gt;</code></p>
<dd>Specifies the output format (overrides autodetection by the file name extension of the file specified by <code>-o</code>). See <code>&#8211;of=help</code> for a full list of supported formats.</p>
<dt><code>&#8211;ofopts=&lt;options&gt;</code></p>
<dd>Specifies the output format options for libavformat. See <code>&#8211;ofopts=help</code> for a full list of supported options. </p>
<p> This is a key/value list option. See <i>List Options</i> for details.</p>
<dt><code>&#8211;ofopts-add=&lt;option&gt;</code></p>
<dd>Appends the option given as an argument to the options list. (Passing multiple options is currently still possible, but deprecated.)</p>
<dt><code>&#8211;ofopts=</code></p>
<dd>Completely empties the options list.</p>
<dt><code>&#8211;oac=&lt;codec&gt;</code></p>
<dd>Specifies the output audio codec. See <code>&#8211;oac=help</code> for a full list of supported codecs.</p>
<dt><code>&#8211;oaoffset=&lt;value&gt;</code></p>
<dd>Shifts audio data by the given time (in seconds) by adding/removing samples at the start. Deprecated.</p>
<dt><code>&#8211;oacopts=&lt;options&gt;</code></p>
<dd>Specifies the output audio codec options for libavcodec. See <code>&#8211;oacopts=help</code> for a full list of supported options.</p>
<dt>Example</p>
<dd>
<dt><code>&#8211;oac=libmp3lame &#8211;oacopts=b=128000</code></p>
<dd>selects 128 kbps MP3 encoding. </p>
<p> This is a key/value list option. See <i>List Options</i> for details.</p>
<dt><code>&#8211;oacopts-add=&lt;option&gt;</code></p>
<dd>Appends the option given as an argument to the options list. (Passing multiple options is currently still possible, but deprecated.)</p>
<dt><code>&#8211;oacopts=</code></p>
<dd>Completely empties the options list.</p>
<dt><code>&#8211;oafirst</code></p>
<dd>Force the audio stream to become the first stream in the output. By default, the order is unspecified. Deprecated.</p>
<dt><code>&#8211;ovc=&lt;codec&gt;</code></p>
<dd>Specifies the output video codec. See <code>&#8211;ovc=help</code> for a full list of supported codecs.</p>
<dt><code>&#8211;ovoffset=&lt;value&gt;</code></p>
<dd>Shifts video data by the given time (in seconds) by shifting the pts values. Deprecated.</p>
<dt><code>&#8211;ovcopts=&lt;options&gt;</code></p>
<dd>Specifies the output video codec options for libavcodec. See &#8211;ovcopts=help for a full list of supported options.</p>
<dt>Examples</p>
<dd>
<dt><code>&#8211;ovc=mpeg4 &#8211;ovcopts=qscale=5</code></p>
<dd>selects constant quantizer scale 5 for MPEG-4 encoding.</p>
<dt><code>&#8211;ovc=libx264 &#8211;ovcopts=crf=23</code></p>
<dd>selects VBR quality factor 23 for H.264 encoding. </p>
<p> This is a key/value list option. See <i>List Options</i> for details.</p>
<dt><code>&#8211;ovcopts-add=&lt;option&gt;</code></p>
<dd>Appends the option given as an argument to the options list. (Passing multiple options is currently still possible, but deprecated.)</p>
<dt><code>&#8211;ovcopts=</code></p>
<dd>Completely empties the options list.</p>
<dt><code>&#8211;ovfirst</code></p>
<dd>Force the video stream to become the first stream in the output. By default, the order is unspecified. Deprecated.</p>
<dt><code>&#8211;orawts</code></p>
<dd>Copies input pts to the output video (not supported by some output container formats, e.g. AVI). In this mode, discontinuities are not fixed and all pts are passed through as-is. Never seek backwards or use multiple input files in this mode!</p>
<dt><code>&#8211;no-ocopy-metadata</code></p>
<dd>Turns off copying of metadata from input files to output files when encoding (which is enabled by default).</p>
<dt><code>&#8211;oset-metadata=&lt;metadata-tag[,metadata-tag,&#8230;]&gt;</code></p>
<dd>Specifies metadata to include in the output file. Supported keys vary between output formats. For example, Matroska (MKV) and FLAC allow almost arbitrary keys, while support in MP4 and MP3 is more limited. </p>
<p> This is a key/value list option. See <i>List Options</i> for details.</p>
<dt>Example</p>
<dd>
<dt><code>&#8211;oset-metadata=title=Output title,comment=Another tag</code></p>
<dd>adds a title and a comment to the output file.</p>
<dt><code>&#8211;oremove-metadata=&lt;metadata-tag[,metadata-tag,&#8230;]&gt;</code></p>
<dd>Specifies metadata to exclude from the output file when copying from the input file. </p>
<p> This is a string list option. See <i>List Options</i> for details.</p>
<dt>Example</p>
<dd>
<dt><code>&#8211;oremove-metadata=comment,genre</code></p>
<dd>excludes copying of the the comment and genre tags to the output file.</dl>
<h2>Command Interface</h2>
<p>The mpv core can be controlled with commands and properties. A number of ways to interact with the player use them: key bindings (<code>input.conf</code>), OSD (showing information with properties), JSON IPC, the client API (<code>libmpv</code>), and the classic slave mode.</p>
<h3>input.conf</h3>
<p>The input.conf file consists of a list of key bindings, for example: </p>
<pre>s screenshot # take a screenshot with the s key
LEFT seek 15 # map the left-arrow key to seeking forward by 15 seconds</pre>
<p>Each line maps a key to an input command. Keys are specified with their literal value (upper case if combined with <code>Shift</code>), or a name for special keys. For example, <code>a</code> maps to the <code>a</code> key without shift, and <code>A</code> maps to <code>a</code> with shift. </p>
<p> The file is located in the mpv configuration directory (normally at <code>~/.config/mpv/input.conf</code> depending on platform). The default bindings are defined here: </p>
<pre><a rel="nofollow" href="https://github.com/mpv-player/mpv/blob/master/etc/input.conf">https://github.com/mpv-player/mpv/blob/master/etc/input.conf</a></pre>
<p>A list of special keys can be obtained with <code>mpv &#8211;input-keylist</code> </p>
<p> In general, keys can be combined with <code>Shift</code>, <code>Ctrl</code> and <code>Alt</code>: </p>
<pre>ctrl+q quit</pre>
<p><code>mpv</code> can be started in input test mode, which displays key bindings and the commands they&#8217;re bound to on the OSD, instead of executing the commands: </p>
<pre>mpv --input-test --force-window --idle</pre>
<p>(Only closing the window will make <code>mpv</code> exit, pressing normal keys will merely display the binding, even if mapped to quit.) </p>
<p> Also see <i>Key names</i>.</p>
<h3>input.conf syntax</h3>
<p><code>[Shift+][Ctrl+][Alt+][Meta+]&lt;key&gt; [{&lt;section&gt;}] &lt;command&gt; ( ; &lt;command&gt; )*</code> </p>
<p> Note that by default, the right Alt key can be used to create special characters, and thus does not register as a modifier. The option <code>&#8211;no-input-right-alt-gr</code> changes this behavior. </p>
<p> Newlines always start a new binding. <code>#</code> starts a comment (outside of quoted string arguments). To bind commands to the <code>#</code> key, <code>SHARP</code> can be used. </p>
<p> <code>&lt;key&gt;</code> is either the literal character the key produces (ASCII or Unicode character), or a symbolic name (as printed by <code>&#8211;input-keylist</code>). </p>
<p> <code>&lt;section&gt;</code> (braced with <code>{</code> and <code>}</code>) is the input section for this command. </p>
<p> <code>&lt;command&gt;</code> is the command itself. It consists of the command name and multiple (or none) arguments, all separated by whitespace. String arguments should be quoted, typically with <code>&quot;</code>. See <code>Flat command syntax</code>. </p>
<p> You can bind multiple commands to one key. For example: </p>
<pre>a show-text &quot;command 1&quot; ; show-text &quot;command 2&quot;</pre>
<p>It&#8217;s also possible to bind a command to a sequence of keys: </p>
<pre>a-b-c show-text &quot;command run after a, b, c have been pressed&quot;</pre>
<p>(This is not shown in the general command syntax.) </p>
<p> If <code>a</code> or <code>a-b</code> or <code>b</code> are already bound, this will run the first command that matches, and the multi-key command will never be called. Intermediate keys can be remapped to <code>ignore</code> in order to avoid this issue. The maximum number of (non-modifier) keys for combinations is currently 4.</p>
<h3>Key names</h3>
<p>All mouse and keyboard input is to converted to mpv-specific key names. Key names are either special symbolic identifiers representing a physical key, or a text key names, which are unicode code points encoded as UTF-8. These are what keyboard input would normally produce, for example <code>a</code> for the A key. As a consequence, mpv uses input translated by the current OS keyboard layout, rather than physical scan codes. </p>
<p> Currently there is the hardcoded assumption that every text key can be represented as a single unicode code point (in NFKC form). </p>
<p> All key names can be combined with the modifiers <code>Shift</code>, <code>Ctrl</code>, <code>Alt</code>, <code>Meta</code>. They must be prefixed to the actual key name, where each modifier is followed by a <code>+</code> (for example <code>ctrl+q</code>). </p>
<p> The <code>Shift</code> modifier requires some attention. For instance <code>Shift+2</code> should usually be specified as key-name <code>@</code> at <code>input.conf</code>, and similarly the combination <code>Alt+Shift+2</code> is usually <code>Alt+@</code>, etc. Special key names like <code>Shift+LEFT</code> work as expected. If in doubt &#8211; use <code>&#8211;input-test</code> to check how a key/combination is seen by mpv. </p>
<p> Symbolic key names and modifier names are case-insensitive. Unicode key names are case-sensitive because input bindings typically respect the shift key. </p>
<p> Another type of key names are hexadecimal key names, that serve as fallback for special keys that are neither unicode, nor have a special mpv defined name. They will break as soon as mpv adds proper names for them, but can enable you to use a key at all if that does not happen. </p>
<p> All symbolic names are listed by <code>&#8211;input-keylist</code>. <code>&#8211;input-test</code> is a special mode that prints all input on the OSD. </p>
<p> Comments on some symbolic names:</p>
<dl COMPACT>
<dt><code>KP*</code></p>
<dd>Keypad names. Behavior varies by backend (whether they implement this, and on how they treat numlock), but typically, mpv tries to map keys on the keypad to separate names, even if they produce the same text as normal keys.</p>
<dt><code>MOUSE_BTN*</code>, <code>MBTN*</code></p>
<dd>Various mouse buttons. </p>
<p> Depending on backend, the mouse wheel might also be represented as a button. In addition, <code>MOUSE_BTN3</code> to <code>MOUSE_BTN6</code> are deprecated aliases for <code>WHEEL_UP</code>, <code>WHEEL_DOWN</code>, <code>WHEEL_LEFT</code>, <code>WHEEL_RIGHT</code>. </p>
<p> <code>MBTN*</code> are aliases for <code>MOUSE_BTN*</code>.</p>
<dt><code>WHEEL_*</code></p>
<dd>Mouse wheels (typically).</p>
<dt><code>AXIS_*</code></p>
<dd>Deprecated aliases for <code>WHEEL_*</code>.</p>
<dt><code>*_DBL</code></p>
<dd>Mouse button double clicks.</p>
<dt><code>MOUSE_MOVE</code>, <code>MOUSE_ENTER</code>, <code>MOUSE_LEAVE</code></p>
<dd>Emitted by mouse move events. Enter/leave happens when the mouse enters or leave the mpv window (or the current mouse region, using the deprecated mouse region input section mechanism).</p>
<dt><code>CLOSE_WIN</code></p>
<dd>Pseudo key emitted when closing the mpv window using the OS window manager (for example, by clicking the close button in the window title bar).</p>
<dt><code>GAMEPAD_*</code></p>
<dd>Keys emitted by the SDL gamepad backend.</p>
<dt><code>UNMAPPED</code></p>
<dd>Pseudo-key that matches any unmapped key. (You should probably avoid this if possible, because it might change behavior or get removed in the future.)</p>
<dt><code>ANY_UNICODE</code></p>
<dd>Pseudo-key that matches any key that produces text. (You should probably avoid this if possible, because it might change behavior or get removed in the future.)</dl>
<h3>Flat command syntax</h3>
<p>This is the syntax used in input.conf, and referred to &quot;input.conf syntax&quot; in a number of other places. </p>
<pre><code>&lt;command&gt; ::= [&lt;prefixes&gt;] &lt;command_name&gt; (&lt;argument&gt;)*</code>
<code>&lt;argument&gt; ::= (&lt;unquoted&gt; | &quot; &lt;double_quoted&gt; &quot; | ' &lt;single_quoted&gt; ' | `X &lt;custom_quoted&gt; X`)</code></pre>
<p><code>command_name</code> is an unquoted string with the command name itself. See <i>List of Input Commands</i> for a list. </p>
<p> Arguments are separated by whitespaces even if the command expects only one argument. Arguments with whitespaces or other special characters must be quoted, or the command cannot be parsed correctly. </p>
<p> Double quotes interpret JSON/C-style escaping, like <code>	</code> or <code>\&quot;</code> or <code>\</code>. JSON escapes according to RFC 8259, minus surrogate pair escapes. This is the only form which allows newlines at the value &#8211; as <code>
</code>. </p>
<p> Single quotes take the content literally, and cannot include the single-quote character at the value. </p>
<p> Custom quotes also take the content literally, but are more flexible than single quotes. They start with <code>`</code> (back-quote) followed by any ASCII character, and end at the first occurance of the same pair in reverse order, e.g. <code>`-foo-`</code> or <code>&#8220;bar&#8220;</code>. The final pair sequence is not allowed at the value &#8211; in these examples <code>-`</code> and <code>&#8220;</code> respectively. In the second example the last character of the value also can&#8217;t be a back-quote. </p>
<p> Mixed quoting at the same argument, like <code>&#8216;foo&#8217;&quot;bar&quot;</code>, is not supported. </p>
<p> Note that argument parsing and property expansion happen at different stages. First, arguments are determined as described above, and then, where applicable, properties are expanded &#8211; regardless of argument quoting. However, expansion can still be prevented with the <code>raw</code> prefix or <code>$&gt;</code>. See <i>Input Command Prefixes</i> and <i>Property Expansion</i>.</p>
<h3>Commands specified as arrays</h3>
<p>This applies to certain APIs, such as <code>mp.commandv()</code> or <code>mp.command_native()</code> (with array parameters) in Lua scripting, or <code>mpv_command()</code> or <code>mpv_command_node()</code> (with MPV_FORMAT_NODE_ARRAY) in the C libmpv client API. </p>
<p> The command as well as all arguments are passed as a single array. Similar to the <i>Flat command syntax</i>, you can first pass prefixes as strings (each as separate array item), then the command name as string, and then each argument as string or a native value. </p>
<p> Since these APIs pass arguments as separate strings or native values, they do not expect quotes, and do support escaping. Technically, there is the input.conf parser, which first splits the command string into arguments, and then invokes argument parsers for each argument. The input.conf parser normally handles quotes and escaping. The array command APIs mentioned above pass strings directly to the argument parsers, or can sidestep them by the ability to pass non-string values. </p>
<p> Property expansion is disabled by default for these APIs. This can be changed with the <code>expand-properties</code> prefix. See <i>Input Command Prefixes</i>. </p>
<p> Sometimes commands have string arguments, that in turn are actually parsed by other components (e.g. filter strings with <code>vf add</code>) &#8211; in these cases, you you would have to double-escape in input.conf, but not with the array APIs. </p>
<p> For complex commands, consider using <i>Named arguments</i> instead, which should give slightly more compatibility. Some commands do not support named arguments and inherently take an array, though.</p>
<h3>Named arguments</h3>
<p>This applies to certain APIs, such as <code>mp.command_native()</code> (with tables that have string keys) in Lua scripting, or <code>mpv_command_node()</code> (with MPV_FORMAT_NODE_MAP) in the C libmpv client API. </p>
<p> The name of the command is provided with a <code>name</code> string field. The name of each command is defined in each command description in the <i>List of Input Commands</i>. <code>&#8211;input-cmdlist</code> also lists them. See the <code>subprocess</code> command for an example. </p>
<p> Some commands do not support named arguments (e.g. <code>run</code> command). You need to use APIs that pass arguments as arrays. </p>
<p> Named arguments are not supported in the &quot;flat&quot; input.conf syntax, which means you cannot use them for key bindings in input.conf at all. </p>
<p> Property expansion is disabled by default for these APIs. This can be changed with the <code>expand-properties</code> prefix. See <i>Input Command Prefixes</i>.</p>
<h3>List of Input Commands</h3>
<p>Commands with parameters have the parameter name enclosed in <code>&lt;</code> / <code>&gt;</code>. Don&#8217;t add those to the actual command. Optional arguments are enclosed in <code>[</code> / <code>]</code>. If you don&#8217;t pass them, they will be set to a default value. </p>
<p> Remember to quote string arguments in input.conf (see <i>Flat command syntax</i>).</p>
<dl COMPACT>
<dt><code>ignore</code></p>
<dd>Use this to &quot;block&quot; keys that should be unbound, and do nothing. Useful for disabling default bindings, without disabling all bindings with <code>&#8211;no-input-default-bindings</code>.</p>
<dt><code>seek &lt;target&gt; [&lt;flags&gt;]</code></p>
<dd>Change the playback position. By default, seeks by a relative amount of seconds. </p>
<p> The second argument consists of flags controlling the seek mode:</p>
<dt><code>relative (default)</code></p>
<dd>Seek relative to current position (a negative value seeks backwards).</p>
<dt><code>absolute</code></p>
<dd>Seek to a given time (a negative value starts from the end of the file).</p>
<dt><code>absolute-percent</code></p>
<dd>Seek to a given percent position.</p>
<dt><code>relative-percent</code></p>
<dd>Seek relative to current position in percent.</p>
<dt><code>keyframes</code></p>
<dd>Always restart playback at keyframe boundaries (fast).</p>
<dt><code>exact</code></p>
<dd>Always do exact/hr/precise seeks (slow). </p>
<p> Multiple flags can be combined, e.g.: <code>absolute+keyframes</code>. </p>
<p> By default, <code>keyframes</code> is used for <code>relative</code>, <code>relative-percent</code>, and <code>absolute-percent</code> seeks, while <code>exact</code> is used for <code>absolute</code> seeks. </p>
<p> Before mpv 0.9, the <code>keyframes</code> and <code>exact</code> flags had to be passed as 3rd parameter (essentially using a space instead of <code>+</code>). The 3rd parameter is still parsed, but is considered deprecated.</p>
<dt><code>revert-seek [&lt;flags&gt;]</code></p>
<dd>Undoes the <code>seek</code> command, and some other commands that seek (but not necessarily all of them). Calling this command once will jump to the playback position before the seek. Calling it a second time undoes the <code>revert-seek</code> command itself. This only works within a single file. </p>
<p> The first argument is optional, and can change the behavior:</p>
<dt><code>mark</code></p>
<dd>Mark the current time position. The next normal <code>revert-seek</code> command will seek back to this point, no matter how many seeks happened since last time.</p>
<dt><code>mark-permanent</code></p>
<dd>If set, mark the current position, and do not change the mark position before the next <code>revert-seek</code> command that has <code>mark</code> or <code>mark-permanent</code> set (or playback of the current file ends). Until this happens, <code>revert-seek</code> will always seek to the marked point. This flag cannot be combined with <code>mark</code>. </p>
<p> Using it without any arguments gives you the default behavior.</p>
<dt><code>frame-step</code></p>
<dd>Play one frame, then pause. Does nothing with audio-only playback.</p>
<dt><code>frame-back-step</code></p>
<dd>Go back by one frame, then pause. Note that this can be very slow (it tries to be precise, not fast), and sometimes fails to behave as expected. How well this works depends on whether precise seeking works correctly (e.g. see the <code>&#8211;hr-seek-demuxer-offset</code> option). Video filters or other video post-processing that modifies timing of frames (e.g. deinterlacing) should usually work, but might make backstepping silently behave incorrectly in corner cases. Using <code>&#8211;hr-seek-framedrop=no</code> should help, although it might make precise seeking slower. </p>
<p> This does not work with audio-only playback.</p>
<dt><code>set &lt;name&gt; &lt;value&gt;</code></p>
<dd>Set the given property or option to the given value.</p>
<dt><code>add &lt;name&gt; [&lt;value&gt;]</code></p>
<dd>Add the given value to the property or option. On overflow or underflow, clamp the property to the maximum. If <code>&lt;value&gt;</code> is omitted, assume <code>1</code>.</p>
<dt><code>cycle &lt;name&gt; [&lt;value&gt;]</code></p>
<dd>Cycle the given property or option. The second argument can be <code>up</code> or <code>down</code> to set the cycle direction. On overflow, set the property back to the minimum, on underflow set it to the maximum. If <code>up</code> or <code>down</code> is omitted, assume <code>up</code>. </p>
<p> Whether or not key-repeat is enabled by default depends on the property. Currently properties with continuous values are repeatable by default (like <code>volume</code>), while discrete values are not (like <code>osd-level</code>).</p>
<dt><code>multiply &lt;name&gt; &lt;value&gt;</code></p>
<dd>Similar to <code>add</code>, but multiplies the property or option with the numeric value.</p>
<dt><code>screenshot &lt;flags&gt;</code></p>
<dd>Take a screenshot. </p>
<p> Multiple flags are available (some can be combined with <code>+</code>):</p>
<dt><code>&lt;subtitles&gt; (default)</code></p>
<dd>Save the video image, in its original resolution, and with subtitles. Some video outputs may still include the OSD in the output under certain circumstances.</p>
<dt><code>&lt;video&gt;</code></p>
<dd>Like <code>subtitles</code>, but typically without OSD or subtitles. The exact behavior depends on the selected video output.</p>
<dt><code>&lt;window&gt;</code></p>
<dd>Save the contents of the mpv window. Typically scaled, with OSD and subtitles. The exact behavior depends on the selected video output, and if no support is available, this will act like <code>video</code>.</p>
<dt><code>&lt;each-frame&gt;</code></p>
<dd>Take a screenshot each frame. Issue this command again to stop taking screenshots. Note that you should disable frame-dropping when using this mode &#8211; or you might receive duplicate images in cases when a frame was dropped. This flag can be combined with the other flags, e.g. <code>video+each-frame</code>. </p>
<p> Older mpv versions required passing <code>single</code> and <code>each-frame</code> as second argument (and did not have flags). This syntax is still understood, but deprecated and might be removed in the future. </p>
<p> If you combine this command with another one using <code>;</code>, you can use the <code>async</code> flag to make encoding/writing the image file asynchronous. For normal standalone commands, this is always asynchronous, and the flag has no effect. (This behavior changed with mpv 0.29.0.)</p>
<dt><code>screenshot-to-file &lt;filename&gt; &lt;flags&gt;</code></p>
<dd>Take a screenshot and save it to a given file. The format of the file will be guessed by the extension (and <code>&#8211;screenshot-format</code> is ignored &#8211; the behavior when the extension is missing or unknown is arbitrary). </p>
<p> The second argument is like the first argument to <code>screenshot</code> and supports <code>subtitles</code>, <code>video</code>, <code>window</code>. </p>
<p> If the file already exists, it&#8217;s overwritten. </p>
<p> Like all input command parameters, the filename is subject to property expansion as described in <i>Property Expansion</i>.</p>
<dt><code>playlist-next &lt;flags&gt;</code></p>
<dd>Go to the next entry on the playlist. </p>
<p> First argument:</p>
<dt><code>weak (default)</code></p>
<dd>If the last file on the playlist is currently played, do nothing.</p>
<dt><code>force</code></p>
<dd>Terminate playback if there are no more files on the playlist.</p>
<dt><code>playlist-prev &lt;flags&gt;</code></p>
<dd>Go to the previous entry on the playlist. </p>
<p> First argument:</p>
<dt><code>weak (default)</code></p>
<dd>If the first file on the playlist is currently played, do nothing.</p>
<dt><code>force</code></p>
<dd>Terminate playback if the first file is being played.</p>
<dt><code>playlist-play-index &lt;integer|current|none&gt;</code></p>
<dd>Start (or restart) playback of the given playlist index. In addition to the 0-based playlist entry index, it supports the following values:</p>
<dt><code>&lt;current&gt;</code></p>
<dd>The current playlist entry (as in <code>playlist-current-pos</code>) will be played again (unload and reload). If none is set, playback is stopped. (In corner cases, <code>playlist-current-pos</code> can point to a playlist entry even if playback is currently inactive,</p>
<dt><code>&lt;none&gt;</code></p>
<dd>Playback is stopped. If idle mode (<code>&#8211;idle</code>) is enabled, the player will enter idle mode, otherwise it will exit. </p>
<p> This comm and is similar to <code>loadfile</code> in that it only manipulates the state of what to play next, without waiting until the current file is unloaded, and the next one is loaded. </p>
<p> Setting <code>playlist-pos</code> or similar properties can have a similar effect to this command. However, it&#8217;s more explicit, and guarantees that playback is restarted if for example the new playlist entry is the same as the previous one.</p>
<dt><code>loadfile &lt;url&gt; [&lt;flags&gt; [&lt;options&gt;]]</code></p>
<dd>Load the given file or URL and play it. Technically, this is just a playlist manipulation command (which either replaces the playlist or appends an entry to it). Actual file loading happens independently. For example, a <code>loadfile</code> command that replaces the current file with a new one returns before the current file is stopped, and the new file even begins loading. </p>
<p> Second argument:</p>
<dt><code>&lt;replace&gt; (default)</code></p>
<dd>Stop playback of the current file, and play the new file immediately.</p>
<dt><code>&lt;append&gt;</code></p>
<dd>Append the file to the playlist.</p>
<dt><code>&lt;append-play&gt;</code></p>
<dd>Append the file, and if nothing is currently playing, start playback. (Always starts with the added file, even if the playlist was not empty before running this command.) </p>
<p> The third argument is a list of options and values which should be set while the file is playing. It is of the form <code>opt1=value1,opt2=value2,..</code>. When using the client API, this can be a <code>MPV_FORMAT_NODE_MAP</code> (or a Lua table), however the values themselves must be strings currently. These options are set during playback, and restored to the previous value at end of playback (see <i>Per-File Options</i>).</p>
<dt><code>loadlist &lt;url&gt; [&lt;flags&gt;]</code></p>
<dd>Load the given playlist file or URL (like <code>&#8211;playlist</code>). </p>
<p> Second argument:</p>
<dt><code>&lt;replace&gt; (default)</code></p>
<dd>Stop playback and replace the internal playlist with the new one.</p>
<dt><code>&lt;append&gt;</code></p>
<dd>Append the new playlist at the end of the current internal playlist.</p>
<dt><code>&lt;append-play&gt;</code></p>
<dd>Append the new playlist, and if nothing is currently playing, start playback. (Always starts with the new playlist, even if the internal playlist was not empty before running this command.)</p>
<dt><code>playlist-clear</code></p>
<dd>Clear the playlist, except the currently played file.</p>
<dt><code>playlist-remove &lt;index&gt;</code></p>
<dd>Remove the playlist entry at the given index. Index values start counting with 0. The special value <code>current</code> removes the current entry. Note that removing the current entry also stops playback and starts playing the next entry.</p>
<dt><code>playlist-move &lt;index1&gt; &lt;index2&gt;</code></p>
<dd>Move the playlist entry at index1, so that it takes the place of the entry index2. (Paradoxically, the moved playlist entry will not have the index value index2 after moving if index1 was lower than index2, because index2 refers to the target entry, not the index the entry will have after moving.)</p>
<dt><code>playlist-shuffle</code></p>
<dd>Shuffle the playlist. This is similar to what is done on start if the <code>&#8211;shuffle</code> option is used.</p>
<dt><code>playlist-unshuffle</code></p>
<dd>Attempt to revert the previous <code>playlist-shuffle</code> command. This works only once (multiple successive <code>playlist-unshuffle</code> commands do nothing). May not work correctly if new recursive playlists have been opened since a <code>playlist-shuffle</code> command.</p>
<dt><code>run &lt;command&gt; [&lt;arg1&gt; [&lt;arg2&gt; [&#8230;]]]</code></p>
<dd>Run the given command. Unlike in MPlayer/mplayer2 and earlier versions of mpv (0.2.x and older), this doesn&#8217;t call the shell. Instead, the command is run directly, with each argument passed separately. Each argument is expanded like in <i>Property Expansion</i>. </p>
<p> This command has a variable number of arguments, and cannot be used with named arguments. </p>
<p> The program is run in a detached way. mpv doesn&#8217;t wait until the command is completed, but continues playback right after spawning it. </p>
<p> To get the old behavior, use <code>/bin/sh</code> and <code>-c</code> as the first two arguments.</p>
<dt>Example</p>
<dd><code>run &quot;/bin/sh&quot; &quot;-c&quot; &quot;echo ${title} &gt; /tmp/playing&quot;</code> </p>
<p> This is not a particularly good example, because it doesn&#8217;t handle escaping, and a specially prepared file might allow an attacker to execute arbitrary shell commands. It is recommended to write a small shell script, and call that with <code>run</code>.</p>
<dt><code>subprocess</code></p>
<dd>Similar to <code>run</code>, but gives more control about process execution to the caller, and does does not detach the process. </p>
<p> You can avoid blocking until the process terminates by running this command asynchronously. (For example <code>mp.command_native_async()</code> in Lua scripting.) </p>
<p> This has the following named arguments. The order of them is not guaranteed, so you should always call them with named arguments, see <i>Named arguments</i>.</p>
<dt><code>args</code> (<code>MPV_FORMAT_NODE_ARRAY[MPV_FORMAT_STRING]</code>)</p>
<dd>Array of strings with the command as first argument, and subsequent command line arguments following. This is just like the <code>run</code> command argument list. </p>
<p> The first array entry is either an absolute path to the executable, or a filename with no path components, in which case the executable is searched in the directories in the <code>PATH</code> environment variable. On Unix, this is equivalent to <code>posix_spawnp</code> and <code>execvp</code> behavior.</p>
<dt><code>playback_only</code> (<code>MPV_FORMAT_FLAG</code>)</p>
<dd>Boolean indicating whether the process should be killed when playback terminates (optional, default: true). If enabled, stopping playback will automatically kill the process, and you can&#8217;t start it outside of playback.</p>
<dt><code>capture_size</code> (<code>MPV_FORMAT_INT64</code>)</p>
<dd>Integer setting the maximum number of stdout plus stderr bytes that can be captured (optional, default: 64MB). If the number of bytes exceeds this, capturing is stopped. The limit is per captured stream.</p>
<dt><code>capture_stdout</code> (<code>MPV_FORMAT_FLAG</code>)</p>
<dd>Capture all data the process outputs to stdout and return it once the process ends (optional, default: no).</p>
<dt><code>capture_stderr</code> (<code>MPV_FORMAT_FLAG</code>)</p>
<dd>Same as <code>capture_stdout</code>, but for stderr.</p>
<dt><code>detach</code> (<code>MPV_FORMAT_FLAG</code>)</p>
<dd>Whether to run the process in detached mode (optional, default: no). In this mode, the process is run in a new process session, and the command does not wait for the process to terminate. If neither <code>capture_stdout</code> nor <code>capture_stderr</code> have been set to true, the command returns immediately after the new process has been started, otherwise the command will read as long as the pipes are open.</p>
<dt><code>env</code> (<code>MPV_FORMAT_NODE_ARRAY[MPV_FORMAT_STRING]</code>)</p>
<dd>Set a list of environment variables for the new process (default: empty). If an empty list is passed, the environment of the mpv process is used instead. (Unlike the underlying OS mechanisms, the mpv command cannot start a process with empty environment. Fortunately, that is completely useless.) The format of the list is as in the <code>execle()</code> syscall. Each string item defines an environment variable as in <code>NANME=VALUE</code>. </p>
<p> On Lua, you may use <code>utils.get_env_list()</code> to retrieve the current environment if you e.g. simply want to add a new variable.</p>
<dt><code>stdin_data</code> (<code>MPV_FORMAT_STRING</code>)</p>
<dd>Feed the given string to the new process&#8217; stdin. Since this is a string, you cannot pass arbitrary binary data. If the process terminates or closes the pipe before all data is written, the remaining data is silently discarded. Probably does not work on win32.</p>
<dt><code>passthrough_stdin</code> (<code>MPV_FORMAT_FLAG</code>)</p>
<dd>If enabled, wire the new process&#8217; stdin to mpv&#8217;s stdin (default: no). Before mpv 0.33.0, this argument did not exist, but the behavior was as if this was set to true. </p>
<p> The command returns the following result (as <code>MPV_FORMAT_NODE_MAP</code>):</p>
<dt><code>status</code> (<code>MPV_FORMAT_INT64</code>)</p>
<dd>The raw exit status of the process. It will be negative on error. The meaning of negative values is undefined, other than meaning error (and does not correspond to OS low level exit status values). </p>
<p> On Windows, it can happen that a negative return value is returned even if the process exits gracefully, because the win32 <code>UINT</code> exit code is assigned to an <code>int</code> variable before being set as <code>int64_t</code> field in the result map. This might be fixed later.</p>
<dt><code>stdout</code> (<code>MPV_FORMAT_BYTE_ARRAY</code>)</p>
<dd>Captured stdout stream, limited to <code>capture_size</code>.</p>
<dt><code>stderr</code> (<code>MPV_FORMAT_BYTE_ARRAY</code>)</p>
<dd>Same as <code>stdout</code>, but for stderr.</p>
<dt><code>error_string</code> (<code>MPV_FORMAT_STRING</code>)</p>
<dd>Empty string if the process exited gracefully. The string <code>killed</code> if the process was terminated in an unusual way. The string <code>init</code> if the process could not be started. </p>
<p> On Windows, <code>killed</code> is only returned when the process has been killed by mpv as a result of <code>playback_only</code> being set to true.</p>
<dt><code>killed_by_us</code> (<code>MPV_FORMAT_FLAG</code>)</p>
<dd>Whether the process has been killed by mpv, for example as a result of <code>playback_only</code> being set to true, aborting the command (e.g. by <code>mp.abort_async_command()</code>), or if the player is about to exit. </p>
<p> Note that the command itself will always return success as long as the parameters are correct. Whether the process could be spawned or whether it was somehow killed or returned an error status has to be queried from the result value. </p>
<p> This command can be asynchronously aborted via API. </p>
<p> In all cases, the subprocess will be terminated on player exit. Also see <i>Asynchronous command details</i>. Only the <code>run</code> command can start processes in a truly detached way.</p>
<dt>Warning</p>
<dd>Don&#8217;t forget to set the <code>playback_only</code> field if you want the command run while the player is in idle mode, or if you don&#8217;t want that end of playback kills the command.</p>
<dt>Example</p>
<dd>
<pre>local r = mp.command_native({
 name = &quot;subprocess&quot;,
 playback_only = false,
 capture_stdout = true,
 args = {&quot;cat&quot;, &quot;/proc/cpuinfo&quot;},
})
if r.status == 0 then
 print(&quot;result: &quot; .. r.stdout)
end</pre>
<p>This is a fairly useless Lua example, which demonstrates how to run a process in a blocking manner, and retrieving its stdout output.</p>
<dt><code>quit [&lt;code&gt;]</code></p>
<dd>Exit the player. If an argument is given, it&#8217;s used as process exit code.</p>
<dt><code>quit-watch-later [&lt;code&gt;]</code></p>
<dd>Exit player, and store current playback position. Playing that file later will seek to the previous position on start. The (optional) argument is exactly as in the <code>quit</code> command.</p>
<dt><code>sub-add &lt;url&gt; [&lt;flags&gt; [&lt;title&gt; [&lt;lang&gt;]]]</code></p>
<dd>Load the given subtitle file or stream. By default, it is selected as current subtitle after loading. </p>
<p> The <code>flags</code> argument is one of the following values: </p>
<p> &lt;select&gt; Select the subtitle immediately (default). </p>
<p> &lt;auto&gt; Don&#8217;t select the subtitle. (Or in some special situations, let the default stream selection mechanism decide.) </p>
<p> &lt;cached&gt; Select the subtitle. If a subtitle with the same filename was already added, that one is selected, instead of loading a duplicate entry. (In this case, title/language are ignored, and if the was changed since it was loaded, these changes won&#8217;t be reflected.) </p>
<p> The <code>title</code> argument sets the track title in the UI. </p>
<p> The <code>lang</code> argument sets the track language, and can also influence stream selection with <code>flags</code> set to <code>auto</code>.</p>
<dt><code>sub-remove [&lt;id&gt;]</code></p>
<dd>Remove the given subtitle track. If the <code>id</code> argument is missing, remove the current track. (Works on external subtitle files only.)</p>
<dt><code>sub-reload [&lt;id&gt;]</code></p>
<dd>Reload the given subtitle tracks. If the <code>id</code> argument is missing, reload the current track. (Works on external subtitle files only.) </p>
<p> This works by unloading and re-adding the subtitle track.</p>
<dt><code>sub-step &lt;skip&gt; &lt;flags&gt;</code></p>
<dd>Change subtitle timing such, that the subtitle event after the next <code>&lt;skip&gt;</code> subtitle events is displayed. <code>&lt;skip&gt;</code> can be negative to step backwards. </p>
<p> Secondary argument:</p>
<dt><code>primary (default)</code></p>
<dd>Steps through the primary subtitles.</p>
<dt><code>secondary</code></p>
<dd>Steps through the secondary subtitles.</p>
<dt><code>sub-seek &lt;skip&gt; &lt;flags&gt;</code></p>
<dd>Seek to the next (skip set to 1) or the previous (skip set to -1) subtitle. This is similar to <code>sub-step</code>, except that it seeks video and audio instead of adjusting the subtitle delay. </p>
<p> Secondary argument:</p>
<dt><code>primary (default)</code></p>
<dd>Seeks through the primary subtitles.</p>
<dt><code>secondary</code></p>
<dd>Seeks through the secondary subtitles. </p>
<p> For embedded subtitles (like with Matroska), this works only with subtitle events that have already been displayed, or are within a short prefetch range.</p>
<dt><code>print-text &lt;text&gt;</code></p>
<dd>Print text to stdout. The string can contain properties (see <i>Property Expansion</i>). Take care to put the argument in quotes.</p>
<dt><code>show-text &lt;text&gt; [&lt;duration&gt;|-1 [&lt;level&gt;]]</code></p>
<dd>Show text on the OSD. The string can contain properties, which are expanded as described in <i>Property Expansion</i>. This can be used to show playback time, filename, and so on.</p>
<dt><code>&lt;duration&gt;</code></p>
<dd>The time in ms to show the message for. By default, it uses the same value as <code>&#8211;osd-duration</code>.</p>
<dt><code>&lt;level&gt;</code></p>
<dd>The minimum OSD level to show the text at (see <code>&#8211;osd-level</code>).</p>
<dt><code>expand-text &lt;string&gt;</code></p>
<dd>Property-expand the argument and return the expanded string. This can be used only through the client API or from a script using <code>mp.command_native</code>. (see <i>Property Expansion</i>).</p>
<dt><code>expand-path &lt;string&gt;</code></p>
<dd>Expand a path&#8217;s double-tilde placeholders into a platform-specific path. As <code>expand-text</code>, this can only be used through the client API or from a script using <code>mp.command_native</code>.</p>
<dt>Example</p>
<dd><code>mp.osd_message(mp.command_native({&quot;expand-path&quot;, &quot;~~home/&quot;}))</code> </p>
<p> This line of Lua would show the location of the user&#8217;s mpv configuration directory on the OSD.</p>
<dt><code>show-progress</code></p>
<dd>Show the progress bar, the elapsed time and the total duration of the file on the OSD.</p>
<dt><code>write-watch-later-config</code></p>
<dd>Write the resume config file that the <code>quit-watch-later</code> command writes, but continue playback normally.</p>
<dt><code>delete-watch-later-config [&lt;filename&gt;]</code></p>
<dd>Delete any existing resume config file that was written by <code>quit-watch-later</code> or <code>write-watch-later-config</code>. If a filename is specified, then the deleted config is for that file; otherwise, it is the same one as would be written by <code>quit-watch-later</code> or <code>write-watch-later-config</code> in the current circumstance.</p>
<dt><code>stop [&lt;flags&gt;]</code></p>
<dd>Stop playback and clear playlist. With default settings, this is essentially like <code>quit</code>. Useful for the client API: playback can be stopped without terminating the player. </p>
<p> The first argument is optional, and supports the following flags:</p>
<dt><code>keep-playlist</code></p>
<dd>Do not clear the playlist.</p>
<dt><code>mouse &lt;x&gt; &lt;y&gt; [&lt;button&gt; [&lt;mode&gt;]]</code></p>
<dd>Send a mouse event with given coordinate (<code>&lt;x&gt;</code>, <code>&lt;y&gt;</code>). </p>
<p> Second argument:</p>
<dt><code>&lt;button&gt;</code></p>
<dd>The button number of clicked mouse button. This should be one of 0-19. If <code>&lt;button&gt;</code> is omitted, only the position will be updated. </p>
<p> Third argument:</p>
<dt><code>&lt;single&gt; (default)</code></p>
<dd>The mouse event represents regular single click.</p>
<dt><code>&lt;double&gt;</code></p>
<dd>The mouse event represents double-click.</p>
<dt><code>keypress &lt;name&gt;</code></p>
<dd>Send a key event through mpv&#8217;s input handler, triggering whatever behavior is configured to that key. <code>name</code> uses the <code>input.conf</code> naming scheme for keys and modifiers. Useful for the client API: key events can be sent to libmpv to handle internally.</p>
<dt><code>keydown &lt;name&gt;</code></p>
<dd>Similar to <code>keypress</code>, but sets the <code>KEYDOWN</code> flag so that if the key is bound to a repeatable command, it will be run repeatedly with mpv&#8217;s key repeat timing until the <code>keyup</code> command is called.</p>
<dt><code>keyup [&lt;name&gt;]</code></p>
<dd>Set the <code>KEYUP</code> flag, stopping any repeated behavior that had been triggered. <code>name</code> is optional. If <code>name</code> is not given or is an empty string, <code>KEYUP</code> will be set on all keys. Otherwise, <code>KEYUP</code> will only be set on the key specified by <code>name</code>.</p>
<dt><code>keybind &lt;name&gt; &lt;command&gt;</code></p>
<dd>Binds a key to an input command. <code>command</code> must be a complete command containing all the desired arguments and flags. Both <code>name</code> and <code>command</code> use the <code>input.conf</code> naming scheme. This is primarily useful for the client API.</p>
<dt><code>audio-add &lt;url&gt; [&lt;flags&gt; [&lt;title&gt; [&lt;lang&gt;]]]</code></p>
<dd>Load the given audio file. See <code>sub-add</code> command.</p>
<dt><code>audio-remove [&lt;id&gt;]</code></p>
<dd>Remove the given audio track. See <code>sub-remove</code> command.</p>
<dt><code>audio-reload [&lt;id&gt;]</code></p>
<dd>Reload the given audio tracks. See <code>sub-reload</code> command.</p>
<dt><code>video-add &lt;url&gt; [&lt;flags&gt; [&lt;title&gt; [&lt;lang&gt; [&lt;albumart&gt;]]]]</code></p>
<dd>Load the given video file. See <code>sub-add</code> command for common options.</p>
<dt><code>albumart</code> (<code>MPV_FORMAT_FLAG</code>)</p>
<dd>If enabled, mpv will load the given video as album art.</p>
<dt><code>video-remove [&lt;id&gt;]</code></p>
<dd>Remove the given video track. See <code>sub-remove</code> command.</p>
<dt><code>video-reload [&lt;id&gt;]</code></p>
<dd>Reload the given video tracks. See <code>sub-reload</code> command.</p>
<dt><code>rescan-external-files [&lt;mode&gt;]</code></p>
<dd>Rescan external files according to the current <code>&#8211;sub-auto</code>, <code>&#8211;audio-file-auto</code> and <code>&#8211;cover-art-auto</code> settings. This can be used to auto-load external files <i>after</i> the file was loaded. </p>
<p> The <code>mode</code> argument is one of the following:</p>
<dt><code>&lt;reselect&gt; (default)</code></p>
<dd>Select the default audio and subtitle streams, which typically selects external files with the highest preference. (The implementation is not perfect, and could be improved on request.)</p>
<dt><code>&lt;keep-selection&gt;</code></p>
<dd>Do not change current track selections.</dl>
<h3>Input Commands that are Possibly Subject to Change</h3>
<dl COMPACT>
<dt><code>af &lt;operation&gt; &lt;value&gt;</code></p>
<dd>Change audio filter chain. See <code>vf</code> command.</p>
<dt><code>vf &lt;operation&gt; &lt;value&gt;</code></p>
<dd>Change video filter chain. </p>
<p> The semantics are exactly the same as with option parsing (see <i>VIDEO FILTERS</i>). As such the text below is a redundant and incomplete summary. </p>
<p> The first argument decides what happens:</p>
<dt><code>&lt;set&gt;</code></p>
<dd>Overwrite the previous filter chain with the new one.</p>
<dt><code>&lt;add&gt;</code></p>
<dd>Append the new filter chain to the previous one.</p>
<dt><code>&lt;toggle&gt;</code></p>
<dd>Check if the given filter (with the exact parameters) is already in the video chain. If it is, remove the filter. If it isn&#8217;t, add the filter. (If several filters are passed to the command, this is done for each filter.) </p>
<p> A special variant is combining this with labels, and using <code>@name</code> without filter name and parameters as filter entry. This toggles the enable/disable flag.</p>
<dt><code>&lt;remove&gt;</code></p>
<dd>Like <code>toggle</code>, but always remove the given filter from the chain.</p>
<dt><code>&lt;del&gt;</code></p>
<dd>Remove the given filters from the video chain. Unlike in the other cases, the second parameter is a comma separated list of filter names or integer indexes. <code>0</code> would denote the first filter. Negative indexes start from the last filter, and <code>-1</code> denotes the last filter. Deprecated, use <code>remove</code>.</p>
<dt><code>&lt;clr&gt;</code></p>
<dd>Remove all filters. Note that like the other sub-commands, this does not control automatically inserted filters. </p>
<p> The argument is always needed. E.g. in case of <code>clr</code> use <code>vf clr &quot;&quot;</code>. </p>
<p> You can assign labels to filter by prefixing them with <code>@name:</code> (where <code>name</code> is a user-chosen arbitrary identifier). Labels can be used to refer to filters by name in all of the filter chain modification commands. For <code>add</code>, using an already used label will replace the existing filter. </p>
<p> The <code>vf</code> command shows the list of requested filters on the OSD after changing the filter chain. This is roughly equivalent to <code>show-text ${vf}</code>. Note that auto-inserted filters for format conversion are not shown on the list, only what was requested by the user. </p>
<p> Normally, the commands will check whether the video chain is recreated successfully, and will undo the operation on failure. If the command is run before video is configured (can happen if the command is run immediately after opening a file and before a video frame is decoded), this check can&#8217;t be run. Then it can happen that creating the video chain fails.</p>
<dt>Example for input.conf</p>
<dd>
<dt>&bull;</p>
<dd><code>a vf set vflip</code> turn the video upside-down on the <code>a</code> key</p>
<dt>&bull;</p>
<dd><code>b vf set &quot;&quot;</code> remove all video filters on <code>b</code></p>
<dt>&bull;</p>
<dd><code>c vf toggle gradfun</code> toggle debanding on <code>c</code></p>
<dt>Example how to toggle disabled filters at runtime</p>
<dd>
<dt>&bull;</p>
<dd>Add something like <code>vf-add=@deband:!gradfun</code> to <code>mpv.conf</code>. The <code>@deband:</code> is the label, an arbitrary, user-given name for this filter entry. The <code>!</code> before the filter name disables the filter by default. Everything after this is the normal filter name and possibly filter parameters, like in the normal <code>&#8211;vf</code> syntax.</p>
<dt>&bull;</p>
<dd>Add <code>a vf toggle @deband</code> to <code>input.conf</code>. This toggles the &quot;disabled&quot; flag for the filter with the label <code>deband</code> when the <code>a</code> key is hit.</p>
<dt><code>cycle-values [&lt;!reverse&gt;] &lt;property&gt; &lt;value1&gt; [&lt;value2&gt; [&#8230;]]</code></p>
<dd>Cycle through a list of values. Each invocation of the command will set the given property to the next value in the list. The command will use the current value of the property/option, and use it to determine the current position in the list of values. Once it has found it, it will set the next value in the list (wrapping around to the first item if needed). </p>
<p> This command has a variable number of arguments, and cannot be used with named arguments. </p>
<p> The special argument <code>!reverse</code> can be used to cycle the value list in reverse. The only advantage is that you don&#8217;t need to reverse the value list yourself when adding a second key binding for cycling backwards.</p>
<dt><code>enable-section &lt;name&gt; [&lt;flags&gt;]</code></p>
<dd>This command is deprecated, except for mpv-internal uses. </p>
<p> Enable all key bindings in the named input section. </p>
<p> The enabled input sections form a stack. Bindings in sections on the top of the stack are preferred to lower sections. This command puts the section on top of the stack. If the section was already on the stack, it is implicitly removed beforehand. (A section cannot be on the stack more than once.) </p>
<p> The <code>flags</code> parameter can be a combination (separated by <code>+</code>) of the following flags:</p>
<dt><code>&lt;exclusive&gt;</code></p>
<dd>All sections enabled before the newly enabled section are disabled. They will be re-enabled as soon as all exclusive sections above them are removed. In other words, the new section shadows all previous sections.</p>
<dt><code>&lt;allow-hide-cursor&gt;</code></p>
<dd>This feature can&#8217;t be used through the public API.</p>
<dt><code>&lt;allow-vo-dragging&gt;</code></p>
<dd>Same.</p>
<dt><code>disable-section &lt;name&gt;</code></p>
<dd>This command is deprecated, except for mpv-internal uses. </p>
<p> Disable the named input section. Undoes <code>enable-section</code>.</p>
<dt><code>define-section &lt;name&gt; &lt;contents&gt; [&lt;flags&gt;]</code></p>
<dd>This command is deprecated, except for mpv-internal uses. </p>
<p> Create a named input section, or replace the contents of an already existing input section. The <code>contents</code> parameter uses the same syntax as the <code>input.conf</code> file (except that using the section syntax in it is not allowed), including the need to separate bindings with a newline character. </p>
<p> If the <code>contents</code> parameter is an empty string, the section is removed. </p>
<p> The section with the name <code>default</code> is the normal input section. </p>
<p> In general, input sections have to be enabled with the <code>enable-section</code> command, or they are ignored. </p>
<p> The last parameter has the following meaning:</p>
<dt><code>&lt;default&gt; (also used if parameter omitted)</code></p>
<dd>Use a key binding defined by this section only if the user hasn&#8217;t already bound this key to a command.</p>
<dt><code>&lt;force&gt;</code></p>
<dd>Always bind a key. (The input section that was made active most recently wins if there are ambiguities.) </p>
<p> This command can be used to dispatch arbitrary keys to a script or a client API user. If the input section defines <code>script-binding</code> commands, it is also possible to get separate events on key up/down, and relatively detailed information about the key state. The special key name <code>unmapped</code> can be used to match any unmapped key.</p>
<dt><code>overlay-add &lt;id&gt; &lt;x&gt; &lt;y&gt; &lt;file&gt; &lt;offset&gt; &lt;fmt&gt; &lt;w&gt; &lt;h&gt; &lt;stride&gt;</code></p>
<dd>Add an OSD overlay sourced from raw data. This might be useful for scripts and applications controlling mpv, and which want to display things on top of the video window. </p>
<p> Overlays are usually displayed in screen resolution, but with some VOs, the resolution is reduced to that of the video&#8217;s. You can read the <code>osd-width</code> and <code>osd-height</code> properties. At least with <code>&#8211;vo-xv</code> and anamorphic video (such as DVD), <code>osd-par</code> should be read as well, and the overlay should be aspect-compensated. </p>
<p> This has the following named arguments. The order of them is not guaranteed, so you should always call them with named arguments, see <i>Named arguments</i>. </p>
<p> <code>id</code> is an integer between 0 and 63 identifying the overlay element. The ID can be used to add multiple overlay parts, update a part by using this command with an already existing ID, or to remove a part with <code>overlay-remove</code>. Using a previously unused ID will add a new overlay, while reusing an ID will update it. </p>
<p> <code>x</code> and <code>y</code> specify the position where the OSD should be displayed. </p>
<p> <code>file</code> specifies the file the raw image data is read from. It can be either a numeric UNIX file descriptor prefixed with <code>@</code> (e.g. <code>@4</code>), or a filename. The file will be mapped into memory with <code>mmap()</code>, copied, and unmapped before the command returns (changed in mpv 0.18.1). </p>
<p> It is also possible to pass a raw memory address for use as bitmap memory by passing a memory address as integer prefixed with an <code>&amp;</code> character. Passing the wrong thing here will crash the player. This mode might be useful for use with libmpv. The <code>offset</code> parameter is simply added to the memory address (since mpv 0.8.0, ignored before). </p>
<p> <code>offset</code> is the byte offset of the first pixel in the source file. (The current implementation always mmap&#8217;s the whole file from position 0 to the end of the image, so large offsets should be avoided. Before mpv 0.8.0, the offset was actually passed directly to <code>mmap</code>, but it was changed to make using it easier.) </p>
<p> <code>fmt</code> is a string identifying the image format. Currently, only <code>bgra</code> is defined. This format has 4 bytes per pixels, with 8 bits per component. The least significant 8 bits are blue, and the most significant 8 bits are alpha (in little endian, the components are B-G-R-A, with B as first byte). This uses premultiplied alpha: every color component is already multiplied with the alpha component. This means the numeric value of each component is equal to or smaller than the alpha component. (Violating this rule will lead to different results with different VOs: numeric overflows resulting from blending broken alpha values is considered something that shouldn&#8217;t happen, and consequently implementations don&#8217;t ensure that you get predictable behavior in this case.) </p>
<p> <code>w</code>, <code>h</code>, and <code>stride</code> specify the size of the overlay. <code>w</code> is the visible width of the overlay, while <code>stride</code> gives the width in bytes in memory. In the simple case, and with the <code>bgra</code> format, <code>stride==4*w</code>. In general, the total amount of memory accessed is <code>stride * h</code>. (Technically, the minimum size would be <code>stride * (h &#8211; 1) + w * 4</code>, but for simplicity, the player will access all <code>stride * h</code> bytes.) </p>
<p> <code>NOTE:</code> Before mpv 0.18.1, you had to do manual &quot;double buffering&quot; when updating an overlay by replacing it with a different memory buffer. Since mpv 0.18.1, the memory is simply copied and doesn&#8217;t reference any of the memory indicated by the command&#8217;s arguments after the commend returns. If you want to use this command before mpv 0.18.1, reads the old docs to see how to handle this correctly.</p>
<dt><code>overlay-remove &lt;id&gt;</code></p>
<dd>Remove an overlay added with <code>overlay-add</code> and the same ID. Does nothing if no overlay with this ID exists.</p>
<dt><code>osd-overlay</code></p>
<dd>Add/update/remove an OSD overlay. </p>
<p> (Although this sounds similar to <code>overlay-add</code>, <code>osd-overlay</code> is for text overlays, while <code>overlay-add</code> is for bitmaps. Maybe <code>overlay-add</code> will be merged into <code>osd-overlay</code> to remove this oddity.) </p>
<p> You can use this to add text overlays in ASS format. ASS has advanced positioning and rendering tags, which can be used to render almost any kind of vector graphics. </p>
<p> This command accepts the following parameters:</p>
<dt><code>id</code></p>
<dd>Arbitrary integer that identifies the overlay. Multiple overlays can be added by calling this command with different <code>id</code> parameters. Calling this command with the same <code>id</code> replaces the previously set overlay. </p>
<p> There is a separate namespace for each libmpv client (i.e. IPC connection, script), so IDs can be made up and assigned by the API user without conflicting with other API users. </p>
<p> If the libmpv client is destroyed, all overlays associated with it are also deleted. In particular, connecting via <code>&#8211;input-ipc-server</code>, adding an overlay, and disconnecting will remove the overlay immediately again.</p>
<dt><code>format</code></p>
<dd>String that gives the type of the overlay. Accepts the following values (HTML rendering of this is broken, view the generated manpage instead, or the raw RST source):</p>
<dt><code>ass-events</code></p>
<dd>The <code>data</code> parameter is a string. The string is split on the newline character. Every line is turned into the <code>Text</code> part of a <code>Dialogue</code> ASS event. Timing is unused (but behavior of timing dependent ASS tags may change in future mpv versions). </p>
<p> Note that it&#8217;s better to put multiple lines into <code>data</code>, instead of adding multiple OSD overlays. </p>
<p> This provides 2 ASS <code>Styles</code>. <code>OSD</code> contains the text style as defined by the current <code>&#8211;osd-&#8230;</code> options. <code>Default</code> is similar, and contains style that <code>OSD</code> would have if all options were set to the default. </p>
<p> In addition, the <code>res_x</code> and <code>res_y</code> options specify the value of the ASS <code>PlayResX</code> and <code>PlayResY</code> header fields. If <code>res_y</code> is set to 0, <code>PlayResY</code> is initialized to an arbitrary default value (but note that the default for this command is 720, not 0). If <code>res_x</code> is set to 0, <code>PlayResX</code> is set based on <code>res_y</code> such that a virtual ASS pixel has a square pixel aspect ratio.</p>
<dt><code>none</code></p>
<dd>Special value that causes the overlay to be removed. Most parameters other than <code>id</code> and <code>format</code> are mostly ignored.</p>
<dt><code>data</code></p>
<dd>String defining the overlay contents according to the <code>format</code> parameter.</p>
<dt><code>res_x</code>, <code>res_y</code></p>
<dd>Used if <code>format</code> is set to <code>ass-events</code> (see description there). Optional, defaults to 0/720.</p>
<dt><code>z</code></p>
<dd>The Z order of the overlay. Optional, defaults to 0. </p>
<p> Note that Z order between different overlays of different formats is static, and cannot be changed (currently, this means that bitmap overlays added by <code>overlay-add</code> are always on top of the ASS overlays added by <code>osd-overlay</code>). In addition, the builtin OSD components are always below any of the custom OSD. (This includes subtitles of any kind as well as text rendered by <code>show-text</code>.) </p>
<p> It&#8217;s possible that future mpv versions will randomly change how Z order between different OSD formats and builtin OSD is handled.</p>
<dt><code>hidden</code></p>
<dd>If set to true, do not display this (default: false).</p>
<dt><code>compute_bounds</code></p>
<dd>If set to true, attempt to determine bounds and write them to the command&#8217;s result value as <code>x0</code>, <code>x1</code>, <code>y0</code>, <code>y1</code> rectangle (default: false). If the rectangle is empty, not known, or somehow degenerate, it is not set. <code>x1</code>/<code>y1</code> is the coordinate of the bottom exclusive corner of the rectangle. </p>
<p> The result value may depend on the VO window size, and is based on the last known window size at the time of the call. This means the results may be different from what is actually rendered. </p>
<p> For <code>ass-events</code>, the result rectangle is recomputed to <code>PlayRes</code> coordinates (<code>res_x</code>/<code>res_y</code>). If window size is not known, a fallback is chosen. </p>
<p> You should be aware that this mechanism is very inefficient, as it renders the full result, and then uses the bounding box of the rendered bitmap list (even if <code>hidden</code> is set). It will flush various caches. Its results also depend on the used libass version. </p>
<p> This feature is experimental, and may change in some way again. </p>
<p> <code>NOTE:</code> Always use named arguments (<code>mpv_command_node()</code>). Lua scripts should use the <code>mp.create_osd_overlay()</code> helper instead of invoking this command directly.</p>
<dt><code>script-message [&lt;arg1&gt; [&lt;arg2&gt; [&#8230;]]]</code></p>
<dd>Send a message to all clients, and pass it the following list of arguments. What this message means, how many arguments it takes, and what the arguments mean is fully up to the receiver and the sender. Every client receives the message, so be careful about name clashes (or use <code>script-message-to</code>). </p>
<p> This command has a variable number of arguments, and cannot be used with named arguments.</p>
<dt><code>script-message-to &lt;target&gt; [&lt;arg1&gt; [&lt;arg2&gt; [&#8230;]]]</code></p>
<dd>Same as <code>script-message</code>, but send it only to the client named <code>&lt;target&gt;</code>. Each client (scripts etc.) has a unique name. For example, Lua scripts can get their name via <code>mp.get_script_name()</code>. Note that client names only consist of alphanumeric characters and <code>_</code>. </p>
<p> This command has a variable number of arguments, and cannot be used with named arguments.</p>
<dt><code>script-binding &lt;name&gt;</code></p>
<dd>Invoke a script-provided key binding. This can be used to remap key bindings provided by external Lua scripts. </p>
<p> The argument is the name of the binding. </p>
<p> It can optionally be prefixed with the name of the script, using <code>/</code> as separator, e.g. <code>script-binding scriptname/bindingname</code>. Note that script names only consist of alphanumeric characters and <code>_</code>. </p>
<p> For completeness, here is how this command works internally. The details could change any time. On any matching key event, <code>script-message-to</code> or <code>script-message</code> is called (depending on whether the script name is included), with the following arguments:</p>
<dt>1.</p>
<dd>The string <code>key-binding</code>.</p>
<dt>2.</p>
<dd>The name of the binding (as established above).</p>
<dt>3.</p>
<dd>The key state as string (see below).</p>
<dt>4.</p>
<dd>The key name (since mpv 0.15.0).</p>
<dt>5.</p>
<dd>The text the key would produce, or empty string if not applicable. </p>
<p> The 5th argument is only set if no modifiers are present (using the shift key with a letter is normally not emitted as having a modifier, and results in upper case text instead, but some backends may mess up). </p>
<p> The key state consists of 2 characters:</p>
<dt>1.</p>
<dd>One of <code>d</code> (key was pressed down), <code>u</code> (was released), <code>r</code> (key is still down, and was repeated; only if key repeat is enabled for this binding), <code>p</code> (key was pressed; happens if up/down can&#8217;t be tracked).</p>
<dt>2.</p>
<dd>Whether the event originates from the mouse, either <code>m</code> (mouse button) or <code>&#8211;</code> (something else). </p>
<p> Future versions can add more arguments and more key state characters to support more input peculiarities.</p>
<dt><code>ab-loop</code></p>
<dd>Cycle through A-B loop states. The first command will set the <code>A</code> point (the <code>ab-loop-a</code> property); the second the <code>B</code> point, and the third will clear both points.</p>
<dt><code>drop-buffers</code></p>
<dd>Drop audio/video/demuxer buffers, and restart from fresh. Might help with unseekable streams that are going out of sync. This command might be changed or removed in the future.</p>
<dt><code>screenshot-raw [&lt;flags&gt;]</code></p>
<dd>Return a screenshot in memory. This can be used only through the client API. The MPV_FORMAT_NODE_MAP returned by this command has the <code>w</code>, <code>h</code>, <code>stride</code> fields set to obvious contents. The <code>format</code> field is set to <code>bgr0</code> by default. This format is organized as <code>B8G8R8X8</code> (where <code>B</code> is the LSB). The contents of the padding <code>X</code> are undefined. The <code>data</code> field is of type MPV_FORMAT_BYTE_ARRAY with the actual image data. The image is freed as soon as the result mpv_node is freed. As usual with client API semantics, you are not allowed to write to the image data. </p>
<p> The <code>stride</code> is the number of bytes from a pixel at <code>(x0, y0)</code> to the pixel at <code>(x0, y0 + 1)</code>. This can be larger than <code>w * 4</code> if the image was cropped, or if there is padding. This number can be negative as well. You access a pixel with <code>byte_index = y * stride + x * 4</code> (assuming the <code>bgr0</code> format). </p>
<p> The <code>flags</code> argument is like the first argument to <code>screenshot</code> and supports <code>subtitles</code>, <code>video</code>, <code>window</code>.</p>
<dt><code>vf-command &lt;label&gt; &lt;command&gt; &lt;argument&gt;</code></p>
<dd>Send a command to the filter with the given <code>&lt;label&gt;</code>. Use <code>all</code> to send it to all filters at once. The command and argument string is filter specific. Currently, this only works with the <code>lavfi</code> filter &#8211; see the libavfilter documentation for which commands a filter supports. </p>
<p> Note that the <code>&lt;label&gt;</code> is a mpv filter label, not a libavfilter filter name.</p>
<dt><code>af-command &lt;label&gt; &lt;command&gt; &lt;argument&gt;</code></p>
<dd>Same as <code>vf-command</code>, but for audio filters.</p>
<dt><code>apply-profile &lt;name&gt; [&lt;mode&gt;]</code></p>
<dd>Apply the contents of a named profile. This is like using <code>profile=name</code> in a config file, except you can map it to a key binding to change it at runtime. </p>
<p> The mode argument:</p>
<dt><code>default</code></p>
<dd>Apply the profile. Default if the argument is omitted.</p>
<dt><code>restore</code></p>
<dd>Restore options set by a previous <code>apply-profile</code> command for this profile. Only works if the profile has <code>profile-restore</code> set to a relevant mode. Prints a warning if nothing could be done. See <i>Runtime profiles</i> for details.</p>
<dt><code>load-script &lt;filename&gt;</code></p>
<dd>Load a script, similar to the <code>&#8211;script</code> option. Whether this waits for the script to finish initialization or not changed multiple times, and the future behavior is left undefined. </p>
<p> On success, returns a <code>mpv_node</code> with a <code>client_id</code> field set to the return value of the <code>mpv_client_id()</code> API call of the newly created script handle.</p>
<dt><code>change-list &lt;name&gt; &lt;operation&gt; &lt;value&gt;</code></p>
<dd>This command changes list options as described in <i>List Options</i>. The <code>&lt;name&gt;</code> parameter is the normal option name, while <code>&lt;operation&gt;</code> is the suffix or action used on the option. </p>
<p> Some operations take no value, but the command still requires the value parameter. In these cases, the value must be an empty string.</p>
<dt>Example</p>
<dd><code>change-list glsl-shaders append file.glsl</code> </p>
<p> Add a filename to the <code>glsl-shaders</code> list. The command line equivalent is <code>&#8211;glsl-shaders-append=file.glsl</code> or alternatively <code>&#8211;glsl-shader=file.glsl</code>.</p>
<dt><code>dump-cache &lt;start&gt; &lt;end&gt; &lt;filename&gt;</code></p>
<dd>Dump the current cache to the given filename. The <code>&lt;filename&gt;</code> file is overwritten if it already exists. <code>&lt;start&gt;</code> and <code>&lt;end&gt;</code> give the time range of what to dump. If no data is cached at the given time range, nothing may be dumped (creating a file with no packets). </p>
<p> Dumping a larger part of the cache will freeze the player. No effort was made to fix this, as this feature was meant mostly for creating small excerpts. </p>
<p> See <code>&#8211;stream-record</code> for various caveats that mostly apply to this command too, as both use the same underlying code for writing the output file. </p>
<p> If <code>&lt;filename&gt;</code> is an empty string, an ongoing <code>dump-cache</code> is stopped. </p>
<p> If <code>&lt;end&gt;</code> is <code>no</code>, then continuous dumping is enabled. Then, after dumping the existing parts of the cache, anything read from network is appended to the cache as well. This behaves similar to <code>&#8211;stream-record</code> (although it does not conflict with that option, and they can be both active at the same time). </p>
<p> If the <code>&lt;end&gt;</code> time is after the cache, the command will _not_ wait and write newly received data to it. </p>
<p> The end of the resulting file may be slightly damaged or incomplete at the end. (Not enough effort was made to ensure that the end lines up properly.) </p>
<p> Note that this command will finish only once dumping ends. That means it works similar to the <code>screenshot</code> command, just that it can block much longer. If continuous dumping is used, the command will not finish until playback is stopped, an error happens, another <code>dump-cache</code> command is run, or an API like <code>mp.abort_async_command</code> was called to explicitly stop the command. See <i>Synchronous vs. Asynchronous</i>. </p>
<p> <code>NOTE:</code> This was mostly created for network streams. For local files, there may be much better methods to create excerpts and such. There are tons of much more user-friendly Lua scripts, that will reencode parts of a file by spawning a separate instance of <code>ffmpeg</code>. With network streams, this is not that easily possible, as the stream would have to be downloaded again. Even if <code>&#8211;stream-record</code> is used to record the stream to the local filesystem, there may be problems, because the recorded file is still written to. </p>
<p> This command is experimental, and all details about it may change in the future.</p>
<dt><code>ab-loop-dump-cache &lt;filename&gt;</code></p>
<dd>Essentially calls <code>dump-cache</code> with the current AB-loop points as arguments. Like <code>dump-cache</code>, this will overwrite the file at <code>&lt;filename&gt;</code>. Likewise, if the B point is set to <code>no</code>, it will enter continuous dumping after the existing cache was dumped. </p>
<p> The author reserves the right to remove this command if enough motivation is found to move this functionality to a trivial Lua script.</p>
<dt><code>ab-loop-align-cache</code></p>
<dd>Re-adjust the A/B loop points to the start and end within the cache the <code>ab-loop-dump-cache</code> command will (probably) dump. Basically, it aligns the times on keyframes. The guess might be off especially at the end (due to granularity issues due to remuxing). If the cache shrinks in the meantime, the points set by the command will not be the effective parameters either. </p>
<p> This command has an even more uncertain future than <code>ab-loop-dump-cache</code> and might disappear without replacement if the author decides it&#8217;s useless. </p>
<p> Undocumented commands: <code>ao-reload</code> (experimental/internal).</dl>
<h3>List of events</h3>
<p>This is a partial list of events. This section describes what <code>mpv_event_to_node()</code> returns, and which is what scripting APIs and the JSON IPC sees. Note that the C API has separate C-level declarations with <code>mpv_event</code>, which may be slightly different. </p>
<p> Note that events are asynchronous: the player core continues running while events are delivered to scripts and other clients. In some cases, you can hooks to enforce synchronous execution. </p>
<p> All events can have the following fields:</p>
<dl COMPACT>
<dt><code>event</code></p>
<dd>Name as the event (as returned by <code>mpv_event_name()</code>).</p>
<dt><code>id</code></p>
<dd>The <code>reply_userdata</code> field (opaque user value). If <code>reply_userdata</code> is 0, the field is not added.</p>
<dt><code>error</code></p>
<dd>Set to an error string (as returned by <code>mpv_error_string()</code>). This field is missing if no error happened, or the event type does not report error. Most events leave this unset. </p>
<p> This list uses the event name field value, and the C API symbol in brackets:</p>
<dt><code>start-file</code> (<code>MPV_EVENT_START_FILE</code>)</p>
<dd>Happens right before a new file is loaded. When you receive this, the player is loading the file (or possibly already done with it). </p>
<p> This has the following fields:</p>
<dt><code>playlist_entry_id</code></p>
<dd>Playlist entry ID of the file being loaded now.</p>
<dt><code>end-file</code> (<code>MPV_EVENT_END_FILE</code>)</p>
<dd>Happens after a file was unloaded. Typically, the player will load the next file right away, or quit if this was the last file. </p>
<p> The event has the following fields:</p>
<dt><code>reason</code></p>
<dd>Has one of these values:</p>
<dt><code>eof</code></p>
<dd>The file has ended. This can (but doesn&#8217;t have to) include incomplete files or broken network connections under circumstances.</p>
<dt><code>stop</code></p>
<dd>Playback was ended by a command.</p>
<dt><code>quit</code></p>
<dd>Playback was ended by sending the quit command.</p>
<dt><code>error</code></p>
<dd>An error happened. In this case, an <code>error</code> field is present with the error string.</p>
<dt><code>redirect</code></p>
<dd>Happens with playlists and similar. Details see <code>MPV_END_FILE_REASON_REDIRECT</code> in the C API.</p>
<dt><code>unknown</code></p>
<dd>Unknown. Normally doesn&#8217;t happen, unless the Lua API is out of sync with the C API. (Likewise, it could happen that your script gets reason strings that did not exist yet at the time your script was written.)</p>
<dt><code>playlist_entry_id</code></p>
<dd>Playlist entry ID of the file that was being played or attempted to be played. This has the same value as the <code>playlist_entry_id</code> field in the corresponding <code>start-file</code> event.</p>
<dt><code>file_error</code></p>
<dd>Set to mpv error string describing the approximate reason why playback failed. Unset if no error known. (In Lua scripting, this value was set on the <code>error</code> field directly. This is deprecated since mpv 0.33.0. In the future, this <code>error</code> field will be unset for this specific event.)</p>
<dt><code>playlist_insert_id</code></p>
<dd>If loading ended, because the playlist entry to be played was for example a playlist, and the current playlist entry is replaced with a number of other entries. This may happen at least with MPV_END_FILE_REASON_REDIRECT (other event types may use this for similar but different purposes in the future). In this case, playlist_insert_id will be set to the playlist entry ID of the first inserted entry, and playlist_insert_num_entries to the total number of inserted playlist entries. Note this in this specific case, the ID of the last inserted entry is playlist_insert_id+num-1. Beware that depending on circumstances, you may observe the new playlist entries before seeing the event (e.g. reading the &quot;playlist&quot; property or getting a property change notification before receiving the event). If this is 0 in the C API, this field isn&#8217;t added.</p>
<dt><code>playlist_insert_num_entries</code></p>
<dd>See playlist_insert_id. Only present if playlist_insert_id is present.</p>
<dt><code>file-loaded</code> (<code>MPV_EVENT_FILE_LOADED</code>)</p>
<dd>Happens after a file was loaded and begins playback.</p>
<dt><code>seek</code> (<code>MPV_EVENT_SEEK</code>)</p>
<dd>Happens on seeking. (This might include cases when the player seeks internally, even without user interaction. This includes e.g. segment changes when playing ordered chapters Matroska files.)</p>
<dt><code>playback-restart</code> (<code>MPV_EVENT_PLAYBACK_RESTART</code>)</p>
<dd>Start of playback after seek or after file was loaded.</p>
<dt><code>shutdown</code> (<code>MPV_EVENT_SHUTDOWN</code>)</p>
<dd>Sent when the player quits, and the script should terminate. Normally handled automatically. See <i>Details on the script initialization and lifecycle</i>.</p>
<dt><code>log-message</code> (<code>MPV_EVENT_LOG_MESSAGE</code>)</p>
<dd>Receives messages enabled with <code>mpv_request_log_messages()</code> (Lua: <code>mp.enable_messages</code>). </p>
<p> This contains, in addition to the default event fields, the following fields:</p>
<dt><code>prefix</code></p>
<dd>The module prefix, identifies the sender of the message. This is what the terminal player puts in front of the message text when using the <code>&#8211;v</code> option, and is also what is used for <code>&#8211;msg-level</code>.</p>
<dt><code>level</code></p>
<dd>The log level as string. See <code>msg.log</code> for possible log level names. Note that later versions of mpv might add new levels or remove (undocumented) existing ones.</p>
<dt><code>text</code></p>
<dd>The log message. The text will end with a newline character. Sometimes it can contain multiple lines. </p>
<p> Keep in mind that these messages are meant to be hints for humans. You should not parse them, and prefix/level/text of messages might change any time.</p>
<dt><code>hook</code></p>
<dd>The event has the following fields:</p>
<dt><code>hook_id</code></p>
<dd>ID to pass to <code>mpv_hook_continue()</code>. The Lua scripting wrapper provides a better API around this with <code>mp.add_hook()</code>.</p>
<dt><code>get-property-reply</code> (<code>MPV_EVENT_GET_PROPERTY_REPLY</code>)</p>
<dd>See C API.</p>
<dt><code>set-property-reply</code> (<code>MPV_EVENT_SET_PROPERTY_REPLY</code>)</p>
<dd>See C API.</p>
<dt><code>command-reply</code> (<code>MPV_EVENT_COMMAND_REPLY</code>)</p>
<dd>This is one of the commands for which the <code>`error</code> field is meaningful. </p>
<p> JSON IPC and Lua and possibly other backends treat this specially and may not pass the actual event to the user. See C API. </p>
<p> The event has the following fields:</p>
<dt><code>result</code></p>
<dd>The result (on success) of any <code>mpv_node</code> type, if any.</p>
<dt><code>client-message</code> (<code>MPV_EVENT_CLIENT_MESSAGE</code>)</p>
<dd>Lua and possibly other backends treat this specially and may not pass the actual event to the user. </p>
<p> The event has the following fields:</p>
<dt><code>args</code></p>
<dd>Array of strings with the message data.</p>
<dt><code>video-reconfig</code> (<code>MPV_EVENT_VIDEO_RECONFIG</code>)</p>
<dd>Happens on video output or filter reconfig.</p>
<dt><code>audio-reconfig</code> (<code>MPV_EVENT_AUDIO_RECONFIG</code>)</p>
<dd>Happens on audio output or filter reconfig.</p>
<dt><code>property-change</code> (<code>MPV_EVENT_PROPERTY_CHANGE</code>)</p>
<dd>Happens when a property that is being observed changes value. </p>
<p> The event has the following fields:</p>
<dt><code>name</code></p>
<dd>The name of the property.</p>
<dt><code>data</code></p>
<dd>The new value of the property. </p>
<p> The following events also happen, but are deprecated: <code>tracks-changed</code>, <code>track-switched</code>, <code>pause</code>, <code>unpause</code>, <code>metadata-update</code>, <code>idle</code>, <code>tick</code>, <code>chapter-change</code>. Use <code>mpv_observe_property()</code> (Lua: <code>mp.observe_property()</code>) instead.</dl>
<h3>Hooks</h3>
<p>Hooks are synchronous events between player core and a script or similar. This applies to client API (including the Lua scripting interface). Normally, events are supposed to be asynchronous, and the hook API provides an awkward and obscure way to handle events that require stricter coordination. There are no API stability guarantees made. Not following the protocol exactly can make the player freeze randomly. Basically, nobody should use this API. </p>
<p> The C API is described in the header files. The Lua API is described in the Lua section. </p>
<p> Before a hook is actually invoked on an API clients, it will attempt to return new values for all observed properties that were changed before the hook. This may make it easier for an application to set defined &quot;barriers&quot; between property change notifications by registering hooks. (That means these hooks will have an effect, even if you do nothing and make them continue immediately.) </p>
<p> The following hooks are currently defined:</p>
<dl COMPACT>
<dt><code>on_load</code></p>
<dd>Called when a file is to be opened, before anything is actually done. For example, you could read and write the <code>stream-open-filename</code> property to redirect an URL to something else (consider support for streaming sites which rarely give the user a direct media URL), or you could set per-file options with by setting the property <code>file-local-options/&lt;option name&gt;</code>. The player will wait until all hooks are run. </p>
<p> Ordered after <code>start-file</code> and before <code>playback-restart</code>.</p>
<dt><code>on_load_fail</code></p>
<dd>Called after after a file has been opened, but failed to. This can be used to provide a fallback in case native demuxers failed to recognize the file, instead of always running before the native demuxers like <code>on_load</code>. Demux will only be retried if <code>stream-open-filename</code> was changed. If it fails again, this hook is _not_ called again, and loading definitely fails. </p>
<p> Ordered after <code>on_load</code>, and before <code>playback-restart</code> and <code>end-file</code>.</p>
<dt><code>on_preloaded</code></p>
<dd>Called after a file has been opened, and before tracks are selected and decoders are created. This has some usefulness if an API users wants to select tracks manually, based on the set of available tracks. It&#8217;s also useful to initialize <code>&#8211;lavfi-complex</code> in a specific way by API, without having to &quot;probe&quot; the available streams at first. </p>
<p> Note that this does not yet apply default track selection. Which operations exactly can be done and not be done, and what information is available and what is not yet available yet, is all subject to change. </p>
<p> Ordered after <code>on_load_fail</code> etc. and before <code>playback-restart</code>.</p>
<dt><code>on_unload</code></p>
<dd>Run before closing a file, and before actually uninitializing everything. It&#8217;s not possible to resume playback in this state. </p>
<p> Ordered before <code>end-file</code>. Will also happen in the error case (then after <code>on_load_fail</code>).</p>
<dt><code>on_before_start_file</code></p>
<dd>Run before a <code>start-file</code> event is sent. (If any client changes the current playlist entry, or sends a quit command to the player, the corresponding event will not actually happen after the hook returns.) Useful to drain property changes before a new file is loaded.</p>
<dt><code>on_after_end_file</code></p>
<dd>Run after an <code>end-file</code> event. Useful to drain property changes after a file has finished.</dl>
<h3>Input Command Prefixes</h3>
<p>These prefixes are placed between key name and the actual command. Multiple prefixes can be specified. They are separated by whitespace.</p>
<dl COMPACT>
<dt><code>osd-auto</code></p>
<dd>Use the default behavior for this command. This is the default for <code>input.conf</code> commands. Some libmpv/scripting/IPC APIs do not use this as default, but use <code>no-osd</code> instead.</p>
<dt><code>no-osd</code></p>
<dd>Do not use any OSD for this command.</p>
<dt><code>osd-bar</code></p>
<dd>If possible, show a bar with this command. Seek commands will show the progress bar, property changing commands may show the newly set value.</p>
<dt><code>osd-msg</code></p>
<dd>If possible, show an OSD message with this command. Seek command show the current playback time, property changing commands show the newly set value as text.</p>
<dt><code>osd-msg-bar</code></p>
<dd>Combine osd-bar and osd-msg.</p>
<dt><code>raw</code></p>
<dd>Do not expand properties in string arguments. (Like <code>&quot;${property-name}&quot;</code>.) This is the default for some libmpv/scripting/IPC APIs.</p>
<dt><code>expand-properties</code></p>
<dd>All string arguments are expanded as described in <i>Property Expansion</i>. This is the default for <code>input.conf</code> commands.</p>
<dt><code>repeatable</code></p>
<dd>For some commands, keeping a key pressed doesn&#8217;t run the command repeatedly. This prefix forces enabling key repeat in any case. For a list of commands: the first command determines the repeatability of the whole list (up to and including version 0.33 &#8211; a list was always repeatable).</p>
<dt><code>async</code></p>
<dd>Allow asynchronous execution (if possible). Note that only a few commands will support this (usually this is explicitly documented). Some commands are asynchronous by default (or rather, their effects might manifest after completion of the command). The semantics of this flag might change in the future. Set it only if you don&#8217;t rely on the effects of this command being fully realized when it returns. See <i>Synchronous vs. Asynchronous</i>.</p>
<dt><code>sync</code></p>
<dd>Allow synchronous execution (if possible). Normally, all commands are synchronous by default, but some are asynchronous by default for compatibility with older behavior. </p>
<p> All of the osd prefixes are still overridden by the global <code>&#8211;osd-level</code> settings.</dl>
<h3>Synchronous vs. Asynchronous</h3>
<p>The <code>async</code> and <code>sync</code> prefix matter only for how the issuer of the command waits on the completion of the command. Normally it does not affect how the command behaves by itself. There are the following cases:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Normal input.conf commands are always run asynchronously. Slow running commands are queued up or run in parallel.</p>
<dt>&bull;</p>
<dd>&quot;Multi&quot; input.conf commands (1 key binding, concatenated with <code>;</code>) will be executed in order, except for commands that are async (either prefixed with <code>async</code>, or async by default for some commands). The async commands are run in a detached manner, possibly in parallel to the remaining sync commands in the list.</p>
<dt>&bull;</p>
<dd>Normal Lua and libmpv commands (e.g. <code>mpv_command()</code>) are run in a blocking manner, unless the <code>async</code> prefix is used, or the command is async by default. This means in the sync case the caller will block, even if the core continues playback. Async mode runs the command in a detached manner.</p>
<dt>&bull;</p>
<dd>Async libmpv command API (e.g. <code>mpv_command_async()</code>) never blocks the caller, and always notify their completion with a message. The <code>sync</code> and <code>async</code> prefixes make no difference.</p>
<dt>&bull;</p>
<dd>Lua also provides APIs for running async commands, which behave similar to the C counterparts.</p>
<dt>&bull;</p>
<dd>In all cases, async mode can still run commands in a synchronous manner, even in detached mode. This can for example happen in cases when a command does not have an asynchronous implementation. The async libmpv API still never blocks the caller in these cases. </p>
<p> Before mpv 0.29.0, the <code>async</code> prefix was only used by screenshot commands, and made them run the file saving code in a detached manner. This is the default now, and <code>async</code> changes behavior only in the ways mentioned above. </p>
<p> Currently the following commands have different waiting characteristics with sync vs. async: sub-add, audio-add, sub-reload, audio-reload, rescan-external-files, screenshot, screenshot-to-file, dump-cache, ab-loop-dump-cache.</dl>
<h3>Asynchronous command details</h3>
<p>On the API level, every asynchronous command is bound to the context which started it. For example, an asynchronous command started by <code>mpv_command_async</code> is bound to the <code>mpv_handle</code> passed to the function. Only this <code>mpv_handle</code> receives the completion notification (<code>MPV_EVENT_COMMAND_REPLY</code>), and only this handle can abort a still running command directly. If the <code>mpv_handle</code> is destroyed, any still running async. commands started by it are terminated. </p>
<p> The scripting APIs and JSON IPC give each script/connection its own implicit <code>mpv_handle</code>. </p>
<p> If the player is closed, the core may abort all pending async. commands on its own (like a forced <code>mpv_abort_async_command()</code> call for each pending command on behalf of the API user). This happens at the same time <code>MPV_EVENT_SHUTDOWN</code> is sent, and there is no way to prevent this.</p>
<h3>Input Sections</h3>
<p>Input sections group a set of bindings, and enable or disable them at once. In <code>input.conf</code>, each key binding is assigned to an input section, rather than actually having explicit text sections. </p>
<p> See also: <code>enable-section</code> and <code>disable-section</code> commands. </p>
<p> Predefined bindings:</p>
<dl COMPACT>
<dt><code>default</code></p>
<dd>Bindings without input section are implicitly assigned to this section. It is enabled by default during normal playback.</p>
<dt><code>encode</code></p>
<dd>Section which is active in encoding mode. It is enabled exclusively, so that bindings in the <code>default</code> sections are ignored.</dl>
<h3>Properties</h3>
<p>Properties are used to set mpv options during runtime, or to query arbitrary information. They can be manipulated with the <code>set</code>/<code>add</code>/<code>cycle</code> commands, and retrieved with <code>show-text</code>, or anything else that uses property expansion. (See <i>Property Expansion</i>.) </p>
<p> The property name is annotated with RW to indicate whether the property is generally writable. </p>
<p> If an option is referenced, the property will normally take/return exactly the same values as the option. In these cases, properties are merely a way to change an option at runtime.</p>
<h3>Property list</h3>
<p><code>NOTE:</code> Most options can be set as runtime via properties as well. Just remove the leading <code>&#8212;</code> from the option name. These are not documented below, see <i>OPTIONS</i> instead. Only properties which do not exist as option with the same name, or which have very different behavior from the options are documented below. </p>
<p> Properties marked as (RW) are writeable, while those that aren&#8217;t are read-only.</p>
<dl COMPACT>
<dt><code>audio-speed-correction</code>, <code>video-speed-correction</code></p>
<dd>Factor multiplied with <code>speed</code> at which the player attempts to play the file. Usually it&#8217;s exactly 1. (Display sync mode will make this useful.) </p>
<p> OSD formatting will display it in the form of <code>+1.23456%</code>, with the number being <code>(raw &#8211; 1) * 100</code> for the given raw property value.</p>
<dt><code>display-sync-active</code></p>
<dd>Whether <code>&#8211;video-sync=display</code> is actually active.</p>
<dt><code>filename</code></p>
<dd>Currently played file, with path stripped. If this is an URL, try to undo percent encoding as well. (The result is not necessarily correct, but looks better for display purposes. Use the <code>path</code> property to get an unmodified filename.) </p>
<p> This has a sub-property:</p>
<dt><code>filename/no-ext</code></p>
<dd>Like the <code>filename</code> property, but if the text contains a <code>.</code>, strip all text after the last <code>.</code>. Usually this removes the file extension.</p>
<dt><code>file-size</code></p>
<dd>Length in bytes of the source file/stream. (This is the same as <code>${stream-end}</code>. For segmented/multi-part files, this will return the size of the main or manifest file, whatever it is.)</p>
<dt><code>estimated-frame-count</code></p>
<dd>Total number of frames in current file. </p>
<p> <code>NOTE:</code> This is only an estimate. (It&#8217;s computed from two unreliable quantities: fps and stream length.)</p>
<dt><code>estimated-frame-number</code></p>
<dd>Number of current frame in current stream. </p>
<p> <code>NOTE:</code> This is only an estimate. (It&#8217;s computed from two unreliable quantities: fps and possibly rounded timestamps.)</p>
<dt><code>pid</code></p>
<dd>Process-id of mpv.</p>
<dt><code>path</code></p>
<dd>Full path of the currently played file. Usually this is exactly the same string you pass on the mpv command line or the <code>loadfile</code> command, even if it&#8217;s a relative path. If you expect an absolute path, you will have to determine it yourself, for example by using the <code>working-directory</code> property.</p>
<dt><code>stream-open-filename</code></p>
<dd>The full path to the currently played media. This is different from <code>path</code> only in special cases. In particular, if <code>&#8211;ytdl=yes</code> is used, and the URL is detected by <code>youtube-dl</code>, then the script will set this property to the actual media URL. This property should be set only during the <code>on_load</code> or <code>on_load_fail</code> hooks, otherwise it will have no effect (or may do something implementation defined in the future). The property is reset if playback of the current media ends.</p>
<dt><code>media-title</code></p>
<dd>If the currently played file has a <code>title</code> tag, use that. </p>
<p> Otherwise, return the <code>filename</code> property.</p>
<dt><code>file-format</code></p>
<dd>Symbolic name of the file format. In some cases, this is a comma-separated list of format names, e.g. mp4 is <code>mov,mp4,m4a,3gp,3g2,mj2</code> (the list may grow in the future for any format).</p>
<dt><code>current-demuxer</code></p>
<dd>Name of the current demuxer. (This is useless.) </p>
<p> (Renamed from <code>demuxer</code>.)</p>
<dt><code>stream-path</code></p>
<dd>Filename (full path) of the stream layer filename. (This is probably useless and is almost never different from <code>path</code>.)</p>
<dt><code>stream-pos</code></p>
<dd>Raw byte position in source stream. Technically, this returns the position of the most recent packet passed to a decoder.</p>
<dt><code>stream-end</code></p>
<dd>Raw end position in bytes in source stream.</p>
<dt><code>duration</code></p>
<dd>Duration of the current file in seconds. If the duration is unknown, the property is unavailable. Note that the file duration is not always exactly known, so this is an estimate. </p>
<p> This replaces the <code>length</code> property, which was deprecated after the mpv 0.9 release. (The semantics are the same.)</p>
<dt><code>avsync</code></p>
<dd>Last A/V synchronization difference. Unavailable if audio or video is disabled.</p>
<dt><code>total-avsync-change</code></p>
<dd>Total A-V sync correction done. Unavailable if audio or video is disabled.</p>
<dt><code>decoder-frame-drop-count</code></p>
<dd>Video frames dropped by decoder, because video is too far behind audio (when using <code>&#8211;framedrop=decoder</code>). Sometimes, this may be incremented in other situations, e.g. when video packets are damaged, or the decoder doesn&#8217;t follow the usual rules. Unavailable if video is disabled. </p>
<p> <code>drop-frame-count</code> is a deprecated alias.</p>
<dt><code>frame-drop-count</code></p>
<dd>Frames dropped by VO (when using <code>&#8211;framedrop=vo</code>). </p>
<p> <code>vo-drop-frame-count</code> is a deprecated alias.</p>
<dt><code>mistimed-frame-count</code></p>
<dd>Number of video frames that were not timed correctly in display-sync mode for the sake of keeping A/V sync. This does not include external circumstances, such as video rendering being too slow or the graphics driver somehow skipping a vsync. It does not include rounding errors either (which can happen especially with bad source timestamps). For example, using the <code>display-desync</code> mode should never change this value from 0.</p>
<dt><code>vsync-ratio</code></p>
<dd>For how many vsyncs a frame is displayed on average. This is available if display-sync is active only. For 30 FPS video on a 60 Hz screen, this will be 2. This is the moving average of what actually has been scheduled, so 24 FPS on 60 Hz will never remain exactly on 2.5, but jitter depending on the last frame displayed.</p>
<dt><code>vo-delayed-frame-count</code></p>
<dd>Estimated number of frames delayed due to external circumstances in display-sync mode. Note that in general, mpv has to guess that this is happening, and the guess can be inaccurate.</p>
<dt><code>percent-pos</code> (RW)</p>
<dd>Position in current file (0-100). The advantage over using this instead of calculating it out of other properties is that it properly falls back to estimating the playback position from the byte position, if the file duration is not known.</p>
<dt><code>time-pos</code> (RW)</p>
<dd>Position in current file in seconds.</p>
<dt><code>time-start</code></p>
<dd>Deprecated. Always returns 0. Before mpv 0.14, this used to return the start time of the file (could affect e.g. transport streams). See <code>&#8211;rebase-start-time</code> option.</p>
<dt><code>time-remaining</code></p>
<dd>Remaining length of the file in seconds. Note that the file duration is not always exactly known, so this is an estimate.</p>
<dt><code>audio-pts</code></p>
<dd>Current audio playback position in current file in seconds. Unlike time-pos, this updates more often than once per frame. For audio-only files, it is mostly equivalent to time-pos, while for video-only files this property is not available.</p>
<dt><code>playtime-remaining</code></p>
<dd><code>time-remaining</code> scaled by the current <code>speed</code>.</p>
<dt><code>playback-time</code> (RW)</p>
<dd>Position in current file in seconds. Unlike <code>time-pos</code>, the time is clamped to the range of the file. (Inaccurate file durations etc. could make it go out of range. Useful on attempts to seek outside of the file, as the seek target time is considered the current position during seeking.)</p>
<dt><code>chapter</code> (RW)</p>
<dd>Current chapter number. The number of the first chapter is 0.</p>
<dt><code>edition</code> (RW)</p>
<dd>Current MKV edition number. Setting this property to a different value will restart playback. The number of the first edition is 0. </p>
<p> Before mpv 0.31.0, this showed the actual edition selected at runtime, if you didn&#8217;t set the option or property manually. With mpv 0.31.0 and later, this strictly returns the user-set option or property value, and the <code>current-edition</code> property was added to return the runtime selected edition (this matters with <code>&#8211;edition=auto</code>, the default).</p>
<dt><code>current-edition</code></p>
<dd>Currently selected edition. This property is unavailable if no file is loaded, or the file has no editions. (Matroska files make a difference between having no editions and a single edition, which will be reflected by the property, although in practice it does not matter.)</p>
<dt><code>chapters</code></p>
<dd>Number of chapters.</p>
<dt><code>editions</code></p>
<dd>Number of MKV editions.</p>
<dt><code>edition-list</code></p>
<dd>List of editions, current entry marked. Currently, the raw property value is useless. </p>
<p> This has a number of sub-properties. Replace <code>N</code> with the 0-based edition index.</p>
<dt><code>edition-list/count</code></p>
<dd>Number of editions. If there are no editions, this can be 0 or 1 (1 if there&#8217;s a useless dummy edition).</p>
<dt><code>edition-list/N/id</code> (RW)</p>
<dd>Edition ID as integer. Use this to set the <code>edition</code> property. Currently, this is the same as the edition index.</p>
<dt><code>edition-list/N/default</code></p>
<dd>Whether this is the default edition.</p>
<dt><code>edition-list/N/title</code></p>
<dd>Edition title as stored in the file. Not always available. </p>
<p> When querying the property with the client API using <code>MPV_FORMAT_NODE</code>, or with Lua <code>mp.get_property_native</code>, this will return a mpv_node with the following contents: </p>
<pre>MPV_FORMAT_NODE_ARRAY
 MPV_FORMAT_NODE_MAP (for each edition)
 &quot;id&quot; MPV_FORMAT_INT64
 &quot;title&quot; MPV_FORMAT_STRING
 &quot;default&quot; MPV_FORMAT_FLAG</pre>
<dt><code>metadata</code></p>
<dd>Metadata key/value pairs. </p>
<p> If the property is accessed with Lua&#8217;s <code>mp.get_property_native</code>, this returns a table with metadata keys mapping to metadata values. If it is accessed with the client API, this returns a <code>MPV_FORMAT_NODE_MAP</code>, with tag keys mapping to tag values. </p>
<p> For OSD, it returns a formatted list. Trying to retrieve this property as a raw string doesn&#8217;t work. </p>
<p> This has a number of sub-properties:</p>
<dt><code>metadata/by-key/&lt;key&gt;</code></p>
<dd>Value of metadata entry <code>&lt;key&gt;</code>.</p>
<dt><code>metadata/list/count</code></p>
<dd>Number of metadata entries.</p>
<dt><code>metadata/list/N/key</code></p>
<dd>Key name of the Nth metadata entry. (The first entry is <code>0</code>).</p>
<dt><code>metadata/list/N/value</code></p>
<dd>Value of the Nth metadata entry.</p>
<dt><code>metadata/&lt;key&gt;</code></p>
<dd>Old version of <code>metadata/by-key/&lt;key&gt;</code>. Use is discouraged, because the metadata key string could conflict with other sub-properties. </p>
<p> The layout of this property might be subject to change. Suggestions are welcome how exactly this property should work. </p>
<p> When querying the property with the client API using <code>MPV_FORMAT_NODE</code>, or with Lua <code>mp.get_property_native</code>, this will return a mpv_node with the following contents: </p>
<pre>MPV_FORMAT_NODE_MAP
 (key and string value for each metadata entry)</pre>
<dt><code>filtered-metadata</code></p>
<dd>Like <code>metadata</code>, but includes only fields listed in the <code>&#8211;display-tags</code> option. This is the same set of tags that is printed to the terminal.</p>
<dt><code>chapter-metadata</code></p>
<dd>Metadata of current chapter. Works similar to <code>metadata</code> property. It also allows the same access methods (using sub-properties). </p>
<p> Per-chapter metadata is very rare. Usually, only the chapter name (<code>title</code>) is set. </p>
<p> For accessing other information, like chapter start, see the <code>chapter-list</code> property.</p>
<dt><code>vf-metadata/&lt;filter-label&gt;</code></p>
<dd>Metadata added by video filters. Accessed by the filter label, which, if not explicitly specified using the <code>@filter-label:</code> syntax, will be <code>&lt;filter-name&gt;NN</code>. </p>
<p> Works similar to <code>metadata</code> property. It allows the same access methods (using sub-properties). </p>
<p> An example of this kind of metadata are the cropping parameters added by <code>&#8211;vf=lavfi=cropdetect</code>.</p>
<dt><code>af-metadata/&lt;filter-label&gt;</code></p>
<dd>Equivalent to <code>vf-metadata/&lt;filter-label&gt;</code>, but for audio filters.</p>
<dt><code>idle-active</code></p>
<dd>Returns <code>yes</code>/true if no file is loaded, but the player is staying around because of the <code>&#8211;idle</code> option. </p>
<p> (Renamed from <code>idle</code>.)</p>
<dt><code>core-idle</code></p>
<dd>Whether the playback core is paused. This can differ from <code>pause</code> in special situations, such as when the player pauses itself due to low network cache. </p>
<p> This also returns <code>yes</code>/true if playback is restarting or if nothing is playing at all. In other words, it&#8217;s only <code>no</code>/false if there&#8217;s actually video playing. (Behavior since mpv 0.7.0.)</p>
<dt><code>cache-speed</code></p>
<dd>Current I/O read speed between the cache and the lower layer (like network). This gives the number bytes per seconds over a 1 second window (using the type <code>MPV_FORMAT_INT64</code> for the client API). </p>
<p> This is the same as <code>demuxer-cache-state/raw-input-rate</code>.</p>
<dt><code>demuxer-cache-duration</code></p>
<dd>Approximate duration of video buffered in the demuxer, in seconds. The guess is very unreliable, and often the property will not be available at all, even if data is buffered.</p>
<dt><code>demuxer-cache-time</code></p>
<dd>Approximate time of video buffered in the demuxer, in seconds. Same as <code>demuxer-cache-duration</code> but returns the last timestamp of buffered data in demuxer.</p>
<dt><code>demuxer-cache-idle</code></p>
<dd>Whether the demuxer is idle, which means that the demuxer cache is filled to the requested amount, and is currently not reading more data.</p>
<dt><code>demuxer-cache-state</code></p>
<dd>Each entry in <code>seekable-ranges</code> represents a region in the demuxer cache that can be seeked to, with a <code>start</code> and <code>end</code> fields containing the respective timestamps. If there are multiple demuxers active, this only returns information about the &quot;main&quot; demuxer, but might be changed in future to return unified information about all demuxers. The ranges are in arbitrary order. Often, ranges will overlap for a bit, before being joined. In broken corner cases, ranges may overlap all over the place. </p>
<p> The end of a seek range is usually smaller than the value returned by the <code>demuxer-cache-time</code> property, because that property returns the guessed buffering amount, while the seek ranges represent the buffered data that can actually be used for cached seeking. </p>
<p> <code>bof-cached</code> indicates whether the seek range with the lowest timestamp points to the beginning of the stream (BOF). This implies you cannot seek before this position at all. <code>eof-cached</code> indicates whether the seek range with the highest timestamp points to the end of the stream (EOF). If both <code>bof-cached</code> and <code>eof-cached</code> are true, and there&#8217;s only 1 cache range, the entire stream is cached. </p>
<p> <code>fw-bytes</code> is the number of bytes of packets buffered in the range starting from the current decoding position. This is a rough estimate (may not account correctly for various overhead), and stops at the demuxer position (it ignores seek ranges after it). </p>
<p> <code>file-cache-bytes</code> is the number of bytes stored in the file cache. This includes all overhead, and possibly unused data (like pruned data). This member is missing if the file cache wasn&#8217;t enabled with <code>&#8211;cache-on-disk=yes</code>. </p>
<p> <code>cache-end</code> is <code>demuxer-cache-time</code>. Missing if unavailable. </p>
<p> <code>reader-pts</code> is the approximate timestamp of the start of the buffered range. Missing if unavailable. </p>
<p> <code>cache-duration</code> is <code>demuxer-cache-duration</code>. Missing if unavailable. </p>
<p> <code>raw-input-rate</code> is the estimated input rate of the network layer (or any other byte-oriented input layer) in bytes per second. May be inaccurate or missing. </p>
<p> When querying the property with the client API using <code>MPV_FORMAT_NODE</code>, or with Lua <code>mp.get_property_native</code>, this will return a mpv_node with the following contents: </p>
<pre>MPV_FORMAT_NODE_MAP
 &quot;seekable-ranges&quot; MPV_FORMAT_NODE_ARRAY
 MPV_FORMAT_NODE_MAP
 &quot;start&quot; MPV_FORMAT_DOUBLE
 &quot;end&quot; MPV_FORMAT_DOUBLE
 &quot;bof-cached&quot; MPV_FORMAT_FLAG
 &quot;eof-cached&quot; MPV_FORMAT_FLAG
 &quot;fw-bytes&quot; MPV_FORMAT_INT64
 &quot;file-cache-bytes&quot; MPV_FORMAT_INT64
 &quot;cache-end&quot; MPV_FORMAT_DOUBLE
 &quot;reader-pts&quot; MPV_FORMAT_DOUBLE
 &quot;cache-duration&quot; MPV_FORMAT_DOUBLE
 &quot;raw-input-rate&quot; MPV_FORMAT_INT64</pre>
<p>Other fields (might be changed or removed in the future):</p>
<dt><code>eof</code></p>
<dd>Whether the reader thread has hit the end of the file.</p>
<dt><code>underrun</code></p>
<dd>Whether the reader thread could not satisfy a decoder&#8217;s request for a new packet.</p>
<dt><code>idle</code></p>
<dd>Whether the thread is currently not reading.</p>
<dt><code>total-bytes</code></p>
<dd>Sum of packet bytes (plus some overhead estimation) of the entire packet queue, including cached seekable ranges.</p>
<dt><code>demuxer-via-network</code></p>
<dd>Whether the stream demuxed via the main demuxer is most likely played via network. What constitutes &quot;network&quot; is not always clear, might be used for other types of untrusted streams, could be wrong in certain cases, and its definition might be changing. Also, external files (like separate audio files or streams) do not influence the value of this property (currently).</p>
<dt><code>demuxer-start-time</code></p>
<dd>The start time reported by the demuxer in fractional seconds.</p>
<dt><code>paused-for-cache</code></p>
<dd>Whether playback is paused because of waiting for the cache.</p>
<dt><code>cache-buffering-state</code></p>
<dd>The percentage (0-100) of the cache fill status until the player will unpause (related to <code>paused-for-cache</code>).</p>
<dt><code>eof-reached</code></p>
<dd>Whether the end of playback was reached. Note that this is usually interesting only if <code>&#8211;keep-open</code> is enabled, since otherwise the player will immediately play the next file (or exit or enter idle mode), and in these cases the <code>eof-reached</code> property will logically be cleared immediately after it&#8217;s set.</p>
<dt><code>seeking</code></p>
<dd>Whether the player is currently seeking, or otherwise trying to restart playback. (It&#8217;s possible that it returns <code>yes</code>/true while a file is loaded. This is because the same underlying code is used for seeking and resyncing.)</p>
<dt><code>mixer-active</code></p>
<dd>Whether the audio mixer is active. </p>
<p> This option is relatively useless. Before mpv 0.18.1, it could be used to infer behavior of the <code>volume</code> property.</p>
<dt><code>ao-volume</code> (RW)</p>
<dd>System volume. This property is available only if mpv audio output is currently active, and only if the underlying implementation supports volume control. What this option does depends on the API. For example, on ALSA this usually changes system-wide audio, while with PulseAudio this controls per-application volume.</p>
<dt><code>ao-mute</code> (RW)</p>
<dd>Similar to <code>ao-volume</code>, but controls the mute state. May be unimplemented even if <code>ao-volume</code> works.</p>
<dt><code>audio-codec</code></p>
<dd>Audio codec selected for decoding.</p>
<dt><code>audio-codec-name</code></p>
<dd>Audio codec.</p>
<dt><code>audio-params</code></p>
<dd>Audio format as output by the audio decoder. This has a number of sub-properties:</p>
<dt><code>audio-params/format</code></p>
<dd>The sample format as string. This uses the same names as used in other places of mpv.</p>
<dt><code>audio-params/samplerate</code></p>
<dd>Samplerate.</p>
<dt><code>audio-params/channels</code></p>
<dd>The channel layout as a string. This is similar to what the <code>&#8211;audio-channels</code> accepts.</p>
<dt><code>audio-params/hr-channels</code></p>
<dd>As <code>channels</code>, but instead of the possibly cryptic actual layout sent to the audio device, return a hopefully more human readable form. (Usually only <code>audio-out-params/hr-channels</code> makes sense.)</p>
<dt><code>audio-params/channel-count</code></p>
<dd>Number of audio channels. This is redundant to the <code>channels</code> field described above. </p>
<p> When querying the property with the client API using <code>MPV_FORMAT_NODE</code>, or with Lua <code>mp.get_property_native</code>, this will return a mpv_node with the following contents: </p>
<pre>MPV_FORMAT_NODE_MAP
 &quot;format&quot; MPV_FORMAT_STRING
 &quot;samplerate&quot; MPV_FORMAT_INT64
 &quot;channels&quot; MPV_FORMAT_STRING
 &quot;channel-count&quot; MPV_FORMAT_INT64
 &quot;hr-channels&quot; MPV_FORMAT_STRING</pre>
<dt><code>audio-out-params</code></p>
<dd>Same as <code>audio-params</code>, but the format of the data written to the audio API.</p>
<dt><code>colormatrix</code></p>
<dd>Redirects to <code>video-params/colormatrix</code>. This parameter (as well as similar ones) can be overridden with the <code>format</code> video filter.</p>
<dt><code>colormatrix-input-range</code></p>
<dd>See <code>colormatrix</code>.</p>
<dt><code>colormatrix-primaries</code></p>
<dd>See <code>colormatrix</code>.</p>
<dt><code>hwdec</code> (RW)</p>
<dd>Reflects the <code>&#8211;hwdec</code> option. </p>
<p> Writing to it may change the currently used hardware decoder, if possible. (Internally, the player may reinitialize the decoder, and will perform a seek to refresh the video properly.) You can watch the other hwdec properties to see whether this was successful. </p>
<p> Unlike in mpv 0.9.x and before, this does not return the currently active hardware decoder. Since mpv 0.18.0, <code>hwdec-current</code> is available for this purpose.</p>
<dt><code>hwdec-current</code></p>
<dd>The current hardware decoding in use. If decoding is active, return one of the values used by the <code>hwdec</code> option/property. <code>no</code>/false indicates software decoding. If no decoder is loaded, the property is unavailable.</p>
<dt><code>hwdec-interop</code></p>
<dd>This returns the currently loaded hardware decoding/output interop driver. This is known only once the VO has opened (and possibly later). With some VOs (like <code>gpu</code>), this might be never known in advance, but only when the decoder attempted to create the hw decoder successfully. (Using <code>&#8211;gpu-hwdec-interop</code> can load it eagerly.) If there are multiple drivers loaded, they will be separated by <code>,</code>. </p>
<p> If no VO is active or no interop driver is known, this property is unavailable. </p>
<p> This does not necessarily use the same values as <code>hwdec</code>. There can be multiple interop drivers for the same hardware decoder, depending on platform and VO.</p>
<dt><code>video-format</code></p>
<dd>Video format as string.</p>
<dt><code>video-codec</code></p>
<dd>Video codec selected for decoding.</p>
<dt><code>width</code>, <code>height</code></p>
<dd>Video size. This uses the size of the video as decoded, or if no video frame has been decoded yet, the (possibly incorrect) container indicated size.</p>
<dt><code>video-params</code></p>
<dd>Video parameters, as output by the decoder (with overrides like aspect etc. applied). This has a number of sub-properties:</p>
<dt><code>video-params/pixelformat</code></p>
<dd>The pixel format as string. This uses the same names as used in other places of mpv.</p>
<dt><code>video-params/hw-pixelformat</code></p>
<dd>The underlying pixel format as string. This is relevant for some cases of hardware decoding and unavailable otherwise.</p>
<dt><code>video-params/average-bpp</code></p>
<dd>Average bits-per-pixel as integer. Subsampled planar formats use a different resolution, which is the reason this value can sometimes be odd or confusing. Can be unavailable with some formats.</p>
<dt><code>video-params/w</code>, <code>video-params/h</code></p>
<dd>Video size as integers, with no aspect correction applied.</p>
<dt><code>video-params/dw</code>, <code>video-params/dh</code></p>
<dd>Video size as integers, scaled for correct aspect ratio.</p>
<dt><code>video-params/aspect</code></p>
<dd>Display aspect ratio as float.</p>
<dt><code>video-params/par</code></p>
<dd>Pixel aspect ratio.</p>
<dt><code>video-params/colormatrix</code></p>
<dd>The colormatrix in use as string. (Exact values subject to change.)</p>
<dt><code>video-params/colorlevels</code></p>
<dd>The colorlevels as string. (Exact values subject to change.)</p>
<dt><code>video-params/primaries</code></p>
<dd>The primaries in use as string. (Exact values subject to change.)</p>
<dt><code>video-params/gamma</code></p>
<dd>The gamma function in use as string. (Exact values subject to change.)</p>
<dt><code>video-params/sig-peak</code></p>
<dd>The video file&#8217;s tagged signal peak as float.</p>
<dt><code>video-params/light</code></p>
<dd>The light type in use as a string. (Exact values subject to change.)</p>
<dt><code>video-params/chroma-location</code></p>
<dd>Chroma location as string. (Exact values subject to change.)</p>
<dt><code>video-params/rotate</code></p>
<dd>Intended display rotation in degrees (clockwise).</p>
<dt><code>video-params/stereo-in</code></p>
<dd>Source file stereo 3D mode. (See the <code>format</code> video filter&#8217;s <code>stereo-in</code> option.)</p>
<dt><code>video-params/alpha</code></p>
<dd>Alpha type. If the format has no alpha channel, this will be unavailable (but in future releases, it could change to <code>no</code>). If alpha is present, this is set to <code>straight</code> or <code>premul</code>. </p>
<p> When querying the property with the client API using <code>MPV_FORMAT_NODE</code>, or with Lua <code>mp.get_property_native</code>, this will return a mpv_node with the following contents: </p>
<pre>MPV_FORMAT_NODE_MAP
 &quot;pixelformat&quot; MPV_FORMAT_STRING
 &quot;hw-pixelformat&quot; MPV_FORMAT_STRING
 &quot;w&quot; MPV_FORMAT_INT64
 &quot;h&quot; MPV_FORMAT_INT64
 &quot;dw&quot; MPV_FORMAT_INT64
 &quot;dh&quot; MPV_FORMAT_INT64
 &quot;aspect&quot; MPV_FORMAT_DOUBLE
 &quot;par&quot; MPV_FORMAT_DOUBLE
 &quot;colormatrix&quot; MPV_FORMAT_STRING
 &quot;colorlevels&quot; MPV_FORMAT_STRING
 &quot;primaries&quot; MPV_FORMAT_STRING
 &quot;gamma&quot; MPV_FORMAT_STRING
 &quot;sig-peak&quot; MPV_FORMAT_DOUBLE
 &quot;light&quot; MPV_FORMAT_STRING
 &quot;chroma-location&quot; MPV_FORMAT_STRING
 &quot;rotate&quot; MPV_FORMAT_INT64
 &quot;stereo-in&quot; MPV_FORMAT_STRING
 &quot;average-bpp&quot; MPV_FORMAT_INT64
 &quot;alpha&quot; MPV_FORMAT_STRING</pre>
<dt><code>dwidth</code>, <code>dheight</code></p>
<dd>Video display size. This is the video size after filters and aspect scaling have been applied. The actual video window size can still be different from this, e.g. if the user resized the video window manually. </p>
<p> These have the same values as <code>video-out-params/dw</code> and <code>video-out-params/dh</code>.</p>
<dt><code>video-dec-params</code></p>
<dd>Exactly like <code>video-params</code>, but no overrides applied.</p>
<dt><code>video-out-params</code></p>
<dd>Same as <code>video-params</code>, but after video filters have been applied. If there are no video filters in use, this will contain the same values as <code>video-params</code>. Note that this is still not necessarily what the video window uses, since the user can change the window size, and all real VOs do their own scaling independently from the filter chain. </p>
<p> Has the same sub-properties as <code>video-params</code>.</p>
<dt><code>video-frame-info</code></p>
<dd>Approximate information of the current frame. Note that if any of these are used on OSD, the information might be off by a few frames due to OSD redrawing and frame display being somewhat disconnected, and you might have to pause and force a redraw. </p>
<p> This has a number of sub-properties:</p>
<dt><code>video-frame-info/picture-type</code></p>
<dd>The type of the picture. It can be &quot;I&quot; (intra), &quot;P&quot; (predicted), &quot;B&quot; (bi-dir predicted) or unavailable.</p>
<dt><code>video-frame-info/interlaced</code></p>
<dd>Whether the content of the frame is interlaced.</p>
<dt><code>video-frame-info/tff</code></p>
<dd>If the content is interlaced, whether the top field is displayed first.</p>
<dt><code>video-frame-info/repeat</code></p>
<dd>Whether the frame must be delayed when decoding.</p>
<dt><code>container-fps</code></p>
<dd>Container FPS. This can easily contain bogus values. For videos that use modern container formats or video codecs, this will often be incorrect. </p>
<p> (Renamed from <code>fps</code>.)</p>
<dt><code>estimated-vf-fps</code></p>
<dd>Estimated/measured FPS of the video filter chain output. (If no filters are used, this corresponds to decoder output.) This uses the average of the 10 past frame durations to calculate the FPS. It will be inaccurate if frame-dropping is involved (such as when framedrop is explicitly enabled, or after precise seeking). Files with imprecise timestamps (such as Matroska) might lead to unstable results.</p>
<dt><code>window-scale</code> (RW)</p>
<dd>Window size multiplier. Setting this will resize the video window to the values contained in <code>dwidth</code> and <code>dheight</code> multiplied with the value set with this property. Setting <code>1</code> will resize to original video size (or to be exact, the size the video filters output). <code>2</code> will set the double size, <code>0.5</code> halves the size. </p>
<p> Note that setting a value identical to its previous value will not resize the window. That&#8217;s because this property mirrors the <code>window-scale</code> option, and setting an option to its previous value is ignored. If this value is set while the window is in a fullscreen, the multiplier is not applied until the window is taken out of that state. Writing this property to a maximized window can unmaximize the window depending on the OS and window manager. If the window does not unmaximize, the multiplier will be applied if the user unmaximizes the window later. </p>
<p> See <code>current-window-scale</code> for the value derived from the actual window size. </p>
<p> Since mpv 0.31.0, this always returns the previously set value (or the default value), instead of the value implied by the actual window size. Before mpv 0.31.0, this returned what <code>current-window-scale</code> returns now, after the window was created.</p>
<dt><code>current-window-scale</code> (RW)</p>
<dd>The <code>window-scale</code> value calculated from the current window size. This has the same value as <code>window-scale</code> if the window size was not changed since setting the option, and the window size was not restricted in other ways. If the window is fullscreened, this will return the scale value calculated from the last non-fullscreen size of the window. The property is unavailable if no video is active. </p>
<p> When setting this property in the fullscreen or maximized state, the behavior is the same as window-scale. In all ther cases, setting the value of this property will always resize the window. This does not affect the value of <code>window-scale</code>.</p>
<dt><code>focused</code></p>
<dd>Whether the window has focus. Might not be supported by all VOs.</p>
<dt><code>display-names</code></p>
<dd>Names of the displays that the mpv window covers. On X11, these are the xrandr names (LVDS1, HDMI1, DP1, VGA1, etc.). On Windows, these are the GDI names (\.DISPLAY1, \.DISPLAY2, etc.) and the first display in the list will be the one that Windows considers associated with the window (as determined by the MonitorFromWindow API.) On macOS these are the Display Product Names as used in the System Information and only one display name is returned since a window can only be on one screen.</p>
<dt><code>display-fps</code></p>
<dd>The refresh rate of the current display. Currently, this is the lowest FPS of any display covered by the video, as retrieved by the underlying system APIs (e.g. xrandr on X11). It is not the measured FPS. It&#8217;s not necessarily available on all platforms. Note that any of the listed facts may change any time without a warning. </p>
<p> Writing to this property is deprecated. It has the same effect as writing to <code>override-display-fps</code>. Since mpv 0.31.0, this property is unavailable if no display FPS was reported (e.g. if no video is active), while in older versions, it returned the <code>&#8211;display-fps</code> option value.</p>
<dt><code>estimated-display-fps</code></p>
<dd>The actual rate at which display refreshes seem to occur, measured by system time. Only available if display-sync mode (as selected by <code>&#8211;video-sync</code>) is active.</p>
<dt><code>vsync-jitter</code></p>
<dd>Estimated deviation factor of the vsync duration.</p>
<dt><code>display-width</code>, <code>display-height</code></p>
<dd>The current display&#8217;s horizontal and vertical resolution in pixels. Whether or not these values update as the mpv window changes displays depends on the windowing backend. It may not be available on all platforms.</p>
<dt><code>display-hidpi-scale</code></p>
<dd>The HiDPI scale factor as reported by the windowing backend. If no VO is active, or if the VO does not report a value, this property is unavailable. It may be saner to report an absolute DPI, however, this is the way HiDPI support is implemented on most OS APIs. See also <code>&#8211;hidpi-window-scale</code>.</p>
<dt><code>video-aspect</code> (RW)</p>
<dd>Deprecated. This is tied to <code>&#8211;video-aspect-override</code>, but always reports the current video aspect if video is active. </p>
<p> The read and write components of this option can be split up into <code>video-params/aspect</code> and <code>video-aspect-override</code> respectively.</p>
<dt><code>osd-width</code>, <code>osd-height</code></p>
<dd>Last known OSD width (can be 0). This is needed if you want to use the <code>overlay-add</code> command. It gives you the actual OSD/window size (not including decorations drawn by the OS window manager). </p>
<p> Alias to <code>osd-dimensions/w</code> and <code>osd-dimensions/h</code>.</p>
<dt><code>osd-par</code></p>
<dd>Last known OSD display pixel aspect (can be 0). </p>
<p> Alias to <code>osd-dimensions/osd-par</code>.</p>
<dt><code>osd-dimensions</code></p>
<dd>Last known OSD dimensions. </p>
<p> Has the following sub-properties (which can be read as <code>MPV_FORMAT_NODE</code> or Lua table with <code>mp.get_property_native</code>):</p>
<dt><code>osd-dimensions/w</code></p>
<dd>Size of the VO window in OSD render units (usually pixels, but may be scaled pixels with VOs like <code>xv</code>).</p>
<dt><code>osd-dimensions/h</code></p>
<dd>Size of the VO window in OSD render units,</p>
<dt><code>osd-dimensions/par</code></p>
<dd>Pixel aspect ratio of the OSD (usually 1).</p>
<dt><code>osd-dimensions/aspect</code></p>
<dd>Display aspect ratio of the VO window. (Computing from the properties above.)</p>
<dt><code>osd-dimensions/mt</code>, <code>osd-dimensions/mb</code>, <code>osd-dimensions/ml</code>, <code>osd-dimensions/mr</code></p>
<dd>OSD to video margins (top, bottom, left, right). This describes the area into which the video is rendered. </p>
<p> Any of these properties may be unavailable or set to dummy values if the VO window is not created or visible.</p>
<dt><code>mouse-pos</code></p>
<dd>Read-only &#8211; last known mouse position, normalizd to OSD dimensions. </p>
<p> Has the following sub-properties (which can be read as <code>MPV_FORMAT_NODE</code> or Lua table with <code>mp.get_property_native</code>):</p>
<dt><code>mouse-pos/x</code>, <code>mouse-pos/y</code></p>
<dd>Last known coordinates of the mouse pointer.</p>
<dt><code>mouse-pos/hover</code></p>
<dd>Boolean &#8211; whether the mouse pointer hovers the video window. The coordinates should be ignored when this value is false, because the video backends update them only when the pointer hovers the window.</p>
<dt><code>sub-text</code></p>
<dd>The current subtitle text regardless of sub visibility. Formatting is stripped. If the subtitle is not text-based (i.e. DVD/BD subtitles), an empty string is returned. </p>
<p> This property is experimental and might be removed in the future.</p>
<dt><code>sub-text-ass</code></p>
<dd>Like <code>sub-text</code>, but return the text in ASS format. Text subtitles in other formats are converted. For native ASS subtitles, events that do not contain any text (but vector drawings etc.) are not filtered out. If multiple events match with the current playback time, they are concatenated with line breaks. Contains only the &quot;Text&quot; part of the events. </p>
<p> This property is not enough to render ASS subtitles correctly, because ASS header and per-event metadata are not returned. You likely need to do further filtering on the returned string to make it useful. </p>
<p> This property is experimental and might be removed in the future.</p>
<dt><code>secondary-sub-text</code></p>
<dd>Same as <code>sub-text</code>, but for the secondary subtitles.</p>
<dt><code>sub-start</code></p>
<dd>The current subtitle start time (in seconds). If there&#8217;s multiple current subtitles, returns the first start time. If no current subtitle is present null is returned instead.</p>
<dt><code>secondary-sub-start</code></p>
<dd>Same as <code>sub-start</code>, but for the secondary subtitles.</p>
<dt><code>sub-end</code></p>
<dd>The current subtitle end time (in seconds). If there&#8217;s multiple current subtitles, return the last end time. If no current subtitle is present, or if it&#8217;s present but has unknown or incorrect duration, null is returned instead.</p>
<dt><code>secondary-sub-end</code></p>
<dd>Same as <code>sub-end</code>, but for the secondary subtitles.</p>
<dt><code>playlist-pos</code> (RW)</p>
<dd>Current position on playlist. The first entry is on position 0. Writing to this property may start playback at the new position. </p>
<p> In some cases, this is not necessarily the currently playing file. See explanation of <code>current</code> and <code>playing</code> flags in <code>playlist</code>. </p>
<p> If there the playlist is empty, or if it&#8217;s non-empty, but no entry is &quot;current&quot;, this property returns -1. Likewise, writing -1 will put the player into idle mode (or exit playback if idle mode is not enabled). If an out of range index is written to the property, this behaves as if writing -1. (Before mpv 0.33.0, instead of returning -1, this property was unavailable if no playlist entry was current.) </p>
<p> Writing the current value back to the property is subject to change. Currently, it will restart playback of the playlist entry. But in the future, writing the current value will be ignored. Use the <code>playlist-play-index</code> command to get guaranteed behavior.</p>
<dt><code>playlist-pos-1</code> (RW)</p>
<dd>Same as <code>playlist-pos</code>, but 1-based.</p>
<dt><code>playlist-current-pos</code> (RW)</p>
<dd>Index of the &quot;current&quot; item on playlist. This usually, but not necessarily, the currently playing item (see <code>playlist-playing-pos</code>). Depending on the exact internal state of the player, it may refer to the playlist item to play next, or the playlist item used to determine what to play next. </p>
<p> For reading, this is exactly the same as <code>playlist-pos</code>. </p>
<p> For writing, this <i>only</i> sets the position of the &quot;current&quot; item, without stopping playback of the current file (or starting playback, if this is done in idle mode). Use -1 to remove the current flag. </p>
<p> This property is only vaguely useful. If set during playback, it will typically cause the playlist entry <i>after</i> it to be played next. Another possibly odd observable state is that if <code>playlist-next</code> is run during playback, this property is set to the playlist entry to play next (unlike the previous case). There is an internal flag that decides whether the current playlist entry or the next one should be played, and this flag is currently inaccessible for API users. (Whether this behavior will kept is possibly subject to change.)</p>
<dt><code>playlist-playing-pos</code></p>
<dd>Index of the &quot;playing&quot; item on playlist. A playlist item is &quot;playing&quot; if it&#8217;s being loaded, actually playing, or being unloaded. This property is set during the <code>MPV_EVENT_START_FILE</code> (<code>start-file</code>) and the <code>MPV_EVENT_START_END</code> (<code>end-file</code>) events. Outside of that, it returns -1. If the playlist entry was somehow removed during playback, but playback hasn&#8217;t stopped yet, or is in progress of being stopped, it also returns -1. (This can happen at least during state transitions.) </p>
<p> In the &quot;playing&quot; state, this is usually the same as <code>playlist-pos</code>, except during state changes, or if <code>playlist-current-pos</code> was written explicitly.</p>
<dt><code>playlist-count</code></p>
<dd>Number of total playlist entries.</p>
<dt><code>playlist</code></p>
<dd>Playlist, current entry marked. Currently, the raw property value is useless. </p>
<p> This has a number of sub-properties. Replace <code>N</code> with the 0-based playlist entry index.</p>
<dt><code>playlist/count</code></p>
<dd>Number of playlist entries (same as <code>playlist-count</code>).</p>
<dt><code>playlist/N/filename</code></p>
<dd>Filename of the Nth entry.</p>
<dt><code>playlist/N/playing</code></p>
<dd><code>yes</code>/true if the <code>playlist-playing-pos</code> property points to this entry, <code>no</code>/false or unavailable otherwise.</p>
<dt><code>playlist/N/current</code></p>
<dd><code>yes</code>/true if the <code>playlist-current-pos</code> property points to this entry, <code>no</code>/false or unavailable otherwise.</p>
<dt><code>playlist/N/title</code></p>
<dd>Name of the Nth entry. Only available if the playlist file contains such fields, and only if mpv&#8217;s parser supports it for the given playlist format.</p>
<dt><code>playlist/N/id</code></p>
<dd>Unique ID for this entry. This is an automatically assigned integer ID that is unique for the entire life time of the current mpv core instance. Other commands, events, etc. use this as <code>playlist_entry_id</code> fields. </p>
<p> When querying the property with the client API using <code>MPV_FORMAT_NODE</code>, or with Lua <code>mp.get_property_native</code>, this will return a mpv_node with the following contents: </p>
<pre>MPV_FORMAT_NODE_ARRAY
 MPV_FORMAT_NODE_MAP (for each playlist entry)
 &quot;filename&quot; MPV_FORMAT_STRING
 &quot;current&quot; MPV_FORMAT_FLAG (might be missing; since mpv 0.7.0)
 &quot;playing&quot; MPV_FORMAT_FLAG (same)
 &quot;title&quot; MPV_FORMAT_STRING (optional)
 &quot;id&quot; MPV_FORMAT_INT64</pre>
<dt><code>track-list</code></p>
<dd>List of audio/video/sub tracks, current entry marked. Currently, the raw property value is useless. </p>
<p> This has a number of sub-properties. Replace <code>N</code> with the 0-based track index.</p>
<dt><code>track-list/count</code></p>
<dd>Total number of tracks.</p>
<dt><code>track-list/N/id</code></p>
<dd>The ID as it&#8217;s used for <code>-sid</code>/<code>&#8211;aid</code>/<code>&#8211;vid</code>. This is unique within tracks of the same type (sub/audio/video), but otherwise not.</p>
<dt><code>track-list/N/type</code></p>
<dd>String describing the media type. One of <code>audio</code>, <code>video</code>, <code>sub</code>.</p>
<dt><code>track-list/N/src-id</code></p>
<dd>Track ID as used in the source file. Not always available. (It is missing if the format has no native ID, if the track is a pseudo-track that does not exist in this way in the actual file, or if the format is handled by libavformat, and the format was not whitelisted as having track IDs.)</p>
<dt><code>track-list/N/title</code></p>
<dd>Track title as it is stored in the file. Not always available.</p>
<dt><code>track-list/N/lang</code></p>
<dd>Track language as identified by the file. Not always available.</p>
<dt><code>track-list/N/image</code></p>
<dd><code>yes</code>/true if this is a video track that consists of a single picture, <code>no</code>/false or unavailable otherwise. The heuristic used to determine if a stream is an image doesn&#8217;t attempt to detect images in codecs normally used for videos. Otherwise, it is reliable.</p>
<dt><code>track-list/N/albumart</code></p>
<dd><code>yes</code>/true if this is an image embedded in an audio file or external cover art, <code>no</code>/false or unavailable otherwise.</p>
<dt><code>track-list/N/default</code></p>
<dd><code>yes</code>/true if the track has the default flag set in the file, <code>no</code>/false or unavailable otherwise.</p>
<dt><code>track-list/N/forced</code></p>
<dd><code>yes</code>/true if the track has the forced flag set in the file, <code>no</code>/false or unavailable otherwise.</p>
<dt><code>track-list/N/codec</code></p>
<dd>The codec name used by this track, for example <code>h264</code>. Unavailable in some rare cases.</p>
<dt><code>track-list/N/external</code></p>
<dd><code>yes</code>/true if the track is an external file, <code>no</code>/false or unavailable otherwise. This is set for separate subtitle files.</p>
<dt><code>track-list/N/external-filename</code></p>
<dd>The filename if the track is from an external file, unavailable otherwise.</p>
<dt><code>track-list/N/selected</code></p>
<dd><code>yes</code>/true if the track is currently decoded, <code>no</code>/false or unavailable otherwise.</p>
<dt><code>track-list/N/main-selection</code></p>
<dd>It indicates the selection order of tracks for the same type. If a track is not selected, or is selected by the <code>&#8211;lavfi-complex</code>, it is not available. For subtitle tracks, <code>0</code> represents the <code>sid</code>, and <code>1</code> represents the <code>secondary-sid</code>.</p>
<dt><code>track-list/N/ff-index</code></p>
<dd>The stream index as usually used by the FFmpeg utilities. Note that this can be potentially wrong if a demuxer other than libavformat (<code>&#8211;demuxer=lavf</code>) is used. For mkv files, the index will usually match even if the default (builtin) demuxer is used, but there is no hard guarantee.</p>
<dt><code>track-list/N/decoder-desc</code></p>
<dd>If this track is being decoded, the human-readable decoder name,</p>
<dt><code>track-list/N/demux-w</code>, <code>track-list/N/demux-h</code></p>
<dd>Video size hint as indicated by the container. (Not always accurate.)</p>
<dt><code>track-list/N/demux-channel-count</code></p>
<dd>Number of audio channels as indicated by the container. (Not always accurate &#8211; in particular, the track could be decoded as a different number of channels.)</p>
<dt><code>track-list/N/demux-channels</code></p>
<dd>Channel layout as indicated by the container. (Not always accurate.)</p>
<dt><code>track-list/N/demux-samplerate</code></p>
<dd>Audio sample rate as indicated by the container. (Not always accurate.)</p>
<dt><code>track-list/N/demux-fps</code></p>
<dd>Video FPS as indicated by the container. (Not always accurate.)</p>
<dt><code>track-list/N/demux-bitrate</code></p>
<dd>Audio average bitrate, in bits per second. (Not always accurate.)</p>
<dt><code>track-list/N/demux-rotation</code></p>
<dd>Video clockwise rotation metadata, in degrees.</p>
<dt><code>track-list/N/demux-par</code></p>
<dd>Pixel aspect ratio.</p>
<dt><code>track-list/N/audio-channels</code> (deprecated)</p>
<dd>Deprecated alias for <code>track-list/N/demux-channel-count</code>.</p>
<dt><code>track-list/N/replaygain-track-peak</code>, <code>track-list/N/replaygain-track-gain</code></p>
<dd>Per-track replaygain values. Only available for audio tracks with corresponding information stored in the source file.</p>
<dt><code>track-list/N/replaygain-album-peak</code>, <code>track-list/N/replaygain-album-gain</code></p>
<dd>Per-album replaygain values. If the file has per-track but no per-album information, the per-album values will be copied from the per-track values currently. It&#8217;s possible that future mpv versions will make these properties unavailable instead in this case. </p>
<p> When querying the property with the client API using <code>MPV_FORMAT_NODE</code>, or with Lua <code>mp.get_property_native</code>, this will return a mpv_node with the following contents: </p>
<pre>MPV_FORMAT_NODE_ARRAY
 MPV_FORMAT_NODE_MAP (for each track)
 &quot;id&quot; MPV_FORMAT_INT64
 &quot;type&quot; MPV_FORMAT_STRING
 &quot;src-id&quot; MPV_FORMAT_INT64
 &quot;title&quot; MPV_FORMAT_STRING
 &quot;lang&quot; MPV_FORMAT_STRING
 &quot;image&quot; MPV_FORMAT_FLAG
 &quot;albumart&quot; MPV_FORMAT_FLAG
 &quot;default&quot; MPV_FORMAT_FLAG
 &quot;forced&quot; MPV_FORMAT_FLAG
 &quot;selected&quot; MPV_FORMAT_FLAG
 &quot;main-selection&quot; MPV_FORMAT_INT64
 &quot;external&quot; MPV_FORMAT_FLAG
 &quot;external-filename&quot; MPV_FORMAT_STRING
 &quot;codec&quot; MPV_FORMAT_STRING
 &quot;ff-index&quot; MPV_FORMAT_INT64
 &quot;decoder-desc&quot; MPV_FORMAT_STRING
 &quot;demux-w&quot; MPV_FORMAT_INT64
 &quot;demux-h&quot; MPV_FORMAT_INT64
 &quot;demux-channel-count&quot; MPV_FORMAT_INT64
 &quot;demux-channels&quot; MPV_FORMAT_STRING
 &quot;demux-samplerate&quot; MPV_FORMAT_INT64
 &quot;demux-fps&quot; MPV_FORMAT_DOUBLE
 &quot;demux-bitrate&quot; MPV_FORMAT_INT64
 &quot;demux-rotation&quot; MPV_FORMAT_INT64
 &quot;demux-par&quot; MPV_FORMAT_DOUBLE
 &quot;audio-channels&quot; MPV_FORMAT_INT64
 &quot;replaygain-track-peak&quot; MPV_FORMAT_DOUBLE
 &quot;replaygain-track-gain&quot; MPV_FORMAT_DOUBLE
 &quot;replaygain-album-peak&quot; MPV_FORMAT_DOUBLE
 &quot;replaygain-album-gain&quot; MPV_FORMAT_DOUBLE</pre>
<dt><code>current-tracks/&#8230;</code></p>
<dd>This gives access to currently selected tracks. It redirects to the correct entry in <code>track-list</code>. </p>
<p> The following sub-entries are defined: <code>video</code>, <code>audio</code>, <code>sub</code>, <code>sub2</code> </p>
<p> For example, <code>current-tracks/audio/lang</code> returns the current audio track&#8217;s language field (the same value as <code>track-list/N/lang</code>). </p>
<p> If tracks of the requested type are selected via <code>&#8211;lavfi-complex</code>, the first one is returned.</p>
<dt><code>chapter-list</code></p>
<dd>List of chapters, current entry marked. Currently, the raw property value is useless. </p>
<p> This has a number of sub-properties. Replace <code>N</code> with the 0-based chapter index.</p>
<dt><code>chapter-list/count</code></p>
<dd>Number of chapters.</p>
<dt><code>chapter-list/N/title</code></p>
<dd>Chapter title as stored in the file. Not always available.</p>
<dt><code>chapter-list/N/time</code></p>
<dd>Chapter start time in seconds as float. </p>
<p> When querying the property with the client API using <code>MPV_FORMAT_NODE</code>, or with Lua <code>mp.get_property_native</code>, this will return a mpv_node with the following contents: </p>
<pre>MPV_FORMAT_NODE_ARRAY
 MPV_FORMAT_NODE_MAP (for each chapter)
 &quot;title&quot; MPV_FORMAT_STRING
 &quot;time&quot; MPV_FORMAT_DOUBLE</pre>
<dt><code>af</code>, <code>vf</code> (RW)</p>
<dd>See <code>&#8211;vf</code>/<code>&#8211;af</code> and the <code>vf</code>/<code>af</code> command. </p>
<p> When querying the property with the client API using <code>MPV_FORMAT_NODE</code>, or with Lua <code>mp.get_property_native</code>, this will return a mpv_node with the following contents: </p>
<pre>MPV_FORMAT_NODE_ARRAY
 MPV_FORMAT_NODE_MAP (for each filter entry)
 &quot;name&quot; MPV_FORMAT_STRING
 &quot;label&quot; MPV_FORMAT_STRING [optional]
 &quot;enabled&quot; MPV_FORMAT_FLAG [optional]
 &quot;params&quot; MPV_FORMAT_NODE_MAP [optional]
 &quot;key&quot; MPV_FORMAT_STRING
 &quot;value&quot; MPV_FORMAT_STRING</pre>
<p>It&#8217;s also possible to write the property using this format.</p>
<dt><code>seekable</code></p>
<dd>Whether it&#8217;s generally possible to seek in the current file.</p>
<dt><code>partially-seekable</code></p>
<dd>Whether the current file is considered seekable, but only because the cache is active. This means small relative seeks may be fine, but larger seeks may fail anyway. Whether a seek will succeed or not is generally not known in advance. </p>
<p> If this property returns <code>yes</code>/true, so will <code>seekable</code>.</p>
<dt><code>playback-abort</code></p>
<dd>Whether playback is stopped or is to be stopped. (Useful in obscure situations like during <code>on_load</code> hook processing, when the user can stop playback, but the script has to explicitly end processing.)</p>
<dt><code>cursor-autohide</code> (RW)</p>
<dd>See <code>&#8211;cursor-autohide</code>. Setting this to a new value will always update the cursor, and reset the internal timer.</p>
<dt><code>osd-sym-cc</code></p>
<dd>Inserts the current OSD symbol as opaque OSD control code (cc). This makes sense only with the <code>show-text</code> command or options which set OSD messages. The control code is implementation specific and is useless for anything else.</p>
<dt><code>osd-ass-cc</code></p>
<dd><code>${osd-ass-cc/0}</code> disables escaping ASS sequences of text in OSD, <code>${osd-ass-cc/1}</code> enables it again. By default, ASS sequences are escaped to avoid accidental formatting, and this property can disable this behavior. Note that the properties return an opaque OSD control code, which only makes sense for the <code>show-text</code> command or options which set OSD messages.</p>
<dt>Example</p>
<dd>
<dt>&bull;</p>
<dd><code>&#8211;osd-msg3=&#8217;This is ${osd-ass-cc/0}{\b1}bold text&#8217;</code></p>
<dt>&bull;</p>
<dd><code>show-text &quot;This is ${osd-ass-cc/0}{\b1}bold text&quot;</code> </p>
<p> Any ASS override tags as understood by libass can be used. </p>
<p> Note that you need to escape the <code>\</code> character, because the string is processed for C escape sequences before passing it to the OSD code. See <i>Flat command syntax</i> for details. </p>
<p> A list of tags can be found here: <i><a rel="nofollow" href="http://docs.aegisub.org/latest/ASS_Tags/">http://docs.aegisub.org/latest/ASS_Tags/</a></i></p>
<dt><code>vo-configured</code></p>
<dd>Whether the VO is configured right now. Usually this corresponds to whether the video window is visible. If the <code>&#8211;force-window</code> option is used, this usually always returns <code>yes</code>/true.</p>
<dt><code>vo-passes</code></p>
<dd>Contains introspection about the VO&#8217;s active render passes and their execution times. Not implemented by all VOs. </p>
<p> This is further subdivided into two frame types, <code>vo-passes/fresh</code> for fresh frames (which have to be uploaded, scaled, etc.) and <code>vo-passes/redraw</code> for redrawn frames (which only have to be re-painted). The number of passes for any given subtype can change from frame to frame, and should not be relied upon. </p>
<p> Each frame type has a number of further sub-properties. Replace <code>TYPE</code> with the frame type, <code>N</code> with the 0-based pass index, and <code>M</code> with the 0-based sample index.</p>
<dt><code>vo-passes/TYPE/count</code></p>
<dd>Number of passes.</p>
<dt><code>vo-passes/TYPE/N/desc</code></p>
<dd>Human-friendy description of the pass.</p>
<dt><code>vo-passes/TYPE/N/last</code></p>
<dd>Last measured execution time, in nanoseconds.</p>
<dt><code>vo-passes/TYPE/N/avg</code></p>
<dd>Average execution time of this pass, in nanoseconds. The exact timeframe varies, but it should generally be a handful of seconds.</p>
<dt><code>vo-passes/TYPE/N/peak</code></p>
<dd>The peak execution time (highest value) within this averaging range, in nanoseconds.</p>
<dt><code>vo-passes/TYPE/N/count</code></p>
<dd>The number of samples for this pass.</p>
<dt><code>vo-passes/TYPE/N/samples/M</code></p>
<dd>The raw execution time of a specific sample for this pass, in nanoseconds. </p>
<p> When querying the property with the client API using <code>MPV_FORMAT_NODE</code>, or with Lua <code>mp.get_property_native</code>, this will return a mpv_node with the following contents: </p>
<pre>MPV_FORMAT_NODE_MAP
&quot;TYPE&quot; MPV_FORMAT_NODE_ARRAY
 MPV_FORMAT_NODE_MAP
 &quot;desc&quot; MPV_FORMAT_STRING
 &quot;last&quot; MPV_FORMAT_INT64
 &quot;avg&quot; MPV_FORMAT_INT64
 &quot;peak&quot; MPV_FORMAT_INT64
 &quot;count&quot; MPV_FORMAT_INT64
 &quot;samples&quot; MPV_FORMAT_NODE_ARRAY
 MP_FORMAT_INT64</pre>
<p>Note that directly accessing this structure via subkeys is not supported, the only access is through aforementioned <code>MPV_FORMAT_NODE</code>.</p>
<dt><code>perf-info</code></p>
<dd>Further performance data. Querying this property triggers internal collection of some data, and may slow down the player. Each query will reset some internal state. Property change notification doesn&#8217;t and won&#8217;t work. All of this may change in the future, so don&#8217;t use this. The builtin <code>stats</code> script is supposed to be the only user; since it&#8217;s bundled and built with the source code, it can use knowledge of mpv internal to render the information properly. See <code>stats</code> script description for some details.</p>
<dt><code>video-bitrate</code>, <code>audio-bitrate</code>, <code>sub-bitrate</code></p>
<dd>Bitrate values calculated on the packet level. This works by dividing the bit size of all packets between two keyframes by their presentation timestamp distance. (This uses the timestamps are stored in the file, so e.g. playback speed does not influence the returned values.) In particular, the video bitrate will update only per keyframe, and show the &quot;past&quot; bitrate. To make the property more UI friendly, updates to these properties are throttled in a certain way. </p>
<p> The unit is bits per second. OSD formatting turns these values in kilobits (or megabits, if appropriate), which can be prevented by using the raw property value, e.g. with <code>${=video-bitrate}</code>. </p>
<p> Note that the accuracy of these properties is influenced by a few factors. If the underlying demuxer rewrites the packets on demuxing (done for some file formats), the bitrate might be slightly off. If timestamps are bad or jittery (like in Matroska), even constant bitrate streams might show fluctuating bitrate. </p>
<p> How exactly these values are calculated might change in the future. </p>
<p> In earlier versions of mpv, these properties returned a static (but bad) guess using a completely different method.</p>
<dt><code>packet-video-bitrate</code>, <code>packet-audio-bitrate</code>, <code>packet-sub-bitrate</code></p>
<dd>Old and deprecated properties for <code>video-bitrate</code>, <code>audio-bitrate</code>, <code>sub-bitrate</code>. They behave exactly the same, but return a value in kilobits. Also, they don&#8217;t have any OSD formatting, though the same can be achieved with e.g. <code>${=video-bitrate}</code>. </p>
<p> These properties shouldn&#8217;t be used anymore.</p>
<dt><code>audio-device-list</code></p>
<dd>The list of discovered audio devices. This is mostly for use with the client API, and reflects what <code>&#8211;audio-device=help</code> with the command line player returns. </p>
<p> When querying the property with the client API using <code>MPV_FORMAT_NODE</code>, or with Lua <code>mp.get_property_native</code>, this will return a mpv_node with the following contents: </p>
<pre>MPV_FORMAT_NODE_ARRAY
 MPV_FORMAT_NODE_MAP (for each device entry)
 &quot;name&quot; MPV_FORMAT_STRING
 &quot;description&quot; MPV_FORMAT_STRING</pre>
<p>The <code>name</code> is what is to be passed to the <code>&#8211;audio-device</code> option (and often a rather cryptic audio API-specific ID), while <code>description</code> is human readable free form text. The description is set to the device name (minus mpv-specific <code>&lt;driver&gt;/</code> prefix) if no description is available or the description would have been an empty string. </p>
<p> The special entry with the name set to <code>auto</code> selects the default audio output driver and the default device. </p>
<p> The property can be watched with the property observation mechanism in the client API and in Lua scripts. (Technically, change notification is enabled the first time this property is read.)</p>
<dt><code>audio-device</code> (RW)</p>
<dd>Set the audio device. This directly reads/writes the <code>&#8211;audio-device</code> option, but on write accesses, the audio output will be scheduled for reloading. </p>
<p> Writing this property while no audio output is active will not automatically enable audio. (This is also true in the case when audio was disabled due to reinitialization failure after a previous write access to <code>audio-device</code>.) </p>
<p> This property also doesn&#8217;t tell you which audio device is actually in use. </p>
<p> How these details are handled may change in the future.</p>
<dt><code>current-vo</code></p>
<dd>Current video output driver (name as used with <code>&#8211;vo</code>).</p>
<dt><code>current-ao</code></p>
<dd>Current audio output driver (name as used with <code>&#8211;ao</code>).</p>
<dt><code>shared-script-properties</code> (RW)</p>
<dd>This is a key/value map of arbitrary strings shared between scripts for general use. The player itself does not use any data in it (although some builtin scripts may). The property is not preserved across player restarts. </p>
<p> This is very primitive, inefficient, and annoying to use. It&#8217;s a makeshift solution which could go away any time (for example, when a better solution becomes available). This is also why this property has an annoying name. You should avoid using it, unless you absolutely have to. </p>
<p> Lua scripting has helpers starting with <code>utils.shared_script_property_</code>. They are undocumented because you should not use this property. If you still think you must, you should use the helpers instead of the property directly. </p>
<p> You are supposed to use the <code>change-list</code> command to modify the contents. Reading, modifying, and writing the property manually could data loss if two scripts update different keys at the same time due to lack of synchronization. The Lua helpers take care of this. </p>
<p> (There is no way to ensure synchronization if two scripts try to update the same key at the same time.)</p>
<dt><code>working-directory</code></p>
<dd>The working directory of the mpv process. Can be useful for JSON IPC users, because the command line player usually works with relative paths.</p>
<dt><code>protocol-list</code></p>
<dd>List of protocol prefixes potentially recognized by the player. They are returned without trailing <code>://</code> suffix (which is still always required). In some cases, the protocol will not actually be supported (consider <code>https</code> if ffmpeg is not compiled with TLS support).</p>
<dt><code>decoder-list</code></p>
<dd>List of decoders supported. This lists decoders which can be passed to <code>&#8211;vd</code> and <code>&#8211;ad</code>.</p>
<dt><code>codec</code></p>
<dd>Canonical codec name, which identifies the format the decoder can handle.</p>
<dt><code>driver</code></p>
<dd>The name of the decoder itself. Often, this is the same as <code>codec</code>. Sometimes it can be different. It is used to distinguish multiple decoders for the same codec.</p>
<dt><code>description</code></p>
<dd>Human readable description of the decoder and codec. </p>
<p> When querying the property with the client API using <code>MPV_FORMAT_NODE</code>, or with Lua <code>mp.get_property_native</code>, this will return a mpv_node with the following contents: </p>
<pre>MPV_FORMAT_NODE_ARRAY
 MPV_FORMAT_NODE_MAP (for each decoder entry)
 &quot;codec&quot; MPV_FORMAT_STRING
 &quot;driver&quot; MPV_FORMAT_STRING
 &quot;description&quot; MPV_FORMAT_STRING</pre>
<dt><code>encoder-list</code></p>
<dd>List of libavcodec encoders. This has the same format as <code>decoder-list</code>. The encoder names (<code>driver</code> entries) can be passed to <code>&#8211;ovc</code> and <code>&#8211;oac</code> (without the <code>lavc:</code> prefix required by <code>&#8211;vd</code> and <code>&#8211;ad</code>).</p>
<dt><code>demuxer-lavf-list</code></p>
<dd>List of available libavformat demuxers&#8217; names. This can be used to check for support for a specific format or use with <code>&#8211;demuxer-lavf-format</code>.</p>
<dt><code>input-key-list</code></p>
<dd>List of <i>Key names</i>, same as output by <code>&#8211;input-keylist</code>.</p>
<dt><code>mpv-version</code></p>
<dd>The mpv version/copyright string. Depending on how the binary was built, it might contain either a release version, or just a git hash.</p>
<dt><code>mpv-configuration</code></p>
<dd>The configuration arguments which were passed to the build system (typically the way <code>./waf configure &#8230;</code> was invoked).</p>
<dt><code>ffmpeg-version</code></p>
<dd>The contents of the <code>av_version_info()</code> API call. This is a string which identifies the build in some way, either through a release version number, or a git hash. This applies to Libav as well (the property is still named the same.) This property is unavailable if mpv is linked against older FFmpeg and Libav versions.</p>
<dt><code>libass-version</code></p>
<dd>The value of <code>ass_library_version()</code>. This is an integer, encoded in a somewhat weird form (apparently &quot;hex BCD&quot;), indicating the release version of the libass library linked to mpv.</p>
<dt><code>options/&lt;name&gt;</code> (RW)</p>
<dd>The value of option <code>&#8211;&lt;name&gt;</code>. Most options can be changed at runtime by writing to this property. Note that many options require reloading the file for changes to take effect. If there is an equivalent property, prefer setting the property instead. </p>
<p> There shouldn&#8217;t be any reason to access <code>options/&lt;name&gt;</code> instead of <code>&lt;name&gt;</code>, except in situations in which the properties have different behavior or conflicting semantics.</p>
<dt><code>file-local-options/&lt;name&gt;</code> (RW)</p>
<dd>Similar to <code>options/&lt;name&gt;</code>, but when setting an option through this property, the option is reset to its old value once the current file has stopped playing. Trying to write an option while no file is playing (or is being loaded) results in an error. </p>
<p> (Note that if an option is marked as file-local, even <code>options/</code> will access the local value, and the <code>old</code> value, which will be restored on end of playback, cannot be read or written until end of playback.)</p>
<dt><code>option-info/&lt;name&gt;</code></p>
<dd>Additional per-option information. </p>
<p> This has a number of sub-properties. Replace <code>&lt;name&gt;</code> with the name of a top-level option. No guarantee of stability is given to any of these sub-properties &#8211; they may change radically in the feature.</p>
<dt><code>option-info/&lt;name&gt;/name</code></p>
<dd>The name of the option.</p>
<dt><code>option-info/&lt;name&gt;/type</code></p>
<dd>The name of the option type, like <code>String</code> or <code>Integer</code>. For many complex types, this isn&#8217;t very accurate.</p>
<dt><code>option-info/&lt;name&gt;/set-from-commandline</code></p>
<dd>Whether the option was set from the mpv command line. What this is set to if the option is e.g. changed at runtime is left undefined (meaning it could change in the future).</p>
<dt><code>option-info/&lt;name&gt;/set-locally</code></p>
<dd>Whether the option was set per-file. This is the case with automatically loaded profiles, file-dir configs, and other cases. It means the option value will be restored to the value before playback start when playback ends.</p>
<dt><code>option-info/&lt;name&gt;/default-value</code></p>
<dd>The default value of the option. May not always be available.</p>
<dt><code>option-info/&lt;name&gt;/min</code>, <code>option-info/&lt;name&gt;/max</code></p>
<dd>Integer minimum and maximum values allowed for the option. Only available if the options are numeric, and the minimum/maximum has been set internally. It&#8217;s also possible that only one of these is set.</p>
<dt><code>option-info/&lt;name&gt;/choices</code></p>
<dd>If the option is a choice option, the possible choices. Choices that are integers may or may not be included (they can be implied by <code>min</code> and <code>max</code>). Note that options which behave like choice options, but are not actual choice options internally, may not have this info available.</p>
<dt><code>property-list</code></p>
<dd>The list of top-level properties.</p>
<dt><code>profile-list</code></p>
<dd>The list of profiles and their contents. This is highly implementation-specific, and may change any time. Currently, it returns an array of options for each profile. Each option has a name and a value, with the value currently always being a string. Note that the options array is not a map, as order matters and duplicate entries are possible. Recursive profiles are not expanded, and show up as special <code>profile</code> options.</p>
<dt><code>command-list</code></p>
<dd>The list of input commands. This returns an array of maps, where each map node represents a command. This map currently only has a single entry: <code>name</code> for the name of the command. (This property is supposed to be a replacement for <code>&#8211;input-cmdlist</code>. The option dumps some more information, but it&#8217;s a valid feature request to extend this property if needed.)</p>
<dt><code>input-bindings</code></p>
<dd>The list of current input key bindings. This returns an array of maps, where each map node represents a binding for a single key/command. This map has the following entries:</p>
<dt><code>key</code></p>
<dd>The key name. This is normalized and may look slightly different from how it was specified in the source (e.g. in input.conf).</p>
<dt><code>cmd</code></p>
<dd>The command mapped to the key. (Currently, this is exactly the same string as specified in the source, other than stripping whitespace and comments. It&#8217;s possible that it will be normalized in the future.)</p>
<dt><code>is_weak</code></p>
<dd>If set to true, any existing and active user bindings will take priority.</p>
<dt><code>owner</code></p>
<dd>If this entry exists, the name of the script (or similar) which added this binding.</p>
<dt><code>section</code></p>
<dd>Name of the section this binding is part of. This is a rarely used mechanism. This entry may be removed or change meaning in the future.</p>
<dt><code>priority</code></p>
<dd>A number. Bindings with a higher value are preferred over bindings with a lower value. If the value is negative, this binding is inactive and will not be triggered by input. Note that mpv does not use this value internally, and matching of bindings may work slightly differently in some cases. In addition, this value is dynamic and can change around at runtime.</p>
<dt><code>comment</code></p>
<dd>If available, the comment following the command on the same line. (For example, the input.conf entry <code>f cycle bla # toggle bla</code> would result in an entry with <code>comment = &quot;toggle bla&quot;, cmd = &quot;cycle bla&quot;</code>.) </p>
<p> This property is read-only, and change notification is not supported. Currently, there is no mechanism to change key bindings at runtime, other than scripts adding or removing their own bindings.</dl>
<h3>Inconsistencies between options and properties</h3>
<p>You can access (almost) all options as properties, though there are some caveats with some properties (due to historical reasons):</p>
<dl COMPACT>
<dt><code>vid</code>, <code>aid</code>, <code>sid</code></p>
<dd>While playback is active, these return the actually active tracks. For example, if you set <code>aid=5</code>, and the currently played file contains no audio track with ID 5, the <code>aid</code> property will return <code>no</code>. </p>
<p> Before mpv 0.31.0, you could set existing tracks at runtime only.</p>
<dt><code>display-fps</code></p>
<dd>This inconsistent behavior is deprecated. Post-deprecation, the reported value and the option value are cleanly separated (<code>override-display-fps</code> for the option value).</p>
<dt><code>vf</code>, <code>af</code></p>
<dd>If you set the properties during playback, and the filter chain fails to reinitialize, the option will be set, but the runtime filter chain does not change. On the other hand, the next video to be played will fail, because the initial filter chain cannot be created. </p>
<p> This behavior changed in mpv 0.31.0. Before this, the new value was rejected <i>iff</i> a video (for <code>vf</code>) or an audio (for <code>af</code>) track was active. If playback was not active, the behavior was the same as the current one.</p>
<dt><code>playlist</code></p>
<dd>The property is read-only and returns the current internal playlist. The option is for loading playlist during command line parsing. For client API uses, you should use the <code>loadlist</code> command instead.</p>
<dt><code>profile</code>, <code>include</code></p>
<dd>These are write-only, and will perform actions as they are written to, exactly as if they were used on the mpv CLI commandline. Their only use is when using libmpv before <code>mpv_initialize()</code>, which in turn is probably only useful in encoding mode. Normal libmpv users should use other mechanisms, such as the <code>apply-profile</code> command, and the <code>mpv_load_config_file</code> API function. Avoid these properties.</dl>
<h3>Property Expansion</h3>
<p>All string arguments to input commands as well as certain options (like <code>&#8211;term-playing-msg</code>) are subject to property expansion. Note that property expansion does not work in places where e.g. numeric parameters are expected. (For example, the <code>add</code> command does not do property expansion. The <code>set</code> command is an exception and not a general rule.)</p>
<dl COMPACT>
<dt>Example for input.conf</p>
<dd>
<dt><code>i show-text Filename: ${filename}</code></p>
<dd>shows the filename of the current file when pressing the <code>i</code> key </p>
<p> Whether property expansion is enabled by default depends on which API is used (see <i>Flat command syntax</i>, <i>Commands specified as arrays</i> and <i>Named arguments</i>), but it can always be enabled with the <code>expand-properties</code> prefix or disabled with the <code>raw</code> prefix, as described in <i>Input Command Prefixes</i>. </p>
<p> The following expansions are supported:</p>
<dt><code>${NAME}</code></p>
<dd>Expands to the value of the property <code>NAME</code>. If retrieving the property fails, expand to an error string. (Use <code>${NAME:}</code> with a trailing <code>:</code> to expand to an empty string instead.) If <code>NAME</code> is prefixed with <code>=</code>, expand to the raw value of the property (see section below).</p>
<dt><code>${NAME:STR}</code></p>
<dd>Expands to the value of the property <code>NAME</code>, or <code>STR</code> if the property cannot be retrieved. <code>STR</code> is expanded recursively.</p>
<dt><code>${?NAME:STR}</code></p>
<dd>Expands to <code>STR</code> (recursively) if the property <code>NAME</code> is available.</p>
<dt><code>${!NAME:STR}</code></p>
<dd>Expands to <code>STR</code> (recursively) if the property <code>NAME</code> cannot be retrieved.</p>
<dt><code>${?NAME==VALUE:STR}</code></p>
<dd>Expands to <code>STR</code> (recursively) if the property <code>NAME</code> expands to a string equal to <code>VALUE</code>. You can prefix <code>NAME</code> with <code>=</code> in order to compare the raw value of a property (see section below). If the property is unavailable, or other errors happen when retrieving it, the value is never considered equal. Note that <code>VALUE</code> can&#8217;t contain any of the characters <code>:</code> or <code>}</code>. Also, it is possible that escaping with <code>&quot;</code> or <code>%</code> might be added in the future, should the need arise.</p>
<dt><code>${!NAME==VALUE:STR}</code></p>
<dd>Same as with the <code>?</code> variant, but <code>STR</code> is expanded if the value is not equal. (Using the same semantics as with <code>?</code>.)</p>
<dt><code>$$</code></p>
<dd>Expands to <code>$</code>.</p>
<dt><code>$}</code></p>
<dd>Expands to <code>}</code>. (To produce this character inside recursive expansion.)</p>
<dt><code>$&gt;</code></p>
<dd>Disable property expansion and special handling of <code>$</code> for the rest of the string. </p>
<p> In places where property expansion is allowed, C-style escapes are often accepted as well. Example:</p>
<dt>&bull;</p>
<dd><code>
</code> becomes a newline character</p>
<dt>&bull;</p>
<dd><code>\</code> expands to <code>\</code></dl>
<h3>Raw and Formatted Properties</h3>
<p>Normally, properties are formatted as human-readable text, meant to be displayed on OSD or on the terminal. It is possible to retrieve an unformatted (raw) value from a property by prefixing its name with <code>=</code>. These raw values can be parsed by other programs and follow the same conventions as the options associated with the properties.</p>
<dl COMPACT>
<dt>Examples</p>
<dd>
<dt>&bull;</p>
<dd><code>${time-pos}</code> expands to <code>00:14:23</code> (if playback position is at 14 minutes 23 seconds)</p>
<dt>&bull;</p>
<dd><code>${=time-pos}</code> expands to <code>863.4</code> (same time, plus 400 milliseconds &#8211; milliseconds are normally not shown in the formatted case) </p>
<p> Sometimes, the difference in amount of information carried by raw and formatted property values can be rather big. In some cases, raw values have more information, like higher precision than seconds with <code>time-pos</code>. Sometimes it is the other way around, e.g. <code>aid</code> shows track title and language in the formatted case, but only the track number if it is raw.</dl>
<h2>On Screen Controller</h2>
<p>The On Screen Controller (short: OSC) is a minimal GUI integrated with mpv to offer basic mouse-controllability. It is intended to make interaction easier for new users and to enable precise and direct seeking. </p>
<p> The OSC is enabled by default if mpv was compiled with Lua support. It can be disabled entirely using the <code>&#8211;osc=no</code> option.</p>
<h3>Using the OSC</h3>
<p>By default, the OSC will show up whenever the mouse is moved inside the player window and will hide if the mouse is not moved outside the OSC for 0.5 seconds or if the mouse leaves the window.</p>
<h3>The Interface</h3>
<pre>+---------+----------+------------------------------------------+----------+
| pl prev | pl next | title | cache |
+------+--+---+------+---------+-----------+------+-------+-----+-----+----+
| play | skip | skip | time | seekbar | time | audio | sub | vol | fs |
| | back | frwd | elapsed | | left | | | | |
+------+------+------+---------+-----------+------+-------+-----+-----+----+</pre>
<dl COMPACT>
<dt><code>pl prev</code></p>
<dd><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> left-click </td>
<td> play previous file in playlist
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> right-click </td>
<td> show playlist
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> shift+L-click </td>
<td> show playlist
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>pl next</code></p>
<dd><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> left-click </td>
<td> play next file in playlist
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> right-click </td>
<td> show playlist
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> shift+L-click </td>
<td> show playlist
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>title</code></p>
<dd>
<pre>Displays current media-title, filename, custom title, or target chapter
name while hovering the seekbar.</pre>
<p><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> left-click </td>
<td> show playlist position and length and full title
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> right-click </td>
<td> show filename
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>cache</code></p>
<dd>
<pre>Shows current cache fill status</pre>
<dt><code>play</code></p>
<dd><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> left-click </td>
<td> toggle play/pause
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>skip back</code></p>
<dd><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> left-click </td>
<td> go to beginning of chapter / previous chapter
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> right-click </td>
<td> show chapters
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> shift+L-click </td>
<td> show chapters
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>skip frwd</code></p>
<dd><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> left-click </td>
<td> go to next chapter
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> right-click </td>
<td> show chapters
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> shift+L-click </td>
<td> show chapters
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>time elapsed</code></p>
<dd>
<pre>Shows current playback position timestamp</pre>
<p><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> left-click </td>
<td> toggle displaying timecodes with milliseconds
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>seekbar</code></p>
<dd>
<pre>Indicates current playback position and position of chapters</pre>
<p><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> left-click </td>
<td> seek to position
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>time left</code></p>
<dd>
<pre>Shows remaining playback time timestamp</pre>
<p><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> left-click </td>
<td> toggle between total and remaining time
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>audio and sub</code></p>
<dd>
<pre>Displays selected track and amount of available tracks</pre>
<p><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> left-click </td>
<td> cycle audio/sub tracks forward
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> right-click </td>
<td> cycle audio/sub tracks backwards
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> shift+L-click </td>
<td> show available audio/sub tracks
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>vol</code></p>
<dd><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> left-click </td>
<td> toggle mute
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> mouse wheel </td>
<td> volume up/down
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>fs</code></p>
<dd><center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> left-click </td>
<td> toggle fullscreen
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></dl>
<h3>Key Bindings</h3>
<p>These key bindings are active by default if nothing else is already bound to these keys. In case of collision, the function needs to be bound to a different key. See the <i>Script Commands</i> section. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> del </td>
<td> Cycles visibility between never / auto (mouse-move) / always
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h3>Configuration</h3>
<p>The OSC offers limited configuration through a config file <code>script-opts/osc.conf</code> placed in mpv&#8217;s user dir and through the <code>&#8211;script-opts</code> command-line option. Options provided through the command-line will override those from the config file.</p>
<h3>Config Syntax</h3>
<p>The config file must exactly follow the following syntax: </p>
<pre># this is a comment
optionA=value1
optionB=value2</pre>
<p><code>#</code> can only be used at the beginning of a line and there may be no spaces around the <code>=</code> or anywhere else.</p>
<h3>Command-line Syntax</h3>
<p>To avoid collisions with other scripts, all options need to be prefixed with <code>osc-</code>. </p>
<p> Example: </p>
<pre>--script-opts=osc-optionA=value1,osc-optionB=value2</pre>
<h3>Configurable Options</h3>
<dl COMPACT>
<dt><code>layout</code></p>
<dd>Default: bottombar </p>
<p> The layout for the OSC. Currently available are: box, slimbox, bottombar and topbar. Default pre-0.21.0 was &#8216;box&#8217;.</p>
<dt><code>seekbarstyle</code></p>
<dd>Default: bar </p>
<p> Sets the style of the playback position marker and overall shape of the seekbar: <code>bar</code>, <code>diamond</code> or <code>knob</code>.</p>
<dt><code>seekbarhandlesize</code></p>
<dd>Default: 0.6 </p>
<p> Size ratio of the seek handle if <code>seekbarstyle</code> is set to <code>dimaond</code> or <code>knob</code>. This is relative to the full height of the seekbar.</p>
<dt><code>seekbarkeyframes</code></p>
<dd>Default: yes </p>
<p> Controls the mode used to seek when dragging the seekbar. If set to <code>yes</code>, default seeking mode is used (usually keyframes, but player defaults and heuristics can change it to exact). If set to <code>no</code>, exact seeking on mouse drags will be used instead. Keyframes are preferred, but exact seeks may be useful in cases where keyframes cannot be found. Note that using exact seeks can potentially make mouse dragging much slower.</p>
<dt><code>seekrangestyle</code></p>
<dd>Default: inverted </p>
<p> Display seekable ranges on the seekbar. <code>bar</code> shows them on the full height of the bar, <code>line</code> as a thick line and <code>inverted</code> as a thin line that is inverted over playback position markers. <code>none</code> will hide them. Additionally, <code>slider</code> will show a permanent handle inside the seekbar with cached ranges marked inside. Note that these will look differently based on the seekbarstyle option. Also, <code>slider</code> does not work with <code>seekbarstyle</code> set to <code>bar</code>.</p>
<dt><code>seekrangeseparate</code></p>
<dd>Default: yes </p>
<p> Controls whether to show line-style seekable ranges on top of the seekbar or separately if <code>seekbarstyle</code> is set to <code>bar</code>.</p>
<dt><code>seekrangealpha</code></p>
<dd>Default: 200 </p>
<p> Alpha of the seekable ranges, 0 (opaque) to 255 (fully transparent).</p>
<dt><code>deadzonesize</code></p>
<dd>Default: 0.5 </p>
<p> Size of the deadzone. The deadzone is an area that makes the mouse act like leaving the window. Movement there won&#8217;t make the OSC show up and it will hide immediately if the mouse enters it. The deadzone starts at the window border opposite to the OSC and the size controls how much of the window it will span. Values between 0.0 and 1.0, where 0 means the OSC will always popup with mouse movement in the window, and 1 means the OSC will only show up when the mouse hovers it. Default pre-0.21.0 was 0.</p>
<dt><code>minmousemove</code></p>
<dd>Default: 0 </p>
<p> Minimum amount of pixels the mouse has to move between ticks to make the OSC show up. Default pre-0.21.0 was 3.</p>
<dt><code>showwindowed</code></p>
<dd>Default: yes </p>
<p> Enable the OSC when windowed</p>
<dt><code>showfullscreen</code></p>
<dd>Default: yes </p>
<p> Enable the OSC when fullscreen</p>
<dt><code>scalewindowed</code></p>
<dd>Default: 1.0 </p>
<p> Scale factor of the OSC when windowed.</p>
<dt><code>scalefullscreen</code></p>
<dd>Default: 1.0 </p>
<p> Scale factor of the OSC when fullscreen</p>
<dt><code>scaleforcedwindow</code></p>
<dd>Default: 2.0 </p>
<p> Scale factor of the OSC when rendered on a forced (dummy) window</p>
<dt><code>vidscale</code></p>
<dd>Default: yes </p>
<p> Scale the OSC with the video <code>no</code> tries to keep the OSC size constant as much as the window size allows</p>
<dt><code>valign</code></p>
<dd>Default: 0.8 </p>
<p> Vertical alignment, -1 (top) to 1 (bottom)</p>
<dt><code>halign</code></p>
<dd>Default: 0.0 </p>
<p> Horizontal alignment, -1 (left) to 1 (right)</p>
<dt><code>barmargin</code></p>
<dd>Default: 0 </p>
<p> Margin from bottom (bottombar) or top (topbar), in pixels</p>
<dt><code>boxalpha</code></p>
<dd>Default: 80 </p>
<p> Alpha of the background box, 0 (opaque) to 255 (fully transparent)</p>
<dt><code>hidetimeout</code></p>
<dd>Default: 500 </p>
<p> Duration in ms until the OSC hides if no mouse movement, must not be negative</p>
<dt><code>fadeduration</code></p>
<dd>Default: 200 </p>
<p> Duration of fade out in ms, 0 = no fade</p>
<dt><code>title</code></p>
<dd>Default: ${media-title} </p>
<p> String that supports property expansion that will be displayed as OSC title. ASS tags are escaped, and newlines and trailing slashes are stripped.</p>
<dt><code>tooltipborder</code></p>
<dd>Default: 1 </p>
<p> Size of the tooltip outline when using bottombar or topbar layouts</p>
<dt><code>timetotal</code></p>
<dd>Default: no </p>
<p> Show total time instead of time remaining</p>
<dt><code>timems</code></p>
<dd>Default: no </p>
<p> Display timecodes with milliseconds</p>
<dt><code>visibility</code></p>
<dd>Default: auto (auto hide/show on mouse move) </p>
<p> Also supports <code>never</code> and <code>always</code></p>
<dt><code>boxmaxchars</code></p>
<dd>Default: 80 </p>
<p> Max chars for the osc title at the box layout. mpv does not measure the text width on screen and so it needs to limit it by number of chars. The default is conservative to allow wide fonts to be used without overflow. However, with many common fonts a bigger number can be used. YMMV.</p>
<dt><code>boxvideo</code></p>
<dd>Default: no </p>
<p> Whether to overlay the osc over the video (<code>no</code>), or to box the video within the areas not covered by the osc (<code>yes</code>). If this option is set, the osc may overwrite the <code>&#8211;video-margin-ratio-*</code> options, even if the user has set them. (It will not overwrite them if all of them are set to default values.) Additionally, <code>visibility</code> must be set to <code>always</code>. Otherwise, this option does nothing. </p>
<p> Currently, this is supported for the <code>bottombar</code> and <code>topbar</code> layout only. The other layouts do not change if this option is set. Separately, if window controls are present (see below), they will be affected regardless of which osc layout is in use. </p>
<p> The border is static and appears even if the OSC is configured to appear only on mouse interaction. If the OSC is invisible, the border is simply filled with the background color (black by default). </p>
<p> This currently still makes the OSC overlap with subtitles (if the <code>&#8211;sub-use-margins</code> option is set to <code>yes</code>, the default). This may be fixed later. </p>
<p> This does not work correctly with video outputs like <code>&#8211;vo=xv</code>, which render OSD into the unscaled video.</p>
<dt><code>windowcontrols</code></p>
<dd>Default: auto (Show window controls if there is no window border) </p>
<p> Whether to show window management controls over the video, and if so, which side of the window to place them. This may be desirable when the window has no decorations, either because they have been explicitly disabled (<code>border=no</code>) or because the current platform doesn&#8217;t support them (eg: gnome-shell with wayland). </p>
<p> The set of window controls is fixed, offering <code>minimize</code>, <code>maximize</code>, and <code>quit</code>. Not all platforms implement <code>minimize</code> and <code>maximize</code>, but <code>quit</code> will always work.</p>
<dt><code>windowcontrols_alignment</code></p>
<dd>Default: right </p>
<p> If window controls are shown, indicates which side should they be aligned to. </p>
<p> Supports <code>left</code> and <code>right</code> which will place the controls on those respective sides.</p>
<dt><code>greenandgrumpy</code></p>
<dd>Default: no </p>
<p> Set to <code>yes</code> to reduce festivity (i.e. disable santa hat in December.)</p>
<dt><code>livemarkers</code></p>
<dd>Default: yes </p>
<p> Update chapter markers positions on duration changes, e.g. live streams. The updates are unoptimized &#8211; consider disabling it on very low-end systems.</dl>
<h3>Script Commands</h3>
<p>The OSC script listens to certain script commands. These commands can bound in <code>input.conf</code>, or sent by other scripts.</p>
<dl COMPACT>
<dt><code>osc-message</code></p>
<dd>Show a message on screen using the OSC. First argument is the message, second the duration in seconds.</p>
<dt><code>osc-visibility</code></p>
<dd>Controls visibility mode <code>never</code> / <code>auto</code> (on mouse move) / <code>always</code> and also <code>cycle</code> to cycle between the modes </p>
<p> Example </p>
<p> You could put this into <code>input.conf</code> to hide the OSC with the <code>a</code> key and to set auto mode (the default) with <code>b</code>: </p>
<pre>a script-message osc-visibility never
b script-message osc-visibility auto</pre>
<dt><code>osc-playlist</code>, <code>osc-chapterlist</code>, <code>osc-tracklist</code></p>
<dd>Shows a limited view of the respective type of list using the OSC. First argument is duration in seconds.</dl>
<h2>Stats</h2>
<p>This builtin script displays information and statistics for the currently played file. It is enabled by default if mpv was compiled with Lua support. It can be disabled entirely using the <code>&#8211;load-stats-overlay=no</code> option.</p>
<h3>Usage</h3>
<p>The following key bindings are active by default unless something else is already bound to them: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> i </td>
<td> Show stats for a fixed duration
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> I </td>
<td> Toggle stats (shown until toggled again)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> While the stats are visible on screen the following key bindings are active, regardless of existing bindings. They allow you to switch between <i>pages</i> of stats: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 1 </td>
<td> Show usual stats
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 2 </td>
<td> Show frame timings (scroll)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 3 </td>
<td> Input cache stats
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 4 </td>
<td> Active key bindings (scroll)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 0 </td>
<td> Internal stuff (scroll)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> On pages which support scroll, these key bindings are also active: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> UP </td>
<td> Scroll one line up
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> DOWN </td>
<td> Scroll one line down
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h3>Font</h3>
<p>For optimal visual experience, a font with support for many font weights and monospaced digits is recommended. By default, the open source font <i>Source Sans Pro</i> is used.</p>
<h3>Configuration</h3>
<p>This script can be customized through a config file <code>script-opts/stats.conf</code> placed in mpv&#8217;s user directory and through the <code>&#8211;script-opts</code> command-line option. The configuration syntax is described in <i>ON SCREEN CONTROLLER</i>.</p>
<h3>Configurable Options</h3>
<dl COMPACT>
<dt><code>key_page_1</code></p>
<dd>Default: 1</p>
<dt><code>key_page_2</code></p>
<dd>Default: 2</p>
<dt><code>key_page_3</code></p>
<dd>Default: 3</p>
<dt><code>key_page_4</code></p>
<dd>Default: 4</p>
<dt><code>key_page_0</code></p>
<dd>Default: 0 </p>
<p> Key bindings for page switching while stats are displayed.</p>
<dt><code>key_scroll_up</code></p>
<dd>Default: UP</p>
<dt><code>key_scroll_down</code></p>
<dd>Default: DOWN</p>
<dt><code>scroll_lines</code></p>
<dd>Default: 1 </p>
<p> Scroll key bindings and number of lines to scroll on pages which support it.</p>
<dt><code>duration</code></p>
<dd>Default: 4 </p>
<p> How long the stats are shown in seconds (oneshot).</p>
<dt><code>redraw_delay</code></p>
<dd>Default: 1 </p>
<p> How long it takes to refresh the displayed stats in seconds (toggling).</p>
<dt><code>persistent_overlay</code></p>
<dd>Default: no </p>
<p> When <i>no</i>, other scripts printing text to the screen can overwrite the displayed stats. When <i>yes</i>, displayed stats are persistently shown for the respective duration. This can result in overlapping text when multiple scripts decide to print text at the same time.</p>
<dt><code>plot_perfdata</code></p>
<dd>Default: yes </p>
<p> Show graphs for performance data (page 2).</p>
<dt><code>plot_vsync_ratio</code></p>
<dd>Default: yes</p>
<dt><code>plot_vsync_jitter</code></p>
<dd>Default: yes </p>
<p> Show graphs for vsync and jitter values (page 1). Only when toggled.</p>
<dt><code>flush_graph_data</code></p>
<dd>Default: yes </p>
<p> Clear data buffers used for drawing graphs when toggling.</p>
<dt><code>font</code></p>
<dd>Default: Source Sans Pro </p>
<p> Font name. Should support as many font weights as possible for optimal visual experience.</p>
<dt><code>font_mono</code></p>
<dd>Default: Source Sans Pro </p>
<p> Font name for parts where monospaced characters are necessary to align text. Currently, monospaced digits are sufficient.</p>
<dt><code>font_size</code></p>
<dd>Default: 8 </p>
<p> Font size used to render text.</p>
<dt><code>font_color</code></p>
<dd>Default: FFFFFF </p>
<p> Font color.</p>
<dt><code>border_size</code></p>
<dd>Default: 0.8 </p>
<p> Size of border drawn around the font.</p>
<dt><code>border_color</code></p>
<dd>Default: 262626 </p>
<p> Color of drawn border.</p>
<dt><code>alpha</code></p>
<dd>Default: 11 </p>
<p> Transparency for drawn text.</p>
<dt><code>plot_bg_border_color</code></p>
<dd>Default: 0000FF </p>
<p> Border color used for drawing graphs.</p>
<dt><code>plot_bg_color</code></p>
<dd>Default: 262626 </p>
<p> Background color used for drawing graphs.</p>
<dt><code>plot_color</code></p>
<dd>Default: FFFFFF </p>
<p> Color used for drawing graphs. </p>
<p> Note: colors are given as hexadecimal values and use ASS tag order: BBGGRR (blue green red).</dl>
<h3>Different key bindings</h3>
<p>Additional keys can be configured in <code>input.conf</code> to display the stats: </p>
<pre>e script-binding stats/display-stats
E script-binding stats/display-stats-toggle</pre>
<p>And to display a certain page directly: </p>
<pre>i script-binding stats/display-page-1
e script-binding stats/display-page-2</pre>
<h3>Active key bindings page</h3>
<p>Lists the active key bindings and the commands they&#8217;re bound to, excluding the interactive keys of the stats script itself. See also <code>&#8211;input-test</code> for more detailed view of each binding. </p>
<p> The keys are grouped automatically using a simple analysis of the command string, and one should not expect documentation-level grouping accuracy, however, it should still be reasonably useful. </p>
<p> Using <code>&#8211;idle &#8211;script-opts=stats-bindlist=yes</code> will print the list to the terminal and quit immediately. By default long lines are shortened to 79 chars, and terminal escape sequences are enabled. A different length limit can be set by changing <code>yes</code> to a number (at least 40), and escape sequences can be disabled by adding <code>&#8211;</code> before the value, e.g. <code>&#8230;=-yes</code> or <code>&#8230;=-120</code>. </p>
<p> Like with <code>&#8211;input-test</code>, the list includes bindings from <code>input.conf</code> and from user scripts. Use <code>&#8211;no-config</code> to list only built-in bindings.</p>
<h3>Internal stuff page</h3>
<p>Most entries shown on this page have rather vague meaning. Likely none of this is useful for you. Don&#8217;t attempt to use it. Forget its existence. </p>
<p> Selecting this for the first time will start collecting some internal performance data. That means performance will be slightly lower than normal for the rest of the time the player is running (even if the stats page is closed). Note that the stats page itself uses a lot of CPU and even GPU resources, and may have a heavy impact on performance. </p>
<p> The displayed information is accumulated over the redraw delay (shown as <code>poll-time</code> field). </p>
<p> This adds entries for each Lua script. If there are too many scripts running, parts of the list will simply be out of the screen, but it can be scrolled. </p>
<p> If the underlying platform does not support pthread per thread times, the displayed times will be 0 or something random (I suspect that at time of this writing, only Linux provides the correct via pthread APIs for per thread times). </p>
<p> Most entries are added lazily and only during data collection, which is why entries may pop up randomly after some time. It&#8217;s also why the memory usage entries for scripts that have been inactive since the start of data collection are missing. </p>
<p> Memory usage is approximate and does not reflect internal fragmentation. </p>
<p> JS scripts memory reporting is disabled by default because collecting the data at the JS side has an overhead. It can be enabled by exporting the env var <code>MPV_LEAK_REPORT=1</code> before starting mpv, and will increase JS memory usage. </p>
<p> If entries have <code>/time</code> and <code>/cpu</code> variants, the former gives the real time (monotonic clock), while the latter the thread CPU time (only if the corresponding pthread API works and is supported).</p>
<h2>Console</h2>
<p>The console is a REPL for mpv input commands. It is displayed on the video window. It also shows log messages. It can be disabled entirely using the <code>&#8211;load-osd-console=no</code> option.</p>
<h3>Keybindings</h3>
<dl COMPACT>
<dt><code>`</code></p>
<dd>Show the console.</p>
<dt><code>ESC</code></p>
<dd>Hide the console.</p>
<dt><code>ENTER, Ctrl+J and Ctrl+M</code></p>
<dd>Run the typed command.</p>
<dt><code>Shift+ENTER</code></p>
<dd>Type a literal newline character.</p>
<dt><code>LEFT and Ctrl+B</code></p>
<dd>Move the cursor to the previous character.</p>
<dt><code>RIGHT and Ctrl+F</code></p>
<dd>Move the cursor to the next character.</p>
<dt><code>Ctrl+LEFT and Alt+B</code></p>
<dd>Move the cursor to the beginning of the current word, or if between words, to the beginning of the previous word.</p>
<dt><code>Ctrl+RIGHT and Alt+F</code></p>
<dd>Move the cursor to the end of the current word, or if between words, to the end of the next word.</p>
<dt><code>HOME and Ctrl+A</code></p>
<dd>Move the cursor to the start of the current line.</p>
<dt><code>END and Ctrl+E</code></p>
<dd>Move the cursor to the end of the current line.</p>
<dt><code>BACKSPACE and Ctrl+H</code></p>
<dd>Delete the previous character.</p>
<dt><code>Ctrl+D</code></p>
<dd>Hide the console if the current line is empty, otherwise delete the next character.</p>
<dt><code>Ctrl+BACKSPACE and Ctrl+W</code></p>
<dd>Delete text from the cursor to the beginning of the current word, or if between words, to the beginning of the previous word.</p>
<dt><code>Ctrl+DEL and Alt+D</code></p>
<dd>Delete text from the cursor to the end of the current word, or if between words, to the end of the next word.</p>
<dt><code>Ctrl+U</code></p>
<dd>Delete text from the cursor to the beginning of the current line.</p>
<dt><code>Ctrl+K</code></p>
<dd>Delete text from the cursor to the end of the current line.</p>
<dt><code>Ctrl+C</code></p>
<dd>Clear the current line.</p>
<dt><code>UP and Ctrl+P</code></p>
<dd>Move back in the command history.</p>
<dt><code>DOWN and Ctrl+N</code></p>
<dd>Move forward in the command history.</p>
<dt><code>PGUP</code></p>
<dd>Go to the first command in the history.</p>
<dt><code>PGDN</code></p>
<dd>Stop navigating the command history.</p>
<dt><code>INSERT</code></p>
<dd>Toggle insert mode.</p>
<dt><code>Ctrl+V</code></p>
<dd>Paste text (uses the clipboard on X11 and Wayland).</p>
<dt><code>Shift+INSERT</code></p>
<dd>Paste text (uses the primary selection on X11 and Wayland).</p>
<dt><code>TAB and Ctrl+I</code></p>
<dd>Complete the command or property name at the cursor.</p>
<dt><code>Ctrl+L</code></p>
<dd>Clear all log messages from the console.</dl>
<h3>Commands</h3>
<dl COMPACT>
<dt><code>script-message-to console type &lt;text&gt; [&lt;cursor_pos&gt;]</code></p>
<dd>Show the console and pre-fill it with the provided text, optionally specifying the initial cursor position as a positive integer starting from 1.</p>
<dt>Example for input.conf</p>
<dd><code>% script-message-to console type &quot;seek absolute-percent&quot; 6</code></dl>
<h3>Known issues</h3>
<dl COMPACT>
<dt>&bull;</p>
<dd>Pasting text is slow on Windows</p>
<dt>&bull;</p>
<dd>Non-ASCII keyboard input has restrictions</p>
<dt>&bull;</p>
<dd>The cursor keys move between Unicode code-points, not grapheme clusters</dl>
<h3>Configuration</h3>
<p>This script can be customized through a config file <code>script-opts/console.conf</code> placed in mpv&#8217;s user directory and through the <code>&#8211;script-opts</code> command-line option. The configuration syntax is described in <i>ON SCREEN CONTROLLER</i>. </p>
<p> Key bindings can be changed in a standard way, see for example stats.lua documentation.</p>
<h3>Configurable Options</h3>
<dl COMPACT>
<dt><code>scale</code></p>
<dd>Default: 1 </p>
<p> All drawing is scaled by this value, including the text borders and the cursor. </p>
<p> If the VO backend in use has HiDPI scale reporting implemented, the option value is scaled with the reported HiDPI scale.</p>
<dt><code>font</code></p>
<dd>Default: unset (picks a hardcoded font depending on detected platform) </p>
<p> Set the font used for the REPL and the console. This probably doesn&#8217;t have to be a monospaced font.</p>
<dt><code>font_size</code></p>
<dd>Default: 16 </p>
<p> Set the font size used for the REPL and the console. This will be multiplied by &quot;scale.&quot;</dl>
<h2>Lua Scripting</h2>
<p>mpv can load Lua scripts. (See <i>Script location</i>.) </p>
<p> mpv provides the built-in module <code>mp</code>, which contains functions to send commands to the mpv core and to retrieve information about playback state, user settings, file information, and so on. </p>
<p> These scripts can be used to control mpv in a similar way to slave mode. Technically, the Lua code uses the client API internally.</p>
<h3>Example</h3>
<p>A script which leaves fullscreen mode when the player is paused: </p>
<pre>function on_pause_change(name, value)
 if value == true then
 mp.set_property(&quot;fullscreen&quot;, &quot;no&quot;)
 end
end
mp.observe_property(&quot;pause&quot;, &quot;bool&quot;, on_pause_change)</pre>
<h3>Script location</h3>
<p>Scripts can be passed to the <code>&#8211;script</code> option, and are automatically loaded from the <code>scripts</code> subdirectory of the mpv configuration directory (usually <code>~/.config/mpv/scripts/</code>). </p>
<p> A script can be a single file. The file extension is used to select the scripting backend to use for it. For Lua, it is <code>.lua</code>. If the extension is not recognized, an error is printed. (If an error happens, the extension is either mistyped, or the backend was not compiled into your mpv binary.) </p>
<p> mpv internally loads the script&#8217;s name by stripping the <code>.lua</code> extension and replacing all nonalphanumeric characters with <code>_</code>. E.g., <code>my-tools.lua</code> becomes <code>my_tools</code>. If there are several scripts with the same name, it is made unique by appending a number. This is the name returned by <code>mp.get_script_name()</code>. </p>
<p> Entries with <code>.disable</code> extension are always ignored. </p>
<p> If a script is a directory (either if a directory is passed to <code>&#8211;script</code>, or any sub-directories in the script directory, such as for example <code>~/.config/mpv/scripts/something/</code>), then the directory represents a single script. The player will try to load a file named <code>main.x</code>, where <code>x</code> is replaced with the file extension. For example, if <code>main.lua</code> exists, it is loaded with the Lua scripting backend. </p>
<p> You must not put any other files or directories that start with <code>main.</code> into the script&#8217;s top level directory. If the script directory contains for example both <code>main.lua</code> and <code>main.js</code>, only one of them will be loaded (and which one depends on mpv internals that may change any time). Likewise, if there is for example <code>main.foo</code>, your script will break as soon as mpv adds a backend that uses the <code>.foo</code> file extension. </p>
<p> mpv also appends the top level directory of the script to the start of Lua&#8217;s package path so you can import scripts from there too. Be aware that this will shadow Lua libraries that use the same package path. (Single file scripts do not include mpv specific directory the Lua package path. This was silently changed in mpv 0.32.0.) </p>
<p> Using a script directory is the recommended way to package a script that consists of multiple source files, or requires other files (you can use <code>mp.get_script_directory()</code> to get the location and e.g. load data files). </p>
<p> Making a script a git repository, basically a repository which contains a <code>main.lua`</code> file in the root directory, makes scripts easily updateable (without the dangers of auto-updates). Another suggestion is to use git submodules to share common files or libraries.</p>
<h3>Details on the script initialization and lifecycle</h3>
<p>Your script will be loaded by the player at program start from the <code>scripts</code> configuration subdirectory, or from a path specified with the <code>&#8211;script</code> option. Some scripts are loaded internally (like <code>&#8211;osc</code>). Each script runs in its own thread. Your script is first run &quot;as is&quot;, and once that is done, the event loop is entered. This event loop will dispatch events received by mpv and call your own event handlers which you have registered with <code>mp.register_event</code>, or timers added with <code>mp.add_timeout</code> or similar. Note that since the script starts execution concurrently with player initialization, some properties may not be populated with meaningful values until the relevant subsystems have initialized. </p>
<p> When the player quits, all scripts will be asked to terminate. This happens via a <code>shutdown</code> event, which by default will make the event loop return. If your script got into an endless loop, mpv will probably behave fine during playback, but it won&#8217;t terminate when quitting, because it&#8217;s waiting on your script. </p>
<p> Internally, the C code will call the Lua function <code>mp_event_loop</code> after loading a Lua script. This function is normally defined by the default prelude loaded before your script (see <code>player/lua/defaults.lua</code> in the mpv sources). The event loop will wait for events and dispatch events registered with <code>mp.register_event</code>. It will also handle timers added with <code>mp.add_timeout</code> and similar (by waiting with a timeout). </p>
<p> Since mpv 0.6.0, the player will wait until the script is fully loaded before continuing normal operation. The player considers a script as fully loaded as soon as it starts waiting for mpv events (or it exits). In practice this means the player will more or less hang until the script returns from the main chunk (and <code>mp_event_loop</code> is called), or the script calls <code>mp_event_loop</code> or <code>mp.dispatch_events</code> directly. This is done to make it possible for a script to fully setup event handlers etc. before playback actually starts. In older mpv versions, this happened asynchronously. With mpv 0.29.0, this changes slightly, and it merely waits for scripts to be loaded in this manner before starting playback as part of the player initialization phase. Scripts run though initialization in parallel. This might change again.</p>
<h3>mp functions</h3>
<p>The <code>mp</code> module is preloaded, although it can be loaded manually with <code>require &#8216;mp&#8217;</code>. It provides the core client API.</p>
<dl COMPACT>
<dt><code>mp.command(string)</code></p>
<dd>Run the given command. This is similar to the commands used in input.conf. See <i>List of Input Commands</i>. </p>
<p> By default, this will show something on the OSD (depending on the command), as if it was used in <code>input.conf</code>. See <i>Input Command Prefixes</i> how to influence OSD usage per command. </p>
<p> Returns <code>true</code> on success, or <code>nil, error</code> on error.</p>
<dt><code>mp.commandv(arg1, arg2, &#8230;)</code></p>
<dd>Similar to <code>mp.command</code>, but pass each command argument as separate parameter. This has the advantage that you don&#8217;t have to care about quoting and escaping in some cases. </p>
<p> Example: </p>
<pre>mp.command(&quot;loadfile &quot; .. filename .. &quot; append&quot;)
mp.commandv(&quot;loadfile&quot;, filename, &quot;append&quot;)</pre>
<p>These two commands are equivalent, except that the first version breaks if the filename contains spaces or certain special characters. </p>
<p> Note that properties are <i>not</i> expanded. You can use either <code>mp.command</code>, the <code>expand-properties</code> prefix, or the <code>mp.get_property</code> family of functions. </p>
<p> Unlike <code>mp.command</code>, this will not use OSD by default either (except for some OSD-specific commands).</p>
<dt><code>mp.command_native(table [,def])</code></p>
<dd>Similar to <code>mp.commandv</code>, but pass the argument list as table. This has the advantage that in at least some cases, arguments can be passed as native types. It also allows you to use named argument. </p>
<p> If the table is an array, each array item is like an argument in <code>mp.commandv()</code> (but can be a native type instead of a string). </p>
<p> If the table contains string keys, it&#8217;s interpreted as command with named arguments. This requires at least an entry with the key <code>name</code> to be present, which must be a string, and contains the command name. The special entry <code>_flags</code> is optional, and if present, must be an array of <i>Input Command Prefixes</i> to apply. All other entries are interpreted as arguments. </p>
<p> Returns a result table on success (usually empty), or <code>def, error</code> on error. <code>def</code> is the second parameter provided to the function, and is nil if it&#8217;s missing.</p>
<dt><code>mp.command_native_async(table [,fn])</code></p>
<dd>Like <code>mp.command_native()</code>, but the command is ran asynchronously (as far as possible), and upon completion, fn is called. fn has three arguments: <code>fn(success, result, error)</code>:</p>
<dt><code>success</code></p>
<dd>Always a Boolean and is true if the command was successful, otherwise false.</p>
<dt><code>result</code></p>
<dd>The result value (can be nil) in case of success, nil otherwise (as returned by <code>mp.command_native()</code>).</p>
<dt><code>error</code></p>
<dd>The error string in case of an error, nil otherwise. </p>
<p> Returns a table with undefined contents, which can be used as argument for <code>mp.abort_async_command</code>. </p>
<p> If starting the command failed for some reason, <code>nil, error</code> is returned, and <code>fn</code> is called indicating failure, using the same error value.</p>
<dt><code>mp.abort_async_command(t)</code></p>
<dd>Abort a <code>mp.command_native_async</code> call. The argument is the return value of that command (which starts asynchronous execution of the command). Whether this works and how long it takes depends on the command and the situation. The abort call itself is asynchronous. Does not return anything.</p>
<dt><code>mp.get_property(name [,def])</code></p>
<dd>Return the value of the given property as string. These are the same properties as used in input.conf. See <i>Properties</i> for a list of properties. The returned string is formatted similar to <code>${=name}</code> (see <i>Property Expansion</i>). </p>
<p> Returns the string on success, or <code>def, error</code> on error. <code>def</code> is the second parameter provided to the function, and is nil if it&#8217;s missing.</p>
<dt><code>mp.get_property_osd(name [,def])</code></p>
<dd>Similar to <code>mp.get_property</code>, but return the property value formatted for OSD. This is the same string as printed with <code>${name}</code> when used in input.conf. </p>
<p> Returns the string on success, or <code>def, error</code> on error. <code>def</code> is the second parameter provided to the function, and is an empty string if it&#8217;s missing. Unlike <code>get_property()</code>, assigning the return value to a variable will always result in a string.</p>
<dt><code>mp.get_property_bool(name [,def])</code></p>
<dd>Similar to <code>mp.get_property</code>, but return the property value as Boolean. </p>
<p> Returns a Boolean on success, or <code>def, error</code> on error.</p>
<dt><code>mp.get_property_number(name [,def])</code></p>
<dd>Similar to <code>mp.get_property</code>, but return the property value as number. </p>
<p> Note that while Lua does not distinguish between integers and floats, mpv internals do. This function simply request a double float from mpv, and mpv will usually convert integer property values to float. </p>
<p> Returns a number on success, or <code>def, error</code> on error.</p>
<dt><code>mp.get_property_native(name [,def])</code></p>
<dd>Similar to <code>mp.get_property</code>, but return the property value using the best Lua type for the property. Most time, this will return a string, Boolean, or number. Some properties (for example <code>chapter-list</code>) are returned as tables. </p>
<p> Returns a value on success, or <code>def, error</code> on error. Note that <code>nil</code> might be a possible, valid value too in some corner cases.</p>
<dt><code>mp.set_property(name, value)</code></p>
<dd>Set the given property to the given string value. See <code>mp.get_property</code> and <i>Properties</i> for more information about properties. </p>
<p> Returns true on success, or <code>nil, error</code> on error.</p>
<dt><code>mp.set_property_bool(name, value)</code></p>
<dd>Similar to <code>mp.set_property</code>, but set the given property to the given Boolean value.</p>
<dt><code>mp.set_property_number(name, value)</code></p>
<dd>Similar to <code>mp.set_property</code>, but set the given property to the given numeric value. </p>
<p> Note that while Lua does not distinguish between integers and floats, mpv internals do. This function will test whether the number can be represented as integer, and if so, it will pass an integer value to mpv, otherwise a double float.</p>
<dt><code>mp.set_property_native(name, value)</code></p>
<dd>Similar to <code>mp.set_property</code>, but set the given property using its native type. </p>
<p> Since there are several data types which cannot represented natively in Lua, this might not always work as expected. For example, while the Lua wrapper can do some guesswork to decide whether a Lua table is an array or a map, this would fail with empty tables. Also, there are not many properties for which it makes sense to use this, instead of <code>set_property</code>, <code>set_property_bool</code>, <code>set_property_number</code>. For these reasons, this function should probably be avoided for now, except for properties that use tables natively.</p>
<dt><code>mp.get_time()</code></p>
<dd>Return the current mpv internal time in seconds as a number. This is basically the system time, with an arbitrary offset.</p>
<dt><code>mp.add_key_binding(key, name|fn [,fn [,flags]])</code></p>
<dd>Register callback to be run on a key binding. The binding will be mapped to the given <code>key</code>, which is a string describing the physical key. This uses the same key names as in input.conf, and also allows combinations (e.g. <code>ctrl+a</code>). If the key is empty or <code>nil</code>, no physical key is registered, but the user still can create own bindings (see below). </p>
<p> After calling this function, key presses will cause the function <code>fn</code> to be called (unless the user remapped the key with another binding). </p>
<p> The <code>name</code> argument should be a short symbolic string. It allows the user to remap the key binding via input.conf using the <code>script-message</code> command, and the name of the key binding (see below for an example). The name should be unique across other bindings in the same script &#8211; if not, the previous binding with the same name will be overwritten. You can omit the name, in which case a random name is generated internally. (Omitting works as follows: either pass <code>nil</code> for <code>name</code>, or pass the <code>fn</code> argument in place of the name. The latter is not recommended and is handled for compatibility only.) </p>
<p> The last argument is used for optional flags. This is a table, which can have the following entries:</p>
<dt><code>repeatable</code></p>
<dd>If set to <code>true</code>, enables key repeat for this specific binding.</p>
<dt><code>complex</code></p>
<dd>If set to <code>true</code>, then <code>fn</code> is called on both key up and down events (as well as key repeat, if enabled), with the first argument being a table. This table has the following entries (and may contain undocumented ones):</p>
<dt><code>event</code></p>
<dd>Set to one of the strings <code>down</code>, <code>repeat</code>, <code>up</code> or <code>press</code> (the latter if key up/down can&#8217;t be tracked).</p>
<dt><code>is_mouse</code></p>
<dd>Boolean Whether the event was caused by a mouse button.</p>
<dt><code>key_name</code></p>
<dd>The name of they key that triggered this, or <code>nil</code> if invoked artificially. If the key name is unknown, it&#8217;s an empty string.</p>
<dt><code>key_text</code></p>
<dd>Text if triggered by a text key, otherwise <code>nil</code>. See description of <code>script-binding</code> command for details (this field is equivalent to the 5th argument). </p>
<p> Internally, key bindings are dispatched via the <code>script-message-to</code> or <code>script-binding</code> input commands and <code>mp.register_script_message</code>. </p>
<p> Trying to map multiple commands to a key will essentially prefer a random binding, while the other bindings are not called. It is guaranteed that user defined bindings in the central input.conf are preferred over bindings added with this function (but see <code>mp.add_forced_key_binding</code>). </p>
<p> Example: </p>
<pre>function something_handler()
 print(&quot;the key was pressed&quot;)
end
mp.add_key_binding(&quot;x&quot;, &quot;something&quot;, something_handler)</pre>
<p>This will print the message <code>the key was pressed</code> when <code>x</code> was pressed. </p>
<p> The user can remap these key bindings. Then the user has to put the following into their input.conf to remap the command to the <code>y</code> key: </p>
<pre>y script-binding something</pre>
<p>This will print the message when the key <code>y</code> is pressed. (<code>x</code> will still work, unless the user remaps it.) </p>
<p> You can also explicitly send a message to a named script only. Assume the above script was using the filename <code>fooscript.lua</code>: </p>
<pre>y script-binding fooscript/something</pre>
<dt><code>mp.add_forced_key_binding(&#8230;)</code></p>
<dd>This works almost the same as <code>mp.add_key_binding</code>, but registers the key binding in a way that will overwrite the user&#8217;s custom bindings in their input.conf. (<code>mp.add_key_binding</code> overwrites default key bindings only, but not those by the user&#8217;s input.conf.)</p>
<dt><code>mp.remove_key_binding(name)</code></p>
<dd>Remove a key binding added with <code>mp.add_key_binding</code> or <code>mp.add_forced_key_binding</code>. Use the same name as you used when adding the bindings. It&#8217;s not possible to remove bindings for which you omitted the name.</p>
<dt><code>mp.register_event(name, fn)</code></p>
<dd>Call a specific function when an event happens. The event name is a string, and the function fn is a Lua function value. </p>
<p> Some events have associated data. This is put into a Lua table and passed as argument to fn. The Lua table by default contains a <code>name</code> field, which is a string containing the event name. If the event has an error associated, the <code>error</code> field is set to a string describing the error, on success it&#8217;s not set. </p>
<p> If multiple functions are registered for the same event, they are run in registration order, which the first registered function running before all the other ones. </p>
<p> Returns true if such an event exists, false otherwise. </p>
<p> See <i>Events</i> and <i>List of events</i> for details.</p>
<dt><code>mp.unregister_event(fn)</code></p>
<dd>Undo <code>mp.register_event(&#8230;, fn)</code>. This removes all event handlers that are equal to the <code>fn</code> parameter. This uses normal Lua <code>==</code> comparison, so be careful when dealing with closures.</p>
<dt><code>mp.observe_property(name, type, fn)</code></p>
<dd>Watch a property for changes. If the property <code>name</code> is changed, then the function <code>fn(name)</code> will be called. <code>type</code> can be <code>nil</code>, or be set to one of <code>none</code>, <code>native</code>, <code>bool</code>, <code>string</code>, or <code>number</code>. <code>none</code> is the same as <code>nil</code>. For all other values, the new value of the property will be passed as second argument to <code>fn</code>, using <code>mp.get_property_&lt;type&gt;</code> to retrieve it. This means if <code>type</code> is for example <code>string</code>, <code>fn</code> is roughly called as in <code>fn(name, mp.get_property_string(name))</code>. </p>
<p> If possible, change events are coalesced. If a property is changed a bunch of times in a row, only the last change triggers the change function. (The exact behavior depends on timing and other things.) </p>
<p> If a property is unavailable, or on error, the value argument to <code>fn</code> is <code>nil</code>. (The <code>observe_property()</code> call always succeeds, even if a property does not exist.) </p>
<p> In some cases the function is not called even if the property changes. This depends on the property, and it&#8217;s a valid feature request to ask for better update handling of a specific property. </p>
<p> If the <code>type</code> is <code>none</code> or <code>nil</code>, sporadic property change events are possible. This means the change function <code>fn</code> can be called even if the property doesn&#8217;t actually change. </p>
<p> You always get an initial change notification. This is meant to initialize the user&#8217;s state to the current value of the property.</p>
<dt><code>mp.unobserve_property(fn)</code></p>
<dd>Undo <code>mp.observe_property(&#8230;, fn)</code>. This removes all property handlers that are equal to the <code>fn</code> parameter. This uses normal Lua <code>==</code> comparison, so be careful when dealing with closures.</p>
<dt><code>mp.add_timeout(seconds, fn)</code></p>
<dd>Call the given function fn when the given number of seconds has elapsed. Note that the number of seconds can be fractional. For now, the timer&#8217;s resolution may be as low as 50 ms, although this will be improved in the future. </p>
<p> This is a one-shot timer: it will be removed when it&#8217;s fired. </p>
<p> Returns a timer object. See <code>mp.add_periodic_timer</code> for details.</p>
<dt><code>mp.add_periodic_timer(seconds, fn)</code></p>
<dd>Call the given function periodically. This is like <code>mp.add_timeout</code>, but the timer is re-added after the function fn is run.</p>
<dt><code>Returns a timer object. The timer object provides the following methods:</code></p>
<dd>
<dt><code>stop()</code></p>
<dd>Disable the timer. Does nothing if the timer is already disabled. This will remember the current elapsed time when stopping, so that <code>resume()</code> essentially unpauses the timer.</p>
<dt><code>kill()</code></p>
<dd>Disable the timer. Resets the elapsed time. <code>resume()</code> will restart the timer.</p>
<dt><code>resume()</code></p>
<dd>Restart the timer. If the timer was disabled with <code>stop()</code>, this will resume at the time it was stopped. If the timer was disabled with <code>kill()</code>, or if it&#8217;s a previously fired one-shot timer (added with <code>add_timeout()</code>), this starts the timer from the beginning, using the initially configured timeout.</p>
<dt><code>is_enabled()</code></p>
<dd>Whether the timer is currently enabled or was previously disabled (e.g. by <code>stop()</code> or <code>kill()</code>).</p>
<dt><code>timeout</code> (RW)</p>
<dd>This field contains the current timeout period. This value is not updated as time progresses. It&#8217;s only used to calculate when the timer should fire next when the timer expires. </p>
<p> If you write this, you can call <code>t:kill() ; t:resume()</code> to reset the current timeout to the new one. (<code>t:stop()</code> won&#8217;t use the new timeout.)</p>
<dt><code>oneshot</code> (RW)</p>
<dd>Whether the timer is periodic (<code>false</code>) or fires just once (<code>true</code>). This value is used when the timer expires (but before the timer callback function fn is run). </p>
<p> Note that these are methods, and you have to call them using <code>:</code> instead of <code>.</code> (Refer to <i><a rel="nofollow" href="https://www.lua.org/manual/5.2/manual.html#3.4.9">https://www.lua.org/manual/5.2/manual.html#3.4.9</a></i> .) </p>
<p> Example: </p>
<pre>seconds = 0
timer = mp.add_periodic_timer(1, function()
 print(&quot;called every second&quot;)
 # stop it after 10 seconds
 seconds = seconds + 1
 if seconds &gt;= 10 then
 timer:kill()
 end
end)</pre>
<dt><code>mp.get_opt(key)</code></p>
<dd>Return a setting from the <code>&#8211;script-opts</code> option. It&#8217;s up to the user and the script how this mechanism is used. Currently, all scripts can access this equally, so you should be careful about collisions.</p>
<dt><code>mp.get_script_name()</code></p>
<dd>Return the name of the current script. The name is usually made of the filename of the script, with directory and file extension removed. If there are several scripts which would have the same name, it&#8217;s made unique by appending a number. Any nonalphanumeric characters are replaced with <code>_</code>.</p>
<dt>Example</p>
<dd>The script <code>/path/to/foo-script.lua</code> becomes <code>foo_script</code>.</p>
<dt><code>mp.get_script_directory()</code></p>
<dd>Return the directory if this is a script packaged as directory (see <i>Script location</i> for a description). Return nothing if this is a single file script.</p>
<dt><code>mp.osd_message(text [,duration])</code></p>
<dd>Show an OSD message on the screen. <code>duration</code> is in seconds, and is optional (uses <code>&#8211;osd-duration</code> by default).</dl>
<h3>Advanced mp functions</h3>
<p>These also live in the <code>mp</code> module, but are documented separately as they are useful only in special situations.</p>
<dl COMPACT>
<dt><code>mp.suspend()</code></p>
<dd>This function has been deprecated in mpv 0.21.0 and does nothing starting with mpv 0.23.0 (no replacement).</p>
<dt><code>mp.resume()</code></p>
<dd>This function has been deprecated in mpv 0.21.0 and does nothing starting with mpv 0.23.0 (no replacement).</p>
<dt><code>mp.resume_all()</code></p>
<dd>This function has been deprecated in mpv 0.21.0 and does nothing starting with mpv 0.23.0 (no replacement).</p>
<dt><code>mp.get_wakeup_pipe()</code></p>
<dd>Calls <code>mpv_get_wakeup_pipe()</code> and returns the read end of the wakeup pipe. This is deprecated, but still works. (See <code>client.h</code> for details.)</p>
<dt><code>mp.get_next_timeout()</code></p>
<dd>Return the relative time in seconds when the next timer (<code>mp.add_timeout</code> and similar) expires. If there is no timer, return <code>nil</code>.</p>
<dt><code>mp.dispatch_events([allow_wait])</code></p>
<dd>This can be used to run custom event loops. If you want to have direct control what the Lua script does (instead of being called by the default event loop), you can set the global variable <code>mp_event_loop</code> to your own function running the event loop. From your event loop, you should call <code>mp.dispatch_events()</code> to dequeue and dispatch mpv events. </p>
<p> If the <code>allow_wait</code> parameter is set to <code>true</code>, the function will block until the next event is received or the next timer expires. Otherwise (and this is the default behavior), it returns as soon as the event loop is emptied. It&#8217;s strongly recommended to use <code>mp.get_next_timeout()</code> and <code>mp.get_wakeup_pipe()</code> if you&#8217;re interested in properly working notification of new events and working timers.</p>
<dt><code>mp.register_idle(fn)</code></p>
<dd>Register an event loop idle handler. Idle handlers are called before the script goes to sleep after handling all new events. This can be used for example to delay processing of property change events: if you&#8217;re observing multiple properties at once, you might not want to act on each property change, but only when all change notifications have been received.</p>
<dt><code>mp.unregister_idle(fn)</code></p>
<dd>Undo <code>mp.register_idle(fn)</code>. This removes all idle handlers that are equal to the <code>fn</code> parameter. This uses normal Lua <code>==</code> comparison, so be careful when dealing with closures.</p>
<dt><code>mp.enable_messages(level)</code></p>
<dd>Set the minimum log level of which mpv message output to receive. These messages are normally printed to the terminal. By calling this function, you can set the minimum log level of messages which should be received with the <code>log-message</code> event. See the description of this event for details. The level is a string, see <code>msg.log</code> for allowed log levels.</p>
<dt><code>mp.register_script_message(name, fn)</code></p>
<dd>This is a helper to dispatch <code>script-message</code> or <code>script-message-to</code> invocations to Lua functions. <code>fn</code> is called if <code>script-message</code> or <code>script-message-to</code> (with this script as destination) is run with <code>name</code> as first parameter. The other parameters are passed to <code>fn</code>. If a message with the given name is already registered, it&#8217;s overwritten. </p>
<p> Used by <code>mp.add_key_binding</code>, so be careful about name collisions.</p>
<dt><code>mp.unregister_script_message(name)</code></p>
<dd>Undo a previous registration with <code>mp.register_script_message</code>. Does nothing if the <code>name</code> wasn&#8217;t registered.</p>
<dt><code>mp.create_osd_overlay(format)</code></p>
<dd>Create an OSD overlay. This is a very thin wrapper around the <code>osd-overlay</code> command. The function returns a table, which mostly contains fields that will be passed to <code>osd-overlay</code>. The <code>format</code> parameter is used to initialize the <code>format</code> field. The <code>data</code> field contains the text to be used as overlay. For details, see the <code>osd-overlay</code> command. </p>
<p> In addition, it provides the following methods:</p>
<dt><code>update()</code></p>
<dd>Commit the OSD overlay to the screen, or in other words, run the <code>osd-overlay</code> command with the current fields of the overlay table. Returns the result of the <code>osd-overlay</code> command itself.</p>
<dt><code>remove()</code></p>
<dd>Remove the overlay from the screen. A <code>update()</code> call will add it again. </p>
<p> Example: </p>
<pre>ov = mp.create_osd_overlay(&quot;ass-events&quot;)
ov.data = &quot;{\an5}{\b1}hello world!&quot;
ov:update()</pre>
<p>The advantage of using this wrapper (as opposed to running <code>osd-overlay</code> directly) is that the <code>id</code> field is allocated automatically.</p>
<dt><code>mp.get_osd_size()</code></p>
<dd>Returns a tuple of <code>osd_width, osd_height, osd_par</code>. The first two give the size of the OSD in pixels (for video outputs like <code>&#8211;vo=xv</code>, this may be &quot;scaled&quot; pixels). The third is the display pixel aspect ratio. </p>
<p> May return invalid/nonsense values if OSD is not initialized yet.</dl>
<h3>mp.msg functions</h3>
<p>This module allows outputting messages to the terminal, and can be loaded with <code>require &#8216;mp.msg&#8217;</code>.</p>
<dl COMPACT>
<dt><code>msg.log(level, &#8230;)</code></p>
<dd>The level parameter is the message priority. It&#8217;s a string and one of <code>fatal</code>, <code>error</code>, <code>warn</code>, <code>info</code>, <code>v</code>, <code>debug</code>, <code>trace</code>. The user&#8217;s settings will determine which of these messages will be visible. Normally, all messages are visible, except <code>v</code>, <code>debug</code> and <code>trace</code>. </p>
<p> The parameters after that are all converted to strings. Spaces are inserted to separate multiple parameters. </p>
<p> You don&#8217;t need to add newlines.</p>
<dt><code>msg.fatal(&#8230;)</code>, <code>msg.error(&#8230;)</code>, <code>msg.warn(&#8230;)</code>, <code>msg.info(&#8230;)</code>, <code>msg.verbose(&#8230;)</code>, <code>msg.debug(&#8230;)</code>, <code>msg.trace(&#8230;)</code></p>
<dd>All of these are shortcuts and equivalent to the corresponding <code>msg.log(level, &#8230;)</code> call.</dl>
<h3>mp.options functions</h3>
<p>mpv comes with a built-in module to manage options from config-files and the command-line. All you have to do is to supply a table with default options to the read_options function. The function will overwrite the default values with values found in the config-file and the command-line (in that order).</p>
<dl COMPACT>
<dt><code>options.read_options(table [, identifier [, on_update]])</code></p>
<dd>A <code>table</code> with key-value pairs. The type of the default values is important for converting the values read from the config file or command-line back. Do not use <code>nil</code> as a default value! </p>
<p> The <code>identifier</code> is used to identify the config-file and the command-line options. These needs to unique to avoid collisions with other scripts. Defaults to <code>mp.get_script_name()</code> if the parameter is <code>nil</code> or missing. </p>
<p> The <code>on_update</code> parameter enables run-time updates of all matching option values via the <code>script-opts</code> option/property. If any of the matching options changes, the values in the <code>table</code> (which was originally passed to the function) are changed, and <code>on_update(list)</code> is called. <code>list</code> is a table where each updated option has a <code>list[option_name] = true</code> entry. There is no initial <code>on_update()</code> call. This never re-reads the config file. <code>script-opts</code> is always applied on the original config file, ignoring previous <code>script-opts</code> values (for example, if an option is removed from <code>script-opts</code> at runtime, the option will have the value in the config file). <code>table</code> entries are only written for option values whose values effectively change (this is important if the script changes <code>table</code> entries independently). </p>
<p> Example implementation: </p>
<pre>require 'mp.options'
local options = {
 optionA = &quot;defaultvalueA&quot;,
 optionB = -0.5,
 optionC = true,
}
read_options(options, &quot;myscript&quot;)
print(options.optionA)</pre>
<p>The config file will be stored in <code>script-opts/identifier.conf</code> in mpv&#8217;s user folder. Comment lines can be started with # and stray spaces are not removed. Boolean values will be represented with yes/no. </p>
<p> Example config: </p>
<pre># comment
optionA=Hello World
optionB=9999
optionC=no</pre>
<p>Command-line options are read from the <code>&#8211;script-opts</code> parameter. To avoid collisions, all keys have to be prefixed with <code>identifier-</code>. </p>
<p> Example command-line: </p>
<pre>--script-opts=myscript-optionA=TEST,myscript-optionB=0,myscript-optionC=yes</pre>
</dl>
<h3>mp.utils functions</h3>
<p>This built-in module provides generic helper functions for Lua, and have strictly speaking nothing to do with mpv or video/audio playback. They are provided for convenience. Most compensate for Lua&#8217;s scarce standard library. </p>
<p> Be warned that any of these functions might disappear any time. They are not strictly part of the guaranteed API.</p>
<dl COMPACT>
<dt><code>utils.getcwd()</code></p>
<dd>Returns the directory that mpv was launched from. On error, <code>nil, error</code> is returned.</p>
<dt><code>utils.readdir(path [, filter])</code></p>
<dd>Enumerate all entries at the given path on the filesystem, and return them as array. Each entry is a directory entry (without the path). The list is unsorted (in whatever order the operating system returns it). </p>
<p> If the <code>filter</code> argument is given, it must be one of the following strings:</p>
<dt><code>files</code></p>
<dd>List regular files only. This excludes directories, special files (like UNIX device files or FIFOs), and dead symlinks. It includes UNIX symlinks to regular files.</p>
<dt><code>dirs</code></p>
<dd>List directories only, or symlinks to directories. <code>.</code> and <code>..</code> are not included.</p>
<dt><code>normal</code></p>
<dd>Include the results of both <code>files</code> and <code>dirs</code>. (This is the default.)</p>
<dt><code>all</code></p>
<dd>List all entries, even device files, dead symlinks, FIFOs, and the <code>.</code> and <code>..</code> entries. </p>
<p> On error, <code>nil, error</code> is returned.</p>
<dt><code>utils.file_info(path)</code></p>
<dd>Stats the given path for information and returns a table with the following entries:</p>
<dt><code>mode</code></p>
<dd>protection bits (on Windows, always 755 (octal) for directories and 644 (octal) for files)</p>
<dt><code>size</code></p>
<dd>size in bytes</p>
<dt><code>atime</code></p>
<dd>time of last access</p>
<dt><code>mtime</code></p>
<dd>time of last modification</p>
<dt><code>ctime</code></p>
<dd>time of last metadata change</p>
<dt><code>is_file</code></p>
<dd>Whether <code>path</code> is a regular file (boolean)</p>
<dt><code>is_dir</code></p>
<dd>Whether <code>path</code> is a directory (boolean) </p>
<p> <code>mode</code> and <code>size</code> are integers. Timestamps (<code>atime</code>, <code>mtime</code> and <code>ctime</code>) are integer seconds since the Unix epoch (Unix time). The booleans <code>is_file</code> and <code>is_dir</code> are provided as a convenience; they can be and are derived from <code>mode</code>. </p>
<p> On error (e.g. path does not exist), <code>nil, error</code> is returned.</p>
<dt><code>utils.split_path(path)</code></p>
<dd>Split a path into directory component and filename component, and return them. The first return value is always the directory. The second return value is the trailing part of the path, the directory entry.</p>
<dt><code>utils.join_path(p1, p2)</code></p>
<dd>Return the concatenation of the 2 paths. Tries to be clever. For example, if <code>p2</code> is an absolute path, <code>p2</code> is returned without change.</p>
<dt><code>utils.subprocess(t)</code></p>
<dd>Runs an external process and waits until it exits. Returns process status and the captured output. This is a legacy wrapper around calling the <code>subprocess</code> command with <code>mp.command_native</code>. It does the following things:</p>
<dt>&bull;</p>
<dd>copy the table <code>t</code></p>
<dt>&bull;</p>
<dd>rename <code>cancellable</code> field to <code>playback_only</code></p>
<dt>&bull;</p>
<dd>rename <code>max_size</code> to <code>capture_size</code></p>
<dt>&bull;</p>
<dd>set <code>capture_stdout</code> field to <code>true</code> if unset</p>
<dt>&bull;</p>
<dd>set <code>name</code> field to <code>subprocess</code></p>
<dt>&bull;</p>
<dd>call <code>mp.command_native(copied_t)</code></p>
<dt>&bull;</p>
<dd>if the command failed, create a dummy result table</p>
<dt>&bull;</p>
<dd>copy <code>error_string</code> to <code>error</code> field if the string is non-empty</p>
<dt>&bull;</p>
<dd>return the result table </p>
<p> It is recommended to use <code>mp.command_native</code> or <code>mp.command_native_async</code> directly, instead of calling this legacy wrapper. It is for compatibility only. </p>
<p> See the <code>subprocess</code> documentation for semantics and further parameters.</p>
<dt><code>utils.subprocess_detached(t)</code></p>
<dd>Runs an external process and detaches it from mpv&#8217;s control. </p>
<p> The parameter <code>t</code> is a table. The function reads the following entries:</p>
<dt><code>args</code></p>
<dd>Array of strings of the same semantics as the <code>args</code> used in the <code>subprocess</code> function. </p>
<p> The function returns <code>nil</code>. </p>
<p> This is a legacy wrapper around calling the <code>run</code> command with <code>mp.commandv</code> and other functions.</p>
<dt><code>utils.getpid()</code></p>
<dd>Returns the process ID of the running mpv process. This can be used to identify the calling mpv when launching (detached) subprocesses.</p>
<dt><code>utils.get_env_list()</code></p>
<dd>Returns the C environment as a list of strings. (Do not confuse this with the Lua &quot;environment&quot;, which is an unrelated concept.)</p>
<dt><code>utils.parse_json(str [, trail])</code></p>
<dd>Parses the given string argument as JSON, and returns it as a Lua table. On error, returns <code>nil, error</code>. (Currently, <code>error</code> is just a string reading <code>error</code>, because there is no fine-grained error reporting of any kind.) </p>
<p> The returned value uses similar conventions as <code>mp.get_property_native()</code> to distinguish empty objects and arrays. </p>
<p> If the <code>trail</code> parameter is <code>true</code> (or any value equal to <code>true</code>), then trailing non-whitespace text is tolerated by the function, and the trailing text is returned as 3rd return value. (The 3rd return value is always there, but with <code>trail</code> set, no error is raised.)</p>
<dt><code>utils.format_json(v)</code></p>
<dd>Format the given Lua table (or value) as a JSON string and return it. On error, returns <code>nil, error</code>. (Errors usually only happen on value types incompatible with JSON.) </p>
<p> The argument value uses similar conventions as <code>mp.set_property_native()</code> to distinguish empty objects and arrays.</p>
<dt><code>utils.to_string(v)</code></p>
<dd>Turn the given value into a string. Formats tables and their contents. This doesn&#8217;t do anything special; it is only needed because Lua is terrible.</dl>
<h3>Events</h3>
<p>Events are notifications from player core to scripts. You can register an event handler with <code>mp.register_event</code>. </p>
<p> Note that all scripts (and other parts of the player) receive events equally, and there&#8217;s no such thing as blocking other scripts from receiving events. </p>
<p> Example: </p>
<pre>function my_fn(event)
 print(&quot;start of playback!&quot;)
end
mp.register_event(&quot;file-loaded&quot;, my_fn)</pre>
<p>For the existing event types, see <i>List of events</i>.</p>
<h3>Extras</h3>
<p>This documents experimental features, or features that are &quot;too special&quot; to guarantee a stable interface.</p>
<dl COMPACT>
<dt><code>mp.add_hook(type, priority, fn)</code></p>
<dd>Add a hook callback for <code>type</code> (a string identifying a certain kind of hook). These hooks allow the player to call script functions and wait for their result (normally, the Lua scripting interface is asynchronous from the point of view of the player core). <code>priority</code> is an arbitrary integer that allows ordering among hooks of the same kind. Using the value 50 is recommended as neutral default value. </p>
<p> <code>fn(hook)</code> is the function that will be called during execution of the hook. The parameter passed to it (<code>hook</code>) is a Lua object that can control further aspects about the currently invoked hook. It provides the following methods:</p>
<dt><code>defer()</code></p>
<dd>Returning from the hook function should not automatically continue the hook. Instead, the API user wants to call <code>hook:cont()</code> on its own at a later point in time (before or after the function has returned).</p>
<dt><code>cont()</code></p>
<dd>Continue the hook. Doesn&#8217;t need to be called unless <code>defer()</code> was called. </p>
<p> See <i>Hooks</i> for currently existing hooks and what they do &#8211; only the hook list is interesting; handling hook execution is done by the Lua script function automatically.</dl>
<h2>Javascript</h2>
<p>JavaScript support in mpv is near identical to its Lua support. Use this section as reference on differences and availability of APIs, but otherwise you should refer to the Lua documentation for API details and general scripting in mpv.</p>
<h3>Example</h3>
<p>JavaScript code which leaves fullscreen mode when the player is paused: </p>
<pre>function on_pause_change(name, value) {
 if (value == true)
 mp.set_property(&quot;fullscreen&quot;, &quot;no&quot;);
}
mp.observe_property(&quot;pause&quot;, &quot;bool&quot;, on_pause_change);</pre>
<h3>Similarities with Lua</h3>
<p>mpv tries to load a script file as JavaScript if it has a <code>.js</code> extension, but otherwise, the documented Lua options, script directories, loading, etc apply to JavaScript files too. </p>
<p> Script initialization and lifecycle is the same as with Lua, and most of the Lua functions at the modules <code>mp</code>, <code>mp.utils</code>, <code>mp.msg</code> and <code>mp.options</code> are available to JavaScript with identical APIs &#8211; including running commands, getting/setting properties, registering events/key-bindings/hooks, etc.</p>
<h3>Differences from Lua</h3>
<p>No need to load modules. <code>mp</code>, <code>mp.utils</code>, <code>mp.msg</code> and <code>mp.options</code> are preloaded, and you can use e.g. <code>var cwd = mp.utils.getcwd();</code> without prior setup. </p>
<p> Errors are slightly different. Where the Lua APIs return <code>nil</code> for error, the JavaScript ones return <code>undefined</code>. Where Lua returns <code>something, error</code> JavaScript returns only <code>something</code> &#8211; and makes <code>error</code> available via <code>mp.last_error()</code>. Note that only some of the functions have this additional <code>error</code> value &#8211; typically the same ones which have it in Lua. </p>
<p> Standard APIs are preferred. For instance <code>setTimeout</code> and <code>JSON.stringify</code> are available, but <code>mp.add_timeout</code> and <code>mp.utils.format_json</code> are not. </p>
<p> No standard library. This means that interaction with anything outside of mpv is limited to the available APIs, typically via <code>mp.utils</code>. However, some file functions were added, and CommonJS <code>require</code> is available too &#8211; where the loaded modules have the same privileges as normal scripts.</p>
<h3>Language features &#8211; ECMAScript 5</h3>
<p>The scripting backend which mpv currently uses is MuJS &#8211; a compatible minimal ES5 interpreter. As such, <code>String.substring</code> is implemented for instance, while the common but non-standard <code>String.substr</code> is not. Please consult the MuJS pages on language features and platform support &#8211; <i><a rel="nofollow" href="https://mujs.com">https://mujs.com</a></i> .</p>
<h3>Unsupported Lua APIs and their JS alternatives</h3>
<p><code>mp.add_timeout(seconds, fn)</code> JS: <code>id = setTimeout(fn, ms)</code> </p>
<p> <code>mp.add_periodic_timer(seconds, fn)</code> JS: <code>id = setInterval(fn, ms)</code> </p>
<p> <code>utils.parse_json(str [, trail])</code> JS: <code>JSON.parse(str)</code> </p>
<p> <code>utils.format_json(v)</code> JS: <code>JSON.stringify(v)</code> </p>
<p> <code>utils.to_string(v)</code> see <code>dump</code> below. </p>
<p> <code>mp.suspend()</code> JS: none (deprecated). </p>
<p> <code>mp.resume()</code> JS: none (deprecated). </p>
<p> <code>mp.resume_all()</code> JS: none (deprecated). </p>
<p> <code>mp.get_next_timeout()</code> see event loop below. </p>
<p> <code>mp.dispatch_events([allow_wait])</code> see event loop below.</p>
<h3>Scripting APIs &#8211; identical to Lua</h3>
<p>(LE) &#8211; Last-Error, indicates that <code>mp.last_error()</code> can be used after the call to test for success (empty string) or failure (non empty reason string). Where the Lua APIs use <code>nil</code> to indicate error, JS APIs use <code>undefined</code>. </p>
<p> <code>mp.command(string)</code> (LE) </p>
<p> <code>mp.commandv(arg1, arg2, &#8230;)</code> (LE) </p>
<p> <code>mp.command_native(table [,def])</code> (LE) </p>
<p> <code>id = mp.command_native_async(table [,fn])</code> (LE) Notes: <code>id</code> is true-thy on success, <code>fn</code> is called always a-sync, <code>error</code> is empty string on success. </p>
<p> <code>mp.abort_async_command(id)</code> </p>
<p> <code>mp.get_property(name [,def])</code> (LE) </p>
<p> <code>mp.get_property_osd(name [,def])</code> (LE) </p>
<p> <code>mp.get_property_bool(name [,def])</code> (LE) </p>
<p> <code>mp.get_property_number(name [,def])</code> (LE) </p>
<p> <code>mp.get_property_native(name [,def])</code> (LE) </p>
<p> <code>mp.set_property(name, value)</code> (LE) </p>
<p> <code>mp.set_property_bool(name, value)</code> (LE) </p>
<p> <code>mp.set_property_number(name, value)</code> (LE) </p>
<p> <code>mp.set_property_native(name, value)</code> (LE) </p>
<p> <code>mp.get_time()</code> </p>
<p> <code>mp.add_key_binding(key, name|fn [,fn [,flags]])</code> </p>
<p> <code>mp.add_forced_key_binding(&#8230;)</code> </p>
<p> <code>mp.remove_key_binding(name)</code> </p>
<p> <code>mp.register_event(name, fn)</code> </p>
<p> <code>mp.unregister_event(fn)</code> </p>
<p> <code>mp.observe_property(name, type, fn)</code> </p>
<p> <code>mp.unobserve_property(fn)</code> </p>
<p> <code>mp.get_opt(key)</code> </p>
<p> <code>mp.get_script_name()</code> </p>
<p> <code>mp.get_script_directory()</code> </p>
<p> <code>mp.osd_message(text [,duration])</code> </p>
<p> <code>mp.get_wakeup_pipe()</code> </p>
<p> <code>mp.register_idle(fn)</code> </p>
<p> <code>mp.unregister_idle(fn)</code> </p>
<p> <code>mp.enable_messages(level)</code> </p>
<p> <code>mp.register_script_message(name, fn)</code> </p>
<p> <code>mp.unregister_script_message(name)</code> </p>
<p> <code>mp.create_osd_overlay(format)</code> </p>
<p> <code>mp.get_osd_size()</code> (returned object has properties: width, height, aspect) </p>
<p> <code>mp.msg.log(level, &#8230;)</code> </p>
<p> <code>mp.msg.fatal(&#8230;)</code> </p>
<p> <code>mp.msg.error(&#8230;)</code> </p>
<p> <code>mp.msg.warn(&#8230;)</code> </p>
<p> <code>mp.msg.info(&#8230;)</code> </p>
<p> <code>mp.msg.verbose(&#8230;)</code> </p>
<p> <code>mp.msg.debug(&#8230;)</code> </p>
<p> <code>mp.msg.trace(&#8230;)</code> </p>
<p> <code>mp.utils.getcwd()</code> (LE) </p>
<p> <code>mp.utils.readdir(path [, filter])</code> (LE) </p>
<p> <code>mp.utils.file_info(path)</code> (LE) Note: like lua &#8211; this does NOT expand meta-paths like <code>~~/foo</code> (other JS file functions do expand meta paths). </p>
<p> <code>mp.utils.split_path(path)</code> </p>
<p> <code>mp.utils.join_path(p1, p2)</code> </p>
<p> <code>mp.utils.subprocess(t)</code> </p>
<p> <code>mp.utils.subprocess_detached(t)</code> </p>
<p> <code>mp.utils.get_env_list()</code> </p>
<p> <code>mp.utils.getpid()</code> (LE) </p>
<p> <code>mp.add_hook(type, priority, fn(hook))</code> </p>
<p> <code>mp.options.read_options(obj [, identifier [, on_update]])</code> (types: string/boolean/number)</p>
<h3>Additional utilities</h3>
<dl COMPACT>
<dt><code>mp.last_error()</code></p>
<dd>If used after an API call which updates last error, returns an empty string if the API call succeeded, or a non-empty error reason string otherwise.</p>
<dt><code>Error.stack</code> (string)</p>
<dd>When using <code>try { &#8230; } catch(e) { &#8230; }</code>, then <code>e.stack</code> is the stack trace of the error &#8211; if it was created using the <code>Error(&#8230;)</code> constructor.</p>
<dt><code>print</code> (global)</p>
<dd>A convenient alias to <code>mp.msg.info</code>.</p>
<dt><code>dump</code> (global)</p>
<dd>Like <code>print</code> but also expands objects and arrays recursively.</p>
<dt><code>mp.utils.getenv(name)</code></p>
<dd>Returns the value of the host environment variable <code>name</code>, or <code>undefined</code> if the variable is not defined.</p>
<dt><code>mp.utils.get_user_path(path)</code></p>
<dd>Expands (mpv) meta paths like <code>~/x</code>, <code>~~/y</code>, <code>~~desktop/z</code> etc. <code>read_file</code>, <code>write_file</code>, <code>append_file</code> and <code>require</code> already use this internally.</p>
<dt><code>mp.utils.read_file(fname [,max])</code></p>
<dd>Returns the content of file <code>fname</code> as string. If <code>max</code> is provided and not negative, limit the read to <code>max</code> bytes.</p>
<dt><code>mp.utils.write_file(fname, str)</code></p>
<dd>(Over)write file <code>fname</code> with text content <code>str</code>. <code>fname</code> must be prefixed with <code>file://</code> as simple protection against accidental arguments switch, e.g. <code>mp.utils.write_file(&quot;file://~/abc.txt&quot;, &quot;hello world&quot;)</code>.</p>
<dt><code>mp.utils.append_file(fname, str)</code></p>
<dd>Same as <code>mp.utils.write_file</code> if the file <code>fname</code> does not exist. If it does exist then append instead of overwrite. </p>
<p> Note: <code>read_file</code>, <code>write_file</code> and <code>append_file</code> throw on errors, allow text content only.</p>
<dt><code>mp.get_time_ms()</code></p>
<dd>Same as <code>mp.get_time()</code> but in ms instead of seconds.</p>
<dt><code>mp.get_script_file()</code></p>
<dd>Returns the file name of the current script.</p>
<dt><code>exit()</code> (global)</p>
<dd>Make the script exit at the end of the current event loop iteration. Note: please remove added key bindings before calling <code>exit()</code>.</p>
<dt><code>mp.utils.compile_js(fname, content_str)</code></p>
<dd>Compiles the JS code <code>content_str</code> as file name <code>fname</code> (without loading anything from the filesystem), and returns it as a function. Very similar to a <code>Function</code> constructor, but shows at stack traces as <code>fname</code>.</p>
<dt><code>mp.module_paths</code></p>
<dd>Global modules search paths array for the <code>require</code> function (see below).</dl>
<h3>Timers (global)</h3>
<p>The standard HTML/node.js timers are available: </p>
<p> <code>id = setTimeout(fn [,duration [,arg1 [,arg2&#8230;]]])</code> </p>
<p> <code>id = setTimeout(code_string [,duration])</code> </p>
<p> <code>clearTimeout(id)</code> </p>
<p> <code>id = setInterval(fn [,duration [,arg1 [,arg2&#8230;]]])</code> </p>
<p> <code>id = setInterval(code_string [,duration])</code> </p>
<p> <code>clearInterval(id)</code> </p>
<p> <code>setTimeout</code> and <code>setInterval</code> return id, and later call <code>fn</code> (or execute <code>code_string</code>) after <code>duration</code> ms. Interval also repeat every <code>duration</code>. </p>
<p> <code>duration</code> has a minimum and default value of 0, <code>code_string</code> is a plain string which is evaluated as JS code, and <code>[,arg1 [,arg2..]]</code> are used as arguments (if provided) when calling back <code>fn</code>. </p>
<p> The <code>clear&#8230;(id)</code> functions cancel timer <code>id</code>, and are irreversible. </p>
<p> Note: timers always call back asynchronously, e.g. <code>setTimeout(fn)</code> will never call <code>fn</code> before returning. <code>fn</code> will be called either at the end of this event loop iteration or at a later event loop iteration. This is true also for intervals &#8211; which also never call back twice at the same event loop iteration. </p>
<p> Additionally, timers are processed after the event queue is empty, so it&#8217;s valid to use <code>setTimeout(fn)</code> as a one-time idle observer.</p>
<h3>CommonJS modules and <code>require(id)</code></h3>
<p>CommonJS Modules are a standard system where scripts can export common functions for use by other scripts. Specifically, a module is a script which adds properties (functions, etc) to its pre-existing <code>exports</code> object, which another script can access with <code>require(module-id)</code>. This runs the module and returns its <code>exports</code> object. Further calls to <code>require</code> for the same module will return its cached <code>exports</code> object without running the module again. </p>
<p> Modules and <code>require</code> are supported, standard compliant, and generally similar to node.js. However, most node.js modules won&#8217;t run due to missing modules such as <code>fs</code>, <code>process</code>, etc, but some node.js modules with minimal dependencies do work. In general, this is for mpv modules and not a node.js replacement. </p>
<p> A <code>.js</code> file extension is always added to <code>id</code>, e.g. <code>require(&quot;./foo&quot;)</code> will load the file <code>./foo.js</code> and return its <code>exports</code> object. </p>
<p> An id which starts with <code>./</code> or <code>../</code> is relative to the script or module which <code>require</code> it. Otherwise it&#8217;s considered a top-level id (CommonJS term). </p>
<p> Top-level id is evaluated as absolute filesystem path if possible, e.g. <code>/x/y</code> or <code>~/x</code>. Otherwise it&#8217;s considered a global module id and searched according to <code>mp.module_paths</code> in normal array order, e.g. <code>require(&quot;x&quot;)</code> tries to load <code>x.js</code> at one of the array paths, and id <code>foo/x</code> tries to load <code>x.js</code> inside dir <code>foo</code> at one of the paths. </p>
<p> The <code>mp.module_paths</code> array is empty by default except for scripts which are loaded as a directory where it contains one item &#8211; <code>&lt;directory&gt;/modules/</code> . The array may be updated from a script (or using custom init &#8211; see below) which will affect future calls to <code>require</code> for global module id&#8217;s which are not already loaded/cached. </p>
<p> No <code>global</code> variable, but a module&#8217;s <code>this</code> at its top lexical scope is the global object &#8211; also in strict mode. If you have a module which needs <code>global</code> as the global object, you could do <code>this.global = this;</code> before <code>require</code>. </p>
<p> Functions and variables declared at a module don&#8217;t pollute the global object.</p>
<h3>Custom initialization</h3>
<p>After mpv initializes the JavaScript environment for a script but before it loads the script &#8211; it tries to run the file <code>init.js</code> at the root of the mpv configuration directory. Code at this file can update the environment further for all scripts. E.g. if it contains <code>mp.module_paths.push(&quot;/foo&quot;)</code> then <code>require</code> at all scripts will search global module id&#8217;s also at <code>/foo</code> (do NOT do <code>mp.module_paths = [&quot;/foo&quot;];</code> because this will remove existing paths &#8211; like <code>&lt;script-dir&gt;/modules</code> for scripts which load from a directory). </p>
<p> The custom-init file is ignored if mpv is invoked with <code>&#8211;no-config</code>. </p>
<p> Before mpv 0.34, the file name was <code>.init.js</code> (with dot) at the same dir.</p>
<h3>The event loop</h3>
<p>The event loop poll/dispatch mpv events as long as the queue is not empty, then processes the timers, then waits for the next event, and repeats this forever. </p>
<p> You could put this code at your script to replace the built-in event loop, and also print every event which mpv sends to your script: </p>
<pre>function mp_event_loop() {
 var wait = 0;
 do {
 var e = mp.wait_event(wait);
 dump(e); // there could be a lot of prints...
 if (e.event != &quot;none&quot;) {
 mp.dispatch_event(e);
 wait = 0;
 } else {
 wait = mp.process_timers() / 1000;
 if (wait != 0) {
 mp.notify_idle_observers();
 wait = mp.peek_timers_wait() / 1000;
 }
 }
 } while (mp.keep_running);
}</pre>
<p><code>mp_event_loop</code> is a name which mpv tries to call after the script loads. The internal implementation is similar to this (without <code>dump</code> though..). </p>
<p> <code>e = mp.wait_event(wait)</code> returns when the next mpv event arrives, or after <code>wait</code> seconds if positive and no mpv events arrived. <code>wait</code> value of 0 returns immediately (with <code>e.event == &quot;none&quot;</code> if the queue is empty). </p>
<p> <code>mp.dispatch_event(e)</code> calls back the handlers registered for <code>e.event</code>, if there are such (event handlers, property observers, script messages, etc). </p>
<p> <code>mp.process_timers()</code> calls back the already-added, non-canceled due timers, and returns the duration in ms till the next due timer (possibly 0), or -1 if there are no pending timers. Must not be called recursively. </p>
<p> <code>mp.notify_idle_observers()</code> calls back the idle observers, which we do when we&#8217;re about to sleep (wait != 0), but the observers may add timers or take non-negligible duration to complete, so we re-calculate <code>wait</code> afterwards. </p>
<p> <code>mp.peek_timers_wait()</code> returns the same values as <code>mp.process_timers()</code> but without doing anything. Invalid result if called from a timer callback. </p>
<p> Note: <code>exit()</code> is also registered for the <code>shutdown</code> event, and its implementation is a simple <code>mp.keep_running = false</code>.</p>
<h2>Json Ipc</h2>
<p>mpv can be controlled by external programs using the JSON-based IPC protocol. It can be enabled by specifying the path to a unix socket or a named pipe using the option <code>&#8211;input-ipc-server</code>. Clients can connect to this socket and send commands to the player or receive events from it. </p>
<p> <code>WARNING:</code> This is not intended to be a secure network protocol. It is explicitly insecure: there is no authentication, no encryption, and the commands themselves are insecure too. For example, the <code>run</code> command is exposed, which can run arbitrary system commands. The use-case is controlling the player locally. This is not different from the MPlayer slave protocol.</p>
<h3>Socat example</h3>
<p>You can use the <code>socat</code> tool to send commands (and receive replies) from the shell. Assuming mpv was started with: </p>
<pre>mpv file.mkv --input-ipc-server=/tmp/mpvsocket</pre>
<p>Then you can control it using socat: </p>
<pre>&gt; echo '{ &quot;command&quot;: [&quot;get_property&quot;, &quot;playback-time&quot;] }' | socat - /tmp/mpvsocket
{&quot;data&quot;:190.482000,&quot;error&quot;:&quot;success&quot;}</pre>
<p>In this case, socat copies data between stdin/stdout and the mpv socket connection. </p>
<p> See the <code>&#8211;idle</code> option how to make mpv start without exiting immediately or playing a file. </p>
<p> It&#8217;s also possible to send input.conf style text-only commands: </p>
<pre>&gt; echo 'show-text ${playback-time}' | socat - /tmp/mpvsocket</pre>
<p>But you won&#8217;t get a reply over the socket. (This particular command shows the playback time on the player&#8217;s OSD.)</p>
<h3>Command Prompt example</h3>
<p>Unfortunately, it&#8217;s not as easy to test the IPC protocol on Windows, since Windows ports of socat (in Cygwin and MSYS2) don&#8217;t understand named pipes. In the absence of a simple tool to send and receive from bidirectional pipes, the <code>echo</code> command can be used to send commands, but not receive replies from the command prompt. </p>
<p> Assuming mpv was started with: </p>
<pre>mpv file.mkv --input-ipc-server=\.\pipe\mpvsocket</pre>
<p>You can send commands from a command prompt: </p>
<pre>echo show-text ${playback-time} &gt;\.\pipe\mpvsocket</pre>
<p>To be able to simultaneously read and write from the IPC pipe, like on Linux, it&#8217;s necessary to write an external program that uses overlapped file I/O (or some wrapper like .NET&#8217;s NamedPipeClientStream.) </p>
<p> You can open the pipe in PuTTY as &quot;serial&quot; device. This is not very comfortable, but gives a way to test interactively without having to write code.</p>
<h3>Protocol</h3>
<p>The protocol uses UTF-8-only JSON as defined by RFC-8259. Unlike standard JSON, &quot;u&quot; escape sequences are not allowed to construct surrogate pairs. To avoid getting conflicts, encode all text characters including and above codepoint U+0020 as UTF-8. mpv might output broken UTF-8 in corner cases (see &quot;UTF-8&quot; section below). </p>
<p> Clients can execute commands on the player by sending JSON messages of the following form: </p>
<pre>{ &quot;command&quot;: [&quot;command_name&quot;, &quot;param1&quot;, &quot;param2&quot;, ...] }</pre>
<p>where <code>command_name</code> is the name of the command to be executed, followed by a list of parameters. Parameters must be formatted as native JSON values (integers, strings, booleans, &#8230;). Every message <code>must</code> be terminated with <code>
</code>. Additionally, <code>
</code> must not appear anywhere inside the message. In practice this means that messages should be minified before being sent to mpv. </p>
<p> mpv will then send back a reply indicating whether the command was run correctly, and an additional field holding the command-specific return data (it can also be null). </p>
<pre>{ &quot;error&quot;: &quot;success&quot;, &quot;data&quot;: null }</pre>
<p>mpv will also send events to clients with JSON messages of the following form: </p>
<pre>{ &quot;event&quot;: &quot;event_name&quot; }</pre>
<p>where <code>event_name</code> is the name of the event. Additional event-specific fields can also be present. See <i>List of events</i> for a list of all supported events. </p>
<p> Because events can occur at any time, it may be difficult at times to determine which response goes with which command. Commands may optionally include a <code>request_id</code> which, if provided in the command request, will be copied verbatim into the response. mpv does not interpret the <code>request_id</code> in any way; it is solely for the use of the requester. The only requirement is that the <code>request_id</code> field must be an integer (a number without fractional parts in the range <code>-2^63..2^63-1</code>). Using other types is deprecated and will currently show a warning. In the future, this will raise an error. </p>
<p> For example, this request: </p>
<pre>{ &quot;command&quot;: [&quot;get_property&quot;, &quot;time-pos&quot;], &quot;request_id&quot;: 100 }</pre>
<p>Would generate this response: </p>
<pre>{ &quot;error&quot;: &quot;success&quot;, &quot;data&quot;: 1.468135, &quot;request_id&quot;: 100 }</pre>
<p>If you don&#8217;t specify a <code>request_id</code>, command replies will set it to 0. </p>
<p> All commands, replies, and events are separated from each other with a line break character (<code>
</code>). </p>
<p> If the first character (after skipping whitespace) is not <code>{</code>, the command will be interpreted as non-JSON text command, as they are used in input.conf (or <code>mpv_command_string()</code> in the client API). Additionally, lines starting with <code>#</code> and empty lines are ignored. </p>
<p> Currently, embedded 0 bytes terminate the current line, but you should not rely on this.</p>
<h3>Data flow</h3>
<p>Currently, the mpv-side IPC implementation does not service the socket while a command is executed and the reply is written. It is for example not possible that other events, that happened during the execution of the command, are written to the socket before the reply is written. </p>
<p> This might change in the future. The only guarantee is that replies to IPC messages are sent in sequence. </p>
<p> Also, since socket I/O is inherently asynchronous, it is possible that you read unrelated event messages from the socket, before you read the reply to the previous command you sent. In this case, these events were queued by the mpv side before it read and started processing your command message. </p>
<p> If the mpv-side IPC implementation switches away from blocking writes and blocking command execution, it may attempt to send events at any time. </p>
<p> You can also use asynchronous commands, which can return in any order, and which do not block IPC protocol interaction at all while the command is executed in the background.</p>
<h3>Asynchronous commands</h3>
<p>Command can be run asynchronously. This behaves exactly as with normal command execution, except that execution is not blocking. Other commands can be sent while it&#8217;s executing, and command completion can be arbitrarily reordered. </p>
<p> The <code>async</code> field controls this. If present, it must be a boolean. If missing, <code>false</code> is assumed. </p>
<p> For example, this initiates an asynchronous command: </p>
<pre>{ &quot;command&quot;: [&quot;screenshot&quot;], &quot;request_id&quot;: 123, &quot;async&quot;: true }</pre>
<p>And this is the completion: </p>
<pre>{&quot;request_id&quot;:123,&quot;error&quot;:&quot;success&quot;,&quot;data&quot;:null}</pre>
<p>By design, you will not get a confirmation that the command was started. If a command is long running, sending the message will lead to any reply until much later when the command finishes. </p>
<p> Some commands execute synchronously, but these will behave like asynchronous commands that finished execution immediately. </p>
<p> Cancellation of asynchronous commands is available in the libmpv API, but has not yet been implemented in the IPC protocol.</p>
<h3>Commands with named arguments</h3>
<p>If the <code>command</code> field is a JSON object, named arguments are expected. This is described in the C API <code>mpv_command_node()</code> documentation (the <code>MPV_FORMAT_NODE_MAP</code> case). In some cases, this may make commands more readable, while some obscure commands basically require using named arguments. </p>
<p> Currently, only &quot;proper&quot; commands (as listed by <i>List of Input Commands</i>) support named arguments.</p>
<h3>Commands</h3>
<p>In addition to the commands described in <i>List of Input Commands</i>, a few extra commands can also be used as part of the protocol:</p>
<dl COMPACT>
<dt><code>client_name</code></p>
<dd>Return the name of the client as string. This is the string <code>ipc-N</code> with N being an integer number.</p>
<dt><code>get_time_us</code></p>
<dd>Return the current mpv internal time in microseconds as a number. This is basically the system time, with an arbitrary offset.</p>
<dt><code>get_property</code></p>
<dd>Return the value of the given property. The value will be sent in the data field of the replay message. </p>
<p> Example: </p>
<pre>{ &quot;command&quot;: [&quot;get_property&quot;, &quot;volume&quot;] }
{ &quot;data&quot;: 50.0, &quot;error&quot;: &quot;success&quot; }</pre>
<dt><code>get_property_string</code></p>
<dd>Like <code>get_property</code>, but the resulting data will always be a string. </p>
<p> Example: </p>
<pre>{ &quot;command&quot;: [&quot;get_property_string&quot;, &quot;volume&quot;] }
{ &quot;data&quot;: &quot;50.000000&quot;, &quot;error&quot;: &quot;success&quot; }</pre>
<dt><code>set_property</code></p>
<dd>Set the given property to the given value. See <i>Properties</i> for more information about properties. </p>
<p> Example: </p>
<pre>{ &quot;command&quot;: [&quot;set_property&quot;, &quot;pause&quot;, true] }
{ &quot;error&quot;: &quot;success&quot; }</pre>
<dt><code>set_property_string</code></p>
<dd>Alias for <code>set_property</code>. Both commands accept native values and strings.</p>
<dt><code>observe_property</code></p>
<dd>Watch a property for changes. If the given property is changed, then an event of type <code>property-change</code> will be generated </p>
<p> Example: </p>
<pre>{ &quot;command&quot;: [&quot;observe_property&quot;, 1, &quot;volume&quot;] }
{ &quot;error&quot;: &quot;success&quot; }
{ &quot;event&quot;: &quot;property-change&quot;, &quot;id&quot;: 1, &quot;data&quot;: 52.0, &quot;name&quot;: &quot;volume&quot; }</pre>
<p><code>WARNING:</code> If the connection is closed, the IPC client is destroyed internally, and the observed properties are unregistered. This happens for example when sending commands to a socket with separate <code>socat</code> invocations. This can make it seem like property observation does not work. You must keep the IPC connection open to make it work.</p>
<dt><code>observe_property_string</code></p>
<dd>Like <code>observe_property</code>, but the resulting data will always be a string. </p>
<p> Example: </p>
<pre>{ &quot;command&quot;: [&quot;observe_property_string&quot;, 1, &quot;volume&quot;] }
{ &quot;error&quot;: &quot;success&quot; }
{ &quot;event&quot;: &quot;property-change&quot;, &quot;id&quot;: 1, &quot;data&quot;: &quot;52.000000&quot;, &quot;name&quot;: &quot;volume&quot; }</pre>
<dt><code>unobserve_property</code></p>
<dd>Undo <code>observe_property</code> or <code>observe_property_string</code>. This requires the numeric id passed to the observed command as argument. </p>
<p> Example: </p>
<pre>{ &quot;command&quot;: [&quot;unobserve_property&quot;, 1] }
{ &quot;error&quot;: &quot;success&quot; }</pre>
<dt><code>request_log_messages</code></p>
<dd>Enable output of mpv log messages. They will be received as events. The parameter to this command is the log-level (see <code>mpv_request_log_messages</code> C API function). </p>
<p> Log message output is meant for humans only (mostly for debugging). Attempting to retrieve information by parsing these messages will just lead to breakages with future mpv releases. Instead, make a feature request, and ask for a proper event that returns the information you need.</p>
<dt><code>enable_event</code>, <code>disable_event</code></p>
<dd>Enables or disables the named event. Mirrors the <code>mpv_request_event</code> C API function. If the string <code>all</code> is used instead of an event name, all events are enabled or disabled. </p>
<p> By default, most events are enabled, and there is not much use for this command.</p>
<dt><code>get_version</code></p>
<dd>Returns the client API version the C API of the remote mpv instance provides. </p>
<p> See also: <code>DOCS/client-api-changes.rst</code>.</dl>
<h3>Utf-8</h3>
<p>Normally, all strings are in UTF-8. Sometimes it can happen that strings are in some broken encoding (often happens with file tags and such, and filenames on many Unixes are not required to be in UTF-8 either). This means that mpv sometimes sends invalid JSON. If that is a problem for the client application&#8217;s parser, it should filter the raw data for invalid UTF-8 sequences and perform the desired replacement, before feeding the data to its JSON parser. </p>
<p> mpv will not attempt to construct invalid UTF-8 with broken &quot;u&quot; escape sequences. This includes surrogate pairs.</p>
<h3>JSON extensions</h3>
<p>The following non-standard extensions are supported:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>a list or object item can have a trailing &quot;,&quot;</p>
<dt>&bull;</p>
<dd>object syntax accepts &quot;=&quot; in addition of &quot;:&quot;</p>
<dt>&bull;</p>
<dd>object keys can be unquoted, if they start with a character in &quot;A-Za-z_&quot; and contain only characters in &quot;A-Za-z0-9_&quot;</p>
<dt>&bull;</p>
<dd>byte escapes with &quot;xAB&quot; are allowed (with AB being a 2 digit hex number) </p>
<p> Example: </p>
<pre>{ objkey = &quot;value
&quot; }</pre>
<p>Is equivalent to: </p>
<pre>{ &quot;objkey&quot;: &quot;value
&quot; }</pre>
</dl>
<h3>Alternative ways of starting clients</h3>
<p>You can create an anonymous IPC connection without having to set <code>&#8211;input-ipc-server</code>. This is achieved through a mpv pseudo scripting backend that starts processes. </p>
<p> You can put <code>.run</code> file extension in the mpv scripts directory in its config directory (see the <i>FILES</i> section for details), or load them through other means (see <i>Script location</i>). These scripts are simply executed with the OS native mechanism (as if you ran them in the shell). They must have a proper shebang and have the executable bit set. </p>
<p> When executed, a socket (the IPC connection) is passed to them through file descriptor inheritance. The file descriptor is indicated as the special command line argument <code>&#8211;mpv-ipc-fd=N</code>, where <code>N</code> is the numeric file descriptor. </p>
<p> The rest is the same as with a normal <code>&#8211;input-ipc-server</code> IPC connection. mpv does not attempt to observe or other interact with the started script process. </p>
<p> This does not work in Windows yet.</p>
<h2>Changelog</h2>
<p>There is no real changelog, but you can look at the following things:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>The release changelog, which should contain most user-visible changes, including new features and bug fixes: </p>
<p> <i><a rel="nofollow" href="https://github.com/mpv-player/mpv/releases">https://github.com/mpv-player/mpv/releases</a></i></p>
<dt>&bull;</p>
<dd>The git log, which is the &quot;real&quot; changelog</p>
<dt>&bull;</p>
<dd>The file <i><a rel="nofollow" href="https://github.com/mpv-player/mpv/blob/master/DOCS/interface-changes.rst">https://github.com/mpv-player/mpv/blob/master/DOCS/interface-changes.rst</a></i> documents changes to the command and user interface, such as options and properties. (It usually documents breaking changes only, additions and enhancements are often not listed.)</p>
<dt>&bull;</p>
<dd>C API changes are listed in <i><a rel="nofollow" href="https://github.com/mpv-player/mpv/blob/master/DOCS/client-api-changes.rst">https://github.com/mpv-player/mpv/blob/master/DOCS/client-api-changes.rst</a></i></p>
<dt>&bull;</p>
<dd>The file <code>mplayer-changes.rst</code> in the <code>DOCS</code> sub directory on the git repository, which used to be in place of this section. It documents some changes that happened since mplayer2 forked off MPlayer. (Not updated anymore.)</dl>
<h2>Embedding Into Other Programs (Libmpv)</h2>
<p>mpv can be embedded into other programs as video/audio playback backend. The recommended way to do so is using libmpv. See <code>libmpv/client.h</code> in the mpv source code repository. This provides a C API. Bindings for other languages might be available (see wiki). </p>
<p> Since libmpv merely allows access to underlying mechanisms that can control mpv, further documentation is spread over a few places:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd><i><a rel="nofollow" href="https://github.com/mpv-player/mpv/blob/master/libmpv/client.h">https://github.com/mpv-player/mpv/blob/master/libmpv/client.h</a></i></p>
<dt>&bull;</p>
<dd><i><a rel="nofollow" href="https://mpv.io/manual/master/#options">https://mpv.io/manual/master/#options</a></i></p>
<dt>&bull;</p>
<dd><i><a rel="nofollow" href="https://mpv.io/manual/master/#list-of-input-commands">https://mpv.io/manual/master/#list-of-input-commands</a></i></p>
<dt>&bull;</p>
<dd><i><a rel="nofollow" href="https://mpv.io/manual/master/#properties">https://mpv.io/manual/master/#properties</a></i></p>
<dt>&bull;</p>
<dd><i><a rel="nofollow" href="https://github.com/mpv-player/mpv-examples/tree/master/libmpv">https://github.com/mpv-player/mpv-examples/tree/master/libmpv</a></i></dl>
<h2>C Plugins</h2>
<p>You can write C plugins for mpv. These use the libmpv API, although they do not use the libmpv library itself. </p>
<p> They are available on Linux/BSD platforms only and enabled by default if the compiler supports linking with the <code>-rdynamic</code> flag.</p>
<h3>C plugins location</h3>
<p>C plugins are put into the mpv scripts directory in its config directory (see the <i>FILES</i> section for details). They must have a <code>.so</code> file extension. They can also be explicitly loaded with the <code>&#8211;script</code> option.</p>
<h3>Api</h3>
<p>A C plugin must export the following function: </p>
<pre>int mpv_open_cplugin(mpv_handle *handle)</pre>
<p>The plugin function will be called on loading time. This function does not return as long as your plugin is loaded (it runs in its own thread). The <code>handle</code> will be deallocated as soon as the plugin function returns. </p>
<p> The return value is interpreted as error status. A value of <code>0</code> is interpreted as success, while <code>-1</code> signals an error. In the latter case, the player prints an uninformative error message that loading failed. </p>
<p> Return values other than <code>0</code> and <code>-1</code> are reserved, and trigger undefined behavior. </p>
<p> Within the plugin function, you can call libmpv API functions. The <code>handle</code> is created by <code>mpv_create_client()</code> (or actually an internal equivalent), and belongs to you. You can call <code>mpv_wait_event()</code> to wait for things happening, and so on. </p>
<p> Note that the player might block until your plugin calls <code>mpv_wait_event()</code> for the first time. This gives you a chance to install initial hooks etc. before playback begins. </p>
<p> The details are quite similar to Lua scripts.</p>
<h3>Linkage to libmpv</h3>
<p>The current implementation requires that your plugins are <code>not</code> linked against libmpv. What your plugins uses are not symbols from a libmpv binary, but symbols from the mpv host binary.</p>
<h3>Examples</h3>
<p>See:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd><i><a rel="nofollow" href="https://github.com/mpv-player/mpv-examples/tree/master/cplugins">https://github.com/mpv-player/mpv-examples/tree/master/cplugins</a></i></dl>
<h2>Environment Variables</h2>
<p>There are a number of environment variables that can be used to control the behavior of mpv.</p>
<dl COMPACT>
<dt><code>HOME</code>, <code>XDG_CONFIG_HOME</code></p>
<dd>Used to determine mpv config directory. If <code>XDG_CONFIG_HOME</code> is not set, <code>$HOME/.config/mpv</code> is used. </p>
<p> <code>$HOME/.mpv</code> is always added to the list of config search paths with a lower priority.</p>
<dt><code>MPV_HOME</code></p>
<dd>Directory where mpv looks for user settings. Overrides <code>HOME</code>, and mpv will try to load the config file as <code>$MPV_HOME/mpv.conf</code>.</p>
<dt><code>MPV_VERBOSE</code> (see also <code>-v</code> and <code>&#8211;msg-level</code>)</p>
<dd>Set the initial verbosity level across all message modules (default: 0). This is an integer, and the resulting verbosity corresponds to the number of <code>&#8211;v</code> options passed to the command line.</p>
<dt><code>MPV_LEAK_REPORT</code></p>
<dd>If set to <code>1</code>, enable internal talloc leak reporting. If set to another value, disable leak reporting. If unset, use the default, which normally is <code>0</code>. If mpv was built with <code>&#8211;enable-ta-leak-report</code>, the default is <code>1</code>. If leak reporting was disabled at compile time (<code>NDEBUG</code> in custom <code>CFLAGS</code>), this environment variable is ignored.</p>
<dt><code>LADSPA_PATH</code></p>
<dd>Specifies the search path for LADSPA plugins. If it is unset, fully qualified path names must be used.</p>
<dt><code>DISPLAY</code></p>
<dd>Standard X11 display name to use.</p>
<dt><code>FFmpeg/Libav:</code></p>
<dd>This library accesses various environment variables. However, they are not centrally documented, and documenting them is not our job. Therefore, this list is incomplete. </p>
<p> Notable environment variables:</p>
<dt><code>http_proxy</code></p>
<dd>URL to proxy for <code>http://</code> and <code>https://</code> URLs.</p>
<dt><code>no_proxy</code></p>
<dd>List of domain patterns for which no proxy should be used. List entries are separated by <code>,</code>. Patterns can include <code>*</code>.</p>
<dt><code>libdvdcss:</code></p>
<dd>
<dt><code>DVDCSS_CACHE</code></p>
<dd>Specify a directory in which to store title key values. This will speed up descrambling of DVDs which are in the cache. The <code>DVDCSS_CACHE</code> directory is created if it does not exist, and a subdirectory is created named after the DVD&#8217;s title or manufacturing date. If <code>DVDCSS_CACHE</code> is not set or is empty, libdvdcss will use the default value which is <code>${HOME}/.dvdcss/</code> under Unix and the roaming application data directory (<code>%APPDATA%</code>) under Windows. The special value &quot;off&quot; disables caching.</p>
<dt><code>DVDCSS_METHOD</code></p>
<dd>Sets the authentication and decryption method that libdvdcss will use to read scrambled discs. Can be one of <code>title</code>, <code>key</code> or <code>disc</code>.</p>
<dt><code>key</code></p>
<dd>is the default method. libdvdcss will use a set of calculated player keys to try to get the disc key. This can fail if the drive does not recognize any of the player keys.</p>
<dt><code>disc</code></p>
<dd>is a fallback method when key has failed. Instead of using player keys, libdvdcss will crack the disc key using a brute force algorithm. This process is CPU intensive and requires 64 MB of memory to store temporary data.</p>
<dt><code>title</code></p>
<dd>is the fallback when all other methods have failed. It does not rely on a key exchange with the DVD drive, but rather uses a crypto attack to guess the title key. On rare cases this may fail because there is not enough encrypted data on the disc to perform a statistical attack, but on the other hand it is the only way to decrypt a DVD stored on a hard disc, or a DVD with the wrong region on an RPC2 drive.</p>
<dt><code>DVDCSS_RAW_DEVICE</code></p>
<dd>Specify the raw device to use. Exact usage will depend on your operating system, the Linux utility to set up raw devices is <a href="/docs/linux/man/8-raw/">raw</a>(8) for instance. Please note that on most operating systems, using a raw device requires highly aligned buffers: Linux requires a 2048 bytes alignment (which is the size of a DVD sector).</p>
<dt><code>DVDCSS_VERBOSE</code></p>
<dd>Sets the libdvdcss verbosity level.</p>
<dt><code>0</code></p>
<dd>Outputs no messages at all.</p>
<dt><code>1</code></p>
<dd>Outputs error messages to stderr.</p>
<dt><code>2</code></p>
<dd>Outputs error messages and debug messages to stderr.</p>
<dt><code>DVDREAD_NOKEYS</code></p>
<dd>Skip retrieving all keys on startup. Currently disabled.</p>
<dt><code>HOME</code></p>
<dd>FIXME: Document this.</dl>
<h2>Exit Codes</h2>
<p>Normally <code>mpv</code> returns 0 as exit code after finishing playback successfully. If errors happen, the following exit codes can be returned:</p>
<dl COMPACT>
<dt><code>1</code></p>
<dd>Error initializing mpv. This is also returned if unknown options are passed to mpv.</p>
<dt><code>2</code></p>
<dd>The file passed to mpv couldn&#8217;t be played. This is somewhat fuzzy: currently, playback of a file is considered to be successful if initialization was mostly successful, even if playback fails immediately after initialization.</p>
<dt><code>3</code></p>
<dd>There were some files that could be played, and some files which couldn&#8217;t (using the definition of success from above).</p>
<dt><code>4</code></p>
<dd>Quit due to a signal, Ctrl+c in a VO window (by default), or from the default quit key bindings in encoding mode. </p>
<p> Note that quitting the player manually will always lead to exit code 0, overriding the exit code that would be returned normally. Also, the <code>quit</code> input command can take an exit code: in this case, that exit code is returned.</dl>
<h2>Files</h2>
<p>For Windows-specifics, see <i>FILES ON WINDOWS</i> section.</p>
<dl COMPACT>
<dt><code>/usr/local/etc/mpv/mpv.conf</code></p>
<dd>mpv system-wide settings (depends on <code>&#8211;prefix</code> passed to configure &#8211; mpv in default configuration will use <code>/usr/local/etc/mpv/</code> as config directory, while most Linux distributions will set it to <code>/etc/mpv/</code>).</p>
<dt><code>~/.config/mpv</code></p>
<dd>The standard configuration directory. This can be overridden by environment variables, in ascending order:</p>
<dt><code>1</code></p>
<dd>If <code>$XDG_CONFIG_HOME</code> is set, then the derived configuration directory will be <code>$XDG_CONFIG_HOME/mpv</code>.</p>
<dt><code>2</code></p>
<dd>If <code>$MPV_HOME</code> is set, then the derived configuration directory will be <code>$MPV_HOME</code>. </p>
<p> If this directory, nor the original configuration directory (see below) do not exist, mpv tries to create this directory automatically.</p>
<dt><code>~/.mpv/</code></p>
<dd>The original (pre 0.5.0) configuration directory. It will continue to be read if present. </p>
<p> If both this directory and the standard configuration directory are present, configuration will be read from both with the standard configuration directory content taking precedence. However, you should fully migrate to the standard directory and a warning will be shown in this situation.</p>
<dt><code>~/.config/mpv/mpv.conf</code></p>
<dd>mpv user settings (see <i>CONFIGURATION FILES</i> section)</p>
<dt><code>~/.config/mpv/input.conf</code></p>
<dd>key bindings (see <i>INPUT.CONF</i> section)</p>
<dt><code>~/.config/mpv/fonts.conf</code></p>
<dd>Fontconfig fonts.conf that is customized for mpv. You should include system fonts.conf in this file or mpv would not know about fonts that you already have in the system. </p>
<p> Only available when libass is built with fontconfig.</p>
<dt><code>~/.config/mpv/subfont.ttf</code></p>
<dd>fallback subtitle font</p>
<dt><code>~/.config/mpv/fonts/</code></p>
<dd>Font files in this directory are used by mpv/libass for subtitles. Useful if you do not want to install fonts to your system. Note that files in this directory are loaded into memory before being used by mpv. If you have a lot of fonts, consider using fonts.conf (see above) to include additional fonts, which is more memory-efficient.</p>
<dt><code>~/.config/mpv/scripts/</code></p>
<dd>All files in this directory are loaded as if they were passed to the <code>&#8211;script</code> option. They are loaded in alphabetical order. </p>
<p> The <code>&#8211;load-scripts=no</code> option disables loading these files. </p>
<p> See <i>Script location</i> for details.</p>
<dt><code>~/.config/mpv/watch_later/</code></p>
<dd>Contains temporary config files needed for resuming playback of files with the watch later feature. See for example the <code>Q</code> key binding, or the <code>quit-watch-later</code> input command. </p>
<p> Each file is a small config file which is loaded if the corresponding media file is loaded. It contains the playback position and some (not necessarily all) settings that were changed during playback. The filenames are hashed from the full paths of the media files. It&#8217;s in general not possible to extract the media filename from this hash. However, you can set the <code>&#8211;write-filename-in-watch-later-config</code> option, and the player will add the media filename to the contents of the resume config file.</p>
<dt><code>~/.config/mpv/script-opts/osc.conf</code></p>
<dd>This is loaded by the OSC script. See the <i>ON SCREEN CONTROLLER</i> docs for details. </p>
<p> Other files in this directory are specific to the corresponding scripts as well, and the mpv core doesn&#8217;t touch them.</dl>
<h2>Files On Windows</h2>
<p>On win32 (if compiled with MinGW, but not Cygwin), the default config file locations are different. They are generally located under <code>%APPDATA%/mpv/</code>. For example, the path to mpv.conf is <code>%APPDATA%/mpv/mpv.conf</code>, which maps to a system and user-specific path, for example <code>C:
