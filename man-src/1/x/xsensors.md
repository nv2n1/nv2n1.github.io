---

title: "xsensors(1)"
name: "xsensors"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xsensors/"
---

xsensors - display hardware sensor information as a graphical read-out.

<h2>SYNOPSIS</h2>

 <b>xsensors</b> [<i>OPTION</i>]... 

<h2>DESCRIPTION</h2>

 View the output from the libsensors library regarding hardware health in a graphical read-out. 

<h2>OPTIONS</h2>

<dl>
<dt><b>-f</b>
</dt><dd> display all temperatures in Fahrenheit.
</dd><dt><b>-c</b> filename
</dt><dd> specify the libsensors configuration file.
</dd><dt><b>-i</b>
</dt><dd> specify the image file to use as the graphical theme.
</dd><dt><b>-t</b> time
</dt><dd> specify the update interval in seconds.
</dd><dt><b>-v</b>
</dt><dd> display the version number. 
</dd></dl>

<h2>CONFIGURATION</h2>

 To find the proper kernel modules necessary for xsensors to work, please run the <b>sensors-detect</b> command as superuser and follow the on-screen instructions; a reboot may be required. The <b>sensors-detect</b> command is provided by the <i>lm-sensors</i> package. 

<h2>FILES</h2>

 <i>/usr/share/xsensors/theme.tiff</i>: the default graphical theme. 

 <i>/etc/sensors3.conf</i>: the default configuration file. 

<h2>AUTHOR</h2>

 This manual page was written by Nick Rusnov &lt;nickrusnov [at] debian.org&gt; and Nanley Chery &lt;nanleychery [at] gmail.com&gt; for the Debian GNU/Linux system (but may be used by others).
