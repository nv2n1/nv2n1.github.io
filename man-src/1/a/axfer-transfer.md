---
title: "axfer-transfer(1)"
name: "axfer-transfer"
section: "1"
letter: "a"
url: "/docs/linux/man/1-axfer-transfer/"
description: "axfer-transfer – transferrer of audio data frame for sound devices and nodes."
---

<h2 class="name">NAME</h2>
<p> axfer-transfer &#8211; transferrer of audio data frame for sound devices and nodes.</p>
<h2>SYNOPSIS</h2>
<p> <code>axfer transfer</code> <i>direction</i> [ <i>common-options</i> ] [ <i>backend-options</i> ] [ <i>filepath</i> ] </p>
<p> <code>axfer transfer</code> <i>direction</i> [ <i>common-options</i> ] [ <i>backend-options</i> ] <i>-I</i> | <i>&#8211;separate-channels filepath &#8230;</i> </p>
<p> direction = <code>capture</code> | <code>playback</code> </p>
<p> common-options = ( read <i>OPTIONS</i> section ) </p>
<p> backend-options = ( read <i>OPTIONS</i> section ) </p>
<p> filepaths = ( read <i>OPTIONS</i> section ) </p>
<h2>DESCRIPTION</h2>
<p> The <code>transfer</code> subcommand of <code>axfer</code> performs transmission of audio data frames for devices available in supported backends. This program is essentially designed to use alsa-lib APIs (libasound backend) to handle sound devices supported by Linux sound subsystem (ALSA). </p>
<h2>OPTIONS</h2>
<h3>Direction</h3>
<dl>
<dt><code>capture</code></p>
<dd> Operates for capture transmission. </p>
<dt><code>playback</code></p>
<dd> Operates for playback transmission. </p>
</dl>
<h3>Filepath</h3>
<p> Filepath is handled as a path relative to current working directory of run time if it&#8217;s not full path from root directory. </p>
<p> The standard input or output is used if filepath is not specified or given as <i>&#8216;-&#8216;</i> . </p>
<p> For playback transmission, container format of given <i>filepath</i> is detected automatically and metadata is used for parameters of sample format, channels, rate, duration. If nothing detected, content of given file path is handled as raw data. In this case, the parameters should be indicated as options. </p>
<p> Multiple <i>filepaths</i> are allowed with <i>-I</i> | <i>&#8211;separate-channels</i> option. In this case, standard input and output is not available. The same <i>filepath</i> is not allowed except for paths listed below:<br />
&nbsp;&#8211;&nbsp;/dev/null<br />
&nbsp;&#8211;&nbsp;/dev/zero<br />
&nbsp;&#8211;&nbsp;/dev/full<br />
&nbsp;&#8211;&nbsp;/dev/random<br />
&nbsp;&#8211;&nbsp;/dev/urandom </p>
<h3>Common options</h3>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print help messages and finish run time. </p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Quiet mode. Suppress messages (not sound :)) </p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Verbose mode. Runtime dumps supplemental information according to the number of this option given in command line. </p>
<dt><code>-d, &#8211;duration=#</code></p>
<dd> Interrupt after # seconds. A value of zero means infinity. The default is zero, so if this option is omitted then the transmission process will run until it is killed. Either <i>-d</i> or <i>-s</i> option is available exclusively. </p>
<dt><code>-s, &#8211;samples=#</code></p>
<dd> Interrupt after transmission of # number of data frames. A value of zero means infinity. The default is zero, so if this options is omitted then the transmission process will run until it is killed. Either <i>-d</i> or <i>-s</i> option is available exclusively. </p>
<dt><code>-f, &#8211;format=FORMAT</code></p>
<dd> Indicate format of audio sample. This is required for capture transmission, or playback transmission with files including raw audio data. </p>
<p> Available sample format is listed below:<br />
&nbsp;&#8211;&nbsp;[S8|U8|S16|U16|S32|U32][_LE|_BE]<br />
&nbsp;&#8211;&nbsp;[S24|U24][_LE|_BE]<br />
&nbsp;&#8211; FLOAT[_LE|_BE]<br />
&nbsp;&#8211; FLOAT64[_LE|_BE]<br />
&nbsp;&#8211; IEC958_SUBFRAME[_LE|_BE]<br />
&nbsp;&#8211; MU_LAW<br />
&nbsp;&#8211; A_LAW<br />
&nbsp;&#8211;&nbsp;[S20|U20][_LE|_BE]<br />
&nbsp;&#8211;&nbsp;[S24|U24][_3LE|_3BE]<br />
&nbsp;&#8211;&nbsp;[S20|U20][_3LE|_3BE]<br />
&nbsp;&#8211;&nbsp;[S18|U18][_3LE|_3BE]<br />
&nbsp;&#8211; DSD_U8<br />
&nbsp;&#8211; DSD_[U16|U32][_LE|_BE] </p>
<p> If endian-ness is omitted, host endian-ness is used. </p>
<p> Some special formats are available:<br />
&nbsp;&#8211; cd&nbsp;(16 bit little endian, 44100, stereo)&nbsp;[=&nbsp;-f S16_LE -c 2 -r 44100]<br />
&nbsp;&#8211; cdr&nbsp;(16 bit big endian, 44100, stereo)&nbsp;[=&nbsp;-f S16_BE -c 2 -f 44100]<br />
&nbsp;&#8211; dat&nbsp;(16 bit little endian, 48000, stereo)&nbsp;[=&nbsp;-f S16_LE -c 2 -r 48000] </p>
<p> If omitted, <i>U8</i> is used as a default. Actual available formats are restricted by each transmission backend. </p>
<p> Unavailable sample format is listed below. These format has size of data frame unaligned to byte unit. </p>
<p>&nbsp;&#8211; IMA_ADPCM<br />
&nbsp;&#8211; MPEG<br />
&nbsp;&#8211; GSM<br />
&nbsp;&#8211; SPECIAL<br />
&nbsp;&#8211; G723_24<br />
&nbsp;&#8211; G723_24_1B<br />
&nbsp;&#8211; G723_40<br />
&nbsp;&#8211; G723_40_1B </p>
<dt><code>-c, &#8211;channels=#</code></p>
<dd> Indicate the number of audio data samples per frame. This is required for capture transmission, or playback transmission with files including raw audio data. The value should be between <i>1 to</i> <i>256</i> . If omitted, <i>1</i> is used as a default. </p>
<dt><code>-r, &#8211;rate=#</code></p>
<dd> Indicate the number of audio data frame per second. This is required for capture transmission, or playback transmission with files including raw audio data. If the value is less than <i>1000</i> , it&#8217;s interpreted by <i>kHz</i> unit. The value should be between <i>2000</i> and <i>192000</i> . If omitted, <i>8000</i> is used as a default. </p>
<dt><code>-t, &#8211;file-type=TYPE</code></p>
<dd> Indicate the type of file. This is required for capture transmission. Available types are listed below:<br />
&nbsp;&#8211; wav: Microsoft/IBM RIFF/Wave format<br />
&nbsp;&#8211; au, sparc: Sparc AU format<br />
&nbsp;&#8211; voc: Creative Tech. voice format<br />
&nbsp;&#8211; raw: raw data </p>
<p> When nothing is indicated, for capture transmission, the type is decided according to suffix of <i>filepath</i> , and <i>raw</i> type is used for fallback. </p>
<dt><code>-I, &#8211;separate-channels</code></p>
<dd> Indicate this option when several files are going to be handled. For capture transmission, if one filepath is given as <i>filepath</i> , a list of <i>filepaths</i> is generated in a formula &#8216;&lt;filepath&gt;-&lt;sequential number&gt;[.suffix]&#8217;. The suffix is omitted when raw format of container is used. </p>
<dt><code>&#8211;dump-hw-params</code></p>
<dd> Dump hardware parameters and finish run time if backend supports it. </p>
<dt><code>&#8211;xfer-backend=BACKEND</code></p>
<dd> Select backend of transmission from a list below. The default is libasound. </p>
<p>&nbsp;&#8211; libasound<br />
&nbsp;&#8211; libffado&nbsp;(optional if compiled) </p>
</dl>
<h3>Backend options for libasound</h3>
<dl>
<dt><code>-D, &#8211;device=NODE</code></p>
<dd>
<p> This option is used to select PCM node in libasound configuration space. Available nodes are listed by <i>pcm</i> operation of <i>list</i> subcommand. </p>
<dt><code>-N, &#8211;nonblock</code></p>
<dd>
<p> With this option, PCM substream is opened in non-blocking mode. When audio data frame is not available in buffer of the PCM substream, I/O operation immediately returns without blocking process. This option implicitly uses <i>&#8211;waiter-type</i> option as well to prevent heavy consumption of CPU time. </p>
<dt><code>-M, &#8211;mmap</code></p>
<dd>
<p> With this option, audio data frame is processed directly in buffer of PCM substream if selected node supports this operation. Without the option, temporary buffers are used to copy audio data frame for buffer of PCM substream. This option implicitly uses <i>&#8211;waiter-type</i> option as well to prevent heavy consumption of CPU time. </p>
<dt><code>-F, &#8211;period-size=#</code></p>
<dd>
<p> This option configures given value to <i>period_size</i> hardware parameter of PCM substream. The parameter indicates the number of audio data frame per period in buffer of the PCM substream. Actual number is decided as a result of interaction between each implementation of PCM plugin chained from the selected PCM node, and in-kernel driver or PCM I/O plugins. </p>
<p> Ideally, the same amount of audio data frame as the value should be handled in one I/O operation. Actually, it is not, depending on implementation of the PCM plugins, in-kernel driver, PCM I/O plugins and scheduling model. For &#8216;hw&#8217; PCM plugin in &#8216;irq&#8217; scheduling model, the value is used to decide intervals of hardware interrupt, thus the same amount of audio data frame as the value is expected to be available for one I/O operation. </p>
<dt><code>&#8211;period-time=#</code></p>
<dd>
<p> This option configures given value to <i>period_time</i> hardware parameter of PCM substream. This option is similar to <i>&#8211;period-size</i> option, however its unit is micro-second. </p>
<dt><code>-B, &#8211;buffer-size=#</code></p>
<dd>
<p> This option configures given value to <i>buffer_size</i> hardware parameter of PCM substream. The parameter indicates the number of audio data frame in buffer of PCM substream. Actual number is decided as a result of interaction between each implementation of PCM plugin chained from the selected PCM node, and in-kernel driver or PCM I/O plugins. </p>
<p> Ideally, this is multiples of the number of audio data frame per period, thus the size of period. Actually, it is not, depending on implementation of the PCM plugins, in-kernel driver and PCM I/O plugins. </p>
<dt><code>&#8211;buffer-time=#</code></p>
<dd>
<p> This option configures given value to <i>buffer_time</i> hardware parameter of PCM substream. This option is similar to <i>&#8211;buffer-size</i> option, however its unit is micro-second. </p>
<dt><code>&#8211;waiter-type=TYPE</code></p>
<dd>
<p> This option indicates the type of waiter for event notification. At present, four types are available; <i>default</i> , <i>select</i> , <i>poll</i> and <i>epoll</i> . With <i>default</i> type, &#8216;snd_pcm_wait()&#8217; is used. With <i>select</i> type, &#8216;<a href="/docs/linux/man/2-select/">select</a>(2)&#8217; system call is used. With <i>poll</i> type, &#8216;<a href="/docs/linux/man/2-poll/">poll</a>(2)&#8217; system call is used. With <i>epoll</i> type, Linux-specific &#8216;<a href="/docs/linux/man/7-epoll/">epoll</a>(7)&#8217; system call is used. </p>
<p> This option should correspond to one of <i>&#8211;nonblock</i> or <i>&#8211;mmap</i> options, or <i>timer</i> value of <i>&#8211;sched-model</i> option. Neither this option nor <i>&#8211;test-nowait</i> is available at the same time. </p>
<dt><code>&#8211;sched-model=MODEL</code></p>
<dd>
<p> This option selects scheduling model for process of this program. One of <i>irq</i> or <i>timer</i> is available. In detail, please read &#8216;SCHEDULING MODEL&#8217; section. </p>
<p> When nothing specified, <i>irq</i> model is used. </p>
<dt><code>-A, &#8211;avail-min=#</code></p>
<dd>
<p> This option configures given value to <i>avail-min</i> software parameter of PCM substream. In blocking mode, the value is used as threshold of the number of available audio data frames in buffer of PCM substream to wake up process blocked by I/O operation. In non-blocking mode, any I/O operation returns -EAGAIN until the available number of audio data frame reaches the threshold. </p>
<p> This option has an effect in cases neither <i>&#8211;mmap</i> nor <i>timer</i> value of <i>&#8211;sched-model</i> option is used. </p>
<dt><code>-R, &#8211;start-delay=#</code></p>
<dd>
<p> This option configures given value to <i>start_threshold</i> software parameter of PCM substream. The value is used as threshold to start PCM substream automatically. At present, this option has an effect in cases neither <i>&#8211;mmap</i> nor <i>timer</i> value of <i>&#8211;sched-model</i> option is used. </p>
<p> For playback transmission, when the number of accumulated audio data frame in buffer of PCM substream to which this program writes out reaches the threshold, the PCM substream starts automatically without an explicit call of <i>snd_pcm_start()</i> to the PCM substream. </p>
<p> For capture transmission, this option is useless. The number of accumulated audio data frame is not increased without an explicit call of <i>snd_pcm_start()</i> to the PCM substream. </p>
<p> This option has an effect in cases neither <i>&#8211;mmap</i> nor <i>timer</i> value of <i>&#8211;sched-model</i> option is used. </p>
<dt><code>-T, &#8211;stop-delay=#</code></p>
<dd>
<p> This option configures given value to <i>stop_threshold</i> software parameter of PCM substream. The value is used as threshold to stop PCM substream automatically. At present, this option has an effect in cases neither <i>&#8211;mmap</i> nor <i>timer</i> value of <i>&#8211;sched-model</i> option is used. </p>
<p> For capture transmission, when the number of accumulated audio data frame in buffer of PCM substream to which a driver or alsa-lib PCM plugins write reaches the threshold, the PCM substream stops automatically without an explicit call of <i>snd_pcm_stop()</i> to the PCM substream. This is a case that this program leaves the audio data frames without reading for a while. </p>
<p> For playback transmission, when the number available audio data frame in buffer of PCM substream from which a driver or alsa-lib PCM plugins read reaches the threshold, the PCM substream stops automatically without an explicit call of <i>snd_pcm_stop()</i> to the PCM substream. This is a case that this program leaves the audio data frames without writing for a while. </p>
<p> This option has an effect in cases neither <i>&#8211;mmap</i> nor <i>timer</i> value of <i>&#8211;sched-model</i> option is used. </p>
<dt><code>&#8211;disable-resample</code></p>
<dd>
<p> This option has an effect for &#8216;plug&#8217; plugin in alsa-lib to suppress conversion of sampling rate for audio data frame. </p>
<dt><code>&#8211;disable-channels</code></p>
<dd>
<p> This option has an effect for &#8216;plug&#8217; plugin in alsa-lib to suppress conversion of channels for audio data frame. </p>
<dt><code>&#8211;disable-format</code></p>
<dd>
<p> This option has an effect for &#8216;plug&#8217; plugin in alsa-lib to suppress conversion of sample format for audio data frame. </p>
<dt><code>&#8211;disable-softvol</code></p>
<dd>
<p> This option has an effect for &#8216;softvol&#8217; plugin in alsa-lib to suppress conversion of samples for audio data frame via additional control element. </p>
<dt><code>&#8211;fatal-errors</code></p>
<dd>
<p> This option suppresses recovery operation from XRUN state of running PCM substream, then process of this program is going to finish as usual. </p>
<dt><code>&#8211;test-nowait</code></p>
<dd>
<p> This option disables any waiter for I/O event notification. I/O operations are iterated till any of audio data frame is available. The option brings heavy load in consumption of CPU time. </p>
</dl>
<h3>Backend options for libffado</h3>
<p> This backend is automatically available when configure script detects <i>ffado_streaming_init()</i> symbol in libffado shared object. </p>
<dl>
<dt><code>-p, &#8211;port=#</code></p>
<dd>
<p> This option uses given value to decide which 1394 OHCI controller is used to communicate. When Linux system has two 1394 OHCI controllers, <i>0</i> or <i>1</i> are available. Neither this option nor <i>-g</i> is available at the same time. If nothing specified, libffado performs to communicate to units on IEEE 1394 bus managed by all of 1394 OHCI controller available in Linux system. </p>
<dt><code>-n, &#8211;node=#</code></p>
<dd>
<p> This option uses given value to decide which unit is used to communicate. This option requires <i>-p</i> option to indicate which 1394 OHCI controller is used to communicate to the specified unit. </p>
<dt><code>-g, &#8211;guid=HEXADECIMAL</code></p>
<dd>
<p> This option uses given value to decide a target unit to communicate. The value should be prefixed with &#8216;0x&#8217; and consists of hexadecimal literal letters (0-9, a-f, A-F). Neither this option nor <i>-p</i> is available at the same time. If nothing specified, libffado performs to communicate to units on IEEE 1394 bus managed by all of 1394 OHCI controller available in Linux system. </p>
<dt><code>&#8211;frames-per-period=#</code></p>
<dd>
<p> This option uses given value to decide the number of audio data frame in one read/write operation. The operation is blocked till the number of available audio data frame exceeds the given value. As a default, 512 audio data frames is used. </p>
<dt><code>&#8211;periods-per-buffer=#</code></p>
<dd>
<p> This option uses given value to decide the size of intermediate buffer between this program and libffado. As a default, 2 periods per buffer is used. </p>
<dt><code>&#8211;slave</code></p>
<dd>
<p> This option allows this program to run slave mode. In this mode, libffado adds unit directory into configuration ROM of 1394 OHCI controller where Linux system runs. The unit directory can be found by the other node on the same bus. Linux system running on the node can transfer isochronous packet with audio data frame to the unit. This program can receive the packet and demultiplex the audio data frame. </p>
<dt><code>&#8211;snoop</code></p>
<dd>
<p> This option allows this program to run snoop mode. In this mode, libffado listens isochronous channels to which device transfers isochronous packet. When isochronous communication starts by any unit on the same bus, the packets can be handled by this program. </p>
<dt><code>&#8211;sched-priority=#</code></p>
<dd>
<p> This option executes <i>pthread_setschedparam()</i> in a call of <i>ffado_streaming_init()</i> to configure scheduling policy and given value as its priority for threads related to isochronous communication. The given value should be within <i>RLIMIT_RTPRIO</i> parameter of process. Please read <i><a href="/docs/linux/man/2-getrlimit/">getrlimit</a>(2)</i> for details. </p>
</dl>
<h2>POSIX SIGNALS</h2>
<p> During transmission, <i>SIGINT</i> and <i>SIGTERM</i> will close handled files and PCM substream to be going to finish run time. </p>
<p> <i>SIGTSTP</i> will suspend PCM substream and <i>SIGCONT</i> will resume it. No XRUNs are expected. With libffado backend, the suspend/resume is not supported and runtime is aboeted immediately. </p>
<p> The other signals perform default behaviours. </p>
<h2>EXAMPLES</h2>
<p> <code>$ axfer transfer playback -d 1 something</code> </p>
<p> The above will transfer audio data frame in &#8216;something&#8217; file for playback during 1 second. The sample format is detected automatically as a result to parse &#8216;something&#8217; as long as it&#8217;s compliant to one of Microsoft/IBM RIFF/Wave, Sparc AU, Creative Tech. voice formats. If nothing detected, <i>-r</i> , <i>-c</i> and <i>-f</i> should be given, or <i>-f</i> should be given with special format. </p>
<p> <code>$ axfer transfer playback -r 22050 -c 1 -f S16_LE -t raw something</code> </p>
<p> The above will transfer audio data frame in &#8216;something&#8217; file including no information of sample format, as sample format of 22050 Hz, monaural, signed 16 bit little endian PCM for playback. The transmission continues till catching <i>SIGINT</i> from keyboard or <i>SIGTERM</i> by <i><a href="/docs/linux/man/1-kill/">kill</a>(1)</i> . </p>
<p> <code>$ axfer transfer capture -d 10 -f cd something.wav</code> </p>
<p> The above will transfer audio data frame to &#8216;something.wav&#8217; file as sample format of 44.1 kHz, 2 channels, signed 16 bit little endian PCM, during 10 seconds. The file format is Microsoft/IBM RIFF/Wave according to suffix of the given <i>filepath</i> . </p>
<p> <code>$ axfer transfer capture -s 1024 -r 48000 -c 2 -f S32_BE -I -t au channels</code> </p>
<p> The above will transfer audio data frame as sample format of 48.0 kHz, 2 channels, signed 32 bit big endian PCM for 1,024 number of data frames to files named &#8216;channels-1.au&#8217; and &#8216;channels-2.au&#8217;. </p>
<h2>SCHEDULING MODEL</h2>
<p> In a design of ALSA PCM core, runtime of PCM substream supports two modes; <i>period-wakeup</i> and <i>no-period-wakeup.</i> These two modes are for different scheduling models. </p>
<h3>IRQ-based scheduling model</h3>
<p> As a default, <i>period-wakeup</i> mode is used. In this mode, in-kernel drivers should operate hardware to generate periodical notification for transmission of audio data frame. The interval of notification is equivalent to the same amount of audio data frame as one period of buffer, against actual time. </p>
<p> In a handler assigned to the notification, a helper function of ALSA PCM core is called to update a position to head of hardware transmission, then compare it with a position to head of application operation to judge overrun/underrun (XRUN) and to wake up blocked processes. </p>
<p> For this purpose, hardware IRQ of controller for serial audio bus such as Inter-IC sound is typically used. In this case, the controller generates the IRQ according to transmission on the serial audio bus. In the handler assigned to the IRQ, direct media access (DMA) transmission is requested between dedicated host memory and device memory. </p>
<p> If target hardware doesn&#8217;t support this kind of mechanism, the periodical notification should be emulated by any timer; e.g. hrtimer, kernel timer. External PCM plugins generated by PCM plugin SDK in alsa-lib should also emulate the above behaviour. </p>
<p> In this mode, PCM applications are programmed according to typical way of I/O operations. They execute blocking system calls to read/write audio data frame in buffer of PCM substream, or blocking system calls to wait until any audio data frame is available. In <i>axfer</i> , this is called <i>IRQ-based</i> scheduling model and a default behaviour. Users can explicitly configure this mode by usage of <i>&#8211;sched-model</i> option with <i>irq</i> value. </p>
<h3>Timer-based scheduling model</h3>
<p> The <i>no-period-wakeup</i> mode is an optional mode of runtime of PCM substream. The mode assumes a specific feature of hardware and assist of in-kernel driver and PCM applications. In this mode, in-kernel drivers don&#8217;t operate hardware to generate periodical notification for transmission of audio data frame. The hardware should automatically continue transmission of audio data frame without periodical operation of the drivers; e.g. according to auto-triggered DMA transmission, a chain of registered descriptors. </p>
<p> In this mode, nothing wakes up blocked processes, therefore PCM applications should be programmed without any blocking operation. For this reason, this mode is enabled when the PCM applications explicitly configure hardware parameter to runtime of PCM substream, to prevent disorder of existing applications. Additionally, nothing maintains timing for transmission of audio data frame, therefore the PCM applications should voluntarily handle any timer to queue audio data frame in buffer of the PCM substream for lapse of time. Furthermore, instead of driver, the PCM application should call a helper function of ALSA PCM core to update a position to head of hardware transmission and to check XRUN. </p>
<p> In <i>axfer</i> , this is called <i>timer-based</i> scheduling model and available as long as hardware/driver assists <i>no-period-wakeup</i> runtime. Users should explicitly set this mode by usage of <i>&#8211;sched-model</i> option with <i>timer</i> value. </p>
<p> In the scheduling model, PCM applications need to care of available space on PCM buffer by lapse of time, typically by yielding CPU and wait for rescheduling. For the yielding, timeout is calculated for preferable amount of PCM frames to process. This is convenient to a kind of applications, like sound servers. when an I/O thread of the server wait for the timeout, the other threads can process audio data frames for server clients. Furthermore, with usage of rewinding/forwarding, applications can achieve low latency between transmission position and handling position even if they uses large size of PCM buffers. </p>
<h3>Advantages and issues</h3>
<p> Ideally, timer-based scheduling model has some advantages than IRQ-based scheduling model. At first, no interrupt context runs for PCM substream. The PCM substream is handled in any process context only. No need to care of race conditions between IRQ and process contexts. This reduces some concerns for some developers of drivers and applications. Secondary, CPU time is not used for handlers on the interrupt context. The CPU time can be dedicated for the other tasks. This is good in a point of Time Sharing System. Thirdly, hardware is not configured to generate interrupts. This is good in a point of reduction of overall power consumption possibly. </p>
<p> In either scheduling model, the hardware should allow drivers to read the number of audio data frame transferred between the dedicated memory and the device memory for audio serial bus. However, in timer-based scheduling model, fine granularity and accuracy of the value is important. Actually hardware performs transmission between dedicated memory and device memory for a small batch of audio data frames or bytes. In a view of PCM applications, the granularity in current transmission is required to decide correct timeout for each I/O operation. As of Linux kernel v4.21, ALSA PCM interface between kernel/userspace has no feature to report it. </p>
<h2>COMPATIBILITY TO APLAY</h2>
<p> The <code>transfer</code> subcommand of <code>axfer</code> is designed to keep compatibility to <a href="/docs/linux/man/1-aplay/">aplay</a>(1). However some options below are not compatible due to several technical reasons. </p>
<dl>
<dt><i>-I, &#8211;separate-channels</i></p>
<dd> This option is supported just for files to store audio data frames corresponding to each channel. In <a href="/docs/linux/man/1-aplay/">aplay</a>(1) implementation, this option has an additional effect to use PCM buffer aligned to non-interleaved order if a target device supports. As of 2018, PCM buffer of non-interleaved order is hardly used by sound devices. </p>
<dt><i>-A, &#8211;avail-min=#</i></p>
<dd> This option indicates threshold to wake up blocked process in a unit of audio data frame. Against <a href="/docs/linux/man/1-aplay/">aplay</a>(1) implementation, this option has no effect with <i>&#8211;mmap</i> option as well as <i>timer</i> of <i>&#8211;sched-model</i> option. </p>
<dt><i>-R, &#8211;start-delay=#</i></p>
<dd> This option indicates threshold to start prepared PCM substream in a unit of audio data frame. Against <a href="/docs/linux/man/1-aplay/">aplay</a>(1) implementation, this option has no effect with <i>&#8211;mmap</i> option as well as <i>timer</i> of <i>&#8211;sched-model</i> option. </p>
<dt><i>-T, &#8211;stop-delay=#</i></p>
<dd> This option indicates threshold to stop running PCM substream in a unit of audio data frame. Against <a href="/docs/linux/man/1-aplay/">aplay</a>(1) implementation, this option has no effect with <i>&#8211;mmap</i> option as well as <i>timer</i> of <i>&#8211;sched-model</i> option. </p>
<dt><i>&#8211;max-file-time=#</i></p>
<dd> This option is unsupported. In <a href="/docs/linux/man/1-aplay/">aplay</a>(1) implementation, the option has an effect for capture transmission to save files up to the same number of data frames as the given value by second unit, or the maximum number of data frames supported by used file format. When reaching to the limitation, used file is closed, then new file is opened and audio data frames are written. However, this option requires extra handling of files and shall increase complexity of main loop of axfer. </p>
<dt><i>&#8211;use-strftime=FORMAT</i></p>
<dd> This option is unsupported. In <a href="/docs/linux/man/1-aplay/">aplay</a>(1) implementation, the option has an effect for capture transmission to generate file paths according to given format in which some extra formats are available as well as formats supported by <a href="/docs/linux/man/3-strftime/">strftime</a>(3). However, this option requires extra string processing for file paths and it&#8217;s bothersome if written in C language. </p>
<dt><i>&#8211;process-id-file=FILEPATH</i></p>
<dd> This option is unsupported. In <a href="/docs/linux/man/1-aplay/">aplay</a>(1) implementation, the option has an effect to create a file for given value and write out process ID to it. This file allows users to get process ID and send any POSIX signal to aplay process. However, this idea has some troubles for file locking when multiple aplay processes run with the same file. </p>
<dt><i>-V, &#8211;vumeter=TYPE</i></p>
<dd> This option is not supported at present. In <a href="/docs/linux/man/1-aplay/">aplay</a>(1) implementation, this option has an effect to occupy stdout with some terminal control characters and display vumeter for monaural and stereo channels. However, some problems lay; this feature is just for audio data frames with PCM format, this feature brings disorder of terminal after aborting, stdout is not available for pipeline. </p>
<dt><i>-i, &#8211;interactive</i></p>
<dd> This option is not supported at present. In <a href="/docs/linux/man/1-aplay/">aplay</a>(1) implementation, this option has an effect to occupy stdin for key input and suspend/resume PCM substream according to pushed enter key. However, this feature requires an additional input handling in main loop and leave bothersome operation to maintain PCM substream. </p>
<dt><i>-m, &#8211;chmap=CH1,CH2,&#8230;</i></p>
<dd> ALSA PCM core and control core doesn&#8217;t support this feature, therefore remapping should be done in userspace. This brings overhead to align audio data frames, especially for mmap operation. Furthermore, as of alsa-lib v1.1.8, some plugins don&#8217;t support this feature expectedly, thus this option is a lack of transparent operation. At present, this option is not supported yet not to confuse users. </p>
<dt><i>SIGTSTP, SIGCONT</i></p>
<dd> This performs suspend/resume of PCM substream. In <a href="/docs/linux/man/1-aplay/">aplay</a>(1) implementation, these operations bring XRUN state to the substream, and suspend/resume is done in interactive mode in the above. Some developers use the signal for recovery test from XRUN. At present, no alternative is supported for the test. </p>
<dt><i>SIGUSR1</i></p>
<dd> This is not supported. In <a href="/docs/linux/man/1-aplay/">aplay</a>(1) implementation, this signal is assigned to a handler to close a current file to store audio data frame and open a new file to continue processing. However, as well as <i>&#8211;max-file-time</i> option, this option should increase complexity of main loop of axfer. </p>
</dl>
<h2>DESIGN</h2>
<h3>Modular structure</h3>
<p> This program consists of three modules; <i>xfer</i> , <i>mapper</i> and <i>container</i> . Each module has an abstraction layer to enable actual implementation. </p>
<pre><code>
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -device &lt;-&gt;| xfer | &lt;-&gt;| mapper | &lt;-&gt;| container | &lt;-&gt;file-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -libasound single wav
                                                                                                        libffado multiple au
                                                                                                            voc
                                                                                                                raw
