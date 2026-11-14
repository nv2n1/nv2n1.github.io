---
title: "sane-test(5)"
name: "sane-test"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-test/"
description: "sane-test – SANE backend for testing frontends"
---

<p>sane-test &#8211; SANE backend for testing frontends</p>
<h2>Description</h2>
<p>The <code>sane-test</code> library implements a SANE (Scanner Access Now Easy) backend that allows testing the SANE installation and SANE frontends. It provides access to a (nearly) unlimited number of virtual devices. There is no support for real scanners or cameras. However, the backend simulates scanning and setting options. The idea is not only to find bugs in frontends but also to show all capabilities of SANE. Therefore <code>sane-test</code> implements functions and options that are not (or seldom) found in other backends. The backend is commented out in <i>/etc/sane.d/dll.conf</i>, so either the comment character must be removed or the backend must be called explicitly. E.g. <i>scanimage -d test</i> or <i>xscanimage test</i>. </p>
<h2>Scan Mode Options</h2>
<p>Option <code>mode</code> selects the scan mode (Gray or Color). </p>
<p> Option <code>depth</code> determines the number of bits per sample (1. 8, or 16). Keep in mind, that this value refers to the sample, not the pixel. So depth=16 results in 48 bits per pixel in color mode. The most usual combinations are mode=Gray, depth=1 for lineart, mode=Gray, depth=8 for gray and mode=Color, depth=8 for color mode. The combination of color and 1-bit mode is quite obscure (8 colors) but allowed in the SANE standard. However, the meaning of bits is not defined. Currently 1 = high intensity and 0 = low intensity is used. </p>
<p> Setting option <code>hand-scanner</code> results in the test-backend behaving like a hand-scanner. Hand-scanners do not know the image height a priori. Instead, they return a height of -1. Setting this option allows one to test whether a frontend can handle this correctly. This option also enables a fixed width of 11 cm. </p>
<p> Setting option <code>three-pass</code> simulates a three-pass scanner. Older color scanners needed to scan the image once per color (red/green/blue) to get the full image. Therefore, in this mode three single frames are transmitted in color mode. </p>
<p> Option <code>three-pass-order</code> provides support for changing the order of the three frames (see option three-pass above). A frontend should support all orders. </p>
<p> Option <code>resolution</code> sets the resolution of the image in dots per inch. </p>
<p> Option <code>source</code> can be used to simulate an Automatic Document Feeder (ADF). After 10 scans, the ADF will be &quot;empty&quot;.</p>
<h2>Special Options</h2>
<p>Option <code>test-picture</code> allows one to set the image that&#8217;s returned to the frontend. While &quot;Solid white&quot; and &quot;Solid black&quot; are quite obvious, the other options need some more explanation. Color patterns are used to determine if all modes and their colors are represented correctly by the frontend. The grid should look like the same in every mode and resolution. A table of all the test pictures can be found at: <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/test-backend/test-pictures.html">http://www.meier-geinitz.de/sane/test-backend/test-pictures.html</a></i>. </p>
<p> If option <code>invert-endianness</code> is set, the upper and lower bytes of image data in 16 bit modes are exchanged. This option can be used to test the 16 bit modes of frontends, e.g. if the frontend uses the correct endianness. </p>
<p> If option <code>read-limit</code> is set, the maximum amount of data transferred with each call to <code>sane_read</code>() is limited. </p>
<p> Option <code>read-limit-size</code> sets the limit for option read-limit. A low limit slows down scanning. It can be used to detect errors in frontend that occur because of wrong assumptions on the size of the buffer or timing problems. </p>
<p> Option <code>read-delay</code> enables delaying data to the frontend. </p>
<p> Option <code>read-delay-duration</code> selects the number of microseconds the backends waits after each transfer of a buffer. This option is useful to find timing-related bugs, especially if used over the network. </p>
<p> If option <code>read-return-value</code> is different from &quot;Default&quot;, the selected status will be returned by every call to <code>sane_read</code>(). This is useful to test the frontend&#8217;s handling of the SANE statuses. </p>
<p> If option <code>ppl-loss</code> is different from 0, it determines the number of pixels that are &quot;lost&quot; at the end of each line. That means, lines are padded with unused data. </p>
<p> Option <code>fuzzy-parameters</code> selects that fuzzy (inexact) parameters are returned as long as the scan hasn&#8217;t been started. This option can be used to test if the frontend uses the parameters it got before the start of the scan (which it shouldn&#8217;t). </p>
<p> Option <code>non-blocking</code> determines if non-blocking IO for <code>sane_read</code>() should be used if supported by the frontend. </p>
<p> If option <code>select-fd</code> is set, the backend offers a select filedescriptor for detecting if <code>sane_read()</code> will return data. </p>
<p> If option <code>enable-test-options</code> is set, a fairly big list of options for testing the various SANE option types is enabled. </p>
<p> Option <code>print-options</code> can be used to print a list of all options to standard error.</p>
<h2>Geometry Options</h2>
<p>Option <code>tl-x</code> determines the top-left x position of the scan area. </p>
<p> Option <code>tl-y</code> determines the top-left y position of the scan area. </p>
<p> Option <code>br-x</code> determines the bottom-right x position of the scan area. </p>
<p> Option <code>br-y</code> determines the bottom-right y position of the scan area.</p>
<h2>Bool Test Options</h2>
<p>There are 6 bool test options in total. Each option is numbered. (3/6) means: this is option 3 of 6. The numbering scheme is intended for easier detection of options not displayed by the frontend (because of missing support or bugs). </p>
<p> Option <code>bool-soft-select-soft-detect</code> (1/6) is a bool test option that has soft select and soft detect (and advanced) capabilities. That&#8217;s just a normal bool option. </p>
<p> Option <code>bool-hard-select-soft-detect</code> (2/6) is a bool test option that has hard select and soft detect (and advanced) capabilities. That means the option can&#8217;t be set by the frontend but by the user (e.g. by pressing a button at the device). </p>
<p> Option <code>bool-hard-select</code> (3/6) is a bool test option that has hard select (and advanced) capabilities. That means the option can&#8217;t be set by the frontend but by the user (e.g. by pressing a button at the device) and can&#8217;t be read by the frontend. </p>
<p> Option <code>bool-soft-detect</code> (4/6) is a bool test option that has soft detect (and advanced) capabilities. That means the option is read-only. </p>
<p> Option <code>bool-soft-select-soft-detect-emulated</code> (5/6) is a Bool test option that has soft select, soft detect, and emulated (and advanced) capabilities. </p>
<p> Option <code>bool-soft-select-soft-detect-auto</code> (6/6) is a Bool test option that has soft select, soft detect, and automatic (and advanced) capabilities. This option can be automatically set by the backend.</p>
<h2>Int Test Options</h2>
<p>There are 6 int test options in total. </p>
<p> Option <code>int</code> (1/6) is an int test option with no unit and no constraint set. </p>
<p> Option <code>int-constraint-range</code> (2/6) is an int test option with unit pixel and constraint range set. Minimum is 4, maximum 192, and quant is 2. </p>
<p> Option <code>int-constraint-word-list</code> (3/6) is an int test option with unit bits and constraint word list set. </p>
<p> Option <code>int-constraint-array</code> (4/6) is an int test option with unit mm and using an array without constraints. </p>
<p> Option <code>int-constraint-array-constraint-range</code> (5/6) is an int test option with unit mm and using an array with a range constraint. Minimum is 4, maximum 192, and quant is 2. </p>
<p> Option <code>int-constraint-array-constraint-word-list</code> (6/6) is an int test option with unit percent and using an array a word list constraint.</p>
<h2>Fixed Test Options</h2>
<p>There are 3 fixed test options in total. </p>
<p> Option <code>fixed</code> (1/3) is a fixed test option with no unit and no constraint set. </p>
<p> Option <code>fixed-constraint-range</code> (2/3) is a fixed test option with unit microsecond and constraint range set. Minimum is -42.17, maximum 32767.9999, and quant is 2.0. </p>
<p> Option <code>fixed-constraint-word-list</code> (3/3) is a Fixed test option with no unit and constraint word list set.</p>
<h2>String Test Options</h2>
<p>There are 3 string test options in total. </p>
<p> Option <code>string</code> (1/3) is a string test option without constraint. </p>
<p> Option <code>string-constraint-string-list</code> (2/3) is a string test option with string list constraint. </p>
<p> Option <code>string-constraint-long-string-list</code> (3/3) is a string test option with string list constraint. Contains some more entries&#8230;</p>
<h2>Button Test Option</h2>
<p>Option <code>button</code> (1/1) is a Button test option. Prints some text&#8230;</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/test.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below). The initial values of most of the basic SANE options can be configured in this file. A template containing all the default values is provided together with this backend. One of the more interesting values may be <code>number_of_devices</code>. It can be used to check the frontend&#8217;s ability to show a long list of devices. The config values concerning resolution and geometry can be useful to test the handling of big file sizes. </p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-test.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-test.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_TEST</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> Example: export SANE_DEBUG_TEST=4 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1)<br />
 <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/test-backend/">http://www.meier-geinitz.de/sane/test-backend/</a></i> </p>
<h2>Author</h2>
<p>Henning Meier-Geinitz &lt;<i>henning [at] meier-geinitz.de</i>&gt;</p>
<h2>Bugs</h2>
<p>&#8211; config file values aren&#8217;t tested for correctness </p>
