---
title: "redshift(1)"
name: "redshift"
section: "1"
letter: "r"
url: "/docs/linux/man/1-redshift/"
description: "redshift – set color temperature of display according to time of day"
---

<h2 class="name">NAME</h2>
<p> redshift &#8211; set color temperature of display according to time of day </p>
<h2>SYNOPSIS</h2>
<p> <code>redshift</code> [<code>-l</code> <i>LAT</i><code>:</code><i>LON</i> | <code>-l</code> <i>PROVIDER</i><code>:</code><i>OPTIONS</i>] [<code>-t</code> <i>DAY</i><code>:</code><i>NIGHT</i>] [<i>OPTIONS</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>redshift</code> adjusts the color temperature of your screen according to your surroundings. This may help your eyes hurt less or reduce the risk for delayed sleep phase syndrome if you are working in front of the screen at night. </p>
<p> The color temperature is set according to the position of the sun. A different color temperature is set during night and daytime. During twilight and early morning, the color temperature transitions smoothly from night to daytime temperature to allow your eyes to slowly adapt over a period of about an hour. At night the color temperature should be set to match the lamps in your room. This is typically a low temperature at around 3000K-4000K (default is 4500K). During the day, the color temperature should match the light from outside, typically around 5500K-6500K (default is 6500K). The light has a higher temperature on an overcast day. </p>
<p> In addition to the command-line tool <code>redshift</code>, the GUI <code>redshift-gtk</code> provides an alternative interface that shows up as a notification icon in the desktop environment.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display help message.</p>
<dt><code>-v</code></p>
<dd> Enable verbose output.</p>
<dt><code>-V</code></p>
<dd> Show program version.</p>
<dt><code>-b</code> <i>DAY</i><code>:</code><i>NIGHT</i></p>
<dd> Screen brightness to apply (between 0.1 and 1.0).</p>
<dt><code>-c</code> <i>FILE</i></p>
<dd> Load settings from specified configuration file.</p>
<dt><code>-g</code> <i>R</i><code>:</code><i>G</i><code>:</code><i>B</i></p>
<dd> Additional gamma correction to apply.</p>
<dt><code>-l</code> <i>LAT</i><code>:</code><i>LON</i></p>
<dd> Your current location, in degrees, given as floating point numbers, towards north and east, with negative numbers representing south and west, respectively.</p>
<dt><code>-l</code> <i>PROVIDER</i>[<code>:</code><i>OPTIONS</i>]</p>
<dd> Select provider for automatic location updates (Use <code>&quot;-l list&quot;</code> to see available providers).</p>
<dt><code>-m</code> <i>METHOD</i>[<code>:</code><i>OPTIONS</i>]</p>
<dd> Method to use to set color temperature (Use <code>&quot;-m list&quot;</code> to see available methods).</p>
<dt><code>-o</code></p>
<dd> One-shot mode (do not continuously adjust color temperature). Use this with the <code>-P</code> option to clear the existing gamma ramps before applying the new color temperature.</p>
<dt><code>-O</code> <i>TEMP</i></p>
<dd> One-shot manual mode (set color temperature). Use this with the <code>-P</code> option to clear the existing gamma ramps before applying the new color temperature.</p>
<dt><code>-p</code></p>
<dd> Print mode (only print parameters and exit).</p>
<dt><code>-P</code></p>
<dd> Reset existing gamma ramps before applying new color effect.</p>
<dt><code>-x</code></p>
<dd> Reset mode (remove adjustment from screen).</p>
<dt><code>-r</code></p>
<dd> Disable fading between color temperatures.</p>
<dt><code>-t</code> <i>DAY</i><code>:</code><i>NIGHT</i></p>
<dd> Color temperature to set at daytime/night.</dl>
<p> The neutral temperature is 6500K. Using this value will not change the color temperature of the display. Setting the color temperature to a value higher than this results in more blue light, and setting a lower value will result in more red light. </p>
<p> Default temperature values:</p>
<dl>
<dt>
<dd> Daytime: 6500K, night: 4500K</dl>
<h2>CONFIGURATION FILE</h2>
<p> A configuration file with the name <i>redshift.conf</i> can optionally be placed in <i>~/.config/</i>. The file has standard INI format. General program options are placed under the <code>redshift</code> header, while options for location providers and adjustment methods are placed under a header with the name of that provider or method. General options are:</p>
<dl>
<dt><code>temp-day</code> = <i>integer</i></p>
<dd> Daytime temperature</p>
<dt><code>temp-night</code> = <i>integer</i></p>
<dd> Night temperature</p>
<dt><code>fade</code> = <i>0 or 1</i></p>
<dd> Disable or enable fading between color temperatures when Redshift starts or stops</p>
<dt><code>brightness-day</code> = <i>0.1-1.0</i></p>
<dd> Screen brightness at daytime</p>
<dt><code>brightness-night</code> = <i>0.1-1.0</i></p>
<dd> Screen brightness at night</p>
<dt><code>elevation-high</code> = <i>decimal</i></p>
<dd> The solar elevation in degrees for the transition to daytime</p>
<dt><code>elevation-low</code> = <i>decimal</i></p>
<dd> The solar elevation in degrees for the transition to night</p>
<dt><code>dawn-time</code> = <i>HH</i><code>:</code><i>MM</i>[<code>&#8211;</code><i>HH</i><code>:</code><i>MM</i>]</p>
<dd> The custom time interval for the transition from night to day in the morning. When specified, the solar elevation will not be used to determine the current daytime/night period. If this option is set, dusk-time must also be specified.</p>
<dt><code>dusk-time</code> = <i>HH</i><code>:</code><i>MM</i>[<code>&#8211;</code><i>HH</i><code>:</code><i>MM</i>]</p>
<dd> The custom time interval for the transition from day to night in the evening. When specified, the solar elevation will not be used to determine the current daytime/night period. If this option is set, dawn-time must also be specified.</p>
<dt><code>gamma</code> = <i>R</i><code>:</code><i>G</i><code>:</code><i>B</i></p>
<dd> Gamma adjustment to apply (day and night)</p>
<dt><code>gamma-day</code> = <i>R</i><code>:</code><i>G</i><code>:</code><i>B</i></p>
<dd> Gamma adjustment to apply at daytime</p>
<dt><code>gamma-night</code> = <i>R</i><code>:</code><i>G</i><code>:</code><i>B</i></p>
<dd> Gamma adjustment to apply at night</p>
<dt><code>adjustment-method</code> = <i>name</i></p>
<dd> Select adjustment method. Options for the adjustment method can be given under the configuration file heading of the same name.</p>
<dt><code>location-provider</code> = <i>name</i></p>
<dd> Select location provider. Options for the location provider can be given under the configuration file heading of the same name.</dl>
<p> Options for location providers and adjustment methods can be found in the help output of the providers and methods.</p>
<h2>EXAMPLE</h2>
<p> Example for Copenhagen, Denmark:</p>
<dl>
<dt>
<dd> <code>$</code> redshift -l 55.7:12.6 -t 5700:3600 -g 0.8 -m randr -v</dl>
<p> An example configuration file with the same effect as the above command line:</p>
<dl>
<dt>
<dd>
<pre><code>
[redshift] temp - day = 5700 temp - night = 3600 gamma = 0.8 adjustment - method = randr
                                                                                       location -
                                                                                   provider = manual
                                                                                       [manual] lat = 55.7 lon = 12.6
</code></pre>
</dl>
<h2>HOOKS</h2>
<p> Executables (e.g. scripts) placed in folder <i>~/.config/redshift/hooks</i> will be run when a certain event happens. The first parameter to the script indicates the event and further parameters may indicate more details about the event. The event <code>period-changed</code> is indicated when the period changes (<code>night</code>, <code>daytime</code>, <code>transition</code>). The second parameter is the old period and the third is the new period. The event is also signaled when Redshift starts up with the old period set to <code>none</code>. Any dotfiles in the folder are skipped. </p>
<p> A simple script to handle these events can be written like this:</p>
<dl>
<dt>
<dd>
<pre>
#!/bin/sh
case <code>$1</code> in
    <code>period-changed</code>)
        exec notify-send &quot;Redshift&quot; &quot;Period changed to <code>$3</code>&quot;
esac
</pre>
</dl>
<h2>AUTHOR</h2>
<p> <code>redshift</code> was written by Jon Lund Steffensen &lt;jonlst [at] gmail.com&gt;. </p>
<p> Both <code>redshift</code> and this manual page are released under the GNU General Public License, version 3.</p>
<h2>BUGS</h2>
<p> Please report bugs to &lt;<a rel="nofollow" href="https://github.com/jonls/redshift/issues">https://github.com/jonls/redshift/issues</a>&gt;</p>
<h2>KNOWN ISSUES</h2>
<p> <code>redshift</code> will not affect the color of your cursor when your graphics driver is configured to use hardware cursors. Some graphics drivers have an option to disable hardware cursors. </p>
<h2>Index</h2>
