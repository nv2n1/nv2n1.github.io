---
title: "alsactl_init(7)"
name: "alsactl_init"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alsactl_init/"
description: "alsactl_init – alsa control management – initialization"
---

<p>alsactl_init &#8211; alsa control management &#8211; initialization</p>
<h2>Description</h2>
<p>&quot;alsactl init&quot; provides soundcard specific initialization.</p>
<h2>Configuration</h2>
<p>All &quot;alsactl init&quot; configuration files are placed in /usr/share/alsa/init/ directory. The top level configuration file is /usr/share/alsa/init/00main. The default top-level file can be also specified using -i or &#8211;initfile parameter for the alsactl tool. Every file consists of a set of lines of text. All empty lines or lines beginning with &#8216;#&#8217; will be ignored.</p>
<h3>Rules files</h3>
<p>The &quot;alsactl init&quot; rules are read from the files located in the /usr/share/alsa/init/*. The top level configuration file is /usr/share/alsa/init/00main. Every line in the rules file contains at least one key value pair. There are two kind of keys, match and assignment keys. If all match keys are matching against its value, the rule gets applied and the assign keys get the specified value assigned. </p>
<p> A rule may consists of a list of one or more key value pairs separated by a comma. Each key has a distinct operation, depending on the used operator. Valid operators are: </p>
<p> <code>==</code></p>
<dl>
<dd>Compare for equality.</dl>
<p> <code>!=</code></p>
<dl>
<dd>Compare for non-equality.</dl>
<p> <code>=</code></p>
<dl>
<dd>Assign a value to a key. Keys that represent a list, are reset and only this single value is assigned.</dl>
<p> <code>+=</code></p>
<dl>
<dd>Add the value to a key that holds a list of entries.</dl>
<p> <code>:=</code></p>
<dl>
<dd>Assign a value to a key finally; disallow any later changes, which may be used to prevent changes by any later rules.</dl>
<p> The following key names can be used to match against device properties: </p>
<p> <code>CARDINDEX</code></p>
<dl>
<dd>Match the card index of the ALSA driver.</dl>
<p> <code>CTL{</code><i>attribute</i><code>}</code></p>
<dl>
<dd>Set or test universal control attribute. Possible attributes: </p>
<p> <code>numid</code></p>
<dl>
<dd>Numeric control identification.</dl>
<p> <code>iface</code>, <code>interface</code></p>
<dl>
<dd>Control interface name (CARD, HWEDEP, MIXER, PCM, RAWMIDI, TIMER, SEQUENCER)</dl>
<p> <code>subdev</code>, <code>subdevice</code></p>
<dl>
<dd>Subdevice number.</dl>
<p> <code>name</code></p>
<dl>
<dd>Control name</dl>
<p> <code>index</code></p>
<dl>
<dd>Control index</dl>
<p> <code>type</code></p>
<dl>
<dd>Control type (BOOLEAN, INTEGER, INTEGER64, ENUMERATED, BYTES, IEC958)</dl>
<p> <code>attr</code>, <code>attribute</code></p>
<dl>
<dd>Attributes (stored in a string &#8211; use match characters * and ?): </p>
<p> <code>r</code></p>
<dl>
<dd>control is readable</dl>
<p> <code>w</code></p>
<dl>
<dd>control is writable</dl>
<p> <code>v</code></p>
<dl>
<dd>control is volatile</dl>
<p> <code>i</code></p>
<dl>
<dd>control is inactive</dl>
<p> <code>l</code></p>
<dl>
<dd>control is locked</dl>
<p> <code>R</code></p>
<dl>
<dd>control is TLV readable</dl>
<p> <code>W</code></p>
<dl>
<dd>control is TLV writable</dl>
<p> <code>C</code></p>
<dl>
<dd>control is TLV commandable</dl>
<p> <code>o</code></p>
<dl>
<dd>process is owner of this control</dl>
<p> <code>u</code></p>
<dl>
<dd>control created in user space</dl>
</dl>
<p> <code>owner</code></p>
<dl>
<dd>Control owner process PID number</dl>
<p> <code>count</code></p>
<dl>
<dd>Control count of values</dl>
<p> <code>min</code></p>
<dl>
<dd>Value range &#8211; minimum value</dl>
<p> <code>max</code></p>
<dl>
<dd>Value range &#8211; maximum value</dl>
<p> <code>step</code></p>
<dl>
<dd>Value range &#8211; step value</dl>
<p> <code>dBmin</code></p>
<dl>
<dd>Value range &#8211; minimum dB value</dl>
<p> <code>dBmax</code></p>
<dl>
<dd>Value range &#8211; maximum dB value</dl>
<p> <code>items</code></p>
<dl>
<dd>Enumerated value &#8211; number of text items</dl>
<p> <code>enums</code></p>
<dl>
<dd>Enumerated value &#8211; list of text names stored between &#8216;|&#8217; character</dl>
<p> <code>value</code></p>
<dl>
<dd>Value of control stored to a string delimited by comma (,).</dl>
<p> <code>do_search</code></p>
<dl>
<dd>Search for a control. Value &quot;1&quot; is returned if a control was found. The CTL{name} key might contain match characters * and ?. An control index might be specified as first argument starting from zero (e.g. CTL{do_search 2}=&quot;1&quot;).</dl>
<p> <code>do_count</code></p>
<dl>
<dd>Search for a controls and return total count of matched ones. The CTL{name} key might contain match characters * and ?.</dl>
</dl>
<p> <code>CONFIG{sysfs_device}</code></p>
<dl>
<dd>The relative path to sysfs subsystem specifying the root directory of a soundcard device. Usually, it should be set to &quot;/class/sound/card$cardinfo{card}/device&quot;.</dl>
<p> <code>ATTR{</code><i>filename</i><code>}</code></p>
<dl>
<dd>Match sysfs attribute values of the soundcard device. The relative path to sysfs tree must be defined by CONFIG{sysfs_device} key. Trailing whitespace in the attribute values is ignored, if the specified match value does not contain trailing whitespace itself. Depending on the type of operator, this key is also used to set the value of a sysfs attribute.</dl>
<p> <code>ENV{</code><i>key</i><code>}</code></p>
<dl>
<dd>Match against the value of an environment variable. Up to five <code>ENV</code> keys can be specified per rule. Depending on the type of operator, this key is also used to export a variable to the environment.</dl>
<p> <code>PROGRAM</code></p>
<dl>
<dd>Execute external program. The key is true, if the program returns without exit code zero. The whole event environment is available to the executed program. The program&#8217;s output printed to stdout is available for the RESULT key. </p>
<p> Several buildin commands are available: </p>
<p> <code>__ctl_search</code></p>
<dl>
<dd>Search for a control. The CTL{name} key might contain match characters * and ?. An control index might be specified as first argument starting from zero (e.g. PROGRAM=&quot;__ctl_search 2&quot;).</dl>
<p> <code>__ctl_count</code></p>
<dl>
<dd>Search for a controls and return total count of matched ones. The CTL{name} key might contain match characters * and ?.</dl>
</dl>
<p> <code>RESULT</code></p>
<dl>
<dd>Match the returned string of the last PROGRAM call. This key can be used in the same or in any later rule after a PROGRAM call.</dl>
<p> Most of the fields support a shell style pattern matching. The following pattern characters are supported: </p>
<p> <code>*</code></p>
<dl>
<dd>Matches zero, or any number of characters.</dl>
<p> <code>?</code></p>
<dl>
<dd>Matches any single character.</dl>
<p> <code>[]</code></p>
<dl>
<dd>Matches any single character specified within the brackets. For example, the pattern string &#8216;tty[SR]&#8217; would match either &#8216;ttyS&#8217; or &#8216;ttyR&#8217;. Ranges are also supported within this match with the &#8216;-&#8216; character. For example, to match on the range of all digits, the pattern [0-9] would be used. If the first character following the &#8216;[&#8216; is a &#8216;!&#8217;, any characters not enclosed are matched.</dl>
<p> The following keys can get values assigned: </p>
<p> <code>CTL{numid}</code>, <code>CTL{iface}</code>, <code>CTL{device}</code>, <code>CTL{subdev}</code>, <code>CTL{name}</code>, <code>CTL{index}</code>,</p>
<dl>
<dd>Select universal control element.</dl>
<p> <code>CTL{value}</code></p>
<dl>
<dd>Value is set (written) also to soundcard&#8217;s control device and RESULT key is set to errno code. The result of set operation is always true (it means continue with next key on line).</dl>
<p> <code>CTL{values}</code></p>
<dl>
<dd>Value is set (written) also to soundcard&#8217;s control device (all control values are set to specified value) and RESULT key is set to errno code. The result of set operation is always true (it means continue with next key on line).</dl>
<p> <code>CTL{write}</code></p>
<dl>
<dd>Value is set (written) also to soundcard&#8217;s control device (all control values are set to specified value). The result of set operation is true when operation succeed (it means continue with next key on line).</dl>
<p> <code>ENV{</code><i>key</i><code>}</code></p>
<dl>
<dd>Export a variable to the environment. Depending on the type of operator, this key is also to match against an environment variable.</dl>
<p> <code>RESULT</code></p>
<dl>
<dd>Set RESULT variable. Note that PROGRAM also sets this variable, but setting this variable manually might be useful to change code execution order (included files).</dl>
<p> <code>LABEL</code></p>
<dl>
<dd>Named label where a GOTO can jump to.</dl>
<p> <code>GOTO</code></p>
<dl>
<dd>Jumps to the next LABEL with a matching name. The goto cannot jump backward.</dl>
<p> <code>INCLUDE</code></p>
<dl>
<dd>Include the specified filename or files in specified directory. </p>
<p> When a directory is specified, only the files with the extension &quot;.conf&quot; are read. Also they are read in the alphabetical order. Thus it&#8217;s highly recommended to use some number prefix (e.g. &quot;01-something.conf&quot;) to assure the order of execucions.</dl>
<p> <code>ACCESS</code></p>
<dl>
<dd>Check if specified file or directory exists</dl>
<p> <code>CONFIG{sysfs_device}</code></p>
<dl>
<dd>The relative path to sysfs subsystem specifying the root directory of a soundcard device. Usually, it should be set to &quot;/class/sound/card$cardinfo{card}/device&quot;.</dl>
<p> <code>PRINT</code></p>
<dl>
<dd>PRINT value to stdout.</dl>
<p> <code>ERROR</code></p>
<dl>
<dd>PRINT value to stderr.</dl>
<p> <code>EXIT</code></p>
<dl>
<dd>Exit immediately and set program exit code to value (should be integer). If value is &quot;return&quot; string, parser leaves current included file and returns to parent configuration file.</dl>
<p> The <code>PROGRAM</code>, <code>RESULT</code>, <code>CTL{value}</code>, <code>PRINT</code>, <code>ERROR</code>, <code>EXIT</code>, <code>CONFIG{}</code> fields support simple printf-like string substitutions. It allows the use of the complete environment set by earlier matching rules. For all other fields, substitutions are applied while the individual rule is being processed. The available substitutions are: </p>
<p> <code>$cardinfo{</code><i>attribute</i><code>}</code>, <code>%i{</code><i>attribute</i><code>}</code></p>
<dl>
<dd>See CARDINFO{} for more details.</dl>
<p> <code>$ctl{</code><i>attribute</i><code>}</code>, <code>%C{</code><i>attribute</i><code>}</code></p>
<dl>
<dd>See CTL{} for more details.</dl>
<p> <code>$attr{</code><i>file</i><code>}</code>, <code>%s{</code><i>file</i><code>}</code></p>
<dl>
<dd>The value of a sysfs attribute found at the device, where all keys of the rule have matched. If the attribute is a symlink, the last element of the symlink target is returned as the value.</dl>
<p> <code>$env{</code><i>key</i><code>}</code>, <code>%E{</code><i>key</i><code>}</code></p>
<dl>
<dd>The value of an environment variable.</dl>
<p> <code>$result</code>, <code>%c</code></p>
<dl>
<dd>The string returned by the external program requested with PROGRAM. A single part of the string, separated by a space character may be selected by specifying the part number as an attribute: <code>%c{N}</code>. If the number is followed by the &#8216;+&#8217; char this part plus all remaining parts of the result string are substituted: <code>%c{N+}</code></dl>
<p> <code>$sysfsroot</code>, <code>%r</code></p>
<dl>
<dd>Root directory where sysfs file-system is mounted. Ususally, this value is just &quot;/sys&quot;.</dl>
<p> <code>$config{</code><i>key</i><code>}</code>, <code>%g{</code><i>key</i><code>}</code></p>
<dl>
<dd>The value of a configuration variable. See CONFIG{} for more details.</dl>
<p> <code>%%</code></p>
<dl>
<dd>The &#8216;%&#8217; character itself.</dl>
<p> <code>$$</code></p>
<dl>
<dd>The &#8216;$&#8217; character itself.</dl>
<p> The count of characters to be substituted may be limited by specifying the format length value. For example, &#8216;%3s{file}&#8217; will only insert the first three characters of the sysfs attribute</p>
<h2>Author</h2>
<p>Written by Jaroslav Kysela &lt;perex [at] perex.cz&gt; </p>
<p> Some portions are written by Greg Kroah-Hartman &lt;greg [at] kroah.com&gt; and Kay Sievers &lt;kay.sievers [at] vrfy.org&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-alsactl/">alsactl</a></code>(1) </p>
