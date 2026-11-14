---
title: "x11perf(1)"
name: "x11perf"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x11perf/"
description: "x11perf – X11 server performance test program"
---

<h2 class="name">NAME</h2>
<p> x11perf &#8211; X11 server performance test program </p>
<h2>SYNTAX</h2>
<p> <code>x11perf</code> [ -option &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> The <i>x11perf</i> program runs one or more performance tests and reports how fast an X server can execute the tests. </p>
<p> Many graphics benchmarks assume that the graphics device is used to display the output of a single fancy graphics application, and that the user gets his work done on some other device, like a terminal. Such benchmarks usually measure drawing speed for lines, polygons, text, etc. </p>
<p> Since workstations are not used as standalone graphics engines, but as super-terminals, <i>x11perf</i> measures window management performance as well as traditional graphics performance. <i>x11perf</i> includes benchmarks for the time it takes to create and map windows (as when you start up an application); to map a pre-existing set of windows onto the screen (as when you deiconify an application or pop up a menu); and to rearrange windows (as when you slosh windows to and fro trying to find the one you want). </p>
<p> <i>x11perf</i> also measures graphics performance for operations not normally used in standalone graphics displays, but are nonetheless used frequently by X applications. Such operations include CopyPlane (used to map bitmaps into pixels), scrolling (used in text windows), and various stipples and tiles (used for CAD and color half-toning, respectively). </p>
<p> <i>x11perf</i> should be used to analyze particular strengths and weaknesses of servers, and is most useful to a server writer who wants to analyze and improve a server. <i>x11perf</i> is meant to comprehensively exercise just about every X11 operation you can perform; it does not purport to be a representative sample of the operations that X11 applications actually use. While it can be used as a benchmark, it was written and is intended as a performance testing tool. </p>
<p> As such, <i>x11perf</i> DOES NOT whittle down measurements to a single &#8220;HeXStones&#8221; or &#8220;MeXops&#8221; number. We consider such numbers to be uninformative at best and misleading at worst. Some servers which are very fast for certain applications can be very slow for others. No single number or small set of numbers are sufficient to characterize how an X implementation will perform on all applications. However, by knowledge of your favorite application, you may be able to use the numbers <i>x11perf</i> reports to predict its performance on a given X implementation. </p>
<p> That said, you might also want to look at <i><a href="/docs/linux/man/1-x11perfcomp/">x11perfcomp</a>(1),</i> a program to compare the outputs of different <i>x11perf</i> runs. You provide a list of files containing results from <i>x11perf,</i> and it lays them out in a nice tabular format. </p>
<p> For repeatable results, <i>x11perf</i> should be run using a local connection on a freshly-started server. The default configuration runs each test 5 times, in order to see if each trial takes approximately the same amount of time. Strange glitches should be examined; if non-repeatable one might chalk them up to daemons and network traffic. Each trial is run for 5 seconds, in order to reduce random time differences. The number of objects processed per second is displayed to 3 significant digits, but you&#8217;ll be lucky on most UNIX system if the numbers are actually consistent to 2 digits. <i>x11perf</i> moves the cursor out of the test window; you should be careful not to bump the mouse and move it back into the window. (A prize to people who correctly explain why!!). </p>
<p> Before running a test, <i>x11perf</i> determines what the round trip time to the server is, and factors this out of the final timing reported. It ensures that the server has actually performed the work requested by fetching a pixel back from the test window, which means that servers talking to graphics accelerators can&#8217;t claim that they are done, while in the meantime the accelerator is painting madly. </p>
<p> By default <i>x11perf</i> automatically calibrates the number of repetitions of each test, so that each should take approximately the same length of time to run across servers of widely differing speeds. However, since each test must be run to completion at least once, some slow servers may take a very long time, particularly on the window moving and resizing tests, and on the arc drawing tests. </p>
<p> All timing reports are for the smallest object involved. For example, the line tests use a PolyLine request to paint several lines at once, but report how many lines per second the server can paint, not how many PolyLine requests per second. Text tests paint a line of characters, but report on the number of characters per second. Some window tests map, unmap, or move a single parent window, but report on how many children windows per second the server can map, unmap, or move. </p>
<p> The current program is mostly the responsibility of Joel McCormack. It is based upon the x11perf developed by Phil Karlton, Susan Angebranndt, Chris Kent, Mary Walker, and Todd Newman, who wanted to assess performance differences between various servers. Several tests were added in order to write and tune the PMAX (DECStation 3100) servers. For a general release to the world, <i>x11perf</i> was rewritten to ease making comparisons between widely varying machines, to cover most important (and unimportant) X functionality, and to exercise graphics operations in as many different orientations and alignments as possible.</p>
<h2>OPTIONS</h2>
<p> <i>x11perf</i> is solely Xlib based, and accepts the options listed below:</p>
<dl>
<dt><code>-display host:dpy</code></p>
<dd> Specifies which display to use.</p>
<dt><code>-sync</code></p>
<dd> Runs the tests in synchronous mode. Normally only useful for debugging <i>x11perf .</i></p>
<dt><code>-pack</code></p>
<dd> Runs rectangle tests so that they pack rectangles right next to each other. This makes it easy to debug server code for stipples and tiles&#8230;if the pattern looks ugly, you&#8217;ve got alignment problems.</p>
<dt><code>-repeat </code><i>&lt;n&gt;</i></p>
<dd> Repeats each test <i>n</i> times (by default each test is run 5 times).</p>
<dt><code>-time </code><i>&lt;s&gt;</i></p>
<dd> Specifies how long in seconds each test should be run (default 5 seconds).</p>
<dt><code>-pause </code><i>&lt;s&gt;</i></p>
<dd> Specifies how long, in seconds, to pause for between each run.</p>
<dt><code>-all</code></p>
<dd> Runs all tests. This may take a while.</p>
<dt><code>-range </code><i>&lt;test1&gt;</i>[,<i>&lt;test2&gt;</i>]</p>
<dd> Runs all the tests starting from the specified name <i>test1</i> until the name <i>test2</i>, including both the specified tests. The testnames should be one of the options starting from -dot. (eg) -range line100 will perform the tests from the 100 pixel line test, and go on till the last test, -range line100,dline10 will do the tests from line100 to dline10.</p>
<dt><code>-labels</code></p>
<dd> Generates just the descriptive labels for each test specified. See <i>x11perfcomp</i> for more details.</p>
<dt><code>-fg </code><i>color-or-pixel</i></p>
<dd> Specifies the foreground color or pixel value to use.</p>
<dt><code>-bg </code><i>color-or-pixel</i></p>
<dd> Specifies the background color or pixel value to use.</p>
<dt><code>-clips </code><i>default</i></p>
<dd> Default number of clip windows.</p>
<dt><code>-ddbg </code><i>color-or-pixel</i></p>
<dd> Specifies the color or pixel value to use for drawing the odd segments of a DoubleDashed line or arc. This will default to the bg color.</p>
<dt><code>-rop &lt;rop0 rop1 &#8230;&gt;</code></p>
<dd> Use specified raster ops (default is GXcopy). This option only affects graphics benchmarks in which the graphics function is actually used.</p>
<dt><code>-pm &lt;pm0 pm1 &#8230;&gt;</code></p>
<dd> Use specified planemasks (default is ~0). This option only affects graphics benchmarks in which the planemask is actually used.</p>
<dt><code>-depth &lt;depth&gt;</code></p>
<dd> Use a visual with &lt;depth&gt; planes per pixel (default is the default visual).</p>
<dt><code>-vclass &lt;vclass&gt;</code></p>
<dd> Use a visual with of class &lt;vclass&gt;. &lt;vclass&gt; can be StaticGray, GrayScale, StaticColor, PseudoColor, TrueColor, or DirectColor. (default is the default visual).</p>
<dt><code>-reps &lt;n&gt;</code></p>
<dd> Specify the repetition count (Default is number that takes approx. 5 seconds)</p>
<dt><code>-subs &lt;s0 s1 &#8230;&gt;</code></p>
<dd> Specify the number of sub windows to use in the Window tests. Default is 4, 16, 25, 50, 75, 100 and 200.</p>
<dt><code>-v1.2</code></p>
<dd> Perform only x11perf Version 1.2 tests using Version 1.2 semantics.</p>
<dt><code>-v1.3</code></p>
<dd> Perform only x11perf Version 1.3 tests using Version 1.3 semantics.</p>
<dt><code>-su</code></p>
<dd> Set the save_under window attribute to True on all windows created by x11perf. Default is False.</p>
<dt><code>-bs &lt;backing_store_hint&gt;</code></p>
<dd> Set the backing_store window attribute to the given value on all windows created by x11perf. &lt;backing_store_hint&gt; can be WhenMapped or Always. Default is NotUseful.</p>
<dt><code>-dot</code></p>
<dd> Dot.</p>
<dt><code>-rect1</code></p>
<dd> 1&#215;1 solid-filled rectangle.</p>
<dt><code>-rect10</code></p>
<dd> 10&#215;10 solid-filled rectangle.</p>
<dt><code>-rect100</code></p>
<dd> 100&#215;100 solid-filled rectangle.</p>
<dt><code>-rect500</code></p>
<dd> 500&#215;500 solid-filled rectangle.</p>
<dt><code>-srect1</code></p>
<dd> 1&#215;1 transparent stippled rectangle, 8&#215;8 stipple pattern.</p>
<dt><code>-srect10</code></p>
<dd> 10&#215;10 transparent stippled rectangle, 8&#215;8 stipple pattern.</p>
<dt><code>-srect100</code></p>
<dd> 100&#215;100 transparent stippled rectangle, 8&#215;8 stipple pattern.</p>
<dt><code>-srect500</code></p>
<dd> 500&#215;500 transparent stippled rectangle, 8&#215;8 stipple pattern.</p>
<dt><code>-osrect1</code></p>
<dd> 1&#215;1 opaque stippled rectangle, 8&#215;8 stipple pattern.</p>
<dt><code>-osrect10</code></p>
<dd> 10&#215;10 opaque stippled rectangle, 8&#215;8 stipple pattern.</p>
<dt><code>-osrect100</code></p>
<dd> 100&#215;100 opaque stippled rectangle, 8&#215;8 stipple pattern.</p>
<dt><code>-osrect500</code></p>
<dd> 500&#215;500 opaque stippled rectangle, 8&#215;8 stipple pattern.</p>
<dt><code>-tilerect1</code></p>
<dd> 1&#215;1 tiled rectangle, 4&#215;4 tile pattern.</p>
<dt><code>-tilerect10</code></p>
<dd> 10&#215;10 tiled rectangle, 4&#215;4 tile pattern.</p>
<dt><code>-tilerect100</code></p>
<dd> 100&#215;100 tiled rectangle, 4&#215;4 tile pattern.</p>
<dt><code>-tilerect500</code></p>
<dd> 500&#215;500 tiled rectangle, 4&#215;4 tile pattern.</p>
<dt><code>-oddsrect1</code></p>
<dd> 1&#215;1 transparent stippled rectangle, 17&#215;15 stipple pattern.</p>
<dt><code>-oddsrect10</code></p>
<dd> 10&#215;10 transparent stippled rectangle, 17&#215;15 stipple pattern.</p>
<dt><code>-oddsrect100</code></p>
<dd> 100&#215;100 transparent stippled rectangle, 17&#215;15 stipple pattern.</p>
<dt><code>-oddsrect500</code></p>
<dd> 500&#215;500 transparent stippled rectangle, 17&#215;15 stipple pattern.</p>
<dt><code>-oddosrect1</code></p>
<dd> 1&#215;1 opaque stippled rectangle, 17&#215;15 stipple pattern.</p>
<dt><code>-oddosrect10</code></p>
<dd> 10&#215;10 opaque stippled rectangle, 17&#215;15 stipple pattern.</p>
<dt><code>-oddosrect100</code></p>
<dd> 100&#215;100 opaque stippled rectangle, 17&#215;15 stipple pattern.</p>
<dt><code>-oddosrect500</code></p>
<dd> 500&#215;500 opaque stippled rectangle, 17&#215;15 stipple pattern.</p>
<dt><code>-oddtilerect1</code></p>
<dd> 1&#215;1 tiled rectangle, 17&#215;15 tile pattern.</p>
<dt><code>-oddtilerect10</code></p>
<dd> 10&#215;10 tiled rectangle, 17&#215;15 tile pattern.</p>
<dt><code>-oddtilerect100</code></p>
<dd> 100&#215;100 tiled rectangle, 17&#215;15 tile pattern.</p>
<dt><code>-oddtilerect500</code></p>
<dd> 500&#215;500 tiled rectangle, 17&#215;15 tile pattern.</p>
<dt><code>-bigsrect1</code></p>
<dd> 1&#215;1 stippled rectangle, 161&#215;145 stipple pattern.</p>
<dt><code>-bigsrect10</code></p>
<dd> 10&#215;10 stippled rectangle, 161&#215;145 stipple pattern.</p>
<dt><code>-bigsrect100</code></p>
<dd> 100&#215;100 stippled rectangle, 161&#215;145 stipple pattern.</p>
<dt><code>-bigsrect500</code></p>
<dd> 500&#215;500 stippled rectangle, 161&#215;145 stipple pattern.</p>
<dt><code>-bigosrect1</code></p>
<dd> 1&#215;1 opaque stippled rectangle, 161&#215;145 stipple pattern.</p>
<dt><code>-bigosrect10</code></p>
<dd> 10&#215;10 opaque stippled rectangle, 161&#215;145 stipple pattern.</p>
<dt><code>-bigosrect100</code></p>
<dd> 100&#215;100 opaque stippled rectangle, 161&#215;145 stipple pattern.</p>
<dt><code>-bigosrect500</code></p>
<dd> 500&#215;500 opaque stippled rectangle, 161&#215;145 stipple pattern.</p>
<dt><code>-bigtilerect1</code></p>
<dd> 1&#215;1 tiled rectangle, 161&#215;145 tile pattern.</p>
<dt><code>-bigtilerect10</code></p>
<dd> 10&#215;10 tiled rectangle, 161&#215;145 tile pattern.</p>
<dt><code>-bigtilerect100</code></p>
<dd> 100&#215;100 tiled rectangle, 161&#215;145 tile pattern.</p>
<dt><code>-bigtilerect500</code></p>
<dd> 500&#215;500 tiled rectangle, 161&#215;145 tile pattern.</p>
<dt><code>-eschertilerect1</code></p>
<dd> 1&#215;1 tiled rectangle, 215&#215;208 tile pattern.</p>
<dt><code>-eschertilerect10</code></p>
<dd> 10&#215;10 tiled rectangle, 215&#215;208 tile pattern.</p>
<dt><code>-eschertilerect100</code></p>
<dd> 100&#215;100 tiled rectangle, 215&#215;208 tile pattern.</p>
<dt><code>-eschertilerect500</code></p>
<dd> 500&#215;500 tiled rectangle, 215&#215;208 tile pattern.</p>
<dt><code>-seg1</code></p>
<dd> 1-pixel thin line segment.</p>
<dt><code>-seg10</code></p>
<dd> 10-pixel thin line segment.</p>
<dt><code>-seg100</code></p>
<dd> 100-pixel thin line segment.</p>
<dt><code>-seg500</code></p>
<dd> 500-pixel thin line segment.</p>
<dt><code>-seg100c1</code></p>
<dd> 100-pixel thin line segment (1 obscuring rectangle).</p>
<dt><code>-seg100c2</code></p>
<dd> 100-pixel thin line segment (2 obscuring rectangles).</p>
<dt><code>-seg100c3</code></p>
<dd> 100-pixel thin line segment (3 obscuring rectangles).</p>
<dt><code>-dseg10</code></p>
<dd> 10-pixel thin dashed segment (3 on, 2 off).</p>
<dt><code>-dseg100</code></p>
<dd> 100-pixel thin dashed segment (3 on, 2 off).</p>
<dt><code>-ddseg100</code></p>
<dd> 100-pixel thin double-dashed segment (3 fg, 2 bg).</p>
<dt><code>-hseg10</code></p>
<dd> 10-pixel thin horizontal line segment.</p>
<dt><code>-hseg100</code></p>
<dd> 100-pixel thin horizontal line segment.</p>
<dt><code>-hseg500</code></p>
<dd> 500-pixel thin horizontal line segment.</p>
<dt><code>-vseg10</code></p>
<dd> 10-pixel thin vertical line segment.</p>
<dt><code>-vseg100</code></p>
<dd> 100-pixel thin vertical line segment.</p>
<dt><code>-vseg500</code></p>
<dd> 500-pixel thin vertical line segment.</p>
<dt><code>-whseg10</code></p>
<dd> 10-pixel wide horizontal line segment.</p>
<dt><code>-whseg100</code></p>
<dd> 100-pixel wide horizontal line segment.</p>
<dt><code>-whseg500</code></p>
<dd> 500-pixel wide horizontal line segment.</p>
<dt><code>-wvseg10</code></p>
<dd> 10-pixel wide vertical line segment.</p>
<dt><code>-wvseg100</code></p>
<dd> 100-pixel wide vertical line segment.</p>
<dt><code>-wvseg500</code></p>
<dd> 500-pixel wide vertical line segment.</p>
<dt><code>-line1</code></p>
<dd> 1-pixel thin (width 0) line.</p>
<dt><code>-line10</code></p>
<dd> 10-pixel thin line.</p>
<dt><code>-line100</code></p>
<dd> 100-pixel thin line.</p>
<dt><code>-line500</code></p>
<dd> 500-pixel thin line.</p>
<dt><code>-dline10</code></p>
<dd> 10-pixel thin dashed line (3 on, 2 off).</p>
<dt><code>-dline100</code></p>
<dd> 100-pixel thin dashed line (3 on, 2 off).</p>
<dt><code>-ddline100</code></p>
<dd> 100-pixel thin double-dashed line (3 fg, 2 bg).</p>
<dt><code>-wline10</code></p>
<dd> 10-pixel line, line width 1.</p>
<dt><code>-wline100</code></p>
<dd> 100-pixel line, line width 10.</p>
<dt><code>-wline500</code></p>
<dd> 500-pixel line, line width 50.</p>
<dt><code>-wdline100</code></p>
<dd> 100-pixel dashed line, line width 10 (30 on, 20 off).</p>
<dt><code>-wddline100</code></p>
<dd> 100-pixel double-dashed line, line width 10 (30 fg, 20 bg).</p>
<dt><code>-orect10</code></p>
<dd> 10&#215;10 thin rectangle outline.</p>
<dt><code>-orect100</code></p>
<dd> 100-pixel thin vertical line segment.</p>
<dt><code>-orect500</code></p>
<dd> 500-pixel thin vertical line segment.</p>
<dt><code>-worect10</code></p>
<dd> 10&#215;10 wide rectangle outline.</p>
<dt><code>-worect100</code></p>
<dd> 100-pixel wide vertical line segment.</p>
<dt><code>-worect500</code></p>
<dd> 500-pixel wide vertical line segment.</p>
<dt><code>-circle1</code></p>
<dd> 1-pixel diameter thin (line width 0) circle.</p>
<dt><code>-circle10</code></p>
<dd> 10-pixel diameter thin circle.</p>
<dt><code>-circle100</code></p>
<dd> 100-pixel diameter thin circle.</p>
<dt><code>-circle500</code></p>
<dd> 500-pixel diameter thin circle.</p>
<dt><code>-dcircle100</code></p>
<dd> 100-pixel diameter thin dashed circle (3 on, 2 off).</p>
<dt><code>-ddcircle100</code></p>
<dd> 100-pixel diameter thin double-dashed circle (3 fg, 2 bg).</p>
<dt><code>-wcircle10</code></p>
<dd> 10-pixel diameter circle, line width 1.</p>
<dt><code>-wcircle100</code></p>
<dd> 100-pixel diameter circle, line width 10.</p>
<dt><code>-wcircle500</code></p>
<dd> 500-pixel diameter circle, line width 50.</p>
<dt><code>-wdcircle100</code></p>
<dd> 100-pixel diameter dashed circle, line width 10 (30 on, 20 off).</p>
<dt><code>-wddcircle100</code></p>
<dd> 100-pixel diameter double-dashed circle, line width 10 (30 fg, 20 bg).</p>
<dt><code>-pcircle10</code></p>
<dd> 10-pixel diameter thin partial circle, orientation and arc angle evenly distributed.</p>
<dt><code>-pcircle100</code></p>
<dd> 100-pixel diameter thin partial circle.</p>
<dt><code>-wpcircle10</code></p>
<dd> 10-pixel diameter wide partial circle.</p>
<dt><code>-wpcircle100</code></p>
<dd> 100-pixel diameter wide partial circle.</p>
<dt><code>-fcircle1</code></p>
<dd> 1-pixel diameter filled circle.</p>
<dt><code>-fcircle10</code></p>
<dd> 10-pixel diameter filled circle.</p>
<dt><code>-fcircle100</code></p>
<dd> 100-pixel diameter filled circle.</p>
<dt><code>-fcircle500</code></p>
<dd> 500-pixel diameter filled circle.</p>
<dt><code>-fcpcircle10</code></p>
<dd> 10-pixel diameter partial filled circle, chord fill, orientation and arc angle evenly distributed.</p>
<dt><code>-fcpcircle100</code></p>
<dd> 100-pixel diameter partial filled circle, chord fill.</p>
<dt><code>-fspcircle10</code></p>
<dd> 10-pixel diameter partial filled circle, pie slice fill, orientation and arc angle evenly distributed.</p>
<dt><code>-fspcircle100</code></p>
<dd> 100-pixel diameter partial filled circle, pie slice fill.</p>
<dt><code>-ellipse10</code></p>
<dd> 10-pixel diameter thin (line width 0) ellipse, major and minor axis sizes evenly distributed.</p>
<dt><code>-ellipse100</code></p>
<dd> 100-pixel diameter thin ellipse.</p>
<dt><code>-ellipse500</code></p>
<dd> 500-pixel diameter thin ellipse.</p>
<dt><code>-dellipse100</code></p>
<dd> 100-pixel diameter thin dashed ellipse (3 on, 2 off).</p>
<dt><code>-ddellipse100</code></p>
<dd> 100-pixel diameter thin double-dashed ellipse (3 fg, 2 bg).</p>
<dt><code>-wellipse10</code></p>
<dd> 10-pixel diameter ellipse, line width 1.</p>
<dt><code>-wellipse100</code></p>
<dd> 100-pixel diameter ellipse, line width 10.</p>
<dt><code>-wellipse500</code></p>
<dd> 500-pixel diameter ellipse, line width 50.</p>
<dt><code>-wdellipse100</code></p>
<dd> 100-pixel diameter dashed ellipse, line width 10 (30 on, 20 off).</p>
<dt><code>-wddellipse100</code></p>
<dd> 100-pixel diameter double-dashed ellipse, line width 10 (30 fg, 20 bg).</p>
<dt><code>-pellipse10</code></p>
<dd> 10-pixel diameter thin partial ellipse.</p>
<dt><code>-pellipse100</code></p>
<dd> 100-pixel diameter thin partial ellipse.</p>
<dt><code>-wpellipse10</code></p>
<dd> 10-pixel diameter wide partial ellipse.</p>
<dt><code>-wpellipse100</code></p>
<dd> 100-pixel diameter wide partial ellipse.</p>
<dt><code>-fellipse10</code></p>
<dd> 10-pixel diameter filled ellipse.</p>
<dt><code>-fellipse100</code></p>
<dd> 100-pixel diameter filled ellipse.</p>
<dt><code>-fellipse500</code></p>
<dd> 500-pixel diameter filled ellipse.</p>
<dt><code>-fcpellipse10</code></p>
<dd> 10-pixel diameter partial filled ellipse, chord fill.</p>
<dt><code>-fcpellipse100</code></p>
<dd> 100-pixel diameter partial filled ellipse, chord fill.</p>
<dt><code>-fspellipse10</code></p>
<dd> 10-pixel diameter partial filled ellipse, pie slice fill.</p>
<dt><code>-fspellipse100</code></p>
<dd> 100-pixel diameter partial filled ellipse, pie slice fill.</p>
<dt><code>-triangle1</code></p>
<dd> Fill 1-pixel/side triangle.</p>
<dt><code>-triangle10</code></p>
<dd> Fill 10-pixel/side triangle.</p>
<dt><code>-triangle100</code></p>
<dd> Fill 100-pixel/side triangle.</p>
<dt><code>-trap1</code></p>
<dd> Fill 1&#215;1 trapezoid.</p>
<dt><code>-trap10</code></p>
<dd> Fill 10&#215;10 trapezoid.</p>
<dt><code>-trap100</code></p>
<dd> Fill 100&#215;100 trapezoid.</p>
<dt><code>-trap300</code></p>
<dd> Fill 300&#215;300 trapezoid.</p>
<dt><code>-strap1</code></p>
<dd> Fill 1&#215;1 transparent stippled trapezoid, 8&#215;8 stipple pattern.</p>
<dt><code>-strap10</code></p>
<dd> Fill 10&#215;10 transparent stippled trapezoid, 8&#215;8 stipple pattern.</p>
<dt><code>-strap100</code></p>
<dd> Fill 100&#215;100 transparent stippled trapezoid, 8&#215;8 stipple pattern.</p>
<dt><code>-strap300</code></p>
<dd> Fill 300&#215;300 transparent stippled trapezoid, 8&#215;8 stipple pattern.</p>
<dt><code>-ostrap1</code></p>
<dd> Fill 10&#215;10 opaque stippled trapezoid, 8&#215;8 stipple pattern.</p>
<dt><code>-ostrap10</code></p>
<dd> Fill 10&#215;10 opaque stippled trapezoid, 8&#215;8 stipple pattern.</p>
<dt><code>-ostrap100</code></p>
<dd> Fill 100&#215;100 opaque stippled trapezoid, 8&#215;8 stipple pattern.</p>
<dt><code>-ostrap300</code></p>
<dd> Fill 300&#215;300 opaque stippled trapezoid, 8&#215;8 stipple pattern.</p>
<dt><code>-tiletrap1</code></p>
<dd> Fill 10&#215;10 tiled trapezoid, 4&#215;4 tile pattern.</p>
<dt><code>-tiletrap10</code></p>
<dd> Fill 10&#215;10 tiled trapezoid, 4&#215;4 tile pattern.</p>
<dt><code>-tiletrap100</code></p>
<dd> Fill 100&#215;100 tiled trapezoid, 4&#215;4 tile pattern.</p>
<dt><code>-tiletrap300</code></p>
<dd> Fill 300&#215;300 tiled trapezoid, 4&#215;4 tile pattern.</p>
<dt><code>-oddstrap1</code></p>
<dd> Fill 1&#215;1 transparent stippled trapezoid, 17&#215;15 stipple pattern.</p>
<dt><code>-oddstrap10</code></p>
<dd> Fill 10&#215;10 transparent stippled trapezoid, 17&#215;15 stipple pattern.</p>
<dt><code>-oddstrap100</code></p>
<dd> Fill 100&#215;100 transparent stippled trapezoid, 17&#215;15 stipple pattern.</p>
<dt><code>-oddstrap300</code></p>
<dd> Fill 300&#215;300 transparent stippled trapezoid, 17&#215;15 stipple pattern.</p>
<dt><code>-oddostrap1</code></p>
<dd> Fill 10&#215;10 opaque stippled trapezoid, 17&#215;15 stipple pattern.</p>
<dt><code>-oddostrap10</code></p>
<dd> Fill 10&#215;10 opaque stippled trapezoid, 17&#215;15 stipple pattern.</p>
<dt><code>-oddostrap100</code></p>
<dd> Fill 100&#215;100 opaque stippled trapezoid, 17&#215;15 stipple pattern.</p>
<dt><code>-oddostrap300</code></p>
<dd> Fill 300&#215;300 opaque stippled trapezoid, 17&#215;15 stipple pattern.</p>
<dt><code>-oddtiletrap1</code></p>
<dd> Fill 10&#215;10 tiled trapezoid, 17&#215;15 tile pattern.</p>
<dt><code>-oddtiletrap10</code></p>
<dd> Fill 10&#215;10 tiled trapezoid, 17&#215;15 tile pattern.</p>
<dt><code>-oddtiletrap100</code></p>
<dd> Fill 100&#215;100 tiled trapezoid, 17&#215;15 tile pattern.</p>
<dt><code>-oddtiletrap300</code></p>
<dd> Fill 300&#215;300 tiled trapezoid, 17&#215;15 tile pattern.</p>
<dt><code>-bigstrap1</code></p>
<dd> Fill 1&#215;1 transparent stippled trapezoid, 161&#215;145 stipple pattern.</p>
<dt><code>-bigstrap10</code></p>
<dd> Fill 10&#215;10 transparent stippled trapezoid, 161&#215;145 stipple pattern.</p>
<dt><code>-bigstrap100</code></p>
<dd> Fill 100&#215;100 transparent stippled trapezoid, 161&#215;145 stipple pattern.</p>
<dt><code>-bigstrap300</code></p>
<dd> Fill 300&#215;300 transparent stippled trapezoid, 161&#215;145 stipple pattern.</p>
<dt><code>-bigostrap1</code></p>
<dd> Fill 10&#215;10 opaque stippled trapezoid, 161&#215;145 stipple pattern.</p>
<dt><code>-bigostrap10</code></p>
<dd> Fill 10&#215;10 opaque stippled trapezoid, 161&#215;145 stipple pattern.</p>
<dt><code>-bigostrap100</code></p>
<dd> Fill 100&#215;100 opaque stippled trapezoid, 161&#215;145 stipple pattern.</p>
<dt><code>-bigostrap300</code></p>
<dd> Fill 300&#215;300 opaque stippled trapezoid, 161&#215;145 stipple pattern.</p>
<dt><code>-bigtiletrap1</code></p>
<dd> Fill 10&#215;10 tiled trapezoid, 161&#215;145 tile pattern.</p>
<dt><code>-bigtiletrap10</code></p>
<dd> Fill 10&#215;10 tiled trapezoid, 161&#215;145 tile pattern.</p>
<dt><code>-bigtiletrap100</code></p>
<dd> Fill 100&#215;100 tiled trapezoid, 161&#215;145 tile pattern.</p>
<dt><code>-bigtiletrap300</code></p>
<dd> Fill 300&#215;300 tiled trapezoid, 161&#215;145 tile pattern.</p>
<dt><code>-eschertiletrap1</code></p>
<dd> Fill 1&#215;1 tiled trapezoid, 216&#215;208 tile pattern.</p>
<dt><code>-eschertiletrap10</code></p>
<dd> Fill 10&#215;10 tiled trapezoid, 216&#215;208 tile pattern.</p>
<dt><code>-eschertiletrap100</code></p>
<dd> Fill 100&#215;100 tiled trapezoid, 216&#215;208 tile pattern.</p>
<dt><code>-eschertiletrap300</code></p>
<dd> Fill 300&#215;300 tiled trapezoid, 216&#215;208 tile pattern.</p>
<dt><code>-complex10</code></p>
<dd> Fill 10-pixel/side complex polygon.</p>
<dt><code>-complex100</code></p>
<dd> Fill 100-pixel/side complex polygon.</p>
<dt><code>-64poly10convex</code></p>
<dd> Fill 10&#215;10 convex 64-gon.</p>
<dt><code>-64poly100convex</code></p>
<dd> Fill 100&#215;100 convex 64-gon.</p>
<dt><code>-64poly10complex</code></p>
<dd> Fill 10&#215;10 complex 64-gon.</p>
<dt><code>-64poly100complex</code></p>
<dd> Fill 100&#215;100 complex 64-gon.</p>
<dt><code>-ftext</code></p>
<dd> Character in 80-char line (6&#215;13).</p>
<dt><code>-f8text</code></p>
<dd> Character in 70-char line (8&#215;13).</p>
<dt><code>-f9text</code></p>
<dd> Character in 60-char line (9&#215;15).</p>
<dt><code>-f14text16</code></p>
<dd> 2-byte character in 40-char line (k14).</p>
<dt><code>-tr10text</code></p>
<dd> Character in 80-char line (Times-Roman 10).</p>
<dt><code>-tr24text</code></p>
<dd> Character in 30-char line (Times-Roman 24).</p>
<dt><code>-polytext</code></p>
<dd> Character in 20/40/20 line (6&#215;13, Times-Roman 10, 6&#215;13).</p>
<dt><code>-polytext16</code></p>
<dd> 2-byte character in 7/14/7 line (k14, k24).</p>
<dt><code>-fitext</code></p>
<dd> Character in 80-char image line (6&#215;13).</p>
<dt><code>-f8itext</code></p>
<dd> Character in 70-char image line (8&#215;13).</p>
<dt><code>-f9itext</code></p>
<dd> Character in 60-char image line (9&#215;15).</p>
<dt><code>-f14itext16</code></p>
<dd> 2-byte character in 40-char image line (k14).</p>
<dt><code>-f24itext16</code></p>
<dd> 2-byte character in 23-char image line (k24).</p>
<dt><code>-tr10itext</code></p>
<dd> Character in 80-char image line (Times-Roman 10).</p>
<dt><code>-tr24itext</code></p>
<dd> Character in 30-char image line (Times-Roman 24).</p>
<dt><code>-scroll10</code></p>
<dd> Scroll 10&#215;10 pixels vertically.</p>
<dt><code>-scroll100</code></p>
<dd> Scroll 100&#215;100 pixels vertically.</p>
<dt><code>-scroll500</code></p>
<dd> Scroll 500&#215;500 pixels vertically.</p>
<dt><code>-copywinwin10</code></p>
<dd> Copy 10&#215;10 square from window to window.</p>
<dt><code>-copywinwin100</code></p>
<dd> Copy 100&#215;100 square from window to window.</p>
<dt><code>-copywinwin500</code></p>
<dd> Copy 500&#215;500 square from window to window.</p>
<dt><code>-copypixwin10</code></p>
<dd> Copy 10&#215;10 square from pixmap to window.</p>
<dt><code>-copypixwin100</code></p>
<dd> Copy 100&#215;100 square from pixmap to window.</p>
<dt><code>-copypixwin500</code></p>
<dd> Copy 500&#215;500 square from pixmap to window.</p>
<dt><code>-copywinpix10</code></p>
<dd> Copy 10&#215;10 square from window to pixmap.</p>
<dt><code>-copywinpix100</code></p>
<dd> Copy 100&#215;100 square from window to pixmap.</p>
<dt><code>-copywinpix500</code></p>
<dd> Copy 500&#215;500 square from window to pixmap.</p>
<dt><code>-copypixpix10</code></p>
<dd> Copy 10&#215;10 square from pixmap to pixmap.</p>
<dt><code>-copypixpix100</code></p>
<dd> Copy 100&#215;100 square from pixmap to pixmap.</p>
<dt><code>-copypixpix500</code></p>
<dd> Copy 500&#215;500 square from pixmap to pixmap.</p>
<dt><code>-copyplane10</code></p>
<dd> Copy 10&#215;10 1-bit deep plane.</p>
<dt><code>-copyplane100</code></p>
<dd> Copy 100&#215;100 1-bit deep plane.</p>
<dt><code>-copyplane500</code></p>
<dd> Copy 500&#215;500 1-bit deep plane.</p>
<dt><code>-putimage10</code></p>
<dd> PutImage 10&#215;10 square.</p>
<dt><code>-putimage100</code></p>
<dd> PutImage 100&#215;100 square.</p>
<dt><code>-putimage500</code></p>
<dd> PutImage 500&#215;500 square.</p>
<dt><code>-putimagexy10</code></p>
<dd> PutImage XY format 10&#215;10 square.</p>
<dt><code>-putimagexy100</code></p>
<dd> PutImage XY format 100&#215;100 square.</p>
<dt><code>-putimagexy500</code></p>
<dd> PutImage XY format 500&#215;500 square.</p>
<dt><code>-shmput10</code></p>
<dd> PutImage 10&#215;10 square, MIT shared memory extension.</p>
<dt><code>-shmput100</code></p>
<dd> PutImage 100&#215;100 square, MIT shared memory extension.</p>
<dt><code>-shmput500</code></p>
<dd> PutImage 500&#215;500 square, MIT shared memory extension.</p>
<dt><code>-shmputxy10</code></p>
<dd> PutImage XY format 10&#215;10 square, MIT shared memory extension.</p>
<dt><code>-shmputxy100</code></p>
<dd> PutImage XY format 100&#215;100 square, MIT shared memory extension.</p>
<dt><code>-shmputxy500</code></p>
<dd> PutImage XY format 500&#215;500 square, MIT shared memory extension.</p>
<dt><code>-getimage10</code></p>
<dd> GetImage 10&#215;10 square.</p>
<dt><code>-getimage100</code></p>
<dd> GetImage 100&#215;100 square.</p>
<dt><code>-getimage500</code></p>
<dd> GetImage 500&#215;500 square.</p>
<dt><code>-getimagexy10</code></p>
<dd> GetImage XY format 10&#215;10 square.</p>
<dt><code>-getimagexy100</code></p>
<dd> GetImage XY format 100&#215;100 square.</p>
<dt><code>-getimagexy500</code></p>
<dd> GetImage XY format 500&#215;500 square.</p>
<dt><code>-compwinwin10</code></p>
<dd> Composite 10&#215;10 from window to window.</p>
<dt><code>-compwinwin100</code></p>
<dd> Composite 100&#215;100 from window to window.</p>
<dt><code>-compwinwin500</code></p>
<dd> Composite 500&#215;500 from window to window.</p>
<dt><code>-comppixwin10</code></p>
<dd> Composite 10&#215;10 from pixmap to window.</p>
<dt><code>-comppixwin100</code></p>
<dd> Composite 100&#215;100 from pixmap to window.</p>
<dt><code>-comppixwin500</code></p>
<dd> Composite 500&#215;500 from pixmap to window.</p>
<dt><code>-magpixwin10</code></p>
<dd> Scale 5&#215;5 from pixmap to 10&#215;10 window.</p>
<dt><code>-magpixwin100</code></p>
<dd> Scale 50&#215;50 from pixmap to 100&#215;100 window.</p>
<dt><code>-magpixwin500</code></p>
<dd> Scale 250&#215;250 from pixmap to 500&#215;500 window.</p>
<dt><code>-minpixwin10</code></p>
<dd> Scale 10&#215;10 from pixmap to 5&#215;5 window.</p>
<dt><code>-minpixwin100</code></p>
<dd> Scale 100&#215;100 from pixmap to 50&#215;50 window.</p>
<dt><code>-minpixwin500</code></p>
<dd> Scale 500&#215;500 from pixmap to 250&#215;250 window.</p>
<dt><code>-noop</code></p>
<dd> X protocol NoOperation.</p>
<dt><code>-atom</code></p>
<dd> GetAtomName.</p>
<dt><code>-pointer</code></p>
<dd> QueryPointer.</p>
<dt><code>-prop</code></p>
<dd> GetProperty.</p>
<dt><code>-gc</code></p>
<dd> Change graphics context.</p>
<dt><code>-create</code></p>
<dd> Create child window and map using MapSubwindows.</p>
<dt><code>-ucreate</code></p>
<dd> Create unmapped window.</p>
<dt><code>-map</code></p>
<dd> Map child window via MapWindow on parent.</p>
<dt><code>-unmap</code></p>
<dd> Unmap child window via UnmapWindow on parent.</p>
<dt><code>-destroy</code></p>
<dd> Destroy child window via DestroyWindow parent.</p>
<dt><code>-popup</code></p>
<dd> Hide/expose window via Map/Unmap popup window.</p>
<dt><code>-move</code></p>
<dd> Move window.</p>
<dt><code>-umove</code></p>
<dd> Moved unmapped window.</p>
<dt><code>-movetree</code></p>
<dd> Move window via MoveWindow on parent.</p>
<dt><code>-resize</code></p>
<dd> Resize window.</p>
<dt><code>-uresize</code></p>
<dd> Resize unmapped window.</p>
<dt><code>-circulate</code></p>
<dd> Circulate lowest window to top.</p>
<dt><code>-ucirculate</code></p>
<dd> Circulate unmapped window to top.</dl>
<h2>X DEFAULTS</h2>
<p> There are no X defaults used by this program.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-x11perfcomp/">x11perfcomp</a>(1)</p>
<h2>AUTHORS</h2>
<p> Joel McCormack<br />
 Phil Karlton<br />
 Susan Angebranndt<br />
 Chris Kent<br />
 Keith Packard<br />
 Graeme Gill </p>
<h2>Index</h2>
