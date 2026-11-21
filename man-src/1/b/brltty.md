---

title: "brltty(1)"
name: "brltty"
section: "1"
letter: "b"
url: "/docs/linux/man/1-brltty/"
description: "brltty – refreshable braille display driver for Linux/Unix"
---

<p> brltty &#8211; refreshable braille display driver for Linux/Unix </p>
<h2>SYNOPSIS</h2>
<p> <code>brltty </code>[<i>option</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>brltty</code> is a background process (daemon) which provides access to the console screen (when in text mode) for a blind person using a refreshable braille display. It drives the braille display, and provides complete screen review functionality. Some speech capability has also been incorporated.</p>
<h2>OPTIONS</h2>
<p> Options can be passed to <code>brltty</code> in a number of ways. From most to least influential, these are:</p>
<dl>
<dt>1.</dt>
<dd> Command Line Options</dd>
<dt>2.</dt>
<dd> Boot Parameters</dd>
<dt>3.</dt>
<dd> Environment Variables (if the <code>-E</code> (<code>&#8211;environment-variables</code>) option is in effect)</dd>
<dt>4.</dt>
<dd> The Configuration File</dd>
<dt>5.</dt>
<dd> Built-in Defaults</dd></dl>
<h3>Command Line Options</h3>
<p> The options are processed sequentially from left to right. If an option is specified more than once, or in case of a conflict, the rightmost specification takes precedence. </p>
<p> The following options are supported:</p>
<dl>
<dt><code>-a </code><i>table</i> (<code>&#8211;attributes-table=</code>)</dt>
<dd> The path to the attributes table. Relative paths are anchored at <code>/etc/brltty/Attributes</code>. The <code>.atb</code> extension is optional. The built-in default is <code>left_right.atb</code>.</dd>
<dt><code>-b </code><i>driver</i><code>,</code>&#8230;|<code>auto</code> (<code>&#8211;braille-driver=</code>)</dt>
<dd> The driver for the braille display (see Driver Specification). The built-in default is <code>auto</code>.</dd>
<dt><code>-c </code><i>table</i> (<code>&#8211;contraction-table=</code>)</dt>
<dd> The path to the contraction table. Relative paths are anchored at <code>/etc/brltty/Contraction</code>. The <code>.ctb</code> extension is optional.</dd>
<dt><code>-d </code><i>device</i><code>,</code>&#8230; (<code>&#8211;braille-device=</code>)</dt>
<dd> The device to which the braille display is connected. The built-in default is <code>usb:,bluetooth:</code>.</dd>
<dl>
<dt>
</dt><dd>
<p> The general form of a braille device specification is <i>qualifier</i><code>:</code><i>data</i>. For backward compatibility with earlier releases, if the qualifier is omitted then <code>serial:</code> is assumed. The following device types are supported:</p>
</dd><dl>
<dt><code>Bluetooth</code></dt>
<dd> For a bluetooth device, specify <code>bluetooth:</code><i>address</i>. The address must be six two-digit hexadecimal numbers separated by colons, e.g. <code>01:23:45:67:89:AB</code>.</dd>
<dt><code>Serial</code></dt>
<dd> For a serial device, specify <code>serial:</code><i>device</i>. The <code>serial:</code> qualifier is optional (for backward compatibility). If a relative path is given then it&#8217;s anchored at <code>/dev/</code> (the usual location where devices are defined on a Unix-like system). The following device specifications all refer to the primary serial device on Linux: <code>serial:ttyS0</code>, <code>serial:/dev/ttyS0</code>, <code>ttyS0</code>, <code>/dev/ttyS0</code>.</dd>
<dt><code>USB</code></dt>
<dd> For a USB device, specify <code>usb:</code>. <code>brltty</code> will search for the first USB device which matches the braille display driver being used. If this is inadequate, e.g. if you have more than one USB braille display which requires the same driver, then you can refine the device specification by appending the serial number of the display to it, e.g. <code>usb:12345</code>. N.B.: The &quot;identification by serial number&quot; feature doesn&#8217;t work for some models because some manufacturers either don&#8217;t set the USB serial number descriptor at all or do set it but not to a unique value.</dd></dl>
<p> A comma-delimited list of braille devices may be specified. If this is done then autodetection is performed on each listed device in sequence. This feature is particularly useful if you have a braille display with more than one interface, e.g. both a serial and a USB port.</dl>
<dt><code>-e</code> (<code>&#8211;standard-error</code>)</dt>
<dd> Write logs to standard error rather than to the system log (useful for debugging).</dd>
<dt><code>-f </code><i>file</i> (<code>&#8211;configuration-file=</code>)</dt>
<dd> The path to the configuration file. Relative paths are anchored at the current working directory. The built-in default is <code>/etc/brltty.conf</code>.</dd>
<dt><code>-h</code> (<code>&#8211;help</code>)</dt>
<dd> Print a command line usage summary (commonly used options only), and then exit.</dd>
<dt><code>-i </code><i>name</i> (<code>&#8211;speech-input=</code>)</dt>
<dd> The file system object (FIFO, named pipe, named socket, etc) which gives other applications access to <code>brltty</code>&#8216;s speech driver for text-to-speech conversion. It&#8217;s created at start-up and removed at termination. Relative paths are anchored at the current working directory. The built-in default is that the file system object is not created.</dd>
<dt><code>-k </code><i>table</i> (<code>&#8211;keyboard-table=</code>)</dt>
<dd> The path to the keyboard table. Relative paths are anchored at <code>/etc/brltty/Keyboard</code>. The <code>.ktb</code> extension is optional.</dd>
<dt><code>-l </code><i>level</i> (<code>&#8211;log-level=</code>)</dt>
<dd> The minimum severity level for messages written to the log. Any of the following numbers, or any abbreviation of their corresponding names, may be specified:</dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd> <code>emergency</code></dd>
<dt><code>1</code></dt>
<dd> <code>alert</code></dd>
<dt><code>2</code></dt>
<dd> <code>critical</code></dd>
<dt><code>3</code></dt>
<dd> <code>error</code></dd>
<dt><code>4</code></dt>
<dd> <code>warning</code></dd>
<dt><code>5</code></dt>
<dd> <code>notice</code></dd>
<dt><code>6</code></dt>
<dd> <code>information</code></dd>
<dt><code>7</code></dt>
<dd> <code>debug</code></dd></dl>
</dl>
</dl>
<p> The built-in default is <code>notice</code>.</p>
<dl>
<dt><code>-m </code><i>device</i> (<code>&#8211;midi-device=</code>)</dt>
<dd> The device to use for the Musical Instrument Digital Interface. For ALSA it&#8217;s <i>client</i><code>:</code><i>port</i>, where each may be either a number or a case-sensitive substring of its name. For other interfaces it&#8217;s the full path to an appropriate system device. The built-in default is:</dd>
<dl>
<dl>
<dt>Linux/ALSA</dt>
<dd> the first available MIDI output port</dd>
<dt>Linux/OSS</dt>
<dd> <code>/dev/sequencer</code></dd></dl>
</dl>
<dt><code>-n</code> (<code>&#8211;no-daemon</code>)</dt>
<dd> Remain in the foreground (useful for debugging).</dd>
<dt><code>-o </code><i>name</i><code>=</code><i>value</i><code>,</code>&#8230; (<code>&#8211;override-preference=</code>)</dt>
<dd> Override a preference setting. For the location of the preferences file, see the <code>-F</code> (<code>&#8211;preferences-file</code>) option.</dd>
<dt><code>-p </code><i>device</i> (<code>&#8211;pcm-device=</code>)</dt>
<dd> The device to use for digital audio. For ALSA it&#8217;s <i>name</i>[<code>:</code><i>argument</i><code>,</code>&#8230;]. For other interfaces it&#8217;s the full path to an appropriate system device. The built-in default is:</dd>
<dl>
<dl>
<dt>FreeBSD</dt>
<dd> <code>/dev/dsp</code></dd>
<dt>Linux/ALSA</dt>
<dd> <code>hw:0,0</code></dd>
<dt>Linux/OSS</dt>
<dd> <code>/dev/dsp</code></dd>
<dt>NetBSD</dt>
<dd> <code>/dev/audio</code></dd>
<dt>OpenBSD</dt>
<dd> <code>/dev/audio</code></dd>
<dt>Qnx</dt>
<dd> the preferred PCM output device</dd>
<dt>Solaris</dt>
<dd> <code>/dev/audio</code></dd></dl>
</dl>
<dt><code>-q</code> (<code>&#8211;quiet</code>)</dt>
<dd> Suppress the start-up messages. This is done by reducing the default log level (see the <code>-l</code> (<code>&#8211;log-level=</code>) option) to <code>warning</code> (<code>information</code> if either <code>-v</code> (<code>&#8211;verify</code>) or <code>-V</code> (<code>&#8211;version</code>) is also specified).</dd>
<dt><code>-r</code> (<code>&#8211;release-device</code>)</dt>
<dd> Release the device to which the braille display is connected when the current screen or window can&#8217;t be read.</dd>
<dt><code>-s </code><i>driver</i><code>,</code>&#8230;|<code>auto</code> (<code>&#8211;speech-driver=</code>)</dt>
<dd> The driver for the speech synthesizer (see Driver Specification). The built-in default is <code>auto</code>.</dd>
<dt><code>-t </code><i>table</i> (<code>&#8211;text-table=</code>)</dt>
<dd> The path to the text table. Relative paths are anchored at <code>/etc/brltty/Text</code>. The <code>.ttb</code> extension is optional. The built-in default is <code>en-nabcc.ttb</code> (the North American Braille Computer Code).</dd>
<dt><code>-v</code> (<code>&#8211;verify</code>)</dt>
<dd> Print the start-up messages and then exit. This always includes the versions of <code>brltty</code> itself, the server side of its application programming interface, and each of the selected braille and speech drivers. If the <code>-q</code> (<code>&#8211;quiet</code>) option isn&#8217;t also specified then it also includes the values of the options after all sources have been considered. If more than one braille driver and/or more than one braille device has been specified then braille display autodetection is performed. If more than one speech driver has been specified then speech synthesizer autodetection is performed.</dd>
<dt><code>-x </code><i>driver</i> (<code>&#8211;screen-driver=</code>)</dt>
<dd> The screen driver. The built-in default is operating system appropriate.</dd>
<dt><code>-A </code><i>name</i><code>=</code><i>value</i><code>,</code>&#8230; (<code>&#8211;api-parameters=</code>)</dt>
<dd> Parameters for the application programming interface. If the same parameter is specified more than once then the rightmost specification is used. Parameter names may be abbreviated.</dd>
<dt><code>-B </code>[<i>driver</i><code>:</code>]<i>name</i><code>=</code><i>value</i><code>,</code>&#8230; (<code>&#8211;braille-parameters=</code>)</dt>
<dd> Parameters for the braille display driver. If the same parameter is specified more than once then the rightmost specification is used. Parameter names may be abbreviated. If a parameter assignment is qualified with a driver identification code then it&#8217;s only processed if that braille display driver is being used.</dd>
<dt><code>-D </code><i>directory</i> (<code>&#8211;drivers-directory=</code>)</dt>
<dd> The path to the directory which contains the dynamically loadable driver objects. The built-in default is /lib/brltty<code>.</code></dd>
<dt><code>-E</code> (<code>&#8211;environment-variables</code>)</dt>
<dd> Recognize environment variables.</dd>
<dt><code>-F </code><i>file</i> (<code>&#8211;preferences-file=</code>)</dt>
<dd> The path to the preferences file. Relative paths are anchored at <code>/var/lib/brltty</code>. The built-in default is <code>brltty.prefs</code>.</dd>
<dt><code>-H</code> (<code>&#8211;full-help</code>)</dt>
<dd> Print a command line usage summary (all options), and then exit.</dd>
<dt><code>-I</code> (<code>&#8211;install-service</code>)</dt>
<dd> (Windows only) Install <code>brltty</code> as the <code>BrlAPI</code> service so that it will be automatically started when the system is booted, and so that applications can know that a <code>BrlAPI</code> server is running.</dd>
<dt><code>-K </code><i>arg</i> (<code>&#8211;keyboard-properties=</code>)</dt>
<dd> Properties of the keyboard.</dd>
<dt><code>-L </code><i>file</i> (<code>&#8211;log-file=</code>)</dt>
<dd> The file to which log messages are written. Relative paths are anchored at the current working directory. The default is to send log messages to the system log.</dd>
<dt><code>-M </code><i>csecs</i> (<code>&#8211;message-delay=</code>)</dt>
<dd> The message hold time in hundredths of a second. The built-in default is <code>400</code> (4 seconds).</dd>
<dt><code>-N</code> (<code>&#8211;no-api</code>)</dt>
<dd> Don&#8217;t start the application programming interface.</dd>
<dt><code>-P </code><i>file</i> (<code>&#8211;pid-file=</code>)</dt>
<dd> The full path to the process identifier file. If this option is supplied, <code>brltty</code> writes its process identifier (pid) into the specified file at start-up. The file is removed when <code>brltty</code> terminates.</dd>
<dt><code>-R</code> (<code>&#8211;remove-service</code>)</dt>
<dd> (Windows only) Remove the <code>BrlAPI</code> service so that <code>brltty</code> will not be automatically started when the system is booted, and so that applications can know that no <code>BrlAPI</code> server is running.</dd>
<dt><code>-S </code>[<i>driver</i><code>:</code>]<i>name</i><code>=</code><i>value</i><code>,</code>&#8230; (<code>&#8211;speech-parameters=</code>)</dt>
<dd> Parameters for the speech synthesizer driver. If the same parameter is specified more than once then the rightmost specification is used. Parameter names may be abbreviated. If a parameter assignment is qualified with a driver identification code then it&#8217;s only processed if that speech synthesizer driver is being used.</dd>
<dt><code>-T </code><i>directory</i> (<code>&#8211;tables-directory=</code>)</dt>
<dd> The path to the directory which contains the text, contraction, attributes, keyboard, and input tables. The built-in default is /etc/brltty<code>.</code></dd>
<dt><code>-U </code><i>directory</i> (<code>&#8211;updatable-directory=</code>)</dt>
<dd> The path to a directory which contains files that can be updated. The built-in default is /var/lib/brltty<code>.</code></dd>
<dt><code>-V</code> (<code>&#8211;version</code>)</dt>
<dd> Print the versions of <code>brltty</code> itself, the server side of its application programming interface, and those drivers which were configured in at build-time, and then exit. If the <code>-q</code> (<code>&#8211;quiet</code>) option isn&#8217;t also specified then also print copyright information.</dd>
<dt><code>-W </code><i>directory</i> (<code>&#8211;writable-directory=</code>)</dt>
<dd> The path to a directory which can be written to. The built-in default is /run/brltty<code>.</code></dd>
<dt><code>-X </code><i>name</i><code>=</code><i>value</i><code>,</code>&#8230; (<code>&#8211;screen-parameters=</code>)</dt>
<dd> Parameters for the screen driver. If the same parameter is specified more than once then the rightmost specification is used. Parameter names may be abbreviated.</dd>
<dt><code>-Y </code><i>text</i> (<code>&#8211;start-message=</code>)</dt>
<dd> The text to be shown when the braille driver starts and to be spoken when the speech driver starts. The built-in default is BRLTTY 6.4<code>.</code></dd>
<dt><code>-Z </code><i>text</i> (<code>&#8211;stop-message=</code>)</dt>
<dd> The text to be shown when the braille driver stops. The built-in default is BRLTTY stopped<code>.</code></dd></dl>
<h3>Environment Variables</h3>
<p> The following environment variables are recognized if the <code>-E</code> (<code>&#8211;environment-variables</code>) option is specified:</p>
<dl>
<dt><code>BRLTTY_API_PARAMETERS=</code><i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</dt>
<dd> Parameters for the application programming interface. See the <code>-A</code> (<code>&#8211;api-parameters=</code>) option for details.</dd>
<dt><code>BRLTTY_ATTRIBUTES_TABLE=</code><i>table</i></dt>
<dd> The attributes table. See the <code>-a</code> (<code>&#8211;attributes-table=</code>) option for details.</dd>
<dt><code>BRLTTY_BRAILLE_DEVICE=</code><i>device</i><code>,</code>&#8230;</dt>
<dd> The device to which the braille display is connected. See the <code>-d</code> (<code>&#8211;braille-device=</code>) option for details.</dd>
<dt><code>BRLTTY_BRAILLE_DRIVER=</code><i>driver</i><code>,</code>&#8230;|<code>auto</code></dt>
<dd> The driver for the braille display. See the <code>-b</code> (<code>&#8211;braille-driver=</code>) option for details.</dd>
<dt><code>BRLTTY_BRAILLE_PARAMETERS=</code>[<i>driver</i><code>:</code>]<i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</dt>
<dd> Parameters for the braille display driver. See the <code>-B</code> (<code>&#8211;braille-parameters=</code>) option for details.</dd>
<dt><code>BRLTTY_CONFIGURATION_FILE=</code><i>file</i></dt>
<dd> The configuration file. See the <code>-f</code> (<code>&#8211;configuration-file=</code>) option for details.</dd>
<dt><code>BRLTTY_CONTRACTION_TABLE=</code><i>table</i></dt>
<dd> The contraction table. See the <code>-c</code> (<code>&#8211;contraction-table=</code>) option for details.</dd>
<dt><code>BRLTTY_MIDI_DEVICE=</code><i>device</i></dt>
<dd> The device to use for the Musical Instrument Digital Interface. See the <code>-m</code> (<code>&#8211;midi-device=</code>) option for details.</dd>
<dt><code>BRLTTY_PCM_DEVICE=</code><i>device</i></dt>
<dd> The device to use for digital audio. See the <code>-p</code> (<code>&#8211;pcm-device=</code>) option for details.</dd>
<dt><code>BRLTTY_PREFERENCES_FILE=</code><i>file</i></dt>
<dd> The preferences file. See the <code>-F</code> (<code>&#8211;preferences-file=</code>) option for details.</dd>
<dt><code>BRLTTY_RELEASE_DEVICE=on</code>|<code>off</code></dt>
<dd> Release the device to which the braille display is connected when the current screen or window can&#8217;t be read. See the <code>-r</code> (<code>&#8211;release-device</code>) option for details.</dd>
<dt><code>BRLTTY_SCREEN_DRIVER=</code><i>driver</i></dt>
<dd> The screen driver. See the <code>-x</code> (<code>&#8211;screen-driver=</code>) option for details.</dd>
<dt><code>BRLTTY_SCREEN_PARAMETERS=</code><i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</dt>
<dd> Parameters for the screen driver. See the <code>-X</code> (<code>&#8211;screen-parameters=</code>) option for details.</dd>
<dt><code>BRLTTY_SPEECH_DRIVER=</code><i>driver</i><code>,</code>&#8230;|<code>auto</code></dt>
<dd> The driver for the speech synthesizer. See the <code>-s</code> (<code>&#8211;speech-driver=</code>) option for details.</dd>
<dt><code>BRLTTY_SPEECH_INPUT=</code><i>name</i></dt>
<dd> The file system object which gives other applications access to <code>brltty</code>&#8216;s speech driver for text-to-speech conversion. See the <code>-i</code> (<code>&#8211;speech-input=</code>) option for details.</dd>
<dt><code>BRLTTY_SPEECH_PARAMETERS=</code>[<i>driver</i><code>:</code>]<i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</dt>
<dd> Parameters for the speech synthesizer driver. See the <code>-S</code> (<code>&#8211;speech-parameters=</code>) option for details.</dd>
<dt><code>BRLTTY_TEXT_TABLE=</code><i>table</i></dt>
<dd> The text table. See the <code>-t</code> (<code>&#8211;text-table=</code>) option for details.</dd></dl>
<h3>The Configuration File</h3>
<p> Blank lines are ignored. If the character <code>#</code> occurs on any line then all characters from it to the end of that line are treated as a comment. </p>
<p> The following configuration directives are supported:</p>
<dl>
<dt><code>api-parameters </code><i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</dt>
<dd> Parameters for the application programming interface. See the <code>-A</code> (<code>&#8211;api-parameters=</code>) option for details.</dd>
<dt><code>attributes-table </code><i>table</i></dt>
<dd> The attributes table. See the <code>-a</code> (<code>&#8211;attributes-table=</code>) option for details.</dd>
<dt><code>braille-device </code><i>device</i><code>,</code>&#8230;</dt>
<dd> The device to which the braille display is connected. See the <code>-d</code> (<code>&#8211;braille-device=</code>) option for details.</dd>
<dt><code>braille-driver </code><i>driver</i><code>,</code>&#8230;|<code>auto</code></dt>
<dd> The driver for the braille display. See the <code>-b</code> (<code>&#8211;braille-driver=</code>) option for details.</dd>
<dt><code>braille-parameters </code>[<i>driver</i><code>:</code>]<i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</dt>
<dd> Parameters for the braille display driver. See the <code>-B</code> (<code>&#8211;braille-parameters=</code>) option for details.</dd>
<dt><code>contraction-table </code><i>table</i></dt>
<dd> The contraction table. See the <code>-c</code> (<code>&#8211;contraction-table=</code>) option for details.</dd>
<dt><code>midi-device </code><i>device</i></dt>
<dd> The device to use for the Musical Instrument Digital Interface. See the <code>-m</code> (<code>&#8211;midi-device=</code>) option for details.</dd>
<dt><code>pcm-device </code><i>device</i></dt>
<dd> The device to use for digital audio. See the <code>-p</code> (<code>&#8211;pcm-device=</code>) option for details.</dd>
<dt><code>preferences-file </code><i>file</i></dt>
<dd> The preferences file. See the <code>-F</code> (<code>&#8211;preferences-file=</code>) option for details.</dd>
<dt><code>release-device on</code>|<code>off</code></dt>
<dd> Release the device to which the braille display is connected when the current screen or window can&#8217;t be read. See the <code>-r</code> (<code>&#8211;release-device</code>) option for details.</dd>
<dt><code>screen-driver </code><i>driver</i></dt>
<dd> The screen driver. See the <code>-x</code> (<code>&#8211;screen-driver=</code>) option for details.</dd>
<dt><code>screen-parameters </code><i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</dt>
<dd> Parameters for the screen driver. See the <code>-X</code> (<code>&#8211;screen-parameters=</code>) option for details.</dd>
<dt><code>speech-driver </code><i>driver</i><code>,</code>&#8230;|<code>auto</code></dt>
<dd> The driver for the speech synthesizer. See the <code>-s</code> (<code>&#8211;speech-driver=</code>) option for details.</dd>
<dt><code>speech-input me</code></dt>
<dd> The file system object which gives other applications access to <code>brltty</code>&#8216;s speech driver for text-to-speech conversion. See the <code>-i</code> (<code>&#8211;speech-input=</code>) option for details.</dd>
<dt><code>speech-parameters </code>[<i>driver</i><code>:</code>]<i>name</i><code>=</code><i>value</i><code>,</code>&#8230;</dt>
<dd> Parameters for the speech synthesizer driver. See the <code>-S</code> (<code>&#8211;speech-parameters=</code>) option for details.</dd>
<dt><code>text-table </code><i>table</i></dt>
<dd> The text table. See the <code>-t</code> (<code>&#8211;text-table=</code>) option for details.</dd></dl>
<h3>Driver Specification</h3>
<p> A braille display or speech synthesizer driver must be specified via its identification code:</p>
<dl>
<dl>
<dt><code>al</code></dt>
<dd> Alva</dd>
<dt><code>an</code></dt>
<dd> Android</dd>
<dt><code>at</code></dt>
<dd> Albatross</dd>
<dt><code>ba</code></dt>
<dd> BrlAPI</dd>
<dt><code>bc</code></dt>
<dd> BrailComm</dd>
<dt><code>bd</code></dt>
<dd> Braudi</dd>
<dt><code>bl</code></dt>
<dd> BrailleLite</dd>
<dt><code>bm</code></dt>
<dd> Baum</dd>
<dt><code>bn</code></dt>
<dd> BrailleNote</dd>
<dt><code>cb</code></dt>
<dd> CombiBraille</dd>
<dt><code>ce</code></dt>
<dd> Cebra</dd>
<dt><code>cn</code></dt>
<dd> Canute</dd>
<dt><code>ec</code></dt>
<dd> EcoBraille</dd>
<dt><code>en</code></dt>
<dd> eSpeak-NG</dd>
<dt><code>es</code></dt>
<dd> eSpeak</dd>
<dt><code>eu</code></dt>
<dd> EuroBraille</dd>
<dt><code>fa</code></dt>
<dd> FrankAudiodata</dd>
<dt><code>fl</code></dt>
<dd> FestivalLite</dd>
<dt><code>fs</code></dt>
<dd> FreedomScientific</dd>
<dt><code>fv</code></dt>
<dd> Festival</dd>
<dt><code>gs</code></dt>
<dd> GenericSay</dd>
<dt><code>hd</code></dt>
<dd> Hedo</dd>
<dt><code>hm</code></dt>
<dd> HIMS</dd>
<dt><code>ht</code></dt>
<dd> HandyTech</dd>
<dt><code>hw</code></dt>
<dd> HumanWare</dd>
<dt><code>ir</code></dt>
<dd> Iris</dd>
<dt><code>ic</code></dt>
<dd> Inceptor</dd>
<dt><code>lb</code></dt>
<dd> Libbraille</dd>
<dt><code>lt</code></dt>
<dd> LogText</dd>
<dt><code>mb</code></dt>
<dd> MultiBraille</dd>
<dt><code>md</code></dt>
<dd> MDV</dd>
<dt><code>mm</code></dt>
<dd> BrailleMemo</dd>
<dt><code>mn</code></dt>
<dd> MiniBraille</dd>
<dt><code>mp</code></dt>
<dd> Mikropuhe</dd>
<dt><code>mt</code></dt>
<dd> Metec</dd>
<dt><code>no</code></dt>
<dd> no driver</dd>
<dt><code>np</code></dt>
<dd> NinePoint</dd>
<dt><code>pg</code></dt>
<dd> Pegasus</dd>
<dt><code>pm</code></dt>
<dd> Papenmeier</dd>
<dt><code>sd</code></dt>
<dd> SpeechDispatcher</dd>
<dt><code>sk</code></dt>
<dd> Seika</dd>
<dt><code>sw</code></dt>
<dd> Swift</dd>
<dt><code>th</code></dt>
<dd> Theta</dd>
<dt><code>tn</code></dt>
<dd> TechniBraille Systems Inc.</dd>
<dt><code>ts</code></dt>
<dd> Telesensory Systems Inc.</dd>
<dt><code>vd</code></dt>
<dd> VideoBraille</dd>
<dt><code>vo</code></dt>
<dd> Voyager, Part232 (serial adapter), BraillePen/EasyLink</dd>
<dt><code>vs</code></dt>
<dd> VisioBraille</dd>
<dt><code>vv</code></dt>
<dd> ViaVoice</dd>
<dt><code>xs</code></dt>
<dd> ExternalSpeech</dd></dl>
<p> A comma-delimited list of drivers may be specified. If this is done then autodetection is performed using each listed driver in sequence. You may need to experiment in order to determine the most reliable order since some drivers autodetect better than others. </p>
<p> If the single word <code>auto</code> is specified then autodetection is performed using only those drivers which are known to be reliable for this purpose.</dl>
<h2>SEE ALSO</h2>
<p> For full documentation, see <code>brltty</code>&#8216;s on-line manual at [<code><a rel="nofollow" href="http://brltty.app/documentation.html">http://brltty.app/documentation.html</a></code>]. </p>
