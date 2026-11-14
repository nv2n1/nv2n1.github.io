---
title: "set_close_button_callback(3)"
name: "set_close_button_callback"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_close_button_callback/"
description: "set_close_button_callback – Handles the user clicking on the close button of the window. Allegro game programming library."
---

<p>set_close_button_callback &#8211; Handles the user clicking on the close button of the window. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int set_close_button_callback(void (*proc)(void));</code></pre>
<h2>Description</h2>
<p>On platforms that have a close button, this routine installs a callback function to handle the close event. In other words, when the user clicks the close button on your program&#8217;s window or any equivalent device, the function you specify here will be called. This function should not generally attempt to exit the program or save any data itself. The function could be called at any time, and there is usually a risk of conflict with the main thread of the program. Instead, you should set a flag during this function, and test it on a regular basis in the main loop of the program. Pass NULL as the `proc&#8217; argument to this function to disable the close button functionality, which is the default state. Note that Allegro cannot intercept the close button of a DOS box in Windows. Also note that the supplied callback is also called under MacOS X when the user hits Command-Q or selects &quot;Quit&quot; from the application menu. Example: </p>
<pre><code>volatile int close_button_pressed = FALSE;

void close_button_handler(void)
{
    close_button_pressed = TRUE;
}
END_OF_FUNCTION(close_button_handler)
...

    allegro_init();
LOCK_FUNCTION(close_button_handler);
set_close_button_callback(close_button_handler);
...

    while (!close_button_pressed)
        do_stuff();</code></pre>
<h2>Return Value</h2>
<p>Returns zero on success and non-zero on failure (e.g. the feature is not supported by the platform). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_window_title/">set_window_title</a></code>(3) </p>