</code></pre>
<p> The <i>xfer</i> module performs actual transmission to devices and nodes. The module can have several transmission backends. As a default backend, <i>libasound</i> backend is used to perform transmission via alsa-lib APIs. The module allows each backend to parse own command line options. </p>
<p> The <i>container</i> module performs to read/write audio data frame via descriptor for file/stream of multimedia container or raw data. The module automatically detect type of multimedia container and parse parameters in its metadata of data header. At present, three types of multimedia containers are supported; Microsoft/IBM RIFF/Wave ( <i>wav</i> ), Sparc AU ( <i>au</i> ) and Creative Technology voice ( <i>voc</i> ). Additionally, a special container is prepared for raw audio data ( <i>raw</i> ). </p>
<p> The <i>mapper</i> module handles buffer layout and alignment for transmission of audio data frame. The module has two implementations; <i>single</i> and <i>multiple</i> . The <i>single</i> backend uses one container to construct the buffer. The <i>multiple</i> backend uses several containers to construct it. </p>
<h3>Care of copying audio data frame</h3>
<p> Between the <i>xfer</i> module and <i>mapper</i> module, a pointer to buffer including audio data frames is passed. This buffer has two shapes for interleaved and non-interleaved order. For the former, the pointer points to one buffer. For the latter, the pointer points to an array in which each element points to one buffer. Between the <i>mapper</i> module and <i>container</i> module, a pointer to one buffer is passed because supported media containers including raw type store audio data frames in interleaved order. </p>
<p> In passing audio data frame between the modules, axfer is programmed to avoid copying between a buffer to another buffer as much as possible. For example, in some scenarios below, no copying occurs between modules. </p>
<p>&nbsp;&#8211; xfer(mmap/interleaved), mapper(single), container(any)<br />
&nbsp;&#8211; xfer(mmap/non-interleaved), mapper(multiple), containers(any) </p>
<h3>Unit test</h3>
<p> For each of the <i>mapper</i> and <i>container</i> module, unit test is available. To run the tests, execute below command: </p>
<pre>
$ make test
</pre>
<p> Each test iterates writing to file and reading to the file for many times and it takes long time to finish. Please take care of the execution time if running on any CI environment. </p>
<h2>SEE ALSO</h2>
<p> <code> <a href="/docs/linux/man/1-axfer/">axfer</a>(1), <a href="/docs/linux/man/1-axfer-list/">axfer-list</a>(1), <a href="/docs/linux/man/1-alsamixer/">alsamixer</a>(1), <a href="/docs/linux/man/1-amixer/">amixer</a>(1) </code> </p>
<h2>AUTHOR</h2>
<p> Takashi Sakamoto &lt;o-takashi [at] sakamocchi.jp&gt; </p>
<h2>Index</h2>
