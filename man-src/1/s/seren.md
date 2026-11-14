---
title: "seren(1)"
name: "seren"
section: "1"
letter: "s"
url: "/docs/linux/man/1-seren/"
description: "Seren – A simple VoIP program to create conferences from the terminal"
---

<h2>NAME</h2>
<p> Seren &#8211; A simple VoIP program to create conferences from the terminal</p>
<h2>SYNOPSIS</h2>
<p> <code>seren</code> [option&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Seren is a simple VoIP program based on the Opus codec that allows you to create a voice conference from the terminal, with up to 10 participants, without having to register accounts, exchange emails, or add people to contact lists. All you need to join an existing conference is the host name or IP address of one of the participants. Seren creates a dynamic peer-to-peer network of equivalent nodes which exchange text and audio data using a udp connection, and offers the user the ability to change the quality/bitrate on the fly, encrypt the traffic and record the calls. </p>
<p> This manual page documents briefly the <code>seren</code> command. Please refer to the README file to get more information on how to use Seren.</p>
<h2>OPTIONS</h2>
<p> A summary of command line options is included below.</p>
<dl>
<dt><code>-h</code></p>
<dd> Print help, showing a list of available command line options. The values in parentheses on the right are the default values.</p>
<dt><code>-v</code></p>
<dd> Increment verbosity level. <code>-v</code> enables verbose messages and <code>-v -v</code> enables verbose and debug messages.</p>
<dt><code>-L</code><i> logfile</i></p>
<dd> Send log messages to logfile (default: $HOME/.seren/seren.log)</p>
<dt><code>-N</code></p>
<dd> Disable ncurses interface and run Seren as a pure command line application.</p>
<dt><code>-t</code><i> theme</i></p>
<dd> Set ncurses theme: 0-simple, 1-dark, 2-clear (default: 1).</p>
<dt><code>-n</code><i> nick</i></p>
<dd> Set nickname (default: login name).</p>
<dt><code>-p</code><i> port</i></p>
<dd> Set udp listening port (default: 8110).</p>
<dt><code>-b</code><i> bitrate</i></p>
<dd> Set Opus encoding bitrate in bit/s (default: 16000).</p>
<dt><code>-C</code><i> complexity</i></p>
<dd> Set Opus encoding complexity. The supported range is 0-10 inclusive with 10 representing the highest complexity. Small values will make Seren run faster, at the expense of quality. You may want to lower this value if you are on a embedded system like the Raspberry Pi or if you notice that Seren is using up all your cpu time (default: 10).</p>
<dt><code>-d</code><i> audiodev</i></p>
<dd> Set alsa playback audio device. If you get an error with the device hw:0,0 try prepending plug to the device name, es. plughw:0,0. If your system has pulseaudio installed, it should be possible to specify &#8216;pulse&#8217; to use it. (default: depends on how Seren was configured, see the output of -h option).</p>
<dt><code>-D</code><i> audiodev</i></p>
<dd> Set alsa capture audio device. Useful if you want to use two different audio devices for playback and capture. (default: same value specified for playback device)</p>
<dt><code>-c</code><i> host[:port]</i></p>
<dd> Automatically call the specified host on startup.</p>
<dt><code>-a</code></p>
<dd> Autoaccept calls. If this options is enabled Seren will accept every incoming call without asking the user first.</p>
<dt><code>-S</code></p>
<dd> Disable STUN to retrieve the external IP address.</dl>
<h2>FILES</h2>
<dl>
<dt><i>$HOME/.seren/seren.log</i></p>
<dd> Log file.</p>
<dt><i>$HOME/.seren/seren.conf</i></p>
<dd> Configuration file.</p>
<dt><i>$HOME/.seren/history</i></p>
<dd> Command history file.</p>
<dt><i>$HOME/.seren/fifo_in</i></p>
<dd> Input fifo: accepts raw audio in 48000Hz/2ch/s16_le format. When fifos are enabled (using the /f command), writing to this fifo will make Seren mix this pcm audio signal with the one coming from the sound card. Useful if you want to transmit pre-recorded audio together with your own voice.</p>
<dt><i>$HOME/.seren/fifo_out</i></p>
<dd> Output fifo: provides raw audio in 48000Hz/2ch/s16_le format. When fifos are enabled (using the /f command), reading from this fifo will allow you to get the pcm audio signal of the conference and pipe it to another process.</dl>
<h2>AUTHOR</h2>
<p> Written by Giorgio Vazzana &lt;mywing81 [at] gmail.com&gt;. </p>
<h2>Index</h2>
