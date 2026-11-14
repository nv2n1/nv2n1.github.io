---
title: "brltty-conf(5)"
name: "brltty-conf"
section: "5"
letter: "b"
url: "/docs/linux/man/5-brltty-conf/"
description: "brltty – refreshable braille display driver for Linux/Unix"
---

<p>brltty &#8211; refreshable braille display driver for Linux/Unix</p>
<h2>Synopsis</h2>
<p><code>brltty </code>[<i>option</i> &#8230;]</p>
<h2>Description</h2>
<p><code>brltty</code> is a background process (daemon) which provides access to the console screen (when in text mode) for a blind person using a refreshable braille display. It drives the braille display, and provides complete screen review functionality. Some speech capability has also been incorporated.</p>
<h2>Options</h2>
<p>Options can be passed to <code>brltty</code> in a number of ways. From most to least influential, these are:</p>
<dl>
<dt>1.</p>
<dd>Command Line Options</p>
<dt>2.</p>
<dd>Boot Parameters</p>
<dt>3.</p>
<dd>Environment Variables (if the <code>-E</code> (<code>&#8211;environment-variables</code>) option is in effect)</p>
<dt>4.</p>
<dd>The Configuration File</p>
<dt>5.</p>
<dd>Built-in Defaults</dl>
<h3>Command Line Options</h3>
<p>The options are processed sequentially from left to right. If an option is specified more than once, or in case of a conflict, the rightmost specification takes precedence. </p>
<p> The following options are supported:</p>
<dl>
<dt><code>-a </code><i>table</i> (<code>&#8211;attributes-table=</code>)</p>
<dd>The path to the attributes table. Relative paths are anchored at <code>/etc/brltty</code>. The <code>.atb</code> extension is optional. The built-in default is <code>attributes.atb</code>.</p>
<dt><code>-b </code><i>driver</i><code>,</code>&#8230;|<code>auto</code> (<code>&#8211;braille-driver=</code>)</p>
<dd>The driver for the braille display (see Driver Specification). The built-in default is <code>auto</code>.</p>
<dt><code>-c </code><i>table</i> (<code>&#8211;contraction-table=</code>)</p>
<dd>The path to the contraction table. Relative paths are anchored at <code>/etc/brltty</code>. The <code>.ctb</code> extension is optional.</p>
<dt><code>-d </code><i>device</i><code>,</code>&#8230; (<code>&#8211;braille-device=</code>)</p>
<dd>The device to which the braille display is connected. The built-in default is <code>usb:</code>.</p>
<dl>
<dd>The general form of a braille device specification is <i>qualifier</i><code>:</code><i>data</i>. For backward compatibility with earlier releases, if the qualifier is omitted then <code>serial:</code> is assumed. The following device types are supported:</p>
<dl>
<dt><code>Bluetooth</code></p>
<dd>For a bluetooth device, specify <code>bluez:</code><i>address</i>. The address must be six two-digit hexadecimal numbers separated by colons, e.g. <code>01:23:45:67:89:AB</code>.</p>
<dt><code>Serial</code></p>
<dd>For a serial device, specify <code>serial:</code><i>/path/to/device</i>. The <code>serial:</code> qualifier is optional (for backward compatibility). If a relative path is given then it&#8217;s anchored at <code>/dev/</code> (the usual location where devices are defined on a Unix-like system). The following device specifications all refer to the primary serial device: <code>serial:/dev/ttyS0</code>, <code>serial:ttyS0</code>, <code>/dev/ttyS0</code>, <code>ttyS0</code>.</p>
<dt><code>USB</code></p>
<dd>For a USB device, specify <code>usb:</code>. <code>brltty</code> will search for the first USB device which matches the braille display driver being used. If this is inadequate, e.g. if you have more than one USB braille display which requires the same driver, then you can refine the device specification by appending the serial number of the display to it, e.g. <code>usb:12345</code>. N.B.: The &quot;identification by serial number&quot; feature doesn&#8217;t work for some models because some manufacturers either don&#8217;t set the USB serial number descriptor at all or do set it but not to a unique value.</dl>
<p> A comma-delimited list of braille devices may be specified. If this is done then autodetection is performed on each listed device in sequence. This feature is particularly useful if you have a braille display with more than one interface, e.g. both a serial and a USB port.</dl>
<dt><code>-e</code> (<code>&#8211;standard-error</code>)</p>
<dd>Write logs to standard error rather than to the system log (useful for debugging).</p>
<dt><code>-f </code><i>file</i> (<code>&#8211;configuration-file=</code>)</p>
<dd>The path to the configuration file. Relative paths are anchored at the current working directory. The built-in default is <code>/etc/brltty.conf</code>.</p>
<dt><code>-h</code> (<code>&#8211;help</code>)</p>
<dd>Print a command line usage summary and then exit.</p>
<dt><code>-i </code><i>name</i> (<code>&#8211;speech-input=</code>)</p>
<dd>The file system object (FIFO, named pipe, named socket, etc) which gives other applications access to <code>brltty</code>&#8216;s speech driver for text-to-speech conversion. It&#8217;s created at start-up and removed at termination. Relative paths are anchored at the current working directory. The built-in default is that the file system object is not created.</p>
<dt><code>-k </code><i>file</i> (<code>&#8211;key-table=</code>)</p>
<dd>Path to key table file.</p>
<dt><code>-l </code><i>level</i> (<code>&#8211;log-level=</code>)</p>
<dd>The minimum severity level for messages written to the log. Any of the following numbers, or any abbreviation of their corresponding names, may be specified:</p>
<dl>
<dd>
<dl>
<dt><code>0</code></p>
<dd><code>emergency</code></p>
<dt><code>1</code></p>
<dd><code>alert</code></p>
<dt><code>2</code></p>
<dd><code>critical</code></p>
<dt><code>3</code></p>
<dd><code>error</code></p>
<dt><code>4</code></p>
<dd><code>warning</code></p>
<dt><code>5</code></p>
<dd><code>notice</code></p>
<dt><code>6</code></p>
<dd><code>information</code></p>
<dt><code>7</code></p>
<dd><code>debug</code></dl>
</dl>
</dl>
<p> The built-in default is <code>notice</code>.</p>
<dl>
<dt><code>-m </code><i>device</i> (<code>&#8211;midi-device=</code>)</p>
<dd>The device to use for the Musical Instrument Digital Interface. For ALSA it&#8217;s <i>client</i><code>:</code><i>port</i>, where each may be either a number or a case-sensitive substring of its name. For other interfaces it&#8217;s the full path to an appropriate system device. The built-in default is:</p>
<dl>
<dd>
<dl>
<dt>Linux/ALSA</p>
<dd>the first available MIDI output port</p>
<dt>Linux/OSS</p>
<dd><code>/dev/sequencer</code></dl>
</dl>
<dt><code>-n</code> (<code>&#8211;no-daemon</code>)</p>
<dd>Remain in the foreground (useful for debugging).</p>
<dt><code>-p </code><i>device</i> (<code>&#8211;pcm-device=</code>)</p>
<dd>The device to use for digital audio. For ALSA it&#8217;s <i>name</i>[<code>:</code><i>argument</i><code>,</code>&#8230;]. For other interfaces it&#8217;s the full path to an appropriate system device. The built-in default is:</p>
<dl>
<dd>
<dl>
<dt>FreeBSD</p>
<dd><code>/dev/dsp</code></p>
<dt>Linux/ALSA</p>
<dd><code>hw:0,0</code></p>
<dt>Linux/OSS</p>
<dd><code>/dev/dsp</code></p>
<dt>NetBSD</p>
<dd><code>/dev/audio</code></p>
<dt>OpenBSD</p>
<dd><code>/dev/audio</code></p>
<dt>Qnx</p>
<dd>the preferred PCM output device</p>
<dt>Solaris</p>
<dd><code>/dev/audio</code></dl>
</dl>
<dt><code>-q</code> (<code>&#8211;quiet</code>)</p>
<dd>Suppress the start-up messages. This is done by reducing the default log level (see the <code>-l</code> (<code>&#8211;log-level=</code>) option) to <code>warning</code> (<code>information</code> if either <code>-v</code> (<code>&#8211;verify</code>) or <code>-V</code> (<code>&#8211;version</code>) is also specified).</p>
<dt><code>-r</code> (<code>&#8211;release-device</code>)</p>
<dd>Release the device to which the braille display is connected when the current screen or window can&#8217;t be read.</p>
<dt><code>-s </code><i>driver</i><code>,</code>&#8230;|<code>auto</code> (<code>&#8211;speech-driver=</code>)</p>
<dd>The driver for the speech synthesizer (see Driver Specification). The built-in default is <code>auto</code>.</p>
<dt><code>-t </code><i>table</i> (<code>&#8211;text-table=</code>)</p>
<dd>The path to the text table. Relative paths are anchored at <code>/etc/brltty</code>. The <code>.ttb</code> extension is optional. The built-in default is <code>nabcc.ttb</code> (the North American Braille Computer Code).</p>
<dt><code>-v</code> (<code>&#8211;verify</code>)</p>
<dd>Print the start-up messages and then exit. This always includes the versions of <code>brltty</code> itself, the server side of its application programming interface, and each of the selected braille and speech drivers. If the <code>-q</code> (<code>&#8211;quiet</code>) option isn&#8217;t also specified then it also includes the values of the options after all sources have been considered. If more than one braille driver and/or more than one braille device has been specified then braille display autodetection is performed. If more than one speech driver has been specified then speech synthesizer autodetection is performed.</p>
<dt><code>-x </code><i>driver</i> (<code>&#8211;screen-driver=</code>)</p>
<dd>The screen driver. The built-in default is operating system appropriate.</p>
<dt><code>-A </code><i>name</i><code>=</code><i>value</i><code>,</code>&#8230; (<code>&#8211;api-parameters=</code>)</p>
<dd>Parameters for the application programming interface. If the same parameter is specified more than once then the rightmost specification is used. Parameter names may be abbreviated.</p>
<dt><code>-B </code>[<i>driver</i><code>:</code>]<i>name</i><code>=</code><i>value</i><code>,</code>&#8230; (<code>&#8211;braille-parameters=</code>)</p>
<dd>Parameters for the braille display driver. If the same parameter is specified more than once then the rightmost specification is used. Parameter names may be abbreviated. If a parameter assignment is qualified with a driver identification code then it&#8217;s only processed if that braille display driver is being used.</p>
<dt><code>-D</code> (<code>&#8211;drivers-directory=</code>)</p>
<dd>Path to directory for loading drivers.</p>
<dt><code>-E</code> (<code>&#8211;environment-variables</code>)</p>
<dd>Recognize environment variables.</p>
<dt><code>-F </code><i>file</i> (<code>&#8211;preferences-file=</code>)</p>
<dd>The path to the preferences file. Relative paths are anchored at <code>/var/lib/brltty</code>. The built-in default is <code>brltty.prefs</code>.</p>
<dt><code>-H</code> (<code>&#8211;full-help</code>)</p>
<dd>Print a usage summary (all options), and then exit.</p>
<dt><code>-I</code> (<code>&#8211;install-service</code>)</p>
<dd>(Windows only) Install <code>brltty</code> as the <code>BrlAPI</code> service so that it will be automatically started when the system is booted and so that applications can know that a <code>BrlAPI</code> server is running.</p>
<dt><code>-K </code><i>arg</i> (<code>&#8211;keyboard-properties=</code>)</p>
<dd>Properties of the keyboard.</p>
<dt><code>-L </code><i>file</i> (<code>&#8211;log-file=</code>)</p>
<dd>The file to which log messages are written. Relative paths are anchored at the current working directory. The default is to send log messages to the system log.</p>
<dt><code>-M </code><i>csecs</i> (<code>&#8211;message-delay=</code>)</p>
<dd>The message hold time in hundredths of a second. The built-in default is <code>400</code> (4 seconds).</p>
<dt><code>-N</code> (<code>&#8211;no-api</code>)</p>
<dd>Don&#8217;t start the application programming interface.</p>
<dt><code>-P </code><i>file</i> (<code>&#8211;pid-file=</code>)</p>
<dd>The full path to the process identifier file. If this option is supplied, <code>brltty</code> writes its process identifier (pid) into the specified file at start-up. The file is removed when <code>brltty</code> terminates.</p>
<dt><code>-R</code> (<code>&#8211;remove-service</code>)</p>
<dd>(Windows only) Remove the <code>BrlAPI</code> service so that <code>brltty</code> will not be automatically started when the system is booted and so that applications can know that no <code>BrlAPI</code> server is running.</p>
<dt><code>-S </code>[<i>driver</i><code>:</code>]<i>name</i><code>=</code><i>value</i><code>,</code>&#8230; (<code>&#8211;speech-parameters=</code>)</p>
<dd>Parameters for the speech synthesizer driver. If the same parameter is specified more than once then the rightmost specification is used. Parameter names may be abbreviated. If a parameter assignment is qualified with a driver identification code then it&#8217;s only processed if that speech synthesizer driver is being used.</p>
<dt><code>-T </code><i>directory</i> (<code>&#8211;tables-directory=</code>)</p>
<dd>Path to directory for text and attributes tables.</p>
<dt><code>-U </code><i>csecs</i> (<code>&#8211;update-interval=</code>)</p>
<dd>The braille window update interval in hundredths of a second. The built-in default is <code>4</code> (25 times per second).</p>
<dt><code>-V</code> (<code>&#8211;version</code>)</p>
<dd>Print the versions of <code>brltty</code> itself, the server side of its application programming interface, and those drivers which were configured in at build-time, and then exit. If the <code>-q</code> (<code>&#8211;quiet</code>) option isn&#8217;t also specified then also print copyright information.</p>
<dt><code>-W </code><i>directory</i> (<code>&#8211;writable-directory=</code>)</p>
<dd>Path to directory which can be written to.</p>
<dt><code>-X </code><i>name</i><code>=</code><i>value</i><code>,</code>&#8230; (<code>&#8211;screen-parameters=</code>)</p>
<dd>Parameters for the screen driver. If the same parameter is specified more than once then the rightmost specification is used. Parameter names may be abbreviated.</dl>
<h3>Environment Variables</h3>
<p>The following environment variables are recognized if the <code>-E</code> (<code>&#8211;environment-variables</code>) option is specified:</p>
<dl>
<dt><code>BRLTTY_API_PARAMETERS=</code><i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</p>
<dd>Parameters for the application programming interface. See the <code>-A</code> (<code>&#8211;api-parameters=</code>) option for details.</p>
<dt><code>BRLTTY_ATTRIBUTES_TABLE=</code><i>table</i></p>
<dd>The attributes table. See the <code>-a</code> (<code>&#8211;attributes-table=</code>) option for details.</p>
<dt><code>BRLTTY_BRAILLE_DEVICE=</code><i>device</i><code>,</code>&#8230;</p>
<dd>The device to which the braille display is connected. See the <code>-d</code> (<code>&#8211;braille-device=</code>) option for details.</p>
<dt><code>BRLTTY_BRAILLE_DRIVER=</code><i>driver</i><code>,</code>&#8230;|<code>auto</code></p>
<dd>The driver for the braille display. See the <code>-b</code> (<code>&#8211;braille-driver=</code>) option for details.</p>
<dt><code>BRLTTY_BRAILLE_PARAMETERS=</code>[<i>driver</i><code>:</code>]<i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</p>
<dd>Parameters for the braille display driver. See the <code>-B</code> (<code>&#8211;braille-parameters=</code>) option for details.</p>
<dt><code>BRLTTY_CONFIGURATION_FILE=</code><i>file</i></p>
<dd>The configuration file. See the <code>-f</code> (<code>&#8211;configuration-file=</code>) option for details.</p>
<dt><code>BRLTTY_CONTRACTION_TABLE=</code><i>table</i></p>
<dd>The contraction table. See the <code>-c</code> (<code>&#8211;contraction-table=</code>) option for details.</p>
<dt><code>BRLTTY_MIDI_DEVICE=</code><i>device</i></p>
<dd>The device to use for the Musical Instrument Digital Interface. See the <code>-m</code> (<code>&#8211;midi-device=</code>) option for details.</p>
<dt><code>BRLTTY_PCM_DEVICE=</code><i>device</i></p>
<dd>The device to use for digital audio. See the <code>-p</code> (<code>&#8211;pcm-device=</code>) option for details.</p>
<dt><code>BRLTTY_PREFERENCES_FILE=</code><i>file</i></p>
<dd>The preferences file. See the <code>-F</code> (<code>&#8211;preferences-file=</code>) option for details.</p>
<dt><code>BRLTTY_RELEASE_DEVICE=on</code>|<code>off</code></p>
<dd>Release the device to which the braille display is connected when the current screen or window can&#8217;t be read. See the <code>-r</code> (<code>&#8211;release-device</code>) option for details.</p>
<dt><code>BRLTTY_SCREEN_DRIVER=</code><i>driver</i></p>
<dd>The screen driver. See the <code>-x</code> (<code>&#8211;screen-driver=</code>) option for details.</p>
<dt><code>BRLTTY_SCREEN_PARAMETERS=</code><i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</p>
<dd>Parameters for the screen driver. See the <code>-X</code> (<code>&#8211;screen-parameters=</code>) option for details.</p>
<dt><code>BRLTTY_SPEECH_DRIVER=</code><i>driver</i><code>,</code>&#8230;|<code>auto</code></p>
<dd>The driver for the speech synthesizer. See the <code>-s</code> (<code>&#8211;speech-driver=</code>) option for details.</p>
<dt><code>BRLTTY_SPEECH_INPUT=</code><i>name</i></p>
<dd>The file system object which gives other applications access to <code>brltty</code>&#8216;s speech driver for text-to-speech conversion. See the <code>-i</code> (<code>&#8211;speech-input=</code>) option for details.</p>
<dt><code>BRLTTY_SPEECH_PARAMETERS=</code>[<i>driver</i><code>:</code>]<i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</p>
<dd>Parameters for the speech synthesizer driver. See the <code>-S</code> (<code>&#8211;speech-parameters=</code>) option for details.</p>
<dt><code>BRLTTY_TEXT_TABLE=</code><i>table</i></p>
<dd>The text table. See the <code>-t</code> (<code>&#8211;text-table=</code>) option for details.</dl>
<h3>The Configuration File</h3>
<p>Blank lines are ignored. If the character <code>#</code> occurs on any line then all characters from it to the end of that line are treated as a comment. </p>
<p> The following configuration directives are supported:</p>
<dl>
<dt><code>api-parameters </code><i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</p>
<dd>Parameters for the application programming interface. See the <code>-A</code> (<code>&#8211;api-parameters=</code>) option for details.</p>
<dt><code>attributes-table </code><i>table</i></p>
<dd>The attributes table. See the <code>-a</code> (<code>&#8211;attributes-table=</code>) option for details.</p>
<dt><code>braille-device </code><i>device</i><code>,</code>&#8230;</p>
<dd>The device to which the braille display is connected. See the <code>-d</code> (<code>&#8211;braille-device=</code>) option for details.</p>
<dt><code>braille-driver </code><i>driver</i><code>,</code>&#8230;|<code>auto</code></p>
<dd>The driver for the braille display. See the <code>-b</code> (<code>&#8211;braille-driver=</code>) option for details.</p>
<dt><code>braille-parameters </code>[<i>driver</i><code>:</code>]<i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</p>
<dd>Parameters for the braille display driver. See the <code>-B</code> (<code>&#8211;braille-parameters=</code>) option for details.</p>
<dt><code>contraction-table </code><i>table</i></p>
<dd>The contraction table. See the <code>-c</code> (<code>&#8211;contraction-table=</code>) option for details.</p>
<dt><code>midi-device </code><i>device</i></p>
<dd>The device to use for the Musical Instrument Digital Interface. See the <code>-m</code> (<code>&#8211;midi-device=</code>) option for details.</p>
<dt><code>pcm-device </code><i>device</i></p>
<dd>The device to use for digital audio. See the <code>-p</code> (<code>&#8211;pcm-device=</code>) option for details.</p>
<dt>The preferences file.</p>
<dd>See the <code>-F</code> (<code>&#8211;preferences-file=</code>) option for details.</p>
<dt><code>release-device on</code>|<code>off</code></p>
<dd>Release the device to which the braille display is connected when the current screen or window can&#8217;t be read. See the <code>-r</code> (<code>&#8211;release-device</code>) option for details.</p>
<dt><code>screen-driver </code><i>driver</i></p>
<dd>The screen driver. See the <code>-x</code> (<code>&#8211;screen-driver=</code>) option for details.</p>
<dt><code>screen-parameters </code><i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</p>
<dd>Parameters for the screen driver. See the <code>-X</code> (<code>&#8211;screen-parameters=</code>) option for details.</p>
<dt><code>speech-driver </code><i>driver</i><code>,</code>&#8230;|<code>auto</code></p>
<dd>The driver for the speech synthesizer. See the <code>-s</code> (<code>&#8211;speech-driver=</code>) option for details.</p>
<dt><code>speech-input me</code></p>
<dd>The file system object which gives other applications access to <code>brltty</code>&#8216;s speech driver for text-to-speech conversion. See the <code>-i</code> (<code>&#8211;speech-input=</code>) option for details.</p>
<dt><code>speech-parameters </code>[<i>driver</i><code>:</code>]<i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</p>
<dd>Parameters for the speech synthesizer driver. See the <code>-S</code> (<code>&#8211;speech-parameters=</code>) option for details.</p>
<dt><code>text-table </code><i>table</i></p>
<dd>The text table. See the <code>-t</code> (<code>&#8211;text-table=</code>) option for details.</dl>
<h3>Driver Specification</h3>
<p>A braille display or speech synthesizer driver must be specified via its identification code:</p>
<dl>
<dd>
<dl>
<dt><code>al</code></p>
<dd>Alva</p>
<dt><code>at</code></p>
<dd>Albatross</p>
<dt><code>ba</code></p>
<dd>BrlAPI</p>
<dt><code>bc</code></p>
<dd>BrailComm</p>
<dt><code>bd</code></p>
<dd>Braudi</p>
<dt><code>bl</code></p>
<dd>BrailleLite</p>
<dt><code>bm</code></p>
<dd>Baum</p>
<dt><code>bn</code></p>
<dd>BrailleNote</p>
<dt><code>cb</code></p>
<dd>CombiBraille</p>
<dt><code>ec</code></p>
<dd>EcoBraille</p>
<dt><code>es</code></p>
<dd>eSpeak</p>
<dt><code>eu</code></p>
<dd>EuroBraille</p>
<dt><code>fl</code></p>
<dd>FestivalLite</p>
<dt><code>fs</code></p>
<dd>FreedomScientific</p>
<dt><code>fv</code></p>
<dd>Festival</p>
<dt><code>gs</code></p>
<dd>GenericSay</p>
<dt><code>hm</code></p>
<dd>HIMS</p>
<dt><code>ht</code></p>
<dd>HandyTech</p>
<dt><code>hw</code></p>
<dd>HumanWare</p>
<dt><code>ir</code></p>
<dd>Iris</p>
<dt><code>lb</code></p>
<dd>Libbraille</p>
<dt><code>lt</code></p>
<dd>LogText</p>
<dt><code>mb</code></p>
<dd>MultiBraille</p>
<dt><code>md</code></p>
<dd>MDV</p>
<dt><code>mn</code></p>
<dd>MiniBraille</p>
<dt><code>mp</code></p>
<dd>Mikropuhe</p>
<dt><code>mt</code></p>
<dd>Metec</p>
<dt><code>no</code></p>
<dd>no driver</p>
<dt><code>np</code></p>
<dd>NinePoint</p>
<dt><code>pg</code></p>
<dd>Pegasus</p>
<dt><code>pm</code></p>
<dd>Papenmeier</p>
<dt><code>sd</code></p>
<dd>SpeechDispatcher</p>
<dt><code>sk</code></p>
<dd>Seika</p>
<dt><code>sw</code></p>
<dd>Swift</p>
<dt><code>th</code></p>
<dd>Theta</p>
<dt><code>tn</code></p>
<dd>TechniBraille Systems Inc.</p>
<dt><code>ts</code></p>
<dd>Telesensory Systems Inc.</p>
<dt><code>tt</code></p>
<dd>TTY</p>
<dt><code>vd</code></p>
<dd>VideoBraille</p>
<dt><code>vo</code></p>
<dd>Voyager, Part232 (serial adapter), BraillePen/EasyLink</p>
<dt><code>vr</code></p>
<dd>Virtual</p>
<dt><code>vs</code></p>
<dd>VisioBraille</p>
<dt><code>vv</code></p>
<dd>ViaVoice</p>
<dt><code>xs</code></p>
<dd>ExternalSpeech</p>
<dt><code>xw</code></p>
<dd>XWindow</dl>
<p> A comma-delimited list of drivers may be specified. If this is done then autodetection is performed using each listed driver in sequence. You may need to experiment in order to determine the most reliable order since some drivers autodetect better than others. </p>
<p> If the single word <code>auto</code> is specified then autodetection is performed using only those drivers which are known to be reliable for this purpose.</dl>
<h2>See Also</h2>
<p>For full documentation, see <code>brltty</code>&#8216;s on-line manual at [<code><a rel="nofollow" href="http://mielke.cc/brltty/doc/Manual-HTML/Manual.html">http://mielke.cc/brltty/doc/Manual-HTML/Manual.html</a></code>]. </p>
