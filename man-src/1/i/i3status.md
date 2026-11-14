---
title: "i3status(1)"
name: "i3status"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i3status/"
description: "i3status – Generates a status line for dzen2 or xmobar"
---

<h2 class="name">NAME</h2>
<p> i3status &#8211; Generates a status line for dzen2 or xmobar </p>
<h2>SYNOPSIS</h2>
<p> i3status [-c configfile]</p>
<h2>OPTIONS</h2>
<p> -c</p>
<dl>
<dt>
<dd> Specifies an alternate configuration file path (default is /etc/i3status.conf or ~/.i3status.conf).</dl>
<h2>DESCRIPTION</h2>
<p> i3status is a small program (less than 1000 SLOC) for generating a status bar for dzen2, xmobar or similar programs. It is designed to be very efficient by issuing a very small number of systemcalls, as one generally wants to update such a status line every second. This ensures that even under high load, your status bar is updated correctly. Also, it saves a bit of energy by not hogging your CPU as much as spawning the corresponding amount of shell commands would.</p>
<h2>CONFIGURATION</h2>
<p> Since version 2, the configuration file for i3status will be parsed using libconfuse. This makes configuration easier in the programmercqs point of view and more flexible for the user at the same time. </p>
<p> The basic idea of i3status is that you can specify which &quot;modules&quot; should be used (the order directive). You can then configure each module with its own section. For every module, you can specify the output format. See below for a complete reference. </p>
<p> <code>Sample configuration</code>. </p>
<dl>
<dt>
<dd>
<pre><code>
general{
    output_format = "dzen2" colors = true interval = 5} order = "ipv6" order += "disk /" order += "run_watch DHCP" order += "run_watch VPN" order += "wireless wlan0" order += "ethernet eth0" order += "battery 0" order += "cpu_temperature 0" order += "load" order += "time" wireless wlan0{
    format_up = "W: (%quality at %essid) %ip" format_down = "W: down"} ethernet eth0
{
#if you use % speed, i3status requires the cap_net_admin capability
    format = "E: %ip (%speed)"
}
battery 0 {
    format = "%status %percentage %remaining"} run_watch DHCP{
    pidfile = "/var/run/dhclient*.pid"} run_watch VPN{
    pidfile = "/var/run/vpnc/pid"} time{
    format = "%Y-%m-%d %H:%M:%S"} load{
    format = "%5min"} cpu_temperature 0 {
    format = "T: %degrees &amp;#176;C"} disk "/"
{
    format = "%free"
}
</code></pre>
</dl>
<h3>General</h3>
<p> The colors directive will disable all colors if you set it to false. interval is the time in seconds which i3status will sleep until printing the next status line. </p>
<p> Using output_format you can chose which format strings i3status should use in its output. Currently available are: </p>
<p> dzen2</p>
<dl>
<dt>
<dd> Dzen is a general purpose messaging, notification and menuing program for X11. It was designed to be scriptable in any language and integrate well with window managers like dwm, wmii and xmonad though it will work with any windowmanger</dl>
<p> xmobar</p>
<dl>
<dt>
<dd> xmobar is a minimalistic, text based, status bar. It was designed to work with the xmonad Window Manager.</dl>
<p> none</p>
<dl>
<dt>
<dd> Does not use any color codes. Separates values by the pipe symbol.</dl>
<h3>IPv6</h3>
<p> This module gets the IPv6 address used for outgoing connections (that is, the best available public IPv6 address on your computer). </p>
<p> <code>Example format_up</code>: %ip </p>
<p> <code>Example format_down</code> no IPv6</p>
<h3>Disk</h3>
<p> Gets used, free and total amount of bytes on the given mounted filesystem. </p>
<p> <code>Example order</code>: disk /mnt/usbstick </p>
<p> <code>Example format</code>: %free / %total</p>
<h3>Run-watch</h3>
<p> Expands the given path to a pidfile and checks if the process ID found inside is valid (that is, if the process is running). You can use this to check if a specific application, such as a VPN client or your DHCP client is running. </p>
<p> <code>Example order</code>: run_watch DHCP</p>
<h3>Wireless</h3>
<p> Gets the link quality and ESSID of the given wireless network interface. You can specify different format strings for the network being connected or not connected. </p>
<p> <code>Example order</code>: wireless wlan0 </p>
<p> <code>Example format</code>: W: (%quality at %essid) %ip</p>
<h3>Ethernet</h3>
<p> Gets the IP address and (if possible) the link speed of the given ethernet interface. Getting the link speed requires the cap_net_admin capability. Set it using setcap cap_net_admin=ep $(which i3status). </p>
<p> <code>Example order</code>: ethernet eth0 </p>
<p> <code>Example format</code>: E: %ip (%speed)</p>
<h3>Battery</h3>
<p> Gets the status (charging, discharging, running), percentage and remaining time of the given battery. If you want to use the last full capacity instead of the design capacity (when using the design capacity, it may happen that your battery is at 23% when fully charged because itcqs old. In general, I want to see it this way, because it tells me how worn off my battery is.), just specify last_full_capacity = true. </p>
<p> <code>Example order</code>: battery 0 </p>
<p> <code>Example format</code>: %status %remaining</p>
<h3>CPU-Temperature</h3>
<p> Gets the temperature of the given thermal zone. </p>
<p> <code>Example order</code>: cpu_temperature 0 </p>
<p> <code>Example format</code>: T: %degrees &#176;C</p>
<h3>Load</h3>
<p> Gets the system load (number of processes waiting for CPU time in the last 5, 10 and 15 minutes). </p>
<p> <code>Example order</code>: load </p>
<p> <code>Example format</code>: %5min %10min %15min</p>
<h3>Time</h3>
<p> Formats the current system time. See <a href="/docs/linux/man/3-strftime/">strftime</a>(3) for the format. </p>
<p> <code>Example order</code>: time </p>
<p> <code>Example format</code>: %Y-%m-%d %H:%M:%S</p>
<h2>USING I3STATUS WITH DZEN2</h2>
<p> After installing dzen2, you can directly use it with i3status: </p>
<p> <code>Example for usage of i3status with dzen2</code>: </p>
<dl>
<dt>
<dd>
<pre>
i3status | dzen2 -fg white -ta r -w 1280 \
-fn &quot;-misc-fixed-medium-r-normal--13-120-75-75-C-70-iso8859-1&quot;
</pre>
</dl>
<h2>USING I3STATUS WITH XMOBAR</h2>
<p> To get xmobar to start, you might need to copy the default configuration file to ~/.xmobarrc. </p>
<p> <code>Example for usage of i3status with xmobar</code>: </p>
<dl>
<dt>
<dd>
<pre>
i3status-xmobar | xmobar -o -t &quot;%StdinReader%&quot; -c &quot;[Run StdinReader]&quot;
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-strftime/">strftime</a>(3), <a href="/docs/linux/man/1-date/">date</a>(1), <a href="/docs/linux/man/3-glob/">glob</a>(3), <a href="/docs/linux/man/1-dzen2/">dzen2</a>(1), <a href="/docs/linux/man/1-xmobar/">xmobar</a>(1)</p>
<h2>AUTHORS</h2>
<p> Michael Stapelberg and contributors </p>
<p> Thorsten Toepper </p>
<p> Baptiste Daroussin </p>
<h2>Index</h2>
