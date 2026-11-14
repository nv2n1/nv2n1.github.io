---
title: "alsaucm(1)"
name: "alsaucm"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alsaucm/"
description: "alsaucm – ALSA Use Case Manager"
---

<h2 class="name">NAME</h2>
<p> alsaucm &#8211; ALSA Use Case Manager </p>
<h2>SYNOPSIS</h2>
<p> <i>alsaucm</i> &lt;options&gt; [command]</p>
<h2>DESCRIPTION</h2>
<p> alsaucm (ALSA Use Case Manager) is a program to use the ALSA <i>Use Case Interface</i> from the command line. </p>
<p> On complex sound cards, setting up audio routes is not trivial and mixer settings can conflict one another preventing the audio card to work at all. </p>
<p> The ALSA Use Case Manager is a mechanism for controlling complex audio hardware establishing a relationship between hardware configurations and meaningful use cases that the end-user can relate with. </p>
<p> The use case manager can also be used to switch between use cases when necessary, in a consistent way. </p>
<p> At a lower level, the use case manager works by configuring the sound card ALSA kcontrols to change the hardware digital and analog audio routing to match the requested device use case. </p>
<p> The use case manager kcontrol configurations are stored in easy to modify text files. An audio use case can be defined by a <code>verb</code> and <code>device</code> parameter. </p>
<p> The verb describes the use case action i.e. a phone call, listening to music, recording a conversation etc. The device describes the physical audio capture and playback hardware i.e. headphones, phone handset, bluetooth headset, etc.</p>
<h2>OPTIONS</h2>
<p> Available options:</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> this help</p>
<dt><code>-c</code>, <code>&#8211;card</code> <i>NAME</i></p>
<dd> open card NAME</p>
<dt><code>-i</code>, <code>&#8211;interactive</code></p>
<dd> interactive mode</p>
<dt><code>-b</code>, <code>&#8211;batch</code> <i>FILE</i></p>
<dd> batch mode (use <code>&#8216;-&#8216;</code> for the stdin input)</p>
<dt><code>-n</code>, <code>&#8211;no-open</code></p>
<dd> do not open first card found </p>
<p> Available commands:</p>
<dt><code>open</code> <i>NAME</i></p>
<dd> open card NAME. </p>
<p> valid names are sound card names as listed in <code>/usr/share/alsa/ucm</code>.</p>
<dt><code>reset</code></p>
<dd> reset sound card to default state.</p>
<dt><code>reload</code></p>
<dd> reload configuration.</p>
<dt><code>listcards</code></p>
<dd> list available cards.</p>
<dt><code>list</code> <i>IDENTIFIER</i></p>
<dd> list command, for items returning two entries (value+comment). </p>
<p> the value of the <i>IDENTIFIER</i> argument can can be:</p>
<dt>&bull;</p>
<dd> <code>_verbs</code> &#8211; get verb list (in pair verb+comment)</p>
<dt>&bull;</p>
<dd> <code>_devices[/{verb}]</code> &#8211; get list of supported devices (in pair device+comment)</p>
<dt>&bull;</p>
<dd> <code>_modifiers[/{verb}]</code> &#8211; get list of supported modifiers (in pair modifier+comment) </p>
<p> The forms without the trailing <code>/{verb}</code> are valid only after a specific verb has been set.</p>
<dt><code>list1</code> <i>IDENTIFIER</i></p>
<dd> list command, for lists returning one item per entry. </p>
<p> the value of the <i>IDENTIFIER</i> argument can vary depending on the context, it can be:</p>
<dt>&bull;</p>
<dd> <code>TQ[/{verb}]</code> &#8211; get list of Tone Quality identifiers</p>
<dt>&bull;</p>
<dd> <code>_enadevs</code> &#8211; get list of enabled devices</p>
<dt>&bull;</p>
<dd> <code>_enamods</code> &#8211; get list of enabled modifiers</p>
<dt>&bull;</p>
<dd> <code>_supporteddevs/{modifier}|{device}[/{verb}]</code> &#8211; list of supported devices</p>
<dt>&bull;</p>
<dd> <code>_conflictingdevs/{modifier}|{device}[/{verb}]</code> &#8211; list of conflicting devices</p>
<dt><code>get</code> <i>IDENTIFIER</i></p>
<dd> get string value. </p>
<p> the value of the <i>IDENTIFIER</i> argument can can be:</p>
<dt>&bull;</p>
<dd> <code>_verb</code> &#8211; return current verb</p>
<dt>&bull;</p>
<dd> <code>[=]{NAME}[/[{modifier}|{/device}][/{verb}]]</code> (For valid NAMEs look at the ALSA <i>Use Case Interface</i>)</p>
<dt><code>geti</code> <i>IDENTIFIER</i></p>
<dd> get integer value. </p>
<p> the value of the <i>IDENTIFIER</i> argument can can be:</p>
<dt>&bull;</p>
<dd> <code>_devstatus/{device}</code></p>
<dt>&bull;</p>
<dd> <code>_modstatus/{device}</code></p>
<dt><code>set</code> <i>IDENTIFIER</i> <i>VALUE</i></p>
<dd> set string value </p>
<p> The value of the <i>IDENTIFIER</i> argument can can be:</p>
<dt>&bull;</p>
<dd> <code>_verb</code> &#8211; set the verb to <i>VALUE</i></p>
<dt>&bull;</p>
<dd> <code>_enadev</code> &#8211; enable the device specified by <i>VALUE</i></p>
<dt>&bull;</p>
<dd> <code>_disdev</code> &#8211; disable the device specified by <i>VALUE</i></p>
<dt>&bull;</p>
<dd> <code>_swdev/{old_device}</code> &#8211; switche device:</p>
<dt>&bull;</p>
<dd> disable <i>old_device</i> and then enable the device specified by <i>VALUE</i></p>
<dt>&bull;</p>
<dd> if no device was enabled just return</p>
<dt>&bull;</p>
<dd> <code>_enamod</code> &#8211; enable the modifier specified by <i>VALUE</i></p>
<dt>&bull;</p>
<dd> <code>_dismod</code> &#8211; disable the modifier specified by <i>VALUE</i></p>
<dt>&bull;</p>
<dd> <code>_swmod/{old_modifier}</code> &#8211; switch modifier:</p>
<dt>&bull;</p>
<dd> disable <i>old_modifier</i> and then enable the modifier specified by <i>VALUE</i></p>
<dt>&bull;</p>
<dd> if no modifier was enabled just return </p>
<p> Note that the identifiers referring to devices and modifiers are valid only after setting a verb.</p>
<dt><code>h</code>, <code>help</code></p>
<dd> help</p>
<dt><code>q</code>, <code>quit</code></p>
<dd> quit</dl>
<h2>FILES</h2>
<p> The master use case files for each supported sound card are in <code>/usr/share/alsa/ucm</code>. </p>
<p> For example, the master use case file for the <i>Pandaboard</i> card is in <code>/usr/share/alsa/ucm/PandaBoard/PandaBoard.conf</code>, this file lists all the supported use cases, e.g. </p>
<pre>
SectionUseCase.&quot;HiFi&quot; {
                File &quot;hifi&quot;
                Comment &quot;Play HiFi quality Music.&quot;
}
...
</pre>
<p> Each use case defines a _verb, which is described in the file specified in the <code>File</code> directive, like above. </p>
<p> The <code>HiFi</code> verb above is described in <code>/usr/share/alsa/ucm/PandaBoard/hifi</code>. </p>
<p> For more details on the syntax of UCM files, see the alsa-lib source code: <i><a rel="nofollow" href="http://git.alsa-project.org/?p=alsa-lib.git;a=blob;f=src/ucm/parser.c">http://git.alsa-project.org/?p=alsa-lib.git;a=blob;f=src/ucm/parser.c</a></i></p>
<h2>EXAMPLES OF USE</h2>
<p> Some commands, like for instance <code>list _devices</code>, can only work after setting a <code>_verb</code> in the <code>same execution</code>, for instance this sequence doesn&#8217;t work: </p>
<pre>
# alsaucm -c bytcr-rt5640 set _verb HiFi
# alsaucm -c bytcr-rt5640 list _devices
</pre>
<p> However this command does: </p>
<pre>
# alsaucm -n -b - &lt;&lt;EOM
open bytcr-rt5640
set _verb HiFi
list _devices
EOM
</pre>
<p> An example of setting the <i>Speaker</i> device for the <i>HiFi</i> verb of the <i>bytcr-rt5640</i> card: </p>
<pre>
# alsaucm -n -b - &lt;&lt;EOM
open bytcr-rt5640
reset
set _verb HiFi
set _enadev Speaker
EOM
</pre>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> Use Case Interface: <i><a rel="nofollow" href="http://www.alsa-project.org/alsa-doc/alsa-lib/group__ucm.html">http://www.alsa-project.org/alsa-doc/alsa-lib/group__ucm.html</a></i></dl>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> Antonio Ospite &lt;ao2 [at] ao2.it&gt;</p>
<h2>COPYRIGHT</h2>
<p> GPLv2+ </p>
<h2>Index</h2>
